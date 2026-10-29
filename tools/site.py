"""Build the download page published on GitHub Pages.

Usage: python3 tools/site.py <dist dir> <output dir>
Copies each standard 7 x 10 reading PDF and EPUB with readable filenames into the
output directory, the online reader dist/html/<volume>/ into read/<volume>/, and writes index.html.
Each volume's card also links its Amazon KDP files from dist/kdp/: the Kindle cover, the paperback
cover, print interior and listing. The download PDF includes its front cover.
"""
import datetime
import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from series_metadata import part_of, subtitle
from print_layout import LAYOUT
from book_outputs import clean
from legacy_urls import OLD_PREFIX, OLD_STEMS, redirect_html
from public_names import filename
from urllib.parse import quote

PRINT_TRIM = f"{LAYOUT['trim_width_in']} × {LAYOUT['trim_height_in']} in"

ROOT = Path(__file__).resolve().parent.parent

PAGE = (Path(__file__).with_name("site-template.html").read_text(encoding="utf-8")
        .replace("{", "{{").replace("}", "}}"))
for field in ("volumes", "count", "repo", "date", "commit", "trim"):
    PAGE = PAGE.replace("{{" + field + "}}", "{" + field + "}")

CARD = """<article class="volume" data-collection="{collection}" data-part="{part}" data-search="{search}">{cover}
<div class="info"><p class="eyebrow">{collection_label}</p><h3>{title}</h3><p class="volume-subtitle">{subtitle}</p><p class="meta">{size} · {trim} PDF with cover</p></div>
<div class="links"><a class="primary" href="{pdf}" download>PDF with cover</a>{print_pdf}{read}{epub}</div>{kdp}</article>"""

# Amazon KDP files made by build.sh in dist/kdp/: (suffix, label, tooltip).
KDP = [("ebook", "Kindle cover", "Front cover, 1792 x 2560 JPEG, for a Kindle eBook"),
       ("wrap", "Paperback cover", f"Back, spine and front with bleed, for a {PRINT_TRIM} paperback"),
       ("listing", "Description and keywords", "Title fields, description and keywords for the KDP form")]


def write_reader_redirects(read_root: Path, new_stem: str) -> None:
    """Mirror each new reader page at the published URL that used the old stem."""
    old_stem = next((old for old, new in OLD_STEMS.items() if new == new_stem), None)
    new_root = read_root / new_stem
    if old_stem is None or not (new_root / "index.html").is_file():
        return
    old_root = read_root / old_stem
    for page in new_root.rglob("*.html"):
        rel = page.relative_to(new_root)
        dest = old_root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        target = "../" * len(rel.parts) + f"{new_stem}/{rel.as_posix()}"
        dest.write_text(redirect_html(target), encoding="utf-8")


def volume_order(pdf: Path):
    """Main sequence by number, followed by the problem book."""
    m = re.match(r"volume([A-Z]?)(\d+)", pdf.stem)
    return (1 if m and m.group(1) == "P" else 0, int(m.group(2)) if m else 0)


