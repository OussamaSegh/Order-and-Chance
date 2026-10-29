"""Reject references to accompanying digital notebooks in first-edition book copy."""
import re
import sys
from pathlib import Path
from epub_prep import inline

ROOT = Path(__file__).resolve().parent.parent
# These refer to handwritten mathematics or a reader's research journal.
HISTORICAL = re.compile(
    r"Ramanujan's Notebooks|his notebooks?|notebooks in the early 1930s|"
    r"thick notebook|spaces of that notebook|Notebooks, Periodic Drawings|"
    r"research notebooks?(?: entry)?|with a notebook open|A notebook entry",
    re.IGNORECASE)
FORBIDDEN = re.compile(r"\bnotebooks?\b|\bJupyter\b|\.ipynb\b", re.IGNORECASE)


def check(book):
    texts = [(book / 'main.tex', inline(book / 'main.tex'))]
    for name in ['blurb.tex', 'kdp.md']:
        path = book / name
        if path.exists():
            texts.append((path, path.read_text()))
    path = ROOT / 'tools/blurb-default.tex'
    texts.append((path, path.read_text()))
    for path, text in texts:
        text = HISTORICAL.sub('', text)
        match = FORBIDDEN.search(text)
        if match:
            context = ' '.join(text[max(0, match.start()-60):match.end()+80].split())
            raise ValueError(f'{path}: first-edition companion reference: {context}')


def main():
    books = [ROOT / name for name in sys.argv[1:]] if sys.argv[1:] else sorted(
        p.parent for p in ROOT.glob('volume*/main.tex'))
    for book in books:
        check(book)
    print(f'First-edition copy checked: {len(books)} books')


if __name__ == '__main__':
    main()
