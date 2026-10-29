"""Build local 6x9 and 7x10 print proofs with identical 11pt manuscript settings.

Run with the normal TeX toolchain activated. This does not change production
formats, build paperback wraps, copy to dist/, or publish anything.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from check_cover_pdf import check_fonts
from check_edition_copy import check

ROOT = Path(__file__).resolve().parent.parent


def build(book, size, output):
    metadata = re.search(r'^% epub-title: .*?Volume ([^:]+): (.+)$',
                         (book / 'main.tex').read_text(), re.M)
    if not metadata:
        raise ValueError('Book lacks title metadata')
    number, title = metadata.groups()
    work = output / size
    work.mkdir(parents=True, exist_ok=True)
    command = (rf'\def\VOLUMENUM{{{number}}}\def\VOLUMETITLE{{{title}}}'
               r'\def\FORMAT{print}\def\PRINTINNER{0.75in}')
    if size in {'6x9', '7x10'}:
        # Override geometry at the end of the existing preamble. This preserves
        # print boxes, mirrored margins, chapter openings and the original font.
        geometry = '6in,paperheight=9in' if size == '6x9' else '7in,paperheight=10in'
        command += (r'\RequirePackage{etoolbox}\AtEndPreamble{'
                    r'\geometry{paperwidth=' + geometry + '}' +
                    r'\setlength{\headwidth}{\textwidth}}')
    command += r'\input{main.tex}'
    (work / 'build-command.txt').write_text(command + '\n')
    for iteration in range(1, 4):
        log = work / f'pass-{iteration}.stdout'
        with log.open('w') as stream:
            result = subprocess.run([
                'xelatex', '-interaction=nonstopmode', '-halt-on-error', '-recorder',
                '-output-directory=' + str(work), '-jobname=interior', command],
                cwd=book, stdout=stream, stderr=subprocess.STDOUT,
                env={**os.environ, 'extra_mem_top': '12000000'})
        if result.returncode:
            raise RuntimeError(f'{size}: TeX failed; see {log}')
    filename = f'Mathematical-Maturity-{size}-print.pdf' if number == '0' else f'{book.name}-{size}-print.pdf'
    target = output / filename
    shutil.copy2(work / 'interior.pdf', target)
    check_fonts(target)
    info = subprocess.check_output(['pdfinfo', str(target)], text=True)
    dimensions = re.search(r'Page size:\s+([\d.]+) x ([\d.]+)', info)
    expected = (432, 648) if size == '6x9' else (504, 720)
    if not dimensions or any(abs(float(dimensions[i + 1]) - expected[i]) > .1 for i in range(2)):
        raise ValueError(f'{size}: unexpected PDF dimensions')
    log = (work / 'interior.log').read_text()
    scales = [float(b) / float(a) for a, b in re.findall(r'SHRINK ([\d.]+)pt> ([\d.]+)pt', log)]
    result = dict(trim=size, file=str(target),
                  pages=int(re.search(r'Pages:\s+(\d+)', info)[1]),
                  page_size=' x '.join(dimensions.groups()) + ' pt',
                  overfull=len(re.findall(r'Overfull \\[hv]box', log)),
                  shrunk_displays=len(scales), minimum_display_scale=min(scales, default=1),
                  reference_warnings=len(re.findall('undefined|multiply defined', log)))
    (work / 'summary.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('book', nargs='?', default='volume1-first-principles')
    parser.add_argument('--out', type=Path, default=ROOT / 'build/volume0-print-review')
    args = parser.parse_args()
    book = (ROOT / args.book).resolve()
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    check(book)
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda size: build(book, size, output), ['6x9', '7x10']))
    (output / 'build-summary.json').write_text(json.dumps(results, indent=2) + '\n')


if __name__ == '__main__':
    main()
