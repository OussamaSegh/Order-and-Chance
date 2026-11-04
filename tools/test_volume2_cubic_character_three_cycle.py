"""Finite independent checks for the local cubic-character three-cycle.

The general congruence is proved in the manuscript by orbits of
u -> 1/(1-u). This test constructs cubic characters from primitive roots,
checks every orbit and counts x^3+y^3=1 independently. Finite computation
is supporting evidence, not a replacement for the symbolic proof.
"""
import math
import unittest
from pathlib import Path


CH11 = (Path(__file__).resolve().parents[1] / "volume2-integers"
        / "chapters" / "ch14-characters.tex")
CH6 = (Path(__file__).resolve().parents[1] / "volume2-integers"
       / "chapters" / "ch06-quadratic-reciprocity.tex")


def primes_up_to(n):
    return [p for p in range(2, n + 1) if
            all(p % d for d in range(2, math.isqrt(p) + 1))]


def primitive_root(p):
    factors = [q for q in primes_up_to(p - 1) if (p - 1) % q == 0]
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError("No generator found")


class TestCubicCharacterThreeCycle(unittest.TestCase):
    def test_every_cubic_character_cycle_and_jacobi_sum(self):
        count = 0
        for p in primes_up_to(211):
            if p % 3 != 1:
                continue
            g = primitive_root(p)
            # chi(g^j) = omega^(j mod 3).
            residue_to_exponent = {
                pow(g, j, p): j % 3 for j in range(p - 1)
            }
            # omega^2 = -1-omega.
            pair = ((1, 0), (0, 1), (-1, -1))
            a = b = 0
            fixed = []
            for u in range(2, p):
                t = pow((1 - u) % p, -1, p)
                if t == u:
                    fixed.append(u)
                v = u * (1 - u) % p
                w = t * (1 - t) % p
                with self.subTest(p=p, u=u):
                    self.assertEqual(
                        residue_to_exponent[v], residue_to_exponent[w]
                    )
                    self.assertEqual(
                        pow((1-t) % p, -1, p),
                        (u-1) * pow(u, -1, p) % p
                    )
                ca, cb = pair[residue_to_exponent[v]]
                a += ca
                b += cb
            self.assertEqual(len(fixed), 2, p)
            self.assertTrue(all(u * (1 - u) % p == 1 for u in fixed))
            self.assertEqual((a + 1) % 3, 0, p)
            self.assertEqual(b % 3, 0, p)
            self.assertEqual(a * a - a * b + b * b, p)
            independently_counted = sum(
                (x ** 3 + y ** 3 - 1) % p == 0
                for x in range(p) for y in range(p)
            )
            self.assertEqual(independently_counted, p - 2 + 2 * a - b)
            count += 1
        self.assertEqual(count, 22)

    def test_independent_exponent_sum_and_unique_integer_norm(self):
        # A second congruence route: omega^e = 1+e(omega-1) mod 3
        # since (omega-1)^2 = -3 omega. Thus sum exponents
        # e(u)+e(1-u) modulo 3 rather than group the u by 3-cycles.
        count = 0
        for p in primes_up_to(211):
            if p % 3 != 1:
                continue
            g = primitive_root(p)
            exponents = {pow(g, j, p): j % 3 for j in range(p - 1)}
            total = sum(exponents[u] + exponents[(1-u) % p]
                        for u in range(2, p))
            self.assertEqual(total % 3, 0, p)
            self.assertEqual((p - 2) % 3, 2, p)
            # The coefficient of omega in the direct Jacobi sum.
            weights = ((1, 0), (0, 1), (-1, -1))
            a_coeff = b_coeff = 0
            for u in range(2, p):
                ca, cb = weights[exponents[(u * (1-u)) % p]]
                a_coeff += ca
                b_coeff += cb
            actual_a = 2 * a_coeff - b_coeff
            candidates = set()
            for A in range(-2 * math.isqrt(p) - 2, 2 * math.isqrt(p) + 3):
                for B in range(-math.isqrt((4*p)//27) - 1,
                               math.isqrt((4*p)//27) + 2):
                    if 4*p == A*A + 27*B*B and A % 3 == 1:
                        candidates.add(A)
            self.assertEqual(candidates, {actual_a}, p)
            count += 1
        self.assertEqual(count, 22)

    def test_character_problem_has_no_future_book_prerequisite(self):
        source = CH11.read_text(encoding="utf-8")
        exercise = source.split(r"\label{pb:fermatcubic}", 1)[1].split(
            r"\end{exercise}", 1
        )[0]
        solution = source.split(r"\begin{solution}{pb:fermatcubic}", 1)[1].split(
            r"\end{solution}", 1
        )[0]
        self.assertNotIn("requires the algebraic-integer", exercise)
        self.assertNotIn("the full ring of integers", solution)
        self.assertIn(r"T(u)=\frac1{1-u}", solution)
        self.assertIn(r"\pmod{3\Z[\omega]}", solution)
        self.assertIn("Every other orbit has three elements", solution)

    def test_waring_follows_earlier_jacobi_sum_proof(self):
        ch11 = CH11.read_text(encoding="utf-8")
        ch6 = CH6.read_text(encoding="utf-8")
        for environment in ("exercise", "hint", "solution"):
            if environment == "exercise":
                target = r"\label{pb:waring}"
                earlier = r"\label{pb:fermatcubic}"
            else:
                target = r"\begin{" + environment + r"}{pb:waring}"
                earlier = r"\begin{" + environment + r"}{pb:fermatcubic}"
            self.assertNotIn(target, ch6)
            self.assertEqual(ch11.count(target), 1)
            self.assertLess(ch11.index(earlier), ch11.index(target))


if __name__ == "__main__":
    unittest.main()
