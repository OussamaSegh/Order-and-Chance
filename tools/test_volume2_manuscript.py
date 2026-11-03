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

    def test_volume1_bridges_have_a_proved_source_and_a_concrete_payoff(self):
        """Step 2: the referenced Volume 1 tools must be present in that volume."""
        first = ROOT / "volume1-first-principles" / "chapters"
        counting = (first / "ch02-counting.tex").read_text(encoding="utf-8")
        complex_roots = (first / "ch02-complex-roots.tex").read_text(encoding="utf-8")
        sums = (first / "ch01-sums.tex").read_text(encoding="utf-8")
        self.assertIn(r"\begin{theorem}[inclusion--exclusion]", counting)
        self.assertIn(r"\begin{proposition}[roots of unity]", complex_roots)
        self.assertIn(r"\begin{theorem}[roots-of-unity filter]", complex_roots)
        self.assertIn("[Brahmagupta's identity]", complex_roots)
        self.assertIn(r"\begin{reminder}[well ordering]", sums)

        expected = {
            "ch04-arithmetic-functions": (
                "From Volume 1: inclusion--exclusion",
                r"\varphi(6)=6-3-2+1=2",
            ),
            "ch05-primitive-roots": (
                "From Volume 1: roots of unity",
                r"2^3\equiv3",
            ),
            "ch10-gaussian-eisenstein": (
                "From Volume 1: complex numbers",
                r"N(1+3i)=10",
            ),
            "ch14-characters": (
                "From Volume 1 to Volume 3",
                r"\mathbf 1_{n\equiv1\pmod4}",
            ),
            "ch02-primes": (
                "First reading and deeper reading",
                "proof by contradiction",
            ),
            "ch06-quadratic-reciprocity": (
                "Three questions, in the right order",
                "pair each nonzero class",
            ),
            "ch09-diophantine": (
                "Choose a first route",
                "well-ordering principle",
            ),
        }
        for name, phrases in expected.items():
            with self.subTest(chapter=name):
                src = (CHAPTER_DIR / (name + ".tex")).read_text(encoding="utf-8")
                for phrase in phrases:
                    self.assertIn(phrase, src)
        ch1 = (CHAPTER_DIR / "ch01-divisibility.tex").read_text(encoding="utf-8")
        self.assertIn("Recall the first groups from Volume~1", ch1)
        ch11 = (CHAPTER_DIR / "ch14-characters.tex").read_text(encoding="utf-8")
        self.assertIn(
            r"Volume~1 introduced group language; Chapter~\ref{ch:congruences}",
            ch11,
        )

    def test_volume1_bridge_examples_are_mathematically_sound(self):
        """Check the arithmetic displayed in the four principal bridges."""
        from math import gcd

        self.assertEqual([k for k in range(1, 7) if gcd(k, 6) == 1], [1, 5])
        self.assertEqual(6 - 3 - 2 + 1, 2)
        self.assertEqual([pow(2, k, 5) for k in range(5)], [1, 2, 4, 3, 1])
        self.assertEqual((1 + 1j) * (2 + 1j), 1 + 3j)
        self.assertEqual(1**2 + 3**2, (1**2 + 1**2) * (2**2 + 1**2))

        for n in range(-20, 21):
            chi4 = 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
            filtered = (int(n % 2 != 0) + chi4) // 2
            self.assertEqual(filtered, int(n % 4 == 1))
        for p in (3, 5, 7, 11, 13):
            squares = {k * k % p for k in range(1, p)}
            self.assertEqual(len(squares), (p - 1) // 2)

    def test_step3_core_workshops_precede_optional_extensions(self):
        """Readers can reach the foundation exercise route without advanced sections."""
        core_before_optional = {
            "ch02-primes": (
                r"\subsection*{Proof workshop: repair a false claim about Euclid's number}",
                r"\section{Chebyshev's bounds}",
                "Optional route: quantitative prime bounds",
            ),
            "ch03-congruences": (
                r"\subsection*{Proof workshop: what cancellation actually requires}",
                r"\section{Lifting modulo prime powers}",
                "Optional route: lifting polynomial roots",
            ),
            "ch04-arithmetic-functions": (
                r"\subsection*{Proof workshop: invert a small divisor sum}",
                r"\section{Average orders}",
                "Optional route: average orders",
            ),
            "ch07-sums-of-squares": (
                r"\subsection*{Proof workshop: an obstruction is not a classification}",
                r"\section{Lattice points in a disc}",
                "Optional route: counting lattice points",
            ),
            "ch09-diophantine": (
                r"\subsection*{Proof workshop: make a nonexistence argument complete}",
                r"\section{Rational points on conics: the chord method}",
                "Two routes through integer equations",
            ),
            "ch14-characters": (
                r"\subsection*{Proof workshop: a small character as a detector}",
                r"\section{One series at the boundary}",
                "Optional route: the analytic boundary",
            ),
        }
        for chapter, (workshop, extension, signpost) in core_before_optional.items():
            with self.subTest(chapter=chapter):
                source = (CHAPTER_DIR / (chapter + ".tex")).read_text(encoding="utf-8")
                self.assertIn(workshop, source)
                self.assertIn(extension, source)
                self.assertIn(signpost, source)
                self.assertLess(source.index(workshop), source.index(extension))
                self.assertLess(source.index(signpost), source.index(extension))

        diophantine = (CHAPTER_DIR / "ch09-diophantine.tex").read_text(
            encoding="utf-8"
        )
        self.assertLess(
            diophantine.index(r"\section{Infinite descent}"),
            diophantine.index(r"\section{Rational points on conics: the chord method}"),
        )
        self.assertIn(
            r"\section{Optional workshop: Vieta jumping and descent}",
            diophantine,
        )
        self.assertLess(
            diophantine.index(r"\section{Factoring with a sum of squares}"),
            diophantine.index(r"\section{Vieta jumping}"),
        )

    def test_step3_optional_problems_label_their_extension(self):
        """Never route a first-time reader silently into skipped material."""
        optional = {
            "ch02-primes": [
                "ex:gaps", "ex:factorial", "ex:erdosdiv",
                "ex:furstenberg", "ex:t1-prod11",
            ],
            "ch03-congruences": ["ex:hensel"],
            "ch06-quadratic-reciprocity": ["pb:rabin", "pb:squaresmodpk"],
            "ch07-sums-of-squares": ["ex:eureka"],
            "ch09-diophantine": [
                "ex:mordell5", "ex:eisentri",
                "ex:markovcoprime", "ex:imo88",
            ],
            "ch14-characters": [
                "ex:t1-char-series", "ex:t1-group3", "pb:powerful",
            ],
        }
        for chapter, labels in optional.items():
            source = (CHAPTER_DIR / (chapter + ".tex")).read_text(
                encoding="utf-8"
            )
            exercises = dict(re.findall(
                r"\\begin\{exercise\}(?:\[[^\]]*\])?"
                r"\\label\{([^}]+)\}([\s\S]*?)\\end\{exercise\}",
                source,
            ))
            for label in labels:
                with self.subTest(chapter=chapter, label=label):
                    self.assertIn(label, exercises)
                    self.assertRegex(exercises[label], r"(?i)optional")

    def test_step3_main_route_has_no_optional_theorem_dependency(self):
        """Core exposition must not cite the theorems inside optional blocks."""
        boundaries = {
            "ch02-primes": (
                r"\section{Chebyshev's bounds}",
                ("thm:cheb", "thm:bertrand"),
            ),
            "ch03-congruences": (
                r"\section{Lifting modulo prime powers}",
                ("thm:hensel",),
            ),
            "ch09-diophantine": (
                r"\section{Rational points on conics: the chord method}",
                ("prop:chord", "thm:mordell7", "thm:markov"),
            ),
            "ch14-characters": (
                r"\section{One series at the boundary}",
                ("prop:t1-chi4series", "prop:t1-charbound"),
            ),
        }
        for chapter, (section, forbidden) in boundaries.items():
            with self.subTest(chapter=chapter):
                src = (CHAPTER_DIR / (chapter + ".tex")).read_text(encoding="utf-8")
                core = src[:src.index(section)]
                for label in forbidden:
                    self.assertNotIn(r"\ref{" + label + "}", core)

        divisibility = (CHAPTER_DIR / "ch01-divisibility.tex").read_text(
            encoding="utf-8"
        )
        start = divisibility.index(r"\begin{solution}{pb:valuation}")
        end = divisibility.index(r"\end{solution}", start)
        self.assertIn("divisibility by the product of those powers", divisibility[start:end])
        self.assertNotIn(
            "by the Chinese remainder theorem.", divisibility[start:end]
        )

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
