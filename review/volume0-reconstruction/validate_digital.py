"""Check complete digital resources, exercise apparatus and PDF-number concordance."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import posixpath
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[2]
BOOK = 'volume0-mathematical-maturity'

class Node:
    def __init__(self, tag, attrs):
        self.tag, self.attrs, self.parts = tag, dict(attrs), []
    @property
    def text(self):
        return ' '.join(''.join(self.parts).split())

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.nodes, self.stack = [], []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        n=Node(tag,attrs);self.nodes.append(n)
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:
            self.stack.append(n)
    def handle_startendtag(self,tag,attrs):
        self.nodes.append(Node(tag,attrs))
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i].tag==tag:
                del self.stack[i:];return
    def handle_data(self,data):
        for node in self.stack:node.parts.append(data)

def validate(resources, documents, aux, expected_ids):
    errors=[];pages={};links=0;reference_checks=0;exercises=[];hints=0;solutions=0
    for name in documents:
        text=resources[name].decode()
        if name.endswith('.xhtml'):
            try:
                xml=ET.fromstring(text)
                for node in xml.iter():
                    if 'math' in node.get('class','').split() and not any(x.tag=='{http://www.w3.org/1998/Math/MathML}math' for x in node.iter()):
                        errors.append(f'{name}: unconverted TeX instead of MathML')
            except ET.ParseError as exc:errors.append(f'{name}: XML error {exc}')
        page=Page(text);pages[name]=page
        ids=[n.attrs['id'] for n in page.nodes if 'id' in n.attrs]
        duplicate=[key for key,count in Counter(ids).items() if count>1]
        if duplicate:errors.append(f'{name}: duplicate IDs {duplicate}')
    known_ids={n.attrs['id'] for p in pages.values() for n in p.nodes if 'id' in n.attrs}
    if expected_ids-known_ids:errors.append('Missing source labels: '+str(sorted(expected_ids-known_ids)))
    for name,page in pages.items():
        for node in page.nodes:
            attr=node.attrs;classes=attr.get('class','').split()
            if 'exercise' in classes:
                label=attr.get('id');exercises.append(label)
                wanted=aux.get(label)
                if not wanted or not node.text.startswith('Exercise '+wanted):
                    errors.append(f'{name}: wrong exercise number {label}: {node.text[:60]} expected {wanted}')
            if 'hint' in classes:hints+=1
            if 'solution' in classes:solutions+=1
            ref=attr.get('data-reference')
            if ref in aux:
                want=aux[ref]
                if attr.get('data-reference-type')=='eqref':want='('+want+')'
                if node.text!=want:errors.append(f'{name}: {ref}: reference {node.text!r}, expected {want!r}')
                reference_checks+=1
            for key in ('href','src'):
                target=attr.get(key)
                if not target:continue
                parsed=urlsplit(target)
                if parsed.scheme or parsed.netloc:continue
                dest=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(parsed.path))) if parsed.path else name
                links+=1
                if dest not in resources:
                    errors.append(f'{name}: missing resource {target}');continue
                fragment=unquote(parsed.fragment)
                if fragment and dest in pages and not any(n.attrs.get('id')==fragment for n in pages[dest].nodes):
                    errors.append(f'{name}: missing fragment {target}')
    if len(exercises)!=155 or len(set(exercises))!=155:errors.append(f'Expected 155 unique exercises, got {len(exercises)}')
    if hints!=155 or solutions!=155:errors.append(f'Incomplete hint/solution apparatus: {hints}/{solutions}')
    return dict(documents=len(pages),local_links_and_resources=links,pdf_reference_checks=reference_checks,
                source_labels_retained=len(expected_ids & known_ids),exercises=len(exercises),hints=hints,solutions=solutions,errors=errors)

def main():
    report=Path(__file__).resolve().parent
    inventory=json.loads((report/'current-inventory.json').read_text())['units']
    expected={label for unit in inventory for label in unit['labels']}
    aux={m[1]:m[2] for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',(ROOT/'build'/BOOK/'main.aux').read_text())}
    epub=ROOT/'dist'/(BOOK+'.epub')
    with zipfile.ZipFile(epub) as z:
        if z.testzip():raise AssertionError('EPUB archive CRC error')
        resources={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
    result={'epub':validate(resources,[n for n in resources if n.endswith('.xhtml')],aux,expected)}
    site=ROOT/'build/digital-review/site'
    resources={p.relative_to(site).as_posix():p.read_bytes() for p in site.rglob('*') if p.is_file()}
    prefix='read/'+BOOK+'/'
    result['html']=validate(resources,[n for n in resources if n.startswith(prefix) and n.endswith('.html')],aux,expected)
    (report/'digital-structure-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    if any(x['errors'] for x in result.values()):raise SystemExit(1)

if __name__=='__main__':main()
