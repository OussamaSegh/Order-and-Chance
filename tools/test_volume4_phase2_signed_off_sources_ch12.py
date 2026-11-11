"""Pin Chapter 12 sole-validator mathematical audit to the actual corrected TeX.

These tests guard source identity, full claim/exercise inventory and exact
finite-dimensional calculations. They cannot establish the general proofs.
"""
import hashlib
import re
import unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "volume4-chance" / "chapters" / "ch11-brownian.tex"
# Caption ink words only. The reviewed mathematics is the predecessor blob
# 7c576031edc38e04019336de0a0a1a1bfefeb2b1; the diff is the reflection caption.
# Reread 2026-11-11 for the existence outer-content argument and the reflection window (V4R2-01, V4R2-10, V4R2-15, V4R2-16). Labels unchanged.
BLOB = "c758f4a72b98528b13ab3b70c398c39a576b977d"
PROOFS = """prop:bmgauss lem:levylevel thm:levy prop:scaling lem:squares
thm:qv thm:dyadicito thm:pwz prop:bmmart prop:restart
thm:reflection prop:bmsquare""".split()
EXERCISES = """ex:maxjoint ex:bridge ex:zeros ex:hittingdensity
ex:pvariation ex:putcall ex:onestep""".split()


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\x00" + data).hexdigest()


def brownian_cov(s, t):
    return min(s, t)


class TestChapter12SoleValidatorSourceLock(unittest.TestCase):
    def test_exact_source_blob_and_complete_label_inventories(self):
        data = SOURCE.read_bytes()
        self.assertEqual(git_blob_sha(data), BLOB, "Manuscript changed; re-review Chapter 12 mathematics")
        src = data.decode("utf-8")
        proof_pattern = r"\\begin\{(?:theorem|lemma|proposition)\}(?:\[[^\]]*\])?\\label\{([^}]+)\}"
        self.assertEqual(re.findall(proof_pattern, src), PROOFS)
        self.assertEqual(src.count(r"\begin{corollaryx}[variation]"), 1,
                         "Re-review the unlabeled variation corollary as well")
        self.assertEqual(src.count(r"\end{corollaryx}"), 1)
        for kind in ("exercise", "hint", "solution"):
            regex = (r"\\begin\{exercise\}(?:\[[^\]]*\])?\\label\{([^}]+)\}"
                     if kind == "exercise" else r"\\begin\{" + kind + r"\}\{([^}]+)\}")
            self.assertEqual(re.findall(regex, src), EXERCISES)
        self.assertEqual(src.count(r"\begin{proof}"), len(PROOFS) + 1)

    def test_independent_normal_grid_covariances(self):
        # Algebraically independent check for all interval pairs on fine grids:
        # Cov(B_b-B_a, B_d-B_c) equals the length of their overlap.
        for denom in (2, 3, 4, 7):
            ts = [F(i, denom) for i in range(denom + 1)]
            for a, b in product(ts, repeat=2):
                if not a < b:
                    continue
                for c, d in product(ts, repeat=2):
                    if not c < d:
                        continue
                    cv = (brownian_cov(b, d) - brownian_cov(b, c)
                          - brownian_cov(a, d) + brownian_cov(a, c))
                    self.assertEqual(cv, max(F(0), min(b, d) - max(a, c)))
                    self.assertEqual(cv, F(0) if b <= c or d <= a else cv)

    def test_bridge_covariance_and_independence_from_endpoint(self):
        for den in (2, 3, 5, 8):
            for i, j in product(range(den + 1), repeat=2):
                s, t = F(i, den), F(j, den)
                cov = brownian_cov(s, t) - s * t
                algebra = (brownian_cov(s, t) - t * brownian_cov(s, F(1))
                           - s * brownian_cov(F(1), t) + s * t * brownian_cov(F(1), F(1)))
                self.assertEqual(algebra, cov)
                self.assertEqual(brownian_cov(s, F(1)) - s * brownian_cov(F(1), F(1)), 0)
                self.assertGreaterEqual(cov if s == t else F(1), 0)

    def test_finite_partition_quadratic_variation(self):
        # For independent N(0,h_j), exact mean/variance of sum of squares.
        for t in (F(0), F(1, 3), F(2, 5), F(1)):
            for n in range(1, 11):
                h = F(1, 2**n)
                full_count = (t / h).__floor__()
                t_n = full_count * h
                remainder = t - t_n
                lengths = [h] * full_count + ([remainder] if remainder else [])
                self.assertEqual(sum(lengths, F(0)), t)
                self.assertEqual(sum((2 * x * x for x in lengths), F(0)),
                                 2 * full_count * h * h + 2 * remainder * remainder)
                self.assertLessEqual(sum((2 * x * x for x in lengths), F(0)), 2 * t * h)
                self.assertEqual(2 * full_count * h * h, 2 * t_n * h)

    def test_put_call_replication_payoff_identity(self):
        for stock in (F(0), F(1), F(9, 4), F(5), F(20)):
            for strike in (F(0), F(1), F(3), F(8)):
                self.assertEqual(max(stock - strike, F(0)) -
                                 max(strike - stock, F(0)), stock - strike)


if __name__ == "__main__":
    unittest.main()
