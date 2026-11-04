"""Complete continued-fraction figure data and corrected Pell-ring scope."""

from fractions import Fraction
import math
from pathlib import Path
import re
import unittest

import mpmath as mp

from tools.test_volume2_ch09_cf_foundations import convergents, evaluate
from tools.test_volume2_ch09_periodic_pell import sqrt_digits

ROOT = Path(__file__).resolve().parents[1]/'volume2-integers'
SOURCE = ROOT/'chapters/ch08-continued-fractions.tex'


class ChapterNineSourceChecks(unittest.TestCase):
    def test_all_five_line_positions_and_below_above_classifications(self):
        source = (ROOT/'figures/ch08-cf-line.tex').read_text()
        positions = {key: Fraction(int(a), int(b)) for key, a, b in re.findall(
            r'\\pgfmathsetmacro\{\\([a-e])\}\{\((\d+)/(\d+)-\\L\)/\\X\}', source)}
        self.assertEqual(positions, dict(zip('abcde', [Fraction(7, 5), Fraction(41, 29),
                                                                   Fraction(3, 2), Fraction(17, 12), Fraction(99, 70)])))
        filled = set(re.findall(r'\\fill\[ocBlue\] \(\\([a-e]),0\)', source))
        opened = set(re.findall(r'\\draw\[ocCoralDeep,thick\] \(\\([a-e]),0\)', source))
        self.assertEqual(filled, {key for key, v in positions.items() if v*v < 2})
        self.assertEqual(opened, set(positions)-filled)
        self.assertTrue(all(Fraction('1.28') < x < Fraction('1.62') for x in positions.values()))
        self.assertLess(Fraction(1), Fraction('1.28'))
        with mp.workdps(40):
            self.assertLess(abs(mp.mpf('1.41421356237')-mp.sqrt(2)), mp.mpf('4e-12'))

    def test_every_quality_plot_coordinate_at_high_precision(self):
        source = (ROOT/'figures/ch08-quality.tex').read_text()
        blocks = re.findall(r'coordinates \{([^}]+)\}', source)
        self.assertEqual(len(blocks), 4)
        with mp.workdps(100):
            targets = [(1+mp.sqrt(5))/2, mp.sqrt(2), mp.e, mp.pi]
            for x, block in zip(targets, blocks):
                t, digits = x, []
                for _ in range(11):
                    a = int(mp.floor(t))
                    digits.append(a)
                    t = 1/(t-a)
                points = [(int(n), mp.mpf(y)) for n, y in re.findall(r'\((\d+),([\d.]+)\)', block)]
                self.assertEqual([n for n, _ in points], list(range(1, 11)))
                for (n, y), (p, q) in zip(points, convergents(digits)[1:]):
                    exact = q*q*abs(x-mp.mpf(p)/q)
                    self.assertLessEqual(abs(y-exact), mp.mpf('0.0000005'), (x, n))
            self.assertLess(abs(mp.mpf('0.4472136')-1/mp.sqrt(5)), mp.mpf('1e-8'))

    def test_lattice_points_line_and_shortened_distance_arrow(self):
        source = (ROOT/'figures/ch08-lattice-errors.tex').read_text()
        filled = {(int(x), int(y)) for x, y in re.findall(r'\\fill \((\d+),(\d+)\) circle', source)}
        opened = {(int(x), int(y)) for x, y in re.findall(r'\\draw\[thick,fill=white\] \((\d+),(\d+)\) circle', source)}
        self.assertEqual(filled, {(1, 1), (5, 7)})
        self.assertEqual(opened, {(2, 3)})
        self.assertTrue(all(p*p < 2*q*q for q, p in filled))
        self.assertTrue(all(p*p > 2*q*q for q, p in opened))
        with mp.workdps(40):
            self.assertLess(abs(mp.mpf('8.9095')-mp.mpf('6.3')*mp.sqrt(2)), mp.mpf('0.00005'))
            # The arrow leaves .04 units clear at each end for the marker/line.
            self.assertLess(abs((mp.mpf('5.61685')-mp.mpf('5.04')+mp.mpf('.08'))-
                                (4*mp.sqrt(2)-5)), mp.mpf('0.000005'))

    def test_quality_data_against_independent_exact_rational_enclosures(self):
        def arctan_interval(denominator):
            # Eighty terms end negative; the next positive term bounds the tail.
            total = sum((Fraction((-1)**k, (2*k+1)*denominator**(2*k+1)) for k in range(80)), Fraction(0))
            return total, total+Fraction(1, 161*denominator**161)
        a, b = arctan_interval(5), arctan_interval(239)
        pi_bounds = 16*a[0]-4*b[1], 16*a[1]-4*b[0]  # Machin's identity.
        e_lower = sum((Fraction(1, math.factorial(k)) for k in range(101)), Fraction(0))
        e_bounds = e_lower, e_lower+Fraction(2, math.factorial(101))
        scale = 10**80
        def root_bounds(d):
            root_floor = math.isqrt(d*scale*scale)
            return Fraction(root_floor, scale), Fraction(root_floor+1, scale)
        root5 = root_bounds(5)
        phi_bounds = (1+root5[0])/2, (1+root5[1])/2
        blocks = re.findall(r'coordinates \{([^}]+)\}', (ROOT/'figures/ch08-quality.tex').read_text())
        for (low, high), block in zip((phi_bounds, root_bounds(2), e_bounds, pi_bounds), blocks):
            lower_tail, upper_tail, digits = low, high, []
            for _ in range(11):
                a = lower_tail.numerator//lower_tail.denominator
                self.assertEqual(a, upper_tail.numerator//upper_tail.denominator)
                digits.append(a)
                lower_tail, upper_tail = 1/(upper_tail-a), 1/(lower_tail-a)
            points = [(int(n), Fraction(y)) for n, y in re.findall(r'\((\d+),([\d.]+)\)', block)]
            for (_, y), (p, q) in zip(points, convergents(digits)[1:]):
                rational = Fraction(p, q)
                self.assertFalse(low <= rational <= high)
                endpoints = [q*q*abs(low-rational), q*q*abs(high-rational)]
                self.assertGreaterEqual(min(endpoints), y-Fraction(1, 2_000_000))
                self.assertLessEqual(max(endpoints), y+Fraction(1, 2_000_000))

    def test_pell_plate_only_draws_nonnegative_y(self):
        source = (ROOT/'figures/ch08-pell.tex').read_text()
        points = {(int(x), int(y)) for x, y in re.findall(r'\\fill\[ocCoralDeep\] \((\d+),(\d+)\)', source)}
        self.assertEqual(points, {(1, 0), (3, 2)})
        self.assertTrue(all(x*x-2*y*y == 1 for x, y in points))
        self.assertIn('sqrt((\\x*\\x-1)/2)', source)
        self.assertIn('The part $x\\ge1$, $y\\ge0$', SOURCE.read_text())
        self.assertEqual(3**2-2*(-2)**2, 1)  # The omitted lower half is real too.

    def test_full_ring_counterexample_and_pell_convergent_candidates(self):
        def product(u, v, d):
            return u[0]*v[0]+d*u[1]*v[1], u[0]*v[1]+u[1]*v[0]
        phi = (Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(product(phi, (Fraction(-1, 2), Fraction(1, 2)), 5), (1, 0))
        phi2 = product(phi, phi, 5)
        self.assertEqual(phi2, (Fraction(3, 2), Fraction(1, 2)))
        power = (1, 0)
        for _ in range(6):
            power = product(power, phi, 5)
        self.assertEqual(power, (9, 4))
        self.assertEqual([y for y in range(1, 5) if math.isqrt(1+5*y*y)**2 == 1+5*y*y], [4])
        for d, fundamental in ((2, (3, 2)), (3, (2, 1)), (5, (9, 4)), (7, (8, 3)),
                                (61, (1766319049, 226153980))):
            prefix, period = sqrt_digits(d)
            candidates = convergents(prefix+period*14)
            norm_one = [(p, q) for p, q in candidates if p*p-d*q*q == 1]
            self.assertEqual(norm_one[0], fundamental)
            power = (1, 0)
            for _ in range(3):
                power = product(power, fundamental, d)
                self.assertIn(power, candidates)
                x, y = power
                self.assertGreater(4*y*(x-y), 1)  # Exact Legendre-error comparison.
        text = SOURCE.read_text()
        self.assertNotIn('fundamental unit, or its square', text)
        self.assertIn(r'$9+4\sqrt5=\varphi^6$', text)
        self.assertIn(r'$q_0=q_1=1$', text)
        self.assertLess(text.index(r'A \emph{unit} is an element'), text.index('associated unit'))

    def test_complete_fixed_decimal_and_negative_workshop(self):
        value, digits = Fraction(24219, 100000), []
        while True:
            a = value.numerator//value.denominator
            digits.append(a)
            value -= a
            if not value:
                break
            value = 1/value
        self.assertEqual(digits, [0, 4, 7, 1, 3, 24, 6, 2, 2])
        self.assertEqual(evaluate(digits), Fraction(24219, 100000))
        self.assertEqual(Fraction(24219, 100000)-Fraction(31, 128), Fraction(1, 400000))
        negative = [-3, 1, 2, 1, 4]
        self.assertEqual(evaluate(negative), Fraction(-43, 19))
        self.assertEqual(convergents(negative), [(-3, 1), (-2, 1), (-7, 3), (-9, 4), (-43, 19)])
        self.assertEqual(-9*19-(-43)*4, 1)
        self.assertEqual(Fraction(-9, 4)-Fraction(-43, 19), Fraction(1, 76))

    def test_bounded_denominator_pi_comparison(self):
        with mp.workdps(50):
            for limit, answer in ((7, (22, 7)), (10, (22, 7)), (100, (311, 99))):
                best = min(((int(mp.nint(q*mp.pi)), q) for q in range(1, limit+1)),
                           key=lambda pair: abs(mp.pi-mp.mpf(pair[0])/pair[1]))
                self.assertEqual(best, answer)
            self.assertGreater(abs(99*mp.pi-311), abs(7*mp.pi-22))


if __name__ == '__main__':
    unittest.main()
