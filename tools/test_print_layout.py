"""Guard trim migration, odd-page spine rounding and mixed-size PDF rejection."""
import unittest
from unittest.mock import patch

from check_cover_pdf import check_interior
from print_layout import LAYOUT, check_sync, specification


class PaperbackTest(unittest.TestCase):
    def test_approved_geometry_and_generated_tex(self):
        check_sync()
        self.assertEqual((LAYOUT['trim_width_in'], LAYOUT['trim_height_in']), (7, 10))

    def test_spine_uses_even_rounded_actual_pages(self):
        odd = specification(233)
        even = specification(234)
        self.assertEqual(odd['interior_pages'], 233)
        self.assertEqual(odd['kdp_pages'], 234)
        self.assertEqual(odd['spine_in'], even['spine_in'])
        self.assertAlmostEqual(odd['wrap_width_in'], 14.25 + 0.5492)
        self.assertEqual(odd['ink'], 'premium_color')
        self.assertEqual(odd['paper'], 'white')
        self.assertEqual(odd['wrap_height_in'], 10.25)
        for pages in (23, 829):
            with self.assertRaises(ValueError):
                specification(pages)

    def test_mixed_size_interior_is_rejected(self):
        with patch('check_cover_pdf.subprocess.check_output', side_effect=[
                'Pages: 2\n', 'Page 1 size: 504 x 720 pts\nPage 2 size: 432 x 648 pts\n']):
            with self.assertRaisesRegex(ValueError, 'page 2'):
                check_interior('mixed.pdf')

    def test_canonical_a4_pdf_is_rejected(self):
        with patch('check_cover_pdf.subprocess.check_output', side_effect=[
                'Pages: 1\n', 'Page 1 size: 595.276 x 841.89 pts\n']):
            with self.assertRaisesRegex(ValueError, 'page 1'):
                check_interior('tome0.pdf')

    def test_missing_page_dimensions_are_rejected(self):
        with patch('check_cover_pdf.subprocess.check_output', side_effect=[
                'Pages: 2\n', 'Page 1 size: 504 x 720 pts\n']):
            with self.assertRaisesRegex(ValueError, 'every interior page'):
                check_interior('incomplete.pdf')


if __name__ == '__main__':
    unittest.main()
