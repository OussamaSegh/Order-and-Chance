"""Finite corroboration for printed Chapter 8's opening proofs and exercises."""

import math
from fractions import Fraction
import unittest


class PythagoreanChecks(unittest.TestCase):
    def test_conic_parametrization_and_vertical_exception(self):
        for denominator in range(1, 13):
            for a in range(-2*denominator, 2*denominator + 1):
                for b in range(-2*denominator, 2*denominator + 1):
                    x, y = Fraction(a, denominator), Fraction(b, denominator)
                    if x*x + x*y + y*y != 1:
                        continue
                    if x == -1:
                        self.assertIn(y, (0, 1))
                        continue
                    t = y / (x + 1)
                    D = 1 + t + t*t
                    self.assertEqual((x, y), ((1-t*t)/D, (2*t+t*t)/D))

    def test_markov_generation_and_descent(self):
        direct = set()
        for x in range(1, 201):
            for y in range(x, 201):
                discriminant = 9*x*x*y*y - 4*(x*x+y*y)
                if discriminant < 0:
                    continue
                root = math.isqrt(discriminant)
                if root*root != discriminant:
                    continue
                for numerator in (3*x*y-root, 3*x*y+root):
                    if numerator % 2 == 0 and y <= numerator // 2 <= 200:
                        direct.add((x, y, numerator // 2))
        reached, pending = {(1, 1, 1)}, [(1, 1, 1)]
        while pending:
            triple = pending.pop()
            for i in range(3):
                others = [triple[j] for j in range(3) if j != i]
                child = tuple(sorted(others + [3*math.prod(others) - triple[i]]))
                if child[-1] <= 200 and child not in reached:
                    reached.add(child)
                    pending.append(child)
        self.assertEqual(direct, reached)
        self.assertEqual(len(direct), 9)
        for x, y, z in direct - {(1, 1, 1)}:
            self.assertTrue(0 < 3*x*y-z < z)
            self.assertEqual((math.gcd(x, y), math.gcd(x, z), math.gcd(y, z)), (1, 1, 1))

    def test_mordell_obstructions_and_vieta_challenge(self):
        for x in range(-1000, 1001):
            for offset in (7, -5):
                value = x**3 + offset
                if value >= 0:
                    self.assertNotEqual(math.isqrt(value)**2, value)
        for a in range(1, 201):
            for b in range(1, 201):
                numerator, denominator = a*a+b*b, a*b+1
                if numerator % denominator == 0:
                    k = numerator // denominator
                    self.assertEqual(math.isqrt(k)**2, k)

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
