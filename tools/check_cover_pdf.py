"""Verify a cover PDF's physical size and embedded vector fonts before publishing."""
import argparse
import re
import subprocess
from pathlib import Path
from print_layout import LAYOUT
from series_metadata import subtitle

def check_cover(path, width, height):
    path=Path(path)
    info=subprocess.check_output(['pdfinfo',str(path)],text=True)
    dimensions=re.search(r'Page size:\s+([\d.]+) x ([\d.]+)',info)
    pages=re.search(r'Pages:\s+(\d+)',info)
    if not pages or int(pages[1])!=1 or not dimensions:
        raise ValueError(f'{path}: expected one cover page with a known page size')
    if abs(float(dimensions[1])-width*72)>.12 or abs(float(dimensions[2])-height*72)>.12:
        raise ValueError(f'{path}: incorrect physical dimensions: {dimensions.groups()}')
    check_fonts(path)

def check_cover_copy(path, title, number, print_export=False):
    """Check the front region alone so back/spine text cannot mask clipping."""
    # Cover width minus front trim and outer bleed gives the actual front origin.
    info = subprocess.check_output(['pdfinfo', str(path)], text=True)
    width = float(re.search(r'Page size:\s+([\d.]+)', info)[1])
    x = width - (LAYOUT['trim_width_in'] + LAYOUT['bleed_in']) * 72
    text = subprocess.check_output(['pdftotext', '-x', str(round(x)), '-y', str(round(LAYOUT['bleed_in']*72)),
        '-W', str(round(LAYOUT['trim_width_in']*72)), '-H', str(round(LAYOUT['trim_height_in']*72)),
        str(path), '-'], text=True)
    text = ' '.join(text.split())
    expected_copy = [title, subtitle(number)]
    # The press export removes invisible searchable duplicates of the traced
    # identity. Its visible slogan is verified by source provenance and render
    # comparison in check_print_cover, rather than requiring invisible text.
    if not print_export:
        expected_copy.append('The Hidden Architecture of Mathematics')
    for expected in expected_copy:
        if expected not in text:
            raise ValueError(f'{path}: incomplete front-panel text: {expected}')

def check_fonts(path):
    path=Path(path)
    fonts=subprocess.check_output(['pdffonts',str(path)],text=True)
    for row in fonts.splitlines()[2:]:
        if 'Type 3' in row:
            raise ValueError(f'{path}: bitmap/Type 3 cover font: {row.strip()}')
        flags=re.search(r'\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$',row)
        if flags and flags[1]!='yes':
            raise ValueError(f'{path}: unembedded cover font: {row.strip()}')

def check_cover_log(path):
    text=Path(path).read_text(errors='replace')
    if ('Missing character:' in text or 'Some font shapes were not available' in text
            or re.search(r'Font shape [^\n]*undefined|Overfull \\hbox',text)):
        raise ValueError(f'{path}: missing cover glyph, substituted font or text overflow')

def check_back_copy(path):
    text=subprocess.check_output(['pdftotext','-x','9','-y','9','-W','504','-H','720',str(path),'-'],text=True)
    if len(text.split())<60:
        raise ValueError(f'{path}: back-cover blurb is missing or incomplete')

def check_interior(path):
    """Check every page, including title pages and inserted figures."""
    info = subprocess.check_output(['pdfinfo', str(path)], text=True)
    pages = int(re.search(r'Pages:\s+(\d+)', info)[1])
    details = subprocess.check_output(['pdfinfo', '-f', '1', '-l', str(pages), str(path)], text=True)
    sizes = re.findall(r'Page\s+\d+ size:\s+([\d.]+) x ([\d.]+)', details)
    if len(sizes) != pages:
        raise ValueError(f'{path}: cannot verify every interior page')
    for number, (width, height) in enumerate(sizes, 1):
        if (abs(float(width)-LAYOUT['trim_width_in']*72) > .12 or
                abs(float(height)-LAYOUT['trim_height_in']*72) > .12):
            raise ValueError(f'{path}: page {number} is not the approved paperback trim')
    check_fonts(path)
    return pages

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',nargs='?')
    parser.add_argument('--log',type=Path,help='Reject missing glyphs, font substitutions and overflow')
    parser.add_argument('--spine',type=float,help='Paperback spine width in inches; otherwise check a 6-inch front')
    parser.add_argument('--height',type=float)
    parser.add_argument('--title', help='Verify complete paperback front title/subtitle/slogan')
    parser.add_argument('--number', help='Volume identifier for subtitle lookup')
    parser.add_argument('--interior',action='store_true',help='Check every interior page size and embedded vector fonts')
    parser.add_argument('--print-export',action='store_true',help='Identity is validated by press-export provenance/visual comparison')
    args=parser.parse_args()
    if args.log:check_cover_log(args.log)
    if not args.pdf:
        if not args.log:parser.error('Supply a PDF or --log')
        raise SystemExit(0)
    if args.interior:
        check_interior(args.pdf)
    else:
        check_cover(args.pdf,2*LAYOUT['trim_width_in']+2*LAYOUT['bleed_in']+args.spine if args.spine is not None else 6,
                    args.height or (LAYOUT['trim_height_in']+2*LAYOUT['bleed_in'] if args.spine is not None else 6*LAYOUT['trim_height_in']/LAYOUT['trim_width_in']))

    if args.title:
        if not args.number or args.spine is None:
            parser.error('--title requires --number and --spine')
        check_cover_copy(args.pdf, args.title, args.number, args.print_export)
