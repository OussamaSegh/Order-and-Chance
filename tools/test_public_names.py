"""Public naming is shared by shell builds, cache assembly and web downloads."""
from pathlib import Path
import tempfile
import unittest
from public_names import ROOT, SUFFIXES, filename, stem


class PublicNamesTest(unittest.TestCase):
    def test_complete_series_has_unique_readable_names(self):
        books = [p.parent.name for p in ROOT.glob('tome*/main.tex')]
        self.assertEqual(len(books), 16)
        names = [filename(book, kind) for book in books for kind in SUFFIXES]
        self.assertEqual(len(names), len(set(names)))
        self.assertTrue(all(' ' in name and not name.startswith('tome') for name in names))
        self.assertEqual(filename('tome0-mathematical-maturity', 'pdf'),
                         'Volume 0 - Mathematical Maturity.pdf')
        self.assertEqual(stem('tomeP1-crossroads'), 'Problem Book 1 - Crossroads')
        self.assertEqual(stem('tome14-order-and-chance'), 'Volume 14 - Order and Chance')

    def test_unsafe_title_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'tome0-test').mkdir()
            (root / 'tome0-test/main.tex').write_text('% epub-title: Series. Volume 0: Bad/Title\n')
            with self.assertRaises(ValueError):
                filename('tome0-test', 'pdf', root)
