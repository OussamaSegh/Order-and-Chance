"""Finite probes for the elementary largest-prime-factor Journey in Chapter 4.

The stronger P(x)>x result is NOT claimed or imported. The book now proves
for each fixed 0<delta<1 that P(x)>x^(1-delta) eventually, from earlier tools.
Tests check small concrete cases and the crucial prime-power root bound,
but only the argument in the manuscript can prove the asymptotic statement.
"""
import math
import re
import unittest
from pathlib import Path


CH4 = Path(__file__).resolve().parents[1] / "volume2-integers" / "chapters" / "ch04-arithmetic-functions.tex"


def prime_factors(n):
    ans = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans.append(n)
    return ans


class TestVolume2PrimeFactorBound(unittest.TestCase):
    def test_problem_and_solution_do_not_import_volume_six(self):
        source = CH4.read_text(encoding="utf-8")
        exercise = re.search(
            r"\\begin\{exercise\}\[\$\\star\\star\\star\$\]"
            r"\\label\{pb:nsq1\}([\s\S]*?)\\end\{exercise\}", source
        )
        hint = re.search(
            r"\\begin\{hint\}\{pb:nsq1\}([\s\S]*?)\\end\{hint\}", source
        )
        sol = re.search(
            r"\\begin\{solution\}\{pb:nsq1\}([\s\S]*?)\\end\{solution\}", source
        )
        self.assertIsNotNone(exercise)
        self.assertIsNotNone(hint)
        self.assertIsNotNone(sol)
        required = exercise.group(1) + hint.group(1) + sol.group(1).split(
            r"\leads", 1
        )[0]
        self.assertNotIn("The solution requires a quantitative theorem", required)
        self.assertNotIn(r"Volume~6 (", required)
        self.assertNotIn(r"Dirichlet's theorem and its quantitative consequence", required)
        self.assertIn("Chebyshev", required)
        self.assertIn(r"x^{1-\delta}", required)
        self.assertIn(r"\pi(y)=O(y/\log y)", required)

    def test_odd_prime_powers_have_at_most_two_sqrt_minus_one_roots(self):
        for p in (3, 5, 7, 11, 13, 17, 19):
            for power in (1, 2, 3):
                m = p**power
                if m > 15000:
                    continue
                roots = [x for x in range(m) if (x*x+1) % m == 0]
                self.assertLessEqual(len(roots), 2)
                for x in roots:
                    self.assertIn((-x) % m, roots)

    def test_large_prime_factor_illustrative_finite_ranges(self):
        big = 0
        for n in range(1, 401):
            big = max(big, max(prime_factors(n*n+1)))
            if n >= 25:
                for delta in (0.2, 0.5, 0.8):
                    self.assertGreater(big, n**(1-delta))


if __name__ == "__main__":
    unittest.main()
