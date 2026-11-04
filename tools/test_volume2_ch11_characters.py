"""Explicit character tables and independent small-group exhaustive checks."""

import cmath
from fractions import Fraction
import itertools
import math
import unittest


def factorization(n):
    result, p = {}, 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result


def unit_coordinates(m):
    sizes, local = [], []
    for p, exponent in factorization(m).items():
        q = p**exponent
        if p == 2 and exponent >= 3:
            length = 2**(exponent-2)
            mapping = {((-1)**a*pow(5, b, q)) % q: (a, b)
                       for a in (0, 1) for b in range(length)}
            sizes.extend((2, length))
        else:
            phi = (p-1)*p**(exponent-1)
            g = next(g for g in range(1, q) if math.gcd(g, q) == 1
                     and len({pow(g, j, q) for j in range(phi)}) == phi)
            mapping = {pow(g, j, q): (j,) for j in range(phi)}
            sizes.append(phi)
        local.append((q, mapping))
    coordinates = {a: tuple(k for q, mapping in local for k in mapping[a % q])
                   for a in range(m) if math.gcd(a, m) == 1}
    return sizes, coordinates


def character_phases(m):
    sizes, coordinates = unit_coordinates(m)
    return [{a: sum((Fraction(j*k, N) for j, k, N in zip(label, ks, sizes)), Fraction()) % 1
             for a, ks in coordinates.items()}
            for label in itertools.product(*(range(N) for N in sizes))]


class CharacterChecks(unittest.TestCase):
    def test_first_two_exercise_tables(self):
        expected = [(1, 1, 1, 1), (1, 1j, -1j, -1),
                    (1, -1, -1, 1), (1, -1j, 1j, -1)]
        for row, values in zip(character_phases(5), expected):
            for a, value in zip((1, 2, 3, 4), values):
                self.assertLess(abs(cmath.exp(2j*math.pi*float(row[a]))-value), 1e-8)
        for p, sign in zip((3, 5, 7, 11, 13, 17, 19), (-1, -1, 1, -1, -1, 1, -1)):
            self.assertEqual(pow(2, (p-1)//2, p), sign % p)
            self.assertEqual(1 if p % 8 in (1, 7) else -1, sign)

    def test_count_separation_and_multiplication(self):
        for m in range(1, 41):
            phases = character_phases(m)
            units = [a for a in range(m) if math.gcd(a, m) == 1]
            self.assertEqual(len(phases), len(units))
            self.assertEqual(len({tuple(row[a] for a in units) for row in phases}), len(units))
            for a in units:
                if a != 1 % m:
                    self.assertTrue(any(row[a] != 0 for row in phases))
                for b in units:
                    for row in phases:
                        self.assertEqual((row[a]+row[b]) % 1, row[a*b % m])

    def test_small_groups_against_all_possible_homomorphisms(self):
        for m in range(1, 13):
            units = [a for a in range(m) if math.gcd(a, m) == 1]
            phi = len(units)
            if phi > 4:
                continue
            others = [a for a in units if a != 1 % m]
            exhaustive = set()
            for values in itertools.product(range(phi), repeat=len(others)):
                mapping = {1 % m: 0, **dict(zip(others, values))}
                if all((mapping[a]+mapping[b]-mapping[a*b % m]) % phi == 0
                       for a in units for b in units):
                    exhaustive.add(tuple(mapping[a] for a in units))
            constructed = {tuple(int(row[a]*phi) for a in units) for row in character_phases(m)}
            self.assertEqual(exhaustive, constructed, m)

    def test_both_orthogonality_relations_including_nonunits(self):
        for m in range(1, 33):
            phases = character_phases(m)
            table = [[cmath.exp(2j*math.pi*float(row[a])) if a in row else 0
                      for a in range(m)] for row in phases]
            phi = len(table)
            for i, row in enumerate(table):
                for j, other in enumerate(table):
                    total = sum(x*y.conjugate() for x, y in zip(row, other))
                    self.assertLess(abs(total-(phi if i == j else 0)), 1e-8)
            for a in range(m):
                for b in range(m):
                    total = sum(row[a]*row[b].conjugate() for row in table)
                    expected = phi if a == b and math.gcd(a, m) == 1 else 0
                    self.assertLess(abs(total-expected), 1e-8)


if __name__ == "__main__":
    unittest.main()
