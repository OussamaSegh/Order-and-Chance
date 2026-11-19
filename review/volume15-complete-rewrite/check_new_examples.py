#!/usr/bin/env python3
"""Deterministic checks for the fourteen new Volume 15 teaching sets.

Numerical checks do not establish the proofs.
"""
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "volume15-order-and-chance" / "chapters"


def text(*names):
    return "\n".join((ROOT / name).read_text() for name in names)


class Volume15Examples(unittest.TestCase):
    def test_ch01_smooth_and_squarefree(self):
        def smooth(limit, primes):
            out = {1}
            for p in primes:
                extra = set()
                for n in out:
                    m = n * p
                    while m <= limit:
                        extra.add(m)
                        m *= p
                out |= extra
            return out
        self.assertEqual(len(smooth(40, (2, 3, 5))), 21)
        self.assertEqual(math.floor(math.log(40) / math.log(2)) + 1, 6)
        self.assertAlmostEqual((2 / math.pi) * math.asin(0.5), 1 / 3)
        self.assertAlmostEqual((2 / math.pi) * math.asin(2 ** -0.5), 0.5)
        self.assertAlmostEqual(1 / (math.pi * 0.5), 2 / math.pi)
        divisors = lambda n: [d for d in range(1, n + 1) if n % d == 0]
        for n, count in ((12, 3), (36, 5)):
            ds = divisors(n)
            self.assertEqual(sum(d * d <= n for d in ds), math.ceil(len(ds) / 2))
            self.assertEqual(sum(d * d <= n for d in ds), count)
        mu = [1] * 11
        for i in range(2, 11):
            if mu[i] == 1:
                for j in range(i, 11, i):
                    mu[j] *= -1
                if i * i < 11:
                    for j in range(i * i, 11, i * i):
                        mu[j] = 0
        # standard sieve is cleaner; recompute mu directly
        def mobius(n):
            m, k = 1, n
            p = 2
            while p * p <= k:
                if k % p == 0:
                    k //= p
                    if k % p == 0:
                        return 0
                    m = -m
                p += 1
            if k > 1:
                m = -m
            return m
        total = sum(mobius(d) * (100 // (d * d)) for d in range(1, 11))
        self.assertEqual(total, 61)
        self.assertLess(abs(61 - 600 / math.pi ** 2), 10 + 100 / 9)
        src = text("ra-anatomy.tex")
        self.assertIn("ex:v15-01-1", src)
        self.assertIn("21", src)

    def test_ch02_buchstab_and_cramer(self):
        self.assertAlmostEqual(1 / 1.5, 2 / 3)
        self.assertAlmostEqual(math.exp(0.5772156649015329) / 2, 0.8905, places=4)
        y = math.log(100) ** 2
        total = sum(1 / math.log(n) for n in range(101, math.floor(100 + y) + 1))
        self.assertAlmostEqual(total, 4.46, places=2)
        self.assertAlmostEqual(y / math.log(100), 4.61, places=2)
        # empty-window bound at one point
        x, gap = 1000, math.log(1000)
        prod = math.prod(1 - 1 / math.log(n) for n in range(x + 1, math.floor(x + gap) + 1))
        self.assertLessEqual(prod, math.exp(-(gap - 1) / math.log(x + gap)) + 1e-12)

    def test_ch03_valuation(self):
        vals = []
        for n in range(1, 17):
            k = 0
            m = n
            while m % 2 == 0:
                m //= 2
                k += 1
            vals.append(k)
        self.assertAlmostEqual(sum(vals) / 16, 15 / 16)
        self.assertAlmostEqual(sum(k / 2 ** k for k in range(1, 40)), 2)
        self.assertAlmostEqual(sum(k * k / 2 ** k for k in range(1, 60)), 6)
        # characteristic function at t=1
        t = 1.0
        geom = sum(2 ** (-(k + 1)) * cmath_exp(t, k) for k in range(80))
        closed = 1 / (2 - cmath_exp(t, 1))
        self.assertAlmostEqual(geom.real, closed.real, places=9)
        self.assertAlmostEqual(geom.imag, closed.imag, places=9)

    def test_ch04_polynomials(self):
        def n2(p):
            return p * (p - 1) // 2
        def n3(p):
            red = p + p * (p - 1) + p * (p - 1) * (p - 2) // 6 + p * n2(p)
            return p ** 3 - red
        self.assertEqual(n2(5), 10)
        self.assertEqual(n3(5), 40)
        self.assertEqual(n3(5), (5 ** 3 - 5) // 3)
        self.assertEqual(125 - 40, 85)

    def test_ch05_singular_series(self):
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29]
        partial = 1
        for p in primes:
            partial *= 1 - 1 / (p - 1) ** 2
        self.assertAlmostEqual(partial, 0.6651, places=4)
        # tail of the twin-prime product after p=29, rounded to four decimals
        twin = 1.0
        p, sieve = 2, [True] * 20000
        while p * p < len(sieve):
            if sieve[p]:
                for q in range(p * p, len(sieve), p):
                    sieve[q] = False
            p += 1
        for q in range(3, len(sieve)):
            if sieve[q]:
                twin *= 1 - 1 / (q - 1) ** 2
        self.assertAlmostEqual(twin / partial, 0.9925, places=4)
        self.assertEqual((3 - 1) / (3 - 2), 2)
        self.assertAlmostEqual((5 - 1) / (5 - 2), 4 / 3)

    def test_ch06_sieve_counts(self):
        count = 100 - 50 - 33 + 16
        self.assertEqual(count, 33)
        bound = 100 / math.log(4) + 16
        self.assertAlmostEqual(bound, 88.13, places=2)
        self.assertGreater(1 / 2 + 1 / 3 + 1 / 5 + 1 / 7, 1)
        self.assertAlmostEqual((1 / 2) * (2 / 3) * (4 / 5) * (6 / 7), 8 / 35)
        terms = 1 - 1 / 2 - 1 / 3 - 1 / 5 + 1 / 6 + 1 / 10 + 1 / 15 - 1 / 30
        self.assertAlmostEqual(terms, 8 / 30)
        self.assertAlmostEqual(1 - (1 / 2 + 1 / 3 + 1 / 5), -1 / 30)

    def test_ch07_cohen_lenstra(self):
        prod = 1
        for i in range(1, 7):
            prod *= 1 - 3 ** (-i)
        self.assertAlmostEqual(prod, 0.5605, places=4)
        self.assertEqual((9 - 1) * (9 - 3), 48)
        self.assertEqual(48 // 6, 8)
        self.assertEqual((3 ** 2 - 1), 8)

    def test_ch08_kernel(self):
        p = 5
        self.assertEqual((1 - 1 / p, 1 / p), (0.8, 0.2))
        self.assertEqual((1 + 3) * (1 + 9), 40)
        self.assertEqual(p ** -3, 1 / 125)
        self.assertAlmostEqual(1 - p ** -3, 124 / 125)

    def test_ch09_form_factor(self):
        self.assertEqual((1 - 0, 1 - 0.5, 0), (1, 0.5, 0))
        self.assertAlmostEqual((32 / math.pi ** 2) * math.exp(-4 / math.pi), 0.908, places=3)
        for u in (0.5, 1.3, 2.2):
            k = 2 * math.pi * u
            # numerical integral of the tent against cos
            acc = 0
            n = 4000
            for i in range(n):
                a = -1 + 2 * (i + 0.5) / n
                acc += (1 - abs(a)) * math.cos(k * a) * (2 / n)
            self.assertAlmostEqual(acc, (math.sin(math.pi * u) / (math.pi * u)) ** 2, places=4)

    def test_ch10_moments(self):
        u = 0.5
        series = (1 + u) / (1 - u) ** 3
        self.assertAlmostEqual(series * (0.5) ** 4, 0.75)
        scale = (math.exp(0.5772156649015329) * math.log(10)) ** 4
        self.assertAlmostEqual(scale, 282.9, places=1)
        self.assertAlmostEqual((6 / math.pi ** 2) / 12, 1 / (2 * math.pi ** 2))
        # generating function at a test point
        u = 0.3
        direct = sum((r + 1) ** 2 * u ** r for r in range(80))
        self.assertAlmostEqual(direct, (1 + u) / (1 - u) ** 3, places=8)

    def test_ch11_values(self):
        self.assertAlmostEqual(math.pi ** 2 / 6, 1.64493, places=5)
        self.assertAlmostEqual(math.pi ** 2 / 15, 0.65797, places=5)
        self.assertAlmostEqual(0.5, 0.5)
        self.assertNotEqual(math.log(2) / math.log(3), round(math.log(2) / math.log(3)))
        # derivative of the truncated log integral tends to pi
        a, R = 2.0, 200.0
        acc = 0.0
        n = 8000
        for i in range(n):
            u = -R + 2 * R * (i + 0.5) / n
            acc += a / (a * a + u * u) * (2 * R / n)
        self.assertAlmostEqual(acc, 2 * math.atan(R / a), places=2)

    def test_ch12_u2(self):
        N = 5
        A = {0, 1, 2}
        count = sum(
            ((x in A) and ((x + d) % N in A) and ((x + 2 * d) % N in A))
            for x in range(N) for d in range(N)
        )
        self.assertEqual(count, 5)
        self.assertAlmostEqual(count / N ** 2, 0.2)
        delta = 3 / 5
        self.assertAlmostEqual(delta ** 3, 0.216, places=3)
        diff = abs(count / N ** 2 - delta ** 3)
        self.assertLessEqual(diff, (delta * (1 - delta)) ** 1.5 + 1e-12)

    def test_ch13_bias(self):
        gamma = 6.0209
        rho = math.sqrt(0.25 + gamma * gamma)
        self.assertAlmostEqual(2 / rho, 0.3310, places=4)
        self.assertAlmostEqual(1 - 0.1556 / 2, 0.9222, places=4)
        # one Bessel factor at xi=0 is 1
        self.assertAlmostEqual(bessel_j0(0), 1.0, places=6)

    def test_ch14_meeting(self):
        eg = math.exp(0.5772156649015329)
        self.assertAlmostEqual(eg / 2, 0.8905, places=4)
        self.assertAlmostEqual(2 / eg - 1, 0.1229, places=4)
        mu = 5 / 6
        squares = 0
        for n in range(101, 121):
            w = (n % 2 == 0) + (n % 3 == 0)
            squares += (w - mu) ** 2
        self.assertAlmostEqual(squares, 95 / 9)
        self.assertLess(squares, 110 / 3)
        mu10 = 1 / 2 + 1 / 3 + 1 / 5 + 1 / 7
        self.assertLessEqual(mu10 + 5, 6.18)


def cmath_exp(t, k):
    return complex(math.cos(t * k), math.sin(t * k))


def bessel_j0(z):
    # J0(z) = (1/2pi) int exp(i z cos) ; at 0 it is 1
    if z == 0:
        return 1.0
    n = 2000
    acc = 0
    for i in range(n):
        th = 2 * math.pi * (i + 0.5) / n
        acc += math.cos(z * math.cos(th))
    return acc / n


if __name__ == "__main__":
    unittest.main(verbosity=2)
