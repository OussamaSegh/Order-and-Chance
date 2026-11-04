"""Reconstruct every Chapter 7 diagram datum and surrounding numeric examples."""

from fractions import Fraction
import itertools
import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]/'volume2-integers'


def disc_points(radius):
    bound = math.floor(radius)
    return {(x, y) for x in range(-bound, bound+1) for y in range(-bound, bound+1)
            if x*x+y*y <= radius*radius}


class ChapterSevenSourceChecks(unittest.TestCase):
    def test_all_sixtyfive_points_labels_and_arc(self):
        source = (ROOT/'figures/ch07-sixtyfive.tex').read_text()
        data = {(int(x), int(y)) for x, y in re.findall(r'(\d+)/(\d+)', source.split('\\fill')[0])}
        expected = {(x, y) for x in range(1, 9) for y in range(1, 9) if x*x+y*y == 65}
        self.assertEqual(data, expected)
        labels = {(int(x), int(y)): (int(a), int(b)) for x, y, a, b in re.findall(
            r'at \((\d+),(\d+)\) \{\$\((\d+),(\d+)\)\$\}', source)}
        self.assertEqual(labels, {point: point for point in expected})
        reflected = {(s*x, t*y) for x, y in data for s in (-1, 1) for t in (-1, 1)}
        self.assertEqual(len(reflected), 16)
        self.assertEqual(reflected, {p for p in disc_points(9) if p[0]**2+p[1]**2 == 65})
        radius = Fraction(re.search(r'radius=([\d.]+)\]', source)[1])
        self.assertLess(abs(radius*radius-65), Fraction(1, 100000))

    def test_all_thirty_representability_cells(self):
        source = (ROOT/'figures/ch07-representable.tex').read_text()
        data = dict((int(n), int(ok)) for n, ok in re.findall(r'(\d+)/([01])', source.split('\\pgfmath')[0]))
        squares = {a*a+b*b for a in range(6) for b in range(6)}
        self.assertEqual(data, {n: int(n in squares) for n in range(1, 31)})
        self.assertEqual([n for n in range(1, 21) if data[n]], [1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20])

    def test_all_disc_square_anchors_points_and_radii(self):
        source = (ROOT/'figures/ch07-disc.tex').read_text()
        anchors = [(int(x), int(y)) for x, y in re.findall(
            r'\\fill\[MidnightBlue!12[^\]]*\] \((-?\d+),(-?\d+)\) rectangle \+\+\(1,1\)', source)]
        points = [(int(x), int(y)) for x, y in re.findall(
            r'\\fill\[MidnightBlue\] \((-?\d+),(-?\d+)\) circle', source)]
        expected = disc_points(6)
        self.assertEqual((len(anchors), len(points), len(expected)), (113, 113, 113))
        self.assertEqual(set(anchors), expected)
        self.assertEqual(set(points), expected)
        radii = [float(x) for x in re.findall(r'\\draw\[BrickRed[^\]]*\] \(0,0\) circle \(([\d.]+)\)', source)]
        for actual, expected_radius in zip(radii, (6, 6+math.sqrt(2), 6-math.sqrt(2))):
            self.assertAlmostEqual(actual, expected_radius, places=4)
        self.assertEqual(len(radii), 3)
        for x, y in anchors:
            for u, v in itertools.product((0, 1), repeat=2):
                self.assertLessEqual(math.hypot(x+u, y+v), 6+math.sqrt(2))
        # Separate coverage check for a grid inside the inner disc.
        for a, b in itertools.product(range(-45, 46), repeat=2):
            x, y = a/10, b/10
            if x*x+y*y < (6-math.sqrt(2))**2:
                self.assertIn((math.floor(x), math.floor(y)), set(anchors))

    def test_exact_descent_run_and_norm_division(self):
        a, b = (4, 2, 1, 0), (1, -1, 1, 0)
        self.assertEqual([x % 3 for x in a], [x % 3 for x in b])
        z = (sum(x*y for x, y in zip(a, b)),
             a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
             a[0]*b[2]-a[2]*b[0]+a[3]*b[1]-a[1]*b[3],
             a[0]*b[3]-a[3]*b[0]+a[1]*b[2]-a[2]*b[1])
        self.assertEqual(z, (3, -6, 3, 3))
        self.assertEqual(sum(x*x for x in z), 21*3)
        self.assertEqual(sum((x//3)**2 for x in z), 7)

    def test_new_product_and_all_small_numeric_counts(self):
        self.assertEqual((1*1-2*4)**2+(1*4+2*1)**2, 85)
        self.assertEqual((1*1+2*4)**2+(1*4-2*1)**2, 85)
        self.assertEqual({tuple(sorted((x, y))) for x in range(10) for y in range(10) if x*x+y*y == 85},
                         {(2, 9), (6, 7)})
        self.assertEqual([len(disc_points(r)) for r in (2, 6, 10)], [13, 113, 317])
        self.assertEqual(sum(x*x+y*y == 25 for x in range(-5, 6) for y in range(-5, 6)), 12)
        self.assertEqual(45**2+1, 2026)
        self.assertEqual(3**2+2**2+1+1, 15)
        self.assertEqual(7 % 8, 7)
        self.assertNotIn(7, {(a+b+c) % 8 for a, b, c in itertools.product((0, 1, 4), repeat=3)})
        self.assertGreater(math.sqrt(10), 3)
        self.assertAlmostEqual(4*math.sqrt(2)*math.pi+2*math.pi, 24.0547170598, places=8)

    def test_three_square_question_removes_factors_of_four(self):
        three_squares = {a*a+b*b+c*c for a, b, c in itertools.product(range(6), repeat=3)}
        missing = [n for n in range(1, 31) if n not in three_squares]
        self.assertEqual(missing, [7, 15, 23, 28])
        self.assertNotEqual(28 % 8, 7)
        for n in missing:
            while n % 4 == 0:
                n //= 4
            self.assertEqual(n % 8, 7)
        source = (ROOT/'chapters/ch07-sums-of-squares.tex').read_text()
        self.assertIn('After removing every factor of $4$', source)

    def test_withdrawn_preprint_is_not_evidence_for_a_bound(self):
        source = (ROOT/'chapters/ch07-sums-of-squares.tex').read_text()
        for withdrawn in ('1709.04340', '517/824', 'Bourgain and Watt', 'Bourgain and N.~Watt'):
            self.assertNotIn(withdrawn, source)
        self.assertIn("Huxley's published 2003 result", source)
        self.assertIn('historical benchmark', source)
        self.assertIn('131/208', source)


if __name__ == '__main__':
    unittest.main()
