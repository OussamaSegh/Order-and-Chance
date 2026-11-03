"""Finite independent checks for the relocated trigonometric reciprocity and
Euler--Jacobi primality exercises in printed Chapter 6.

A finite sample does not prove either theorem; the manuscript supplies
the symbolic polynomial and CRT arguments.
"""
import math
import unittest
from pathlib import Path


CH6 = (Path(__file__).resolve().parents[1] / "volume2-integers"
       / "chapters" / "ch06-quadratic-reciprocity.tex")


def primes_to(n):
    return [p for p in range(2, n + 1)
            if all(p % d for d in range(2, math.isqrt(p) + 1))]


def legendre(a, p):
    if a % p == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1


def jacobi(a, n):
    """Euclidean reciprocity algorithm; n must be positive odd."""
    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0


def polynomial_value(coeff, y):
    return sum(c*y**i for i, c in enumerate(coeff))


def chebyshev_odd_polynomials(n):
    """sin((2m+1)x)/sin(x) as a polynomial in y=sin(x)^2."""
    seq = [[1], [3, -4]]
    while len(seq) <= n:
        previous, current = seq[-2:]
        next_poly = [0]*(len(current)+1)
        for j, c in enumerate(current):
            next_poly[j] += 2*c
            next_poly[j+1] -= 4*c
        for j, c in enumerate(previous):
            next_poly[j] -= c
        while next_poly and next_poly[-1] == 0:
            next_poly.pop()
        seq.append(next_poly)
    return seq[:n+1]


class TestRelocatedEisensteinEuler(unittest.TestCase):
    def test_eisenstein_polynomial_independent_recurrence(self):
        polynomials = chebyshev_odd_polynomials(13)
        for m, coeff in enumerate(polynomials):
            q = 2*m+1
            self.assertEqual(coeff[-1], (-4)**m)
            for x in (0.19, 0.38, 0.71, 1.08):
                with self.subTest(q=q, x=x):
                    actual = math.sin(q*x)/math.sin(x)
                    via_recurrence = polynomial_value(coeff, math.sin(x)**2)
                    via_roots = (-4)**m*math.prod(
                        math.sin(x)**2-(math.sin(2*math.pi*k/q))**2
                        for k in range(1,m+1)
                    )
                    self.assertAlmostEqual(actual, via_recurrence, places=6)
                    self.assertAlmostEqual(actual, via_roots, places=6)

    def test_eisenstein_sine_legendre_and_reciprocity(self):
        primes = [p for p in primes_to(47) if p > 2]
        for p in primes:
            H = range(1,(p+1)//2)
            for q in range(1,2*p+1):
                if q % p == 0:
                    continue
                product = math.prod(
                    math.sin(2*math.pi*q*j/p)/
                    math.sin(2*math.pi*j/p) for j in H
                )
                with self.subTest(p=p, q=q):
                    self.assertAlmostEqual(product, legendre(q,p),
                                           places=6)
        for p in primes:
            for q in primes:
                if p==q:
                    continue
                sign = (-1)**(((p-1)//2)*((q-1)//2))
                self.assertEqual(legendre(p,q)*legendre(q,p), sign)

    def test_euler_liars_form_proper_subgroup_for_composites(self):
        for n in range(9, 402, 2):
            if all(n%d for d in range(2, math.isqrt(n)+1)):
                continue
            units = [a for a in range(1,n) if math.gcd(a,n)==1]
            liars = [a for a in units
                     if pow(a,(n-1)//2,n) == jacobi(a,n)%n]
            with self.subTest(n=n):
                self.assertIn(1,liars)
                self.assertLessEqual(2*len(liars),len(units))
                self.assertEqual(len(units) % len(liars),0)
                L = set(liars)
                for a in liars:
                    self.assertIn(pow(a,-1,n),L)
                for a in liars:
                    for b in liars:
                        self.assertIn(a*b%n,L)

    def test_placement_and_no_forward_prerequisites(self):
        text = CH6.read_text(encoding="utf-8")
        for kind in ("exercise","hint","solution"):
            for key in ("pb:eisensine","pb:euler"):
                mark = (r"\label{" + key + "}" if kind == "exercise"
                        else r"\begin{" + kind + "}{" + key + "}")
                self.assertEqual(text.count(mark),1)
        self.assertLess(text.index(r"\label{pb:eisensine}"),
                        text.index(r"\label{pb:euler}"))
        self.assertIn("Gauss's lemma",
                      text.split(r"\begin{solution}{pb:eisensine}",1)[1]
                      .split(r"\end{solution}",1)[0])
        euler = text.split(r"\begin{solution}{pb:euler}",1)[1].split(
            r"\end{solution}",1)[0]
        self.assertIn("p(p-1)",euler)
        self.assertIn("the two sets are disjoint",euler)


if __name__ == "__main__":
    unittest.main()
