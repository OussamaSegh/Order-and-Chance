"""Independent finite arithmetic checks for Volume 2's local cyclotomic proof.

No finite-field extension package is used. The factors are found by trial
division by monic polynomials, independently of the manuscript's field proof.
These finite checks support, but do not replace, the general proof.
"""
import itertools
import math
import re
import unittest
from functools import lru_cache
from pathlib import Path


CHAPTER = (Path(__file__).resolve().parents[1] / "volume2-integers"
           / "chapters" / "ch06-quadratic-reciprocity.tex")


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def exact_division(a, b):
    """Divide monic integer polynomials; coefficients in ascending order."""
    a, b = list(a), list(b)
    q = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        k, z = len(a) - len(b), a[-1]
        q[k] = z
        for j, bj in enumerate(b):
            a[k + j] -= z * bj
        a = list(trim(a))
    if a != [0]:
        raise AssertionError("Polynomial division had a nonzero remainder")
    return trim(q)


@lru_cache(None)
def cyclotomic(n):
    result = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            result = list(exact_division(result, cyclotomic(d)))
    return trim(result)


def divmod_p(a, b, p):
    a = list(trim([x % p for x in a]))
    b = list(trim([x % p for x in b]))
    q = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        k = len(a) - len(b)
        z = a[-1] * pow(b[-1], -1, p) % p
        q[k] = z
        for j, bj in enumerate(b):
            a[k + j] = (a[k + j] - z * bj) % p
        a = list(trim(a))
    return trim(q), trim(a)


def factors_by_trial(f, p):
    """Exhaustively find monic factors, without an algebra package."""
    f = trim([v % p for v in f])
    if len(f) <= 2:
        return [f]
    for d in range(1, (len(f) - 1) // 2 + 1):
        for coefficients in itertools.product(range(p), repeat=d):
            trial = coefficients + (1,)
            quotient, remainder = divmod_p(f, trial, p)
            if remainder == (0,):
                return factors_by_trial(trial, p) + factors_by_trial(
                    quotient, p
                )
    return [f]


def multiplicative_order(a, n):
    if math.gcd(a, n) != 1:
        raise ValueError("No multiplicative order")
    power = a % n
    for f in range(1, n + 1):
        if power == 1:
            return f
        power = power * a % n
    raise AssertionError("No multiplicative order found")


def polynomial_mul_p(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] = (c[i + j] + ai * bj) % p
    return trim(c)


def polynomial_pow_p(a, k, p):
    result = (1,)
    for _ in range(k):
        result = polynomial_mul_p(result, a, p)
    return result


class TestCyclotomicLocalProof(unittest.TestCase):
    def test_no_volume_three_field_theorem_import(self):
        source = CHAPTER.read_text(encoding="utf-8")
        exercise = source.split(r"\label{pb:phimodp}", 1)[1].split(
            r"\end{exercise}", 1
        )[0]
        solution = source.split(r"\begin{solution}{pb:phimodp}", 1)[1].split(
            r"\end{solution}", 1
        )[0]
        self.assertNotIn("Return to this problem after", exercise)
        self.assertNotIn("Volume~3 (finite fields", solution)
        self.assertIn("polynomial B", exercise)
        self.assertIn("polynomial B", solution)
        self.assertIn("p^d-1", solution)
        self.assertIn(r"\beta^{p^f}=\beta", solution)
        self.assertIn(r"\Phi_m(X^p)=\Phi_m(X)\Phi_{pm}(X)", solution)

    def test_factor_degrees_by_independent_trial_factorisation(self):
        checks = 0
        for n in range(2, 26):
            phi = sum(math.gcd(k, n) == 1 for k in range(1, n + 1))
            if phi > 8:  # Keep trial division fast and reproducible.
                continue
            for p in (2, 3, 5, 7):
                if n % p == 0:
                    continue
                factors = factors_by_trial(cyclotomic(n), p)
                f = multiplicative_order(p, n)
                with self.subTest(n=n, p=p):
                    self.assertEqual(len(factors), phi // f)
                    self.assertEqual(len(set(factors)), len(factors))
                    self.assertTrue(all(len(g) == f + 1 for g in factors))
                    product = (1,)
                    for factor in factors:
                        product = polynomial_mul_p(product, factor, p)
                    self.assertEqual(product, trim([x % p for x in cyclotomic(n)]))
                checks += 1
        self.assertGreaterEqual(checks, 40)

    def test_prime_power_index_congruence_mod_p(self):
        checks = 0
        for p in (2, 3, 5):
            for a in (1, 2, 3):
                for m in range(1, 11):
                    if m % p == 0 or p ** a * m > 110:
                        continue
                    lhs = trim([x % p for x in cyclotomic(p ** a * m)])
                    exponent = p ** (a - 1) * (p - 1)
                    rhs = polynomial_pow_p(cyclotomic(m), exponent, p)
                    with self.subTest(p=p, a=a, m=m):
                        self.assertEqual(lhs, rhs)
                    checks += 1
        self.assertGreaterEqual(checks, 40)

    def test_phi_eight_explicit_reductions(self):
        self.assertEqual(cyclotomic(8), (1, 0, 0, 0, 1))
        for p in (2, 3, 5, 7, 11, 13):
            factors = factors_by_trial(cyclotomic(8), p)
            self.assertGreaterEqual(len(factors), 2)


if __name__ == "__main__":
    unittest.main()
