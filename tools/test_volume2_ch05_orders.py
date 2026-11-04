"""Finite checks supporting the Chapter 5 order audit, not general proofs."""

import math
import unittest


def order(a, n):
    if math.gcd(a, n) != 1:
        raise ValueError("a must be a unit")
    x = a % n
    k = 1
    while x != 1 % n:
        x = x * a % n
        k += 1
    return k


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def monic_quotient(numerator, divisor):
    """Exact ascending-coefficient polynomial division by a monic factor."""
    remainder = numerator[:]
    quotient = [0] * (len(numerator) - len(divisor) + 1)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = remainder[shift + len(divisor) - 1]
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            remainder[shift + i] -= coefficient * value
    if any(remainder):
        raise AssertionError("non-exact cyclotomic division")
    return quotient


def cyclotomic_polynomials(limit):
    phi = {}
    for n in range(1, limit + 1):
        polynomial = [-1] + [0] * (n - 1) + [1]
        for d in range(1, n):
            if n % d == 0:
                polynomial = monic_quotient(polynomial, phi[d])
        phi[n] = polynomial
    return phi


class Chapter5OrderChecks(unittest.TestCase):
    def test_order_of_powers_and_returns(self):
        for n in range(1, 81):
            for a in range(n):
                if math.gcd(a, n) != 1:
                    continue
                k = order(a, n)
                self.assertTrue(all((pow(a, m, n) == 1 % n) == (m % k == 0)
                                    for m in range(0, 2 * k + 2)))
                for j in range(-2 * k, 2 * k + 1):
                    self.assertEqual(order(pow(a, j, n), n), k // math.gcd(k, j))

    def test_cyclic_modulus_classification(self):
        for n in range(1, 121):
            phi = sum(math.gcd(a, n) == 1 for a in range(n))
            cyclic = any(order(a, n) == phi for a in range(n)
                         if math.gcd(a, n) == 1)
            classified = n in (1, 2, 4) or any(
                n in (p**k, 2 * p**k)
                for p in range(3, n + 1, 2) if is_prime(p)
                for k in range(1, 8)
            )
            self.assertEqual(cyclic, classified, n)

    def test_exercises(self):
        roots = {p: [a for a in range(1, p) if order(a, p) == p - 1]
                 for p in (7, 11, 13)}
        self.assertEqual(roots[13], [2, 6, 7, 11])
        self.assertIn(3, roots[7])
        self.assertIn(2, roots[11])
        self.assertEqual((order(10, 7), order(10, 17)), (6, 16))
        for n in range(0, 6):
            fermat = 2 ** (2**n) + 1
            for p in range(3, math.isqrt(fermat) + 1, 2):
                if fermat % p == 0 and is_prime(p):
                    self.assertEqual(order(2, p), 2 ** (n + 1))
        for p in (2, 3, 5, 7, 11, 13, 17, 19):
            for k in range(0, 2 * p + 1):
                expected = -1 if k % (p - 1) == 0 else 0
                self.assertEqual(sum(pow(x, k, p) for x in range(1, p)) % p,
                                 expected % p)

    def test_two_power_structure_and_squares(self):
        for k in range(3, 11):
            n = 2**k
            forms = [(-1)**a * pow(5, b, n) % n
                     for a in (0, 1) for b in range(2 ** (k - 2))]
            self.assertEqual(len(set(forms)), 2 ** (k - 1))
            self.assertEqual(set(forms), set(range(1, n, 2)))
            squares = {x * x % n for x in range(1, n, 2)}
            self.assertEqual(squares, set(range(1, n, 8)))

    def test_kth_roots_and_unit_product(self):
        for p in (2, 3, 5, 7, 11, 13, 17, 19):
            for k in range(1, 2 * p):
                d = math.gcd(k, p - 1)
                for a in range(1, p):
                    count = sum(pow(x, k, p) == a for x in range(1, p))
                    self.assertEqual(count, d if pow(a, (p - 1) // d, p) == 1 else 0)
        for n in range(3, 121):
            units = [x for x in range(n) if math.gcd(x, n) == 1]
            product = math.prod(units) % n
            cyclic = any(order(a, n) == len(units) for a in units)
            self.assertEqual(product, (-1 if cyclic else 1) % n)

    def test_cyclotomic_order_implication(self):
        for n, coefficients in cyclotomic_polynomials(24).items():
            self.assertEqual(coefficients[-1], 1)
            if n > 1:
                self.assertEqual(coefficients[0], 1)
            for p in range(2, 98):
                if not is_prime(p) or n % p == 0:
                    continue
                for a in range(p):
                    value = sum(c * pow(a, j, p) for j, c in enumerate(coefficients)) % p
                    if value == 0:
                        self.assertEqual(order(a, p), n)


if __name__ == "__main__":
    unittest.main()
