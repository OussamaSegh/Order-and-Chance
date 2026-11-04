"""Finite corroboration of DEP-029's symbolic Chapter 4 audits.

Divisor and word enumeration provide checks independent of the printed
prime-power formulas. These samples cannot certify the universal proofs.
"""

from fractions import Fraction
from itertools import product
from math import gcd, isqrt, log, pi, prod, sqrt
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "volume2-integers/chapters/ch04-arithmetic-functions.tex"
EXERCISES = (
    "ex:sigmaodd", "ex:coprimesum", "ex:even", "ex:oddperfect",
    "ex:primitive", "ex:coprimeprob", "ex:t1-mu12",
)


def mobius(n):
    sign = 1
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
    return -sign if n > 1 else sign


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def primitive(word):
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d)
                   for d in range(1, n))


class TestChapterFourPerfectPeriodsDensity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Enumerate every divisor by a sieve, not by prime-power formulas.
        cls.tau = [0] * 5001
        cls.sigma = [0] * 5001
        for d in range(1, 5001):
            for n in range(d, 5001, d):
                cls.tau[n] += 1
                cls.sigma[n] += d

    def test_odd_divisor_sums_including_one_and_two(self):
        for n in range(1, 5001):
            square_or_twice = isqrt(n) ** 2 == n or (
                n % 2 == 0 and isqrt(n // 2) ** 2 == n // 2)
            self.assertEqual(self.sigma[n] % 2 == 1, square_or_twice, n)
        self.assertEqual([self.sigma[n] for n in (1, 2, 12, 18)],
                         [1, 3, 28, 39])

    def test_coprime_sum_by_enumeration_and_divisor_inversion(self):
        for n in range(2, 501):
            units = [k for k in range(1, n + 1) if gcd(k, n) == 1]
            self.assertEqual(2 * sum(units), n * len(units), n)
            inverted = sum(mobius(d) * d * (n // d) * (n // d + 1) // 2
                           for d in range(1, n + 1) if n % d == 0)
            self.assertEqual(sum(units), inverted, n)
        self.assertEqual(sum(k for k in range(1, 2) if gcd(k, 1) == 1), 1)

    def test_even_perfect_classification_and_false_mersenne_converse(self):
        actual = [n for n in range(2, 5001, 2) if self.sigma[n] == 2*n]
        expected = [2**(p-1) * (2**p-1) for p in range(2, 13)
                    if prime(2**p-1) and 2**(p-1)*(2**p-1) <= 5000]
        self.assertEqual(actual, expected)
        self.assertEqual(actual, [6, 28, 496])
        for p in (2, 3, 5, 7, 13, 17, 19, 31):
            n = 2**(p-1) * (2**p-1)
            self.assertIn(n % 10, (6, 8))
        # A prime exponent does not guarantee that its Mersenne number is prime.
        self.assertEqual(2**11 - 1, 23 * 89)
        n = 2**10 * 23 * 89
        self.assertNotEqual((2**11-1) * 24 * 90, 2*n)

    def test_two_odd_prime_factor_ratio_bound_exactly(self):
        ps = [p for p in range(3, 32) if prime(p)]
        for i, p in enumerate(ps):
            for q in ps[i+1:]:
                for a in range(1, 5):
                    for b in range(1, 5):
                        reciprocal_sum = sum(
                            (Fraction(1, p**j * q**k)
                             for j in range(a+1) for k in range(b+1)),
                            Fraction(0))
                        upper = Fraction(p, p-1) * Fraction(q, q-1)
                        self.assertLess(reciprocal_sum, upper)
                        self.assertLessEqual(upper, Fraction(15, 8))

    def test_primitive_words_and_unique_cyclic_period_by_exhaustion(self):
        for q, last_n in ((1, 10), (2, 10), (3, 8)):
            for n in range(1, last_n + 1):
                count = 0
                for word in product(range(q), repeat=n):
                    roots = [word[:d] for d in range(1, n+1)
                             if n % d == 0
                             and word == word[:d] * (n // d)
                             and primitive(word[:d])]
                    self.assertEqual(len(roots), 1, word)
                    periods = [h for h in range(1, n+1)
                               if word[h:] + word[:h] == word]
                    g = min(periods)
                    self.assertEqual(n % g, 0)
                    self.assertTrue(all(h % g == 0 for h in periods))
                    self.assertEqual(g, len(roots[0]))
                    count += primitive(word)
                predicted = sum(mobius(d) * q**(n//d)
                                for d in range(1, n+1) if n % d == 0)
                self.assertEqual(count, predicted, (q, n))
        self.assertEqual(sum(primitive(w) for w in product(range(2), repeat=4)), 12)

    def test_real_hyperbola_counts_at_squares_and_fractional_boundaries(self):
        prefix = [0]
        for t in self.tau[1:]:
            prefix.append(prefix[-1] + t)
        values = {Fraction(r, 4) for r in range(4, 4001)}
        values.update(Fraction(m*m) + offset
                      for m in range(2, 70)
                      for offset in (Fraction(-1, 4), Fraction(0), Fraction(1, 4)))
        gamma = 0.5772156649015329
        for x in sorted(values):
            m = isqrt(x.numerator // x.denominator)
            strips = 2 * sum(x // a for a in range(1, m+1)) - m*m
            # Independently count by the smaller coordinate, subtracting its
            # diagonal point once; each off-diagonal point has a reflected mate.
            shells = sum(2 * (x // a - a) + 1 for a in range(1, m+1))
            self.assertEqual(strips, prefix[int(x)], x)
            self.assertEqual(shells, prefix[int(x)], x)
            main = float(x) * log(float(x)) + (2*gamma - 1) * float(x)
            self.assertLessEqual(abs(prefix[int(x)] - main), 6*sqrt(float(x)), x)
        self.assertEqual(prefix[10], 27)
        self.assertEqual(prefix[30], 111)
        # Subtracting only the diagonal instead of the square is false.
        self.assertNotEqual(2 * sum(10 // a for a in range(1, 4)) - 3, prefix[10])

    def test_harmonic_remainder_bound_used_in_hyperbola_proof(self):
        gamma = 0.5772156649015329
        h = 0.
        for m in range(1, 5001):
            h += 1/m
            self.assertLessEqual(h - log(m+1), gamma + 1e-12)
            self.assertLessEqual(gamma, h - log(m) + 1e-12)
            self.assertLessEqual(h - log(m) - gamma, 1/m + 1e-12)

    def test_coprime_square_counts_and_signed_tail_error_exactly(self):
        count = 0
        harmonic = Fraction(0)
        for n in range(1, 251):
            count += (1 if n == 1 else
                      2 * sum(gcd(k, n) == 1 for k in range(1, n)))
            harmonic += Fraction(1, n)
            exact_floor = sum(mobius(d) * (n // d)**2 for d in range(1, n+1))
            self.assertEqual(count, exact_floor, n)
            mu_partial = sum((Fraction(mobius(d), d*d) for d in range(1, n+1)),
                             Fraction(0))
            self.assertLessEqual(abs(Fraction(count, n*n) - mu_partial),
                                 2*harmonic/n)
            self.assertLessEqual(abs(count/(n*n) - 6/(pi*pi)),
                                 float((2*harmonic + 1)/n))
        self.assertEqual(sum(gcd(a, b) == 1 for a in range(1, 13)
                             for b in range(1, 13)), 91)

    def test_grouped_product_cancellation_uses_finite_sums(self):
        # Group by dm and explicitly enumerate each coefficient; no zeta or
        # Euler-product library is used to obtain the expected constant 1.
        for t in (1, 2, 7, 30, 100):
            total = sum((Fraction(mobius(d), (d*m)**2)
                         for d in range(1, t+1)
                         for m in range(1, t//d + 1)), Fraction(0))
            self.assertEqual(total, 1, t)

    def test_finite_prime_exclusion_density_by_residue_enumeration(self):
        for ps in ((2,), (2, 3), (2, 3, 5), (2, 3, 5, 7)):
            modulus = prod(ps)
            actual = sum(gcd(gcd(a, b), modulus) == 1
                         for a in range(modulus) for b in range(modulus))
            expected = prod(p*p-1 for p in ps)
            self.assertEqual(actual, expected, ps)

    def test_four_mobius_examples_by_explicit_divisors(self):
        actual = [sum(mobius(d) for d in range(1, n+1) if n % d == 0)
                  for n in (1, 6, 12, 30)]
        self.assertEqual(actual, [1, 0, 0, 0])

    def test_complete_chapter_structure_and_no_hidden_cyclic_subgroup_step(self):
        source = SOURCE.read_text(encoding="utf-8")
        for key in EXERCISES:
            self.assertEqual(source.count(r"\label{" + key + "}"), 1)
            self.assertEqual(source.count(r"\begin{hint}{" + key + "}"), 1)
            self.assertEqual(source.count(r"\begin{solution}{" + key + "}"), 1)
        for env in ("exercise", "hint", "solution"):
            self.assertEqual(len(re.findall(r"\\begin\{" + env + r"\}", source)), 10)
            self.assertEqual(source.count(r"\end{" + env + "}"), 10)
        body = source.split(r"\begin{solution}{ex:primitive}")[1].split(
            r"\end{solution}")[0]
        self.assertNotIn(r"\Z/n\Z", body)
        self.assertIn("remainder", body)
        self.assertIn("period", body)
        self.assertNotIn("subtract the diagonal contribution", source)
        for paragraph in re.split(r"\n\s*\n", source):
            text = re.sub(r"(?<!\\)%[^\n]*", "", paragraph)
            self.assertEqual(len(re.findall(r"(?<!\\)\$", text)) % 2, 0,
                             paragraph[:160])


if __name__ == "__main__":
    unittest.main()
