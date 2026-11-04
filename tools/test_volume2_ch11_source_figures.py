"""Complete Chapter 11 plotted data and independently reconstructed examples."""

from collections import Counter
from fractions import Fraction as F
from itertools import product
import math
from pathlib import Path
import re
import unittest

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]/'volume2-integers'


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))


def mu(n):
    factors = [p for p in range(2, n+1) if prime(p) and n % p == 0]
    return 0 if any(n % (p*p) == 0 for p in factors) else (-1)**len(factors)


def chi4(n):
    return 0 if n % 2 == 0 else 1 if n % 4 == 1 else -1


def chi8(n):
    return 0 if n % 2 == 0 else 1 if n % 8 in (1, 7) else -1


class ChapterElevenSourceChecks(unittest.TestCase):
    def test_all_clock_entries_and_complete_multiplicativity(self):
        source = (ROOT/'figures/ch14-chi8.tex').read_text()
        entries = [(int(n), int(v), c) for n, v, c in re.findall(r'(\d+)/([+-]?\d+)/(oc\w+)', source)]
        self.assertEqual([n for n, _, _ in entries], list(range(8)))
        self.assertEqual([v for _, v, _ in entries], [chi8(n) for n in range(8)])
        self.assertEqual([c for _, _, c in entries], ['ocInk', 'ocTeal', 'ocInk', 'ocCoralDeep', 'ocInk', 'ocCoralDeep', 'ocInk', 'ocTeal'])
        for a, b in product(range(8), repeat=2):
            self.assertEqual(chi8(a*b), chi8(a)*chi8(b))
        for p in range(3, 1000, 2):
            if prime(p):
                self.assertEqual(pow(2, (p-1)//2, p), chi8(p) % p)
        self.assertIn('90-\\k*45', source)

    def test_every_prime_race_point_and_horizontal_cutoff(self):
        source = (ROOT/'figures/ch14-race.tex').read_text()
        blocks = re.findall(r'\\foreach \\x/\\y in \{([^}]+)\}', source)
        self.assertEqual(len(blocks), 2)
        for block, residue in zip(blocks, (3, 1)):
            data = [(int(x), int(y)) for x, y in re.findall(r'(\d+)/(\d+)', block)]
            self.assertEqual([x for x, _ in data], list(range(0, 20, 2)))
            for x, count in data:
                cutoff = 10+5*x
                self.assertEqual(count, sum(prime(p) and p % 4 == residue for p in range(2, cutoff+1)))
        ticks = re.search(r'\\foreach \\t/\\lab in \{([^}]+)\}', source)[1]
        self.assertTrue(all(int(label) == 10+5*int(x) for x, label in re.findall(r'(\d+)/(\d+)', ticks)))
        self.assertIn('18/100', ticks)
        # The caption must restrict its strict lead to the actual cutoffs:
        # at17 there is a tie (3 and3), so a claim at every x would fail.
        self.assertEqual(sum(prime(p) and p % 4 == 1 for p in range(2, 18)), 3)
        self.assertEqual(sum(prime(p) and p % 4 == 3 for p in range(2, 18)), 3)

    def test_every_sieve_cell_survivor_and_dot(self):
        source = (ROOT/'figures/ch14-sieve.tex').read_text()
        blocks = re.findall(r'\\foreach \\n/\\x/\\y in \{([^}]+)\}', source)
        self.assertEqual(len(blocks), 2)
        for block, expected in zip(blocks, ({n for n in range(1, 31) if math.gcd(n, 30) == 1}, set(range(5, 31, 5)))):
            entries = [(int(n), int(x), int(y)) for n, x, y in re.findall(r'(\d+)/(\d+)/(-?\d+)', block)]
            self.assertEqual({n for n, _, _ in entries}, expected)
            self.assertEqual(len(entries), len(expected))
            for n, x, y in entries:
                self.assertEqual((x, y), ((n-1) % 15, 0 if n <= 15 else -1))
        self.assertIn('dark grey frame', source)
        self.assertIn('ochre dot', source)
        self.assertNotIn('teal frame:', source)
        for cutoff, expected in ((30, 8), (48, 13), (49, 14), (50, 14), (100, 26)):
            count = sum(math.gcd(n, 30) == 1 for n in range(1, cutoff+1))
            self.assertEqual(count, expected)
            self.assertEqual(count, sum(mu(d)*(cutoff//d) for d in range(1, 31) if 30 % d == 0))
        self.assertEqual(sum(mu(d)*(100//d) for d in range(1, 211) if 210 % d == 0), 22)
        self.assertNotEqual(30 % 4, 0)
        self.assertNotEqual(30 % 9, 0)

    def test_all_cubic_plot_primes_counts_norm_forms_and_rounding(self):
        source = (ROOT/'figures/ch05-cubic.tex').read_text()
        data = [(int(p), float(y)) for p, y in re.findall(r'\\fill\[MidnightBlue\] \((\d+),(-?[\d.]+)\)', source)]
        expected_primes = [p for p in range(2, 3000) if prime(p) and p % 3 == 1]
        self.assertEqual([p for p, _ in data], expected_primes)
        edge, middle = 0, 0
        for p, plotted in data:
            roots = Counter(pow(x, 3, p) for x in range(p))
            count = sum(k*roots[(1-u) % p] for u, k in roots.items())
            a = count-(p-2)
            # Separate derivation via the integral norm form and trace class,
            # independent of the cube-root convolution and original generator.
            candidates = {A for B in range(-math.isqrt(4*p//27), math.isqrt(4*p//27)+1)
                          for A in range(-math.isqrt(4*p), math.isqrt(4*p)+1)
                          if A % 3 == 1 and A*A+27*B*B == 4*p}
            self.assertEqual(candidates, {a})
            self.assertLessEqual(a*a, 4*p)
            exact = a/(2*math.sqrt(p))
            self.assertLessEqual(abs(plotted-exact), .000050001)
            edge += abs(exact) >= .8
            middle += abs(exact) <= .2
        self.assertGreater(edge, middle)
        self.assertEqual(len(data), len(set(p for p, _ in data)))

    def test_new_sign_rows_and_mod8_detector_including_nonunits(self):
        rows = [lambda n: int(n % 2 == 1), chi4, chi8, lambda n: chi4(n)*chi8(n)]
        self.assertEqual(len({tuple(f(n) for n in range(8)) for f in rows}), 4)
        self.assertEqual(sum(chi4(n)*chi8(n) for n in range(8)), 0)
        for n in range(-40, 41):
            numerator = rows[0](n)+chi4(n)-chi8(n)-chi4(n)*chi8(n)
            self.assertEqual(numerator, 4*int(n % 8 == 5))
        self.assertEqual(1+chi4(2)-chi8(2)-chi4(2)*chi8(2), 1)

    def test_euler_examples_and_finite_mobius_arithmetic(self):
        partial = sum((F(1, n*n) for n in range(1, 31)), F())
        product_value = math.prod(F(p*p, p*p-1) for p in range(2, 31) if prime(p))
        self.assertTrue(F('1.61215') < partial < F('1.61216'))
        self.assertTrue(F('1.63307') < product_value < F('1.63308'))
        self.assertLess(partial, product_value)
        mobius = sum((F(mu(n), n*n) for n in range(1, 11)), F())
        self.assertTrue(F('.61625') < mobius < F('.61635'))
        self.assertEqual(1-F(1, 4)-F(1, 9)+F(1, 36), F(2, 3))
        with mp.workdps(40):
            retained = mp.fsum(mp.mpf(1)/(n*n) for n in range(1, 10001) if math.gcd(n, 6) == 1)
            self.assertTrue(retained < mp.pi**2/9 < retained+mp.mpf(1)/10000)
        self.assertEqual(sum(mu(n)*(10//n) for n in range(1, 11)), 1)
        grouped = sum((F(1, 4*k+1)-F(1, 4*k+3) for k in range(3)), F())
        self.assertEqual(grouped, F(2578, 3465))

    def test_large_four_square_count_by_quotient_blocks(self):
        def triangular(n):
            return n*(n+1)//2
        def divisor_sum_total(x):
            total, left = 0, 1
            while left <= x:
                q = x//left
                right = x//q
                total += q*(triangular(right)-triangular(left-1))
                left = right+1
            return total
        x = 10**7
        total = 8*(divisor_sum_total(x)-4*divisor_sum_total(x//4))
        self.assertEqual(total, 493480252693888)
        with mp.workdps(40):
            ratio = total/(mp.pi**2*x*x/2)
            self.assertLess(abs(ratio-mp.mpf('1.00000007')), mp.mpf('5e-9'))

    def test_all_small_power_sum_exceptions_below_proved_cutoffs(self):
        expected = {3: [7], 4: [5, 13, 17, 29],
                    8: [5, 13, 17, 29, 41, 73, 89, 97, 113, 137, 233, 257, 337, 761]}
        for k, bad_primes in expected.items():
            bad = []
            for p in range(2, k**4):
                if not prime(p):
                    continue
                powers = {pow(a, k, p) for a in range(p)}
                bits = sum(1 << a for a in powers)
                covered, mask = 0, (1 << p)-1
                for a in powers:
                    covered |= ((bits << a) | (bits >> (p-a))) & mask
                if covered != mask:
                    bad.append(p)
            self.assertEqual(bad, bad_primes)


if __name__ == '__main__':
    unittest.main()
