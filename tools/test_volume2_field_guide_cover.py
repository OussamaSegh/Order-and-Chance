"""Independent reconstruction of field-guide arithmetic and the Volume 2 cover."""

import math
import unittest

from tools.series_cover import _front


def _primes_to(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for d in range(2, math.isqrt(limit) + 1):
        if sieve[d]:
            for n in range(d * d, limit + 1, d):
                sieve[n] = False
    return [n for n in range(limit + 1) if sieve[n]]


def _representations(n):
    radius = int(math.sqrt(n))
    return [(x, y) for x in range(-radius, radius + 1)
            for y in range(-radius, radius + 1) if x * x + y * y == n]


class FieldGuideCoverChecks(unittest.TestCase):
    def test_prime_circles_are_the_sums_of_two_squares(self):
        # The disc count proved in Sums of Squares, independent of the plate.
        self.assertEqual(sum(1 for x in range(-6, 7) for y in range(-6, 7)
                             if x * x + y * y <= 36), 113)
        primes = _primes_to(53)
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53])
        expected = {}
        for prime in primes:
            points = _representations(prime)
            if prime % 4 == 3:
                self.assertEqual(points, [])
            elif prime == 2:
                self.assertEqual(set(points), {(x, y) for x in (-1, 1) for y in (-1, 1)})
            else:
                self.assertEqual(len(points), 8)
                self.assertTrue(all(math.gcd(x, y) == 1 for x, y in points))
            expected[prime] = set(points)
        scene, mode = _front().arts.v2()
        self.assertEqual(mode, 'bbox')
        self.assertEqual(scene.fill_frac, 0.90)
        circles = [item for item in scene.items if item[0] == 'circle']
        dots = [item for item in scene.items if item[0] == 'dot']
        drawn = {round(item[2] ** 2) for item in circles if item[4] > 0}
        self.assertEqual(drawn, set(primes))
        for item in circles:
            prime = round(item[2] ** 2)
            if item[4] == 0:
                self.assertAlmostEqual(item[2], math.sqrt(53) + 0.15)
                continue
            if prime % 4 == 3:
                self.assertEqual((item[3], item[4], item[6]), (0.32, 0.20, 0.0))
            else:
                self.assertEqual((item[3], item[4], item[6]), (0.58, 0.78, 0.45))
        coral = [tuple(int(v) for v in item[1][0]) for item in dots if item[4] == 'ocCoral']
        origin = [tuple(int(v) for v in item[1][0]) for item in dots if item[4] == 'ocCoverTitle']
        self.assertEqual(origin, [(0, 0)])
        self.assertEqual(set(coral), set().union(*expected.values()))
        self.assertEqual(len(coral), 4 + 8 * sum(1 for p in primes if p % 4 == 1))
        for point in coral:
            self.assertIn(point[0] * point[0] + point[1] * point[1],
                          {p for p in primes if p % 4 != 3})

    def test_field_guide_bezout_inverse_and_complete_nonunit_obstruction(self):
        self.assertEqual(3*12-35, 1)
        self.assertEqual(35*11, 32*12+1)
        self.assertEqual(math.gcd(18, 12), 6)
        for x in range(-100, 101):
            self.assertEqual((35*x-1) % 12 == 0, (x-11) % 12 == 0)
            self.assertNotEqual((18*x) % 6, 1)
            self.assertNotEqual((18*x-1) % 12, 0)

    def test_field_guide_prime_factor_and_symmetry_examples(self):
        self.assertEqual([pow(3, k, 7) for k in range(1, 7)], [3, 2, 6, 4, 5, 1])
        self.assertEqual({(n*n) % 4 for n in range(4)}, {0, 1})
        for n in range(-100, 101):
            value = n*n+1
            for p in range(3, value+1, 2):
                if value % p == 0 and all(p % d for d in range(2, math.isqrt(p)+1)):
                    self.assertEqual(p % 4, 1)
                    # Separate order certificate: n²=-1, n⁴=1, so order4.
                    self.assertEqual(pow(n, 2, p), p-1)
                    self.assertEqual(pow(n, 4, p), 1)
        self.assertEqual((2+1j)*(2-1j), 5)


if __name__ == '__main__':
    unittest.main()
