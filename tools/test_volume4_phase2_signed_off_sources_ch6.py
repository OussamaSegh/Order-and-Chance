"""Protect exact mathematical acceptance of printed Volume 4 Chapter 6.

These are source-identity and concrete numerical regressions, NOT a formal
proof of the general CLT, Fourier inversion or Gaussian independence.
"""
import hashlib
import re
import unittest
from fractions import Fraction as F
from math import comb, erfc, exp, factorial, sqrt
from pathlib import Path

SOURCE=Path(__file__).resolve().parents[1]/"volume4-chance"/"chapters"/"ch06-clt.tex"
# Reread 2026-11-11 for V4-01, V4-02, V4-04, V4-06, V4-07, V4-18, V4-19.
# Numbered labels are unchanged. This pin is identity, not a proof.
# Reread 2026-11-11 for the unnumbered characteristic-function label (V4R2-08). Numbered labels unchanged.
# 2026-11-13: V4-02. The clip of the other blocks is charged to the tails
# E[Q_j^2 1_{|Q_j|>K}], and the square is factored so that bound tends to 0.
# Numbered labels unchanged. This pin is identity, not a proof.
# 2026-11-20: series review V4-003, V4-004, V4-005, V4-006, V4-016, V4-017, V4-024.
# Numbered labels unchanged. Not a new sign-off.
# Second review the same day: continuity points are constructed, the open pieces do not
# contain 0, and the sample-variance limit does not send n to infinity before M.
# Not a new sign-off.
# 2026-11-22: Independent reread of the new exact dice count. Existing proof and exercise labels match.
# 2026-11-27: the strong-law cover is the finite-bit gap, and the square is a sum of clips.
# Labels unchanged. Not a new sign-off.
# 2026-11-27 round 2: the single-index moment groups as E[Y], and the CLT cutoffs name their directions.
# Not a new sign-off.
# 2026-11-27 round 3: Gaussian covariance and the two squares are clipped before the product, and the sample second moment uses four allowances of ε/4.
# Not a new sign-off.
SHA="0c95109cfba2e5c795b880e239141c14065568ee"
PROOFS="prop:modes prop:cdf thm:slln4 thm:gc lem:diffint prop:cfexamples thm:cfconv thm:inversion lem:normalsum thm:lindeberg cor:clt thm:local prop:cyclebern thm:gaussvec".split()
EX="ex:slutsky ex:confidence ex:delta ex:cauchyclt ex:poissonhalf ex:returns ex:thirdmoment ex:cyclesclt".split()

def git_blob(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\x00"+data).hexdigest()

class TestChapter6VerifiedSourceAndNumerics(unittest.TestCase):
    def test_exact_blob_and_all_theorem_proposition_lemma_theoremx_corollary_labels(self):
        data=SOURCE.read_bytes()
        self.assertEqual(git_blob(data),SHA,"Math acceptance must be repeated if source changes")
        tex=data.decode()
        self.assertEqual(
          re.findall(r"\\begin\{(?:theorem|theoremx|proposition|lemma|corollary)\}(?:\[[^\]]*\])?\\label\{([^}]+)\}",tex),PROOFS)
        for typ in ("exercise","hint","solution"):
            pattern=(r"\\begin\{exercise\}(?:\[[^\]]*\])?\\label\{([^}]+)\}" if typ=="exercise"
                     else r"\\begin\{"+typ+r"\}\{([^}]+)\}")
            self.assertEqual(re.findall(pattern,tex),EX)

    def test_exact_cycle_permutation_variance_and_local_binomial_counts(self):
        # Bernoulli(1/k) cycle indicators checked on all n up to 14.
        for n in range(2,15):
            mean=sum((F(1,k) for k in range(1,n+1)),F(0))
            variance=sum((F(k-1,k*k) for k in range(1,n+1)),F(0))
            self.assertEqual(variance,mean-sum((F(1,k*k) for k in range(1,n+1)),F(0)))
            self.assertGreater(variance,F(0))
        for m in range(1,30):
            u=F(comb(2*m,m),4**m)
            self.assertGreaterEqual(float(u),1/(2*sqrt(m))-1.e-15)
            # mean-zero fair walk has exact middle-binomial return mass u.
            self.assertEqual(u*4**m,comb(2*m,m))

    def test_normal_cdf_smooth_cutoff_polynomial(self):
        # q(u)=1-35u^4+84u^5-70u^6+20u^7:
        # first, second and third derivatives vanish at 0 and 1.
        terms={0:1,4:-35,5:84,6:-70,7:20}
        def nth_derivative_at(x,d):
            return sum(F(c*factorial(k),factorial(k-d))*(F(x)**(k-d))
                       for k,c in terms.items() if k>=d)
        for d in (1,2,3):
            self.assertEqual(nth_derivative_at(0,d),F(0))
            self.assertEqual(nth_derivative_at(1,d),F(0))
        self.assertEqual(nth_derivative_at(0,0),F(1))
        self.assertEqual(nth_derivative_at(1,0),F(0))
        for i in range(0,101):
            x=F(i,100)
            v=nth_derivative_at(x,0)
            self.assertGreaterEqual(v,0)
            self.assertLessEqual(v,1)

    def test_dice_tail_count_and_printed_comparisons(self):
        counts = [1]
        for _ in range(100):
            counts = [sum(counts[max(0, total - 6):total]) for total in range(len(counts) + 6)]
        tail = F(sum(counts[400:]), 6**100)
        # Reflect the rolls, subtract one from each, and count total <= 200.
        by_inclusion_exclusion = sum(
            (-1)**j * comb(100, j) * comb(300 - 6*j, 100) for j in range(34)
        )
        self.assertEqual(sum(counts), 6**100)
        self.assertEqual(tail, F(by_inclusion_exclusion, 6**100))
        self.assertEqual(f"{float(tail):.8f}", "0.00182302")
        self.assertEqual(f"{erfc(sqrt(30/7)) / 2:.8f}", "0.00170740")
        self.assertEqual(f"{exp(-2):.8f}", "0.13533528")


if __name__=="__main__":
    unittest.main()
