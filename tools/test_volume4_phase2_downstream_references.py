"""Volume 4 -> Volume 12 Brownian prerequisite regression.

Check the exact textbook contract, plus the independently derived dyadic
time-approximation argument. This is not a substitute for a mathematical
review of all later volumes.
"""
from pathlib import Path
from fractions import Fraction
from math import cos, sin, sqrt
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
V4 = ROOT / "volume4-chance" / "chapters" / "ch11-brownian.tex"
V12 = ROOT / "volume12-random-motion" / "chapters" / "ch02-paths.tex"


def left_dyadic_step(t, m):
    """Left endpoint of the dyadic strip containing a nonnegative time."""
    return (t * (1 << m)).numerator // (t * (1 << m)).denominator / (1 << m)


class TestVolume4DownstreamBrownianDependencies(unittest.TestCase):
    def test_missing_exercise_subparts_cannot_be_cited_as_proved_claims(self):
        source = V4.read_text(encoding="utf-8")
        downstream = V12.read_text(encoding="utf-8")
        section = source.split(r"\label{ex:zeros}", 1)[1].split(
            r"\end{exercise}", 1
        )[0]
        self.assertNotIn(r"\begin{enumerate}", section)
        self.assertNotIn("Exercise~12.3(a)", downstream)
        self.assertNotIn("Exercise~12.3(c)", downstream)
        self.assertIn("Exercise~12.3, where this consequence is proved", downstream)
        self.assertIn("First establish the joint measurability", downstream)
        self.assertIn(r"B^{(m)}(t,\omega)=B_{2^{-m}\lfloor 2^m t\rfloor}", downstream)
        self.assertIn("the pointwise limit is jointly measurable", downstream)

    def test_left_dyadic_approximation_on_exact_rational_times(self):
        # A constructive consequence of the displayed time-quantisation:
        # 0 <= t - floor(2^m*t)/2^m < 2^-m, including times not in [0,1].
        for t in (Fraction(0), Fraction(1, 3), Fraction(5, 7),
                  Fraction(1), Fraction(11, 9), Fraction(13, 4)):
            for m in range(1, 15):
                q = Fraction((t * (1 << m)).numerator //
                             (t * (1 << m)).denominator, 1 << m)
                self.assertLessEqual(q, t)
                self.assertLess(t-q, Fraction(1, 1 << m))
                self.assertEqual(left_dyadic_step(t, m), float(q))
                # Uniformly continuous deterministic paths obey exactly
                # the pathwise estimate the proof uses.
                self.assertLessEqual(abs(float(q)-float(t)), 2.0**-m)
                self.assertLessEqual(abs(sin(float(q))-sin(float(t))),
                                     2.0**-m + 1.e-14)

    def test_no_downstream_volume4_zero_set_phantom_subparts(self):
        # Scan every later-volume source, not just the repaired chapter.
        count = 0
        for root in ROOT.glob("volume*"):
            match = re.match(r"volume(\d+)(?:-|$)", root.name)
            if not match or int(match.group(1)) < 5:
                continue
            for path in (root / "chapters").glob("*.tex"):
                count += 1
                text = path.read_text(encoding="utf-8")
                self.assertIsNone(
                    re.search(r"Volume~4,\s*Exercise~12\.3\([a-z]\)", text),
                    f"{path} cites a nonexistent subsection of V4 ex:zeros"
                )
        self.assertGreater(count, 100)


if __name__ == "__main__":
    unittest.main()
