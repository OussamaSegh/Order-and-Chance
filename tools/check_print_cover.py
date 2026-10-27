"""Print preflight: vector artwork, embedded fonts and genuine >=300 ppi grain.

The only permitted raster content is the native paper texture. A resized approved
cover bitmap is rejected even if its DPI tag says 300. Physical DPI comes from the
PDF placement matrix, as reported by poppler, not PNG metadata.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess

from PIL import Image
from pypdf import PdfReader

from check_cover_pdf import check_fonts

ROOT = Path(__file__).resolve().parent.parent
PRINT = ROOT / 'tools/assets/print'
MINIMUM_PPI = 300


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def raster_placements(table):
    result = []
    for line in table.splitlines():
        fields = line.split()
        if len(fields) < 2 or not fields[0].isdigit() or not fields[1].isdigit():
            continue
        if len(fields) < 16:
            raise ValueError('Could not verify a print raster placement')
        result.append({'page': int(fields[0]), 'index': int(fields[1]),
                       'type': fields[2], 'width': int(fields[3]), 'height': int(fields[4]),
                       'object_id': fields[10],
                       'x_ppi': float(fields[12]), 'y_ppi': float(fields[13])})
    return result


def check_placements(placements, minimum=MINIMUM_PPI):
    for item in placements:
        if item.get('type', 'image') != 'image' or not str(item.get('object_id', '0')).isdigit():
            raise ValueError('Only opaque paper-grain image resources are permitted in print')
        if min(item['x_ppi'], item['y_ppi']) < minimum:
            raise ValueError(f"Print image {item['index']} is only "
                             f"{item['x_ppi']:g} x {item['y_ppi']:g} ppi; need {minimum}")


def pixel_key(image):
    image = image.convert('RGB')
    return image.size, hashlib.sha256(image.tobytes()).hexdigest()


def check_paper(image, allowed):
    if pixel_key(image) not in allowed:
        raise ValueError('Print cover contains a bitmap other than native paper grain; '
                         'approved artwork and lettering must use the vector masters')


def resource_images(resources, seen=None):
    """Walk shared PDF resources once, without parsing millions of vector segments."""
    seen = set() if seen is None else seen
    resources = resources.get_object()
    xobjects = resources.get('/XObject')
    if not xobjects:
        return
    for ref in xobjects.get_object().values():
        obj = ref.get_object()
        if id(obj) in seen:
            continue
        seen.add(id(obj))
        if obj.get('/Subtype') == '/Image':
            yield obj
        elif obj.get('/Subtype') == '/Form' and obj.get('/Resources'):
            yield from resource_images(obj['/Resources'], seen)


def check_masters(number):
    manifest = json.loads((PRINT / 'manifest.json').read_text())
    numbers = {'0', str(number)} & manifest['masters'].keys()
    for value in numbers:
        spec = manifest['masters'][value]
        if sha(ROOT / spec['source']) != spec['source_sha256']:
            raise ValueError(f'Approved Volume {value} image changed after its vector trace')
        for name, expected in spec['files'].items():
            path = PRINT / name
            if sha(path) != expected:
                raise ValueError(f'Print vector asset does not match its manifest: {name}')
            if path.suffix == '.pdf':
                pdf = PdfReader(path)
                if len(pdf.pages) != 1 or list(resource_images(pdf.pages[0]['/Resources'])):
                    raise ValueError(f'{name}: vector master contains a raster image')
    if sha(PRINT / 'paper-muted.png') != manifest['paper_muted_sha256']:
        raise ValueError('Muted print paper changed after preblending')
    return sorted(numbers)


def check_frame_alignment(path, width):
    """Check visible borders, since searchable text cannot reveal a shifted form."""
    wrap = width > 600
    top = 9 if wrap else 0
    origins = [9, width - 513] if wrap else [0]
    for origin in origins:
        for offset in (10, 482):
            data = subprocess.check_output([
                'pdftoppm', '-singlefile', '-png', '-r', '72',
                '-x', str(round(origin + offset)), '-y', str(top + 18),
                '-W', '12', '-H', '684', str(path)])
            strip = Image.open(io.BytesIO(data)).convert('RGB')
            rows = sum(any(r > 130 and r > g * 1.25 and r > b * 1.25
                           for r, g, b in (strip.getpixel((x, y)) for x in range(strip.width)))
                       for y in range(strip.height))
            if strip.height != 684 or rows < 650:
                raise ValueError('Visible cover frame is shifted or clipped; inspect the print proof')


def check(path, number, report=None):
    path = Path(path)
    check_fonts(path)
    masters = check_masters(number)
    table = subprocess.check_output(['pdfimages', '-list', str(path)], text=True)
    placements = raster_placements(table)
    check_placements(placements)
    allowed = {pixel_key(Image.open(p)) for p in
               [ROOT / 'tools/assets/approved-charcoal-paper.png', PRINT / 'paper-muted.png']}
    pdf = PdfReader(path)
    check_frame_alignment(path, float(pdf.pages[0].mediabox.width))
    count = 0
    for page in pdf.pages:
        for image in resource_images(page['/Resources']):
            if (image.get('/ColorSpace') != '/DeviceRGB' or image.get('/BitsPerComponent') != 8
                    or image.get('/SMask') or image.get('/Mask')):
                raise ValueError('Print grain must be opaque, native RGB artwork')
            key = ((int(image['/Width']), int(image['/Height'])),
                   hashlib.sha256(image.get_data()).hexdigest())
            if key not in allowed:
                raise ValueError('Print cover contains an unapproved raster image; use vector artwork')
            count += 1
    result = {'schema': 1, 'volume': str(number), 'minimum_required_ppi': MINIMUM_PPI,
              'minimum_observed_ppi': min((min(p['x_ppi'], p['y_ppi']) for p in placements), default=None),
              'raster_content': 'native paper grain only', 'unique_images': count,
              'raster_placements': len(placements), 'vector_masters': masters,
              'embedded_fonts': True, 'visible_frame_alignment': True, 'status': 'pass'}
    if report:
        Path(report).write_text(json.dumps(result, indent=2) + '\n')
    observed = result['minimum_observed_ppi']
    print(f'PASS print preflight: vector artwork/lettering, native grain '
          f'{observed:g} ppi, embedded fonts.' if observed is not None else
          'PASS print preflight: all-vector artwork/lettering and embedded fonts.')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--number', required=True)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    check(args.pdf, args.number, args.report)
