"""An assigned paperback ISBN must reach the listing without inventing an eBook ISBN."""
from pathlib import Path
import tempfile
import unittest

import listing


class ListingIsbnTest(unittest.TestCase):
    def make_listing(self, assigned):
        with tempfile.TemporaryDirectory() as directory:
            book = Path(directory)
            source = '% epub-title: Order and Chance. Volume 3: Symmetry\n'
            if assigned is not None:
                source += '\\renewcommand{\\bookisbnprint}{' + assigned + '}\n'
            (book / 'main.tex').write_text(source)
            output = book / 'listing.md'
            listing.main(str(book), str(output))
            return output.read_text()

    def test_assigned_paperback_and_unassigned_editions(self):
        text = self.make_listing('9798167514683')
        self.assertIn('| Paperback ISBN | 9798167514683 |', text)
        self.assertNotIn('eBook ISBN', text)
        self.assertNotIn('Paperback ISBN', self.make_listing(None))

    def test_invalid_assignment_is_rejected(self):
        for isbn in ('9798167514684', '123', '4006381333931'):
            with self.subTest(isbn=isbn), self.assertRaises(SystemExit):
                self.make_listing(isbn)
