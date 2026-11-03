"""Finite arithmetic regression cases for Volume 2.

These tests check small examples and theorem boundary cases only.
They do not replace mathematical proofs or editorial review.
Run: python3 -m unittest discover -s tools -p 'test_volume2_*.py'
"""
import math
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "volume2-integers" / "chapters"


def primes_up_to(limit):
    return [
        n for n in range(2, limit + 1)
        if all(n % d != 0 for d in range(2, math.isqrt(n) + 1))
    ]


def totient(n):
    return sum(math.gcd(k, n) == 1 for k in range(1, n + 1))


def quadratic_character(a, p):
    x = pow(a % p, (p - 1) // 2, p)
    return 0 if x == 0 else (1 if x == 1 else -1)


def two_square_representations(n):
    bound = math.isqrt(n)
    return sum(
        x * x + y * y == n
        for x in range(-bound, bound + 1)
        for y in range(-bound, bound + 1)
    )


class TestVolume2ArithmeticSanity(unittest.TestCase):
    def test_fermat_quotient_odd_prime_domain_and_lerch(self):
        source = (CHAPTERS / "ch14-characters.tex").read_text(encoding="utf-8")
        exercise = source.split(r"\label{pb:fermatquot}", 1)[1].split(
            r"\end{exercise}", 1
        )[0]
        self.assertIn("For an odd prime", exercise)
        for p in primes_up_to(79):
            quotient_sum = sum(
                ((pow(a, p - 1, p * p) - 1) // p) for a in range(1, p)
            ) % p
            factorial = math.factorial(p - 1)
            wilson_quotient = ((factorial + 1) // p) % p
            if p == 2:
                self.assertNotEqual(
                    quotient_sum, wilson_quotient,
                    "Lerch's congruence is invalid at the excluded prime 2",
                )
            else:
                with self.subTest(p=p):
                    self.assertEqual(quotient_sum, wilson_quotient)

    def test_hensel_exercise_contains_both_lifts(self):
        source = (CHAPTERS / "ch03-congruences.tex").read_text(encoding="utf-8")
        exercise = source.split(r"\label{ex:hensel}", 1)[1].split(
            r"\end{exercise}", 1
        )[0]
        solution = source.split(r"\begin{solution}{ex:hensel}", 1)[1].split(
            r"\end{solution}", 1
        )[0]
        self.assertIn(r"\emph{all}", exercise)
        roots = [x for x in range(125) if (x * x + 1) % 125 == 0]
        self.assertEqual(roots, [57, 68])
        self.assertIn(r"\{57,68\}", solution)
        for root_mod5 in (2, 3):
            lifts = [x for x in roots if x % 5 == root_mod5]
            self.assertEqual(len(lifts), 1)

    def test_two_square_criterion_and_jacobi_counts(self):
        for n in range(1, 151):
            r2 = two_square_representations(n)
            divisor_sum = sum(
                (1 if d % 4 == 1 else -1)
                for d in range(1, n + 1)
                if n % d == 0 and d % 2 == 1
            )
            with self.subTest(n=n):
                self.assertEqual(r2, 4 * divisor_sum)
            factors = []
            rem = n
            for p in primes_up_to(n):
                if rem % p == 0:
                    exponent = 0
                    while rem % p == 0:
                        rem //= p
                        exponent += 1
                    factors.append((p, exponent))
                if rem == 1:
                    break
            allowed = all(p % 4 != 3 or exp % 2 == 0 for p, exp in factors)
            self.assertEqual(r2 > 0, allowed)

    def test_quadratic_reciprocity_on_small_primes(self):
        odd_primes = [p for p in primes_up_to(79) if p > 2]
        for p in odd_primes:
            for q in odd_primes:
                if p == q:
                    continue
                lhs = quadratic_character(p, q) * quadratic_character(q, p)
                rhs = (-1) ** (((p - 1) // 2) * ((q - 1) // 2))
                with self.subTest(p=p, q=q):
                    self.assertEqual(lhs, rhs)

    def test_kloosterman_fourth_moment_and_small_prime_bound(self):
        """The fourth-moment formula holds at 3; its bound improves only from 5."""
        source = (CHAPTERS / "ch03-congruences.tex").read_text(encoding="utf-8")
        solution = source.split(r"\begin{solution}{pb:kloosterman}", 1)[1].split(
            r"\end{solution}", 1
        )[0]
        self.assertIn(r"For $p=3$", solution)
        self.assertIn(r"p\ge5", solution)
        for p in (3, 5, 7, 11):
            pair_counts = {}
            inverses = {x: pow(x, -1, p) for x in range(1, p)}
            for x in range(1, p):
                for y in range(1, p):
                    key = ((x + y) % p, (inverses[x] + inverses[y]) % p)
                    pair_counts[key] = pair_counts.get(key, 0) + 1
            quadruples = sum(count * count for count in pair_counts.values())
            numerator = p * p * quadruples - (p - 1) ** 4 - (p - 1)
            self.assertEqual(numerator % (p - 1), 0)
            moment = numerator // (p - 1)
            with self.subTest(p=p):
                self.assertEqual(moment, 2 * p ** 3 - 3 * p ** 2 - 3 * p)
                self.assertEqual(1.19 * p ** .75 < p - 1, p >= 5)

    def test_schur_exercise_counts_only_nonzero_polynomial_values(self):
        """Nonzero values avoid the trivial fact that every prime divides 0."""
        source = (CHAPTERS / "ch03-congruences.tex").read_text(encoding="utf-8")
        exercise = source.split(r"\label{pb:primepoly}", 1)[1].split(
            r"\end{exercise}", 1
        )[0]
        solution = source.split(r"\begin{solution}{pb:primepoly}", 1)[1].split(
            r"\end{solution}", 1
        )[0]
        self.assertIn(r"\emph{nonzero} value", exercise)
        self.assertIn(r"c=P(a)\ne0", solution)
        self.assertIn(r"M=|c|p_1\cdots p_r>0", solution)
        self.assertNotIn("If $c=0$, every prime", solution)

    def test_integer_square_locality_uses_elementary_moduli(self):
        """Step 4: a nonsquare integer has an elementary modular obstruction."""
        source = (CHAPTERS / "ch06-quadratic-reciprocity.tex").read_text(
            encoding="utf-8"
        )
        solution = source.split(
            r"\begin{solution}{pb:squaresmodpk}", 1
        )[1].split(r"\end{solution}", 1)[0]
        self.assertIn(r"m=p^{r+1}", solution)
        self.assertIn(r"m=4b^2", solution)
        self.assertNotIn(
            r"choose, by Chinese remainders and quadratic reciprocity, a prime",
            solution,
        )

        for a in range(-35, 36):
            if a >= 0 and math.isqrt(a) ** 2 == a:
                continue
            n = abs(a)
            odd_exponent = None
            for p in primes_up_to(n):
                exponent = 0
                while n % p == 0:
                    n //= p
                    exponent += 1
                if exponent % 2 and odd_exponent is None:
                    odd_exponent = (p, exponent)
            if odd_exponent:
                p, exponent = odd_exponent
                modulus = p ** (exponent + 1)
            else:
                self.assertLess(a, 0)
                modulus = 4 * abs(a)
            with self.subTest(a=a, modulus=modulus):
                self.assertFalse(any(
                    (x * x - a) % modulus == 0
                    for x in range(modulus)
                ))

    def test_corrected_radius_two_disc_count(self):
        """Radius two includes four axis points on its boundary."""
        source = (CHAPTERS / "ch07-sums-of-squares.tex").read_text(
            encoding="utf-8"
        )
        example = source.split(
            r"\begin{examplex}[the disc of radius $2$]", 1
        )[1].split(r"\end{examplex}", 1)[0]
        self.assertIn(r"N(2)=1+4+4+4=13", example)
        for radius, expected in ((2, 13), (6, 113), (10, 317)):
            with self.subTest(radius=radius):
                count = sum(
                    x * x + y * y <= radius * radius
                    for x in range(-radius, radius + 1)
                    for y in range(-radius, radius + 1)
                )
                self.assertEqual(count, expected)

    def test_eisenstein_norm_and_split_seven(self):
        """The Eisenstein norm is a²-ab+b², not a²+ab+b²."""
        source = (CHAPTERS / "ch10-gaussian-eisenstein.tex").read_text(
            encoding="utf-8"
        )
        example = source.split(
            r"\begin{examplex}[a split prime modulo $3$]", 1
        )[1].split(r"\end{examplex}", 1)[0]
        self.assertIn(r"N(2-\omega)", example)
        self.assertIn(r"7=(2-\omega)(2-\omega^2)", example)

        def eisenstein_norm(a, b):
            return a * a - a * b + b * b

        def eisenstein_multiply(u, v):
            a, b = u
            c, d = v
            # omega^2 = -1-omega.
            return (a * c - b * d, a * d + b * c - b * d)

        self.assertEqual(eisenstein_norm(2, -1), 7)
        self.assertEqual(eisenstein_norm(2, 1), 3)
        self.assertEqual(eisenstein_multiply((2, -1), (3, 1)), (7, 0))
        for a in range(-3, 4):
            for b in range(-3, 4):
                for c, d in ((1, 0), (0, 1), (2, -1), (1, 2)):
                    x, y = eisenstein_multiply((a, b), (c, d))
                    self.assertEqual(
                        eisenstein_norm(x, y),
                        eisenstein_norm(a, b) * eisenstein_norm(c, d),
                    )

    def test_mobius_series_first_ten_terms(self):
        """Restore the positive n=6 and negative n=7 terms."""
        source = (CHAPTERS / "ch14-characters.tex").read_text(
            encoding="utf-8"
        )
        example = source.split(
            r"\begin{examplex}[the series for $\mu$ at $s=2$]", 1
        )[1].split(r"\end{examplex}", 1)[0]
        self.assertIn(r"+\frac1{36}", example)
        self.assertIn(r"-\frac1{49}", example)
        self.assertIn(r"\approx0.6163", example)

        def mobius(n):
            result = 1
            for p in primes_up_to(n):
                if n % p:
                    continue
                result = -result
                n //= p
                if n % p == 0:
                    return 0
                while n % p == 0:
                    n //= p
            return result

        terms = [mobius(n) for n in range(1, 11)]
        self.assertEqual(terms, [1, -1, -1, 0, -1, 1, -1, 0, 0, 1])
        partial = sum(terms[n - 1] / (n * n) for n in range(1, 11))
        self.assertAlmostEqual(partial, 0.6162585, places=6)

    def test_diophantine_mod_four_and_markov_examples(self):
        source = (CHAPTERS / "ch09-diophantine.tex").read_text(
            encoding="utf-8"
        )
        example = source.split(
            r"\begin{examplex}[a modulus excludes half the inputs]", 1
        )[1].split(r"\end{examplex}", 1)[0]
        self.assertIn(r"$1,3,3,1$", example)
        residues = [(x * x + x + 1) % 4 for x in range(4)]
        self.assertEqual(residues, [1, 3, 3, 1])
        self.assertEqual(0 * 0 + 0 + 1, 1)
        self.assertEqual((-1) ** 2 - 1 + 1, 1)
        self.assertIn(r"n=2u^2v^2", source)
        self.assertIn(r"$(5,2,29)$", source)
        for x, y, z in ((1, 1, 1), (2, 1, 1), (5, 2, 1), (5, 2, 29)):
            with self.subTest(markov=(x, y, z)):
                self.assertEqual(
                    x * x + y * y + z * z, 3 * x * y * z
                )

    def test_primitive_pythagorean_parameters(self):
        for m in range(2, 16):
            for n in range(1, m):
                if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                    continue
                x, y, z = m * m - n * n, 2 * m * n, m * m + n * n
                self.assertTrue(x > 0 and y > 0 and z > 0)
                self.assertEqual(x * x + y * y, z * z)
                self.assertEqual(math.gcd(math.gcd(x, y), z), 1)

    def test_first_four_squares_have_representations(self):
        limit = 120
        sums_of_two = {a * a + b * b for a in range(12) for b in range(12)}
        four_sums = {u + v for u in sums_of_two for v in sums_of_two}
        for n in range(limit + 1):
            with self.subTest(n=n):
                self.assertIn(n, four_sums)

    def test_primitive_roots_count_for_small_primes(self):
        for p in primes_up_to(47):
            if p == 2:
                continue
            generators = []
            for a in range(1, p):
                current = 1
                powers = set()
                for exponent in range(1, p):
                    current = current * a % p
                    powers.add(current)
                    if current == 1:
                        if exponent == p - 1:
                            generators.append(a)
                        break
            with self.subTest(p=p):
                self.assertEqual(len(generators), totient(p - 1))


if __name__ == "__main__":
    unittest.main()
