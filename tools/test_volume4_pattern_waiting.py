"""Independent finite-state audits for printed Volume 4 Chapter 11.

The exact absorbing prefix automaton is mathematically separate from the
casino/optional-stopping proof. It does not verify unsampled martingale claims.

Run: python3 -m unittest discover -s tools -p test_volume4_pattern_waiting.py
"""

from fractions import Fraction
from itertools import product
from pathlib import Path
import unittest


MARTINGALES = (
    Path(__file__).resolve().parents[1]
    / "volume4-chance"
    / "chapters"
    / "ch10-martingales.tex"
)


def matched_prefix_length(pattern, current_length, new_letter):
    """Length of the longest pattern prefix suffix of a new observed word."""
    observed = pattern[:current_length] + new_letter
    for size in range(min(len(pattern), len(observed)), -1, -1):
        if observed.endswith(pattern[:size]):
            return size
    raise AssertionError("Empty prefix must match")


def exact_expected_wait(pattern, alphabet):
    """Solve exact E_i=1+mean(E_next) with E_absorbed=0 using fractions.

    State i records the longest suffix matching a length-i prefix. For a new
    symbol the state follows the prefix automaton. The full-pattern state
    is absorbing. This is not the casino martingale/overlap argument.
    """
    m = len(pattern)
    if not pattern or not set(pattern) <= set(alphabet):
        raise ValueError("Pattern needs letters from a nonempty alphabet")
    if len(alphabet) != len(set(alphabet)):
        raise ValueError("Alphabet must contain distinct equally likely symbols")

    # Augmented linear system: (I-Q) E = 1 over rational numbers.
    matrix = []
    for state in range(m):
        row = [Fraction(int(state == j)) for j in range(m)] + [Fraction(1)]
        for letter in alphabet:
            new_state = matched_prefix_length(pattern, state, letter)
            if new_state < m:
                row[new_state] -= Fraction(1, len(alphabet))
        matrix.append(row)

    for pivot_col in range(m):
        pivot = next(
            row for row in range(pivot_col, m)
            if matrix[row][pivot_col] != 0
        )
        matrix[pivot_col], matrix[pivot] = matrix[pivot], matrix[pivot_col]
        factor = matrix[pivot_col][pivot_col]
        matrix[pivot_col] = [entry / factor for entry in matrix[pivot_col]]
        for row in range(m):
            if row != pivot_col:
                factor = matrix[row][pivot_col]
                matrix[row] = [
                    entry - factor * chosen
                    for entry, chosen in zip(matrix[row], matrix[pivot_col])
                ]
    return matrix[0][-1]


class TestVolume4WaitingTimeAndStopping(unittest.TestCase):
    def test_abra_pattern_expectation_from_exact_prefix_chain(self):
        pattern = "ABRACADABRA"
        expected = exact_expected_wait(pattern, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(expected, 3670344487444778)
        self.assertEqual(expected, 26**11 + 26**4 + 26)
        src = MARTINGALES.read_text(encoding="utf-8")
        theorem = src.split(r"\label{thm:monkey}", 1)[1].split(
            r"\end{theorem}", 1
        )[0]
        self.assertIn("3670344487444778", theorem)
        self.assertIn(r"26^{11}+26^4+26", theorem)

    def test_binary_short_pattern_waits_from_separate_linear_systems(self):
        # H and T form an equiprobable two-symbol alphabet. HT and TH
        # have no proper border; HH and TT have a one-symbol border.
        for pattern, expected in {
            "H": 2, "T": 2,
            "HT": 4, "TH": 4, "HH": 6, "TT": 6,
            "HTH": 10, "HHH": 14, "HTT": 8
        }.items():
            with self.subTest(pattern=pattern):
                self.assertEqual(
                    exact_expected_wait(pattern, "HT"), Fraction(expected)
                )

    def test_anticipating_clock_fails_time_zero_measurability(self):
        src = MARTINGALES.read_text(encoding="utf-8")
        definition = src.split(r"\label{def:stopping}", 1)[1].split(
            r"\end{definition}", 1
        )[0]
        self.assertIn(r"\emph{random time}", definition)
        self.assertIn(r"\{\tau\le0\}=\{X_1=-1\}", definition)
        self.assertNotIn("declare the stopping time to be", definition)

        # At time zero, F_0={empty, full}. The event
        # {tau<=0} is exactly {one-step sign=-1}, probability 1/2,
        # neither empty nor full, so the clock is anticipative.
        sample_space = (+1, -1)
        tau = {sign: (1 if sign > 0 else 0) for sign in sample_space}
        early = frozenset(sign for sign in sample_space if tau[sign] <= 0)
        sigma_zero = {frozenset(), frozenset(sample_space)}
        self.assertEqual(early, frozenset((-1,)))
        self.assertNotIn(early, sigma_zero)
        self.assertEqual(Fraction(len(early), len(sample_space)), Fraction(1, 2))


if __name__ == "__main__":
    unittest.main()
