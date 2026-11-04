"""Independent Chapter 3 figure/first-use and repaired-solution checks."""

import math
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'volume2-integers'


class ChapterThreeSourceChecks(unittest.TestCase):
    def test_field_and_fraction_conventions_precede_first_use(self):
        source = (ROOT/'chapters/ch03-congruences.tex').read_text()
        definition = source.index(r'\mathbb F_p=\Z/p\Z')
        self.assertEqual(definition, source.index(r'\mathbb F_p'))
        self.assertLess(source.index(r'the notation $a/b$ means'), source.index(r'\label{pb:wolsten}'))
        self.assertIn(r'For $n\ge2$, the nonzero classes', source)
        korselt = source.split(r'\label{ex:korselt}', 1)[1].split(r'\end{exercise}', 1)[0]
        self.assertIn(r'called a \emph{Carmichael number}', korselt)
        self.assertNotIn('Volume~1', korselt)
        for n in range(1, 31):
            for b in range(1, 21):
                if math.gcd(b, n) != 1:
                    continue
                for a in range(-10, 11):
                    for scale in (1, 7, 11):
                        if math.gcd(scale, n) == 1:
                            self.assertEqual(a*pow(b, -1, n) % n,
                                             (a*scale)*pow(b*scale, -1, n) % n)

    def test_clock_marks_units_and_additive_cycles(self):
        source = (ROOT/'figures/ch03-clock.tex').read_text()
        lists = re.findall(r'\\foreach \\k in \{([^}]+)\}', source)
        self.assertEqual(len(lists), 2)
        nonunits, units = [set(map(int, v.split(','))) for v in lists]
        self.assertEqual(units, {n for n in range(12) if math.gcd(n, 12) == 1})
        self.assertEqual(nonunits, set(range(12))-units)
        self.assertEqual({5*k % 12 for k in range(12)}, set(range(12)))
        self.assertEqual([4*k % 12 for k in range(4)], [0, 4, 8, 0])
        self.assertIn('90-\\k*30', source)
        self.assertIn('arc (90:90-150:1.55)', source)

    def test_every_crt_grid_cell_and_nonwrapping_arrow(self):
        source = (ROOT/'figures/ch03-crt.tex').read_text()
        scopes = re.findall(r'\\begin\{scope\}[^\n]*\n(.*?)\\end\{scope\}', source, re.S)
        self.assertEqual(len(scopes), 2)
        for text, rows, cols, period in ((scopes[0], 3, 4, 12), (scopes[1], 2, 4, 8)):
            nodes = re.findall(r'\\node\[font=\\footnotesize\] at \(([\d.]+),([\d.]+)\) \{([\d,]+)\}', text)
            cells = {(float(x), float(y)): set(map(int, values.split(','))) for x, y, values in nodes}
            expected = {}
            for n in range(period):
                key = (n % cols+0.5, rows-1-(n % rows)+0.5)
                expected.setdefault(key, set()).add(n)
            self.assertEqual(cells, expected)
            arrows = re.findall(r'\\draw\[[^\n]*?\] \(([\d.]+),([\d.]+)\)--\(([\d.]+),([\d.]+)\);', text)
            self.assertEqual(len(arrows), 6 if rows == 3 else 4)
            for x, y, X, Y in arrows:
                start, end = (float(x), float(y)), (float(X), float(Y))
                self.assertEqual((end[0]-start[0], end[1]-start[1]), (1., -1.))
                self.assertEqual({(n+1) % period for n in cells[start]}, cells[end])

    def test_unit_class_positions_and_all_hensel_branches(self):
        source = (ROOT/'figures/ch03-unit-classes.tex').read_text()
        groups = re.findall(r'\\foreach \\n/\\x/\\y in \{(.*?)\}', source, re.S)
        self.assertEqual(len(groups), 2)
        actual = []
        coordinates = set()
        for group in groups:
            triples = [v.strip().split('/') for v in group.split(',')]
            actual.append({int(n) for n, x, y in triples})
            for n, x, y in triples:
                self.assertNotIn((float(x), float(y)), coordinates)
                coordinates.add((float(x), float(y)))
        self.assertEqual(actual[1], {1, 5, 7, 11})
        self.assertEqual(actual[0], set(range(12))-actual[1])
        source = (ROOT/'figures/ch03-hensel-branches.tex').read_text()
        rows = re.search(r'\\foreach \\x/\\a/\\b/\\c in \{([^}]+)\}', source).group(1)
        branches = [[int(v) for v in row.split('/')[1:]] for row in rows.split(',')]
        for j, modulus in enumerate((5, 25, 125)):
            self.assertEqual({row[j] for row in branches},
                             {n for n in range(modulus) if (n*n+1) % modulus == 0})
            self.assertTrue(all(math.gcd(2*row[j], 5) == 1 for row in branches))
            if j:
                self.assertTrue(all(row[j] % (modulus//5) == row[j-1] for row in branches))

    def test_modular_remainder_and_requested_moment_comparison(self):
        source = (ROOT/'chapters/ch03-congruences.tex').read_text()
        wolsten = source.split(r'\begin{solution}{pb:wolsten}', 1)[1].split(r'\end{solution}', 1)[0]
        self.assertNotIn('O(p^3)', wolsten)
        self.assertIn(r'\equiv1+pe_1+p^2e_2\pmod{p^3}', wolsten)
        kloosterman = source.split(r'\begin{solution}{pb:kloosterman}', 1)[1]
        self.assertIn(r'\sqrt{p^2-p}', kloosterman)
        self.assertGreater(1.19*3**0.75, math.sqrt(6))
        self.assertLess(18**0.25, math.sqrt(6))
        self.assertGreater(18**0.25, 2)
        for p in (5, 7, 11, 13, 31, 101):
            self.assertLess(1.19*p**0.75, p-1)
            self.assertLess(p-1, math.sqrt(p*p-p))
        self.assertEqual([pow(pow(x, 3, 5), 3, 5) for x in range(5)], list(range(5)))

    def test_epigraph_digit_lower_bound_and_unnamed_examples(self):
        # log10(3)>47/100 follows from an exact integer comparison.
        self.assertGreater(3**100, 10**47)
        self.assertGreater(47*3**27, 100*3*10**12)
        self.assertEqual(pow(3, pow(3, 27, 40), 100), 87)
        self.assertEqual(pow(7, 13, 23), 20)
        self.assertEqual(sum(math.gcd(n, 100) == 1 for n in range(1, 101)), 40)
        for n, m, a, b, modulus, answer in ((5, 7, 2, 3, 35, 17),
                                          (6, 8, 1, 3, 24, 19)):
            self.assertEqual([x for x in range(modulus) if x % n == a and x % m == b], [answer])
        self.assertFalse(any(x % 6 == 1 and x % 8 == 2 for x in range(24)))


if __name__ == '__main__':
    unittest.main()
