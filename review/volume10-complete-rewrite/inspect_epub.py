#!/usr/bin/env python3
"""Inspect an actual EPUB package and all local links; not a visual review."""
import argparse
from collections import Counter
import json
import posixpath
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zipfile


def inspect(path):
    errors = []
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        if z.testzip():
            errors.append('ZIP CRC failure')
        first = z.infolist()[0]
        if first.filename != 'mimetype' or first.compress_type != zipfile.ZIP_STORED:
            errors.append('mimetype must be first and uncompressed')
        if z.read('mimetype') != b'application/epub+zip':
            errors.append('incorrect mimetype')
        container = ET.fromstring(z.read('META-INF/container.xml'))
        opf = next(e.attrib['full-path'] for e in container.iter() if e.tag.endswith('rootfile'))
        package = ET.fromstring(z.read(opf))
        ns = {'o': 'http://www.idpf.org/2007/opf'}
        items = package.findall('o:manifest/o:item', ns)
        ids = [e.attrib['id'] for e in items]
        if len(ids) != len(set(ids)):
            errors.append('duplicate manifest IDs')
        by_id = {e.attrib['id']: e for e in items}
        uid = package.attrib.get('unique-identifier')
        if not uid or not any(e.attrib.get('id') == uid and (e.text or '').strip() for e in package.iter()):
            errors.append('missing unique identifier target/value')
        spine = package.findall('o:spine/o:itemref', ns)
        for e in spine:
            if e.attrib['idref'] not in by_id:
                errors.append('missing spine item: ' + e.attrib['idref'])
        def resolve(doc, ref):
            parts = urlsplit(ref)
            if parts.scheme or parts.netloc:
                return None
            target = posixpath.normpath(posixpath.join(posixpath.dirname(doc), unquote(parts.path))) if parts.path else doc
            return target, unquote(parts.fragment)
        manifest_paths = {}
        for e in items:
            target, fragment = resolve(opf, e.attrib['href'])
            if target not in names:
                errors.append('missing manifest resource: ' + target)
            manifest_paths[target] = e.attrib['media-type']
        documents, refs, duplicate_ids = {}, [], []
        for name in sorted(names):
            if name.endswith(('.xhtml', '.html', '.svg', '.ncx')):
                tree = ET.fromstring(z.read(name))
                doc_ids = [e.attrib['id'] for e in tree.iter() if 'id' in e.attrib]
                dup = [i for i, n in Counter(doc_ids).items() if n > 1]
                if dup:
                    duplicate_ids.append({'path': name, 'ids': dup})
                documents[name] = set(doc_ids)
                for e in tree.iter():
                    for key, value in e.attrib.items():
                        if key.split('}')[-1] in ('href', 'src', 'data') and value:
                            refs.append((name, value))
            elif name.endswith('.css'):
                for ref in re.findall(r'url\(\s*[\"\x27]?([^\"\x27)]+)', z.read(name).decode()):
                    refs.append((name, ref.strip()))
        local = 0
        for doc, ref in refs:
            resolved = resolve(doc, ref)
            if resolved is None:
                continue
            target, fragment = resolved
            local += 1
            if target not in names:
                errors.append(f'{doc}: missing {ref} -> {target}')
            elif fragment and target in documents and fragment not in documents[target]:
                errors.append(f'{doc}: missing fragment {ref}')
        if duplicate_ids:
            errors.append('duplicate document IDs: ' + repr(duplicate_ids))
        size = Path(path).stat().st_size
        if size >= 50_000_000:
            errors.append('EPUB is not below 50 MB')
        result = {'path': str(path), 'bytes': size, 'zip_crc': 'pass', 'opf': opf,
                  'manifest_items': len(items), 'spine_items': len(spine),
                  'unique_identifier': uid, 'documents': len(documents),
                  'local_references_checked': local,
                  'media_types': dict(Counter(manifest_paths.values())),
                  'errors': errors}
        return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('epub')
    args = parser.parse_args()
    result = inspect(args.epub)
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(result['errors']))
