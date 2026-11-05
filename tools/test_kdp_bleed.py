"""KDP's page-13 rejection: trim-size edge ink must become real mirrored bleed."""
from pathlib import Path
import tempfile
import unittest

import pymupdf
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

from kdp_bleed import add_bleed, check_bleed
from kdp_pdf import compare_pages

ROOT = Path(__file__).resolve().parent.parent


class InteriorBleedTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.source = self.folder / 'source.pdf'
        self.output = self.folder / 'print.pdf'
        doc = pymupdf.open()
        # The actual rejected part page has a solid charcoal rectangle at the
        # trim edges and embedded vector type. Cover both physical page sides.
        for index in range(3):
            page = doc.new_page(width=504, height=720)
            if index == 0:
                # XeTeX emits TikZ's rectangle as four line segments, with
                # xcolor's three-decimal RGB values and a tiny trim overshoot.
                page.draw_polyline([(0, 0), (0, 720.00928), (504.00648, 720.00928),
                                    (504.00648, 0), (0, 0)], closePath=False,
                                   color=None, fill=(.082, .082, .086))
            elif index == 1:
                page.draw_rect(page.rect, color=None, fill=(.082, .082, .086))
            page.insert_font(fontname='book', fontfile=str(ROOT / 'common/fonts/EBGaramond-Regular.otf'))
            page.insert_text((65, 90), f'Part page {index + 1}', fontname='book', fontsize=24,
                             color=(1, 1, 1) if index < 2 else (0, 0, 0))
        doc.save(self.source)
        doc.close()

    def test_real_bleed_preserves_vectors_and_trim_positions_on_both_sides(self):
        original = self.source.read_bytes()
        backgrounds = add_bleed(self.source, self.output)
        self.assertEqual([item['page'] for item in backgrounds], [1, 2])
        self.assertEqual(check_bleed(self.output, backgrounds), 3)
        self.assertEqual(check_bleed(self.output), 3)
        self.assertEqual(self.source.read_bytes(), original)
        reader = PdfReader(self.output)
        self.assertTrue(all(tuple(page.mediabox) == (0, 0, 513, 738) for page in reader.pages))
        self.assertEqual(tuple(reader.pages[0].trimbox), (0, 9, 504, 729))
        self.assertEqual(tuple(reader.pages[1].trimbox), (9, 9, 513, 729))
        self.assertEqual(tuple(reader.pages[2].trimbox), (0, 9, 504, 729))
        with pymupdf.open(self.output) as doc:
            self.assertTrue(all('Part page' in page.get_text() for page in doc))
            self.assertTrue(all(not page.get_images() for page in doc))
        self.assertEqual(compare_pages(self.source, self.output, trim_bleed=True)['compared_pages'], 3)

    def test_rejected_trim_size_and_four_sided_bleed_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'page 1.*media box'):
            check_bleed(self.source)
        add_bleed(self.source, self.output)
        writer = PdfWriter(clone_from=PdfReader(self.output))
        writer.pages[0].mediabox = RectangleObject((0, 0, 522, 738))
        writer.write(self.folder / 'four-sided.pdf')
        with self.assertRaisesRegex(ValueError, 'page 1.*media box'):
            check_bleed(self.folder / 'four-sided.pdf')

    def test_white_padding_around_a_divider_is_not_bleed(self):
        # Independently construct the tempting but incorrect correction: a
        # larger white page with the old divider pasted at the trim position.
        with pymupdf.open(self.source) as source, pymupdf.open() as padded:
            page = padded.new_page(width=513, height=738)
            page.show_pdf_page(pymupdf.Rect(0, 9, 504, 729), source, 0)
            padded.save(self.folder / 'padded.pdf')
        writer = PdfWriter(clone_from=PdfReader(self.folder / 'padded.pdf'))
        writer.pages[0].trimbox = RectangleObject((0, 9, 504, 729))
        writer.pages[0].bleedbox = RectangleObject((0, 0, 513, 738))
        writer.write(self.output)
        with self.assertRaisesRegex(ValueError, 'page 1 background does not fill the bleed'):
            check_bleed(self.output)

    def test_wrong_facing_page_trim_is_rejected(self):
        add_bleed(self.source, self.output)
        writer = PdfWriter(clone_from=PdfReader(self.output))
        writer.pages[1].trimbox = RectangleObject((0, 9, 504, 729))
        writer.write(self.folder / 'wrong-side.pdf')
        with self.assertRaisesRegex(ValueError, 'page 2.*trim box'):
            check_bleed(self.folder / 'wrong-side.pdf')

    def test_unextendable_edge_art_is_rejected(self):
        with pymupdf.open() as doc:
            page = doc.new_page(width=504, height=720)
            page.draw_rect((470, 100, 504, 200), color=None, fill=(.3, .4, .5))
            doc.save(self.folder / 'edge-art.pdf')
        with self.assertRaisesRegex(ValueError, 'Page 1: edge-reaching artwork needs authored bleed'):
            add_bleed(self.folder / 'edge-art.pdf', self.output)


if __name__ == '__main__':
    unittest.main()
