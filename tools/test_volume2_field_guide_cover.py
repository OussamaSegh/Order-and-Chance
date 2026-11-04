"""Independent reconstruction of field-guide arithmetic and complete cover data."""

import math
import unittest

from tools.series_cover import _front


def spiral_position(n):
    if n == 1:
        return 0, 0
    k = (math.isqrt(n-1)+1)//2
    side, distance = 2*k, (2*k+1)**2-n
    if distance < side:
        return k-distance, -k
    if distance < 2*side:
        return -k, -k+distance-side
    if distance < 3*side:
        return -k+distance-2*side, k
    return k, k-distance+3*side


class FieldGuideCoverChecks(unittest.TestCase):
    def test_full_prime_spiral_by_closed_coordinates_and_eratosthenes(self):
        limit = 71**2
        sieve = [True]*(limit+1)
        sieve[0] = sieve[1] = False
        for d in range(2, math.isqrt(limit)+1):
            if sieve[d]:
                for n in range(d*d, limit+1, d):
                    sieve[n] = False
        positions = [spiral_position(n) for n in range(1, limit+1)]
        self.assertEqual(len(set(positions)), limit)
        self.assertEqual(set(positions), {(a, b) for a in range(-35, 36) for b in range(-35, 36)})
        expected = {positions[n-1] for n in range(2, limit+1)
                    if sieve[n] and sum(v*v for v in positions[n-1]) < 35.5**2}
        scene, mode = _front().arts.v2()
        self.assertEqual(mode, 'bbox')
        self.assertTrue(all(item[0] == 'dot' for item in scene.items))
        coral = [tuple(item[1][0]) for item in scene.items if item[4] == 'ocCoral']
        origin = [tuple(item[1][0]) for item in scene.items if item[4] == 'ocCoverTitle']
        self.assertEqual(len(coral), len(set(coral)))
        self.assertEqual(set(coral), expected)
        self.assertEqual(origin, [(0, 0)])
        self.assertNotIn((0, 0), expected)
        for item in scene.items:
            if item[4] == 'ocCoral':
                self.assertEqual(item[2], .30)
                self.assertGreater(item[3], 0)
                self.assertLessEqual(item[3], .95)

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
