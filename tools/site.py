"""Build the download page published on GitHub Pages.

Usage: python3 tools/site.py <dist dir> <output dir>
Copies every dist/<tome>.pdf (with its -kindle variant) and .epub into the
output directory, the online reader dist/html/<tome>/ into read/<tome>/, and writes index.html.
Each tome's card also links its Amazon KDP files from dist/kdp/: the Kindle cover, the paperback
cover, the paperback interior and the listing.
"""
import datetime
import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Order and Chance</title>
<style>
  :root {{ --ink:#1d1d1f; --muted:#5f6368; --line:#e3e0d8; --bg:#fbfaf6; --card:#fff; --accent:#1f4e79; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --ink:#ecebe6; --muted:#a8a6a0; --line:#34332f; --bg:#171716; --card:#202020; --accent:#8ab4e8; }}
  }}
  body {{ margin:0; background:var(--bg); color:var(--ink); font:17px/1.6 Georgia, "Palatino Linotype", serif; }}
  main {{ max-width:760px; margin:0 auto; padding:48px 16px 64px; }}
  h1 {{ font-size:2.1em; margin:0 0 .2em; }}
  .subtitle {{ font-style:italic; margin:0 0 1.2em; }}
  .lead {{ color:var(--muted); margin:0 0 2em; }}
  .tome {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px 20px; margin:14px 0;
          display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:12px; }}
  .tome img {{ width:96px; height:154px; border-radius:3px; box-shadow:0 2px 8px rgba(0,0,0,.25); }}
  .tome .info {{ flex:1; min-width:180px; }}
  .tome h2 {{ font-size:1.15em; margin:0; }}
  .tome p {{ margin:2px 0 0; color:var(--muted); font-size:.92em; }}
  .links a {{ display:inline-block; margin:4px 0 4px 8px; padding:6px 14px; border:1px solid var(--accent); border-radius:6px;
             color:var(--accent); text-decoration:none; font-family:system-ui, sans-serif; font-size:.9em; }}
  .kdp {{ flex-basis:100%; font-family:system-ui, sans-serif; font-size:.82em; color:var(--muted); }}
  .kdp a {{ color:var(--accent); margin-left:10px; }}
  .links a:hover, .links a.read {{ background:var(--accent); color:var(--card); }}
  footer {{ margin-top:2.5em; color:var(--muted); font-size:.88em; }}
  footer a {{ color:var(--accent); }}
</style>
</head>
<body>
<main>
<h1>Order and Chance</h1>
<p class="subtitle">Beautiful mathematics through problems and proofs<br>by SEGHAIER Oussama</p>
<p class="lead">A series of books of beautiful mathematics, written for pleasure, from a refresher of undergraduate mathematics
toward research in probability, probabilistic number theory and algebra. Every statement is proved, and every exercise
has a solution that explains how to find it.</p>
{tomes}
<footer>Built automatically from the
<a href="https://github.com/{repo}">source repository</a> on {date}{commit}.
Python companion notebooks are in the repository's <code>python/</code> folder.</footer>
</main>
</body>
</html>
"""

CARD = """<div class="tome">{cover}<div class="info"><h2>{title}</h2><p>{subtitle} · {size}</p></div>
<div class="links">{read}<a href="{pdf}" title="A4 pages, for a computer, tablet or printing">PDF</a>{variants}<a href="{epub}">EPUB</a></div>
{kdp}</div>"""

# Amazon KDP files made by build.sh in dist/kdp/: (suffix, label, tooltip).
KDP = [("ebook-cover.jpg", "Kindle cover", "Front cover, 1600 x 2560 JPEG, for a Kindle eBook"),
       ("cover-wrap.pdf", "Paperback cover", "Back, spine and front with bleed, for a 6 x 9 in paperback"),
       ("print.pdf", "Paperback interior", "6 x 9 in pages for printing on demand"),
       ("listing.md", "Description and keywords", "Title fields, description and keywords for the KDP form")]

# Extra PDF layouts made by build.sh, with their button labels.
VARIANTS = [("kindle", "Kindle PDF", "Pages sized for a 7-inch e-reader (Kindle Paperwhite)")]


def tome_order(pdf: Path):
    """Main line by number (tome0..tome15), then the Computing track C1..C5, then S1..S4."""
    m = re.match(r"tome([A-Z]?)(\d+)", pdf.stem)
    return ("", "C", "S").index(m.group(1)) if m and m.group(1) in "CS" else 3, int(m.group(2)) if m else 0


def main(dist: str, out: str) -> None:
    dist_dir, out_dir = Path(dist), Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)
    cards = []
    for pdf in sorted(dist_dir.glob("*.pdf"), key=tome_order):
        if pdf.stem.endswith("-phone") or any(pdf.stem.endswith("-" + v) for v, _, _ in VARIANTS):
            continue
        tome = pdf.stem
        epub = pdf.with_suffix(".epub")
        main_tex = ROOT / tome / "main.tex"
        title = tome
        if main_tex.exists():
            m = re.search(r"^% epub-title: (.*)$", main_tex.read_text(encoding="utf-8"), re.M)
            if m:
                title = m.group(1)
        series, _, rest = title.partition(". ")
        shutil.copy(pdf, out_dir / pdf.name)
        variants = ""
        for v, label, tip in VARIANTS:
            extra = dist_dir / f"{tome}-{v}.pdf"
            if extra.exists():
                shutil.copy(extra, out_dir / extra.name)
                variants += f'<a href="{extra.name}" title="{tip}">{label}</a>'
        if epub.exists():
            shutil.copy(epub, out_dir / epub.name)
        read = ""
        reader = dist_dir / "html" / tome
        if (reader / "index.html").exists():
            shutil.copytree(reader, out_dir / "read" / tome, dirs_exist_ok=True)
            read = f'<a class="read" href="read/{tome}/" title="Read in the browser, one page per chapter">Read online</a>'
        kdp = []
        for suffix, label, tip in KDP:
            src = dist_dir / "kdp" / f"{tome}-{suffix}"
            if src.exists():
                # The listing is served as plain text, so that browsers show it instead of downloading it.
                name = src.name.replace(".md", ".txt")
                shutil.copy(src, out_dir / name)
                kdp.append(f'<a href="{name}" title="{tip}">{label}</a>')
        kdp = f'<div class="kdp">For Amazon KDP:{"".join(kdp)}</div>' if kdp else ""
        size = f"{pdf.stat().st_size / 1e6:.1f} MB PDF"
        # Cover thumbnail, rendered from the cover page that build.sh made.
        cover = ""
        cover_pdf = ROOT / "build" / tome / "cover.pdf"
        if cover_pdf.exists():
            subprocess.run(["pdftoppm", "-png", "-singlefile", "-scale-to-x", "300", "-scale-to-y", "480",
                            str(cover_pdf), str(out_dir / f"{tome}-cover")], check=True)
            cover = f'<img src="{tome}-cover.png" alt="Cover of {html.escape(rest or series)}">'
        cards.append(CARD.format(title=html.escape(rest or series), subtitle=html.escape(series if rest else ""),
                                 size=size, cover=cover, read=read, pdf=pdf.name, variants=variants, epub=epub.name,
                                 kdp=kdp))
    sha = os.environ.get("GITHUB_SHA", "")
    commit = f" (commit {sha[:7]})" if sha else ""
    repo = os.environ.get("GITHUB_REPOSITORY", "OussamaSegh/Order-and-Chance")
    (out_dir / "index.html").write_text(
        PAGE.format(tomes="\n".join(cards), repo=repo, date=datetime.date.today().isoformat(), commit=commit),
        encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
