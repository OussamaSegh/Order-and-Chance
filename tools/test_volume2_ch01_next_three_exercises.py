"""Arithmetic and first-use regressions for three further Chapter 1 exercises.

Finite checks of floor inequalities, factorial divisibility, the minimal
prime factor obstruction, and lattice sum/intersection identities are
supporting evidence. The infinite claims require the printed and ledger
symbolic proofs.
"""
import math
import unittest
from fractions import Fraction
from pathlib import Path


CH1 = (Path(__file__).resolve().parents[1] / "volume2-integers"
       / "chapters" / "ch01-divisibility.tex")


def floor(x):
    return x.numerator // x.denominator


def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, r = divmod(a, b)
        a, b = b, r
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1
    return a, x0, y0


class TestChapterOneNextThreeExercises(unittest.TestCase):
    def test_supercatalan_floor_and_factorial_quotients(self):
        for a in range(-21, 22):
            for b in range(-21, 22):
                x, y = Fraction(a, 7), Fraction(b, 11)
                self.assertGreaterEqual(
                    floor(2*x)+floor(2*y),
                    floor(x)+floor(y)+floor(x+y),
                    (x, y))
        for m in range(42):
            for n in range(42):
                numer = math.factorial(2*m)*math.factorial(2*n)
                denom = (math.factorial(m)*math.factorial(n)
                         *math.factorial(m+n))
                with self.subTest(m=m, n=n):
                    self.assertEqual(numer % denom, 0)

    def test_2_to_n_minus_1_not_divisible_by_n(self):
        for n in range(2, 10001):
            with self.subTest(n=n):
                self.assertNotEqual(pow(2, n, n), 1 % n)
            if n % 2:
                p = next(p for p in range(3, n+1, 2)
                         if n % p == 0)
                # Any prime factor of p-1 would be smaller than p,
                # so it cannot divide n if p is n's least prime.
                self.assertEqual(math.gcd(n, p-1), 1)
                # The complete Fermat/binomial proof is symbolic:
                # its finite modular consequence is checked here.
                self.assertEqual(pow(2, p-1, p), 1)

    def test_divisor_lattice_sum_intersection_and_bezout(self):
        count = 0
        for a in range(1, 110):
            for b in range(1, 110):
                d, u, v = extended_gcd(a, b)
                self.assertEqual(d, math.gcd(a, b))
                self.assertEqual(a*u+b*v, d)
                l = a*b//d
                for t in range(-40, 41):
                    self.assertEqual(
                        t%a==0 and t%b==0,
                        t%l==0,
                        (a,b,t))
                count += 1
        self.assertEqual(count, 109**2)
        self.assertEqual(math.gcd(12,18), 6)
        self.assertEqual(math.lcm(12,18), 36)
        self.assertNotEqual(30%12, 0)
        self.assertNotEqual(30%18, 0)

    def test_exercise_hint_solution_contract(self):
        text = CH1.read_text(encoding="utf-8")
        for key in ("ex:supercat", "ex:n2n", "ex:t1-divisibility-lattice"):
            with self.subTest(key=key):
                self.assertEqual(text.count(r"\label{" + key + "}"), 1)
                self.assertEqual(text.count(r"\begin{hint}{" + key + "}"), 1)
                self.assertEqual(
                    text.count(r"\begin{solution}{" + key + "}"), 1)
        supercat = text.split(r"\begin{solution}{ex:supercat}",1)[1].split(
            r"\end{solution}",1)[0]
        n2n = text.split(r"\begin{solution}{ex:n2n}",1)[1].split(
            r"\end{solution}",1)[0]
        lattice = text.split(
            r"\begin{solution}{ex:t1-divisibility-lattice}",1
        )[1].split(r"\end{solution}",1)[0]
        self.assertIn(r"e_k\\ge0", supercat)
        self.assertIn(r"\gcd(n,p-1)", n2n)
        self.assertIn(r"\operatorname{lcm}(a,b)=ab/d", lattice)


if __name__ == "__main__":
    unittest.main()
