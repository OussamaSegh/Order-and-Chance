"""Regressions for the actual KDP upload format, not merely a readable PDF."""
from pathlib import Path
import json
import shutil
import tempfile
import unittest

import pymupdf
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import (ArrayObject, DecodedStreamObject, DictionaryObject,
                          EncodedStreamObject, FloatObject, NameObject)

from book_pdf import check_pair, make_download
from kdp_pdf import check, export, prepare, repair_hex

ROOT = Path(__file__).resolve().parent.parent


class PrintPreparationTest(unittest.TestCase):
    def test_hex_end_marker_is_repaired_without_changing_decoded_bytes(self):
        stream = EncodedStreamObject()
        stream[NameObject('/Filter')] = NameObject('/ASCIIHexDecode')
        stream._data = b'0011ff'
        self.assertEqual(repair_hex(stream), 1)
        self.assertEqual(stream.get_data(), b'\x00\x11\xff')
        self.assertEqual(repair_hex(stream), 0)

    def fixture(self, directory):
        path = Path(directory) / 'source.pdf'
        native = Path(directory) / 'native.pdf'
        doc = pymupdf.open()
        for text in ['First page: x = 1.', 'Second page: y = 2.']:
            page = doc.new_page(width=504, height=720)
            page.insert_font(fontname='ebgaramond', fontfile=str(ROOT / 'common/fonts/EBGaramond-Regular.otf'))
            page.insert_text((54, 80), text, fontname='ebgaramond', fontsize=11)
            page.draw_rect((54, 100, 200, 150), color=(.1, .3, .5), fill=(.9, .95, 1))
        doc.save(native)
        doc.close()
        writer = PdfWriter(clone_from=PdfReader(native))
        writer.add_metadata({'/Title': 'Interactive source'})
        writer.add_named_destination('chapter.1', 0)
        writer.add_outline_item('First chapter', 0)
        writer.add_annotation(0, Link(rect=(54, 70, 100, 80), url='https://example.org'))
        for page in writer.pages:
            resources = DictionaryObject(page['/Resources'].get_object())
            resources[NameObject('/ExtGState')] = DictionaryObject({
                NameObject('/UnusedAlpha'): DictionaryObject({NameObject('/ca'): FloatObject(.2)}),
                NameObject('/LiveAlpha'): DictionaryObject({NameObject('/ca'): FloatObject(.5)})})
            page[NameObject('/Resources')] = resources
        stream = DecodedStreamObject()
        stream.set_data(writer.pages[1].get_contents().get_data() +
                        b'\nq /LiveAlpha gs 0.2 0.4 0.8 rg 54 500 100 30 re f Q\n')
        writer.pages[1][NameObject('/Contents')] = stream
        writer.write(path)
        return path

    def test_raw_pdf_is_rejected_and_preparation_preserves_the_source(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.fixture(directory)
            original = source.read_bytes()
            with self.assertRaisesRegex(ValueError, 'PDF 1.3|metadata'):
                check(source)
            output = Path(directory) / 'prepared.pdf'
            report = prepare(source, output)
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(report['transparency_pages'], [2])
            self.assertGreaterEqual(report['unused_graphics_states_pruned'], 3)
            reader = PdfReader(output)
            self.assertFalse(reader.metadata)
            self.assertFalse(reader.named_destinations)
            self.assertFalse(reader.outline)
            self.assertTrue(all('/Annots' not in p for p in reader.pages))

    @unittest.skipUnless(shutil.which('gs') and shutil.which('pdffonts'), 'Ghostscript and Poppler required')
    def test_export_and_reading_provenance_and_changed_print_rejection(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = self.fixture(directory)
            # Production has a 24-page minimum; keep the actual test font/vector
            # pages and pad with legitimate blank pages for this upload fixture.
            writer = PdfWriter(clone_from=PdfReader(source))
            for _ in range(22):
                writer.add_blank_page(width=504, height=720)
            writer.write(directory / 'book.pdf')
            source = directory / 'book.pdf'
            output, report = directory / 'print.pdf', directory / 'report.json'
            data = export(source, output, report)
            self.assertEqual(data['flattened_pages'], [2])
            self.assertEqual(check(output, report), 24)
            with pymupdf.open(output) as printed:
                self.assertIn('First page', printed[0].get_text())
                self.assertEqual(printed[1].get_text().strip(), '')
            cover = PdfWriter()
            cover.add_blank_page(width=504, height=720)
            cover.write(directory / 'front.pdf')
            make_download(directory / 'front.pdf', source, directory / 'download.pdf')
            self.assertEqual(check_pair(directory / 'download.pdf', output, report), 24)
            altered = PdfWriter(clone_from=PdfReader(output))
            altered.pages[0][NameObject('/Rotate')] = FloatObject(90)
            altered.write(directory / 'changed.pdf')
            with self.assertRaisesRegex(ValueError, 'rotated|report'):
                check(directory / 'changed.pdf', report)
            altered = PdfWriter(clone_from=PdfReader(directory / 'download.pdf'))
            stream = DecodedStreamObject()
            stream.set_data(b'')
            altered.pages[1][NameObject('/Contents')] = stream
            altered.write(directory / 'changed-reading.pdf')
            with self.assertRaisesRegex(ValueError, 'body differs'):
                check_pair(directory / 'changed-reading.pdf', output, report)

    def test_in_place_export_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = self.fixture(directory)
            with self.assertRaisesRegex(ValueError, 'separate'):
                export(source, source, Path(directory) / 'report.json')


if __name__ == '__main__':
    unittest.main()
