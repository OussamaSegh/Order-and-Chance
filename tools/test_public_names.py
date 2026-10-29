"""Public naming is shared by shell builds, cache assembly and web downloads."""
from pathlib import Path
import tempfile
import unittest
from public_names import ROOT, SUFFIXES, filename, stem


class PublicNamesTest(unittest.TestCase):
    def test_complete_series_has_unique_readable_names(self):
        books = [p.parent.name for p in ROOT.glob('volume*/main.tex')]
        self.assertEqual(len(books), 15)
        names = [filename(book, kind) for book in books for kind in SUFFIXES]
        self.assertEqual(len(names), len(set(names)))
        self.assertTrue(all(' ' in name and not name.startswith('volume') for name in names))
        self.assertEqual(filename('volume1-first-principles', 'pdf'),
                         'Volume 1 - First Principles.pdf')
        self.assertEqual(stem('volume15-order-and-chance'), 'Volume 15 - Order and Chance')
        self.assertEqual(stem('volume6-crossroads'), 'Volume 6 - Crossroads')

    def test_unsafe_title_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'volume0-test').mkdir()
            (root / 'volume0-test/main.tex').write_text('% epub-title: Series. Volume 0: Bad/Title\n')
            with self.assertRaises(ValueError):
                filename('volume0-test', 'pdf', root)
