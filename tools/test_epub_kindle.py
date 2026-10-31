"""Kindle figure and math rendering on a miniature EPUB.

Run: python3 -m unittest discover -s tools -p test_epub_kindle.py
Needs xelatex, pdftocairo, pandoc, pngquant and oxipng. Skipped when they are absent.
"""
import io
import re
import shutil
import subprocess
import unittest
import zipfile
from pathlib import Path

from PIL import Image

import check_epub_media
import epub_fix
import epub_math
import epub_png


ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
HAVE = all(
    shutil.which(name) for name in ("xelatex", "pdftocairo", "pandoc", "pngquant", "oxipng")
)


@unittest.skipUnless(HAVE, "xelatex, pdftocairo, pandoc, pngquant and oxipng are required")
class KindleMath(unittest.TestCase):
    def test_descender_sits_below_the_baseline(self):
        glyphs = epub_math.render_formulas([("x=1", False), ("y=-x", False), ("0+y=0", False)])
        flat = glyphs[("x=1", False)]
        descended = glyphs[("y=-x", False)]
        self.assertGreater(descended.depth_em, flat.depth_em + 0.05)
        self.assertIn(f"vertical-align:{-descended.depth_em:.4f}em", descended.html("m.png", "y=-x"))
        self.assertNotIn("px", descended.html("m.png", "y=-x"))
        self.assertTrue(descended.png.startswith(b"\x89PNG"))

    def test_superscripts_and_square_render(self):
        formulas = [
            (r"\R^\N", False),
            (r"\mathbb{R}^\mathbb{N}", False),
            (r"\int_\R f", False),
            (r"K\otimes_\mathbb{Z}", False),
            (r"G\mathbin\square H", False),
            ("\\begin{split}a&=b\\\\c&=d\\end{split}\\qedhere", True),
        ]
        glyphs = epub_math.render_formulas(formulas)
        self.assertEqual(set(glyphs), set(formulas))

    def test_a_batch_of_ten_or_more_still_returns_every_png(self):
        formulas = [(f"x+{i}", False) for i in range(12)]
        glyphs = epub_math.render_formulas(formulas)
        self.assertEqual(set(glyphs), set(formulas))
        self.assertTrue(all(glyph.png.startswith(b"\x89PNG") for glyph in glyphs.values()))

    def test_display_alignment_renders(self):
        tex = r"\begin{aligned} a&=b+c\\ d&=e \end{aligned}"
        glyphs = epub_math.render_formulas([(tex, True)])
        glyph = glyphs[(tex, True)]
        self.assertTrue(glyph.display)
        self.assertGreater(glyph.width_em, 1)
        tag = glyph.html("m.png", tex)
        self.assertIn("oc-math-display", tag)
        self.assertIn('width="', tag)
        self.assertIn('height="', tag)
        self.assertNotIn("display:block", tag)

    def test_right_padding_does_not_precede_punctuation(self):
        glyph = epub_math.render_formulas([("100", False)])[("100", False)]
        png, ratio = epub_png.fit_formula_png(glyph.png, glyph.height_em)
        self.assertLess(ratio, 0.95)
        image = Image.open(io.BytesIO(png)).convert("RGBA")
        width, height = image.size
        self.assertTrue(any(image.getpixel((width - 1, y))[3] > 0 for y in range(height)))
        shown = epub_math.replace(glyph, width_em=glyph.width_em * ratio)
        wrapped = epub_math.attach_punctuation(shown.html("m.png", "100") + " .")
        self.assertIn('"/>.</span>', wrapped)
        self.assertNotRegex(wrapped, r'"/>\s+[.,]')
        self.assertLess(shown.width_em, glyph.width_em)


