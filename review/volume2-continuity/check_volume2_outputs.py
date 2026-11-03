#!/usr/bin/env python3
"""Independent cross-format Volume 2 QA, after ./build.sh volume2-integers.

Requires Python standard library and Poppler (pdfinfo/pdftotext).
The checks complement rendered visual and publisher-side proofing.
"""
import json
import posixpath
import re
import subprocess
import sys
import zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
STEM = "Volume 2 - The Integers"
ISBN = "9798167208650"


def check(condition, reason):
    if not condition:
        raise AssertionError(reason)


def pdfinfo(path):
    raw = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return {k.strip(): v.strip() for k, v in
            (line.split(":", 1) for line in raw.splitlines() if ":" in line)}


def pdftotext(path):
    return subprocess.check_output(["pdftotext", "-layout", str(path), "-"],
                                   text=True)


class LinkReader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.classes = Counter()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for cl in attrs.get("class", "").split():
            self.classes[cl] += 1
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


def run(root=ROOT):
    dist = root / "dist"
    kdp = dist / "kdp"
    reading = dist / (STEM + ".pdf")
    interior = kdp / (STEM + " - Print.pdf")
    wrap = kdp / (STEM + " - Paperback Cover.pdf")
    meta = json.loads((kdp / (STEM + " - Print Metadata.json")).read_text())
    read_info, print_info, cover_info = [pdfinfo(p) for p in
                                        (reading, interior, wrap)]
    read_pages = int(read_info["Pages"])
    interior_pages = int(print_info["Pages"])
    check(read_pages == interior_pages + 1,
          "The reading PDF should add exactly one cover page")
    check(interior_pages == meta["interior_pages"],
          "Print PDF and publishing metadata disagree on page count")
    check(meta["kdp_pages"] == interior_pages + interior_pages % 2,
          "KDP counted pages must include an even-count padding page")
    # The canonical print specification retains four decimal places (not three).
    # A one-decimal-place mismatch in mils rejects a correct 315-page wrap.
    check(meta["spine_in"] ==
          round(meta["kdp_pages"] * meta["spine_in_per_page"], 4),
          "Spine is inconsistent with the KDP page count and selected stock")
    check(print_info["Page size"].startswith("504 x 720"),
          "Print interior must be 7 by 10 inches")
    check(int(cover_info["Pages"]) == 1, "Print wrap must be one PDF page")
    size = re.search(r"Page size:\s*([\d.]+) x ([\d.]+)",
                     subprocess.check_output(["pdfinfo", str(wrap)], text=True))
    check(size is not None, "No cover dimensions")
    check(abs(float(size.group(1))/72 - meta["wrap_width_in"]) < 0.001 and
          abs(float(size.group(2))/72 - meta["wrap_height_in"]) < 0.001,
          "Cover dimensions do not match spine and bleed metadata")
    check(re.search(r"ISBN\s*979\s*[- ]?\s*8167208650", pdftotext(wrap)),
          "Full printed ISBN missing from paperback cover")
    text = pdftotext(reading)
    check(ISBN in text, "Paperback ISBN missing from copyright page")
    chapters = [int("".join(m.group(1).split()))
                for line in text.splitlines()
                if (m := re.match(r"^ *C H A PT E R ([0-9 ]+) *$", line))]
    check(chapters == list(range(1, 12)),
          f"Wrong physical chapter order: {chapters}")
    preflight = json.loads((root / "build/volume2-integers/cover-preflight.json").read_text())
    check(preflight.get("embedded_fonts") is True and
          preflight.get("vector_lettering") is True and
          preflight.get("exact_art_pixels_and_placement") is True,
          "Cover preflight did not retain font, vector and image integrity")

    with zipfile.ZipFile(dist / (STEM + ".epub")) as z:
        names = set(z.namelist())
        check(z.infolist()[0].filename == "mimetype" and
              z.infolist()[0].compress_type == zipfile.ZIP_STORED and
              z.read("mimetype") == b"application/epub+zip",
              "EPUB container/OCF header invalid")
        check(z.testzip() is None, "Damaged ZIP member in EPUB")
        opf = ET.fromstring(z.read("EPUB/content.opf"))
        manifest = [el.get("href") for el in opf.iter()
                    if el.tag.endswith("}item") and el.get("href")]
        check(all("EPUB/" + href.split("#")[0] in names
                  for href in manifest), "Missing EPUB OPF asset")
        nav = ET.fromstring(z.read("EPUB/nav.xhtml"))
        headings = [" ".join("".join(el.itertext()).split()) for el in nav.iter()
                    if el.tag.endswith("}a")]
        nav_chapters = [h for h in headings if re.match(r"^\d+\s", h)]
        check([int(re.match(r"^(\d+)", h).group(1)) for h in nav_chapters]
              == list(range(1, 12)), "EPUB navigation chapter order is wrong")
        xml = {p: ET.fromstring(z.read(p)) for p in names
               if p.endswith(".xhtml")}
        anchors = {p: {x.get("id") for x in tree.iter() if x.get("id")}
                   for p, tree in xml.items()}
        epub_counts = Counter()
        epub_links = 0
        for path, tree in xml.items():
            for el in tree.iter():
                for cls in el.get("class", "").split():
                    if cls in ("exercise", "hint", "solution"):
                        epub_counts[cls] += 1
                if el.tag.endswith("}img"):
                    check(el.get("alt") is not None, f"Missing EPUB image alt in {path}")
                for attr in ("href", "src"):
                    u = el.get(attr)
                    if not u or u.startswith(("http:", "https:", "mailto:",
                                               "data:", "javascript:")):
                        continue
                    link = urlsplit(u)
                    dest = posixpath.normpath(posixpath.join(
                        posixpath.dirname(path), unquote(link.path))) if link.path else path
                    check(dest in names, f"Broken EPUB file: {path} -> {u}")
                    if link.fragment and dest in anchors:
                        check(unquote(link.fragment) in anchors[dest],
                              f"Broken EPUB anchor: {path} -> {u}")
                    epub_links += 1
        check(all(epub_counts[k] == 144 for k in
                  ("exercise", "hint", "solution")),
              f"EPUB lost exercises or their hints/solutions: {epub_counts}")

    html = dist / "html/volume2-integers"
    chapter_html = [p for p in html.glob("*.html") if p.name[:1].isdigit()]
    check(len(chapter_html) == 11, "Online reader chapter count changed")
    html_counts = Counter()
    html_links = 0
    for file in html.glob("*.html"):
        reader = LinkReader()
        reader.feed(file.read_text(encoding="utf-8"))
        html_counts.update({k: reader.classes[k] for k in
                            ("exercise", "hint", "solution")})
        for u in reader.links:
            if u == "../../index.html":
                # CI's later site job supplies the collection-wide homepage.
                continue
            if u.startswith(("http:", "https:", "mailto:", "data:", "#")):
                continue
            target = (file.parent / unquote(urlsplit(u).path)).resolve()
            check(target.is_file(), f"Broken online asset: {file.name} -> {u}")
            html_links += 1
    check(all(html_counts[k] == 144 for k in
              ("exercise", "hint", "solution")),
          f"Online reader lost exercises or solutions: {html_counts}")
    result = {
        "status": "pass",
        "reading_pdf_pages": read_pages,
        "print_interior_pages": interior_pages,
        "kdp_counted_pages": meta["kdp_pages"],
        "spine_in": meta["spine_in"],
        "wrap_width_in": meta["wrap_width_in"],
        "wrap_height_in": meta["wrap_height_in"],
        "print_isbn": ISBN,
        "printed_chapters": chapters,
        "epub_chapters": len(nav_chapters),
        "epub_manifest_items": len(manifest),
        "epub_internal_assets_and_links": epub_links,
        "epub_exercise_hint_solution": dict(epub_counts),
        "html_chapters": len(chapter_html),
        "html_local_asset_links": html_links,
        "html_exercise_hint_solution": {k: html_counts[k] for k in
                                        ("exercise", "hint", "solution")},
    }
    report = root / "build/volume2-integers/production-output-qa.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Volume 2 cross-format QA PASS: {read_pages} reading pages, "
          f"{interior_pages} print pages, {meta['kdp_pages']} KDP-counted "
          f"pages, spine {meta['spine_in']} in; 11 chapters and "
          "144 exercise/hint/solution triplets in EPUB and HTML")
    return result


if __name__ == "__main__":
    run(Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT)
