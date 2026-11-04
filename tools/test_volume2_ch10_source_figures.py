"""Every plotted quadratic prime checked by exact trial factors, plus geometry."""

from fractions import Fraction as F
from itertools import product
import math
from pathlib import Path
import re
import unittest

from tools.test_volume2_ch10_euclidean import QuadraticRing

ROOT = Path(__file__).resolve().parents[1]/'volume2-integers'


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n)+1))


def exact_irreducibles(ring):
    # Norm<=225 forces |b|<=sqrt(300), |a|<=sqrt(300) in the
    # Eisenstein lattice, and <=15 in the Gaussian lattice.
    points = [z for z in product(range(-18, 19), repeat=2) if 1 < ring.norm(z) <= 225]
    # A reducible z has a nonunit factor of norm <=sqrt(N(z))<=15.
    factors = [z for z in product(range(-5, 6), repeat=2) if 1 < ring.norm(z) <= 15]
    answer = set()
    for z in points:
        nz = ring.norm(z)
        for d in factors:
            nd = ring.norm(d)
            if nd*nd > nz or nz % nd:
                continue
            numerator = ring.multiply(z, ring.conjugate(d))
            if all(a % nd == 0 for a in numerator):
                break
        else:
            answer.add(z)
    return answer


class ChapterTenSourceChecks(unittest.TestCase):
    def test_every_prime_plate_point_by_independent_trial_division(self):
        source = (ROOT/'figures/ch10-primes.tex').read_text()
        # Explicitly separate the two data scopes from the legend.
        blocks = re.findall(r'\\begin\{scope\}\[[^\]]+\](.*?)\\end\{scope\}', source, re.S)
        self.assertEqual(len(blocks), 3)
        for block, ring, eisenstein in zip(blocks, (QuadraticRing(-1), QuadraticRing(-1, -1)), (False, True)):
            data = re.findall(r'\\fill\[([^\]]+)\] \((-?[\d.]+),(-?[\d.]+)\) circle', block)
            actual = {}
            for color, sx, sy in data:
                x, y = float(sx), float(sy)
                b = round(2*y/math.sqrt(3)) if eisenstein else round(y)
                a = round(x+b/2) if eisenstein else round(x)
                self.assertLessEqual(abs(y-(math.sqrt(3)*b/2 if eisenstein else b)), .000501)
                self.assertLessEqual(abs(x-(a-b/2 if eisenstein else a)), .000501)
                self.assertNotIn((a, b), actual)
                actual[a, b] = color
            expected = exact_irreducibles(ring)
            self.assertEqual(set(actual), expected)
            for z, color in actual.items():
                n = ring.norm(z)
                if n == (3 if eisenstein else 2):
                    self.assertEqual(color, 'ForestGreen')
                elif is_prime(n):
                    self.assertEqual(n % (3 if eisenstein else 4), 1)
                    self.assertEqual(color, 'MidnightBlue')
                else:
                    q = math.isqrt(n)
                    self.assertEqual(q*q, n)
                    self.assertTrue(is_prime(q))
                    self.assertEqual(q % (3 if eisenstein else 4), 2 if eisenstein else 3)
                    self.assertEqual(color, 'BrickRed')
            units = [z for z in product(range(-1, 2), repeat=2) if ring.norm(z) == 1]
            self.assertEqual({ring.multiply(z, u) for z in expected for u in units}, expected)

    def test_rounding_point_cell_and_every_division_certificate(self):
        a, b = (11, 3), (1, 8)
        r = QuadraticRing(-1)
        num = r.multiply(a, r.conjugate(b))
        self.assertEqual(tuple(F(c, r.norm(b)) for c in num), (F(7, 13), -F(17, 13)))
        delta = F(7, 13)-1, -F(17, 13)+1
        self.assertEqual(sum(c*c for c in delta), F(4, 13))
        self.assertTrue(all(abs(c) < F(1, 2) for c in delta))
        steps = [(a, b, (1, -1), (2, -4)), (b, (2, -4), (-1, 1), (-1, 2)),
                 ((2, -4), (-1, 2), (-2, 0), (0, 0))]
        for aa, bb, q, remainder in steps:
            p = r.multiply(bb, q)
            self.assertEqual(tuple(x+y for x, y in zip(p, remainder)), aa)
            self.assertLess(r.norm(remainder), r.norm(bb))
        source = (ROOT/'figures/ch10-rounding.tex').read_text()
        self.assertIn('(.5,-1.5) rectangle (1.5,-.5)', source)
        self.assertIn('(7/13,-17/13)--(1,-1)', source)
        self.assertEqual(sum(F(1, 2)**2 for _ in range(2)), F(1, 2))

    def test_eisenstein_division_and_bezout_certificate(self):
        r = QuadraticRing(-1, -1)
        a, b = (5, 2), (2, -1)
        self.assertEqual(r.multiply(a, r.conjugate(b)), (13, 9))
        q, rem = r.divide(a, b)
        self.assertEqual((q, rem), ((2, 1), (0, 1)))
        self.assertEqual(r.norm(b), 7)
        terms = [r.multiply((-1, -1), a), r.multiply((1, 2), b)]
        self.assertEqual(tuple(sum(xs) for xs in zip(*terms)), (1, 0))
        # The coefficient-square estimate is a convex quadratic on a box;
        # its maximum occurs at a corner and is 3/4 (not a nearest-point claim).
        corners = [F(x*x-x*y+y*y, 4) for x, y in product((-1, 1), repeat=2)]
        self.assertEqual(max(corners), F(3, 4))

    def test_ramified_arrow_has_the_correct_vector_not_unit_length(self):
        source = (ROOT/'figures/ch10-eisenstein.tex').read_text()
        m = re.search(r'\\draw\[ocCoralDeep,dashed,->\] \(([-\d.]+),([-\d.]+)\)--\(([-\d.]+),([-\d.]+)\);', source)
        self.assertIsNotNone(m)
        x0, y0, x1, y1 = map(float, m.groups())
        self.assertEqual((x0, x1, y1), (-.5, 1, 0))
        self.assertLess(abs(y0-math.sqrt(3)/2), .00003)
        self.assertLess(abs((x1-x0)**2+(y1-y0)**2-3), .00005)
        self.assertIn('\\m in {-1,0,1,2}', source)
        self.assertIn('\\n in {-1,0,1,2}', source)
        self.assertEqual(len({(2*m-n, n) for m, n in product(range(-1, 3), repeat=2)}), 16)

    def test_coprime_without_bezout_obstruction(self):
        self.assertEqual(math.gcd(4, 6), 2)
        self.assertFalse(any(a*a+5*b*b == 2 for a, b in product(range(-2, 3), repeat=2)))
        # Exact parity truth table for the coefficient comparison: no
        # solution mod2 exists, hence no integer coefficients can exist.
        self.assertFalse(any((2*a+c-5*d) % 2 == 1 and (2*b+c+d) % 2 == 0
                             for a, b, c, d in product(range(2), repeat=4)))
        source = (ROOT/'chapters/ch10-gaussian-eisenstein.tex').read_text()
        self.assertIn('coprime without a B', source)
        self.assertNotIn('has nothing to divide by', source)
        self.assertNotIn('It is still an open problem', source)

    def test_workshop_factor_lists_and_representation_counts(self):
        r = QuadraticRing(-1)
        self.assertEqual(r.multiply((2, -1), (3, 2)), (8, 1))
        self.assertEqual(r.multiply((2, 1), (3, 2)), (4, 7))
        self.assertEqual(r.norm((8, 1)), r.norm((4, 7)))
        units = ((1, 0), (-1, 0), (0, 1), (0, -1))
        self.assertNotIn((4, 7), {r.multiply((8, 1), u) for u in units})
        for n, expected in ((15, 0), (45, 8), (65, 16), (325, 24)):
            self.assertEqual(sum(a*a+b*b == n for a, b in product(range(-math.isqrt(n), math.isqrt(n)+1), repeat=2)), expected)
        self.assertTrue(is_prime(1013))
        self.assertEqual([p for p in range(2, 32) if is_prime(p)], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])


if __name__ == '__main__':
    unittest.main()
