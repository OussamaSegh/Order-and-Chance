"""Finite checks supporting the opening two-square proofs and exercises."""

import math
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


if __name__ == "__main__":
    unittest.main()
