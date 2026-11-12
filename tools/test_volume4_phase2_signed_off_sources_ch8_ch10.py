"""Pin exact TeX blobs underlying sole-validator Ch8 and Ch10 math signoff.

These are structural regression guards plus exact arithmetic checks.
They are not proofs of recurrence, Poisson independence, or optional stopping.
"""
import hashlib
import math
import re
import unittest
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "volume4-chance" / "chapters"
SPECS = {
 "ch07-walks.tex": {
   # Reread 2026-11-11 for the factor 1/4 in the arcsine identity (V4-22)
   # and the first boundary vertex in the harmonic argument (V4-23).
   # Reread 2026-11-11 for the ruin constants and the iterated integral (V4R2-03, V4R2-04). Labels unchanged.
   # Writer repair the same day: return attribution, half-line Gaussian citation, meeting sign (V4R2-18, V4R2-19, V4R2-20). Not an independent sign-off.
   # 2026-11-11: thm:twosat appended after the existing claims. Exercise labels unchanged.
   # The new proof was checked in this preparation. Not an independent sign-off.
   "sha": "e45393f9961dae38495ddee1eb39594ccd5655cc",
   "proofs": "thm:rwreflect thm:ruin prop:duration prop:visits thm:polya thm:arcsine prop:harmonic thm:arcsinelimit lem:centralbin thm:twosat".split(),
   "ex": "ex:ballotwalk ex:maxlaw ex:timepositive ex:unfair ex:meet ex:escape ex:exittime ex:electric".split(),
 },
 "ch09-poisson.tex": {
   # Caption ink word only ("blue" -> "charcoal"). Proofs and exercises
   # are unchanged from 6de4e7e1fd5c6369d553e45190e54807c553a743.
   # Reread 2026-11-11 for G(0) in {0,1} and the rational powers (V4-08).
   "sha": "c4c36ee1b854ebc7b8a34a35f77f5c4b952549af",
   "proofs": "prop:memoryless lem:gamma thm:uniform lem:colouring thm:increments thm:thinning thm:superpose prop:residual prop:onesidedgap prop:race thm:lecam thm:mm1 prop:emptiness".split(),
   "ex": "ex:twoexp ex:minexp ex:bus ex:lecamnum ex:mm1mean ex:emptycheck ex:superpose ex:firstarrival".split(),
 },
}

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\x00" + data).hexdigest()

def proof_labels(src):
    return re.findall(r"\\begin\{(?:theorem|lemma|proposition)\}(?:\[[^\]]*\])?\\label\{([^}]+)\}",src)

def block_labels(src,typ):
    if typ=="exercise":
        return re.findall(r"\\begin\{exercise\}(?:\[[^\]]*\])?\\label\{([^}]+)\}",src)
    return re.findall(r"\\begin\{" + typ + r"\}\{([^}]+)\}",src)


class TestVolume4Ch8Ch10MathematicalScope(unittest.TestCase):
    def test_source_exact_blob_and_complete_proof_inventory(self):
        for filename,spec in SPECS.items():
            with self.subTest(filename=filename):
                data=(ROOT/filename).read_bytes()
                self.assertEqual(git_blob_sha(data),spec["sha"],
                                 "Source changed: revalidate mathematical acceptance")
                source=data.decode("utf-8")
                self.assertEqual(proof_labels(source),spec["proofs"])
                for typ in ("exercise","hint","solution"):
                    self.assertEqual(block_labels(source,typ),spec["ex"])

    def test_walk_return_probabilities_and_arcsine_exact_paths(self):
        for n in range(1,7):
            last=[0]*(n+1)
            count_nonnegative=0
            for steps in product((-1,1),repeat=2*n):
                cur,latest,all_nonnegative=0,0,True
                for i,s in enumerate(steps,1):
                    cur+=s
                    if cur==0: latest=i
                    if cur<0: all_nonnegative=False
                last[latest//2]+=1
                count_nonnegative+=int(all_nonnegative)
            total=4**n
            u=lambda k: Q(math.comb(2*k,k),4**k)
            self.assertEqual(Q(count_nonnegative,total),u(n))
            for k,value in enumerate(last):
                self.assertEqual(Q(value,total),u(k)*u(n-k))
            self.assertEqual(sum(last),total)

    def test_poisson_colour_factorisation_finite_coefficients(self):
        # Independent discrete mass calculation, checking colouring/Poisson
        # factorization for k=2 categories and several rational parameters.
        from math import factorial
        for lam,p in [(Q(1,2),Q(1,3)),(Q(3,2),Q(3,4)),(Q(4,1),Q(1,2))]:
            for a in range(0,6):
                for b in range(0,6):
                    # Both sides share exp(-lambda), so compare rational
                    # coefficients exactly instead of floating exponentials.
                    left=lam**(a+b)*math.comb(a+b,a)*p**a*(1-p)**b/factorial(a+b)
                    right=(lam*p)**a/factorial(a)*(lam*(1-p))**b/factorial(b)
                    self.assertEqual(left,right)


if __name__=="__main__":
    unittest.main()
