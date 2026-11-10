"""Pin the Volume 11 repair of the phantom Volume 4 theorem number."""

import unittest
from pathlib import Path

SOURCE = (
    Path(__file__).resolve().parents[1]
    / "volume11-randomness"
    / "chapters"
    / "ch09-martingales.tex"
)


class TestVolume11PolyaCitation(unittest.TestCase):
    def test_de_finetti_example_cites_the_polya_theorem(self):
        text = SOURCE.read_text(encoding="utf-8")
        self.assertIn("Volume~4 (Theorem~11.13)", text)
        self.assertNotIn("Theorem~10.21", text)


if __name__ == "__main__":
    unittest.main()
