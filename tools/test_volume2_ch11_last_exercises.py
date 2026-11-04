"""Independent finite counts for the final five keyed exercises."""

from fractions import Fraction
from functools import lru_cache
import math
import unittest

from tools.test_volume2_ch06_carmichael_pratt import factors, prime


@lru_cache(None)
def winning(a, b):
    a, b = sorted((a, b))
    if b % a == 0:
        return True
    return any(not winning(*sorted((a, b-k*a))) for k in range(1, b//a+1))


def powerful(n):
    return all(e >= 2 for e in factors(n).values())


class LastExerciseChecks(unittest.TestCase):
    def test_euclid_mullin_sequences(self):
        for choose, expected in ((min, [2, 3, 7, 43, 13, 53, 5]),
                                 (max, [2, 3, 7, 43, 139, 50207])):
            terms, product = [2], 2
            while len(terms) < len(expected):
                term = choose(factors(product+1))
                self.assertNotIn(term, terms)
                terms.append(term)
                product *= term
            self.assertEqual(terms, expected)
        self.assertEqual(factors(1807), {13: 1, 139: 1})
        self.assertEqual(factors(23479), {53: 1, 443: 1})
        self.assertEqual(1244335, 5*248867)

    def test_safe_prime_primitive_roots_by_full_orbit(self):
        for q in range(3, 1000, 2):
            p = 2*q+1
            if p <= 7 or not prime(q) or not prime(p):
                continue
            a = 2 if q % 4 == 1 else -2
            self.assertEqual({pow(a, k, p) for k in range(p-1)}, set(range(1, p)))

    def test_euclid_game_by_all_legal_moves(self):
        for b in range(2, 181):
            for a in range(1, b):
                # Both sides of 2b-a > sqrt(5)*a are positive; compare exactly.
                self.assertEqual(winning(a, b), (2*b-a)**2 > 5*a*a)
        for N in (10, 30, 100, 180):
            count = sum(winning(a, b) for b in range(2, N+1) for a in range(1, b))
            self.assertLess(abs(count/(N*(N-1)/2)-(math.sqrt(5)-1)/2), 2/N)

    def test_pascal_digit_counts_and_all_residue_totals(self):
        for p in (2, 3, 5):
            for n in range(151):
                digits, m = [], n
                while m:
                    digits.append(m % p)
                    m //= p
                residues = [math.comb(n, k) % p for k in range(n+1)]
                self.assertEqual(sum(r != 0 for r in residues), math.prod(d+1 for d in digits))
                if p == 3:
                    self.assertEqual(residues.count(1)-residues.count(2), 2**digits.count(1))
        for k in range(6):
            counts = [0, 0, 0]
            for n in range(3**k):
                for j in range(n+1):
                    counts[math.comb(n, j) % 3] += 1
            total = 3**k*(3**k+1)//2
            self.assertEqual(counts, [total-6**k, (6**k+4**k)//2, (6**k-4**k)//2])

    def test_powerful_decomposition_count_and_pell_pairs(self):
        limit = 10000
        representations = {}
        for b in range(1, 22):
            if not all(e == 1 for e in factors(b).values()):
                continue
            for a in range(1, math.isqrt(limit//(b**3))+1):
                n = a*a*b**3
                self.assertNotIn(n, representations)
                representations[n] = (a, b)
        direct = {n for n in range(1, limit+1) if powerful(n)}
        self.assertEqual(set(representations), direct)
        constant_lower = sum(b**(-1.5) for b in range(1, 4001)
                             if all(e == 1 for e in factors(b).values()))
        for x in (1, 8, 9, 100, 1000, limit):
            B = next(b for b in range(1, 23) if (b+1)**3 > x)
            count = sum(n <= x for n in direct)
            bound = B+2*math.sqrt(x/B)
            self.assertLessEqual(abs(count-math.sqrt(x)*constant_lower),
                                 bound+2*math.sqrt(x/4000))
        # Local Euler-factor identity: (1-z^6)/((1-z^2)(1-z^3)).
        for e in range(31):
            coefficient = sum(2*a+3*b == e for a in range(16) for b in range(11))
            coefficient -= sum(2*a+3*b+6 == e for a in range(16) for b in range(11))
            self.assertEqual(coefficient, e == 0 or e >= 2)
        X, Y = 3, 1
        pairs = []
        for _ in range(4):
            self.assertEqual(X*X-8*Y*Y, 1)
            self.assertTrue(powerful(8*Y*Y))
            self.assertTrue(powerful(X*X))
            pairs.append((8*Y*Y, X*X))
            X, Y = 3*X+8*Y, X+3*Y
        self.assertEqual(pairs[:2], [(8, 9), (288, 289)])


if __name__ == '__main__':
    unittest.main()
