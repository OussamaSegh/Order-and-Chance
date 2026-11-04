"""Finite arithmetic checks for the local four-square densities.

The infinite p-adic statements in the manuscript are proved by lifting and
primitive/nonprimitive decomposition. Finite modular enumeration here detects
errors but cannot certify the limits or the infinite Euler product.
"""
from fractions import Fraction
import unittest
from pathlib import Path


CH11 = (Path(__file__).resolve().parents[1] / "volume2-integers"
        / "chapters" / "ch14-characters.tex")


def convolve(a, b):
    m = len(a)
    out = [0]*m
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i+j)%m] += x*y
    return out


def four_squares_mod(m):
    root = [0]*m
    for a in range(m):
        root[a*a % m] += 1
    pairs = convolve(root, root)
    return convolve(pairs, pairs)


def valuation(n, p):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def density(p, n):
    a = valuation(n, p)
    if p == 2:
        return Fraction(1) if a == 0 else Fraction(3, 2**a)
    return (1-Fraction(1, p*p))*sum(
        (Fraction(1, p**j) for j in range(a+1)), Fraction(0)
    )


class TestFourSquareLocalDensities(unittest.TestCase):
    def test_exact_mod_eight_primitive_counts(self):
        all_counts = four_squares_mod(8)
        # Every all-even vector is twice a residue vector modulo 4:
        # for each coordinate this introduces two lifts.
        even_counts = [0]*8
        mod_two = four_squares_mod(2)
        for residue in range(8):
            if residue % 4 == 0:
                even_counts[residue] = 16 * mod_two[(residue//4) % 2]
        self.assertEqual(
            [a-b for a,b in zip(all_counts,even_counts)],
            [0,512,768,512,256,512,768,512]
        )

    def test_exact_stabilised_density_mod_prime_powers(self):
        cases = 0
        for p, powers in ((2, (3,4,5,6)), (3, (2,3,4)),
                          (5, (2,3))):
            for k in powers:
                m = p**k
                counts = four_squares_mod(m)
                for n in range(1,m):
                    a = valuation(n,p)
                    if k < (a+3 if p==2 else a+1):
                        continue
                    predicted = density(p,n)*p**(3*k)
                    with self.subTest(p=p, k=k, n=n):
                        self.assertEqual(counts[n], predicted)
                    cases += 1
        self.assertGreater(cases, 200)

    def test_global_factor_matches_divisor_count(self):
        # After removing the universal odd-prime factor 8/pi^2,
        # the local-to-global identity becomes this exact rational one.
        for n in range(1,301):
            u = n
            a = valuation(n,2)
            u //= 2**a
            sigma_u = sum(d for d in range(1,u+1) if u%d==0)
            from_local = 8*2**a*density(2,n)*sigma_u
            from_divisors = 8*sum(d for d in range(1,n+1)
                                  if n%d==0 and d%4!=0)
            self.assertEqual(from_local, from_divisors)

    def test_manuscript_explains_two_adic_split(self):
        src = CH11.read_text(encoding="utf-8")
        segment = src.split(r"\begin{solution}{pb:densities}",1)[1].split(
            r"\end{solution}",1)[0]
        self.assertIn("where $e_i$ has $1$ in position $i$", segment)
        self.assertIn("(4z+2+2z^4)^4-(2+2z^4)^4", segment)
        self.assertIn(r"\delta_2(n)", segment)
        self.assertIn(r"\delta_p(n)", segment)


if __name__ == "__main__":
    unittest.main()
