"""Build the download page published on GitHub Pages.

Usage: python3 tools/site.py <dist dir> <output dir>
Copies every dist/<tome>.pdf and .epub into the output directory and writes index.html.
"""
import datetime
import html
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Numbers, Structures and Chance</title>
<style>
  :root {{ --ink:#1d1d1f; --muted:#5f6368; --line:#e3e0d8; --bg:#fbfaf6; --card:#fff; --accent:#1f4e79; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --ink:#ecebe6; --muted:#a8a6a0; --line:#34332f; --bg:#171716; --card:#202020; --accent:#8ab4e8; }}
  }}
  body {{ margin:0; background:var(--bg); color:var(--ink); font:17px/1.6 Georgia, "Palatino Linotype", serif; }}
  main {{ max-width:760px; margin:0 auto; padding:48px 16px 64px; }}
  h1 {{ font-size:2.1em; margin:0 0 .2em; }}
  .lead {{ color:var(--muted); margin:0 0 2em; }}
  .tome {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px 20px; margin:14px 0;
          display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:12px; }}
  .tome h2 {{ font-size:1.15em; margin:0; }}
  .tome p {{ margin:2px 0 0; color:var(--muted); font-size:.92em; }}
  .links a {{ display:inline-block; margin-left:8px; padding:6px 14px; border:1px solid var(--accent); border-radius:6px;
             color:var(--accent); text-decoration:none; font-family:system-ui, sans-serif; font-size:.9em; }}
  .links a:hover {{ background:var(--accent); color:var(--card); }}
  footer {{ margin-top:2.5em; color:var(--muted); font-size:.88em; }}
  footer a {{ color:var(--accent); }}
</style>
</head>
<body>
<main>
<h1>Numbers, Structures and Chance</h1>
<p class="lead">A series of books of beautiful mathematics, written for pleasure, from a refresher of prépa mathematics
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

CARD = """<div class="tome"><div><h2>{title}</h2><p>{subtitle} · {size}</p></div>
<div class="links"><a href="{pdf}">PDF</a><a href="{epub}">EPUB</a></div></div>"""


def main(dist: str, out: str) -> None:
    dist_dir, out_dir = Path(dist), Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)
    cards = []
    for pdf in sorted(dist_dir.glob("*.pdf")):
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
        if epub.exists():
            shutil.copy(epub, out_dir / epub.name)
        size = f"{pdf.stat().st_size / 1e6:.1f} MB PDF"
        cards.append(CARD.format(title=html.escape(rest or series), subtitle=html.escape(series if rest else ""),
                                 size=size, pdf=pdf.name, epub=epub.name))
    sha = os.environ.get("GITHUB_SHA", "")
    commit = f" (commit {sha[:7]})" if sha else ""
    repo = os.environ.get("GITHUB_REPOSITORY", "OussamaSegh/numbers-structures-chance")
    (out_dir / "index.html").write_text(
        PAGE.format(tomes="\n".join(cards), repo=repo, date=datetime.date.today().isoformat(), commit=commit),
        encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
