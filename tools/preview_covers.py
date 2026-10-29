"""Render every series front at production sizes without rebuilding the books.

Usage: python3 tools/preview_covers.py [tome1-first-principles tome2-integers] [--jobs 4]
Requires the same xelatex/poppler setup as build.sh. Writes preview PDFs and PNGs,
not release assets or production paperback wraps. Mathematical motifs are read as-is.
"""
import argparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import subprocess
from series_metadata import subtitle, check_sync
from check_cover_pdf import check_cover, check_cover_log
from check_cover_template import check as check_template
from print_layout import LAYOUT, check_sync as check_print_sync

ROOT = Path(__file__).resolve().parent.parent
PRINT = (LAYOUT["trim_width_in"], LAYOUT["trim_height_in"])
FORMATS = {"reference": PRINT, "ebook": (6, 6*PRINT[1]/PRINT[0])}


def render(main: Path, output: Path, print_mode=False) -> str:
    metadata = re.search(r"^% epub-title: (.+)$", main.read_text(), re.M).group(1)
    number = re.search(r"Volume ([0-9A-Z]+):", metadata).group(1)
    title = metadata.split(": ", 1)[1]
    tome = main.parent.name
    out = output / tome
    out.mkdir(parents=True, exist_ok=True)
    environment=os.environ.copy()
    environment.setdefault('extra_mem_top','12000000')  # Match production's dense-vector allowance.
    formats = {"reference": PRINT} if print_mode else FORMATS
    for fmt, (width, height) in formats.items():
        tex = (rf"\def\TOMENUM{{{number}}}\def\TOMETITLE{{{title}}}"
               rf"\def\CW{{{width}}}\def\CH{{{6*height/width}}}\def\MOTIF{{{tome}/cover-motif}}"
               r"\input{tools/cover.tex}")
        if print_mode:
            tex = r"\def\PRINTQUALITY{}" + tex
        with (out / f"{fmt}.stdout").open("w") as log:
            # xsavebox needs one XDV-only pass for references; encode images once.
            for flags in (["-no-pdf"], []):
                subprocess.run(["xelatex", *flags, "-interaction=nonstopmode", "-halt-on-error",
                                f"-output-directory={out}", f"-jobname={fmt}", tex],
                               cwd=ROOT, env=environment, stdout=log, stderr=subprocess.STDOUT, check=True)
        check_cover(out / f"{fmt}.pdf", width, height)
        check_cover_log(out / f"{fmt}.log")
        check_template(out / f"{fmt}.pdf", number)
        text = subprocess.check_output(["pdftotext", str(out / f"{fmt}.pdf"), "-"]).decode()
        text = " ".join(text.split())
        expected_text = (title, subtitle(number), "Discover the patterns. Understand the proofs.")
        for expected in expected_text:
            if expected not in text:
                raise ValueError(f"{tome}/{fmt}: missing or clipped text: {expected}")
    subprocess.run(["pdftoppm", "-singlefile", "-scale-to", "900", "-png",
                    str(out / "reference.pdf"), str(out / "cover")], check=True)
    return tome


def main():
    check_sync()
    check_print_sync()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tomes", nargs="*", help="Only render these volume directories; default: all")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--out", type=Path, default=ROOT / "build/cover-previews")
    parser.add_argument("--print", action="store_true", dest="print_mode",
                        help="Render the print vector master at 7x10, instead of digital fronts")
    args = parser.parse_args()
    books = [ROOT / tome / "main.tex" for tome in args.tomes] if args.tomes else sorted(ROOT.glob("tome*/main.tex"))
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(render, book, args.out.resolve(), args.print_mode) for book in books]
        for future in as_completed(futures):
            print("PASS", future.result(), flush=True)
    print(f"Verified {len(books)} volumes in {1 if args.print_mode else len(FORMATS)} cover sizes.", flush=True)


if __name__ == "__main__":
    main()
