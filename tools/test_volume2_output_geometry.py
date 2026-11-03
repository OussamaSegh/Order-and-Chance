"""Regression for printed page-count/cover geometry in Volume 2 QA.

The manuscript's page count is allowed to change during rewriting.
The spine must follow the canonical KDP specification at four decimal
places; the earlier three-decimal verifier rejected a valid 315-page
interior and 0.7417-inch spine.
"""
from pathlib import Path
import runpy
import unittest

from print_layout import specification


ROOT = Path(__file__).resolve().parents[1]
check_paper_geometry = runpy.run_path(
    str(ROOT / "review/volume2-continuity/check_volume2_outputs.py")
)["check_paper_geometry"]


class TestVolume2OutputGeometry(unittest.TestCase):
    def test_even_padding_and_spine_are_exactly_the_print_specification(self):
        for pages in (24, 25, 233, 313, 314, 315, 316, 828):
            with self.subTest(pages=pages):
                spec = specification(pages)
                self.assertIsNone(check_paper_geometry(spec, pages))
                self.assertEqual(spec["kdp_pages"] % 2, 0)
        self.assertEqual(specification(315)["kdp_pages"], 316)
        self.assertEqual(specification(315)["spine_in"], 0.7417)
        self.assertEqual(specification(315)["wrap_width_in"], 14.9917)

    def test_three_decimal_truncation_is_not_equivalent(self):
        spec = specification(315)
        incorrectly_rounded = dict(spec, spine_in=round(
            spec["kdp_pages"] * spec["spine_in_per_page"], 3
        ))
        self.assertNotEqual(incorrectly_rounded["spine_in"], spec["spine_in"])
        with self.assertRaisesRegex(AssertionError, "Spine is inconsistent"):
            check_paper_geometry(incorrectly_rounded, 315)

    def test_reject_wrong_page_count_or_cover_geometry(self):
        spec = specification(315)
        with self.assertRaisesRegex(AssertionError, "page count"):
            check_paper_geometry(spec, 314)
        with self.assertRaisesRegex(AssertionError, "Wrap width"):
            check_paper_geometry(dict(spec, wrap_width_in=14.99), 315)
        with self.assertRaisesRegex(AssertionError, "Wrap height"):
            check_paper_geometry(dict(spec, wrap_height_in=10.20), 315)
        with self.assertRaisesRegex(AssertionError, "KDP counted pages"):
            check_paper_geometry(dict(spec, kdp_pages=315), 315)


if __name__ == "__main__":
    unittest.main()
