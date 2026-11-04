"""Finite exact checks for analytic identities, sieve endpoints and boundary sums."""

import cmath
import itertools
import math
from fractions import Fraction
import unittest

from tools.test_volume2_ch06_carmichael_pratt import factors
from tools.test_volume2_ch11_characters import character_phases


def mobius(n):
    fs = factors(n)
    return 0 if any(e > 1 for e in fs.values()) else (-1)**len(fs)


class SeriesSieveChecks(unittest.TestCase):
    def test_pseries_tails_and_finite_convolution(self):
        for K in range(1, 31):
            for s in (2, 3):
                partial_tail = sum(Fraction(1, n**s) for n in range(K+1, 301))
                self.assertLessEqual(partial_tail, Fraction(1, (s-1)*K**(s-1)))
        a, b = [0, 2, -3, 5, 0, 7], [0, -1, 4, 1, 8]
        left = sum(Fraction(a[n], n*n) for n in range(1, len(a))) * sum(
            Fraction(b[n], n*n) for n in range(1, len(b)))
        convolution = [0] * 21
        for n in range(1, len(a)):
            for m in range(1, len(b)):
                convolution[n*m] += a[n]*b[m]
        right = sum(Fraction(convolution[n], n*n) for n in range(1, 21))
        self.assertEqual(left, right)

    def test_finite_euler_products_and_mobius_inverse(self):
        primes = (2, 3, 5, 7)
        functions = (lambda n: 1, lambda n: (-1)**sum(factors(n).values()),
                     lambda n: 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1))
        for X in primes:
            included = [p for p in primes if p <= X]
            lower = math.prod(Fraction(p*p, p*p+1) for p in included)
            for f in functions:
                product = math.prod(1/(1-Fraction(f(p), p*p)) for p in included)
                partial = sum(Fraction(f(n), n*n) for n in range(1, 501)
                              if all(p <= X for p in factors(n)))
                self.assertLessEqual(abs(product-partial), Fraction(1, 500))
                self.assertGreaterEqual(abs(product), lower)
            inverse = math.prod(1-Fraction(1, p*p) for p in included)
            expansion = sum(Fraction((-1)**sum(bits), math.prod(p for p, bit in zip(included, bits)
                            if bit)**2) for bits in itertools.product((0, 1), repeat=len(included)))
            self.assertEqual(inverse, expansion)

    def test_sieve_real_endpoints(self):
        primes = (2, 3, 5, 7, 11)
        for quarters in range(201):
            x = Fraction(quarters, 4)
            for z in (Fraction(2), Fraction(5, 2), Fraction(3), Fraction(5), Fraction(11)):
                ps = [p for p in primes if p <= z]
                P = math.prod(ps)
                direct = sum(math.gcd(n, P) == 1 for n in range(1, math.floor(x)+1))
                terms = 0
                for bits in itertools.product((0, 1), repeat=len(ps)):
                    d = math.prod(p for p, bit in zip(ps, bits) if bit)
                    terms += (-1)**sum(bits) * math.floor(x/d)
                self.assertEqual(direct, terms)
                if x >= 1 and z*z >= x:
                    count = 1 + sum(n > z and all(n % d for d in range(2, math.isqrt(n)+1))
                                    for n in range(2, math.floor(x)+1))
                    self.assertEqual(direct, count)

    def test_boundary_groups_and_character_bounds(self):
        total = Fraction(0)
        for k in range(500):
            previous = total
            total += Fraction(2, (4*k+1)*(4*k+3))
            self.assertGreater(total, previous)
            self.assertLessEqual(total, Fraction(13, 15))
            if k:
                self.assertGreater(total, Fraction(2, 3))
        self.assertLess(abs(float(total)-math.pi/4), 1/2001)
        for m in range(1, 33):
            phases = character_phases(m)
            phi = len(phases)
            for row in phases[1:]:
                partial = 0
                for n in range(1, 5*m+1):
                    partial += cmath.exp(2j*math.pi*float(row[n % m])) if n % m in row else 0
                    self.assertLessEqual(abs(partial), phi/2+1e-8)

    def test_sieve30_and50_survivors(self):
        survivors = lambda x: [n for n in range(1, x+1) if math.gcd(n, 30) == 1]
        self.assertEqual(survivors(30), [1, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(len(survivors(50)), 14)
        self.assertEqual([n for n in survivors(50)[1:]
                          if any(n % d == 0 for d in range(2, math.isqrt(n)+1))], [49])

    def test_totient_ratio_and_real_mobius_floor(self):
        for n in range(1, 401):
            divisors = [d for d in range(1, n+1) if n % d == 0]
            ratio = Fraction(sum(math.gcd(a, n) == 1 for a in range(1, n+1)), n)
            self.assertEqual(ratio, sum(Fraction(mobius(d), d) for d in divisors))
            self.assertEqual(ratio, math.prod(1-Fraction(1, p) for p in factors(n)))
        for quarters in range(4, 801):
            x = Fraction(quarters, 4)
            self.assertEqual(sum(mobius(d)*math.floor(x/d)
                                 for d in range(1, math.floor(x)+1)), 1)

    def test_squarefree_detector_and_real_count(self):
        for n in range(1, 501):
            self.assertEqual(sum(mobius(d) for d in range(1, math.isqrt(n)+1)
                                 if n % (d*d) == 0), all(e == 1 for e in factors(n).values()))
        for quarters in range(801):
            x = Fraction(quarters, 4)
            direct = sum(all(e == 1 for e in factors(n).values())
                         for n in range(1, math.floor(x)+1))
            formula = sum(mobius(d)*math.floor(x/(d*d))
                          for d in range(1, math.isqrt(math.floor(x))+1))
            self.assertEqual(direct, formula)

    def test_exact_summation_by_parts_and_three_groups(self):
        chi = lambda n: 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
        for N in range(1, 101):
            A = [sum(chi(k) for k in range(1, n+1)) for n in range(N+1)]
            for b in (lambda n: Fraction(1, n), lambda n: Fraction((-1)**n*n, n+1)):
                direct = sum(chi(n)*b(n) for n in range(1, N+1))
                transformed = A[N]*b(N)-sum(A[n]*(b(n+1)-b(n)) for n in range(1, N))
                self.assertEqual(direct, transformed)
        self.assertEqual(sum(Fraction(2, (4*k+1)*(4*k+3)) for k in range(3)),
                         Fraction(2578, 3465))


if __name__ == "__main__":
    unittest.main()
