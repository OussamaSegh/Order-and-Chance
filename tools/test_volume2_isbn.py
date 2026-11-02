"""ISBN and barcode regression guard for Volume 2's paperback edition."""
from pathlib import Path
import re
import unittest

from ean13 import check_digit, modules

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ISBN = "9798167208650"


class Volume2PaperbackIsbnTest(unittest.TestCase):
    def test_paperback_isbn_is_valid_and_encodable(self):
        source = (ROOT / "volume2-integers" / "main.tex").read_text(encoding="utf-8")
        found = re.search(r"^\\renewcommand\{\\bookisbnprint\}\{([0-9]{13})\}$", source, re.MULTILINE)
        self.assertIsNotNone(found, "Set the paperback ISBN in main.tex")
        isbn = found.group(1)
        self.assertEqual(isbn, EXPECTED_ISBN)
        self.assertEqual(check_digit(isbn[:12]), int(isbn[-1]))
        bits = modules(isbn)
        self.assertEqual(len(bits), 95)
        self.assertTrue(bits.startswith("101"))
        self.assertEqual(bits[45:50], "01010")
        self.assertTrue(bits.endswith("101"))


if __name__ == "__main__":
    unittest.main()
