"""Render a volume's cover illustration for the chapter openers of the EPUB and online reader.

Usage: python3 tools/opener_motif.py <volume> <figure dir>
Writes <figure dir>/opener-motif.png: the illustration of <volume>/cover-motif.tex in the
opener's 4.76 x 3.46 in viewport (tools/opener-motif.tex), 960 px wide, transparent so the
charcoal opener panel shows through, reduced to a 128-colour palette (about 100 KB).
tools/epub_prep.py hands it to tools/epub.lua, which puts it under every chapter title.
Design 5e (docs/design/interior.md); the PDF draws the same motif in common/chapter-opener.tex.
A volume without cover-motif.tex gets no motif.
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent


def main(volume: str, figdir: str) -> None:
    out = Path(figdir).resolve()
    target = out / "opener-motif.png"
    target.unlink(missing_ok=True)
    if not (ROOT / volume / "cover-motif.tex").is_file():
        return
    out.mkdir(parents=True, exist_ok=True)
    job = "opener-motif"
    log = out / f"{job}.out"
    with log.open("w") as stdout:
        done = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"-output-directory={out}",
             f"-jobname={job}", f"\\def\\MOTIF{{{volume}/cover-motif}}\\input{{tools/opener-motif.tex}}"],
            cwd=ROOT, stdout=stdout, stderr=subprocess.STDOUT)
    if done.returncode:
        sys.exit(log.read_text(errors="replace")[-3000:])
    subprocess.run(["pdftocairo", "-png", "-transp", "-f", "1", "-l", "1", "-singlefile",
                    "-scale-to-x", "960", "-scale-to-y", "-1", str(out / f"{job}.pdf"), str(out / f"{job}-full")],
                   check=True)
    full = out / f"{job}-full.png"
    image = Image.open(full).convert("RGBA")
    image.quantize(colors=128, method=Image.Quantize.FASTOCTREE).save(target, optimize=True)
    full.unlink()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
