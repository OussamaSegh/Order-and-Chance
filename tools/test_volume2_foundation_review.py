"""Independent finite regression probes for first-volume handoff into Volume 2.

These computations test examples and edge cases. The proofs remain in the
manuscript and must be checked symbolically, independently of these tests.
"""
import math
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "volume2-integers" / "chapters"


def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def euclid_steps(a, b):
    count = 0
    while b:
        a, b = b, a % b
        count += 1
    return count


class TestVolume2FoundationReview(unittest.TestCase):
    def test_first_four_independent_integer_exercise_checks(self):
        div = (CHAPTERS / "ch01-divisibility.tex").read_text()
        for label in ("ex:bez", "ex:gcdn", "ex:zeros", "ex:lame5"):
            self.assertIn(r"\label{" + label + "}", div)
            self.assertIn(r"\begin{hint}{" + label + "}", div)
            self.assertIn(r"\begin{solution}{" + label + "}", div)

        # Complete family for 91x + 35y = 7, including negative x.
        for x in range(-200, 201):
            numerator = 7 - 91 * x
            if numerator % 35 == 0:
                t, remainder = divmod(x - 2, 5)
                self.assertEqual(remainder, 0)
                self.assertEqual(numerator // 35, -5 - 13 * t)
        for t in range(-80, 81):
            x, y = 2 + 5*t, -5 - 13*t
            self.assertEqual(91*x + 35*y, 7)

        # Gcd identity includes n=0 and all residue classes modulo 5.
        for n in range(0, 10001):
            want = 5 if n % 5 == 2 else 1
            self.assertEqual(
                math.gcd(n*n + 1, (n+1)*(n+1) + 1), want
            )

        # Independent prime-layer computation for 1000! trailing zeros.
        def valuation(n, p):
            count = 0
            while n:
                n //= p
                count += n
            return count
        self.assertEqual(valuation(1000, 5), 249)
        self.assertEqual(valuation(1000, 2), 994)

    def test_lame_division_bound_for_every_small_positive_pair(self):
        fib = [0, 1]
        for _ in range(20):
            fib.append(fib[-1] + fib[-2])
        for a in range(2, 201):
            for b in range(1, a):
                n = euclid_steps(a, b)
                self.assertGreaterEqual(b, fib[n+1])
                self.assertGreaterEqual(a, fib[n+2])
                digits = len(str(b))
                self.assertLessEqual(n, 5*digits)

    def test_euclid_and_euler_prime_probes(self):
        src = (CHAPTERS / "ch02-primes.tex").read_text()
        self.assertIn(r"\label{thm:euclid-primes}", src)
        self.assertIn(r"\label{thm:euler}", src)
        self.assertEqual(2*3*5*7*11*13 + 1, 59*509)
        self.assertTrue(prime(59) and prime(509))
        self.assertEqual(math.factorial(5) + 1, 11**2)

        # Bound is valid at every tested x, but finiteness never proves it.
        total = 0.
        for x in range(2, 10001):
            if prime(x):
                total += 1/x
            self.assertGreaterEqual(total + 1e-12, math.log(math.log(x)) - 1)


if __name__ == "__main__":
    unittest.main()
