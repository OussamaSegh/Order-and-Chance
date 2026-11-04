"""Recompute actual Chapter 5 diagrams and repaired worked examples."""

from collections import Counter
import cmath
import math
from pathlib import Path
import re
import unittest

from tools.test_volume2_ch05_orders import mobius, order

ROOT = Path(__file__).resolve().parents[1] / 'volume2-integers'
SOURCE = ROOT / 'chapters/ch05-primitive-roots.tex'


class ChapterFiveSourceChecks(unittest.TestCase):
    def test_order_histogram_uses_exact_orders_and_actual_tick_labels(self):
        source = (ROOT/'figures/ch05-orders.tex').read_text()
        labels = [int(x) for x in re.search(r'xticklabels=\{([^}]+)\}', source)[1]
                  .replace('$', '').split(',')]
        points = [(int(x), int(y)) for x, y in re.findall(r'\((\d+),(\d+)\)', source)]
        expected = Counter(order(a, 13) for a in range(1, 13))
        self.assertEqual(dict((labels[x-1], y) for x, y in points), dict(expected))
        self.assertEqual(sum(y for _, y in points), 12)

    def test_every_primitive_root_panel_label_arrow_and_highlight(self):
        source = (ROOT/'figures/ch05-primroot.tex').read_text()
        panels = re.findall(r'\\begin\{scope\}.*?\\end\{scope\}', source, re.S)
        self.assertEqual(len(panels), 2)
        for multiplier, panel in zip((2, 3), panels):
            nodes = re.findall(r'\\node\[([^\]]+)\] at \(([-\d.]+),([-\d.]+)\) \{(\d+)\};', panel)
            by_coord = {(float(x), float(y)): int(label) for _, x, y, label in nodes}
            self.assertEqual(len(by_coord), 12)
            self.assertEqual([int(label) for _, _, _, label in nodes], [pow(2, j, 13) for j in range(12)])
            shaded = {int(label) for style, _, _, label in nodes if 'Goldenrod!40' in style}
            self.assertEqual(shaded, {a for a in range(1, 13) if order(a, 13) == 12})
            arrows = re.findall(r'\(([-\d.]+),([-\d.]+)\)--\(([-\d.]+),([-\d.]+)\);', panel)
            self.assertEqual(len(arrows), 12)
            mapping = {}
            for x, y, u, v in arrows:
                a, b = by_coord[float(x), float(y)], by_coord[float(u), float(v)]
                self.assertEqual(a*multiplier % 13, b)
                mapping[a] = b
            unseen, lengths = set(mapping), []
            while unseen:
                a = start = min(unseen)
                length = 0
                while True:
                    unseen.remove(a)
                    length += 1
                    a = mapping[a]
                    if a == start:
                        break
                lengths.append(length)
            self.assertEqual(lengths, [12] if multiplier == 2 else [3]*4)

    def test_every_modulo_seven_cycle_edge(self):
        source = (ROOT/'figures/ch05-cycle.tex').read_text()
        nodes = dict((int(a), int(b)) for a, b in re.findall(r'([0-5])/([1-6])', source.split('\\foreach \\a')[0]))
        edges = [(int(a), int(b)) for a, b in re.findall(r'([0-5])/([0-5])', source.split('\\foreach \\a')[1])]
        self.assertEqual(nodes, dict(enumerate([1, 3, 2, 6, 4, 5])))
        self.assertEqual(edges, [(j, (j+1) % 6) for j in range(6)])
        self.assertTrue(all(nodes[b] == 3*nodes[a] % 7 for a, b in edges))

    def test_four_roots_change_representatives_with_modulus(self):
        text = SOURCE.read_text()
        self.assertNotIn('The same four roots survive', text)
        self.assertIn('$1,-1,2^{k-1}+1,2^{k-1}-1$', text)
        self.assertNotEqual(pow(3, 2, 16), 1)
        for k in range(3, 12):
            n = 2**k
            self.assertEqual({x for x in range(n) if x*x % n == 1},
                             {1, n-1, n//2+1, n//2-1})

    def test_equalities_do_not_replace_congruences(self):
        text = SOURCE.read_text()
        for wrong in ('5^8=(1+16)^2', '5^4=17', '9&=5^2', '2^4=3'):
            self.assertNotIn(wrong, text)
        self.assertEqual((pow(5, 4, 32), pow(5, 8, 32)), (17, 1))
        self.assertNotEqual(5**8, 17**2)
        self.assertEqual([pow(5, j, 16) for j in range(4)], [1, 5, 9, 13])

    def test_new_power_equation_and_generator_workshop(self):
        self.assertEqual([x for x in range(13) if pow(x, 5, 13) == 3], [9])
        self.assertEqual([u for u in range(12) if 5*u % 12 == 4], [8])
        self.assertEqual([pow(2, e, 29) for e in (4, 7, 14, 28)], [16, 12, 28, 1])
        self.assertEqual((order(2, 29), order(4, 29)), (28, 14))
        self.assertEqual([pow(4, e, 29) for e in (2, 7, 14)], [16, 28, 1])

    def test_ramanujan_sum_zero_signed_inputs_and_holder_formula(self):
        text = SOURCE.read_text().split(r'\begin{solution}{pb:ramsum}')[1].split(r'\end{solution}')[0]
        self.assertIn('If $n=0$', text)
        self.assertIn(r'v_p(|n|)', text)
        phi = lambda q: sum(math.gcd(a, q) == 1 for a in range(1, q+1))
        for q in range(1, 41):
            for n in range(-q, q+1):
                direct = sum(cmath.exp(2j*math.pi*a*n/q) for a in range(1, q+1) if math.gcd(a, q) == 1)
                divisor = sum(d*mobius(q//d) for d in range(1, q+1) if q % d == 0 and n % d == 0)
                reduced = q//math.gcd(q, n)
                holder = mobius(reduced)*phi(q)//phi(reduced)
                self.assertAlmostEqual(direct.real, divisor, places=9)
                self.assertAlmostEqual(direct.imag, 0, places=9)
                self.assertEqual(divisor, holder)


if __name__ == '__main__':
    unittest.main()
