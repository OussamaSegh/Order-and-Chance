"""Regenerate the approved covers from the shared TikZ generator.

Optical centring is baked in tools/covergen/centring.json. CI checks that the
committed plates match the generator; it does not remeasure the renders.
"""
import difflib
import hashlib
import json
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / 'common/cover-notes.json'
MANIFEST = ROOT / 'tools/assets/series/manifest.json'
CREDITS = ROOT / 'common/cover-credits.tex'
NOTES_MD = ROOT / 'docs/COVER-NOTES.md'

SHARED = [
    'tools/series_cover.py',
    'tools/covergen/front.py',
    'tools/covergen/arts.py',
    'tools/covergen/scene.py',
    'tools/covergen/collatz.py',
    'tools/covergen/collatz_art.py',
    'tools/covergen/centring.json',
    'tools/covergen/zeros.json',
    'tools/covergen/zeta-curve.json',
    'common/cover-notes.json',
    'common/series-catalog.json',
    'common/volume-subtitles.tex',
    'tools/cover-front.tex',
    'tools/cover-back.tex',
    'tools/cover-wrap.tex',
    'tools/cover-colors.tex',
    'tools/cover-template.tex',
    'tools/cover.tex',
    'tools/assets/fonts/CormorantGaramond-Regular.ttf',
    'tools/assets/fonts/CormorantGaramond-Medium.ttf',
    'tools/assets/fonts/CormorantGaramond-MediumItalic.ttf',
    'tools/assets/fonts/CormorantGaramond-SemiBold.ttf',
    'tools/assets/fonts/CormorantGaramond-Bold.ttf',
    'tools/assets/fonts/FiraSans-Light.otf',
    'tools/assets/fonts/OFL-CormorantGaramond.txt',
    'tools/assets/fonts/OFL-FiraSans.txt',
    'tools/assets/print/identity-0.pdf',
    'tools/assets/print/paper-muted.png',
]


def settings():
    """Camera record kept for the retired plate experiments. Live covers do not read it."""
    return json.loads((ROOT / 'tools/assets/series-template.json').read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def catalog():
    return json.loads((ROOT / 'common/series-catalog.json').read_text())['volumes']


def cover_notes():
    return json.loads(NOTES.read_text())


def _front():
    gen = str(ROOT / 'tools/covergen')
    if gen not in sys.path:
        sys.path.insert(0, gen)
    import front
    return front


def about_tex(text):
    return ('% Generated from common/cover-notes.json by tools/series_cover.py.\n'
            '\\backmatter\n\\cleardoublepage\n'
            '\\chapter*{About the Cover}\n'
            '\\addcontentsline{toc}{chapter}{About the Cover}\n'
            '\\noindent ' + text + '\n')


def credits_tex(notes):
    lines = ['% Generated from common/cover-notes.json by tools/series_cover.py.']
    for number, row in notes.items():
        lines.append('\\expandafter\\def\\csname occovercredit@%s\\endcsname{%s}' % (number, row['credit']))
    lines.append('\\newcommand{\\covercredit}{\\ifcsname occovercredit@\\VOLUMENUM\\endcsname'
                 '\\csname occovercredit@\\VOLUMENUM\\endcsname\\par\\fi}')
    return '\n'.join(lines) + '\n'


def notes_markdown(notes):
    lines = ['# About the covers', '',
             'Generated from [`common/cover-notes.json`](../common/cover-notes.json).',
             'The same sentences are the copyright-page credit, the colophon and the library gallery.',
             '']
    titles = catalog()
    for number, row in notes.items():
        lines.append('## Volume %s — %s' % (number, titles[number]['title']))
        lines.append('')
        lines.append(row['credit'])
        lines.append('')
        lines.append(row['about'])
        lines.append('')
    return '\n'.join(lines)


def expected(numbers=None):
    front = _front()
    offsets = front.load_offsets()
    notes = cover_notes()
    books = catalog()
    numbers = [str(n) for n in (numbers or offsets)]
    plates = {}
    for number in numbers:
        motif, lockup = front.plates(number, offsets)
        plates[number] = {
            'stem': books[number]['stem'],
            'motif': motif,
            'lettering': lockup,
            'about': about_tex(notes[number]['about']),
        }
    return plates, credits_tex(notes), notes_markdown(notes)


def manifest_text(plates):
    files = {name: sha(ROOT / name) for name in SHARED}
    artwork = []
    for number, plate in plates.items():
        artwork.append({
            'number': number,
            'book': plate['stem'],
            'motif': plate['stem'] + '/cover-motif.tex',
            'motif_sha256': hashlib.sha256(plate['motif'].encode()).hexdigest(),
            'lettering': plate['stem'] + '/cover-lettering.tex',
            'lettering_sha256': hashlib.sha256(plate['lettering'].encode()).hexdigest(),
            'about': plate['stem'] + '/about-the-cover.tex',
            'about_sha256': hashlib.sha256(plate['about'].encode()).hexdigest(),
        })
    return json.dumps({'schema': 2, 'family': 'cormorant-fira-2026', 'files': files,
                       'artwork': artwork}, indent=2) + '\n'


def generate():
    plates, credits, markdown = expected()
    for plate in plates.values():
        book = ROOT / plate['stem']
        (book / 'cover-motif.tex').write_text(plate['motif'])
        (book / 'cover-lettering.tex').write_text(plate['lettering'])
        (book / 'about-the-cover.tex').write_text(plate['about'])
    CREDITS.write_text(credits)
    NOTES_MD.write_text(markdown)
    MANIFEST.write_text(manifest_text(plates))


def check_sync():
    plates, credits, markdown = expected()
    for number, plate in plates.items():
        book = ROOT / plate['stem']
        for name, text in (('cover-motif.tex', plate['motif']),
                           ('cover-lettering.tex', plate['lettering']),
                           ('about-the-cover.tex', plate['about'])):
            path = book / name
            if not path.exists() or path.read_text() != text:
                got = path.read_text() if path.exists() else ''
                diff = ''.join(difflib.unified_diff(
                    got.splitlines(True), text.splitlines(True),
                    fromfile='committed', tofile='regenerated', n=1))
                import numpy
                raise ValueError(
                    f'Volume {number}: {name} is stale on {platform.platform()} '
                    f'CPython {platform.python_version()} NumPy {numpy.__version__}.\n{diff[:2500]}')
    if not CREDITS.exists() or CREDITS.read_text() != credits:
        raise ValueError('Cover credits are stale; run tools/series_cover.py')
    if not NOTES_MD.exists() or NOTES_MD.read_text() != markdown:
        raise ValueError('Cover notes markdown is stale; run tools/series_cover.py')
    if not MANIFEST.exists() or MANIFEST.read_text() != manifest_text(plates):
        raise ValueError('Cover manifest is stale; run tools/series_cover.py')
    words = {n: len(row['about'].split()) for n, row in cover_notes().items()}
    bad = {n: count for n, count in words.items() if not 80 <= count <= 150}
    if bad:
        raise ValueError(f'Cover notes must be 80 to 150 words: {bad}')


if __name__ == '__main__':
    if '--check' in sys.argv:
        check_sync()
    else:
        generate()
        check_sync()
        print('Cover plates, notes and manifest regenerated.')
