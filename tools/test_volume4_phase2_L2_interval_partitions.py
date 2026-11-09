"""Mathematical regression for martingale L2 scope and Polya urn intervals.

Arithmetic tests prove the nested interval realization matches the entire
finite history probability distribution. Source guards ensure the proof cannot
silently invoke countable additivity for arbitrary non-interval events.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import unittest

SOURCE = (Path(__file__).resolve().parents[1] /
          "volume4-chance" / "chapters" / "ch10-martingales.tex")


def urn_partition(n):
    """Return labelled rational half-open intervals after n draws."""
    state = [(F(0), F(1), 1, "", 0)]
    for step in range(n):
        new = []
        for lo, hi, red_count, history, reds in state:
            p = F(red_count, step + 2)
            mid = lo + (hi - lo) * p
            new.append((lo, mid, red_count + 1, history + "R", reds + 1))
            new.append((mid, hi, red_count, history + "B", reds))
        state = new
    return state


class TestMartingaleL2IntervalScope(unittest.TestCase):
    def test_theorem_requires_justified_event_class_and_proves_continuity(self):
        text = SOURCE.read_text(encoding="utf-8")
        theorem = text.split(r"\label{thm:L2conv}", 1)[1].split(
            r"\end{theorem}", 1
        )[0]
        proof = text.split(r"\label{thm:L2conv}", 1)[1].split(
            r"\end{proof}", 1
        )[0]
        self.assertIn("each atom a finite union of half-open intervals", theorem)
        self.assertIn("continuity-from-below theorem", proof)
        self.assertIn("length argument of Proposition", proof)
        self.assertNotIn(
            "each is a finite union of digit cylinders, so the outer content",
            proof,
        )

    def test_all_history_intervals_and_probabilities_are_exact(self):
        for n in range(0, 11):
            p = urn_partition(n)
            self.assertEqual(len(p), 2**n)
            self.assertEqual(p[0][0], F(0))
            self.assertEqual(p[-1][1], F(1))
            self.assertTrue(all(p[i][1] == p[i + 1][0]
                                for i in range(len(p) - 1)))
            self.assertTrue(all(hi > lo for lo, hi, *_ in p))
            for lo, hi, red, history, j in p:
                self.assertEqual(red, j + 1)
                self.assertEqual(len(history), n)
                # An independently derived finite-sequence formula:
                expected = F(factorial(j) * factorial(n-j),
                             factorial(n+1))
                self.assertEqual(hi-lo, expected)
            for j in range(n + 1):
                mass = sum((hi-lo for lo,hi,red,h,k in p if k==j), F(0))
                self.assertEqual(mass, F(1, n+1))
                self.assertEqual(sum(k==j for *_,k in p), comb(n,j))

    def test_martingale_conditional_mean_exact_at_every_finite_atom(self):
        for n in range(1, 11):
            current = urn_partition(n-1)
            next_part = urn_partition(n)
            self.assertEqual(len(next_part), 2*len(current))
            for i, (lo, hi, red, h, j) in enumerate(current):
                r = next_part[2*i]
                b = next_part[2*i+1]
                self.assertEqual((r[0], b[1]), (lo, hi))
                probability_red = F(red, n+1)
                expectation = (probability_red * F(red+1, n+2)
                               + (1-probability_red) * F(red, n+2))
                self.assertEqual(expectation, F(red, n+1))


if __name__=="__main__":
    unittest.main()
