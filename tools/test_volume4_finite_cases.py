"""Exhaustive small finite-case checks for Appendix B's exact Ramsey and van der Waerden values.

These independently enumerate the advertised finite colouring spaces; they do
not establish the general theorems or substitute for a mathematical referee.
"""

from itertools import combinations
from pathlib import Path
import unittest


APPENDIX = (
    Path(__file__).resolve().parents[1]
    / "volume4-chance"
    / "chapters"
    / "extremal.tex"
)


def mono_triangle_free_colours(vertices, colouring):
    """True if the binary edge colouring has no monochromatic triangle."""
    edges = list(combinations(range(vertices), 2))
    indices = {edge: i for i, edge in enumerate(edges)}
    for triple in combinations(range(vertices), 3):
        triangle_mask = sum(1 << indices[edge] for edge in combinations(triple, 2))
        occupied = colouring & triangle_mask
        if occupied == 0 or occupied == triangle_mask:
            return False
    return True


def avoids_three_term_ap(length, colouring):
    """True if neither colour contains a nonconstant three-term progression."""
    for step in range(1, length):
        for first in range(1, length - 2 * step + 1):
            bits = [
                (colouring >> (position - 1)) & 1
                for position in (first, first + step, first + 2 * step)
            ]
            if bits[0] == bits[1] == bits[2]:
                return False
    return True


class TestAppendixBExactFiniteCases(unittest.TestCase):
    def test_r33_is_six_by_exhaustive_edge_colouring(self):
        """12 avoiding K5 colourings exist, but no K6 colouring avoids a triangle."""
        appendix = APPENDIX.read_text(encoding="utf-8")
        self.assertIn("R(3,3)=6", appendix)
        self.assertEqual(
            sum(mono_triangle_free_colours(5, m) for m in range(1 << 10)), 12
        )
        self.assertFalse(
            any(mono_triangle_free_colours(6, m) for m in range(1 << 15))
        )

    def test_w_3_2_is_nine_by_exhaustive_integer_colouring(self):
        """Six avoiding 8-word colourings exist, but none on nine integers."""
        appendix = APPENDIX.read_text(encoding="utf-8")
        self.assertIn("W(3,2)=9", appendix)
        self.assertEqual(
            sum(avoids_three_term_ap(8, m) for m in range(1 << 8)), 6
        )
        self.assertFalse(
            any(avoids_three_term_ap(9, m) for m in range(1 << 9))
        )


if __name__ == "__main__":
    unittest.main()
