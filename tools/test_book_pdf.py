"""Check cover attachment, unchanged interiors and usable PDF navigation."""
from pathlib import Path
import tempfile
import unittest

from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import DecodedStreamObject, NameObject

from book_pdf import check_pair, make_download


class DownloadPdfTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.cover, self.print_pdf, self.download = [self.root / n for n in
                                                    ['front.pdf', 'print.pdf', 'download.pdf']]
        cover = PdfWriter()
        cover.add_blank_page(width=432, height=4320 / 7)
        cover.write(self.cover)
        body = PdfWriter()
        for i in range(2):
            page = body.add_blank_page(width=504, height=720)
            stream = DecodedStreamObject()
            stream.set_data(f'{i} 0 m 100 100 l S'.encode())
            page[NameObject('/Contents')] = stream
        body.add_metadata({'/Title': 'Sample book', '/Author': 'Sample author'})
        body.add_named_destination('exercise.1', 1)
        body.add_outline_item('First chapter', 1)
        body.add_annotation(0, Link(rect=(10, 10, 50, 30), target_page_index=1))
        # Local PDF destinations refer to page objects, as pdfLaTeX does.
        body.pages[0]['/Annots'][0].get_object()['/Dest'][0] = body.pages[1].indirect_reference
        body.add_annotation(1, Link(rect=(10, 10, 50, 30), url='https://example.org'))
        body.set_page_label(0, 0, style='/r', start=1)
        body.set_page_label(1, 1, style='/D', start=1)
        body.write(self.print_pdf)

    def test_front_attachment_keeps_navigation_labels_and_original_file(self):
        original = self.print_pdf.read_bytes()
        make_download(self.cover, self.print_pdf, self.download)
        self.assertEqual(self.print_pdf.read_bytes(), original)
        self.assertEqual(check_pair(self.download, self.print_pdf), 2)
        book = PdfReader(self.download)
        self.assertEqual(book.page_labels, ['Cover', 'i', '1'])
        self.assertEqual(book.metadata.title, 'Sample book')
        self.assertEqual(book.metadata.author, 'Sample author')
        self.assertEqual(tuple(book.pages[0].mediabox), (0, 0, 504, 720))
        self.assertEqual(book.get_destination_page_number(book.outline[0]), 2)
        link = book.pages[1]['/Annots'][0].get_object()
        self.assertEqual(link['/Dest'][0], book.pages[2].indirect_reference)
        external = book.pages[2]['/Annots'][0].get_object()
        self.assertEqual(external['/A']['/URI'], 'https://example.org')

    def test_download_cannot_overwrite_print_file(self):
        with self.assertRaisesRegex(ValueError, 'separate'):
            make_download(self.cover, self.print_pdf, self.print_pdf)

    def test_coverless_download_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'one front cover'):
            check_pair(self.print_pdf, self.print_pdf)

    def test_changed_interior_is_rejected(self):
        make_download(self.cover, self.print_pdf, self.download)
        changed = PdfWriter(clone_from=self.download)
        stream = DecodedStreamObject()
        stream.set_data(b'0 0 m 500 500 l S')
        changed.pages[1][NameObject('/Contents')] = stream
        changed.write(self.root / 'changed.pdf')
        with self.assertRaisesRegex(ValueError, 'body differs'):
            check_pair(self.root / 'changed.pdf', self.print_pdf)

    def test_wrong_cover_proportions_are_rejected(self):
        cover = PdfWriter()
        cover.add_blank_page(width=432, height=691.2)
        cover.write(self.cover)
        with self.assertRaisesRegex(ValueError, 'aspect ratio'):
            make_download(self.cover, self.print_pdf, self.download)
