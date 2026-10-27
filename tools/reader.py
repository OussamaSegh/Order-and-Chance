"""Build the online reader of a tome: one HTML page per chapter, for the GitHub Pages site.

Usage: python3 tools/reader.py <tome> <build dir of the tome> <output dir>
Reuses what build.sh made for the EPUB (the flattened LaTeX epub.tex, the SVG figures and the
cover) and the EPUB's pandoc filter, so the numbering and cross-references match the EPUB.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path
from series_metadata import subtitle

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent


def main(tome: str, build: str, out: str) -> None:
    build_dir, out_dir = Path(build).resolve(), Path(out).resolve()
    title = re.search(r"^% epub-title: (.*)$", (ROOT / tome / "main.tex").read_text(encoding="utf-8"), re.M)
    title = title.group(1) if title else tome
    book = title.partition(". ")[2] or title
    shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pandoc", str(build_dir / "epub.tex"), "-f", "latex", "-t", "chunkedhtml", "--katex",
         "--toc", "--toc-depth=2", "--split-level=1", "--number-sections",
         "--lua-filter", str(TOOLS / "epub.lua"), "--template", str(TOOLS / "reader-template.html"),
         "--metadata", "title=" + title, "--metadata", "lang=en",
         "-V", "booktitle=" + book,
         "-V", "volumesubtitle=" + subtitle(re.search(r"Volume ([0-9A-Z]+):", title).group(1)), "-V", "tome=" + tome, "-o", str(out_dir)],
        cwd=ROOT / tome, check=True)
    # Pandoc names the pages of unnumbered chapters "-preface.html", and of chapters with a
    # \label "3-ch:eigen.html"; make plain file names.
    renames = {p.name: p.name.lstrip("-").replace(":", "-") for p in out_dir.glob("*.html")
               if p.name.startswith("-") or ":" in p.name}
    for old, new in renames.items():
        (out_dir / old).rename(out_dir / new)
    # Figures: build.sh made one SVG per figure; copy them, and the portrait JPEGs, next to the pages.
    figdir = out_dir / "figures"
    figdir.mkdir()
    for page in out_dir.glob("*.html"):
        text = page.read_text(encoding="utf-8")
        for old, new in renames.items():
            text = text.replace(f'"{old}', f'"{new}')

        def figure(m):
            src = Path(m.group(1))
            shutil.copy(src, figdir / src.name)
            return f'src="figures/{src.name}"'

        text = re.sub(r'src="(/[^"]*\.(?:svg|jpg))"', figure, text)
        page.write_text(text, encoding="utf-8")
    (out_dir / "sitemap.json").unlink(missing_ok=True)
    shutil.copytree(TOOLS / "assets/fonts", out_dir / "fonts", dirs_exist_ok=True)
    for font in (ROOT / "common/fonts").glob("*.woff2"):
        shutil.copy2(font, out_dir / "fonts" / font.name)
    shutil.copy(TOOLS / "reader.css", out_dir / "reader.css")
    shutil.copy(TOOLS / "reader.js", out_dir / "reader.js")
    number = re.search(r"Volume ([0-9A-Z]+):", title).group(1)
    master = TOOLS / f"assets/approved-volume-{number}.png"
    if master.is_file():
        shutil.copy2(master, out_dir / "cover.png")
    else:
        subprocess.run(["pdftoppm", "-png", "-singlefile", "-scale-to", "960",
                        str(build_dir / "cover.pdf"), str(out_dir / "cover")], check=True)



if __name__ == "__main__":
    main(*sys.argv[1:4])
