"""Independent finite checks for the three-part central binomial lemma.

The first proof in Chapter 2 uses Pascal-row sums and Legendre floors;
the independent proof in DEP-019 uses induction for the numeric bounds
and the digit-carry theorem previously established in Chapter 1.
These probes corroborate both proofs without replacing either.
"""
import math
import unittest
from pathlib import Path

PRIMES = Path(__file__).resolve().parents[1] / "volume2-integers" / "chapters" / "ch02-primes.tex"


def primes_up_to(limit):
    a = [True] * (limit+1)
    for p in range(2,math.isqrt(limit)+1):
        if a[p]:
            for q in range(p*p,limit+1,p):
                a[q] = False
    return [p for p in range(2,limit+1) if a[p]]


def carries_adding_n_twice(n,p):
    carry=0
    total=0
    a=b=n
    while a or b or carry:
        a,aa=divmod(a,p)
        b,bb=divmod(b,p)
        carry=(aa+bb+carry)//p
        assert carry in (0,1)
        total+=carry
    return total


def prime_exponent(integer,p):
    k=0
    while integer%p==0:
        k+=1
        integer//=p
    return k


class TestCentralBinomialThreePartLemma(unittest.TestCase):
    def test_all_numerical_bounds_via_exact_integers(self):
        for n in range(1,1001):
            B=math.comb(2*n,n)
            self.assertLessEqual(4**n,2*n*B,n)
            self.assertLessEqual(B,4**n,n)
            self.assertLessEqual(math.comb(2*n+1,n),4**n,n)
        self.assertEqual(math.comb(2,1),2)
        self.assertEqual(math.comb(3,1),3)

    def test_prime_exponent_bound_vs_independent_digit_carries(self):
        count=0
        for n in range(1,181):
            B=math.comb(2*n,n)
            for p in primes_up_to(2*n):
                exponent=prime_exponent(B,p)
                carries=carries_adding_n_twice(n,p)
                self.assertEqual(exponent,carries,(n,p))
                self.assertLessEqual(p**exponent,2*n,(n,p))
                if p*p>2*n:
                    self.assertLessEqual(exponent,1,(n,p))
                if n>=5 and 3*p>2*n and p<=n:
                    self.assertEqual(exponent,0,(n,p))
                count+=1
        self.assertEqual(count,7197)

    def test_low_n_caveat_is_real(self):
        # The exclusion p in (2n/3,n] is stated only for n>=5.
        n,p=2,2
        self.assertGreater(3*p,2*n)
        self.assertLessEqual(p,n)
        self.assertEqual(math.comb(2*n,n)%p,0)

    def test_named_lemma_and_hypotheses_are_structural(self):
        content=PRIMES.read_text(encoding="utf-8")
        self.assertEqual(content.count(r"\label{lem:binom}"),1)
        block=content.split(r"\begin{lemma}\label{lem:binom}",1)[1].split(
            r"\end{lemma}",1)[0]
        self.assertIn(r"For $n\ge1$",block)
        self.assertIn(r"a=v_p\binom{2n}n",block)
        self.assertIn(r"n\ge5",block)
        self.assertLess(content.index(r"\label{lem:binom}"),
                        content.index(r"\label{thm:cheb}"))


if __name__=="__main__":
    unittest.main()
