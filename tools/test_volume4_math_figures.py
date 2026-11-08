"""Source-data consistency checks for selected exact mathematical Volume 4 figures.

Tests are meaningful for the stored coordinates, but *not* image rendering,
font/contrast, or all 41 diagrams. Human visual review remains mandatory.
"""

from itertools import combinations
from pathlib import Path
import re
import unittest


FIGURES = Path(__file__).resolve().parents[1] / "volume4-chance" / "figures"
POINT = re.compile(r"\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)")


def points(text):
    return [(float(x), float(y)) for x, y in POINT.findall(text)]


class TestVolume4MathFigures(unittest.TestCase):
    def test_polya_urn_simulations_have_possible_red_counts(self):
        """20 stored paths should be compatible with one added ball per draw."""
        src = (FIGURES / "ch10-polya.tex").read_text(encoding="utf-8")
        paths = [
            line for line in src.splitlines()
            if line.startswith(r"\draw[") and "(0,0.5000)" in line
        ]
        self.assertEqual(len(paths), 20)
        checked = 0
        for path in paths:
            samples = points(path)
            self.assertEqual(len(samples), 146)
            self.assertEqual(samples[0], (0.0, 0.5))
            self.assertEqual(samples[-1][0], 1000.0)
            prev_n, prev_r = 0, 1
            for nfloat, frac in samples:
                n = int(nfloat)
                self.assertEqual(nfloat, n)
                self.assertGreaterEqual(n, prev_n)
                # M_n=R_n/(n+2), stored as a four-decimal rounded value.
                red = round(frac * (n + 2))
                self.assertAlmostEqual(frac, red / (n + 2), delta=0.000051)
                self.assertGreaterEqual(red, prev_r)
                self.assertLessEqual(red - prev_r, n - prev_n)
                self.assertLessEqual(red, n + 1)
                prev_n, prev_r = n, red
                checked += 1
        self.assertEqual(checked, 2920)

    def test_brownian_reflection_figure_is_exact_mirror(self):
        """Post-hit y coordinates must sum to 2a at each plotted time."""
        src = (FIGURES / "ch12-reflection.tex").read_text(encoding="utf-8")
        original = re.search(r"\\draw\[MidnightBlue,very thick\](.*?);", src, re.S)
        reflected = re.search(r"\\draw\[BrickRed,very thick\](.*?);", src, re.S)
        self.assertIsNotNone(original)
        self.assertIsNotNone(reflected)
        blue = [(x, y) for x, y in points(original.group(1)) if x >= 4]
        red = points(reflected.group(1))
        self.assertEqual(len(blue), 9)
        self.assertEqual(len(red), 9)
        for (xb, yb), (xr, yr) in zip(blue, red):
            self.assertAlmostEqual(xb, xr)
            self.assertAlmostEqual(yb + yr, 2.0)  # a=1 horizontal barrier
        self.assertEqual(blue[0], (4.0, 1.0))
        self.assertEqual(red[0], (4.0, 1.0))

    def test_ramsey_k5_colouring_has_no_monochromatic_triangle(self):
        """All 10 edges are present and each of the two colour graphs is C5."""
        src = (FIGURES / "ch12-ramsey.tex").read_text(encoding="utf-8")
        edges = {}
        for line in src.splitlines():
            if not line.startswith((r"\draw[BrickRed,thick]", r"\draw[MidnightBlue,thick]")):
                continue
            endpoints = points(line)
            self.assertEqual(len(endpoints), 2)
            edge = frozenset(endpoints)
            self.assertNotIn(edge, edges)
            edges[edge] = "red" if "BrickRed" in line else "blue"
        vertices = set().union(*edges.keys())
        self.assertEqual(len(vertices), 5)
        self.assertEqual(len(edges), 10)
        self.assertEqual(sum(c == "red" for c in edges.values()), 5)
        self.assertEqual(sum(c == "blue" for c in edges.values()), 5)
        for triplet in combinations(vertices, 3):
            colours = [
                edges[frozenset(pair)] for pair in combinations(triplet, 2)
            ]
            self.assertGreater(len(set(colours)), 1)


if __name__ == "__main__":
    unittest.main()