def main(dist: str, out: str) -> None:
    dist_dir, out_dir = Path(dist), Path(out)
    out_dir.mkdir(parents=True, exist_ok=True)
    assets = Path(__file__).resolve().parent / "assets"
    shutil.copytree(assets / "fonts", out_dir / "fonts", dirs_exist_ok=True)
    shutil.copy2(assets / "approved-charcoal-paper.png", out_dir / "paper.png")
    clean(out_dir)
    for pattern in ["Volume *", "Problem Book *", "volume*", OLD_PREFIX + "*"]:
        for path in out_dir.glob(pattern):
            if path.is_file():
                path.unlink()
    current = {p.parent.name for p in ROOT.glob("volume*/main.tex")}
    read_root = out_dir / "read"
    for path in list(read_root.glob("volume*")) + list(read_root.glob(OLD_PREFIX + "*")):
        if path.is_dir() and path.name not in current:
            shutil.rmtree(path)
    cards = []
    current_part = None
    for source in sorted(ROOT.glob("volume*/main.tex"), key=lambda p: volume_order(p.parent)):
        volume = source.parent.name
        pdf = dist_dir / filename(volume, "pdf", ROOT)
        if not pdf.exists():
            continue
        if not (ROOT / volume / "main.tex").is_file():
            continue
        epub = pdf.with_suffix(".epub")
        main_tex = ROOT / volume / "main.tex"
        title = volume
        if main_tex.exists():
            m = re.search(r"^% epub-title: (.*)$", main_tex.read_text(encoding="utf-8"), re.M)
            if m:
                title = m.group(1)
        series, _, rest = title.partition(". ")
        number_match = re.search(r"Volume ([0-9]+):", title)
        number = number_match.group(1) if number_match else ""
        try:
            part = part_of(number) if number else {"roman": "", "name": ""}
        except KeyError:
            part = {"roman": "", "name": ""}
        if part["roman"] and part["roman"] != current_part:
            current_part = part["roman"]
            cards.append(
                f'<h3 class="series-part" data-part="{html.escape(part["roman"])}">'
                f'Part {html.escape(part["roman"])} · {html.escape(part["name"])}</h3>')
        shutil.copy(pdf, out_dir / pdf.name)
        if epub.exists():
            shutil.copy(epub, out_dir / epub.name)
        read = ""
        reader = dist_dir / "html" / volume
        if (reader / "index.html").exists():
            shutil.copytree(reader, out_dir / "read" / volume, dirs_exist_ok=True)
            write_reader_redirects(out_dir / "read", volume)
            read = f'<a class="read" href="read/{volume}/" title="Read in the browser, one page per chapter">Read online</a>'
        print_pdf = ""
        print_file = dist_dir / "kdp" / filename(volume, "print", ROOT)
        if print_file.exists():
            shutil.copy(print_file, out_dir / print_file.name)
            print_pdf = f'<a href="{quote(print_file.name)}" download title="Paperback interior without the front cover">Print PDF</a>'
        kdp = []
        for suffix, label, tip in KDP:
            src = dist_dir / "kdp" / filename(volume, suffix, ROOT)
            if src.exists():
                # The listing is served as plain text, so that browsers show it instead of downloading it.
                name = src.name.replace(".md", ".txt")
                shutil.copy(src, out_dir / name)
                kdp.append(f'<a href="{quote(name)}" title="{tip}">{label}</a>')
        kdp = f'<details class="kdp"><summary>Paperback &amp; publishing files</summary>{"".join(kdp)}</details>' if kdp else ""
        size = f"{pdf.stat().st_size / 1e6:.1f} MB"
        # Cover thumbnail, rendered from the cover page that build.sh made.
        cover = '<div class="cover placeholder" aria-hidden="true">∑</div>'
        cover_pdf = ROOT / "build" / volume / "cover.pdf"
        if cover_pdf.exists():
            subprocess.run(["pdftoppm", "-png", "-singlefile", "-scale-to", "480",
                            str(cover_pdf), str(out_dir / filename(volume, "thumbnail", ROOT)[:-4])], check=True)
            cover = f'<img class="cover" width="336" height="480" loading="lazy" src="{quote(filename(volume, "thumbnail", ROOT))}" alt="Cover of {html.escape(rest or series)}">'
        collection, label = ("main", f"Part {part['roman']}" if part["roman"] else "Main series")
        epub_link = f'<a href="{quote(epub.name)}" download>EPUB</a>' if epub.exists() else ""
        number = re.search(r"Volume ([0-9A-Z]+):", title)
        tagline = subtitle(number.group(1)) if number else ""
        cards.append(CARD.format(subtitle=html.escape(tagline), title=html.escape(rest or series), size=size, trim=PRINT_TRIM, cover=cover, read=read,
                                 pdf=quote(pdf.name), print_pdf=print_pdf, epub=epub_link, kdp=kdp,
                                 collection=collection, collection_label=label, part=html.escape(part["roman"]),
                                 search=html.escape((volume + " " + title + " " + tagline + " " + label + " " + part["name"]).lower(), quote=True)))
    sha = os.environ.get("GITHUB_SHA", "")
    commit = f" (commit {sha[:7]})" if sha else ""
    repo = os.environ.get("GITHUB_REPOSITORY", "OussamaSegh/Order-and-Chance")
    (out_dir / "index.html").write_text(
        PAGE.format(volumes="\n".join(cards), count=len(cards), trim=PRINT_TRIM, repo=html.escape(repo, quote=True), date=datetime.date.today().isoformat(), commit=commit),
        encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
