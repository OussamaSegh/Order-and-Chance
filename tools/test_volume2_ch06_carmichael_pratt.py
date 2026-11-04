"""Independent finite corroboration for the Carmichael and Pratt exercises."""

from functools import lru_cache
import math
import unittest


def factors(n):
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


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


@lru_cache(None)
def tree_size(p):
    return 1 if p == 2 else 1 + sum(tree_size(q) for q in factors(p - 1))


class CarmichaelPrattChecks(unittest.TestCase):
    def test_strong_liar_count_and_bound(self):
        for n in range(9, 1001, 2):
            if prime(n):
                continue
            d, s = n - 1, 0
            while d % 2 == 0:
                d //= 2
                s += 1
            fs = factors(n)
            odd_parts, valuations = [], []
            for p in fs:
                m, nu = p - 1, 0
                while m % 2 == 0:
                    m //= 2
                    nu += 1
                odd_parts.append(m)
                valuations.append(nu)
            r, nu = len(fs), min(valuations)
            predicted = math.prod(math.gcd(d, m) for m in odd_parts) * (
                1 + sum(2 ** (j * r) for j in range(nu)))
            units = [a for a in range(1, n) if math.gcd(a, n) == 1]
            actual = sum(pow(a, d, n) == 1 or any(pow(a, 2**j * d, n) == n - 1
                         for j in range(s)) for a in units)
            self.assertEqual(actual, predicted, n)
            if n != 9:
                self.assertLessEqual(4 * actual, len(units), n)
            else:
                self.assertEqual((actual, len(units)), (2, 6))

    def test_square_counts_and_recurrence(self):
        def squares(n):
            return len({a * a % n for a in range(n)})
        for p in (3, 5, 7):
            for k in range(1, 6):
                expected = 1 + sum((p - 1) * p ** (k - 2*j - 1) // 2
                                   for j in range((k + 1) // 2))
                self.assertEqual(squares(p**k), expected)
        for k in range(3, 13):
            self.assertEqual(squares(2**k), 2 ** (k - 3) + squares(2 ** (k - 2)))
        for m in range(1, 20):
            for n in range(1, 20):
                if math.gcd(m, n) == 1:
                    self.assertEqual(squares(m*n), squares(m) * squares(n))

    def test_carmichael_definition_against_criterion(self):
        for n in list(range(4, 701)) + [1105, 1729]:
            if prime(n):
                continue
            factorization = factors(n)
            criterion = all(e == 1 and (n - 1) % (p - 1) == 0
                            for p, e in factorization.items())
            definition = all(pow(a, n - 1, n) == 1 for a in range(1, n)
                             if math.gcd(a, n) == 1)
            self.assertEqual(definition, criterion, n)
            if definition:
                self.assertEqual(n % 2, 1)
                self.assertGreaterEqual(len(factorization), 3)

    def test_chernick_family(self):
        examples = []
        for k in range(1, 1001):
            ps = [6 * k + 1, 12 * k + 1, 18 * k + 1]
            if not all(prime(p) for p in ps):
                continue
            n = math.prod(ps)
            examples.append(n)
            for p in ps:
                self.assertEqual((n - 1) % (p - 1), 0)
        self.assertEqual(min(examples), 1729)

    def test_pratt_criterion_and_tree_bound(self):
        for n in range(3, 251):
            qs = factors(n - 1)
            witnesses = [a for a in range(1, n)
                         if pow(a, n - 1, n) == 1
                         and all(pow(a, (n - 1) // q, n) != 1 for q in qs)]
            self.assertEqual(bool(witnesses), prime(n), n)
        for p in range(3, 10001, 2):
            if prime(p):
                self.assertLessEqual(tree_size(p), 2 * math.log2(p) - 1)
        self.assertEqual(tree_size(3), 2)
        self.assertEqual(tree_size(7), 4)


if __name__ == "__main__":
    unittest.main()
