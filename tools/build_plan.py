"""Content-addressed book planning and complete-library cache assembly for CI."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path
from book_outputs import clean, check
from check_cover_pdf import check_interior
from check_interior_style import check as check_style
from book_pdf import check_pair
from check_print_cover import check as check_print_cover
from print_layout import specification

SCHEMA = 6
NAME = re.compile(r"tome[A-Z]?\d+-[A-Za-z0-9-]+\Z")


def fingerprints(root):
    files = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    books = sorted(p.name for p in root.glob('tome*') if (p / 'main.tex').is_file())
    if not all(NAME.fullmatch(book) for book in books):
        raise ValueError('Unsupported book directory name')
    shared = [f for f in files if f in {'build.sh', 'tools/requirements-build.txt'} or f.startswith('common/') or f.startswith('tools/assets/') or (
        f.startswith('tools/') and Path(f).suffix in {'.py', '.tex', '.lua', '.css', '.html'}
        and Path(f).name not in {'site.py', 'site-template.html', 'build_plan.py'}
        and not Path(f).name.startswith('test_'))]

    def digest(paths):
        h = hashlib.sha256(b'book-output-v6\0')
        for name in sorted(paths):
            h.update(name.encode() + b'\0' + (root / name).read_bytes() + b'\0')
        return h.hexdigest()

    inputs = {book: [f for f in files if f.startswith(book + '/')] for book in books}
    result = {book: digest(shared + inputs[book]) for book in books}
    return result


def complete(cache, book):
    required = [f'dist/{book}.pdf', f'dist/{book}.epub',
                f'dist/html/{book}/index.html', f'build/{book}/cover.pdf']
    required += [f'dist/kdp/{book}-{suffix}' for suffix in
                 ['print.pdf', 'cover-wrap.pdf', 'ebook-cover.jpg', 'listing.md', 'print-metadata.json']]
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
    changed = [b for b, key in current.items() if force or old.get(b) != key or not complete(cache, b)]
    return {'schema': SCHEMA, 'books': current, 'changed': changed,
            'removed': sorted(set(previous_books) - set(current))}


def remove_book(root, book):
    if not NAME.fullmatch(book):
        raise ValueError('Invalid cached book name')
    for p in (root / 'dist').glob(book + '.*'):
        if p.is_file():
            p.unlink()
    for p in (root / 'dist').glob(book + '-*.pdf'):
        p.unlink()
    for p in (root / 'dist/kdp').glob(book + '-*'):
        if p.is_file():
            p.unlink()
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


def snapshot(root, cache, data):
    check(root / 'dist')
    for book in data['books']:
        if not complete(root, book):
            raise ValueError(f'Incomplete output for {book}')
        download = root / 'dist' / f'{book}.pdf'
        interior = root / 'dist/kdp' / f'{book}-print.pdf'
        pages = check_interior(interior)
        check_style(interior)
        check_interior(download)
        if check_pair(download, interior) != pages:
            raise ValueError(f'PDF pair page counts disagree for {book}')
        metadata = json.loads((root / 'dist/kdp' / f'{book}-print-metadata.json').read_text())
        if metadata != specification(pages, metadata.get('inner_margin', '0.75in')):
            raise ValueError(f'PDF and paperback metadata disagree for {book}')
        number = re.match(r'tome([A-Z]?\d+)-', book).group(1)
        check_print_cover(root / 'dist/kdp' / f'{book}-cover-wrap.pdf', number)
    shutil.rmtree(cache, ignore_errors=True)
    cache.mkdir(parents=True)
    shutil.copytree(root / 'dist', cache / 'dist')
    for book in data['books']:
        target = cache / 'build' / book
        target.mkdir(parents=True)
        shutil.copy2(root / 'build' / book / 'cover.pdf', target / 'cover.pdf')
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
