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


    def test_additional_downstream_number_and_scope_reconciliations(self):
        modular = source("volume6-crossroads/chapters/ch12-modular.tex")
        spectral = source("volume12-random-motion/chapters/spectral.tex")
        euler = source("volume15-order-and-chance/chapters/ch11-values.tex")
        logcorr = source("volume12-random-motion/chapters/ch11-logcorrelated.tex")
        self.assertNotIn("Volume~4, Theorems~4.11 and~6.10", modular)
        self.assertIn("Volume~4, Theorems~4.4 and~6.10", modular)
        self.assertNotIn("Cayley's formula again (Volume~4, Chapter~12)", spectral)
        self.assertIn("Cayley's formula, now recovered", spectral)
        self.assertIn("general-filtration martingale convergence theorem of Volume~11", euler)
        self.assertIn("finite interval partitions", euler)
        self.assertIn("Volume~11, Theorem~9.2", logcorr)
        self.assertIn("restricted finite-interval-partition case", logcorr)


    def test_general_independent_series_has_real_maximal_inequality_proof(self):
        ch1 = source("volume11-randomness/chapters/ch01-zero-one.tex")
        ch9 = source("volume11-randomness/chapters/ch09-martingales.tex")
        self.assertIn(r"\label{prop:l2series}", ch1)
        block = ch1.split(r"\label{prop:l2series}", 1)[1].split(r"\end{proof}", 1)[0]
        self.assertNotIn("Volume~4, Theorem~11.12 applies", block)
        self.assertIn("Kolmogorov's maximal inequality", block)
        self.assertIn(r"\sup_{m>N_j}|S_m-S_{N_j}|>2^{-j}", block)
        self.assertIn("even if the supremum is never attained", block)
        self.assertIn(r"|S_m-S_n|\le2^{1-j}", block)
        self.assertIn("Borel--Cantelli", block)
        self.assertIn("Cauchy in $L^2$", block)
        self.assertIn(r"Proposition~\ref{prop:l2series}", ch9)
        self.assertNotIn("by Volume~4, Theorem~11.12", ch9)
        self.assertNotIn("Theorem~10.18", ch1)

    def test_exact_finite_tail_maximal_inequality(self):
        # Independent centred fair signs: check Kolmogorov's bound exactly.
        for weights in [(1, 1, 1), (1, 2, 1, 2), (1, 2, 3, 1, 1)]:
            variance = Fraction(sum(w * w for w in weights))
            for a in (1, 2, 3, 4, 5):
                violations = 0
                for signs in product((-1, 1), repeat=len(weights)):
                    partial = 0
                    maximal = 0
                    for w, s in zip(weights, signs):
                        partial += w * s
                        maximal = max(maximal, abs(partial))
                    violations += maximal >= a
                prob = Fraction(violations, 2 ** len(weights))
                self.assertLessEqual(prob, variance / (a * a))


    def test_finite_conditional_expectation_and_jensen_citation(self):
        original = source("volume4-chance/chapters/ch10-martingales.tex")
        dependent = source("volume6-crossroads/chapters/ch10-random.tex")
        self.assertIn(r"\begin{definition}", original)
        self.assertIn(r"\label{def:condexp}", original)
        self.assertNotIn("Volume~4, Theorem~4.14", dependent)
        self.assertIn("Volume~4, Definition~11.1", dependent)
        self.assertIn("Jensen's inequality and harmonic numbers (Volume~1)", dependent)


    def test_printed_v4_number_contract_in_live_v11(self):
        lln = source("volume11-randomness/chapters/ch02-lln.tex")
        donsker = source("volume11-randomness/chapters/ch03-donsker.tex")
        mart = source("volume11-randomness/chapters/ch09-martingales.tex")
        zeros = source("volume11-randomness/chapters/ch01-zero-one.tex")
        stein = source("volume11-randomness/chapters/ch06-stein.tex")
        large = source("volume11-randomness/chapters/ch07-ldp.tex")
        for doc in (lln, donsker, mart):
            self.assertNotIn("Volume~4, Theorem~11.3", doc)
        self.assertIn("Volume~4, Theorem~11.4", lln)
        self.assertIn("Volume~4, Theorem~11.4", donsker)
        self.assertIn(r"\mathbf1_{\{J\ge j\}}", donsker)
        self.assertIn("conditional mean zero", donsker)
        self.assertIn("Volume~4, Theorem~11.5", mart)
        self.assertNotIn("case~(c)", mart)
        self.assertNotIn("Theorem~10.21", zeros)
        self.assertIn("Theorem~11.13", zeros)
        self.assertNotIn("Volume~4, Proposition~1.8", stein)
        self.assertIn("Volume~4, Exercise~1.1", stein)
        self.assertNotIn("Volume~4, Theorem~4.7", large)
        self.assertIn(r"\theta_x=\ln\frac{x(1-p)}{p(1-x)}", large)
        self.assertIn("matching lower bound follows", large)

    def test_bernoulli_rate_upper_bound_exact_finite_cases(self):
        from math import comb, log
        for p, a in ((Fraction(1,4), Fraction(1,2)),
                     (Fraction(1,3), Fraction(2,3)),
                     (Fraction(1,2), Fraction(3,4))):
            x, y = float(p), float(a)
            I = y*log(y/x) + (1-y)*log((1-y)/(1-x))
            for n in (6, 12, 18):
                tail = sum((Fraction(comb(n,k))*p**k*(1-p)**(n-k)
                           for k in range((n*a).__ceil__(), n+1)), Fraction())
                self.assertLessEqual(float(tail), exp(-n*I) + 1e-13)


if __name__ == "__main__":
    unittest.main()
