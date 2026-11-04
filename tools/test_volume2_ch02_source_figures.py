"""Recompute all Chapter 2 plotted data and catch first-use/discovery defects."""

import bisect
from fractions import Fraction
import math
from pathlib import Path
import re
import unittest

from tools.test_volume2_ch06_carmichael_pratt import prime

ROOT = Path(__file__).resolve().parents[1] / 'volume2-integers'


def logarithmic_integral(x):
    # Substitution t=exp(u) gives a smooth integrand away from the pole at0.
    f = lambda u: math.exp(u)/u
    a, b = math.log(2), math.log(x)
    if a == b:
        return 0.0
    def integrate(a, b, fa, fm, fb, whole, tolerance, depth):
        m = (a+b)/2
        fl, fr = f((a+m)/2), f((m+b)/2)
        left = (m-a)*(fa+4*fl+fm)/6
        right = (b-m)*(fm+4*fr+fb)/6
        error = left+right-whole
        if depth == 0 or abs(error) <= 15*tolerance:
            return left+right+error/15
        return (integrate(a, m, fa, fl, fm, left, tolerance/2, depth-1)
                + integrate(m, b, fm, fr, fb, right, tolerance/2, depth-1))
    fa, fm, fb = f(a), f((a+b)/2), f(b)
    return integrate(a, b, fa, fm, fb, (b-a)*(fa+4*fm+fb)/6, 1e-8, 20)


class ChapterTwoSourceChecks(unittest.TestCase):
    def test_fermat_discovery_uses_product_not_false_difference(self):
        source = (ROOT/'chapters/ch02-primes.tex').read_text()
        idea = source.split(r'\begin{solution}{ex:fermatnum}', 1)[1].split(r'\writeup', 1)[0]
        self.assertNotIn('their difference, which is a power', idea)
        self.assertIn(r'\mathcal F_n-2', idea)
        numbers = [2**(2**k)+1 for k in range(7)]
        self.assertEqual(numbers[2]-numbers[1], 12)  # A concrete counterexample to the old note.
        for n, value in enumerate(numbers):
            self.assertEqual(math.prod(numbers[:n]), value-2)
            for old in numbers[:n]:
                self.assertEqual(math.gcd(old, value), 1)
        self.assertIn(r'A set is \emph{closed} when its complement is open.', source)
        self.assertIn(r'A positive integer is \emph{squarefree}', source)

    def test_sieve_marks_every_composite_at_its_first_stage(self):
        text = (ROOT/'figures/ch02-sieve.tex').read_text()
        nodes = list(re.finditer(r'\\node at \([^)]+\) \{\$ (\d+) \$\};', text))
        self.assertEqual([int(m.group(1)) for m in nodes], list(range(2, 51)))
        for i, m in enumerate(nodes):
            n = int(m.group(1))
            body = text[m.end():nodes[i+1].start() if i+1 < len(nodes) else len(text)]
            stage = (2 if r'\draw[gray,thick]' in body else
                     3 if r'\draw[black,thick]' in body else
                     5 if 'rectangle' in body else 7 if '--cycle' in body else None)
            expected = next((p for p in (2, 3, 5, 7) if p < n and n % p == 0), None)
            self.assertEqual(stage, expected, n)
            self.assertEqual(stage is None, prime(n), n)

    def test_both_mod4_lanes_exhaust_the_odd_primes(self):
        text = (ROOT/'figures/ch02-mod4-line.tex').read_text()
        lists = re.findall(r'\\foreach \\p in \{([^}]+)\}', text)
        self.assertEqual(len(lists), 2)
        for residues, r in zip(lists, (1, 3)):
            self.assertEqual(list(map(int, residues.split(','))),
                             [p for p in range(3, 61) if prime(p) and p % 4 == r])

    def test_every_primecount_curve_coordinate(self):
        text = (ROOT/'figures/ch02-primecount.tex').read_text()
        plots = re.findall(r'\\addplot\[[^\]]+\] coordinates \{([^}]+)\}', text)
        self.assertEqual(len(plots), 5)
        curves = [[tuple(map(float, pair)) for pair in re.findall(r'\(([-\d.]+),([-\d.]+)\)', plot)]
                  for plot in plots]
        # Trial division independently supplies counts, rather than the plot's original sieve.
        primes = [n for n in range(2, 100001) if prime(n)]
        count = lambda x: bisect.bisect_right(primes, x)
        staircase = [(0., 0.)]
        for j, p in enumerate(primes[:25]):
            staircase += [(float(p), float(j)), (float(p), float(j+1))]
        staircase += [(100., 25.)]
        self.assertEqual(curves[0], staircase)
        for x, y in curves[1]:
            self.assertAlmostEqual(y, x/math.log(x), delta=0.000501)
        for x, y in curves[2]:
            self.assertAlmostEqual(y, logarithmic_integral(x), delta=0.000501)
        self.assertEqual(curves[3][-1][0], 100000)
        self.assertEqual(curves[4][-1][0], 100000)
        for x, y in curves[3]:
            self.assertAlmostEqual(y, count(x)*math.log(x)/x, delta=0.000051)
        for x, y in curves[4]:
            self.assertAlmostEqual(y, count(x)/logarithmic_integral(x), delta=0.000051)
        self.assertEqual(count(100000), 9592)
        self.assertAlmostEqual(count(100000)*math.log(100000)/100000, 1.104, delta=0.0005)
        self.assertAlmostEqual(count(100000)/logarithmic_integral(100000), 0.996, delta=0.0005)

    def test_examples_binomial_factors_and_finite_prime_chain(self):
        self.assertEqual(Fraction(1, 2)+Fraction(1, 3)+Fraction(1, 5)+Fraction(1, 7), Fraction(247, 210))
        self.assertEqual(math.comb(20, 10), 4*11*13*17*19)
        self.assertEqual(math.comb(12, 6), 924)
        self.assertEqual(math.prod((2, 3, 5, 7, 11)), 2310)
        self.assertEqual(4**11, 4194304)
        chain = [2, 3, 5, 7, 11, 13, 19, 23]
        for n in range(1, 21):
            self.assertTrue(any(n < p <= 2*n and prime(p) for p in chain))


if __name__ == '__main__':
    unittest.main()
