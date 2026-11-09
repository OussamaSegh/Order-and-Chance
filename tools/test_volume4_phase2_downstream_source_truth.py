"""Guard corrected Volume-4-attribution and scope in live downstream volumes.

Structural guards prevent a phantom V4 citation reappearing. The exact finite
inequality exercise is corroborating arithmetic, not a proof of Azuma.
"""
from itertools import product
from math import exp
from pathlib import Path
from fractions import Fraction
import unittest

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return (ROOT / path).read_text(encoding="utf-8")


class TestDownstreamSourceTruth(unittest.TestCase):
    def test_no_nonexistent_shuffle_proposition(self):
        text = source("volume11-randomness/chapters/shuffling.tex")
        self.assertNotIn("Proposition~8.16", text)
        self.assertNotIn("Volume~4, Chapter~8", text)
        self.assertNotIn("Volume~4 (Chapter~8)", text)
        self.assertIn(r"Proposition~\ref{prop:eigenvalues}", text)
        self.assertIn("Chapter~9", text)

    def test_v4_measure_scope_does_not_import_tonelli(self):
        text = source("volume7-spaces/chapters/ch08-products.tex")
        self.assertNotIn("Volume~4 admitted Tonelli and Fubini", text)
        self.assertIn("without importing general Tonelli or Fubini", text)

    def test_berry_esseen_theorem_referred_to_actual_proof(self):
        origin = source("volume11-randomness/chapters/ch04-clt.tex")
        dependent = source("volume6-crossroads/chapters/ch09-erdoskac.tex")
        self.assertIn(r"\begin{theorem}[Berry--Esseen]\label{thm:berryesseen}", origin)
        self.assertNotIn("Berry--Esseen theorem (stated in Volume~4)", dependent)
        self.assertIn("Berry--Esseen theorem (proved in Volume~11, Chapter~4)", dependent)

    def test_bounded_difference_derived_from_real_azuma(self):
        parent = source("volume4-chance/chapters/ch10-martingales.tex")
        downstream = source("volume11-randomness/chapters/ch08-concentration.tex")
        self.assertIn(r"\begin{theorem}[Azuma]\label{thm:azuma}", parent)
        self.assertNotIn("Volume~4, Theorem~10.25", downstream)
        self.assertIn("Volume~4, Theorem~11.10", downstream)
        self.assertIn(r"M_i=\mathbb E[F\mid X_1,\dots,X_i]", downstream)

    def test_general_filtration_l2_not_attributed_to_restricted_v4(self):
        v4 = source("volume4-chance/chapters/ch10-martingales.tex")
        v11 = source("volume11-randomness/chapters/ch09-martingales.tex")
        v12 = source("volume12-random-motion/chapters/ch03-martingales.tex")
        self.assertIn(r"\begin{theorem}[uniformly integrable martingales]\label{thm:uimart}", v11)
        self.assertIn("finite half-open interval", v12)
        self.assertIn("Volume~11, Theorem~9.2", v12)
        self.assertIn(r"\mathbb E(M_n-M_m)^2=\mathbb EM_n^2-\mathbb EM_m^2", v12)
        self.assertIn("finite", v4.split(r"\label{thm:L2conv}", 1)[1][:800])
        self.assertIn("dyadic partitions of $[0,t]$", v12)

    def test_independent_finite_weighted_coin_bound(self):
        # Validate a separate finite bounded-differences test model exactly:
        # X_i fair bits, F=sum_i c_i X_i, changing bit i changes F by c_i.
        # Azuma's two-sided bound must dominate the actual 2^n tail.
        for weights in [(1, 2, 1), (1, 1, 1, 1), (2, 3, 1, 2)]:
            outcomes = [sum(Fraction(w * x) for w, x in zip(weights, bits))
                        for bits in product((0, 1), repeat=len(weights))]
            mean = sum(outcomes, Fraction()) / len(outcomes)
            C = sum(w * w for w in weights)
            for t in [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]:
                actual = Fraction(sum(abs(v - mean) >= t for v in outcomes), len(outcomes))
                bound = 2 * exp(-float(t * t) / (2 * C))
                self.assertLessEqual(float(actual), bound + 1e-13)


if __name__ == "__main__":
    unittest.main()
