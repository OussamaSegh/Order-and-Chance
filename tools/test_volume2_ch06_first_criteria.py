"""Finite support for the first Chapter 6 criteria; symbolic proofs are in the ledger."""

import math
import unittest


def odd_primes(limit):
    return [p for p in range(3, limit + 1, 2)
            if all(p % d for d in range(2, math.isqrt(p) + 1))]


class QuadraticCriteriaChecks(unittest.TestCase):
    def test_euler_and_gauss_against_direct_squares(self):
        for p in odd_primes(257):
            half = (p - 1) // 2
            squares = {x * x % p for x in range(1, p)}
            self.assertEqual(len(squares), half)
            for a in range(-p, 2 * p):
                symbol = 0 if a % p == 0 else (1 if a % p in squares else -1)
                self.assertEqual(pow(a, half, p), symbol % p)
                if symbol:
                    signed = [a * k % p for k in range(1, half + 1)]
                    negatives = sum(r > half for r in signed)
                    self.assertEqual((-1) ** negatives, symbol)

    def test_supplementary_laws(self):
        for p in odd_primes(1009):
            squares = {x * x % p for x in range(1, p)}
            self.assertEqual((-1) % p in squares, p % 4 == 1)
            self.assertEqual(2 in squares, p % 8 in (1, 7))
            self.assertEqual((1 if 2 in squares else -1), (-1) ** ((p * p - 1) // 8))


if __name__ == "__main__":
    unittest.main()
