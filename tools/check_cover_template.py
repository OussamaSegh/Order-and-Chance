"""Verify the locked Volume-0 master instead of separate concept-image layouts."""
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
from series_cover import ROOT, settings, check_sync, check_titles, sha, subtitle_baseline, subtitle_cap_top
from series_metadata import subtitle


def form_hashes(resources, seen=None):
    seen=set() if seen is None else seen
    objects=resources.get_object().get('/XObject')
    if not objects:return
    for ref in objects.get_object().values():
        obj=ref.get_object()
        if id(obj) in seen:continue
        seen.add(id(obj))
        if obj.get('/Subtype')!='/Form':continue
        yield hashlib.sha256(obj.get_data()).hexdigest()
        if obj.get('/Resources'):yield from form_hashes(obj['/Resources'],seen)


def check_assets(number):
    check_sync();check_titles();data=settings()
    manifest=json.loads((ROOT/'tools/assets/series/manifest.json').read_text())
    for name,expected in manifest['files'].items():
        if sha(ROOT/name)!=expected:raise ValueError(f'Shared cover master changed without regeneration: {name}')
    art=next(row for row in manifest['artwork'] if row['number']==str(number))
    path=ROOT/art['book']/'cover-motif.tex'
    if sha(path)!=art['sha256']:raise ValueError(f'Volume {number}: illustration differs from the shared 3D manifest')
    if art['space']!='3D':raise ValueError('Every cover needs one world-space 3D illustration')
    if art['shared_camera']!=data['camera'] or art['shared_material']!=data['material']:
        raise ValueError('A volume overrides the common camera or wireframe material')
    if (art.get('glow')!='five-layer-vector-radiance'
                            or art.get('hidden_lines')!='depth-tested-before-glow'):
        raise ValueError('A volume bypasses the approved luminous wireframe treatment')
    if art['renderer']=='shared-camera-vector':
        directions=json.loads((ROOT/'tools/assets/cover-art-direction.json').read_text())
        if art.get('art_direction')!=directions[str(number)]:raise ValueError('Illustration composition differs from its reviewed direction')
        bounds=art['screen_bounds_px'];clip=data['art_clip_px']
        if bounds[0]<clip[0]+10 or bounds[2]>clip[2]-10 or bounds[3]>clip[3]-10:
            raise ValueError('Illustration silhouette or glow is clipped')
        minimum=680 if len(check_titles()[str(number)])==2 else 570
        if bounds[1]<minimum:raise ValueError('Illustration overlaps its title/subtitle area')
    return data


def check_font_sizes(page,data):
    fonts=page['/Resources']['/Font']
    names={str(key).lstrip('/'):str(value.get_object().get('/BaseFont','')) for key,value in fonts.items()}
    uses=re.findall(rb'/([A-Za-z0-9]+)\s+([\d.]+)\s+Tf',page.get_contents().get_data())
    title=[float(size) for name,size in uses if 'InterDisplay-Bold' in names.get(name.decode(), '')]
    expected=data['title_size_pt']*72/72.27
    if not title or any(abs(size-expected)>.02 for size in title):
        raise ValueError('Cover title is not in the one fixed bold typeface and size')


def check_subtitle(path,number,height):
    xml=subprocess.check_output(['pdftotext','-f','1','-l','1','-bbox',str(path),'-'])
    words=[e for e in ET.fromstring(xml).iter() if e.tag.endswith('word')]
    expected=subtitle(number).split()
    for i in range(len(words)-len(expected)+1):
        if [''.join(e.itertext()) for e in words[i:i+len(expected)]]==expected:
            top=float(words[i].attrib['yMin'])/height
            # Same font ascent and gap; a one-line title moves the subtitle up one leading.
            expected_top=.3928264+(subtitle_baseline(number)-settings()['subtitle_baseline_source_px'])/1500
            if abs(top-expected_top)>.0001:
                raise ValueError(f'Volume {number}: subtitle moved from the shared title-relative anchor')
            return
    raise ValueError(f'Volume {number}: missing complete subtitle')


def check(path,number,cover_png=None,epub=None,reader=None):
    path=Path(path);data=check_assets(number);page=PdfReader(path).pages[0]
    width,height=float(page.mediabox.width),float(page.mediabox.height)
    if abs(width/height-.7)>.0001:raise ValueError('Cover no longer has the 7:10 master proportions')
    reference=PdfReader(ROOT/data['identity']).pages[0].get_contents().get_data()
    wanted=hashlib.sha256(reference).hexdigest()
    forms=set(form_hashes(page['/Resources']))
    if wanted not in forms:
        raise ValueError('Cover does not reuse the exact common Volume-0 frame/masthead/author form')
    if str(number)=='0':
        archived=PdfReader(ROOT/data['reference_illustration']).pages[0].get_contents().get_data()
        if hashlib.sha256(archived).hexdigest() in forms:
            raise ValueError('Volume 0 still embeds the archived Gaussian instead of the common native material')
    check_font_sizes(page,data);check_subtitle(path,number,height)
    if cover_png:
        pixels=Path(cover_png).read_bytes()
        if reader and (Path(reader)/'cover.png').read_bytes()!=pixels:
            raise ValueError('Reader still uses a different cover master')
        if epub:
            with zipfile.ZipFile(epub) as z:
                container=ET.fromstring(z.read('META-INF/container.xml'))
                opf=container.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile').attrib['full-path']
                tree=ET.fromstring(z.read(opf))
                item=next(e for e in tree.findall('.//{http://www.idpf.org/2007/opf}item') if 'cover-image' in e.attrib.get('properties','').split())
                name=posixpath.normpath(posixpath.join(posixpath.dirname(opf),item.attrib['href']))
                if z.read(name)!=pixels:raise ValueError('EPUB still uses a different cover master')
    print(f'PASS shared cover master, Volume {number}: fixed bold type, subtitle below title, identical common identity.')
    return {'fixed_template':True,'subtitle_cap_top_source_px':subtitle_cap_top(number),'identity':'Volume 0','space':'3D'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf',type=Path);p.add_argument('--number',required=True)
    p.add_argument('--cover-png',type=Path);p.add_argument('--epub',type=Path);p.add_argument('--reader',type=Path)
    a=p.parse_args();check(a.pdf,a.number,a.cover_png,a.epub,a.reader)
