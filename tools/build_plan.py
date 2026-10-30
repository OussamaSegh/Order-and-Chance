"""Content-addressed book planning and complete-library cache assembly for CI."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from book_outputs import clean, check
from legacy_urls import OLD_PREFIX, OLD_STEMS
from public_names import filename
from check_cover_pdf import check_interior
from check_interior_style import check as check_style
from book_pdf import check_pair
from kdp_pdf import check as check_kdp
from check_print_cover import check as check_print_cover
from check_cover_template import check as check_cover_template
from print_layout import specification

SCHEMA = 8
NAME = re.compile(r"volume[A-Z]?\d+-[A-Za-z0-9-]+\Z")


def fingerprints(root):
    files = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    books = sorted(p.name for p in root.glob('volume*') if (p / 'main.tex').is_file())
    if not all(NAME.fullmatch(book) for book in books):
        raise ValueError('Unsupported book directory name')
    shared = [f for f in files if f in {'build.sh', 'tools/requirements-build.txt'} or f.startswith('common/') or f.startswith('tools/assets/') or (
        f.startswith('tools/') and Path(f).suffix in {'.py', '.tex', '.lua', '.css', '.html'}
        and Path(f).name not in {'site.py', 'site-template.html', 'build_plan.py'}
        and not Path(f).name.startswith('test_'))]

    def digest(paths):
        h = hashlib.sha256(b'book-output-v8\0')
        for name in sorted(paths):
            h.update(name.encode() + b'\0' + (root / name).read_bytes() + b'\0')
        return h.hexdigest()

    inputs = {book: [f for f in files if f.startswith(book + '/')] for book in books}
    result = {book: digest(shared + inputs[book]) for book in books}
    return result


def complete(cache, book, root=None):
    root = root or cache.parent
    name = lambda kind: filename(book, kind, root)
    required = [f'dist/{name("pdf")}', f'dist/{name("epub")}',
                f'dist/html/{book}/index.html', f'build/{book}/cover.pdf',
                f'build/{book}/kdp-preflight.json', f'build/{book}/cover-preflight.json']
    required += [f'dist/kdp/{name(kind)}' for kind in
                 ['print', 'wrap', 'ebook', 'listing', 'metadata']]
    return all((cache / p).is_file() and (cache / p).stat().st_size for p in required)


def plan(root, cache, force=False):
    current = fingerprints(root)
    try:
        previous = json.loads((cache / 'manifest.json').read_text())
        previous_books = previous['books']
        old = previous_books if previous.get('schema') == SCHEMA else {}
    except (OSError, ValueError, KeyError):
        previous_books = {}
        old = {}
    changed = [b for b, key in current.items() if force or old.get(b) != key or not complete(cache, b, root)]
    return {'schema': SCHEMA, 'books': current, 'changed': changed,
            'removed': sorted(set(previous_books) - set(current))}


def remove_book(root, book):
    if not (NAME.fullmatch(book) or book in OLD_STEMS):
        raise ValueError('Invalid cached book name')
    for p in (root / 'dist').glob(book + '.*'):
        if p.is_file():
            p.unlink()
    for p in (root / 'dist').glob(book + '-*.pdf'):
        p.unlink()
    for p in (root / 'dist/kdp').glob(book + '-*'):
        if p.is_file():
            p.unlink()
    if (root / book / 'main.tex').exists():
        for kind in ['pdf', 'epub', 'print', 'wrap', 'ebook', 'listing', 'metadata']:
            folder = root / 'dist' if kind in ['pdf', 'epub'] else root / 'dist/kdp'
            (folder / filename(book, kind, root)).unlink(missing_ok=True)
    shutil.rmtree(root / 'dist/html' / book, ignore_errors=True)
    shutil.rmtree(root / 'build' / book, ignore_errors=True)


def prepare(root, cache, data):
    for folder in ['dist', 'build']:
        if (cache / folder).is_dir():
            shutil.copytree(cache / folder, root / folder, dirs_exist_ok=True)
    # Clear rebuilt readers too, so deleted chapters cannot survive the overlay.
    for book in data['changed'] + data['removed']:
        remove_book(root, book)
    clean(root / 'dist')
    allowed = {filename(book, kind, root) for book in data['books']
               for kind in ['pdf', 'epub', 'print', 'wrap', 'ebook', 'listing', 'metadata']}
    for folder in [root / 'dist', root / 'dist/kdp']:
        for path in folder.glob('*'):
            if path.is_file() and path.name.startswith((OLD_PREFIX, 'volume', 'Volume ', 'Problem Book ')) and path.name not in allowed:
                path.unlink()


def snapshot(root, cache, data):
    check(root / 'dist')
    expected = {filename(book, kind, root) for book in data['books']
                for kind in ['pdf', 'epub', 'print', 'wrap', 'ebook', 'listing', 'metadata']}
    actual = [p for folder in [root / 'dist', root / 'dist/kdp']
              for p in folder.glob('*') if p.is_file()]
    unexpected = [p.name for p in actual if p.name not in expected]
    if unexpected:
        raise ValueError(f'Unexpected public assets: {unexpected}')
    for book in data['books']:
        if not complete(root, book, root):
            raise ValueError(f'Incomplete output for {book}')
        download = root / 'dist' / filename(book, 'pdf', root)
        interior = root / 'dist/kdp' / filename(book, 'print', root)
        pages = check_interior(interior)
        report = root / 'build' / book / 'kdp-preflight.json'
        check_kdp(interior, report)
        check_style(interior)
        check_interior(download)
        if check_pair(download, interior, report=report) != pages:
            raise ValueError(f'PDF pair page counts disagree for {book}')
        metadata = json.loads((root / 'dist/kdp' / filename(book, 'metadata', root)).read_text())
        if metadata != specification(pages, metadata.get('inner_margin', '0.9in')):
            raise ValueError(f'PDF and paperback metadata disagree for {book}')
        number = re.match(r'volume([A-Z]?\d+)-', book).group(1)
        check_print_cover(root / 'dist/kdp' / filename(book, 'wrap', root), number,
                          press_report=root / 'build' / book / 'cover-preflight.json', spine=metadata['spine_in'])
        check_cover_template(root / 'dist' / filename(book, 'pdf', root), number)
    shutil.rmtree(cache, ignore_errors=True)
    cache.mkdir(parents=True)
    shutil.copytree(root / 'dist', cache / 'dist')
    for book in data['books']:
        target = cache / 'build' / book
        target.mkdir(parents=True)
        shutil.copy2(root / 'build' / book / 'cover.pdf', target / 'cover.pdf')
        shutil.copy2(root / 'build' / book / 'kdp-preflight.json', target / 'kdp-preflight.json')
        shutil.copy2(root / 'build' / book / 'cover-preflight.json', target / 'cover-preflight.json')
    (cache / 'manifest.json').write_text(json.dumps({'schema': SCHEMA, 'books': data['books']}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['plan', 'prepare', 'snapshot'])
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    root = Path.cwd()
    cache = root / '.book-cache'
    path = root / 'build-plan.json'
    if args.action == 'plan':
        data = plan(root, cache, args.force)
        path.write_text(json.dumps(data, indent=2))
        print(json.dumps(data['changed']))
    else:
        data = json.loads(path.read_text())
        {'prepare': prepare, 'snapshot': snapshot}[args.action](root, cache, data)


if __name__ == '__main__':
    main()
