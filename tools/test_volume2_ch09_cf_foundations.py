"""Exact finite checks for continued-fraction foundations, not infinite proofs."""

from fractions import Fraction
import itertools
import math
import unittest


def convergents(digits):
    p_old, p, q_old, q = 1, digits[0], 0, 1
    result = [(p, q)]
    for a in digits[1:]:
        p_old, p = p, a*p+p_old
        q_old, q = q, a*q+q_old
        result.append((p, q))
    return result


def evaluate(digits):
    result = Fraction(digits[-1])
    for a in reversed(digits[:-1]):
        result = a + 1/result
    return result


class ContinuedFractionFoundationChecks(unittest.TestCase):
    def test_tail_formula_and_determinants(self):
        for a0 in (-3, 0, 2):
            for tail in itertools.product((1, 2, 4), repeat=4):
                digits = [a0, *tail]
                pairs = [(1, 0), *convergents(digits)]
                for n, (p, q) in enumerate(pairs[1:]):
                    previous_p, previous_q = pairs[n]
                    self.assertEqual(p*previous_q-previous_p*q, (-1)**(n+1))
                    self.assertEqual(math.gcd(p, q), 1)
                    self.assertEqual(Fraction(p, q), evaluate(digits[:n+1]))
                for t in (Fraction(1, 3), Fraction(7, 2), Fraction(11)):
                    p, q = pairs[-2]
                    pp, qq = pairs[-3]
                    self.assertEqual(evaluate([*digits[:-1], t]), (t*p+pp)/(t*q+qq))

    def test_sqrt_two_strict_error_bounds(self):
        pairs = convergents([1] + [2]*31)
        for n, (p, q) in enumerate(pairs[:-1]):
            next_q = pairs[n+1][1]
            L, U = Fraction(1, q*(q+next_q)), Fraction(1, q*next_q)
            lower, upper = ((Fraction(p, q)+L, Fraction(p, q)+U) if n % 2 == 0
                            else (Fraction(p, q)-U, Fraction(p, q)-L))
            self.assertLess(lower*lower, 2)
            self.assertGreater(upper*upper, 2)

    def test_nested_prefix_intervals_and_bezout(self):
        digits = [-2] + [1, 2, 1, 5]*20
        pairs = [(1, 0), *convergents(digits)]
        last_interval = None
        for i, (p, q) in enumerate(pairs[1:]):
            pp, qq = pairs[i]
            endpoints = sorted((Fraction(p, q), Fraction(p+pp, q+qq)))
            if last_interval:
                self.assertGreaterEqual(endpoints[0], last_interval[0])
                self.assertLessEqual(endpoints[1], last_interval[1])
            self.assertEqual(endpoints[1]-endpoints[0], Fraction(1, q*(q+qq)))
            last_interval = endpoints
        self.assertEqual(convergents([4, 2, 6, 7]), [(4, 1), (9, 2), (58, 13), (415, 93)])
        for k in range(-10, 11):
            self.assertEqual(415*(13+93*k)-93*(58+415*k), 1)


if __name__ == "__main__":
    unittest.main()
