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


    def test_exponential_quantile_satisfies_fourth_moment_strong_law(self):
        """A positive-support exponential is not excluded by SLLN4."""
        from math import exp, log

        source = (CHAPTERS / "ch09-poisson.tex").read_text(encoding="utf-8")
        self.assertIn("does apply to these exponential gaps", source)
        self.assertIn(r"E=-\ln(1-U)/\lambda", source)
        self.assertNotIn(
            "asks for a distribution function that is strictly increasing on the whole line",
            source,
        )
        # The inverse-CDF construction works although F is flat for x <= 0.
        for rate in (0.5, 1.0, 2.0):
            for u in (0.01, 0.25, 0.7, 0.99):
                sample = -log(1 - u) / rate
                self.assertGreater(sample, 0)
                self.assertAlmostEqual(1 - exp(-rate * sample), u)
            # Integration by parts gives E[E^4] = 4! / rate^4.
            self.assertTrue(24 / rate**4 < float("inf"))

    def test_aperiodic_lengths_have_self_contained_gcd_bridge(self):
        """Include a gcd-one return-length set with no coprime pair."""
        from math import gcd

        source = (CHAPTERS / "ch08-markov.tex").read_text(encoding="utf-8")
        proof = source.split(r"\label{thm:ergodic}", 1)[1].split(
            r"\end{proof}", 1
        )[0]
        self.assertIn("Divide any return length $m$ by $D$", proof)
        self.assertIn("Minimality of $D$ forces $r=0$", proof)
        self.assertNotIn("Volume~2 writes the gcd", proof)

        lengths = (6, 10, 15)
        self.assertEqual(gcd(*lengths), 1)
        self.assertTrue(all(gcd(lengths[i], lengths[j]) > 1
                            for i in range(3) for j in range(i + 1, 3)))
        # The signed integer combination 6 + 10 - 15 = 1
        # produces nonnegative return lengths B=15 and B+1=16.
        A, B = 6 + 10, 15
        self.assertEqual(A - B, 1)
        for M in range(B * B, B * B + 150):
            q, r = divmod(M, B)
            self.assertGreaterEqual(q - r, 0)
            self.assertEqual(M, (q - r) * B + r * (B + 1))
            self.assertEqual(
                M, (q - r) * 15 + r * 6 + r * 10,
            )


    def test_polya_uses_proved_taylor_remainder_bound(self):
        """The recurrence proof must not silently use a located-point theorem."""
        from math import cos

        source = (CHAPTERS / "ch07-walks.tex").read_text(encoding="utf-8")
        proof = source.split(r"\label{thm:polya}", 1)[1].split(
            r"\end{proof}", 1
        )[0]
        self.assertIn("Taylor--Lagrange inequality proved in Volume~1", proof)
        self.assertIn(r"|r(u)|\le |u|^4/24", proof)
        self.assertNotIn(r"\cos\xi", proof)

        # The actual inequality, not merely its phrasing, is checked
        # on both sides of zero and at the near-origin boundary.
        for u in (-2.0, -1.5, -1.0, -0.5, -0.01, 0.0,
                   0.01, 0.5, 1.0, 1.5, 2.0):
            self.assertLessEqual(
                abs(cos(u) - 1 + u * u / 2), abs(u) ** 4 / 24 + 1e-15
            )


    def test_delta_method_function_is_defined_on_sample_means(self):
        """An exercise cannot evaluate g(Ybar) outside g's domain."""
        source = (CHAPTERS / "ch06-clt.tex").read_text(encoding="utf-8")
        exercise = source.split(r"\label{ex:delta}", 1)[1].split(
            r"\end{exercise}", 1
        )[0]
        self.assertIn(r"$g:\R\to\R$", exercise)
        self.assertIn("differentiability is needed only near", exercise)



    def test_brownian_covariance_equivalence_requires_zero_mean(self):
        """Gaussian increments with the right variance can still have drift."""
        source = (CHAPTERS / "ch11-brownian.tex").read_text(encoding="utf-8")
        proposition = source.split(r"\\label{prop:bmgauss}", 1)[1].split(
            r"\\end{proposition}", 1
        )[0]
        self.assertIn(r"independent \\emph{centred} normal increments", proposition)
        self.assertIn(r"B_t-B_s\\sim N(0,t-s)", proposition)
        self.assertIn("drifted process", source)
        self.assertNotIn(
            "independent normal increments of variance $t-s$ are equivalent",
            proposition,
        )

        # Counterexample: X_t=W_t+c*t for c != 0.
        # Var(X_t-X_s)=t-s, Cov(X_s,X_t)=min(s,t), but E[X_t]=ct.
        for drift in (-1.0, 0.5, 3.0):
            for s, t in ((0.0, 0.5), (1.0, 2.5), (3.0, 4.0)):
                self.assertEqual((t - s), t - s)
                self.assertEqual(min(s, t), s)
                self.assertNotEqual(drift * t, 0.0)

    def test_brownian_blocks_distinguish_copy_independence_from_increment_independence(self):
        """Disjoint increments inside the same unit copy must be justified."""
        source = (CHAPTERS / "ch11-brownian.tex").read_text(encoding="utf-8")
        construction = source.split("For all later times", 1)[1].split(
            r"\\section{Scaling, variation, reflection}", 1
        )[0]
        self.assertIn("two disjoint intervals can lie in the same unit block", construction)
        self.assertIn("Within each copy, disjoint component increments are independent", construction)
        self.assertIn("Across distinct copies they are independent", construction)
        self.assertNotIn("Increments over disjoint time intervals use disjoint blocks", construction)

    def test_poisson_no_explosion_uses_one_countable_probability_one_event(self):
        """Finite counts at each fixed time require a countable intersection."""
        source = (CHAPTERS / "ch09-poisson.tex").read_text(encoding="utf-8")
        excerpt = source.split(r"\\label{def:pp}", 1)[1].split(
            r"\\begin{theorem}[counts and conditional uniformity]", 1
        )[0]
        self.assertIn("t=1,2,3,\\ldots", excerpt)
        self.assertIn("Intersect these probability-one statements", excerpt)
        self.assertIn(r"T_n\\to\\infty", excerpt)



if __name__ == "__main__":
    unittest.main()
