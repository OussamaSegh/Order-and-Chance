"""Independent finite arithmetic and source guards for two Phase 2 proof gaps.

These checks confirm Gaussian covariance algebra and the Pólya urn finite-grid
distribution. They cannot certify independent mathematical refereeing.
"""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import unittest

CHAPTERS = Path(__file__).resolve().parents[1] / "volume4-chance" / "chapters"


def covariance_of_brownian_increments(a, b, c, d):
    """Expand Cov(B_b-B_a, B_d-B_c) from Cov(B_s,B_t)=min(s,t)."""
    return min(b, d) - min(b, c) - min(a, d) + min(a, c)


def lower_cutoff(y, x, eta):
    if y <= x - eta:
        return 1.0
    if y >= x:
        return 0.0
    return float((x - y) / eta)


def upper_cutoff(y, x, eta):
    if y <= x:
        return 1.0
    if y >= x + eta:
        return 0.0
    return float((x + eta - y) / eta)


class TestVolume4ProofCompletion(unittest.TestCase):
    def test_brownian_increment_covariance_and_gaussian_vector_hypothesis(self):
        source = (CHAPTERS / "ch11-brownian.tex").read_text(encoding="utf-8")
        proof = source.split(r"\label{prop:bmgauss}", 1)[1].split(
            r"\end{proof}", 1
        )[0]
        # Pairwise normal marginals are insufficient: the full vector must be
        # represented as sums of jointly independent Gaussian increments.
        self.assertIn("a linear image of independent centred normals", proof)
        self.assertIn("jointly centred Gaussian vector", proof)
        self.assertIn("Any finite set of disjoint intervals", proof)
        self.assertIn(r"N(0,t-s)", proof)

        grid = [Fraction(0), Fraction(1, 8), Fraction(3, 8),
                Fraction(1, 2), Fraction(7, 8), Fraction(1)]
        variances = [grid[i] - grid[i - 1] for i in range(1, len(grid))]
        for i in range(1, len(grid)):
            for j in range(1, len(grid)):
                # B_{t_i} and B_{t_j} are triangular sums of independent
                # increments. Their only shared summands are indexed <= min.
                covariance_from_independent_normals = sum(
                    variances[:min(i, j)], Fraction(0)
                )
                self.assertEqual(covariance_from_independent_normals,
                                 min(grid[i], grid[j]))

        intervals = [(grid[i], grid[j]) for i in range(len(grid))
                     for j in range(i + 1, len(grid))]
        for a, b in intervals:
            for c, d in intervals:
                self.assertEqual(
                    covariance_of_brownian_increments(a, b, c, d),
                    max(Fraction(0), min(b, d) - max(a, c)),
                )

    def test_polya_finite_law_and_continuous_test_sandwich(self):
        source = (CHAPTERS / "ch10-martingales.tex").read_text(encoding="utf-8")
        proof = source.split(r"\label{thm:polyaurn}", 1)[1].split(
            r"\end{proof}", 1
        )[0]
        self.assertIn("To recover the distribution function", proof)
        self.assertIn(r"g^-_\eta(y)\le\mathbf1_{\{y\le x\}}\le g^+_\eta(y)", proof)
        self.assertIn(r"x-\eta\le P(M_\infty\le x)\le x+\eta", proof)
        self.assertIn(r"P(M_\infty=0)", proof)
        for n in range(1, 21):
            # Every sequence with j red draws has probability
            # j! (n-j)!/(n+1)!; summing the C(n,j) such sequences
            # gives exactly 1/(n+1), for *each* j.
            for j in range(n + 1):
                mass = Fraction(comb(n, j) * factorial(j) * factorial(n-j),
                                factorial(n + 1))
                self.assertEqual(mass, Fraction(1, n + 1))

        for x, eta in [(Fraction(1, 4), Fraction(1, 16)),
                       (Fraction(1, 2), Fraction(1, 8)),
                       (Fraction(3, 4), Fraction(1, 16))]:
            # The continuous cutoffs squeeze 1_{y<=x}, including endpoints.
            for k in range(101):
                y = Fraction(k, 100)
                self.assertLessEqual(lower_cutoff(y, x, eta),
                                     float(y <= x))
                self.assertLessEqual(float(y <= x),
                                     upper_cutoff(y, x, eta))
            for n in (128, 1024):
                grid = [Fraction(k, n + 2) for k in range(1, n + 2)]
                cdf = Fraction(sum(y <= x for y in grid), n + 1)
                self.assertLessEqual(abs(cdf - x), Fraction(2, n + 1))
                lo = sum(lower_cutoff(y, x, eta) for y in grid) / (n + 1)
                hi = sum(upper_cutoff(y, x, eta) for y in grid) / (n + 1)
                self.assertLessEqual(lo, float(cdf) + 1e-12)
                self.assertLessEqual(float(cdf), hi + 1e-12)
                # The integrals of the lower/upper trapezoids are
                # x - eta/2 and x + eta/2 respectively.
                self.assertLess(abs(lo - float(x - eta / 2)), 2 / (n + 1))
                self.assertLess(abs(hi - float(x + eta / 2)), 2 / (n + 1))


if __name__ == "__main__":
    unittest.main()
