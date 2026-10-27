"""Render every series front at production sizes without rebuilding the books.

Usage: python3 tools/preview_covers.py [tome0-mathematical-maturity tome1-integers] [--jobs 4]
Requires the same pdflatex/poppler setup as build.sh. Writes preview PDFs and PNGs,
not release assets or production paperback wraps. Mathematical motifs are read as-is.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import subprocess
from series_metadata import subtitle, check_sync

ROOT = Path(__file__).resolve().parent.parent
FORMATS = {"reference": 9, "ebook": 9.6, "a4": 8.4857, "kindle": 7.9626, "print-front": 9}


def render(main: Path, output: Path) -> str:
    metadata = re.search(r"^% epub-title: (.+)$", main.read_text(), re.M).group(1)
    number = re.search(r"Tome ([0-9A-Z]+):", metadata).group(1)
    title = metadata.split(": ", 1)[1]
    tome = main.parent.name
    out = output / tome
    out.mkdir(parents=True, exist_ok=True)
    for fmt, height in FORMATS.items():
        tex = (rf"\def\TOMENUM{{{number}}}\def\TOMETITLE{{{title}}}"
               rf"\def\CH{{{height}}}\def\MOTIF{{{tome}/cover-motif}}"
               r"\input{tools/cover.tex}")
        with (out / f"{fmt}.stdout").open("w") as log:
            subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                            f"-output-directory={out}", f"-jobname={fmt}", tex],
                           cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tomes", nargs="*", help="Only render these volume directories; default: all")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--out", type=Path, default=ROOT / "build/cover-previews")
    args = parser.parse_args()
    books = [ROOT / tome / "main.tex" for tome in args.tomes] if args.tomes else sorted(ROOT.glob("tome*/main.tex"))
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(render, book, args.out.resolve()) for book in books]
        for future in as_completed(futures):
            print("PASS", future.result(), flush=True)
    print(f"Verified {len(books)} volumes in {len(FORMATS)} cover sizes.", flush=True)


if __name__ == "__main__":
    main()
