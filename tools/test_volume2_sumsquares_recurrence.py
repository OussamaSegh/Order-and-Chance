"""Independent arithmetic and teaching-order checks for Volume 2 pb:sumsquares.

The symbolic recurrence in the manuscript is supported by two *different*
finite oracles: direct tuple enumeration and iterative convolution. Finite
checks are not substitutes for a proof.
"""
import itertools
import math
import re
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CH4 = ROOT / "volume2-integers/chapters/ch04-arithmetic-functions.tex"
CH6 = ROOT / "volume2-integers/chapters/ch06-quadratic-reciprocity.tex"
KEYS = ("pb:eisensine", "pb:euler", "pb:sumsquares")


def isprime(n):
    return n > 1 and all(n % k for k in range(2, math.isqrt(n) + 1))


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def expected(p, n, c):
    eps = chi(-1, p)
    if n % 2:
        m = (n - 1) // 2
        return p ** (n - 1) + eps ** m * p ** m * chi(c, p)
    m = n // 2
    return p ** (n - 1) + eps ** m * p ** (m - 1) * (
        p * (c == 0) - 1
    )


def histogram(p, n):
    counts = [0] * p
    for coordinates in itertools.product(range(p), repeat=n):
        counts[sum(x * x for x in coordinates) % p] += 1
    return counts


class TestSumsOfSquaresTeachingAndArithmetic(unittest.TestCase):
    def test_all_three_journeys_follow_their_prerequisites(self):
        chapter4, chapter6 = CH4.read_text(), CH6.read_text()
        for key in KEYS:
            with self.subTest(key=key):
                for environment in ("exercise", "hint", "solution"):
                    if environment == "exercise":
                        marker = re.compile(
                            r"\\begin\{exercise\}(?:\[[^\]]*\])?"
                            r"\\label\{" + key + r"\}"
                        )
                    else:
                        marker = re.compile(
                            r"\\begin\{" + environment + r"\}\{" + key + r"\}"
                        )
                    self.assertIsNone(marker.search(chapter4))
                    self.assertEqual(len(marker.findall(chapter6)), 1)
        self.assertLess(chapter6.index(r"\label{ex:gausssum}"),
                        chapter6.index(r"\label{pb:sumsquares}"))
        self.assertLess(chapter6.index(r"\label{pb:carmichael}"),
                        chapter6.index(r"\label{pb:euler}"))
        exercise = chapter6.split(r"\label{pb:sumsquares}", 1)[1].split(
            r"\end{exercise}", 1
        )[0]
        solution = chapter6.split(r"\begin{solution}{pb:sumsquares}", 1)[1].split(
            r"\end{solution}", 1
        )[0]
        self.assertIn("total-variation distance", exercise)
        self.assertIn(r"\frac12\sum", exercise)
        self.assertNotIn("Volume~4", exercise + solution)
        self.assertIn(r"D_{n+2}(c)=\varepsilon pD_n(c)", solution)

    def test_two_square_counts_by_hyperbola(self):
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
            eps = chi(-1, p)
            for c in range(p):
                pairs = sum((x * x + y * y - c) % p == 0
                            for x in range(p) for y in range(p))
                formula = p + eps * (p * (c == 0) - 1)
                self.assertEqual(pairs, formula, (p, c))

    def test_all_distributions_and_total_variation_convolution(self):
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
            square_counts = [0] * p
            for x in range(p):
                square_counts[x * x % p] += 1
            counts = square_counts[:]
            for n in range(1, 9):
                self.assertEqual(sum(counts), p ** n)
                for c, actual in enumerate(counts):
                    self.assertEqual(actual, expected(p, n, c), (p, n, c))
                tv = Fraction(
                    sum(abs(v - p ** (n - 1)) for v in counts), 2 * p ** n
                )
                target = (Fraction(p - 1, p) * Fraction(1, p ** (n // 2))
                          if n % 2 == 0 else
                          Fraction(p - 1, 2 * p ** ((n + 1) // 2)))
                self.assertEqual(tv, target, (p, n))
                new = [0] * p
                for c, ways in enumerate(counts):
                    for residue, multiplicity in enumerate(square_counts):
                        new[(c + residue) % p] += ways * multiplicity
                counts = new

    def test_independent_direct_tuple_enumeration(self):
        for p in (3, 5, 7):
            for n in (1, 2, 3, 4):
                expected_counts = [expected(p, n, c) for c in range(p)]
                self.assertEqual(histogram(p, n), expected_counts)


if __name__ == "__main__":
    unittest.main()
