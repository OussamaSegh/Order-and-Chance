"""Shrink EPUB images without moving their CSS size.

Formula ink is black with an alpha edge, so those files become a 16-level
palette and are then repacked. Plates stay full colour: oxipng only, lossless,
so coral and the other inks are the pixels the renderer drew. The TeX width
and depth, which set the CSS, are untouched.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def _require(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise RuntimeError(f"{name} is required to compress EPUB images")
    return path


def _compress(data: bytes, colors: int | None, posterize: bool, quality: str | None) -> bytes:
    pngquant = _require("pngquant")
    oxipng = _require("oxipng")
    with tempfile.TemporaryDirectory(prefix="oc-png-") as tmp:
        src = Path(tmp) / "in.png"
        quant = Path(tmp) / "q.png"
        out = Path(tmp) / "out.png"
        src.write_bytes(data)
        command = [pngquant, "--force", "--speed", "1"]
        if posterize:
            command.append("--nofs")
        if quality:
            command.append(f"--quality={quality}")
        if colors is not None:
            command.append(str(colors))
        command += ["--output", str(quant), str(src)]
        quantised = subprocess.run(command, capture_output=True)
        # Exit 99: the palette would fall below the quality floor. Keep colour.
        source = quant if quantised.returncode == 0 else src
        if quantised.returncode not in (0, 99):
            raise RuntimeError(quantised.stderr.decode(errors="replace")[-400:])
        packed = subprocess.run(
            [oxipng, "-o", "2", "--strip", "safe", "-q", "--threads", "1", str(source), "--out", str(out)],
            capture_output=True,
        )
        if packed.returncode != 0:
            raise RuntimeError(packed.stderr.decode(errors="replace")[-400:])
        return out.read_bytes()


def compress_math(data: bytes) -> bytes:
    """Black-on-transparent formula: 16-level palette, no dither."""
    return _compress(data, 16, posterize=True, quality=None)


def compress_plate(data: bytes) -> bytes:
    """Full colour. Lossless repack only; the inks are not quantised."""
    oxipng = _require("oxipng")
    with tempfile.TemporaryDirectory(prefix="oc-png-") as tmp:
        src = Path(tmp) / "in.png"
        out = Path(tmp) / "out.png"
        src.write_bytes(data)
        packed = subprocess.run(
            [oxipng, "-o", "2", "--strip", "safe", "-q", "--threads", "1", str(src), "--out", str(out)],
            capture_output=True,
        )
        if packed.returncode != 0:
            raise RuntimeError(packed.stderr.decode(errors="replace")[-400:])
        return out.read_bytes()


def compress_math_many(images: list[bytes]) -> list[bytes]:
    if not images:
        return []
    workers = min(8, os.cpu_count() or 2, len(images))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(compress_math, images))
