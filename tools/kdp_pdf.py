"""Create and validate the approved noninteractive PDF 1.3 KDP interior.

The reading PDF must be made from the original typeset manuscript, never this
export: Ghostscript rewrites font encodings and flattens transparent pages.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

import numpy as np
import pymupdf
from PIL import Image, ImageFilter
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, IndirectObject, NameObject, StreamObject

from check_cover_pdf import check_interior
from print_layout import LAYOUT

SCHEMA = 1
RESOLUTION = 600
CATALOG_REMOVE = ('/OpenAction', '/PageMode', '/PageLabels', '/Names', '/Outlines',
                  '/Metadata', '/AcroForm', '/OCProperties', '/AA')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def objects(reader):
    seen_refs, seen_direct = set(), set()

    def walk(obj):
        if isinstance(obj, IndirectObject):
            key = (obj.idnum, obj.generation)
            if key in seen_refs:
                return
            seen_refs.add(key)
            obj = obj.get_object()
        if not isinstance(obj, (dict, list)) or id(obj) in seen_direct:
            return
        seen_direct.add(id(obj))
        yield obj
        for child in (obj.values() if isinstance(obj, dict) else obj):
            yield from walk(child)

    for generation, entries in reader.xref.items():
        for number in entries:
            if number:
                yield from walk(IndirectObject(number, generation, reader))
    for number in reader.xref_objStm:
        yield from walk(IndirectObject(number, 0, reader))


def group_transparent(container):
    return container.get('/Group', DictionaryObject()).get_object().get('/S') == '/Transparency'


def transparent(state):
    return (any(float(state.get(key, 1)) < 1 for key in ('/ca', '/CA'))
            or state.get('/SMask') not in (None, '/None')
            or state.get('/BM', '/Normal') not in ('/Normal', '/Compatible'))


def repair_hex(stream):
    filters = stream.get('/Filter', [])
    if not isinstance(filters, list):
        filters = [filters]
    if filters and filters[0] == '/ASCIIHexDecode' and not stream._data.rstrip().endswith(b'>'):
        stream._data += b'>'
        return 1
    return 0


def prepare(source, output):
    """Remove interactive material, repair mesh streams and prune unused alpha.

    Unused global PGF opacity resources otherwise make Ghostscript rasterize
    almost every page, including pages that never use transparency.
    """
    reader = PdfReader(source, strict=True)
    writer = PdfWriter(clone_from=reader)
    for key in CATALOG_REMOVE:
        writer.root_object.pop(key, None)
    writer.metadata = None
    repaired = sum(repair_hex(obj) for obj in writer._objects if isinstance(obj, StreamObject))
    removed = 0

    def prune(container, contents, ancestry=()):
        nonlocal removed
        resources = DictionaryObject(container.get('/Resources', DictionaryObject()).get_object())
        operations = contents.operations if contents is not None else []
        states = resources.get('/ExtGState', DictionaryObject()).get_object()
        used = {args[0] for args, op in operations if op == b'gs'}
        kept = DictionaryObject({key: ref for key, ref in states.items() if key in used})
        removed += len(states) - len(kept)
        if kept:
            resources[NameObject('/ExtGState')] = kept
        else:
            resources.pop('/ExtGState', None)
        has_alpha = any(transparent(ref.get_object()) for ref in kept.values())
        xobjects = resources.get('/XObject', DictionaryObject()).get_object()
        used_forms = {args[0] for args, op in operations if op == b'Do'}
        kept_objects = DictionaryObject({key: ref for key, ref in xobjects.items() if key in used_forms})
        if kept_objects:
            resources[NameObject('/XObject')] = kept_objects
        else:
            resources.pop('/XObject', None)
        for ref in kept_objects.values():
            obj = ref.get_object()
            if obj.get('/SMask') not in (None, '/None'):
                has_alpha = True
            if obj.get('/Subtype') == '/Form' and id(obj) not in ancestry:
                from pypdf.generic import ContentStream
                if obj.get('/Resources'):
                    has_alpha |= prune(obj, ContentStream(obj, writer), ancestry + (id(obj),))
                has_alpha |= group_transparent(obj)
        has_alpha |= group_transparent(container)
        container[NameObject('/Resources')] = resources
        return has_alpha

    alpha_pages = []
    for index, page in enumerate(writer.pages):
        page.pop('/Annots', None)
        page.pop('/AA', None)
        if prune(page, page.get_contents()):
            alpha_pages.append(index + 1)
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    writer.write(output)
    return {'repaired_hex_streams': repaired, 'unused_graphics_states_pruned': removed,
            'transparency_pages': alpha_pages}


def body_digest(reader, offset=0):
    digest = hashlib.sha256()
    for page in reader.pages[offset:]:
        stream = page.get_contents()
        data = stream.get_data() if stream is not None else b''
        digest.update(len(data).to_bytes(8, 'big') + data)
    return digest.hexdigest()


def navigation(reader):
    return {'labels': reader.page_labels,
            'destinations': {name: reader.get_destination_page_number(target)
                             for name, target in reader.named_destinations.items()},
            'annotations': [len(page.get('/Annots', []).get_object()) if page.get('/Annots') else 0
                            for page in reader.pages]}


def compare_pages(source, output, offset=0, ignore_rectangles=None):
    """Check visible content with two-sided ink coverage and colour comparison.

    A one-pixel allowance at 72 dpi accommodates the different font antialiasing
    of the two renderers. Raster pages require 600 dpi separately in preflight.
    """
    flattened, worst_mean, worst_ink = [], 0.0, 0.0
    with pymupdf.open(source) as original, pymupdf.open(output) as printed:
        if len(original) - offset != len(printed):
            raise ValueError('PDF pair page counts disagree')
        for index, page in enumerate(printed):
            before = original[index + offset]
            if before.rect != page.rect or before.rotation != page.rotation:
                raise ValueError(f'PDF body differs in geometry on page {index + 1}')
            a, b = before.get_pixmap(alpha=False), page.get_pixmap(alpha=False)
            aa = np.frombuffer(a.samples, dtype=np.uint8).reshape(a.height, a.width, 3).astype(np.int16)
            bb = np.frombuffer(b.samples, dtype=np.uint8).reshape(b.height, b.width, 3).astype(np.int16)
            is_flat = bool(before.get_text().strip()) and not page.get_text().strip()
            if is_flat:
                flattened.append(index + 1)
            valid = np.ones(aa.shape[:2], dtype=bool)
            for rectangle in (ignore_rectangles or {}).get(index, []):
                rect = pymupdf.Rect(rectangle).irect
                valid[max(0, rect.y0 - 2):rect.y1 + 2, max(0, rect.x0 - 2):rect.x1 + 2] = False
            mean = float(np.abs(aa - bb)[valid].mean())
            masks = [(pixels.mean(axis=2) < 160) & (np.ptp(pixels, axis=2) < 40)
                     & valid for pixels in (aa, bb)]
            expanded = [np.asarray(Image.fromarray((mask * 255).astype(np.uint8))
                                   .filter(ImageFilter.MaxFilter(3))) > 0 for mask in masks]
            missing = float((masks[0] & ~expanded[1]).sum() / max(1, masks[0].sum()))
            added = float((masks[1] & ~expanded[0]).sum() / max(1, masks[1].sum()))
            if mean > (8 if is_flat else 1) or max(missing, added) > .03:
                raise ValueError(f'PDF body differs visually on page {index + 1}: '
                                 f'mean={mean:.3f}, missing ink={missing:.4f}, added ink={added:.4f}')
            worst_mean, worst_ink = max(worst_mean, mean), max(worst_ink, missing, added)
    return {'compared_pages': index + 1, 'flattened_pages': flattened,
            'maximum_mean_pixel_difference': round(worst_mean, 5),
            'maximum_unmatched_ink_fraction': round(worst_ink, 5)}


def check(path, report=None):
    """Reject regression to the raw TeX PDF, live alpha, low DPI or interactions."""
    path = Path(path)
    reader = PdfReader(path, strict=True)
    if reader.is_encrypted or reader.pdf_header != '%PDF-1.3':
        raise ValueError(f'{path}: KDP interior must be unencrypted PDF 1.3')
    if reader.metadata or any(key in reader.trailer['/Root'] for key in CATALOG_REMOVE):
        raise ValueError(f'{path}: KDP interior contains document metadata or navigation')
    for page in reader.pages:
        if any(key in page for key in ('/Annots', '/AA')):
            raise ValueError(f'{path}: KDP interior contains annotations or actions')
        if page.rotation != 0 or tuple(page.cropbox) != tuple(page.mediabox):
            raise ValueError(f'{path}: KDP interior has a rotated or cropped page')
    for obj in objects(reader):
        if not hasattr(obj, 'get'):
            continue
        if transparent(obj) or group_transparent(obj):
            raise ValueError(f'{path}: KDP interior contains live transparency')
        if '/ASCIIHexDecode' in str(obj.get('/Filter', '')):
            raise ValueError(f'{path}: KDP interior contains unnormalised ASCIIHex streams')
        if obj.get('/S') in ('/JavaScript', '/Launch') or obj.get('/Type') == '/Annot':
            raise ValueError(f'{path}: KDP interior contains interactive objects')
    pages = check_interior(path)
    if not 24 <= pages <= 828 or path.stat().st_size > 650_000_000:
        raise ValueError(f'{path}: KDP premium-colour page/file-size limits exceeded')
    table = subprocess.check_output(['pdfimages', '-list', str(path)], text=True)
    for line in table.splitlines()[2:]:
        fields = line.split()
        if len(fields) >= 16 and fields[0].isdigit() and min(float(fields[12]), float(fields[13])) < 299.5:
            raise ValueError(f'{path}: KDP interior image below 300 ppi: {line.strip()}')
    if report is not None:
        data = json.loads(Path(report).read_text())
        if data.get('schema') != SCHEMA or data.get('print_sha256') != sha(path) or data.get('pages') != pages:
            raise ValueError(f'{path}: KDP preflight report does not match the PDF')
    return pages


def check_reading(download, report):
    """Verify that the reading file retains its original body and navigation."""
    reader = PdfReader(download)
    data = json.loads(Path(report).read_text())
    if body_digest(reader, 1) != data['source_body_sha256']:
        raise ValueError('Download body differs from the typeset manuscript')
    expected, actual = data['source_navigation'], navigation(reader)
    if (actual['labels'][1:] != expected['labels'] or actual['annotations'][1:] != expected['annotations']
            or any(actual['destinations'].get(name) != page + 1
                   for name, page in expected['destinations'].items())):
        raise ValueError('Download changed the original navigation')


def export(source, output, report):
    source, output, report = map(Path, (source, output, report))
    if len({source.resolve(), output.resolve(), report.resolve()}) != 3:
        raise ValueError('KDP output and report must be separate from the typeset source')
    output.parent.mkdir(parents=True, exist_ok=True)
    original = PdfReader(source)
    with tempfile.TemporaryDirectory(prefix='kdp-', dir=output.parent) as directory:
        directory = Path(directory)
        repairs = prepare(source, directory / 'clean.pdf')
        result = subprocess.run([
            'gs', '-q', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.3', f'-r{RESOLUTION}', '-dEmbedAllFonts=true', '-dSubsetFonts=true',
            '-dDownsampleColorImages=false', '-dDownsampleGrayImages=false', '-dDownsampleMonoImages=false',
            '-dAutoRotatePages=/None', '-dPreserveAnnots=false', '-sColorConversionStrategy=LeaveColorUnchanged',
            '-sOutputFile=' + str(directory / 'press.pdf'), str(directory / 'clean.pdf')],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=1200)
        if result.returncode or result.stdout.strip():
            raise ValueError('KDP PDF export failed or reported a repair: ' + result.stdout[-3000:])
        writer = PdfWriter(clone_from=PdfReader(directory / 'press.pdf', strict=True))
        writer.metadata = None
        for key in CATALOG_REMOVE:
            writer.root_object.pop(key, None)
        writer.pdf_header = '%PDF-1.3'
        candidate = directory / 'final.pdf'
        writer.write(candidate)
        check(candidate)
        comparison = compare_pages(source, candidate)
        if set(comparison['flattened_pages']) - set(repairs['transparency_pages']):
            raise ValueError('KDP export rasterized pages without live transparency')
        data = {'schema': SCHEMA, 'pages': len(original.pages), 'pdf_version': '1.3',
                'flattening_ppi': RESOLUTION, 'source_sha256': sha(source),
                'source_body_sha256': body_digest(original), 'source_navigation': navigation(original),
                'print_sha256': sha(candidate), **repairs, **comparison}
        candidate.replace(output)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(data, indent=2) + '\n')
    print(f'KDP interior checked: {data["pages"]} pages, PDF 1.3, no interactions/live transparency; '
          f'{len(comparison["flattened_pages"])} pages flattened at {RESOLUTION} ppi')
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path, nargs='?')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    if args.output:
        export(args.source, args.output, args.report)
    else:
        print(f'KDP preflight passed: {check(args.source, args.report)} pages')
