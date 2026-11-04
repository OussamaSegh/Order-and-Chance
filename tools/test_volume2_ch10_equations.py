"""Exact arithmetic corroboration for the quadratic-ring equation exercises."""

import itertools
import math
import unittest

from tools.test_volume2_ch10_euclidean import QuadraticRing


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))


class QuadraticEquationChecks(unittest.TestCase):
    def test_gaussian_gcd_and_euler_factor(self):
        ring = QuadraticRing(-1)
        for p in range(5, 200, 4):
            if prime(p):
                for a in range(p):
                    if (a*a+1) % p == 0:
                        self.assertEqual(ring.norm(ring.extended_gcd((p, 0), (a, 1))[0]), p)
        self.assertEqual(ring.multiply((23, -22), (1, 1)), (45, 1))
        self.assertEqual(ring.multiply((23, -22), (23, 22)), (1013, 0))
        dividends = [(1000, 3), (972, 235), (28, -232), (44, 123)]
        divisors = [(972, 235), (28, -232), (44, 123), (-7, 58)]
        quotients = [(1, 0), (0, 4), (-2, -1), (2, -1)]
        remainders = [(28, -232), (44, 123), (-7, 58), (0, 0)]
        for a, b, q, r in zip(dividends, divisors, quotients, remainders):
            bq = ring.multiply(b, q)
            self.assertEqual(tuple(x+y for x, y in zip(bq, r)), a)
            self.assertLess(ring.norm(r), ring.norm(b))
        self.assertEqual(ring.norm((-7, 58)), 3413)
        self.assertEqual(math.gcd(1000009, 232084), 3413)
        self.assertEqual(293*3413, 1000009)

    def test_cubic_coefficient_cases_and_coprimality(self):
        for D, expected in ((1, {(0, -1)}), (2, {(-1, 1), (1, 1)})):
            ring = QuadraticRing(-D)
            found = set()
            for a, b in itertools.product(range(-5, 6), repeat=2):
                cube = ring.multiply(ring.multiply((a, b), (a, b)), (a, b))
                self.assertEqual(cube, (a**3-3*D*a*b*b, 3*a*a*b-D*b**3))
                if cube[1] == 1:
                    found.add((a, b))
            self.assertEqual(found, expected)
            for y in range(-100, 101):
                if y % 2 == (0 if D == 1 else 1):
                    self.assertEqual(ring.norm(ring.extended_gcd((y, 1), (y, -1))[0]), 1)
        self.assertEqual(3**3-2, 5**2)

    def test_eisenstein_norm_criterion_and_thirteen(self):
        for p in range(2, 300):
            if not prime(p):
                continue
            bound = math.isqrt(2*p)+1
            represented = any(x*x+x*y+y*y == p for x in range(-bound, bound+1)
                              for y in range(-bound, bound+1))
            self.assertEqual(represented, p == 3 or p % 3 == 1)
        self.assertEqual(QuadraticRing(-1).multiply((2, 3), (2, -3)), (13, 0))
        self.assertEqual(QuadraticRing(-1, -1).multiply((3, -1), (4, 1)), (13, 0))


if __name__ == "__main__":
    unittest.main()
