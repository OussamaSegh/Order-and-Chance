"""Match the approved cover's opaque PDF 1.5 export, retaining vector lettering.

Only transparent illustration regions are composited at 600 ppi. Full-cover
rasterization and changes to the artwork/template are forbidden.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import tempfile

import pymupdf
from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, DecodedStreamObject, DictionaryObject, FloatObject, NameObject, StreamObject

from check_print_cover import check as check_cover, pixel_key
from kdp_pdf import CATALOG_REMOVE, RESOLUTION, compare_pages, prepare, sha, objects, transparent, group_transparent
from series_cover import ROOT


def flatten_art(source, output, directory):
    """Composite the illustration only; do not touch text, frames or barcodes."""
    patches = []
    with pymupdf.open(source) as doc:
        page = doc[0]
        bounds = None
        for drawing in page.get_drawings():
            live = ((drawing.get('fill') is not None and 0 < drawing.get('fill_opacity', 1) < 1)
                    or (drawing.get('color') is not None and 0 < drawing.get('stroke_opacity', 1) < 1))
            if live:
                margin = (drawing.get('width') or 0) / 2 + 2
                rect = drawing['rect'] + (-margin, -margin, margin, margin)
                bounds = rect if bounds is None else bounds | rect
        if bounds is not None:
            bounds &= page.rect
            scale = RESOLUTION / 72
            bounds = pymupdf.Rect(math.floor(bounds.x0 * scale) / scale,
                                 math.floor(bounds.y0 * scale) / scale,
                                 math.ceil(bounds.x1 * scale) / scale,
                                 math.ceil(bounds.y1 * scale) / scale)
            if bounds.get_area() > page.rect.get_area() * .35:
                raise ValueError('Cover transparency extends beyond the illustration; do not rasterize the whole cover')
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines', []):
                    for span in line['spans']:
                        if span['text'].strip() and pymupdf.Rect(span['bbox']).intersects(bounds):
                            raise ValueError('Transparent cover art overlaps lettering; keep typography vector')
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=bounds, alpha=False)
            image = Path(directory) / 'art.png'
            pixmap.save(image)
            size, pixel_hash = pixel_key(Image.open(image))
            patches.append({'size': list(size), 'pixel_sha256': pixel_hash,
                            'bounds_pt': list(bounds), 'ppi': RESOLUTION})
            page.add_redact_annot(bounds, fill=None)
            page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                                  graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
                                  text=pymupdf.PDF_REDACT_TEXT_NONE)
            page.insert_image(bounds, filename=image, keep_proportion=False, overlay=True)
        doc.save(output, garbage=4, deflate=True)
    return patches


def check_opaque(path):
    reader = PdfReader(path, strict=True)
    if reader.pdf_header != '%PDF-1.5' or reader.is_encrypted or reader.metadata:
        raise ValueError('Print cover must match the approved unencrypted, metadata-free PDF 1.5 export')
    if len(reader.pages) != 1 or any(key in reader.trailer['/Root'] for key in CATALOG_REMOVE):
        raise ValueError('Print cover contains unexpected pages or document navigation')
    if '/Annots' in reader.pages[0] or '/AA' in reader.pages[0]:
        raise ValueError('Print cover contains annotations or page actions')
    for obj in objects(reader):
        if hasattr(obj, 'get') and (transparent(obj) or group_transparent(obj)
                                    or '/ASCIIHexDecode' in str(obj.get('/Filter', ''))):
            raise ValueError('Print cover contains live transparency or unnormalised graphics')


def remove_empty_opacity(source, output):
    # MuPDF removes/redacts the art paths but can retain their stroke states,
    # including zero-opacity suppressed paths underneath the opaque composite.
    # Do this only after proving there is no visible transparent drawing/text.
    with pymupdf.open(source) as doc:
        for drawing in doc[0].get_drawings():
            if ((drawing.get('color') is not None and 0 < drawing.get('stroke_opacity', 1) < 1)
                    or (drawing.get('fill') is not None and 0 < drawing.get('fill_opacity', 1) < 1)):
                raise ValueError('Unflattened visible cover artwork remains')
    reader = PdfReader(source)
    # The shared identity has an invisible searchable duplicate of its traced
    # masthead/author. Remove its text-show operators rather than making it
    # visible when clearing zero-opacity graphics states.
    def strip_hidden(container, contents):
        resources = container.get('/Resources', DictionaryObject()).get_object()
        states = resources.get('/ExtGState', DictionaryObject()).get_object()
        state, stack, kept = {'/ca': 1, '/CA': 1, 'Tr': 0}, [], []
        for args, op in contents.operations:
            if op == b'q':
                stack.append(state.copy())
            elif op == b'Q':
                state = stack.pop()
            elif op == b'gs':
                applied = states[args[0]].get_object()
                state.update({key: float(applied[key]) for key in ('/ca', '/CA') if key in applied})
            elif op == b'Tr':
                state['Tr'] = int(args[0])
            if op in (b'Tj', b'TJ'):
                mode = state['Tr']
                visible = ((mode in (0, 2, 4, 6) and state['/ca'] > 0)
                           or (mode in (1, 2, 5, 6) and state['/CA'] > 0))
                if not visible:
                    continue
                if state['/ca'] < 1 and mode in (0, 2, 4, 6):
                    raise ValueError('Visible transparent cover lettering is unsupported')
            kept.append((args, op))
        contents.operations = kept
        return contents.get_data()

    for page in reader.pages:
        stream = DecodedStreamObject()
        stream.set_data(strip_hidden(page, page.get_contents()))
        page[NameObject('/Contents')] = stream
        # PdfReader's flattened PageObject can wrap the original page-tree
        # dictionary. Update that dictionary too before cloning the catalog.
        if page.indirect_reference is not None:
            page.indirect_reference.get_object()[NameObject('/Contents')] = stream
    for obj in list(objects(reader)):
        if isinstance(obj, StreamObject) and obj.get('/Subtype') == '/Form' and obj.get('/Resources'):
            data = strip_hidden(obj, ContentStream(obj, reader))
            obj._data = data
            obj.pop('/Filter', None)
            obj.pop('/DecodeParms', None)
    for obj in list(objects(reader)):
        if not isinstance(obj, dict):
            continue
        if obj.get('/SMask') not in (None, '/None'):
            raise ValueError('Unexpected image transparency outside the cover illustration')
        if '/ca' in obj:
            obj[NameObject('/ca')] = FloatObject(1)
        if '/CA' in obj:
            obj[NameObject('/CA')] = FloatObject(1)
        if group_transparent(obj):
            obj.pop('/Group')
    writer = PdfWriter(clone_from=reader)
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    writer.write(output)


def export(source, output, number, report):
    source, output, report = map(Path, (source, output, report))
    if len({source.resolve(), output.resolve(), report.resolve()}) != 3:
        raise ValueError('Cover export must be separate from the approved vector source')
    # The original shared-template, vector-art and paper provenance gates run
    # before compositing; an arbitrary raster front cannot enter this path.
    original_preflight = check_cover(source, number)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='cover-', dir=output.parent) as directory:
        directory = Path(directory)
        patches = flatten_art(source, directory / 'composited.pdf', directory)
        prepare(directory / 'composited.pdf', directory / 'clean.pdf')
        remove_empty_opacity(directory / 'clean.pdf', directory / 'opaque.pdf')
        # Keep the original font programs and Unicode maps. Unlike interiors,
        # the now-opaque cover needs no Ghostscript transparency conversion.
        writer = PdfWriter(clone_from=PdfReader(directory / 'opaque.pdf', strict=True))
        writer.metadata = None
        for key in CATALOG_REMOVE:
            writer.root_object.pop(key, None)
        writer.pdf_header = '%PDF-1.5'
        candidate = directory / 'final.pdf'
        writer.write(candidate)
        check_opaque(candidate)
        comparison = compare_pages(source, candidate)
        if comparison['flattened_pages']:
            raise ValueError('The cover lettering was rasterized; preserve vector typography')
        data = {'schema': 2, 'volume': str(number), 'press_export': True,
                'source_sha256': sha(source), 'print_sha256': sha(candidate),
                'series_manifest_sha256': sha(ROOT / 'tools/assets/series/manifest.json'),
                'source_preflight': original_preflight, 'illustration_patches': patches,
                'pdf_version': '1.5', 'embedded_fonts': True, 'vector_lettering': True,
                'live_transparency': False, **comparison}
        candidate.replace(output)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(data, indent=2) + '\n')
    check_cover(output, number, press_report=report)
    print(f'KDP cover checked: approved artwork, vector lettering, {len(patches)} opaque art patch(es) at {RESOLUTION} ppi')
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--number', required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    export(args.source, args.output, args.number, args.report)
