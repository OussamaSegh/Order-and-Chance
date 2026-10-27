"""Prevent low-resolution or enlarged cover bitmaps returning to print output."""
import unittest
import io
from unittest.mock import patch

from PIL import Image

from check_print_cover import (check_frame_alignment, check_placements, check_paper,
                               pixel_key, raster_placements)


HEADER = 'page num type width height color comp bpc enc interp object ID x-ppi y-ppi size ratio\n'


class PrintCoverQualityTest(unittest.TestCase):
    def test_visible_frame_guard_catches_shift_despite_valid_page_size(self):
        strip = Image.new('RGB', (12, 684), (21, 21, 22))
        for correct in (False, True):
            if correct:
                for y in range(684):
                    strip.putpixel((3, y), (255, 113, 99))
            data = io.BytesIO()
            strip.save(data, format='PNG')
            with patch('check_print_cover.subprocess.check_output', return_value=data.getvalue()):
                if correct:
                    check_frame_alignment('proof.pdf', 504)
                else:
                    with self.assertRaisesRegex(ValueError, 'shifted or clipped'):
                        check_frame_alignment('proof.pdf', 504)

    def test_native_grain_at_true_print_scale_passes(self):
        rows = raster_placements(HEADER +
            '1 0 image 1049 1500 rgb 3 8 image no 6 0 360 360 771K 24%\n')
        self.assertEqual(len(rows), 1)
        check_placements(rows)

    def test_original_front_and_stretched_background_are_rejected(self):
        for x, y in [(150, 150), (70, 146), (300, 299)]:
            with self.subTest(ppi=(x, y)):
                rows = raster_placements(HEADER +
                    f'1 0 image 1049 1500 rgb 3 8 image no 6 0 {x} {y} 771K 24%\n')
                with self.assertRaisesRegex(ValueError, 'ppi'):
                    check_placements(rows)

    def test_300_ppi_boundary_and_all_vector_pages_pass(self):
        check_placements([{'index': 0, 'x_ppi': 300, 'y_ppi': 300}])
        check_placements([])

    def test_a_resized_cover_cannot_masquerade_as_high_resolution_paper(self):
        paper = Image.new('RGB', (32, 32), (21, 21, 22))
        allowed = {pixel_key(paper)}
        check_paper(paper.copy(), allowed)
        art = paper.copy()
        art.putpixel((16, 16), (255, 138, 120))
        with self.assertRaisesRegex(ValueError, 'bitmap other than native paper'):
            check_paper(art, allowed)


if __name__ == '__main__':
    unittest.main()
