"""Verify the shared Cormorant/Fira cover family."""
import argparse
import hashlib
import json
from pathlib import Path
import posixpath
import re
import subprocess
import xml.etree.ElementTree as ET
import zipfile

from pypdf import PdfReader
from series_cover import ROOT, sha
from series_metadata import subtitle


def form_hashes(resources, seen=None):
    seen = set() if seen is None else seen
    objects = resources.get_object().get('/XObject')
    if not objects:
        return
    for ref in objects.get_object().values():
        obj = ref.get_object()
        if id(obj) in seen:
            continue
        seen.add(id(obj))
        if obj.get('/Subtype') != '/Form':
            continue
        yield hashlib.sha256(obj.get_data()).hexdigest()
        if obj.get('/Resources'):
            yield from form_hashes(obj['/Resources'], seen)


def content_streams(page):
    contents = page.get_contents()
    if contents is not None:
        yield contents.get_data()
    resources = page.get('/Resources')
    if resources is not None and hasattr(resources, 'get_object'):
        yield from _form_streams(resources)


def _form_streams(resources, seen=None):
    seen = set() if seen is None else seen
    objects = resources.get_object().get('/XObject')
    if not objects:
        return
    for ref in objects.get_object().values():
        obj = ref.get_object()
        if id(obj) in seen or obj.get('/Subtype') != '/Form':
            continue
        seen.add(id(obj))
        yield obj.get_data()
        if obj.get('/Resources'):
            yield from _form_streams(obj['/Resources'], seen)


def font_names(page):
    found = {}
    resources = page.get('/Resources')
    if resources is None:
        return found
    if hasattr(resources, 'get_object'):
        _font_names(resources, found)
        return found
    for key, value in (resources.get('/Font') or {}).items():
        obj = value.get_object() if hasattr(value, 'get_object') else value
        found[str(key).lstrip('/')] = str(obj.get('/BaseFont', ''))
    return found


def _font_names(resources, found, seen=None):
    seen = set() if seen is None else seen
    obj = resources.get_object()
    fonts = obj.get('/Font')
    if fonts:
        for key, value in fonts.get_object().items():
            found[str(key).lstrip('/')] = str(value.get_object().get('/BaseFont', ''))
    objects = obj.get('/XObject')
    if not objects:
        return
    for ref in objects.get_object().values():
        form = ref.get_object()
        if id(form) in seen or form.get('/Subtype') != '/Form' or not form.get('/Resources'):
            continue
        seen.add(id(form))
        _font_names(form['/Resources'], found, seen)


def check_assets(number):
    manifest = json.loads((ROOT / 'tools/assets/series/manifest.json').read_text())
    for name, expected in manifest['files'].items():
        if sha(ROOT / name) != expected:
            raise ValueError(f'Shared cover source changed without regeneration: {name}')
    art = next(row for row in manifest['artwork'] if row['number'] == str(number))
    for key in ('motif', 'lettering', 'about'):
        if sha(ROOT / art[key]) != art[key + '_sha256']:
            raise ValueError(f'Volume {number}: {art[key]} differs from the cover manifest')
    lettering = (ROOT / art['lettering']).read_text()
    if 'lower-rule y=2.9500in' not in lettering or 'upper-rule y=6.9000in' not in lettering:
        raise ValueError('The coral rules are no longer at the shared heights')
    return {'identity': 'tools/assets/print/identity-0.pdf', 'fixed_template': True}


def check_font_sizes(page):
    names = font_names(page)
    blob = b'\n'.join(content_streams(page))
    uses = re.findall(rb'/([A-Za-z0-9]+)\s+([\d.]+)\s+Tf', blob)
    title = [float(size) for name, size in uses if 'CormorantGaramond-Regular' in names.get(name.decode(), '')]
    expected = 42 * 72 / 72.27
    if not title or any(abs(size - expected) > .05 for size in title):
        raise ValueError('Cover title is not Cormorant Garamond Regular at 42pt')
    families = ' '.join(names.values())
    for face in ('CormorantGaramond-SemiBold', 'CormorantGaramond-Medium', 'FiraSans-Light'):
        if face not in families:
            raise ValueError(f'Cover is missing the shared face {face}')


def check_copy(path, number):
    text = ' '.join(subprocess.check_output(['pdftotext', '-f', '1', '-l', '1', str(path), '-'], text=True).split())
    catalog = json.loads((ROOT / 'common/series-catalog.json').read_text())['volumes']
    for expected in (catalog[str(number)]['title'], subtitle(number),
                     'The Hidden Architecture of Mathematics', 'SEGHAIER Oussama'):
        if expected not in text:
            raise ValueError(f'Volume {number}: cover is missing “{expected}”')


def check(path, number, cover_png=None, epub=None, reader=None):
    path = Path(path)
    check_assets(number)
    page = PdfReader(path).pages[0]
    width, height = float(page.mediabox.width), float(page.mediabox.height)
    if abs(width / height - .7) > .0001:
        raise ValueError('Cover no longer has the 7:10 proportions')
    reference = PdfReader(ROOT / 'tools/assets/print/identity-0.pdf').pages[0].get_contents().get_data()
    if hashlib.sha256(reference).hexdigest() not in set(form_hashes(page['/Resources'])):
        raise ValueError('Cover does not reuse the shared double frame')
    check_font_sizes(page)
    check_copy(path, number)
    if cover_png:
        pixels = Path(cover_png).read_bytes()
        if reader and (Path(reader) / 'cover.png').read_bytes() != pixels:
            raise ValueError('Reader still uses a different cover')
        if epub:
            with zipfile.ZipFile(epub) as archive:
                container = ET.fromstring(archive.read('META-INF/container.xml'))
                opf = container.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile').attrib['full-path']
                tree = ET.fromstring(archive.read(opf))
                item = next(e for e in tree.findall('.//{http://www.idpf.org/2007/opf}item')
                            if 'cover-image' in e.attrib.get('properties', '').split())
                name = posixpath.normpath(posixpath.join(posixpath.dirname(opf), item.attrib['href']))
                if archive.read(name) != pixels:
                    raise ValueError('EPUB still uses a different cover')
    print(f'PASS shared cover family, Volume {number}: Cormorant title, Fira small type, shared frame.')
    return {'fixed_template': True, 'identity': 'shared frame', 'family': 'cormorant-fira'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--number', required=True)
    parser.add_argument('--cover-png', type=Path)
    parser.add_argument('--epub', type=Path)
    parser.add_argument('--reader', type=Path)
    args = parser.parse_args()
    check(args.pdf, args.number, args.cover_png, args.epub, args.reader)
