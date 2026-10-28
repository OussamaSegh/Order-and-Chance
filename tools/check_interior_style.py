"""Reject a print interior that loses the approved fonts or colour accents."""
import argparse
from pathlib import Path
import re
import subprocess

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent


def check(path):
    fonts = subprocess.check_output(['pdffonts', str(path)], text=True)
    for family in ('STIXTwoText', 'STIXTwoMath', 'Inter-'):
        if family not in fonts:
            raise ValueError(f'{path}: missing interior font family {family}')
    palette = dict(re.findall(r'\\definecolor\{([^}]+)\}\{HTML\}\{([0-9A-Fa-f]{6})\}',
                              (ROOT / 'common/design-colors.tex').read_text()))
    wanted = {name: tuple(int(palette[name][i:i + 2], 16) / 255 for i in (0, 2, 4))
              for name in ('ocCoralDeep', 'ocInk')}
    pattern = rb'([0-9.]+)\s+([0-9.]+)\s+([0-9.]+)\s+(?:rg|RG)\b'
    found = set()
    for page in PdfReader(path).pages:
        contents = page.get_contents()
        if contents is None:
            continue
        for values in re.findall(pattern, contents.get_data()):
            rgb = tuple(float(value) for value in values)
            found.update(name for name, expected in wanted.items()
                         if all(abs(a - b) < .003 for a, b in zip(rgb, expected)))
        if found == set(wanted):
            return
    raise ValueError(f'{path}: missing colour accents: {", ".join(sorted(set(wanted) - found))}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    args = parser.parse_args()
    check(args.pdf)
    print('Interior style checked: STIX Two text/math, cover Inter headings, charcoal and coral accents')
