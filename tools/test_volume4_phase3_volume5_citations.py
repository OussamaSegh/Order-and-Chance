"""Pin the Volume 5 repair of the false Volume 4 monotone-convergence citation."""

import unittest
from pathlib import Path

SOURCE = (
    Path(__file__).resolve().parents[1]
    / "volume5-calculation"
    / "chapters"
    / "ch03-series.tex"
)


class TestVolume5RitelliCitation(unittest.TestCase):
    def test_odd_squares_are_not_credited_to_volume4_monotone_convergence(self):
        text = SOURCE.read_text(encoding="utf-8")
        self.assertNotIn("monotone convergence (Volume~4, Chapter~5)", text)
        self.assertIn(r"\int_0^1 s_N\to\frac{\pi^2}8", text)
        self.assertIn(r"2\delta-\delta^2\ge\delta", text)
        self.assertIn("Volume~7, Theorem~9.5", text)
        self.assertNotIn("By Tonelli,", text)


if __name__ == "__main__":
    unittest.main()
