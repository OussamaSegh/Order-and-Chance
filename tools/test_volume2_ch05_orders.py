"""Finite checks supporting the Chapter 5 order audit, not general proofs."""

import cmath
import math
from fractions import Fraction
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


def mobius(n):
    value = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    return -value if n > 1 else value


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


def determinant(matrix):
    """Fraction-free elimination for small exact integer matrices."""
    entries = [row[:] for row in matrix]
    n = len(entries)
    previous = 1
    for k in range(n - 1):
        pivot = entries[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                entries[i][j] = (entries[i][j] * pivot - entries[i][k] * entries[k][j]) // previous
            entries[i][k] = 0
        previous = pivot
    return entries[-1][-1]


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

    def test_smith_determinant(self):
        for n in range(1, 9):
            for f in (lambda d: d, lambda d: d * d - 3 * d + 1):
                divisor_sums = {m: sum(f(d) for d in range(1, m + 1) if m % d == 0)
                                for m in range(1, n + 1)}
                matrix = [[divisor_sums[math.gcd(i, j)] for j in range(1, n + 1)]
                          for i in range(1, n + 1)]
                self.assertEqual(determinant(matrix), math.prod(f(d) for d in range(1, n + 1)))

    def test_lambert_coefficients_and_special_values(self):
        for m in range(1, 101):
            totient_sum = sum(sum(math.gcd(a, d) == 1 for a in range(1, d + 1))
                               for d in range(1, m + 1) if m % d == 0)
            self.assertEqual(totient_sum, m)
            liouville_sum = 0
            for d in range(1, m + 1):
                if m % d:
                    continue
                x, omega, factor = d, 0, 2
                while factor * factor <= x:
                    while x % factor == 0:
                        omega += 1
                        x //= factor
                    factor += 1
                if x > 1:
                    omega += 1
                liouville_sum += (-1) ** omega
            self.assertEqual(liouville_sum, int(math.isqrt(m) ** 2 == m))
        partial = sum(Fraction(sum(math.gcd(a, n) == 1 for a in range(1, n + 1)),
                               2**n - 1) for n in range(1, 31))
        self.assertGreater(partial, 2 - Fraction(1, 1_000_000))
        self.assertLess(partial, 2)

    def test_ramanujan_sums_and_orthogonality(self):
        for q in range(1, 13):
            for n in range(1, 13):
                direct = sum(cmath.exp(2j * math.pi * a * n / q)
                             for a in range(1, q + 1) if math.gcd(a, q) == 1)
                divisor_form = sum(d * mobius(q // d) for d in range(1, q + 1)
                                   if q % d == 0 and n % d == 0)
                self.assertAlmostEqual(direct.real, divisor_form, places=8)
                self.assertAlmostEqual(direct.imag, 0, places=8)
        for q in range(1, 9):
            for r in range(1, 9):
                N = math.lcm(q, r)
                def c(modulus, n):
                    return sum(cmath.exp(2j * math.pi * a * n / modulus)
                               for a in range(1, modulus + 1)
                               if math.gcd(a, modulus) == 1)
                average = sum(c(q, n) * c(r, n) for n in range(1, N + 1)) / N
                expected = sum(math.gcd(a, q) == 1 for a in range(1, q + 1)) if q == r else 0
                self.assertAlmostEqual(average.real, expected, places=8)
                self.assertAlmostEqual(average.imag, 0, places=8)

    def test_cyclotomic_values_and_inverse_identity(self):
        polynomials = cyclotomic_polynomials(40)
        for n, coefficients in polynomials.items():
            if n < 2:
                continue
            prime_powers = [p for p in range(2, n + 1) if is_prime(p)
                            and any(p**a == n for a in range(1, 7))]
            value_at_one = sum(coefficients)
            self.assertEqual(value_at_one, prime_powers[0] if prime_powers else 1)
            if n >= 3:
                expected_minus_one = 1 if n % 2 else sum(polynomials[n // 2])
                self.assertEqual(sum(c * (-1)**j for j, c in enumerate(coefficients)),
                                 expected_minus_one)
            if value_at_one == 1:
                # (1-X) Q(X) = 1-Phi_n(X), so Q(zeta) is an inverse of 1-zeta.
                q = [sum(coefficients[j + 1:]) for j in range(len(coefficients) - 1)]
                product = [q[0]] + [q[i] - q[i - 1] for i in range(1, len(q))] + [-q[-1]]
                self.assertEqual(product, [1 - coefficients[0]] + [-c for c in coefficients[1:]])


if __name__ == "__main__":
    unittest.main()
