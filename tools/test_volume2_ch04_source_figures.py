"""Recompute Chapter 4 diagram data, inversion workshop and degree factor."""

from collections import Counter
from fractions import Fraction
import math
from pathlib import Path
import re
import unittest

from tools.test_volume2_ch06_carmichael_pratt import factors

ROOT = Path(__file__).resolve().parents[1] / 'volume2-integers'


def mu(n):
    fs = factors(n)
    return 0 if any(e > 1 for e in fs.values()) else (-1)**len(fs)


def remainder_f2(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a


class ChapterFourSourceChecks(unittest.TestCase):
    def test_workshop_inversion_against_primitive_residue_pair_counts(self):
        values = {}
        for n in range(1, 51):
            inverted = sum(mu(d)*(n//d)**2 for d in range(1, n+1) if n % d == 0)
            direct = sum(math.gcd(math.gcd(a, b), n) == 1
                         for a in range(1, n+1) for b in range(1, n+1))
            self.assertEqual(inverted, direct)
            values[n] = inverted
            self.assertEqual(sum(values[d] for d in values if n % d == 0), n*n)
        self.assertEqual([values[n] for n in (1, 2, 3, 4, 6, 12)], [1, 3, 8, 12, 24, 96])

    def test_finite_field_preview_requires_division_by_degree(self):
        source = (ROOT/'chapters/ch04-arithmetic-functions.tex').read_text()
        self.assertRegex(source, r'dividing the primitive-word count[^.]*by \$n\$')
        for n in range(1, 7):
            count = 0
            for low in range(2**n):
                polynomial = (1 << n) | low
                reducible = any(remainder_f2(polynomial, (1 << d) | c) == 0
                                for d in range(1, n//2+1) for c in range(2**d))
                count += not reducible
            words = sum(mu(d)*2**(n//d) for d in range(1, n+1) if n % d == 0)
            self.assertEqual(n*count, words)
        # At degree2 there is one monic irreducible, but two primitive words.
        self.assertEqual(sum(mu(d)*2**(2//d) for d in (1, 2)), 2)

    def test_every_orchard_point_cross_and_sight_line(self):
        source = (ROOT/'figures/ch04-orchard.tex').read_text()
        filled = {(int(a), int(b)) for a, b in re.findall(
            r'\\fill \((\d+),(\d+)\) circle \(1.5pt\);', source)}
        crossed = set()
        for a, b, c, d in re.findall(
                r'\\draw\[gray\] \(([\d.]+),([\d.]+)\)--\(([\d.]+),([\d.]+)\)', source):
            x, y = (Fraction(a)+Fraction(c))/2, (Fraction(b)+Fraction(d))/2
            self.assertEqual((x.denominator, y.denominator), (1, 1))
            crossed.add((int(x), int(y)))
        expected = {(a, b) for a in range(1, 13) for b in range(1, 13) if math.gcd(a, b) == 1}
        self.assertEqual(filled, expected)
        self.assertEqual(crossed, {(a, b) for a in range(1, 13) for b in range(1, 13)}-expected)
        self.assertEqual((len(filled), len(crossed)), (91, 53))
        self.assertEqual(3*Fraction('8.4'), 2*Fraction('12.6'))
        self.assertEqual([(a, b) for a in range(1, 13) for b in range(1, 13) if 3*a == 2*b],
                         [(2, 3), (4, 6), (6, 9), (8, 12)])

    def test_every_divisor_grid_label(self):
        source = (ROOT/'figures/ch04-divisor-grid.tex').read_text()
        cells = re.findall(r'\\node at \(([\d.]+),([\d.]+)\) \{\$(\d+)\$\};', source)
        self.assertEqual(len(cells), 12)
        labels = []
        for x, y, n in cells:
            i, j = Fraction(x)-Fraction(1, 2), Fraction(5, 2)-Fraction(y)
            self.assertEqual((i.denominator, j.denominator), (1, 1))
            self.assertEqual(int(n), 2**int(i)*3**int(j))
            labels.append(int(n))
        self.assertEqual(set(labels), {d for d in range(1, 73) if 72 % d == 0})
        self.assertEqual(sum(labels), 195)

    def test_every_hyperbola_point_and_overlap_colour(self):
        source = (ROOT/'figures/ch04-hyperbola.tex').read_text()
        points = {(int(a), int(b)): colour for colour, a, b in re.findall(
            r'\\fill\[(MidnightBlue|ForestGreen|Orange)\] \((\d+),(\d+)\) circle \(4pt\);', source)}
        expected = {(a, b): ('MidnightBlue' if a <= 5 and b <= 5 else
                             'ForestGreen' if a <= 5 else 'Orange')
                    for a in range(1, 31) for b in range(1, 31) if a*b <= 30}
        self.assertEqual(points, expected)
        self.assertEqual(Counter(points.values()), {'MidnightBlue': 25, 'ForestGreen': 43, 'Orange': 43})
        self.assertEqual(sum(30//a for a in range(1, 6)), 68)
        self.assertEqual(2*68-25, len(points))
        self.assertLess(abs(Fraction('5.47723')**2-30), Fraction(1, 10000))

    def test_all_main_numeric_function_examples(self):
        divisors = lambda n: [d for d in range(1, n+1) if n % d == 0]
        self.assertEqual(divisors(12), [1, 2, 3, 4, 6, 12])
        self.assertEqual(sum(divisors(12)), 28)
        self.assertEqual((mu(12), mu(30), mu(1)), (0, -1, 1))
        self.assertEqual([mu(d) for d in divisors(12)], [1, -1, -1, 0, 1, 0])
        self.assertEqual(sum(mu(d)*len(divisors(12//d)) for d in divisors(12)), 1)
        self.assertEqual(sum(divisors(28)), 56)
        self.assertEqual(sum(divisors(90)), 234)
        self.assertEqual(sum(divisors(496)), 992)
        self.assertEqual(math.prod(e+1 for e in factors(720720).values()), 240)
        self.assertEqual([len(divisors(n)) for n in range(1, 11)], [1, 2, 2, 3, 2, 4, 2, 4, 3, 4])


if __name__ == '__main__':
    unittest.main()
