"""Finite corroboration for printed Chapter 8's opening proofs and exercises."""

import math
import unittest


class PythagoreanChecks(unittest.TestCase):
    def test_primitive_parametrization_is_complete(self):
        limit = 500
        direct = set()
        for z in range(1, limit + 1):
            for x in range(1, z, 2):
                y2 = z*z - x*x
                y = math.isqrt(y2)
                if y*y == y2 and y % 2 == 0 and math.gcd(x, y) == 1:
                    direct.add((x, y, z))
        generated = set()
        for m in range(2, math.isqrt(limit) + 1):
            for n in range(1, m):
                if math.gcd(m, n) == 1 and (m-n) % 2 and m*m+n*n <= limit:
                    generated.add((m*m-n*n, 2*m*n, m*m+n*n))
        self.assertEqual(direct, generated)

    def test_square_hypotenuse_fourth_power_search(self):
        for x in range(1, 101):
            for y in range(1, 101):
                value = x**4 + y**4
                self.assertNotEqual(math.isqrt(value)**2, value)

    def test_opening_exercises(self):
        triangles = set()
        for a in range(1, 101):
            for b in range(a, 101):
                c = math.isqrt(a*a+b*b)
                if c*c == a*a+b*b and a*b == 2*(a+b+c):
                    triangles.add((a, b, c))
        self.assertEqual(triangles, {(5, 12, 13), (6, 8, 10)})
        self.assertEqual([(x, y) for x in range(3) for y in range(3)
                          if (x*x+y*y) % 3 == 0], [(0, 0)])
        self.assertEqual([(x, y) for x in range(31) for y in range(31)
                          if 2**x-3**y == 1], [(1, 0), (2, 1)])


if __name__ == "__main__":
    unittest.main()
