"""Independent finite checks for the remaining continued-fraction exercises."""

from decimal import Decimal, localcontext
from fractions import Fraction
import math
import unittest

from tools.test_volume2_ch09_cf_foundations import convergents
from tools.test_volume2_ch09_periodic_pell import sqrt_digits


class ContinuedFractionExerciseChecks(unittest.TestCase):
    def test_fibonacci_and_quadratic_periods(self):
        fib = [0, 1]
        for _ in range(20):
            fib.append(sum(fib[-2:]))
        self.assertEqual(convergents([1]*15), [(fib[n+2], fib[n+1]) for n in range(15)])
        self.assertEqual(sqrt_digits(3), ([1], [1, 2]))
        self.assertEqual(convergents([1, 1, 2])[:2], [(1, 1), (2, 1)])
        for n in range(1, 31):
            D = n*n+1
            self.assertEqual(sqrt_digits(D), ([n], [2*n]))
            self.assertEqual((2*n*n+1)**2-D*(2*n)**2, 1)

    def test_calendar_exact_arithmetic(self):
        target = Fraction(24219, 100000)
        r, digits = target, []
        while True:
            a = r.numerator // r.denominator
            digits.append(a)
            if r == a:
                break
            r = 1/(r-a)
        self.assertEqual(digits, [0, 4, 7, 1, 3, 24, 6, 2, 2])
        self.assertEqual(convergents(digits)[1:6], [(1, 4), (7, 29), (8, 33), (31, 128), (752, 3105)])
        self.assertEqual(Fraction(1, 4)-target, Fraction(781, 100000))
        self.assertEqual(Fraction(8, 33)-target, Fraction(773, 3300000))
        self.assertEqual(Fraction(97, 400)-target, Fraction(31, 100000))
        self.assertEqual(Fraction(31, 128)-target, -Fraction(1, 400000))

    def test_square_triangular_completeness_in_finite_range(self):
        direct = {m for m in range(100001)
                  if math.isqrt(m*(m+1)//2)**2 == m*(m+1)//2}
        generated, x, y = {0}, 3, 2
        while (x-1)//2 <= 100000:
            self.assertEqual((x % 2, y % 2), (1, 0))
            generated.add((x-1)//2)
            x, y = 3*x+4*y, 2*x+3*y
        self.assertEqual(direct, generated)

    def test_golden_scaled_errors_and_stronger_threshold(self):
        with localcontext() as context:
            context.prec = 100
            root5 = Decimal(5).sqrt()
            phi = (1+root5)/2
            for n, (p, q) in enumerate(convergents([1]*45)):
                scaled = Decimal(q*q)*abs(phi-Decimal(p)/q)
                exact = (1-(-1/(phi*phi))**(n+1))/root5
                self.assertLess(abs(scaled-exact), Decimal('1e-60'))
            found = set()
            for q in range(1, 501):
                floor = int(phi*q)
                for p in (floor, floor+1):
                    if abs(phi-Decimal(p)/q) < Decimal(4)/(9*q*q):
                        found.add((p, q))
            self.assertEqual(found, {(2, 1), (5, 3)})

    def test_liouville_finite_tail_and_polynomial_bound(self):
        for n in range(1, 5):
            tail = sum(Fraction(1, 10**math.factorial(k)) for k in range(n+1, n+4))
            q = 10**math.factorial(n)
            self.assertGreater(tail, 0)
            self.assertLess(tail, Fraction(2, q**(n+1)))
        with localcontext() as context:
            context.prec = 80
            root = Decimal(2).sqrt()
            for q in range(1, 201):
                floor = math.isqrt(2*q*q)
                for p in (floor, floor+1):
                    self.assertGreaterEqual(abs(root-Decimal(p)/q), Decimal(1)/(4*q*q))


if __name__ == "__main__":
    unittest.main()