@unittest.skipUnless(HAVE, "xelatex, pdftocairo, pandoc, pngquant and oxipng are required")
class KindleEpub(unittest.TestCase):
    def test_plate_and_inline_math_pass_the_check(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            figures = work / "figures"
            figures.mkdir()
            (work / "sample.tex").write_text(
                "\\documentclass{book}\n\\begin{document}\n"
                "Increasing means that $x<y$ forces $f(x)\\le f(y)$.\n"
                "A single $y$ would have to satisfy $0+y=0$.\n"
                "\\begin{equation}y=-x\\end{equation}\n"
                "\\begin{figure}\\includegraphics{" + str(figures / "plate.svg") + "}\n"
                "\\caption{The domain is part of the question.}\n"
                "\\end{figure}\n\\end{document}\n",
                encoding="utf-8",
            )
            subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                 "-output-directory", str(figures), "-jobname", "plate",
                 r"\documentclass[border=4pt]{standalone}\begin{document}A plate.\end{document}"],
                check=True, capture_output=True, cwd=work,
            )
            subprocess.run(
                ["pdftocairo", "-svg", str(figures / "plate.pdf"), str(figures / "plate.svg")],
                check=True,
            )
            book = work / "sample.epub"
            subprocess.run(
                ["pandoc", str(work / "sample.tex"), "-f", "latex", "-t", "epub3", "--mathml",
                 "--css", str(TOOLS / "epub.css"), "--metadata", "title=Sample", "-o", str(book)],
                check=True, capture_output=True,
            )
            epub_fix.main(str(book), str(figures))
            errors = check_epub_media.check(book)
            self.assertEqual(errors, [], errors)
            with zipfile.ZipFile(book) as archive:
                chapter = "\n".join(
                    archive.read(name).decode("utf-8")
                    for name in archive.namelist()
                    if name.endswith(".xhtml"))
                manifest = archive.read(next(name for name in archive.namelist() if name.endswith(".opf"))).decode("utf-8")
                import struct
                plate = next(archive.read(name) for name in archive.namelist() if "oc-plate-" in name)
            pixel_w, pixel_h = struct.unpack(">II", plate[16:24])
            info = subprocess.check_output(["pdfinfo", str(figures / "plate.pdf")], text=True)
            size = re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", info)
            self.assertAlmostEqual(pixel_w / pixel_h, float(size.group(1)) / float(size.group(2)), delta=0.02)
            self.assertGreaterEqual(pixel_w, 1600)
            self.assertIn('class="oc-plate"', chapter)
            self.assertIn("width:100%;max-width:100%;height:auto", chapter)
            self.assertIn('class="oc-math-inline"', chapter)
            self.assertIn("vertical-align:-", chapter)
            self.assertNotIn("<math", chapter)
            self.assertNotIn(".svg", chapter)
            self.assertIn("image/png", manifest)
            self.assertNotIn("image/svg", manifest)
            epub_fix.main(str(book), str(figures))
            self.assertEqual(check_epub_media.check(book), [])


class FormulaPadding(unittest.TestCase):
    @unittest.skipUnless(HAVE, "xelatex, pdftocairo, pandoc, pngquant and oxipng are required")
    def test_transparent_right_columns_are_cropped(self):
        image = Image.new("RGBA", (40, 12), (0, 0, 0, 0))
        for x in range(4, 28):
            for y in range(2, 10):
                image.putpixel((x, y), (0, 0, 0, 255))
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        png, ratio = epub_png.fit_formula_png(buf.getvalue(), 0.4)
        self.assertAlmostEqual(ratio, 28 / 40)
        cropped = Image.open(io.BytesIO(png)).convert("RGBA")
        self.assertEqual(cropped.size[0], 28)
        self.assertTrue(any(cropped.getpixel((27, y))[3] > 0 for y in range(cropped.size[1])))

    def test_punctuation_is_flush_with_the_image(self):
        tag = (
            '<img class="oc-math-inline" src="m.png" alt="100" width="28" height="12" '
            'style="display:inline;width:1.7000em;height:0.7000em;max-width:100%;'
            'max-height:0.7000em;vertical-align:-0.0500em"/>'
        )
        wrapped = epub_math.attach_punctuation(tag + " .\n")
        self.assertIn('"/>.</span>', wrapped)
        self.assertNotRegex(wrapped, r'"/>\s+[.,]')
        display = epub_math.attach_punctuation(tag.replace("oc-math-inline", "oc-math-display") + ",")
        self.assertIn('"/>,</div>', display)
        self.assertNotIn(" ,", display)


if __name__ == "__main__":
    unittest.main()
