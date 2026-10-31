"""Shrink EPUB images without moving their CSS size.

Formula ink is black with an alpha edge, so those files become a 16-level
palette and are then repacked. Plates stay full colour: oxipng only, lossless,
so coral and the other inks are the pixels the renderer drew. The TeX depth,
which sets the baseline, is untouched. Transparent columns on the right of a
formula are cropped, and the caller shrinks the TeX width by the same fraction
so the following punctuation sits against the ink.
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


def trim_right_padding(image, alpha_floor: int = 0):
    """Crop fully transparent columns from the right.

    The preview border and the math list's right sidebearing are empty pixels
    inside the TeX advance. They read as a gap before ``.`` or ``,``. The
    returned fraction is the share of the width that remains, so the CSS width
    can shrink with the bitmap instead of stretching the ink.
    """
    im = image.convert("RGBA")
    width, height = im.size
    if width <= 1 or height <= 0:
        return im, 1.0
    alpha = im.getchannel("A").load()
    last = width - 1
    while last > 0 and all(alpha[last, y] <= alpha_floor for y in range(height)):
        last -= 1
    kept = last + 1
    if kept == width:
        return im, 1.0
    return im.crop((0, 0, kept, height)), kept / width


def fit_formula_png(data: bytes, height_em: float) -> tuple[bytes, float]:
    """Keep the bitmap about 2.5 CSS pixels per displayed pixel, not 10.

    Moon+ draws an image at its intrinsic pixel size when it ignores em
    widths. A 480 ppi glyph is then several times the body. The HTML width
    and height are the real constraint; this stops the fallback being huge.
    The second value is the fraction of the TeX width still occupied after
    the right-hand transparent padding is removed.
    """
    import io
    from PIL import Image
    target_h = max(8, int(round(height_em * 16 * 2.5)))
    im = Image.open(io.BytesIO(data))
    im, ratio = trim_right_padding(im)
    resized = im.height > int(target_h * 1.25)
    if resized:
        target_w = max(1, int(round(im.width * target_h / im.height)))
        im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
        im, extra = trim_right_padding(im)
        ratio *= extra
    if ratio == 1.0 and not resized:
        return data, 1.0
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return compress_math(buf.getvalue()), ratio


def compress_math_many(images: list[bytes]) -> list[bytes]:
    if not images:
        return []
    workers = min(8, os.cpu_count() or 2, len(images))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(compress_math, images))
