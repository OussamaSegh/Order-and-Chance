"""Independent finite regression probes for Chapter 4 fundamentals (DEP-028).

Symbolic Pass A and independent Pass B are recorded in the ledger.
Numerical probes here cannot establish general identities by themselves.
"""
import math
import unittest
from pathlib import Path

SOURCE = (Path(__file__).resolve().parents[1] /
          "volume2-integers" / "chapters" / "ch04-arithmetic-functions.tex")


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    if n == 1:
        return 1
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            sign = -sign
        p += 1
    if n > 1:
        sign = -sign
    return sign


def omega(n):
    return sum(abs(mobius(d)) for d in divisors(n) if d > 1
               and all(d % q for q in range(2, math.isqrt(d) + 1))
               and d != 1)


def convolve(f, g, n):
    return sum(f(d) * g(n // d) for d in divisors(n))


def one(n):
    return 1


def epsilon(n):
    return int(n == 1)


class TestChapterFourFundamentals(unittest.TestCase):
    def test_dirichlet_convolution_association_unit_commutation(self):
        fs=(one,epsilon,lambda n:n,lambda n:n*n,mobius)
        for n in range(1,121):
            for f in fs:
                self.assertEqual(convolve(f,epsilon,n),f(n))
                for g in fs:
                    self.assertEqual(convolve(f,g,n),convolve(g,f,n))
                    for h in fs[:3]:
                        left=convolve(lambda d:convolve(f,g,d),h,n)
                        right=convolve(f,lambda d:convolve(g,h,d),n)
                        self.assertEqual(left,right,(n,f,g,h))

    def test_multiplicative_convolution_factorization(self):
        fs=(one,mobius,lambda n:n,epsilon)
        for f in fs:
            for g in fs:
                for a in range(1,40):
                    for b in range(1,40):
                        if math.gcd(a,b)==1:
                            self.assertEqual(convolve(f,g,a*b),
                                convolve(f,g,a)*convolve(f,g,b),(a,b))

    def test_mobius_inversion_for_a_nonmultiplicative_function(self):
        f=lambda n:(n%7)**2-(n%5)
        for n in range(1,301):
            self.assertEqual(convolve(mobius,one,n),epsilon(n))
            g=lambda m:sum(f(d) for d in divisors(m))
            self.assertEqual(sum(mobius(d)*g(n//d) for d in divisors(n)),
                             f(n))

    def test_360_by_prime_powers_and_direct_divisor_enumeration(self):
        n=360
        ds=divisors(n)
        self.assertEqual(len(ds),24)
        self.assertEqual(sum(ds),1170)
        self.assertEqual(sum(math.gcd(k,n)==1 for k in range(1,n+1)),96)
        self.assertEqual(4*3*2,24)
        self.assertEqual(15*13*6,1170)
        self.assertEqual(n-180-120-72+60+36+24-12,96)

    def test_mobius_divisor_identities_by_subset_and_local_products(self):
        for n in range(1,501):
            ds=divisors(n)
            ps=[p for p in range(2,n+1) if n%p==0 and
                all(p%q for q in range(2,math.isqrt(p)+1))]
            r=len(ps)
            self.assertEqual(sum(abs(mobius(d)) for d in ds),2**r,n)
            self.assertEqual(sum(mobius(d)*len(divisors(d)) for d in ds),
                             (-1)**r,n)
        self.assertEqual(sum(abs(mobius(d)) for d in divisors(1)),1)

    def test_source_has_first_use_and_four_matched_items(self):
        s=SOURCE.read_text(encoding="utf-8")
        for key in ("prop:conv","thm:mobius","ex:360","ex:muid"):
            self.assertEqual(s.count(r"\\label{"+key+"}"),1)
        for key in ("ex:360","ex:muid"):
            self.assertEqual(s.count(r"\\begin{hint}{"+key+"}"),1)
            self.assertEqual(s.count(r"\\begin{solution}{"+key+"}"),1)
        self.assertLess(s.index(r"\\label{prop:conv}"),
                        s.index(r"\\label{thm:mobius}"))
        self.assertLess(s.index(r"\\label{thm:mobius}"),
                        s.index(r"\\label{ex:360}"))


if __name__=="__main__":
    unittest.main()
