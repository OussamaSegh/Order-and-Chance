"""Regression checks for Volume 2 exercises and chapter-level LaTeX structure.

These tests guard editorial structure. They do not certify mathematical proofs.
Run with: python -m unittest tools/test_volume2_manuscript.py
"""
from pathlib import Path
import re
import json
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

    def test_series_catalog_matches_reader_facing_parts(self):
        source = (ROOT / "volume2-integers" / "main.tex").read_text(encoding="utf-8")
        book_parts = re.findall(r"\\part\{([^}]+)\}", source)
        catalog = json.loads((ROOT / "common" / "series-catalog.json").read_text(encoding="utf-8"))
        catalog_parts = [part["name"] for part in catalog["volumes"]["2"]["parts"]]
        self.assertEqual(book_parts, catalog_parts, "Update the canonical catalog when part names change")

    def test_every_local_reference_has_a_target(self):
        manuscript = [CHAPTER_DIR / (name + ".tex") for name in CHAPTERS]
        manuscript += [CHAPTER_DIR / "preface.tex", CHAPTER_DIR / "field-guide.tex"]
        sources = [(path.name, path.read_text(encoding="utf-8")) for path in manuscript]
        definitions = {}
        duplicates = []
        for filename, source in sources:
            for label in LABEL.findall(source):
                if label in definitions:
                    duplicates.append((label, definitions[label], filename))
                else:
                    definitions[label] = filename
        self.assertEqual(duplicates, [], "Duplicated labels across manuscript chapters")

        missing = []
        for filename, source in sources:
            for label in re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", source):
                if label not in definitions:
                    missing.append((filename, label))
        self.assertEqual(missing, [], "Unresolved manuscript-local references")

    def test_chapter_labels_are_unique(self):
        for chapter in CHAPTERS:
            with self.subTest(chapter=chapter):
                source = (CHAPTER_DIR / (chapter + ".tex")).read_text(encoding="utf-8")
                labels = LABEL.findall(source)
                self.assertEqual(len(labels), len(set(labels)))

    def test_early_chapter_roadmap_matches_printed_order(self):
        """Orders are Chapter 5; characters are taught in Chapter 11, not Volume 3."""
        primes = (CHAPTER_DIR / "ch02-primes.tex").read_text(encoding="utf-8")
        congruences = (CHAPTER_DIR / "ch03-congruences.tex").read_text(encoding="utf-8")
        self.assertIn(r"Chapter~\ref{ch:characters}", primes)
        self.assertNotIn("characters, built in Volume~3", primes)
        self.assertIn(r"\subsection*{A counting identity for divisor sums}", congruences)
        self.assertIn(r"multiplicative order in Chapter~\ref{ch:orders}", congruences)
        self.assertNotIn("order is defined as the least positive exponent in the next chapter", congruences)

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

    def test_sieve_theorem_counts_cutoffs_past_x(self):
        """Legendre's sieve has a min(x,z) boundary, not pi(z) alone."""
        source = (CHAPTER_DIR / "ch14-characters.tex").read_text(encoding="utf-8")
        self.assertIn(r"\pi(\min\{x,z\})", source)

        def prime(n):
            return n >= 2 and all(n % d for d in range(2, int(n ** .5) + 1))

        def pi(n):
            return sum(prime(k) for k in range(2, int(n) + 1))

        def sifted(x, z):
            return sum(
                all(n % p for p in range(2, z + 1) if prime(p))
                for n in range(1, x + 1)
            )

        self.assertEqual(sifted(4, 10), 1)
        for x in range(1, 31):
            for z in range(max(2, int(x ** .5) + 1), 36):
                with self.subTest(x=x, z=z):
                    self.assertEqual(sifted(x, z), 1 + pi(x) - pi(min(x, z)))

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
