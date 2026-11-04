"""Exact quadratic-ring arithmetic supporting the Chapter 10 audit."""

import itertools
import unittest


class QuadraticRing:
    def __init__(self, u, v=0):
        self.u, self.v = u, v  # theta^2 = u + v theta

    def multiply(self, a, b):
        x, y = a
        z, w = b
        return x*z+self.u*y*w, x*w+y*z+self.v*y*w

    def conjugate(self, a):
        x, y = a
        return x+self.v*y, -y

    def norm(self, a):
        x, y = a
        return x*x+self.v*x*y-self.u*y*y

    def divide(self, a, b):
        numerator = self.multiply(a, self.conjugate(b))
        denominator = self.norm(b)
        q = tuple((2*n+denominator)//(2*denominator) for n in numerator)
        product = self.multiply(b, q)
        return q, tuple(x-y for x, y in zip(a, product))

    def extended_gcd(self, a, b):
        old_s, s, old_t, t = (1, 0), (0, 0), (0, 0), (1, 0)
        while b != (0, 0):
            q, r = self.divide(a, b)
            if self.norm(r) >= self.norm(b):
                raise AssertionError("non-decreasing remainder norm")
            a, b = b, r
            qs, qt = self.multiply(q, s), self.multiply(q, t)
            old_s, s = s, tuple(x-y for x, y in zip(old_s, qs))
            old_t, t = t, tuple(x-y for x, y in zip(old_t, qt))
        return a, old_s, old_t


class EuclideanRingChecks(unittest.TestCase):
    def test_norms_units_and_euclidean_division(self):
        for ring, unit_count in ((QuadraticRing(-1), 4), (QuadraticRing(-1, -1), 6),
                                 (QuadraticRing(-2), 2)):
            points = list(itertools.product(range(-3, 4), repeat=2))
            units = [a for a in points if ring.norm(a) == 1]
            self.assertEqual(len(units), unit_count)
            for a in units:
                self.assertEqual(ring.multiply(a, ring.conjugate(a)), (1, 0))
            for a in points:
                for b in points:
                    self.assertEqual(ring.norm(ring.multiply(a, b)), ring.norm(a)*ring.norm(b))
                    if b != (0, 0):
                        q, r = ring.divide(a, b)
                        product = ring.multiply(b, q)
                        self.assertEqual(tuple(x+y for x, y in zip(product, r)), a)
                        self.assertLess(ring.norm(r), ring.norm(b))

    def test_extended_gcd_and_gaussian_examples(self):
        for ring in (QuadraticRing(-1), QuadraticRing(-1, -1), QuadraticRing(-2)):
            points = list(itertools.product(range(-2, 3), repeat=2))
            for a in points:
                for b in points:
                    if a == b == (0, 0):
                        continue
                    g, s, t = ring.extended_gcd(a, b)
                    sa, tb = ring.multiply(s, a), ring.multiply(t, b)
                    self.assertEqual(tuple(x+y for x, y in zip(sa, tb)), g)
                    self.assertEqual(ring.divide(a, g)[1], (0, 0))
                    self.assertEqual(ring.divide(b, g)[1], (0, 0))
        ring = QuadraticRing(-1)
        product = (1, 0)
        for factor in ((2, 1), (2, -1), (3, 2), (3, -2)):
            product = ring.multiply(product, factor)
        self.assertEqual(product, (65, 0))
        product = (0, -1)
        for factor in ((1, 1), (1, 1), (22, 23), (22, -23)):
            product = ring.multiply(product, factor)
        self.assertEqual(product, (2026, 0))
        self.assertEqual(ring.extended_gcd((11, 3), (1, 8))[0], (-1, 2))

    def test_minus_five_norm_obstruction(self):
        ring = QuadraticRing(-5)
        norms = {ring.norm(a) for a in itertools.product(range(-4, 5), repeat=2)}
        self.assertNotIn(2, norms)
        self.assertNotIn(3, norms)
        self.assertEqual(ring.multiply((1, 1), (1, -1)), (6, 0))
        self.assertEqual({a for a in itertools.product(range(-2, 3), repeat=2)
                          if ring.norm(a) == 1}, {(-1, 0), (1, 0)})


if __name__ == "__main__":
    unittest.main()
