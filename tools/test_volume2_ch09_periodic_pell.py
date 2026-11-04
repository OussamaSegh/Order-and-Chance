"""Finite exact and high-precision checks supporting continued-fraction proofs."""

from decimal import Decimal, localcontext
from fractions import Fraction
import math
import unittest

from tools.test_volume2_ch09_cf_foundations import convergents


def multiply(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def matrix(digits):
    result = [[1, 0], [0, 1]]
    for a in digits:
        result = multiply(result, [[a, 1], [1, 0]])
    return result


def sqrt_digits(D):
    a0 = math.isqrt(D)
    m, denominator, a = 0, 1, a0
    digits, states = [a0], {}
    while True:
        m = denominator*a-m
        denominator = (D-m*m)//denominator
        a = (a0+m)//denominator
        state = (m, denominator, a)
        if state in states:
            start = states[state]
            return digits[:start], digits[start:]
        states[state] = len(digits)
        digits.append(a)


class PeriodicPellChecks(unittest.TestCase):
    def test_period_matrix_gives_pell_unit(self):
        for D in range(2, 81):
            if math.isqrt(D)**2 == D:
                continue
            prefix, period = sqrt_digits(D)
            P, M = matrix(prefix), matrix(period)
            determinant = P[0][0]*P[1][1]-P[0][1]*P[1][0]
            inverse = [[determinant*P[1][1], -determinant*P[0][1]],
                       [-determinant*P[1][0], determinant*P[0][0]]]
            T = multiply(multiply(P, M), inverse)
            u, v = T[0][0], T[1][0]
            self.assertEqual(T, [[u, D*v], [v, u]])
            norm = u*u-D*v*v
            self.assertIn(norm, (-1, 1))
            self.assertNotEqual(v, 0)
            if norm == -1:
                u, v = u*u+D*v*v, 2*u*v
            self.assertEqual(u*u-D*v*v, 1)
            self.assertNotEqual(v, 0)

    def test_best_approximation_and_legendre(self):
        with localcontext() as context:
            context.prec = 80
            for D in (2, 3, 7):
                prefix, period = sqrt_digits(D)
                pairs = convergents(prefix + period*12)
                root = Decimal(D).sqrt()
                for n, (pn, qn) in enumerate(pairs[:-1]):
                    next_q = pairs[n+1][1]
                    error = abs(Decimal(qn)*root-pn)
                    for q in range(1, min(next_q, 201)):
                        floor = math.isqrt(D*q*q)
                        for p in (floor, floor+1):
                            self.assertGreaterEqual(abs(Decimal(q)*root-p), error)
                values = {Fraction(p, q) for p, q in pairs}
                for q in range(1, 201):
                    floor = math.isqrt(D*q*q)
                    for p in (floor, floor+1):
                        if abs(root-Decimal(p)/q) < Decimal(1)/(2*q*q):
                            self.assertIn(Fraction(p, q), values)

    def test_positive_pell_solutions_are_powers(self):
        for D in range(2, 16):
            if math.isqrt(D)**2 == D:
                continue
            direct = set()
            for y in range(1, 10001):
                x = math.isqrt(1+D*y*y)
                if x*x-D*y*y == 1:
                    direct.add((x, y))
            self.assertTrue(direct)
            u, v = min(direct, key=lambda pair: pair[1])
            generated, x, y = set(), u, v
            while y <= 10000:
                generated.add((x, y))
                x, y = u*x+D*v*y, v*x+u*y
            self.assertEqual(direct, generated)


if __name__ == "__main__":
    unittest.main()
