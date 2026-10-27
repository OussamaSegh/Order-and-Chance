"""Validate the typeset 7x10 interior's box measurements and TeX diagnostics."""
import argparse
from pathlib import Path
import re


def check(log, measurements):
    log, measurements = Path(log), Path(measurements)
    text = log.read_text(errors='replace')
    if 'Missing character:' in text:
        raise ValueError(f'{log}: missing font glyph; text or mathematics would be lost')
    if re.search(r'Font shape [^\n]*undefined', text):
        raise ValueError(f'{log}: requested font shape is unavailable')
    if re.search(r'Overfull \\vbox|Float too large for page', text):
        raise ValueError(f'{log}: vertical overflow or oversized figure')
    if re.search(r'Overfull \\hbox', text):
        raise ValueError(f'{log}: text protrudes beyond the final book measure')
    if re.search(r'undefined references|multiply defined|Reference .* undefined', text):
        raise ValueError(f'{log}: unresolved or duplicate references')
    rows = measurements.read_text().splitlines()
    if not rows:
        raise ValueError(f'{measurements}: no measured boxes')
    heights = []
    for row in rows:
        match = re.fullmatch(r'BOX\|([^|]+)\|(\d+)\|([\d.]+)pt\|([\d.]+)pt', row)
        if not match:
            raise ValueError(f'{measurements}: malformed box measurement: {row}')
        source, line, height, limit = match.groups()
        height, limit = float(height), float(limit)
        if height > limit:
            raise ValueError(f'{source}:{line}: {height}pt box exceeds {limit}pt text height')
        heights.append(height)
    return len(heights), max(heights)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('log', type=Path)
    parser.add_argument('measurements', type=Path)
    args = parser.parse_args()
    count, maximum = check(args.log, args.measurements)
    print(f'Book layout checked: {count} whole boxes, maximum height {maximum:.1f}pt; no overflow or unresolved references')
