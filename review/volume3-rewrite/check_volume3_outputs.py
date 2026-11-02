#!/usr/bin/env python3
"""Publication-level smoke test for the generated Volume 3 PDF and EPUB.

Run after: ./build.sh volume3-symmetry
Usage: python3 review/volume3-rewrite/check_volume3_outputs.py

This checks generated artifacts, not just LaTeX sources. A successful run
is NOT a substitute for human page-by-page visual proofreading.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
REPORT = ROOT / "build" / "volume3-symmetry" / "edition-qa.json"


def run(*args: str) -> str:
    return subprocess.check_output(args, text=True, errors="replace")


def public_stem() -> str:
    return run("python3", str(ROOT / "tools" / "public_names.py"),
               "volume3-symmetry", "stem").strip()


def inspect_pdf(path: Path) -> tuple[int, str]:
    assert path.is_file() and path.stat().st_size > 200_000, f"Missing/empty PDF: {path}"
    info = run("pdfinfo", str(path))
    count = re.search(r"^Pages:\s*(\d+)\s*$", info, re.MULTILINE)
    assert count, f"No PDF page count: {path}"
    pages = int(count.group(1))
    assert pages >= 100, f"Suspiciously short PDF ({pages} pp): {path}"
    text = run("pdftotext", "-layout", str(path), "-")
    assert len(text) > 75_000, f"Non-searchable or very short PDF: {path}"
    for token in ("Lagrange", "Sylow", "Galois", "Hadamard", "quaternion"):
        assert token.lower() in text.lower(), f"Missing content {token}: {path}"
    unresolved = re.search(
        r"\b(?:theorem|lemma|figure|chapter|proposition|exercise|appendix)\s+\?\?",
        text, re.IGNORECASE)
    assert not unresolved, f"Unresolved cross-reference {unresolved.group()}: {path}"
    return pages, text


def inspect_epub(path: Path) -> dict[str, int]:
    assert path.is_file() and path.stat().st_size > 50_000, f"Missing/empty EPUB: {path}"
    with zipfile.ZipFile(path, "r") as z:
        error = z.testzip()
        assert error is None, f"Corrupt EPUB ZIP member: {error}"
        members = z.namelist()
        assert "mimetype" in members, "EPUB lacks mimetype"
        assert z.read("mimetype") == b"application/epub+zip", "Bad EPUB MIME type"
        xhtml = [n for n in members if n.lower().endswith((".html", ".xhtml"))]
        assert len(xhtml) >= 12, f"Missing EPUB chapters: only {len(xhtml)} XHTML pages"
        xml = [n for n in members if n.lower().endswith(".opf")]
        assert xml, "EPUB lacks OPF package"
        body = b" ".join(z.read(n) for n in xhtml).lower()
        for token in (b"sylow", b"galois", b"hadamard", b"quaternion"):
            assert token in body, f"Missing EPUB content: {token.decode()}"
    return {"xhtml_files": len(xhtml), "zip_entries": len(members)}


def render_samples(print_pdf: Path, pages: int) -> list[dict[str, object]]:
    # Render both an early instructional spread and widely separated
    # mid/late pages. The PNGs are uploaded alongside the build artifact;
    # a human must still inspect them for clipping, bad line breaks, glyphs.
    out = ROOT / "build" / "volume3-symmetry" / "qa-page-renders"
    out.mkdir(parents=True, exist_ok=True)
    samples = sorted({1, 2, 3, max(4, pages // 4),
                      max(4, pages // 2), max(4, pages * 3 // 4), pages})
    rendered = []
    for page in samples:
        target = out / f"print-page-{page:04d}"
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page),
                        "-singlefile", "-png", "-scale-to", "900",
                        str(print_pdf), str(target)], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        png = target.with_suffix(".png")
        assert png.is_file() and png.stat().st_size > 4000, f"Empty render: {png}"
        rendered.append({"page": page, "png": str(png.relative_to(ROOT)),
                         "size_bytes": png.stat().st_size})
    return rendered


def main() -> None:
    stem = public_stem()
    reading = DIST / f"{stem}.pdf"
    print_pdf = DIST / "kdp" / f"{stem} - Print.pdf"
    epub = DIST / f"{stem}.epub"
    reading_pages, _ = inspect_pdf(reading)
    print_pages, _ = inspect_pdf(print_pdf)
    assert reading_pages == print_pages + 1, (
        f"Reading cover/interior page mismatch: reading={reading_pages}, "
        f"print={print_pages}")
    info = inspect_epub(epub)
    renders = render_samples(print_pdf, print_pages)
    report = {
        "stem": stem, "reading_pdf_pages": reading_pages,
        "print_pdf_pages": print_pages, "epub": info,
        "representative_render_samples": renders,
        "limitations": ("Structural checks and seven sample renders only; "
                        "a complete human visual review and mathematical "
                        "proof-by-proof sign-off remain outstanding."),
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n",
                      encoding="utf-8")
    print(f"Volume 3 publication checks PASS: {reading_pages} reading pages, "
          f"{print_pages} print pages, {len(renders)} renders, "
          f"{info['xhtml_files']} EPUB XHTML documents")


if __name__ == "__main__":
    main()
