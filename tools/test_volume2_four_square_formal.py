"""Finite symbolic coefficient regressions for the four-square journey.

The book derives these infinite identities formally and supplies a finite
annulus proof of the 4-ball volume. These tests check coefficients and
finite arithmetic only; they are not substitutes for those proofs.
"""
import math
import unittest
from pathlib import Path


CH11 = (Path(__file__).resolve().parents[1] / "volume2-integers"
        / "chapters" / "ch14-characters.tex")


def multiply(a, b):
    n = len(a)-1
    return [sum(a[j]*b[m-j] for j in range(m+1)) for m in range(n+1)]


def power(a, k):
    unit = [1] + [0]*(len(a)-1)
    for _ in range(k):
        unit = multiply(unit, a)
    return unit


def euler(n):
    p = [1] + [0]*n
    for d in range(1, n+1):
        for m in range(n, d-1, -1):
            p[m] -= p[m-d]
    return p


def theta(n, alternating=False):
    out = [0]*(n+1)
    out[0] = 1
    for j in range(1, math.isqrt(n)+1):
        out[j*j] += 2*(-1 if alternating and j % 2 else 1)
    return out


def triangular_theta(n):
    out = [0]*(n+1)
    for j in range(math.isqrt(n)+2):
        d = j*(j+1)
        if d <= n:
            out[d] += 2
    return out


class TestFourSquareFormalIdentities(unittest.TestCase):
    def test_jacobi_cubic_and_double_sum_derivative_identity(self):
        n = 155
        E3 = power(euler(n), 3)
        E6 = power(euler(n), 6)
        cubic = [0]*(n+1)
        for k in range(n+1):
            t = k*(k+1)//2
            if t > n:
                break
            cubic[t] += (-1)**k*(2*k+1)
        self.assertEqual(E3, cubic)
        T = theta(n)
        B = triangular_theta(n)
        DB = [j*B[j] for j in range(n+1)]
        DT = [j*T[j] for j in range(n+1)]
        rhs = [a - 4*b for a,b in zip(
            multiply(T, [B[j]+4*DB[j] for j in range(n+1)]),
            multiply(B, DT)
        )]
        self.assertEqual([2*x for x in E6], rhs)

    def test_lambert_series_and_four_square_divisors(self):
        n = 155
        theta4 = power(theta(n), 4)
        signed_theta4 = power(theta(n, alternating=True), 4)
        lambert = [0]*(n+1)
        lambert[0] = 1
        for m in range(1,n+1):
            coefficient = -8*m if m%2 else 8*m
            for j in range(1,n//m+1):
                lambert[m*j] += coefficient*((-1)**(j-1))
        self.assertEqual(signed_theta4, lambert)
        for m in range(1, n+1):
            divisor_formula = 8*sum(d for d in range(1, m+1)
                                    if m%d == 0 and d%4)
            self.assertEqual(theta4[m], divisor_formula, m)

    def test_four_ball_annulus_squeeze(self):
        for radius in (1, 2, 7):
            volume = math.pi**2 * radius**4 / 2
            for m in (1, 2, 3, 10, 100, 1000):
                lower = volume*(m-1)/m
                upper = volume*(m+1)/m
                self.assertLessEqual(lower, volume)
                self.assertLessEqual(volume, upper)
                self.assertAlmostEqual((lower+upper)/2, volume, places=7)
        source = CH11.read_text(encoding="utf-8")
        proof = source.split(r"\begin{solution}{pb:jacobi}", 1)[1].split(
            r"\end{solution}", 1)[0]
        self.assertIn("The corresponding annuli", proof)
        self.assertIn(r"V_4(R)=\pi^2R^4/2", proof)
        self.assertIn("only finitely many factors affect any one coefficient",
                      proof)


if __name__ == "__main__":
    unittest.main()
