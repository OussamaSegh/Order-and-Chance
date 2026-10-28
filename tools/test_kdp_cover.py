"""Keep cover typography vector while removing only illustration transparency."""
from pathlib import Path
import tempfile
import unittest

import pymupdf
from pypdf import PdfReader, PdfWriter

from kdp_cover import check_opaque, flatten_art, remove_empty_opacity
from check_print_cover import check_patch_placements
from kdp_pdf import compare_pages

ROOT = Path(__file__).resolve().parent.parent


class CoverExportTest(unittest.TestCase):
    def source(self, directory, rectangle):
        path = Path(directory) / 'cover.pdf'
        doc = pymupdf.open()
        page = doc.new_page(width=504, height=720)
        page.insert_font(fontname='inter', fontfile=str(ROOT / 'common/fonts/Inter-SemiBold.ttf'))
        page.insert_text((54, 80), 'Cover typography', fontname='inter', fontsize=24)
        page.draw_rect(rectangle, color=(.9, .3, .2), fill=(.9, .3, .2), fill_opacity=.4, stroke_opacity=.4)
        doc.save(path)
        doc.close()
        return path

    def test_only_art_is_composited_at_600ppi_and_text_remains_vector(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.source(directory, (180, 300, 400, 500))
            output = Path(directory) / 'composited.pdf'
            patches = flatten_art(source, output, directory)
            self.assertEqual(len(patches), 1)
            self.assertEqual(patches[0]['ppi'], 600)
            check_patch_placements(output, patches)
            wrong = [{**patches[0], 'bounds_pt': [v + 20 for v in patches[0]['bounds_pt']]}]
            with self.assertRaisesRegex(ValueError, 'pixels or placement'):
                check_patch_placements(output, wrong)
            with pymupdf.open(output) as doc:
                self.assertIn('Cover typography', doc[0].get_text())
                self.assertEqual(len(doc[0].get_images()), 1)
                self.assertTrue(doc[0].get_fonts())

    def test_overlap_with_typography_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.source(directory, (50, 50, 350, 100))
            with self.assertRaisesRegex(ValueError, 'overlaps lettering'):
                flatten_art(source, Path(directory) / 'bad.pdf', directory)

    def test_whole_cover_rasterization_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.source(directory, (1, 1, 503, 719))
            with self.assertRaisesRegex(ValueError, 'whole cover'):
                flatten_art(source, Path(directory) / 'bad.pdf', directory)

    def test_live_cover_opacity_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.source(directory, (180, 300, 400, 500))
            writer = PdfWriter(clone_from=PdfReader(source))
            writer.metadata = None
            writer.pdf_header = '%PDF-1.5'
            writer.write(Path(directory) / 'raw.pdf')
            with self.assertRaisesRegex(ValueError, 'live transparency'):
                check_opaque(Path(directory) / 'raw.pdf')

    def test_invisible_identity_duplicates_are_removed_without_changing_visible_text(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.source(directory, (180, 300, 400, 500))
            with pymupdf.open(source) as doc:
                doc[0].insert_text((54, 110), 'Invisible duplicate', fill_opacity=0)
                doc.save(Path(directory) / 'hidden.pdf')
            flattened = Path(directory) / 'flattened.pdf'
            flatten_art(Path(directory) / 'hidden.pdf', flattened, directory)
            output = Path(directory) / 'opaque.pdf'
            remove_empty_opacity(flattened, output)
            with pymupdf.open(output) as doc:
                self.assertIn('Cover typography', doc[0].get_text())
                self.assertNotIn('Invisible duplicate', doc[0].get_text())
                self.assertTrue(all(s['opacity'] == 1 for s in doc[0].get_texttrace()))

    def test_compositing_comparison_still_rejects_changes_outside_the_art(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.source(directory, (180, 300, 400, 500))
            flattened = Path(directory) / 'flat.pdf'
            patches = flatten_art(source, flattened, directory)
            ignore = {0: [patches[0]['bounds_pt']]}
            compare_pages(source, flattened, ignore_rectangles=ignore)
            with pymupdf.open(flattened) as doc:
                doc[0].draw_rect((50, 50, 350, 110), color=(0, 0, 0), fill=(0, 0, 0))
                doc.save(Path(directory) / 'changed.pdf')
            with self.assertRaisesRegex(ValueError, 'body differs'):
                compare_pages(source, Path(directory) / 'changed.pdf', ignore_rectangles=ignore)


if __name__ == '__main__':
    unittest.main()
