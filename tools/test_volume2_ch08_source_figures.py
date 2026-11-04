"""Recompute printed Chapter 8's geometry, tree, domains and fresh descent."""

from fractions import Fraction
import itertools
import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]/'volume2-integers'
SOURCE = ROOT/'chapters/ch09-diophantine.tex'


def markov_neighbors(triple):
    return {tuple(sorted([triple[j] for j in range(3) if j != i]+
                         [3*math.prod(triple[j] for j in range(3) if j != i)-triple[i]]))
            for i in range(3)}


class ChapterEightSourceChecks(unittest.TestCase):
    def test_all_incircle_contacts_lengths_and_right_angles(self):
        source = (ROOT/'figures/ch09-triangle-incircle.tex').read_text()
        x, y, radius = re.search(r'\\draw\[thick\] \(([\d.]+),([\d.]+)\) circle\[radius=([\d.]+)\]', source).groups()
        centre = (Fraction(x), Fraction(y))
        self.assertEqual(centre, (1, 1))
        self.assertEqual(Fraction(radius), 1)
        contacts = [(Fraction(x), Fraction(y)) for x, y in re.findall(
            r'\\draw\[dashed\] \(1,1\)--\(([\d.]+),([\d.]+)\)', source)]
        self.assertEqual(contacts, [(1, 0), (0, 1), (Fraction(8, 5), Fraction(9, 5))])
        for x, y in contacts:
            self.assertEqual((x-1)**2+(y-1)**2, 1)
        x, y = contacts[-1]
        self.assertEqual(3*x+4*y, 12)  # Contact is on the sloping side.
        self.assertEqual(-4*(x-1)+3*(y-1), 0)  # Perpendicular to that side.
        self.assertEqual(4*3/2, (3+4+5)/2)  # Area and semiperimeter are both6.
        self.assertEqual(sorted(int(x) for x in re.findall(r'\{\$(\d+)\$\};', source)), [3, 4, 5])

    def test_every_chord_endpoint_label_and_slope(self):
        source = (ROOT/'figures/ch09-chord-markov.tex').read_text().split(r'\end{scope}')[0]
        labels = re.findall(r'\$t=\\frac\{(-?\d+)\}\{(\d+)\}\\colon\\ \\left\(\\frac\{(-?\d+)\}\{(\d+)\},\\frac\{(-?\d+)\}\{(\d+)\}\\right\)\$', source)
        endpoints = [(Fraction(x), Fraction(y)) for x, y in re.findall(
            r'\\draw\[(?:MidnightBlue|ForestGreen|BrickRed|Plum),[^\]]*\] \(-1,0\)--\(([-\d.]+),([-\d.]+)\)', source)]
        self.assertEqual((len(labels), len(endpoints)), (4, 4))
        self.assertEqual([Fraction(a, b) for a, b, *_ in ([int(t) for t in row] for row in labels)],
                         [Fraction(1, 4), Fraction(1, 2), Fraction(2, 3), Fraction(3, 2)])
        for row, point in zip(labels, endpoints):
            a, b, c, d, e, f = map(int, row)
            t, x, y = Fraction(a, b), Fraction(c, d), Fraction(e, f)
            self.assertEqual(x*x+y*y, 1)
            self.assertEqual(y, t*(x+1))
            self.assertEqual((x, y), ((1-t*t)/(1+t*t), 2*t/(1+t*t)))
            self.assertLessEqual(abs(point[0]-x), Fraction(1, 20000))
            self.assertLessEqual(abs(point[1]-y), Fraction(1, 20000))

    def test_every_markov_node_edge_and_complete_first_four_levels(self):
        source = (ROOT/'figures/ch09-chord-markov.tex').read_text().split(r'\end{scope}')[1]
        nodes = {key: tuple(map(int, (a, b, c))) for key, a, b, c in re.findall(
            r'\\node \((\w+)\) at \([^)]*\) \{\$\((\d+),(\d+),(\d+)\)\$\}', source)}
        self.assertEqual(len(nodes), 9)
        edges = []
        for draw in re.findall(r'\\draw ([^;]+);', source):
            chain = re.findall(r'\((\w+)\)', draw)
            edges += list(zip(chain, chain[1:]))
        self.assertEqual(len(edges), 8)
        for parent, child in edges:
            self.assertIn(nodes[child], markov_neighbors(nodes[parent]))
            self.assertGreater(sum(nodes[child]), sum(nodes[parent]))
        reached = frontier = {(1, 1, 1)}
        for _ in range(4):
            next_level = set().union(*(markov_neighbors(t) for t in frontier))-reached
            reached = reached | next_level
            frontier = next_level
        self.assertEqual(set(nodes.values()), reached)
        for a, b, c in nodes.values():
            self.assertEqual(a*a+b*b+c*c, 3*a*b*c)

    def test_descent_plate_and_correct_twice_square_condition(self):
        source = (ROOT/'figures/ch09-descent.tex').read_text()
        self.assertIn(r'$x^4+y^4=z^2$', source)
        self.assertIn(r'$m>n>0$', source)
        self.assertIn(r'$x_1^4+y_1^4=z_1^2$', source)
        self.assertIn(r'$0<z_1<z$', source)
        self.assertEqual(re.findall(r'\((top|mid|bot)\)--\((top|mid|bot)\)', source), [('top', 'mid'), ('mid', 'bot')])
        text = SOURCE.read_text()
        self.assertNotIn('require $m$ and $n$ to be squares', text)
        self.assertIn('$m$ to be a square and $n$ twice a square', text)
        # Twice a square is not itself a square for nonzero inputs.
        for u, v in itertools.product(range(1, 20), repeat=2):
            n = 2*u*u*v*v
            self.assertNotEqual(math.isqrt(n)**2, n)

    def test_fresh_seven_descent_and_epigraph_domain(self):
        squares = {x*x % 7 for x in range(7)}
        self.assertEqual(squares, {0, 1, 2, 4})
        self.assertEqual([(a, b) for a, b in itertools.product(squares, repeat=2) if (a+b) % 7 == 0], [(0, 0)])
        text = SOURCE.read_text()
        self.assertIn('$x^4+y^4=z^4$ has no solution in positive integers', text)
        self.assertIn('The only integer solution of $x^2+y^2=7z^2$', text)
        self.assertIn('$|z|/7<|z|$', text)
        self.assertEqual(0**4+1**4, 1**4)  # Counterexample when zero is allowed.

    def test_factorization_and_unit_circle_second_chart(self):
        direct = {(x, y) for x in range(1, 46) for y in range(x) if x*x-y*y == 45}
        self.assertEqual(direct, {(23, 22), (9, 6), (7, 2)})
        for denominator in range(1, 11):
            for numerator in range(-20, 21):
                t = Fraction(numerator, denominator)
                x, y = (t*t-1)/(t*t+1), -2*t/(t*t+1)
                self.assertEqual(x*x+y*y, 1)
                self.assertEqual(y, t*(x-1))
        self.assertEqual(((2**2-1)/5, -2*2/5), (3/5, -4/5))
        self.assertIn('The sign is fixed by the chosen line equation', SOURCE.read_text())

    def test_integer_negative_root_obstruction_needs_no_upper_k_bound(self):
        # With h>=1, f(-h)=h²+b²+k(bh-1)>0 for every positive k,b.
        for h, b, k in itertools.product(range(1, 12), range(1, 12), (1, 2, 3, 10, 1000)):
            self.assertGreater(h*h+b*b+k*(b*h-1), 0)
        text = SOURCE.read_text().split(r'\begin{solution}{ex:imo88}')[1].split(r'\end{solution}')[0]
        self.assertNotIn('invalid without a bound on $k$', text)
        self.assertIn(r'f(-1)=b^2+1+k(b-1)>0', text)


if __name__ == '__main__':
    unittest.main()
