"""Protect exact mathematical acceptance of printed Volume 4 Chapter 6.

These are source-identity and concrete numerical regressions, NOT a formal
proof of the general CLT, Fourier inversion or Gaussian independence.
"""
import hashlib
import re
import unittest
from fractions import Fraction as F
from math import comb, factorial, sqrt
from pathlib import Path

SOURCE=Path(__file__).resolve().parents[1]/"volume4-chance"/"chapters"/"ch06-clt.tex"
SHA="8b1863f270060898cb28eaa9eb3672b18fdd8847"
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

if __name__=="__main__":
    unittest.main()
