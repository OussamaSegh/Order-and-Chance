"""Independent complete Chapter 6 figure data and worked computations."""

from collections import Counter
from fractions import Fraction
import math
from pathlib import Path
import re
import unittest

from tools.volume2_liar_figure import factors, liar_counts, render

ROOT = Path(__file__).resolve().parents[1]/'volume2-integers'


def legendre(a, p):
    return 0 if a % p == 0 else (1 if a % p in {x*x % p for x in range(1, p)} else -1)


def jacobi(a, n):
    return math.prod(legendre(a, p)**e for p, e in factors(n).items())


def unit_liars(n):
    d, s = n-1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    units = [a for a in range(1, n) if math.gcd(a, n) == 1]
    euler = sum(pow(a, (n-1)//2, n) == jacobi(a, n) % n for a in units)
    strong = sum(pow(a, d, n) == 1 or any(pow(a, 2**j*d, n) == n-1 for j in range(s)) for a in units)
    return len(units), euler, strong


class ChapterSixSourceChecks(unittest.TestCase):
    def test_every_residue_strip_class_and_colour_independent_legend(self):
        source = (ROOT/'figures/ch06-residues.tex').read_text()
        data = dict((int(n), int(square)) for n, square in re.findall(r'(\d+)/(\d+)', source.split('\\ifnum')[0]))
        self.assertEqual(data, {n: int(n in {x*x % 11 for x in range(11)}) for n in range(11)})
        self.assertIn('shaded: quadratic residues', source)
        self.assertNotIn('teal:', source)

    def test_every_reciprocity_table_sign_and_shaded_exception(self):
        source = (ROOT/'figures/ch06-reciprocity-table.tex').read_text()
        nodes = {(int(x), int(y)): value for x, y, value in re.findall(
            r'\\node at \((-?\d+),(-?\d+)\) \{\$([\d+\-]+)\$\};', source)}
        primes = [3, 5, 7, 11, 13]
        self.assertEqual([int(nodes[j, 1]) for j in range(5)], primes)
        self.assertEqual([int(nodes[-1, -j]) for j in range(5)], primes)
        for i, p in enumerate(primes):
            for j, q in enumerate(primes):
                expected = {0: '0', 1: '+', -1: '-'}[legendre(p, q)]
                self.assertEqual(nodes[j, -i], expected)
        shaded = set()
        for x, y, u, v in re.findall(r'\\fill\[gray!20\] \(([-\d.]+),([-\d.]+)\) rectangle \(([-\d.]+),([-\d.]+)\)', source):
            shaded.add(((Fraction(x)+Fraction(u))/2, (Fraction(y)+Fraction(v))/2))
        self.assertEqual(shaded, {(j, -i) for i, p in enumerate(primes) for j, q in enumerate(primes)
                                 if p != q and p % 4 == q % 4 == 3})

    def test_all_eisenstein_points_and_both_counts(self):
        source = (ROOT/'figures/ch06-eisenstein.tex').read_text()
        data = {(int(x), int(y)): colour for colour, x, y in re.findall(
            r'\\fill\[(MidnightBlue|ForestGreen)\] \((\d+),(\d+)\) circle', source)}
        self.assertEqual(data, {(x, y): 'MidnightBlue' if 7*y < 11*x else 'ForestGreen'
                                for x in range(1, 4) for y in range(1, 6)})
        self.assertEqual(Counter(data.values()), {'MidnightBlue': 8, 'ForestGreen': 7})
        self.assertEqual(sum(11*x//7 for x in range(1, 4)), 8)
        self.assertEqual(sum(7*y//11 for y in range(1, 6)), 7)
        self.assertEqual(Fraction('5.5')/Fraction('3.5'), Fraction(11, 7))

    def test_complete_liar_plot_matches_every_enumerated_unit_base(self):
        source = (ROOT/'figures/ch03-liars.tex').read_text()
        self.assertEqual(source, render())
        plotted_euler = {int(n): Fraction(y) for n, y in re.findall(
            r'\\draw\[Goldenrod!85!black,line width=0.35pt\] \((\d+),([\d.]+)\)', source)}
        plotted_strong = {int(n): Fraction(y) for n, y in re.findall(
            r'\\fill\[MidnightBlue\] \((\d+),([\d.]+)\)', source)}
        composites = {n for n in range(9, 1500, 2) if any(n % d == 0 for d in range(2, math.isqrt(n)+1))}
        self.assertEqual(len(composites), 511)
        self.assertEqual(set(plotted_euler), composites)
        self.assertEqual(set(plotted_strong), composites)
        for n in sorted(composites):
            direct = unit_liars(n)
            self.assertEqual(liar_counts(n), direct, n)
            phi, euler, strong = direct
            self.assertLessEqual(abs(plotted_euler[n]-Fraction(euler, phi)), Fraction(1, 2_000_000))
            self.assertLessEqual(abs(plotted_strong[n]-Fraction(strong, phi)), Fraction(1, 2_000_000))
            self.assertLessEqual(2*euler, phi)
            self.assertLessEqual(4*strong, n-1)  # Actual stated random-base model.
            if n != 9:
                self.assertLessEqual(4*strong, phi)
        self.assertIn('circle (1.1pt)', source)
        self.assertIn('circle (0.6pt)', source)

    def test_zero_boundary_in_strong_liar_probability_model(self):
        phi, _, strong = unit_liars(9)
        self.assertEqual((phi, strong), (6, 2))
        self.assertEqual(Fraction(strong, phi), Fraction(1, 3))
        self.assertEqual(Fraction(strong, 8), Fraction(1, 4))
        source = (ROOT/'chapters/ch06-quadratic-reciprocity.tex').read_text()
        proof = source.split(r'\begin{solution}{pb:rabin}')[1].split(r'\end{solution}')[0]
        self.assertIn(r'uniformly from $1,\ldots,n-1$', proof)
        self.assertIn('Bach (1990)', proof)

    def test_complete_219_root_certificate_and_signed_lists(self):
        self.assertTrue(all(383 % p for p in (2, 3, 5, 7, 11, 13, 17, 19)))
        self.assertEqual([pow(219, 2**j, 383) for j in range(1, 7)], [86, 119, 373, 100, 42, 232])
        self.assertEqual(pow(219, 96, 383), 169)
        self.assertEqual([x for x in range(383) if x*x % 383 == 219], [169, 214])
        self.assertEqual(169**2, 383*74+219)
        for a, p, expected in ((3, 11, [3, -5, -2, 1, 4]), (2, 11, [2, 4, -5, -3, -1]),
                                (3, 13, [3, 6, -4, -1, 2, 5])):
            signed = [((a*k+p//2) % p)-p//2 for k in range(1, (p+1)//2)]
            self.assertEqual(signed, expected)
            self.assertEqual((-1)**sum(x < 0 for x in signed), legendre(a, p))

    def test_actual_jacobi_chain_and_small_swap(self):
        chain = [(1001, 9907), (898, 1001), (449, 1001), (103, 449), (37, 103), (29, 37), (8, 29)]
        self.assertEqual([jacobi(a, n) for a, n in chain], [-1]*len(chain))
        self.assertEqual((jacobi(19, 35), jacobi(16, 19), jacobi(2, 15)), (-1, 1, 1))
        self.assertNotIn(2, {x*x % 15 for x in range(15)})
        self.assertEqual([jacobi(a, n) for a, n in ((43, 91), (91, 43), (5, 43), (43, 5), (3, 5), (83, 101), (18, 83))],
                         [1, -1, -1, -1, -1, -1, -1])

    def test_character_abbreviation_is_defined_before_first_sum(self):
        source = (ROOT/'chapters/ch06-quadratic-reciprocity.tex').read_text()
        definition = source.index(r'Write $\chi(a)=\left(\frac ap\right)$')
        first_use = source.index(r'\chi(a)')
        self.assertEqual(definition+len('Write $'), first_use)
        self.assertIn('pair the nonzero inputs', source)


if __name__ == '__main__':
    unittest.main()
