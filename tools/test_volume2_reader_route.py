"""Volume 2 Step 7: guard printed chapter bridges, back-cover and KDP promises.

Source-level reader/metadata checks; they cannot replace PDF/EPUB visual QA.
Run: python3 -m unittest tools/test_volume2_reader_route.py
"""
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "volume2-integers"
CHAPTERS = (
    "ch01-divisibility", "ch02-primes", "ch03-congruences",
    "ch04-arithmetic-functions", "ch05-primitive-roots",
    "ch06-quadratic-reciprocity", "ch07-sums-of-squares",
    "ch09-diophantine", "ch08-continued-fractions",
    "ch10-gaussian-eisenstein", "ch14-characters",
)
# Each bridge must have a mathematical, not just a generic, topic.
NEXT_BRIDGE = (
    "prime factorisation",
    "congruences",
    "arithmetic functions",
    "primitive root",
    "quadratic reciprocity",
    "sum of two squares",
    "Diophantine equations",
    "continued fractions",
    "Gaussian",
    "characters",
    r"Volume~3",
)
PREVIOUS_BRIDGE = (
    None,
    "divisibility chapter",
    "primes chapter",
    "congruences chapter",
    "Arithmetic functions",
    "Primitive roots",
    "Quadratic reciprocity",
    "sums-of-squares chapter",
    "Diophantine chapter",
    "continued-fractions chapter",
    "Gaussian and Eisenstein chapters",
)


def chapter_source(chapter):
    return (BOOK / "chapters" / (chapter + ".tex")).read_text(encoding="utf-8")


class TestVolume2ReaderRoute(unittest.TestCase):
    def test_chapter_route_matches_print_and_has_local_openings_and_outros(self):
        main = (BOOK / "main.tex").read_text(encoding="utf-8")
        mainmatter = main.split(r"\mainmatter", 1)[1].split(
            r"\backmatter", 1
        )[0]
        self.assertEqual(
            re.findall(r"\\input\{chapters/([^}]+)\}", mainmatter),
            list(CHAPTERS),
        )
        self.assertEqual(len(re.findall(r"\\part\{", mainmatter)), 4)
        for index, chapter in enumerate(CHAPTERS):
            with self.subTest(chapter=chapter):
                src = chapter_source(chapter)
                self.assertEqual(src.count(r"\section{Exercises}"), 1)
                opening = src[:src.index(r"\section{")]
                main_text = src[:src.index(r"\section{Exercises}")]
                exercises = src[src.index(r"\section{Exercises}"):]
                forward = r"\noindent\emph{The next question.}"
                self.assertEqual(main_text.count(forward), 1)
                self.assertNotIn(forward, exercises)
                self.assertIn(NEXT_BRIDGE[index], main_text.split(forward)[-1])
                if index == 0:
                    self.assertNotIn(
                        r"\noindent\emph{What carries forward.}", opening
                    )
                else:
                    backward = r"\noindent\emph{What carries forward.}"
                    self.assertEqual(opening.count(backward), 1)
                    self.assertIn(
                        PREVIOUS_BRIDGE[index], opening.split(backward)[-1]
                    )

    def test_book_metadata_makes_no_fourteen_chapter_or_p_adic_claim(self):
        listing = (BOOK / "kdp.md").read_text(encoding="utf-8")
        sections = re.split(r"(?m)^#\s+(Description|Keywords)\s*$", listing)
        self.assertEqual(len(sections), 5)
        desc, keyword_text = sections[2].strip(), sections[4].strip()
        keywords = [line.strip() for line in keyword_text.splitlines()
                    if line.strip()]
        self.assertLessEqual(len(desc), 4000)
        self.assertEqual(len(keywords), 7)
        for keyword in keywords:
            self.assertLessEqual(len(keyword), 50)
        self.assertIn("four parts and eleven chapters", desc)
        self.assertIn("Volume 1", desc)
        self.assertIn("No abstract algebra course is assumed", desc)
        self.assertIn("144 graded exercises", desc)
        self.assertIn("The next volume", desc)
        self.assertIn("Symmetry: Groups, Rings and Fields", desc)
        self.assertIn("belong to later volumes", desc)
        self.assertNotIn("Fourteen chapters", desc)
        self.assertNotIn("to ideals, where unique factorisation", desc)
        self.assertNotIn("to the p-adic numbers", desc)

    def test_field_guide_keeps_advanced_notation_out_of_first_toolbox(self):
        src = chapter_source("field-guide")
        main, preview = src.split(
            r"\section*{Optional later-volume preview: ideals and $p$-adic notation}",
            1,
        )
        self.assertIn(r"\section*{Which tool should I try?}", main)
        self.assertIn(r"\section*{Five questions", main)
        self.assertIn(r"\section*{One investigation", main)
        for advanced in (
            r"\item[$v_p(0)$.]",
            r"\item[$\mathcal O_K$.]",
            r"\item[$(\alpha),\ (\alpha,\beta)$.]",
            r"\item[$|x|_p$.]",
            r"\item[$\Z_p,\ \Q_p$.]",
        ):
            self.assertNotIn(advanced, main)
            self.assertIn(advanced, preview)
        self.assertLess(
            src.index(r"\section*{Optional later-volume preview"),
            src.index(r"\section*{From arithmetic to symmetry"),
        )
        last = src.split(r"\section*{From arithmetic to symmetry}", 1)[1]
        self.assertIn(r"Volume~3", last)
        self.assertIn(r"\chi_4(3)^2", last)
        self.assertIn(r"Volume~13", last)

    def test_preface_back_cover_and_print_isbn_agree(self):
        preface = chapter_source("preface")
        blurb = (BOOK / "blurb.tex").read_text(encoding="utf-8")
        main = (BOOK / "main.tex").read_text(encoding="utf-8")
        catalog = (ROOT / "common/series-catalog.json").read_text(
            encoding="utf-8"
        )
        self.assertIn("the four parts in order", preface)
        self.assertIn(r"Volume~1", preface)
        self.assertIn(r"Volume~3", preface)
        self.assertIn(r"Volume~13", preface)
        self.assertIn("all 144 graded exercises", blurb)
        self.assertIn(r"Volume~3, \emph{Symmetry}", blurb)
        self.assertLessEqual(len(blurb.split()), 180)
        self.assertIn(r"\renewcommand{\bookisbnprint}{9798167208650}", main)
        self.assertIn('"subtitle": "Primes, Patterns and Proofs"', catalog)


if __name__ == "__main__":
    unittest.main()
