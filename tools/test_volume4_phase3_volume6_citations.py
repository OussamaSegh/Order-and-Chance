"""Pins for the Volume 6 citation repairs proposed in Phase 3.

These checks do not prove the Chernoff estimate. They keep the false
Volume 4 theorem number from returning, and they check the two elementary
inequalities used in the repaired solution of ex:shortmodel.
"""

import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "volume6-crossroads" / "chapters" / "ch10-random.tex"


class TestVolume6Phase3Citations(unittest.TestCase):
    def test_short_interval_solution_does_not_cite_phantom_theorems(self):
        text = SOURCE.read_text(encoding="utf-8")
        self.assertIn("Theorem~2.1", text)
        self.assertNotIn("Theorem~2.11", text)
        self.assertNotIn("Chernoff's bounds (Volume~4, Chapter~4)", text)
        self.assertIn(r"2e^{-\delta^2\mu_N/3}", text)
        self.assertIn("It is not Hoeffding's inequality", text)

    def test_relative_entropy_lower_bounds_used_in_the_solution(self):
        for step in range(1, 1001):
            delta = step / 1000
            upper = (1 + delta) * math.log(1 + delta) - delta - delta * delta / 3
            self.assertGreaterEqual(upper, -1e-12)
            if delta < 1:
                lower = (
                    delta
                    + (1 - delta) * math.log(1 - delta)
                    - delta * delta / 2
                )
                self.assertGreaterEqual(lower, -1e-12)


if __name__ == "__main__":
    unittest.main()
