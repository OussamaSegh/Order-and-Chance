"""Finite support for the first Chapter 6 criteria; symbolic proofs are in the ledger."""

import cmath
import math
import unittest


def odd_primes(limit):
    return [p for p in range(3, limit + 1, 2)
            if all(p % d for d in range(2, math.isqrt(p) + 1))]


def jacobi_by_factors(a, n):
    result = 1
    d = 3
    while d * d <= n:
        while n % d == 0:
            if a % d == 0:
                return 0
            squares = {x * x % d for x in range(1, d)}
            result *= 1 if a % d in squares else -1
            n //= d
        d += 2
    if n > 1:
        if a % n == 0:
            return 0
        squares = {x * x % n for x in range(1, n)}
        result *= 1 if a % n in squares else -1
    return result


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

    def test_jacobi_and_first_exercises(self):
        for n in range(1, 102, 2):
            self.assertEqual(jacobi_by_factors(-1, n), (-1) ** ((n - 1) // 2))
            self.assertEqual(jacobi_by_factors(2, n), (-1) ** ((n * n - 1) // 8))
            for m in range(1, 102, 2):
                if math.gcd(m, n) == 1:
                    expected = (-1) ** (((m - 1) // 2) * ((n - 1) // 2))
                    self.assertEqual(jacobi_by_factors(m, n) * jacobi_by_factors(n, m),
                                     expected)
        for p in odd_primes(257):
            squares = {x * x % p for x in range(1, p)}
            if p > 3:
                self.assertEqual((-3) % p in squares, p % 3 == 1)
            self.assertEqual((-2) % p in squares, p % 8 in (1, 3))
        for n in range(1, 101):
            value = n * n + 1
            for p in odd_primes(math.isqrt(value)):
                if value % p == 0:
                    self.assertEqual(p % 4, 1)

    def test_next_three_exercises(self):
        safe_primes = set(odd_primes(1009))
        for p in odd_primes(503):
            if p % 4 == 3 and 2 * p + 1 in safe_primes:
                self.assertEqual(pow(2, p, 2 * p + 1), 1)
        for p in odd_primes(257):
            squares = {x * x % p for x in range(1, p)}
            def chi(a):
                return 0 if a % p == 0 else (1 if a % p in squares else -1)
            self.assertEqual(sum(chi(a * (a + 1)) for a in range(1, p)), -1)
            count = sum(a in squares and a + 1 in squares for a in range(1, p - 1))
            self.assertEqual(count, (p - 4 - chi(-1)) // 4)
        for n in range(1, 6):
            fermat = 2 ** (2**n) + 1
            is_prime = all(fermat % d for d in range(2, math.isqrt(fermat) + 1))
            self.assertEqual(pow(3, (fermat - 1) // 2, fermat) == fermat - 1,
                             is_prime)

    def test_residue_chance_and_small_symbols(self):
        for p in odd_primes(257):
            squares = {x * x % p for x in range(1, p)}
            values = [0 if a == 0 else (1 if a in squares else -1)
                      for a in range(p)]
            shifted = values[1:] + values[:1]
            self.assertEqual(values.count(0), 1)
            self.assertEqual(values.count(1), (p - 1) // 2)
            self.assertEqual(values.count(-1), (p - 1) // 2)
            self.assertEqual(sum(values), 0)
            self.assertEqual(sum(shifted), 0)
            self.assertEqual(sum(x * y for x, y in zip(values, shifted)), -1)
        self.assertEqual({x * x % 11 for x in range(11)}, {0, 1, 3, 4, 5, 9})
        self.assertNotIn(6, {x * x % 13 for x in range(13)})
        self.assertNotIn(6, {x * x % 17 for x in range(17)})

    def test_primitive_root_sums(self):
        for p in odd_primes(101):
            m = p - 1
            generators = []
            for a in range(1, p):
                value, order = a, 1
                while value != 1:
                    value = value * a % p
                    order += 1
                if order == m:
                    generators.append(a)
            for k in range(0, 2 * m + 1):
                field_sum = sum(pow(a, k, p) for a in generators) % p
                ramanujan = sum(cmath.exp(2j * math.pi * a * k / m)
                                for a in range(1, m + 1) if math.gcd(a, m) == 1)
                self.assertAlmostEqual(ramanujan.imag, 0, places=7)
                self.assertEqual(field_sum, round(ramanujan.real) % p)
            if p > 3:
                self.assertEqual(math.prod(generators) % p, 1)


if __name__ == "__main__":
    unittest.main()
