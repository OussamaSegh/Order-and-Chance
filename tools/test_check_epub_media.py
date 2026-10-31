"""The EPUB figure and math rules, without building a book.

Run: python3 -m unittest discover -s tools -p test_check_epub_media.py
"""
import struct
import tempfile
import unittest
import zipfile
import zlib
from pathlib import Path

import check_epub_media


TOOLS = Path(__file__).resolve().parent


def png(width: int, height: int = 40) -> bytes:
    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    raw = b"".join(b"\x00" + b"\xff\xff\xff" * width for _ in range(height))
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")


STYLES = """
figure img, img.oc-plate { width: 100%; max-width: 100%; height: auto; }
img.oc-math-inline { height: auto; max-width: 100%; }
img.oc-math-display { display: block; height: auto; max-width: 100%; }
"""

PAGE = """<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<body>
<figure>
<img class="oc-plate" src="../media/plate.png" alt="Three number lines." style="width:100%;max-width:100%;height:auto"/>
<figcaption>forces <img class="oc-math-inline" src="../media/inline.png" alt="x &lt; y" style="width:1.2500em;max-width:100%;height:auto;vertical-align:-0.2200em"/> here</figcaption>
</figure>
<p><img class="oc-math-display" src="../media/display.png" alt="y=-x" style="display:block;width:2.6000em;max-width:100%;height:auto;margin:0.6em auto"/></p>
</body>
</html>
"""


def epub(path: Path, page: str = PAGE, styles: str = STYLES, plate: int = 1800) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("EPUB/styles/stylesheet1.css", styles)
        archive.writestr("EPUB/text/ch001.xhtml", page)
        archive.writestr("EPUB/media/plate.png", png(plate, 80))
        archive.writestr("EPUB/media/inline.png", png(80, 30))
        archive.writestr("EPUB/media/display.png", png(120, 40))


class CheckEpubMedia(unittest.TestCase):
    def test_shared_stylesheet_carries_the_rule(self):
        css = (TOOLS / "epub.css").read_text(encoding="utf-8")
        self.assertEqual(check_epub_media.stylesheet_errors(css), [])

    def _run(self, **kwargs):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "book.epub"
            epub(path, **kwargs)
            return check_epub_media.check(path)

    def test_full_width_plate_and_baseline_math_pass(self):
        self.assertEqual(self._run(), [])

    def test_fixed_pixel_width_fails(self):
        page = PAGE.replace(
            'style="width:100%;max-width:100%;height:auto"',
            'style="width:320px;height:110px"',
        )
        errors = self._run(page=page)
        self.assertTrue(any("px/pt" in error or "fixed" in error for error in errors), errors)

    def test_small_plate_fails(self):
        errors = self._run(plate=400)
        self.assertTrue(any("400px" in error for error in errors), errors)

    def test_svg_plate_fails(self):
        page = PAGE.replace("../media/plate.png", "../media/plate.svg")
        errors = self._run(page=page)
        self.assertTrue(any("SVG" in error for error in errors), errors)

    def test_missing_responsive_rule_fails(self):
        errors = self._run(styles="figure img { max-width: 100%; height: auto; }\nimg.oc-math-inline { }")
        self.assertTrue(any("full-width figure rule" in error for error in errors), errors)

    def test_inline_math_without_baseline_fails(self):
        page = PAGE.replace(
            "width:1.2500em;max-width:100%;height:auto;vertical-align:-0.2200em",
            "width:1.2500em;max-width:100%;height:auto;vertical-align:middle",
        )
        errors = self._run(page=page)
        self.assertTrue(any("vertical-align" in error for error in errors), errors)

    def test_leftover_mathml_fails(self):
        page = PAGE + "<p><math xmlns='http://www.w3.org/1998/Math/MathML'><mi>x</mi></math></p>"
        errors = self._run(page=page)
        self.assertTrue(any("MathML" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
