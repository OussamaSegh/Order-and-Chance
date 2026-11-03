"""Coefficientwise regression for the Volume 2 Ramanujan Journey.

No complex-analysis or later-volume theorem is needed in the exercise.
Finite coefficients validate examples; the infinite-series identities
and all partition congruences still require their manuscript proof.
"""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "volume2-integers/chapters/ch03-congruences.tex"


def multiply(a, b, maximum):
    out = [0] * (maximum + 1)
    for i, x in enumerate(a[:maximum + 1]):
        if x:
            for j, y in enumerate(b[:maximum + 1 - i]):
                if y:
                    out[i+j] += x*y
    return out


def euler_product(maximum):
    # Each new factor is (1 - x^r), with r <= maximum.
    coef = [1] + [0] * maximum
    for r in range(1, maximum + 1):
        for k in range(maximum, r - 1, -1):
            coef[k] -= coef[k-r]
    return coef


class TestVolume2RamanujanFormal(unittest.TestCase):
    def test_advanced_problem_derives_its_own_identities(self):
        text = SOURCE.read_text(encoding="utf-8")
        start = text.index(r"\begin{exercise}[Journey]\label{pb:ramanujan5}")
        stop = text.index(r"\end{exercise}", start)
        question = text[start:stop]
        start = text.index(r"\begin{solution}{pb:ramanujan5}")
        stop = text.index(r"\end{solution}", start)
        proof = text[start:stop].split(r"\leads", 1)[0]
        required = question + proof
        for forbidden in ("Later-volume exploration", "holomorphic",
                          "Analytic continuation", "Volume~5",
                          "theorem from Volume~5"):
            self.assertNotIn(forbidden, required)
        for needed in ("formal power series", "triple product",
                       "pentagonal identity", r"\frac1{E(x)}",
                       r"p(5m+4)\equiv0\pmod5"):
            self.assertIn(needed, required)

    def test_euler_pentagonal_and_jacobi_cube_coefficients(self):
        top = 140
        e = euler_product(top)
        pentagonal = [0] * (top+1)
        for j in range(-30, 31):
            exponent = j*(3*j-1)//2
            if 0 <= exponent <= top:
                pentagonal[exponent] += (-1)**j
        self.assertEqual(e, pentagonal)

        cube = multiply(multiply(e, e, top), e, top)
        jacobi = [0] * (top+1)
        for k in range(40):
            exponent = k*(k+1)//2
            if exponent <= top:
                jacobi[exponent] = (-1)**k*(2*k+1)
        self.assertEqual(cube, jacobi)

        square = multiply(e, e, top)
        fourth = multiply(square, square, top)
        for power in range(5, top + 1, 5):
            self.assertEqual(fourth[power-1] % 5, 0)

    def test_partition_numbers_mod_five(self):
        top = 254
        counts = [1] + [0] * top
        for part in range(1, top + 1):
            for total in range(part, top + 1):
                counts[total] += counts[total-part]
        self.assertEqual([counts[n] for n in range(5)], [1, 1, 2, 3, 5])
        for n in range(0, 51):
            self.assertEqual(
                counts[5*n+4] % 5, 0, f"partition residue at n={n}"
            )


if __name__ == "__main__":
    unittest.main()
