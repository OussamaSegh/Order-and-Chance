"""Finite support for the first Chapter 6 criteria; symbolic proofs are in the ledger."""

import cmath
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

    def test_eisenstein_and_reciprocity(self):
        for p in odd_primes(101):
            squares = {x * x % p for x in range(1, p)}
            for a in range(-2 * p + 1, 2 * p + 1, 2):
                if a % p == 0:
                    continue
                symbol = 1 if a % p in squares else -1
                total = sum((k * a) // p for k in range(1, (p + 1) // 2))
                self.assertEqual((-1) ** total, symbol)
            for q in odd_primes(101):
                if q == p:
                    continue
                sq_q = {x * x % q for x in range(1, q)}
                left = (1 if p % q in sq_q else -1) * (1 if q % p in squares else -1)
                self.assertEqual(left, (-1) ** (((p - 1) // 2) * ((q - 1) // 2)))
                t_qp = sum((k * q) // p for k in range(1, (p + 1) // 2))
                t_pq = sum((k * p) // q for k in range(1, (q + 1) // 2))
                self.assertEqual(t_qp + t_pq, ((p - 1) // 2) * ((q - 1) // 2))

    def test_quadratic_gauss_sum(self):
        for p in odd_primes(31):
            zeta = cmath.exp(2j * math.pi / p)
            squares = {x * x % p for x in range(1, p)}
            g = sum((1 if a in squares else -1) * zeta**a for a in range(1, p))
            G = sum(zeta ** ((x * x) % p) for x in range(p))
            p_star = p if p % 4 == 1 else -p
            self.assertAlmostEqual((g * g).real, p_star, places=8)
            self.assertAlmostEqual((g * g).imag, 0, places=8)
            self.assertAlmostEqual(abs(g - G), 0, places=8)


if __name__ == "__main__":
    unittest.main()
