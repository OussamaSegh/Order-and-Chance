"""Regression checks for Volume 2 exercises and chapter-level LaTeX structure.

These tests guard editorial structure. They do not certify mathematical proofs.
Run with: python -m unittest tools/test_volume2_manuscript.py
"""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = (
    "ch01-divisibility",
    "ch02-primes",
    "ch03-congruences",
    "ch04-arithmetic-functions",
    "ch05-primitive-roots",
    "ch06-quadratic-reciprocity",
    "ch07-sums-of-squares",
    "ch09-diophantine",
    "ch08-continued-fractions",
    "ch10-gaussian-eisenstein",
    "ch14-characters",
)
CHAPTER_DIR = ROOT / "volume2-integers" / "chapters"
EXERCISE = re.compile(r"\\begin\{exercise\}(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}")
HINT = re.compile(r"\\begin\{hint\}\{([^}]+)\}")
SOLUTION = re.compile(r"\\begin\{solution\}\{([^}]+)\}")
SOLUTION_BODY = re.compile(
    r"\\begin\{solution\}\{([^}]+)\}([\s\S]*?)\\end\{solution\}"
)
LABEL = re.compile(r"\\label\{([^}]+)\}")
ENVIRONMENTS = (
    "proof", "exercise", "solution", "hint", "enumerate",
    "figure", "theorem", "lemma", "proposition", "definition",
)


class TestVolume2Manuscript(unittest.TestCase):
    def test_every_exercise_has_a_matching_hint_and_solution(self):
        total = 0
        for chapter in CHAPTERS:
            with self.subTest(chapter=chapter):
                source = (CHAPTER_DIR / (chapter + ".tex")).read_text(encoding="utf-8")
                exercises = EXERCISE.findall(source)
                hints = HINT.findall(source)
                solutions = SOLUTION.findall(source)
                self.assertTrue(exercises, "The chapter must contain graded exercises")
                self.assertEqual(len(exercises), len(set(exercises)), "Duplicate exercise labels")
                self.assertEqual(exercises, hints, "Exercise and hint keys/order differ")
                self.assertEqual(exercises, solutions, "Exercise and solution keys/order differ")
                for label, body in SOLUTION_BODY.findall(source):
                    self.assertIn("\\idea", body, "Missing discovery note for " + label)
                    self.assertIn("\\writeup", body, "Missing formal proof for " + label)
                total += len(exercises)
        self.assertEqual(total, 144, "Preserve all 144 graded exercises and their hints/solutions")

    def test_approved_four_part_reading_order(self):
        source = (ROOT / "volume2-integers" / "main.tex").read_text(encoding="utf-8")
        self.assertIn(r"\mainmatter", source)
        body = source.split(r"\mainmatter", 1)[1].split(r"\backmatter", 1)[0]
        parts = re.findall(r"\\part\{([^}]+)\}", body)
        chapters = re.findall(r"\\input\{chapters/([^}]+)\}", body)
        self.assertEqual(parts, [
            "The Arithmetic of Integers",
            "Patterns in Remainders",
            "Equations in Integers",
            "The Hidden Structure",
        ])
        self.assertEqual(chapters, list(CHAPTERS), "Source order must match the approved curriculum")
        self.assertEqual(len(chapters), len(set(chapters)), "Chapter appears more than once")

    def test_chapter_labels_are_unique(self):
        for chapter in CHAPTERS:
            with self.subTest(chapter=chapter):
                source = (CHAPTER_DIR / (chapter + ".tex")).read_text(encoding="utf-8")
                labels = LABEL.findall(source)
                self.assertEqual(len(labels), len(set(labels)))

    def test_major_latex_environment_counts_balance(self):
        for chapter in CHAPTERS:
            with self.subTest(chapter=chapter):
                source = (CHAPTER_DIR / (chapter + ".tex")).read_text(encoding="utf-8")
                for env in ENVIRONMENTS:
                    self.assertEqual(
                        source.count("\\begin{" + env + "}"),
                        source.count("\\end{" + env + "}"),
                        "Unbalanced LaTeX environment: " + env,
                    )

    def test_new_tikz_plates_exist(self):
        for name in ("ch01-remainder-staircase.tex", "ch03-unit-classes.tex"):
            with self.subTest(plate=name):
                source = (
                    ROOT / "volume2-integers" / "figures" / name
                ).read_text(encoding="utf-8")
                self.assertIn("\\begin{tikzpicture}", source)
                self.assertIn("\\end{tikzpicture}", source)


if __name__ == "__main__":
    unittest.main()
