"""Verify a cover PDF's physical size and embedded vector fonts before publishing."""
import argparse
import re
import subprocess
from pathlib import Path

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

def check_fonts(path):
    path=Path(path)
    fonts=subprocess.check_output(['pdffonts',str(path)],text=True)
    for row in fonts.splitlines()[2:]:
        if 'Type 3' in row:
            raise ValueError(f'{path}: bitmap/Type 3 cover font: {row.strip()}')
        flags=re.search(r'\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$',row)
        if flags and flags[1]!='yes':
            raise ValueError(f'{path}: unembedded cover font: {row.strip()}')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf')
    parser.add_argument('--spine',type=float,help='Paperback spine width in inches; otherwise check a 6-inch front')
    parser.add_argument('--height',type=float)
    parser.add_argument('--interior',action='store_true',help='Check embedded vector fonts in a multi-page interior')
    args=parser.parse_args()
    if args.interior:
        check_fonts(args.pdf)
    else:
        check_cover(args.pdf,12.25+args.spine if args.spine is not None else 6,
                    args.height or (9.25 if args.spine is not None else 9.6))
