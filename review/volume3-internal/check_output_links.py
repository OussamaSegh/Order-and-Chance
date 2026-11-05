"""Audit actual Volume 3 local destinations and keyed exercise output parity.

This checks produced files and DOM structure, not mathematical correctness,
visual approval, external URL availability, or native Kindle behavior.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile


class Node:
    def __init__(self, tag='', attrs=(), parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []

    def walk(self):
        yield self
        for child in self.children:
            yield from child.walk()

    def has(self, cls):
        return cls in self.attrs.get('class', '').split()


class Document(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(n)
        if tag not in self.VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break


def audit(root, files, expected):
    docs = {p.resolve(): Document(p.read_text()) for p in files}
    ids = {p: Counter(n.attrs['id'] for n in d.root.walk()
                      if 'id' in n.attrs) for p, d in docs.items()}
    errors, links, blocks = [], [], {c: [] for c in ('exercise', 'hint', 'solution')}

    def resolve(source, value):
        u = urlsplit(value)
        if u.scheme or u.netloc:
            return None
        path = ((root / unquote(u.path).lstrip('/')) if u.path.startswith('/')
                else (source.parent / unquote(u.path))) if u.path else source
        path = path.resolve()
        if path.is_dir():
            path /= 'index.html'
        return path, unquote(u.fragment)

    for p, doc in docs.items():
        relative = p.relative_to(root).as_posix()
        errors += [{'file': relative, 'error': 'duplicate id', 'id': k}
                   for k, v in ids[p].items() if v > 1]
        for node in doc.root.walk():
            destinations = [(a, node.attrs[a]) for a in ('href', 'src', 'poster')
                            if a in node.attrs]
            if node.tag == 'meta' and node.attrs.get('http-equiv', '').lower() == 'refresh':
                match = re.search(r'url\s*=\s*(.*)', node.attrs.get('content', ''), re.I)
                if match:
                    destinations.append(('refresh', match[1].strip(' \"\'')))
            for attr, value in destinations:
                result = resolve(p, value)
                if result is None:
                    continue
                target, fragment = result
                row = {'file': relative, 'tag': node.tag, 'attribute': attr,
                       'destination': value, 'target_exists': target.is_file(),
                       'fragment': fragment}
                if fragment and target.suffix.lower() in ('.xhtml', '.html', '.svg', '.xml'):
                    if target not in ids and target.is_file():
                        parsed = Document(target.read_text())
                        ids[target] = Counter(n.attrs['id'] for n in parsed.root.walk()
                                              if 'id' in n.attrs)
                    row['fragment_exists'] = bool(ids.get(target, {}).get(fragment))
                links.append(row)
                if not row['target_exists'] or row.get('fragment_exists') is False:
                    errors.append(dict(row, error='missing local destination'))
            if node.tag != 'div':
                continue
            for cls in blocks:
                if not node.has(cls):
                    continue
                if cls == 'exercise':
                    key = node.attrs.get('id')
                else:
                    heads = [n for n in node.walk() if n.has('oc-head')]
                    refs = [n.attrs['href'] for head in heads for n in head.walk()
                            if n.tag == 'a' and 'href' in n.attrs]
                    if len(refs) != 1:
                        errors.append({'file': relative, 'kind': cls,
                                       'error': 'expected exactly one prompt backlink'})
                        key = None
                    else:
                        resolved = resolve(p, refs[0])
                        key = resolved[1] if resolved else None
                blocks[cls].append({'key': key, 'file': relative,
                                    'ordinal_in_kind': len(blocks[cls])+1,
                                    'number': node.attrs.get('data-number')})
    for cls, rows in blocks.items():
        actual = Counter(x['key'] for x in rows)
        if actual != Counter(expected):
            errors.append({'error': 'keyed block parity', 'kind': cls,
                           'missing': list((Counter(expected)-actual).elements()),
                           'extra': list((actual-Counter(expected)).elements())})
    return {'files': len(files), 'local_destinations': len(links),
            'links': links, 'exercise_blocks': blocks, 'problems': errors}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('site', type=Path)
    p.add_argument('epub', type=Path)
    p.add_argument('--inventory', type=Path, required=True)
    p.add_argument('--source-commit', required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    inv = json.loads(a.inventory.read_text())
    keys = [x['key'] for x in inv['items'] if x['kind'] == 'exercise']
    root = a.site.resolve()
    reader = audit(root, sorted((root/'read/volume3-symmetry').glob('*.html')), keys)
    with tempfile.TemporaryDirectory() as tmp:
        epubroot = Path(tmp)
        with zipfile.ZipFile(a.epub) as z:
            z.extractall(epubroot)
        epub = audit(epubroot, sorted(epubroot.rglob('*.xhtml')), keys)
    result = {'source_commit': a.source_commit,
              'measurement_tool_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'epub_sha256': hashlib.sha256(a.epub.read_bytes()).hexdigest(),
              'inventory_sha256': hashlib.sha256(a.inventory.read_bytes()).hexdigest(),
              'scope': 'Actual unmodified reader/EPUB local href/src/poster and redirect destinations, all HTML/XHTML IDs, and every keyed exercise/hint/solution block and prompt backlink. Hint/solution blocks have no source IDs; block ordinal and exact exercise key are recorded. No fabricated hint/solution deep links. External links, CSS URL assets, UI behavior and visual approval are separate.',
              'expected_exercises': len(keys), 'reader': reader, 'epub': epub}
    a.output.write_text(json.dumps(result, indent=2)+'\n')
    print(f"reader {reader['files']} files/{reader['local_destinations']} destinations, "
          f"EPUB {epub['files']} files/{epub['local_destinations']} destinations; "
          f"{len(keys)} keyed triples each; "
          f"{len(reader['problems'])+len(epub['problems'])} problems")
    return bool(reader['problems'] or epub['problems'])


if __name__ == '__main__':
    raise SystemExit(main())
