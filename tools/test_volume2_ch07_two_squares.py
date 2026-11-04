"""Finite checks supporting the opening two-square proofs and exercises."""

import math
from collections import defaultdict
import unittest


def factorization(n):
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


class TwoSquareChecks(unittest.TestCase):
    def test_euler_identity_formal_coefficients(self):
        # Eight formal variables: a_1,...,a_4,b_1,...,b_4.
        forms = [
            [(1, 0, 4), (1, 1, 5), (1, 2, 6), (1, 3, 7)],
            [(1, 0, 5), (-1, 1, 4), (1, 2, 7), (-1, 3, 6)],
            [(1, 0, 6), (-1, 2, 4), (1, 3, 5), (-1, 1, 7)],
            [(1, 0, 7), (-1, 3, 4), (1, 1, 6), (-1, 2, 5)],
        ]
        actual = defaultdict(int)
        for form in forms:
            for c, i, j in form:
                for d, k, l in form:
                    actual[tuple(sorted((i, j, k, l)))] += c*d
        actual = {m: c for m, c in actual.items() if c}
        expected = {tuple(sorted((i, i, j, j))): 1
                    for i in range(4) for j in range(4, 8)}
        self.assertEqual(actual, expected)

    def test_zagier_involution(self):
        for p in range(5, 1000, 4):
            if factorization(p) != {p: 1}:
                continue
            S = set()
            for x in range(1, math.isqrt(p) + 1):
                if (p - x*x) % 4:
                    continue
                product = (p - x*x) // 4
                for y in range(1, product + 1):
                    if product % y == 0:
                        S.add((x, y, product // y))
            def f(point):
                x, y, z = point
                if x < y - z:
                    return x + 2*z, z, y - x - z
                if x < 2*y:
                    return 2*y - x, y, x - y + z
                return x - 2*y, x - y + z, y
            self.assertEqual({s for s in S if f(s) == s}, {(1, 1, (p - 1) // 4)})
            for s in S:
                self.assertIn(f(s), S)
                self.assertEqual(f(f(s)), s)
            self.assertTrue(any(y == z for x, y, z in S))

    def test_circle_bound(self):
        for quarters in range(4, 401):
            R = quarters / 4
            bound = math.floor(R)
            count = sum(x*x+y*y <= R*R for x in range(-bound, bound+1)
                        for y in range(-bound, bound+1))
            self.assertLessEqual(abs(count - math.pi*R*R),
                                 math.sqrt(2)*math.pi*R + math.pi/2)
        self.assertEqual(sum(x*x+y*y <= 100 for x in range(-10, 11)
                             for y in range(-10, 11)), 317)

    def test_thue_small_primes(self):
        for p in range(2, 200):
            if len(factorization(p)) != 1 or factorization(p).get(p) != 1:
                continue
            m = math.isqrt(p)
            small = set(range(1, m + 1)) | set(range(-m, 0))
            for a in range(1, p):
                self.assertTrue(any((a * x) % p in {y % p for y in small}
                                    for x in small), (p, a))

    def test_two_square_criterion(self):
        limit = 5000
        sums = {a*a + b*b for a in range(math.isqrt(limit) + 1)
                for b in range(math.isqrt(limit) + 1) if a*a + b*b <= limit}
        for n in range(1, limit + 1):
            condition = all(p % 4 != 3 or e % 2 == 0 for p, e in factorization(n).items())
            self.assertEqual(n in sums, condition, n)
        self.assertEqual({n for n in range(2021, 2031) if n in sums}, {2025, 2026, 2029})
        self.assertEqual(22**2 + 23**2, 1013)

    def test_three_square_obstruction(self):
        self.assertNotIn(7, {(a+b+c) % 8 for a in (0, 1, 4)
                            for b in (0, 1, 4) for c in (0, 1, 4)})
        self.assertEqual([(a, b, c) for a in (0, 1) for b in (0, 1)
                          for c in (0, 1) if (a+b+c) % 4 == 0], [(0, 0, 0)])

    def test_primitive_and_weighted_representations(self):
        for x in range(0, 51):
            for y in range(0, 51):
                if math.gcd(x, y) != 1:
                    continue
                n = x*x + y*y
                self.assertNotEqual(n % 4, 0)
                self.assertFalse(any(p % 4 == 3 for p in factorization(n)))
        for p in range(3, 1000, 2):
            fs = factorization(p)
            if fs != {p: 1}:
                continue
            for coefficient, required in ((2, p % 8 in (1, 3)), (3, p % 3 == 1)):
                if required:
                    self.assertTrue(any(p - coefficient*y*y >= 0 and
                        math.isqrt(p - coefficient*y*y)**2 == p - coefficient*y*y
                        for y in range(math.isqrt(p // coefficient) + 1)),
                        (p, coefficient))


if __name__ == "__main__":
    unittest.main()
