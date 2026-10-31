"""Rasterize an EPUB TikZ plate to a full-column PNG.

``pdftocairo -svg`` writes a width in points and a viewBox in the same numbers.
Kindle treats that viewBox as CSS pixels and ignores ``max-width``, so a plate
about 340 pt wide occupies about a third of a Paperwhite. A PNG wider than the
screen, with ``width: 100%`` on the ``img``, is what KF8 and KFX actually scale
to the text column. ``max-width`` stays in the stylesheet for other readers;
Enhanced Typesetting ignores it.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import tempfile
from pathlib import Path

import epub_png


PLATE_PX = 1800


def index_svgs(figures: Path) -> dict[bytes, Path]:
    found = {}
    for svg in sorted(figures.glob("*.svg")):
        found[hashlib.sha256(svg.read_bytes()).digest()] = svg
    return found


def match_svg(data: bytes, by_hash: dict[bytes, Path]) -> Path | None:
    if data.startswith(b"\x1f\x8b"):
        import gzip
        data = gzip.decompress(data)
    candidates = [data, data.strip(), data.rstrip(b"\n") + b"\n"]
    if not data.endswith(b"\n"):
        candidates.append(data + b"\n")
    for candidate in candidates:
        hit = by_hash.get(hashlib.sha256(candidate).digest())
        if hit is not None:
            return hit
    return None


def page_points(pdf: Path) -> tuple[float, float]:
    info = subprocess.check_output(["pdfinfo", "-f", "1", "-l", "1", str(pdf)], text=True)
    match = re.search(r"Page\s+1 size:\s+([\d.]+) x ([\d.]+) pts", info) or re.search(
        r"Page size:\s+([\d.]+) x ([\d.]+) pts", info)
    if not match:
        raise RuntimeError(f"could not read the page size of {pdf}")
    return float(match.group(1)), float(match.group(2))


def rasterize(pdf: Path, width: int = PLATE_PX) -> bytes:
    """Rasterize page 1 at ``width`` pixels, keeping the PDF's aspect ratio.

    ``pdftocairo -scale-to-x`` alone leaves the height at the default
    resolution, which squashes a wide plate. Both axes have to be set.
    """
    if not pdf.is_file():
        raise FileNotFoundError(f"missing figure PDF {pdf}")
    width_pt, height_pt = page_points(pdf)
    height = max(1, round(width * height_pt / width_pt))
    with tempfile.TemporaryDirectory(prefix="oc-plate-") as tmp:
        prefix = Path(tmp) / "plate"
        proc = subprocess.run(
            ["pdftocairo", "-png", "-singlefile", "-f", "1", "-l", "1",
             "-scale-to-x", str(width), "-scale-to-y", str(height),
             str(pdf), str(prefix)],
            capture_output=True,
        )
        if proc.returncode != 0:
            raise RuntimeError(
                f"pdftocairo failed on {pdf.name}: {proc.stderr.decode(errors='replace')[-500:]}")
        png = prefix.with_suffix(".png").read_bytes()
    if not png.startswith(b"\x89PNG"):
        raise RuntimeError(f"{pdf.name} did not rasterize to a PNG")
    return epub_png.compress_plate(png)
