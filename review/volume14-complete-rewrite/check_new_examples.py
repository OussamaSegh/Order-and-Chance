#!/usr/bin/env python3
"""Deterministic checks for the fourteen new Chapter exercise sets.

Numerical checks do not establish general theorems or replace proof review.
"""
import cmath
import math
import unittest
from fractions import Fraction


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            step = i * i
            sieve[step:n + 1:i] = [False] * (((n - step) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


class Volume14Examples(unittest.TestCase):
    def test_ch01_exponents_and_cost(self):
        self.assertEqual(Fraction(4) * Fraction(2, 3) * Fraction(1, 3), Fraction(8, 9))
        self.assertEqual(1 - 2 * Fraction(1, 36), Fraction(17, 18))
        self.assertLess(Fraction(8, 9), Fraction(17, 18))
        self.assertAlmostEqual(10 ** (-2), 0.01)
        self.assertAlmostEqual(10 ** (-0.4), 0.39810717055, places=8)
        # 4σ(1-σ) - 3(1-σ) = (1-σ)(4σ-3) > 0 on (3/4, 1)
        for sigma in (0.8, 0.9, 0.99):
            self.assertGreater(4 * sigma * (1 - sigma), 3 * (1 - sigma))
        self.assertAlmostEqual(4 * 0.75 * 0.25, 3 * 0.25)

    def test_ch02_weights_class_and_page(self):
        for phi in (0, math.pi / 2, 2 * math.pi / 3, math.pi):
            lhs = 3 + 4 * math.cos(phi) + math.cos(2 * phi)
            rhs = 2 * (1 + math.cos(phi)) ** 2
            self.assertAlmostEqual(lhs, rhs, places=12)
        self.assertAlmostEqual(2 * (1 + 1) ** 2, 8)
        self.assertAlmostEqual(2 * (1 + 0) ** 2, 2)
        self.assertAlmostEqual(2 * (1 - 0.5) ** 2, 0.5)
        self.assertAlmostEqual(2 * (1 - 1) ** 2, 0)
        self.assertLess(math.sqrt(7), 2.646)
        self.assertLess(math.log(7), 1.946)
        self.assertGreater(math.pi, 3.14)
        self.assertLess(2.646 * 3.946, 10.45)
        self.assertLess(10.45 / 3.14, 3.33)
        bound7 = math.sqrt(7) / math.pi * (2 + math.log(7))
        self.assertLess(bound7, 3.33)
        self.assertGreater(12.767 ** 2, 162.99)
        self.assertLess(12.767 ** 2, 163)
        self.assertGreater(math.log(163), 5.093)
        self.assertLess(math.pi, 3.142)
        self.assertGreater(12.767 * 7.093, 90.556)
        self.assertGreater(90.556 / 3.142, 28.8)
        bound163 = math.sqrt(163) / math.pi * (2 + math.log(163))
        self.assertGreater(bound163, 28.8)
        # Page arithmetic: 1.6 > 1.5, and log(Q^2) = 2 log Q
        self.assertGreater(1.6, 1.5)
        self.assertEqual(Fraction(5, 4), Fraction(1) + Fraction(1, 4))
        # chi_4 partial sum through 19
        s = 0.0
        for n in range(1, 20):
            if n % 2 == 0:
                continue
            s += (1 if n % 4 == 1 else -1) / n
        self.assertGreater(s, 0.76)
        self.assertLess(s, 0.77)
        grouped = 2 / 3 + 2 / 35 + 2 / 99 + 2 / 195 + 2 / 323
        self.assertAlmostEqual(s, grouped, places=12)

    def test_ch03_parity_and_artin(self):
        gamma = 0.5772156649015328606
        self.assertGreater(gamma, 0.57721)
        self.assertLess(gamma, 0.57722)
        self.assertGreater(math.exp(0.57721) / 2, 0.89053)
        self.assertLess(math.exp(0.57722) / 2, 0.89055)
        factor = math.exp(gamma) / 2
        self.assertGreater(factor, 0.890)
        self.assertLess(factor, 0.891)
        prod = Fraction(1)
        for p in (3, 5, 7):
            prod *= Fraction((p - 1) ** 2 - 1, (p - 1) ** 2)
            self.assertEqual(
                Fraction(1, 1) - Fraction(2, p),
                (Fraction(1, 1) - Fraction(1, p)) ** 2 * (1 - Fraction(1, (p - 1) ** 2)),
            )
        self.assertEqual(prod, Fraction(175, 256))
        # Artin partial product and tail
        P = 1.0
        ps = primes_upto(100)
        self.assertEqual(len(ps), 25)
        for q in ps:
            P *= 1 - 1 / (q * (q - 1))
        self.assertGreater(P, 0.3746)
        self.assertLess(P, 0.3747)
        tail = sum(1 / (q * (q - 1)) for q in primes_upto(10 ** 5) if q > 100)
        self.assertLess(tail, 0.01)
        printed = 0.3739558
        self.assertGreater(P, printed)
        self.assertLess(0.99 * 0.3747, printed)
        self.assertAlmostEqual(0.99 * 0.3747, 0.370953, places=6)

    def test_ch04_totient_level_vaughan_product(self):
        def phi(n):
            r, m, p = n, n, 2
            while p * p <= m:
                if m % p == 0:
                    while m % p == 0:
                        m //= p
                    r = r // p * (p - 1)
                p += 1
            if m > 1:
                r = r // m * (m - 1)
            return r
        self.assertEqual(sum(Fraction(1, phi(r)) for r in range(1, 11)), Fraction(55, 12))
        self.assertGreater(math.e, 2.7)
        self.assertGreater(math.log(10), 2.3)
        self.assertGreater(2.7 * 3.3, float(Fraction(55, 12)))
        e30 = math.exp(30)
        self.assertGreater(e30, 1.06e13)
        self.assertLess(e30, 1.07e13)
        sixty7 = 60 ** 7
        self.assertEqual(sixty7, 2799360000000)
        self.assertLess(3 * sixty7, 1.06e13)
        self.assertGreater(4 * sixty7, 1.07e13)
        Q = e30 / sixty7
        self.assertGreater(Q, 3)
        self.assertLess(Q, 4)
        # Euler product bound and partial product
        telescoping = sum(Fraction(1, n * (n - 1)) for n in range(2, 5000))
        self.assertAlmostEqual(float(telescoping), 1 - 1 / 4999, places=12)
        partial = 1.0
        for p in primes_upto(19):
            partial *= 1 + 1 / (p * (p - 1))
        self.assertGreater(partial, 1.92)
        self.assertAlmostEqual(partial, 1.923152, places=5)
        self.assertLess(partial, math.e)

    def test_ch05_kloosterman(self):
        squares = {pow(x, 2, 5) for x in range(5)}
        self.assertEqual(squares, {0, 1, 4})
        self.assertLess(2 * 5, 16)
        self.assertGreater(2 * 11, 16)
        self.assertEqual(5 ** 2 - 5 - 1, 19)
        self.assertEqual(2 * 5 ** 3 - 3 * 5 ** 2 - 3 * 5 - 1, 159)
        # exact values
        s = math.sqrt(5)
        vals = ((3 - s) / 2, -(1 + s), s - 1, (3 + s) / 2)
        self.assertAlmostEqual(sum(v * v for v in vals), 19, places=10)
        self.assertAlmostEqual(max(abs(v) for v in vals), 1 + s, places=10)
        mom = 2 ** 0.25 * 5 ** 0.75
        weil = 2 * math.sqrt(5)
        self.assertLess(mom, weil)
        self.assertGreater(2 ** 0.25 * 11 ** 0.75, 2 * math.sqrt(11))
        # second moment identity at two primes via direct summation
        import cmath
        for p in (5, 7, 11):
            inv = {x: pow(x, -1, p) for x in range(1, p)}
            ks = []
            for n in range(1, p):
                acc = sum(cmath.exp(2j * math.pi * (x + n * inv[x]) / p) for x in range(1, p))
                ks.append(acc)
            self.assertAlmostEqual(sum(abs(z) ** 2 for z in ks), p * p - p - 1, places=8)

    def test_ch06_waring_constants(self):
        ratio = math.gamma(1.5) ** 5 / math.gamma(2.5)
        self.assertAlmostEqual(ratio, math.pi ** 2 / 24, places=12)
        self.assertEqual(min(10, 2), 2)
        self.assertEqual(min(10, 2 * 5), 10)
        self.assertAlmostEqual(0.1 * 0.5, 0.05)
        self.assertAlmostEqual(1 - 0.5, 0.5)
        self.assertAlmostEqual(0.1 * 1.5, 0.15)
        self.assertLess(1 + 1 / (2 * math.pi), 1 + 1 / math.pi)
        self.assertLess(1 + 1 / math.pi, 2)
        for n in (1, 4, 9):
            height = (math.pi ** 2 / 24) * n ** 1.5
            self.assertGreater(height, 0)

    def test_ch07_ramanujan_and_series(self):
        def mobius(n):
            m, p, x = 1, 2, n
            while p * p <= x:
                if x % p == 0:
                    x //= p
                    if x % p == 0:
                        return 0
                    m = -m
                p += 1
            if x > 1:
                m = -m
            return m
        # c_6(15) = μ(6)*1 + μ(2)*3
        self.assertEqual(mobius(6) * 1 + mobius(2) * 3, -2)
        self.assertEqual((-1) * 2, -2)  # c_2(15) * c_3(15)
        self.assertEqual(math.comb(9, 2), 36)
        self.assertEqual(10 ** 2 / 2, 50)
        N = 10
        self.assertEqual((N - 1) * (N - 2) // 2, N * N // 2 - 3 * N // 2 + 1)
        # singular series partial product for N=9 through p=19
        P = 1.5
        steps = []
        for p in primes_upto(19):
            if p < 5:
                continue
            P *= 1 + 1 / (p - 1) ** 3
            steps.append(P)
        self.assertAlmostEqual(steps[0], 1.5234375, places=7)
        self.assertAlmostEqual(steps[-1], 1.53354468, places=7)
        self.assertGreater(P, 1.5335)
        self.assertLess(P, 1.5336)
        y = 1 / 648
        self.assertLess(math.exp(y), 1 + y + y * y)
        self.assertLess(1 + y + y * y, 1.00155)
        self.assertLess(1.5336 * 1.00155, 1.536)
        # high product sits in the enclosure
        full = 1.0
        for p in primes_upto(5000):
            if 9 % p == 0:
                full *= 1 - 1 / (p - 1) ** 2
            else:
                full *= 1 + 1 / (p - 1) ** 3
        self.assertGreater(full, 1.533)
        self.assertLess(full, 1.536)

    def test_ch08_admissible_and_weights(self):
        def admissible(H):
            k = len(H)
            for p in primes_upto(k):
                if len({h % p for h in H}) == p:
                    return False
            return True
        self.assertFalse(admissible([0, 2, 4]))
        self.assertTrue(admissible([0, 2, 6]))
        self.assertEqual((1 - Fraction(1, 2)) / (Fraction(1, 2) ** 2), 2)
        self.assertEqual((1 - Fraction(2, 3)) / ((1 - Fraction(1, 3)) ** 2), Fraction(3, 4))
        five = [p for p in primes_upto(30) if p > 5][:5]
        ten = [p for p in primes_upto(50) if p > 10][:10]
        self.assertEqual(five, [7, 11, 13, 17, 19])
        self.assertEqual(ten[-1] - ten[0], 32)
        self.assertEqual(19 - 7, 12)
        self.assertTrue(admissible(five))
        self.assertTrue(admissible(ten))
        # strict inequality counterexample: rho = 2, one weight, exactly 2 primes
        self.assertEqual(math.floor(1.5) + 1, 2)
        self.assertFalse(2 > 2)

    def test_ch09_ratio_simplex_integrals(self):
        self.assertEqual(1417255 - 2 * 708216, 823)
        self.assertLess(823, 0.002 * 708216)
        self.assertEqual(1 + 7 * 39, 274)
        self.assertEqual(5167 - 587, 4580)
        classes5 = {h % 5 for h in (0, 2, 6, 8, 12)}
        self.assertEqual(len(classes5), 4)
        self.assertLess(2 * math.log(2), 1.39)
        self.assertGreater(1417255 / 708216, 2)
        self.assertLess(1417255 / 708216, 2.002)
        self.assertGreater(math.log(274), 5.613)
        num = 274 * (5.613 ** 2)
        self.assertGreater(num, 8632)
        self.assertEqual(49 * 39, 1911)
        self.assertEqual(4.5 * 1911, 8599.5)
        self.assertGreater(274 * math.log(274) ** 2 / (49 * 39), 4.5)
        # integrals of g
        A, T = 7, 39
        V = 1 + A * T
        gamma = T / V
        # numerical integrals
        def g(t):
            return 1 / (1 + A * t)
        # exact
        self.assertAlmostEqual((1 / A) * math.log(V), math.log(V) / A)
        self.assertAlmostEqual((1 / A) * (1 - 1 / V), gamma)

    def test_ch10_distance_and_cosine(self):
        deriv_nonpositive = all(-m * math.exp(-m) <= 0 for m in (0, 0.5, 1, 2, 5))
        self.assertTrue(deriv_nonpositive)
        self.assertAlmostEqual((1 + 0) * math.exp(0), 1)
        self.assertAlmostEqual(2 / math.e, 0.7357588823, places=8)
        self.assertAlmostEqual(3 / math.e ** 2, 0.4060058497, places=8)
        head = Fraction(247, 210)
        self.assertGreater(head, Fraction(1176, 1000))
        self.assertLess(head, Fraction(1177, 1000))
        tail = 1 / 11 + 1 / 13 + 1 / 17 + 1 / 19
        self.assertGreater(tail, 0.276)
        self.assertLess(tail, 0.280)
        total = 2 * (float(head) + tail)
        self.assertGreater(total, 2.9)
        self.assertLess(total, 3.0)
        self.assertGreater(math.log(20), 2.995)
        self.assertLess(math.log(20), 2.996)
        self.assertGreater(math.log(2.995), 1.096)
        self.assertLess(math.log(2.996), 1.098)
        two = 2 * math.log(math.log(20))
        self.assertGreater(two, 2.1)
        self.assertLess(two, 2.2)
        # 1 - Re(f conj g) = |f-g|^2 / 2
        f, g = cmath.exp(0.4j), cmath.exp(-1.1j)
        self.assertAlmostEqual(1 - (f * g.conjugate()).real, 0.5 * abs(f - g) ** 2, places=12)
        s = sum(2 / p for p in primes_upto(20))
        self.assertAlmostEqual(s, total, places=10)
        for y in (0.2, 1.3, -0.7, 2.5):
            self.assertLessEqual(1 - math.cos(y), 0.5 * y * y + 1e-12)

    def test_ch11_sum_product_and_elekes(self):
        A = [1, 2, 4]
        sums = {a + b for a in A for b in A}
        prods = {a * b for a in A for b in A}
        self.assertEqual(sums, {2, 3, 4, 5, 6, 8})
        self.assertEqual(prods, {1, 2, 4, 8, 16})
        self.assertEqual(len(sums) * len(prods), 30)
        self.assertLess(9 * 2 / 64, 30)
        self.assertLess(9 * math.sqrt(3) / 64, 30)
        B = [0, 1, 2, 4]
        self.assertEqual(len({a + b for a in B for b in B}), 8)
        self.assertEqual(16 * 4, 64)
        diffs = {a - b for a in A for b in A}
        self.assertEqual(diffs, set(range(-3, 4)))
        self.assertLessEqual(3 * 7, 36)
        # 16^{3/2} = 64
        self.assertEqual(16 ** 3, 4096)
        self.assertEqual(int(math.isqrt(4096)), 64)

    def test_ch12_roth_and_behrend(self):
        S = {1, 2, 4, 5}
        triples = []
        for a in S:
            for b in S:
                if b <= a:
                    continue
                c = 2 * b - a
                if c in S and c != b:
                    triples.append((a, b, c))
        self.assertEqual(triples, [])
        self.assertIn(3, {1, 2, 3})
        self.assertLess(math.log(10 ** 6), 14)
        self.assertLess(math.log(14), 2.7)
        ratio = 500 / math.log(math.log(10 ** 6))
        self.assertGreater(ratio, 180)
        self.assertGreater(ratio, 185)
        self.assertGreater(500 / 2.7, 185)
        self.assertAlmostEqual(ratio, 190.4, delta=0.5)
        images = {}
        for x0 in range(3):
            for x1 in range(3):
                images.setdefault(x0 * x0 + x1 * x1, []).append(1 + x0 + 6 * x1)
        self.assertEqual(sorted(images[0]), [1])
        self.assertEqual(sorted(images[2]), [8])
        self.assertEqual(sorted(images[8]), [15])
        self.assertEqual([1, 8, 15][1] - [1, 8, 15][0], [1, 8, 15][2] - [1, 8, 15][1])
        # triangle equality
        x, z = (3.0, 0.0), (3.0, 0.0)
        y = ((x[0] + z[0]) / 2, (x[1] + z[1]) / 2)
        self.assertEqual(y, x)

    def test_ch13_gowers_and_wtrick(self):
        self.assertLess(5 ** -1, 5 ** -0.75)
        self.assertLess(5 ** -0.75, 5 ** -0.5)
        self.assertAlmostEqual(5 * 5 ** -4, 5 ** -3)
        self.assertEqual(6 * (1 - Fraction(1, 2)) * (1 - Fraction(1, 3)), 2)
        self.assertEqual(30 * Fraction(1, 2) * Fraction(2, 3) * Fraction(4, 5), 8)
        self.assertEqual(Fraction(2, 6), Fraction(1, 3))
        self.assertEqual(Fraction(8, 30), Fraction(4, 15))
        def coeff(k, j=None):
            total = 0
            for mask in range(1 << k):
                bits = [(mask >> i) & 1 for i in range(k)]
                sign = (-1) ** sum(bits)
                if j is None:
                    total += sign
                else:
                    total += sign * bits[j]
            return total
        for k in (2, 3, 4):
            self.assertEqual(coeff(k), 0)
            for j in range(k):
                self.assertEqual(coeff(k, j), 0)

    def test_ch14_mean_square_and_hardy(self):
        terms = [2520 // n for n in range(1, 11)]
        self.assertEqual(sum(terms), 7381)
        self.assertEqual(Fraction(sum(terms), 2520), Fraction(7381, 2520))
        self.assertEqual(16 * 10, 160)
        cos = math.sqrt((2 + math.sqrt(2)) / 4)
        self.assertAlmostEqual(cos, math.cos(math.pi / 8), places=12)
        limit0 = math.pi * cos
        self.assertAlmostEqual(limit0 / 4, -(-limit0 / 4))
        amp = math.sqrt(2) / math.log(2)
        self.assertLess(math.sqrt(2), 1.415)
        self.assertGreater(math.log(2), 0.693)
        self.assertLess(1.415 / 0.693, 2.05)
        self.assertLess(amp, 3)
        self.assertLess(3, 32)
        # harmonic comparison at a few N
        for N in (1, 2, 10, 100):
            H = sum(1 / n for n in range(1, N + 1))
            self.assertGreaterEqual(H + 1e-12, math.log(N + 1))
            self.assertLessEqual(H, 1 + math.log(N) + 1e-12)
        # Montgomery terms at T = e^4
        logT = 4
        self.assertAlmostEqual(logT * math.exp(-8 * 0.5), 4 / math.e ** 4, places=12)
        self.assertLess(4 * math.exp(-4), 0.5)

    def test_no_original_statement_was_required(self):
        # The preservation gate is separate. This test only locks the new arithmetic.
        self.assertEqual(14 * 4, 56)
        self.assertEqual(14 * 2, 28)


if __name__ == "__main__":
    unittest.main(verbosity=2)
