"""Focused Volume 4 mathematical regression checks.

These checks protect known proof/precision repairs. They are not substitutes for
a line-by-line independent referee or native artifact verification.

Run: python3 -m unittest discover -s tools -p test_volume4_math_audit.py
"""

from decimal import Decimal, localcontext
from itertools import product
from math import comb, factorial
from pathlib import Path
import unittest


CHAPTERS = Path(__file__).resolve().parents[1] / "volume4-chance" / "chapters"


def eulerian_descent_counts(n):
    """Number of permutations of n with 0, 1, ..., n-1 descents."""
    row = [1]
    for size in range(2, n + 1):
        old = row
        row = [
            (size - j) * (old[j - 1] if j else 0)
            + (j + 1) * (old[j] if j < len(old) else 0)
            for j in range(size)
        ]
    return row


def riffle_tv_exact(n, k, descents):
    """Exact rational total variation, returned as an integer fraction."""
    a = 2**k
    scale = a**n
    fact = factorial(n)
    numerator = sum(
        descents[r - 1] * abs(comb(a + n - r, n) * fact - scale)
        for r in range(1, n + 1)
    )
    return numerator, 2 * scale * fact


class TestVolume4MathAudit(unittest.TestCase):
    def test_fourier_cutoff_controls_both_growing_tails(self):
        source = (CHAPTERS / "ch06-clt.tex").read_text(encoding="utf-8")
        proof = source.split(r"\label{thm:inversion}", 1)[1].split(
            r"\section{Lindeberg", 1
        )[0]
        self.assertIn(r"P(|W|>A/2)+P(|\sigma Z|>A/2)", proof)
        self.assertNotIn(r"P(|\sigma Z|>1)", proof)
        self.assertIn("independent of both variables", proof)
        # The union-bound event inclusion behind the corrected inequality.
        for A, x, z in product(
            (1, 2, 5, 20),
            (-25, -7, -1, 0, 1, 7, 25),
            (-25, -7, -1, 0, 1, 7, 25),
        ):
            if abs(x + z) > A:
                self.assertTrue(abs(x) > A / 2 or abs(z) > A / 2)

    def test_lindeberg_split_uses_the_strict_hypothesis(self):
        source = (CHAPTERS / "ch06-clt.tex").read_text(encoding="utf-8")
        proof = source.split(r"\label{thm:lindeberg}", 1)[1].split(
            r"\end{proof}", 1
        )[0]
        self.assertIn(r"|X_{n,k}|>\varepsilon", proof)
        self.assertNotIn(r"|X_{n,k}|\ge\varepsilon", proof)
        # An atom at the threshold belongs to the small-increment part.
        epsilon = 0.5
        outcomes = (-epsilon, epsilon)
        gt = sum(x * x for x in outcomes if abs(x) > epsilon) / 2
        ge = sum(x * x for x in outcomes if abs(x) >= epsilon) / 2
        self.assertEqual(gt, 0)
        self.assertEqual(ge, epsilon * epsilon)

    def test_52_card_riffle_values_are_rounded_not_equal_to_one(self):
        descents = eulerian_descent_counts(52)
        self.assertEqual(sum(descents), factorial(52))
        expected = [
            "1.000", "1.000", "1.000", "1.000", "0.924",
            "0.614", "0.334", "0.167", "0.085", "0.043",
        ]
        with localcontext() as ctx:
            ctx.prec = 80
            for k, rounded in enumerate(expected, start=1):
                num, den = riffle_tv_exact(52, k, descents)
                self.assertGreater(num, 0)
                self.assertLess(num, den)  # Exact distance is never 1.
                self.assertEqual(
                    str((Decimal(num) / Decimal(den)).quantize(Decimal("0.001"))),
                    rounded,
                )
            num, den = riffle_tv_exact(52, 4, descents)
            self.assertTrue(
                Decimal("0.9999995") < Decimal(num) / Decimal(den) < Decimal("1")
            )
        source = (CHAPTERS / "ch08-markov.tex").read_text(encoding="utf-8")
        self.assertIn("rounded values, not exact equalities", source)
        self.assertIn("The first four plotted distances round to $1$", source)

    def test_memorylessness_degenerate_survival_case_is_justified(self):
        source = (CHAPTERS / "ch09-poisson.tex").read_text(encoding="utf-8")
        proof = source.split(r"\label{prop:memoryless}", 1)[1].split(
            r"\end{proof}", 1
        )[0]
        self.assertIn(r"monotonicity and $G(0)=1$", proof)
        self.assertIn(r"Multiplicativity then gives $G(t)=1$", proof)


if __name__ == "__main__":
    unittest.main()
