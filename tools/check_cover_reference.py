"""Verify that the approved cover image is used unchanged, not reconstructed.

Usage: python3 tools/check_cover_reference.py front.pdf [--epub book.epub]
Requires poppler and Pillow. Compares actual decoded PDF image pixels, plus exact
PNG file bytes in EPUB, reader and website when those paths are supplied.
"""
import argparse
import hashlib
import json
from pathlib import Path
import posixpath
import subprocess
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from PIL import Image

ROOT=Path(__file__).resolve().parent.parent


def check(pdf, epub=None, reader=None, site=None, number="0"):
    if not str(number).isalnum():
        raise ValueError("Invalid volume number")
    name = "approved-cover.json" if str(number) == "0" else f"approved-cover-{number}.json"
    spec=json.loads((ROOT/'tools/assets'/name).read_text())
    source=ROOT/spec['source']
    master=ROOT/spec['asset']
    data=source.read_bytes()
    assert hashlib.sha256(data).hexdigest()==spec['sha256'], 'Approved reference was changed'
    assert master.read_bytes()==data, 'Production master differs from approved reference'
    metadata=(ROOT/spec['book']/'main.tex').read_text()
    assert f"Volume {number}: {spec['title']}" in metadata, 'Visible master no longer matches the book title'
    expected=Image.open(master).convert('RGB')
    with tempfile.TemporaryDirectory() as directory:
        prefix=Path(directory)/'embedded'
        subprocess.run(['pdfimages','-f','1','-l','1','-png',str(pdf),str(prefix)],check=True)
        matches=[]
        for path in Path(directory).glob('*.png'):
            actual=Image.open(path).convert('RGB')
            matches.append(actual.size==expected.size and actual.tobytes()==expected.tobytes())
        assert any(matches),'PDF does not contain the exact approved image pixels'
    if epub:
        with zipfile.ZipFile(epub) as z:
            container=ET.fromstring(z.read('META-INF/container.xml'))
            opf=container.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile').attrib['full-path']
            tree=ET.fromstring(z.read(opf))
            item=next(e for e in tree.findall('.//{http://www.idpf.org/2007/opf}item') if 'cover-image' in e.attrib.get('properties','').split())
            name=posixpath.normpath(posixpath.join(posixpath.dirname(opf),item.attrib['href']))
            assert z.read(name)==data,'EPUB cover is not the unchanged approved PNG'
    if reader:
        assert (reader/'cover.png').read_bytes()==data,'Reader cover differs from approved PNG'
    if site:
        assert (site/(spec['book']+'-cover.png')).read_bytes()==data,'Website cover differs from approved PNG'
    print('PASS exact approved master: file hash, embedded PDF pixels and supplied digital covers.')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('pdf',type=Path)
    p.add_argument('--number',default='0',help='Approved volume number (default: 0)')
    p.add_argument('--epub',type=Path)
    p.add_argument('--reader',type=Path)
    p.add_argument('--site',type=Path)
    a=p.parse_args()
    check(a.pdf,a.epub,a.reader,a.site,a.number)
