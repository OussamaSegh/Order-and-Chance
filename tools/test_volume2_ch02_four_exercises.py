"""Independent arithmetic regressions for four first Chapter 2 exercises.

Two general symbolic checks per exercise appear in DEP-022. This file
supplies finite exact corroboration, notably *different* Euclid-style
mod-4 constructions, modular Sophie Germain factor divisibility,
odd-part exponent obstructions and Fermat pairwise gcd identities.
"""
import math
import unittest
from pathlib import Path

CH2 = (Path(__file__).resolve().parents[1] /
       "volume2-integers" / "chapters" / "ch02-primes.tex")


def prime_factors(n):
    out=[]
    d=2
    while d*d<=n:
        while n%d==0:
            out.append(d)
            n//=d
        d+=1 if d==2 else 2
    if n>1:
        out.append(n)
    return out


def isprime(n):
    return n>=2 and prime_factors(n)==[n]


def fermat(n):
    return 2**(2**n)+1


class TestChapterTwoFourExercises(unittest.TestCase):
    def test_two_different_mod_four_prime_constructions(self):
        candidates=(3,7,11,19,23,31,43,47)
        self.assertTrue(all(isprime(p) and p%4==3 for p in candidates))
        for k in range(9):
            P=math.prod(candidates[:k])
            for N in (4*P-1,2*P+1):
                self.assertEqual(N%4,3)
                self.assertEqual(math.gcd(N,P),1)
                fs=prime_factors(N)
                self.assertEqual(math.prod(fs),N)
                self.assertTrue(any(p%4==3 and p not in candidates[:k]
                                    for p in fs),(k,N,fs))
        self.assertEqual(4*3*7*11-1,13*71)

    def test_mersenne_factor_and_odd_exponent_obstructions(self):
        for n in range(1,111):
            if n>=4:
                a=next((a for a in range(2,math.isqrt(n)+1)
                        if n%a==0),None)
                if a is not None:
                    d=2**a-1
                    self.assertGreater(d,1)
                    self.assertLess(d,2**n-1)
                    self.assertEqual((2**n-1)%d,0)
            twopart=n & -n
            oddpart=n//twopart
            if oddpart>1:
                d=2**twopart+1
                self.assertGreater(d,1)
                self.assertLess(d,2**n+1)
                self.assertEqual((2**n+1)%d,0)
        self.assertEqual(2**11-1,23*89)
        self.assertEqual(2**32+1,641*6700417)
        self.assertEqual(2**1-1,1)
        self.assertEqual(2**1+1,3)

    def test_germain_factor_and_independent_modular_divisibility(self):
        for n in range(2,1001):
            u=n*n-2*n+2
            v=n*n+2*n+2
            z=n**4+4
            self.assertEqual(u*v,z,n)
            self.assertEqual(u,(n-1)**2+1)
            self.assertGreater(u,1)
            self.assertGreater(v,1)
            self.assertLess(u,z)
            # A distinct proof: n² == 2n−2 mod u, so n⁴ == −4.
            self.assertEqual(n*n%u,(2*n-2)%u)
            self.assertEqual((n**4+4)%u,0)
        self.assertEqual(1**4+4,5)

    def test_fermat_telescope_coprimality_and_modular_method(self):
        for n in range(0,13):
            expected=fermat(n)-2
            self.assertEqual(math.prod(fermat(k) for k in range(n)),
                             expected)
            self.assertEqual(expected,2**(2**n)-1)
            for m in range(n):
                self.assertEqual(math.gcd(fermat(m),fermat(n)),1)
                # For n>m, (2^(2^m))^(2^(n−m)) == +1 mod F_m.
                self.assertEqual(fermat(n)%fermat(m),2)
        self.assertEqual(fermat(0),3)
        self.assertEqual(fermat(5),4294967297)

    def test_question_hint_solution_cardinality_and_endpoints(self):
        text=CH2.read_text(encoding="utf-8")
        for key in ("ex:mod4","ex:mersenne","ex:germain","ex:fermatnum"):
            self.assertEqual(text.count(r"\label{"+key+"}"),1)
            self.assertEqual(text.count(r"\begin{hint}{"+key+"}"),1)
            self.assertEqual(text.count(r"\begin{solution}{"+key+"}"),1)
        self.assertIn("when $n=0$, the empty product is $1$",text)
        self.assertIn("2047=23",text)
        self.assertEqual(text.count(r"\begin{exercise}"),11)
        self.assertEqual(text.count(r"\end{exercise}"),11)
        self.assertEqual(text.count(r"\begin{solution}{"),11)
        self.assertEqual(text.count(r"\begin{hint}{"),11)


if __name__=="__main__":
    unittest.main()
