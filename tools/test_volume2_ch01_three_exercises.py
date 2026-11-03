"""Independent finite probes for three elementary Chapter 1 solutions.

Every general theorem is established in the manuscript and proof ledger.
Tests use different routes: integer arithmetic and prime divisibility for
rational roots, direct gcds versus exponent identities, and a residue-class
coin computation rather than the manuscript's canonical x-in-[0,b) proof.
"""
import math
import unittest
from pathlib import Path


CH1 = (Path(__file__).resolve().parents[1] / "volume2-integers"
       / "chapters" / "ch01-divisibility.tex")


def largest_coin_gap_by_residues(a, b):
    """For each residue modulo a choose the least nonnegative multiple of b."""
    minima = {}
    for y in range(a):
        value = b*y
        minima[value % a] = value
    assert len(minima) == a
    return max(value-a for value in minima.values())


def smallest_common_mersenne_via_factor(a, b):
    d = math.gcd(a, b)
    value = 2**d-1
    # The divisibility (2^d-1) | (2^(dm)-1) comes from a finite
    # geometric sum. Test it directly as a second inclusion.
    assert (2**a-1) % value == 0
    assert (2**b-1) % value == 0
    return value


class TestChapterOneThreeExercises(unittest.TestCase):
    def test_rational_roots_of_integer_monic_polynomials(self):
        # A reduced nonintegral p/q cannot solve a monic integral
        # polynomial: reducing q^d P(p/q)=0 mod a prime dividing q
        # leaves p^d != 0. Exercise this with independent finite probes.
        for d in range(1, 6):
            for p in range(-9, 10):
                for q in range(2, 10):
                    if math.gcd(p, q) != 1:
                        continue
                    # For any integral coefficients, equality would
                    # require p^d divisible by q. This cannot happen.
                    self.assertNotEqual(p**d % q, 0)
                    for c in (-3, -1, 0, 1, 3):
                        # P(X)=X^d + c X^(d-1) + (2-c).
                        numerator = p**d + c*p**(d-1)*q + (2-c)*q**d
                        self.assertNotEqual(numerator, 0)
        for n in range(0, 2001):
            root = math.isqrt(n)
            # n is a square precisely when every valuation is even.
            value = n
            odd_val = False
            for prime in range(2, math.isqrt(n)+2):
                if value <= 1:
                    break
                if any(prime%d == 0 for d in range(2, math.isqrt(prime)+1)):
                    continue
                exponent = 0
                while value % prime == 0:
                    value //= prime
                    exponent += 1
                odd_val |= bool(exponent % 2)
            if value > 1:
                odd_val = True
            self.assertEqual(root*root == n, not odd_val, n)

    def test_mersenne_gcd_and_second_divisibility_inclusion(self):
        tested = 0
        for a in range(1, 121):
            for b in range(1, 121):
                expected = smallest_common_mersenne_via_factor(a, b)
                actual = math.gcd(2**a - 1, 2**b - 1)
                self.assertEqual(actual, expected, (a, b))
                tested += 1
        self.assertEqual(tested, 14400)

    def test_coin_formula_including_unit_denomination(self):
        cases = 0
        for a in range(1, 55):
            for b in range(1, 55):
                if math.gcd(a, b) != 1:
                    continue
                f = a*b-a-b
                self.assertEqual(largest_coin_gap_by_residues(a,b), f)
                # Enumerate nonnegative combinations through a safe
                # upper bound, independently of the residue proof.
                max_n = a*b+a+b+1
                can = [False] * (max_n+1)
                for x in range(max_n//a+1):
                    for y in range((max_n-a*x)//b+1):
                        can[a*x+b*y] = True
                if f >= 0:
                    self.assertFalse(can[f])
                else:
                    self.assertEqual(f, -1)
                    self.assertTrue(a == 1 or b == 1)
                self.assertTrue(all(can[n] for n in range(max(0, f+1),
                                                         max_n+1)))
                cases += 1
        self.assertGreater(cases, 1500)

    def test_exercises_hints_and_solutions_stay_aligned(self):
        source = CH1.read_text(encoding="utf-8")
        for key in ("ex:sqrt", "ex:mersgcd", "ex:frob"):
            self.assertEqual(source.count(r"\label{" + key + "}"), 1)
            self.assertEqual(source.count(r"\begin{hint}{" + key + "}"), 1)
            self.assertEqual(source.count(r"\begin{solution}{" + key + "}"), 1)
        sqrt_solution = source.split(r"\begin{solution}{ex:sqrt}", 1)[1].split(
            r"\end{solution}", 1)[0]
        mers_solution = source.split(r"\begin{solution}{ex:mersgcd}", 1)[1].split(
            r"\end{solution}", 1)[0]
        frob_solution = source.split(r"\begin{solution}{ex:frob}", 1)[1].split(
            r"\end{solution}", 1)[0]
        self.assertIn(r"\gcd(p,q)=1", sqrt_solution)
        self.assertIn(r"2^{\gcd(a,b)}-1", mers_solution)
        self.assertIn("If $a=1$ or $b=1$", frob_solution)


if __name__ == "__main__":
    unittest.main()
