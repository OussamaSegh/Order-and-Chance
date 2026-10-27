"""Content-addressed book planning and complete-library cache assembly for CI."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

SCHEMA = 1
NAME = re.compile(r"tome[A-Z]?\d+-[A-Za-z0-9-]+\Z")


def fingerprints(root):
    files = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    books = sorted(p.name for p in root.glob('tome*') if (p / 'main.tex').is_file())
    if not all(NAME.fullmatch(book) for book in books):
        raise ValueError('Unsupported book directory name')
    shared = [f for f in files if f == 'build.sh' or f.startswith('common/') or f.startswith('tools/assets/') or (
        f.startswith('tools/') and Path(f).suffix in {'.py', '.tex', '.lua', '.css', '.html'}
        and Path(f).name not in {'site.py', 'site-template.html', 'build_plan.py'}
        and not Path(f).name.startswith('test_'))]

    def digest(paths):
        h = hashlib.sha256(b'book-output-v1\0')
        for name in sorted(paths):
            h.update(name.encode() + b'\0' + (root / name).read_bytes() + b'\0')
        return h.hexdigest()

    inputs = {book: [f for f in files if f.startswith(book + '/')] for book in books}
    result = {book: digest(shared + inputs[book]) for book in books}
    # S4's generator reads the other tomes, not just its own directory.
    if 'tomeS4-companion' in result:
        result['tomeS4-companion'] = digest(shared + [f for paths in inputs.values() for f in paths])
    return result


def complete(cache, book):
    required = [f'dist/{book}.pdf', f'dist/{book}-kindle.pdf', f'dist/{book}.epub',
                f'dist/html/{book}/index.html', f'build/{book}/cover.pdf']
    required += [f'dist/kdp/{book}-{suffix}' for suffix in
                 ['print.pdf', 'cover-wrap.pdf', 'ebook-cover.jpg', 'listing.md']]
    return all((cache / p).is_file() and (cache / p).stat().st_size for p in required)


def plan(root, cache, force=False):
    current = fingerprints(root)
    try:
        previous = json.loads((cache / 'manifest.json').read_text())
        old = previous['books'] if previous.get('schema') == SCHEMA else {}
    except (OSError, ValueError, KeyError):
        old = {}
    changed = [b for b, key in current.items() if force or old.get(b) != key or not complete(cache, b)]
    return {'schema': SCHEMA, 'books': current, 'changed': changed,
            'removed': sorted(set(old) - set(current))}


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
    for p in (root / 'dist').glob('*-phone.pdf'):
        p.unlink()


def snapshot(root, cache, data):
    for book in data['books']:
        if not complete(root, book):
            raise ValueError(f'Incomplete output for {book}')
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
