"""Kindle figure and math rendering on a miniature EPUB.

Run: python3 -m unittest discover -s tools -p test_epub_kindle.py
Needs xelatex, pdftocairo and pandoc. Skipped when they are absent.
"""
import re
import shutil
import subprocess
import unittest
import zipfile
from pathlib import Path

import check_epub_media
import epub_fix
import epub_math


ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
HAVE = all(shutil.which(name) for name in ("xelatex", "pdftocairo", "pandoc"))


@unittest.skipUnless(HAVE, "xelatex, pdftocairo and pandoc are required")
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
        self.assertIn("height:auto", tag)


@unittest.skipUnless(HAVE, "xelatex, pdftocairo and pandoc are required")
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


if __name__ == "__main__":
    unittest.main()
