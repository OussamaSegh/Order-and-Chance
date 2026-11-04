"""Recalculate Chapter 1 figure data and the rational-valuation first-use repair."""

from fractions import Fraction
import itertools
import math
from pathlib import Path
import re
import unittest

from tools.test_volume2_ch06_carmichael_pratt import factors

ROOT = Path(__file__).resolve().parents[1] / 'volume2-integers'


class ChapterOneSourceChecks(unittest.TestCase):
    def test_rational_valuation_is_defined_before_use(self):
        text = (ROOT/'chapters/ch01-divisibility.tex').read_text()
        definition = text.index('v_p(a/b)=v_p(a)-v_p(b)')
        self.assertLess(definition, text.index(r'\begin{exercise}[$\star\star\star$]\label{ex:supercat}'))
        for a in range(-30, 31):
            if not a:
                continue
            for b in range(1, 31):
                x = Fraction(a, b)
                for p in (2, 3, 5, 7):
                    v = factors(abs(a)).get(p, 0)-factors(b).get(p, 0)
                    reduced = factors(abs(x.numerator)).get(p, 0)-factors(x.denominator).get(p, 0)
                    self.assertEqual(v, reduced)
                fs = set(factors(abs(a))) | set(factors(b))
                self.assertEqual(all(factors(abs(a)).get(p, 0) >= factors(b).get(p, 0) for p in fs),
                                 x.denominator == 1)

    def test_divisor_lattice_edges_are_exact_cover_relations(self):
        text = (ROOT/'figures/ch01-divisor-lattice.tex').read_text()
        nodes = {int(n) for n in re.findall(r'\\node\[lat\] \((\d+)\)', text)}
        self.assertEqual(nodes, {n for n in range(1, 13) if 12 % n == 0})
        edges = {(int(a), int(b)) for a, b in re.findall(r'\((\d+)\)--\((\d+)\)', text)}
        covers = {(a, b) for a in nodes for b in nodes if b > a and b % a == 0
                  and not any(a < c < b and c % a == 0 and b % c == 0 for c in nodes)}
        self.assertEqual(edges, covers)

    def test_bezout_points_line_and_displacement(self):
        text = (ROOT/'figures/ch01-bezout-line.tex').read_text()
        for x, y in ((-3, 2), (2, -1), (7, -4), (1, Fraction(-2, 5))):
            self.assertEqual(3*x+5*y, 1)
        for x, y in ((-4, Fraction('2.6')), (8, Fraction('-4.6'))):
            self.assertEqual(3*x+5*y, 1)
        match = re.search(r'\\draw\[->,dashed,thick\] \(([-\d.]+),([-\d.]+)\)--\(([-\d.]+),([-\d.]+)\)', text)
        x1, y1, x2, y2 = map(Fraction, match.groups())
        self.assertEqual((x2-x1, y2-y1), (5, -3))

    def test_euclidean_square_tilings_cover_rectangles(self):
        text = (ROOT/'figures/ch01-euclid.tex').read_text()
        squares = [tuple(map(Fraction, values)) for values in re.findall(
            r'\\filldraw\[[^\]]+\] \(([-\d.]+),([-\d.]+)\) rectangle \+\+\(([-\d.]+),([-\d.]+)\)', text)]
        self.assertEqual(len(squares), 18)
        scale = Fraction(17, 100)
        for left, width, height in ((Fraction(0), 34*scale, 21*scale),
                                    (Fraction('6.6'), 45*scale, 16*scale)):
            group = [sq for sq in squares if left <= sq[0] < left+width]
            self.assertEqual(sum(w*h for x, y, w, h in group), width*height)
            for x, y, w, h in group:
                self.assertEqual(w, h)
                self.assertEqual((w/scale).denominator, 1)
                self.assertTrue(left <= x < x+w <= left+width)
                self.assertTrue(0 <= y < y+h <= height)
            for (x, y, w, h), (X, Y, W, H) in itertools.combinations(group, 2):
                self.assertTrue(x+w <= X or X+W <= x or y+h <= Y or Y+H <= y)

    def test_orchard_plot_matches_every_lattice_point_and_gcd(self):
        text = (ROOT/'figures/ch06-visible.tex').read_text()
        plotted = {(int(a), int(b)): command == 'fill' for command, a, b in re.findall(
            r'\\(draw|fill)\[[^\]]*\] \((-?\d+),(-?\d+)\) circle\[radius=3.2pt\]', text)}
        expected = {(a, b): math.gcd(a, b) == 1 for a in range(-11, 12) for b in range(-11, 12)
                    if 0 < a*a+b*b <= 121}
        self.assertEqual(plotted, expected)
        self.assertEqual((len(plotted), sum(plotted.values())), (376, 224))
        self.assertTrue(all(4*a-11*b != 0 for a, b in plotted))


if __name__ == '__main__':
    unittest.main()
