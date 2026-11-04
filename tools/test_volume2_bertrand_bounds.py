"""Independent exact finite checks of the Bertrand-postulate proof.

The general proof (including all n>=631) is symbolic in ledger DEP-021.
Finite checks reconstruct the prime chain, its coverage, the binomial
factor inequalities, h(512), and monotonic/alternative log estimates.
They are corroboration, not a substitute for the universal proof.
"""
import bisect
import math
import unittest
from pathlib import Path

CH2 = (Path(__file__).resolve().parents[1] /
       "volume2-integers" / "chapters" / "ch02-primes.tex")

CHAIN = (2,3,5,7,13,23,43,83,163,317,631)


def sieve(limit):
    isprime=bytearray(b"\x01")*(limit+1)
    isprime[:2]=b"\x00\x00"
    for p in range(2,math.isqrt(limit)+1):
        if isprime[p]:
            for k in range(p*p,limit+1,p):
                isprime[k]=0
    return [p for p in range(2,limit+1) if isprime[p]]


def h(n):
    return n*math.log(4)/3-(1+math.sqrt(2*n))*math.log(2*n)


def h_derivative(n):
    return (math.log(4)/3-math.log(2*n)/math.sqrt(2*n)
            -(1+math.sqrt(2*n))/n)


def independent_h_over_n(n):
    t=math.sqrt(2*n)
    return 2*math.log(2)/3 - 4*(math.log(t)/t
                               +math.log(t)/(t*t))


class TestBertrandProof(unittest.TestCase):
    def test_all_chain_primes_and_full_small_interval_coverage(self):
        primes=set(sieve(632))
        self.assertTrue(all(p in primes for p in CHAIN))
        self.assertEqual(len(CHAIN),11)
        self.assertTrue(all(v<2*u for u,v in zip(CHAIN,CHAIN[1:])))
        seen=set()
        for n in range(1,631):
            q=1 if n==1 else max(p for p in CHAIN if p<=n)
            qp=next(p for p in CHAIN if p>n)
            self.assertLess(n,qp)
            self.assertLessEqual(qp,2*q)
            self.assertLessEqual(qp,2*n)
            seen.add(qp)
        self.assertEqual(len(seen),11)
        self.assertEqual((1,2), (1, min(CHAIN)))
        self.assertEqual(next(p for p in CHAIN if p>630),631)

    def test_conclusion_for_many_more_n_by_direct_prime_sieve(self):
        primes=sieve(25000)
        for n in range(1,12001):
            ix=bisect.bisect_right(primes,n)
            self.assertLessEqual(primes[ix],2*n)

    def test_h_base_and_analytic_monotonicity(self):
        self.assertAlmostEqual(h(512),math.log(2)*34/3,places=10)
        for n in range(512,20001):
            self.assertGreater(h(n),0)
            self.assertGreater(h_derivative(n),0)
            self.assertGreater(independent_h_over_n(n),0)
            self.assertAlmostEqual(h(n)/n,independent_h_over_n(n),places=11)
        self.assertGreater(h(631),0)
        # A second monotonicity route checks h(n)/n, not h'(n).
        self.assertLess(
            independent_h_over_n(512),
            independent_h_over_n(4096))
        self.assertLess(
            independent_h_over_n(4096),
            independent_h_over_n(65536))

    def test_large_n_contradiction_components(self):
        for n in (512,513,630,631,632,1000,4096,5000,10000):
            lhs=(n/3)*math.log(4)
            rhs=(1+math.sqrt(2*n))*math.log(2*n)
            self.assertGreater(lhs,rhs,n)
            # If (n,2n] had no primes, the printed prime-factor
            # argument would imply exactly the opposite inequality.
        self.assertGreater(2*631/3,math.sqrt(2*631))

    def test_source_lemma_prerequisite_and_boundaries(self):
        text=CH2.read_text(encoding="utf-8")
        self.assertEqual(text.count(r"\label{thm:bertrand}"),1)
        self.assertLess(text.index(r"\label{lem:binom}"),
                        text.index(r"\label{thm:bertrand}"))
        self.assertLess(text.index(r"\label{thm:cheb}"),
                        text.index(r"\label{thm:bertrand}"))
        self.assertIn("n=630",text)
        self.assertIn("n=512",text)
        self.assertIn(r"n\ge631",text)
        self.assertEqual(text.count(r"\section{Exercises}"),1)
        self.assertEqual(text.count(r"\section{Solutions}"),1)


if __name__=="__main__":
    unittest.main()
