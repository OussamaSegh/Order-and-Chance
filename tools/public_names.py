"""Canonical, human-readable public asset names; source identifiers stay stable."""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUFFIXES = {'pdf': '.pdf', 'epub': '.epub', 'print': ' - Print.pdf',
            'wrap': ' - Paperback Cover.pdf', 'ebook': ' - eBook Cover.jpg',
            'listing': ' - Publishing Listing.md', 'metadata': ' - Print Metadata.json',
            'thumbnail': ' - Cover.png'}


def stem(book, root=ROOT):
    source = (Path(root) / book / 'main.tex').read_text(encoding='utf-8')
    match = re.search(r'^% epub-title: .*?Volume ([0-9A-Z]+): (.+)$', source, re.M)
    if match:
        number, title = match.groups()
    else:
        match = re.fullmatch(r'tome(P?\d+)-(.+)', book)
        if not match:
            raise ValueError(f'Invalid book identifier: {book}')
        number, title = match.groups()
        title = title.replace('-', ' ').title()
    label = f'Problem Book {number[1:]}' if number.startswith('P') else f'Volume {number}'
    if any(c in title for c in '/\\<>:"|?*') or any(ord(c) < 32 for c in title):
        raise ValueError(f'Unsafe public title: {title}')
    return f'{label} - {title}'


def filename(book, kind, root=ROOT):
    return stem(book, root) + SUFFIXES[kind]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('book')
    parser.add_argument('kind', choices=['stem', *SUFFIXES])
    args = parser.parse_args()
    print(stem(args.book) if args.kind == 'stem' else filename(args.book, args.kind))
