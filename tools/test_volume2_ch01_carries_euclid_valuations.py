"""Independent finite checks for Chapter 1 binomial carries, Euclid and valuations.

These tests are supporting evidence. The full proofs, including limits,
joint independence and the O(1) estimate, are in the mathematical ledger.
All algorithms here follow separate routes from the printed explanations.
"""
import itertools
import math
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path

CH1 = (Path(__file__).resolve().parents[1] / "volume2-integers"
       / "chapters" / "ch01-divisibility.tex")


def valuation(number, prime):
    assert number >= 1
    exponent = 0
    while number % prime == 0:
        number //= prime
        exponent += 1
    return exponent


def base_digits_sum(n, base):
    total = 0
    while n:
        n, digit = divmod(n, base)
        total += digit
    return total


def addition_carries(m, n, base):
    total_carries = 0
    carry = 0
    while m or n or carry:
        m, a = divmod(m, base)
        n, b = divmod(n, base)
        carry = (a + b + carry) // base
        assert carry in (0, 1)
        total_carries += carry
    return total_carries


def independent_euclid(a, b):
    old_r, r = a, b
    old_u, u = 1, 0
    old_v, v = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_u, u = u, old_u - q*u
        old_v, v = v, old_v - q*v
    return old_r, old_u, old_v


class TestChapterOneCarriesEuclidAndValuations(unittest.TestCase):
    def test_binomial_valuation_equals_digit_carries(self):
        # Separate checks: modular factor count in an integer binomial,
        # digit-sum identity, and ordinary schoolbook addition carries.
        cases = 0
        for p in (2, 3, 5, 7, 11):
            for m in range(0, 65):
                for n in range(0, 65):
                    value = math.comb(m+n, m)
                    by_division = valuation(value, p)
                    by_digit_sums = (
                        base_digits_sum(m,p) + base_digits_sum(n,p)
                        - base_digits_sum(m+n,p)) // (p-1)
                    by_carries = addition_carries(m,n,p)
                    self.assertEqual(by_division, by_digit_sums, (p,m,n))
                    self.assertEqual(by_division, by_carries, (p,m,n))
                    cases += 1
        self.assertEqual(cases, 21125)
        self.assertEqual(math.comb(10,4),210)
        self.assertEqual(addition_carries(4,6,2),1)
        self.assertEqual(valuation(210,2),1)

    def test_euclid_and_bezout_two_independent_routes(self):
        a,b = 1071,462
        # A direct Euclid descent and a separate prime divisibility view.
        d,u,v=independent_euclid(a,b)
        self.assertEqual((d,u,v),(21,-3,7))
        self.assertEqual((a//d,b//d),(51,22))
        self.assertEqual(7*22-3*51,1)
        self.assertEqual(a*u+b*v,21)
        for t in range(-100,101):
            self.assertEqual(a*(-3+22*t)+b*(7-51*t),21)
        # The earlier demonstration now uses a DIFFERENT problem;
        # it must no longer give away the exercise's arithmetic.
        aa,bb = 899,372
        self.assertEqual(independent_euclid(aa,bb),(31,5,-12))
        self.assertEqual(aa*5-bb*12,31)
        for t in range(-100,101):
            self.assertEqual(aa*(5+12*t)+bb*(-12-29*t),31)

    def test_exact_prime_valuation_probabilities_and_means(self):
        cases=0
        for p in (2,3,5,7,11):
            for N in (1,2,3,4,5,17,31,64,100,127,256,511,1000,4096):
                counts = Counter(valuation(n,p) for n in range(1,N+1))
                bound = math.floor(math.log(N,p))+2
                for k in range(0,bound+1):
                    expected = N//(p**k)-N//(p**(k+1))
                    self.assertEqual(counts[k],expected,(p,N,k))
                exact_mean = Fraction(
                    sum(k*v for k,v in counts.items()),N)
                tail_sum = Fraction(
                    sum(N//(p**k) for k in range(1,bound+1)),N)
                self.assertEqual(exact_mean,tail_sum,(p,N))
                cases+=1
        self.assertEqual(cases,70)

    def test_joint_residue_counts_for_three_primes(self):
        primes=(2,3,5)
        # A common period sufficient for all exact k=0,1,2 events.
        period=math.prod(p**3 for p in primes)
        events=Counter()
        for x in range(1,period+1):
            key=tuple(valuation(x,p) for p in primes)
            if all(k<=2 for k in key):
                events[key]+=1
        for ks in itertools.product(range(3),repeat=3):
            prob=math.prod([Fraction(p-1,p**(k+1))
                           for p,k in zip(primes,ks)])
            self.assertEqual(events[ks],period*prob,(ks,period))

    def test_heavy_tail_mean_and_typical_event(self):
        for N in (1,2,3,5,11,31,32,64,100,127,256,511,1000,4096,8192):
            values=[valuation(n,2) for n in range(1,N+1)]
            exact=Fraction(sum(2**k for k in values),N)
            L=N.bit_length()-1
            alternate=Fraction(1,1)+Fraction(
                sum(2**(k-1)*(N//(2**k)) for k in range(1,L+1)),N)
            self.assertEqual(exact,alternate)
            self.assertLess(abs(float(exact)-math.log2(N)/2),2)
            self.assertEqual(sum(k<=1 for k in values),
                             N-N//4)
        self.assertEqual(
            Fraction(sum(valuation(n,2)<=1 for n in range(1,4097)),4096),
            Fraction(3,4))

    def test_source_question_hint_and_solution_contract(self):
        source=CH1.read_text(encoding="utf-8")
        for key in ("ex:t1-binomial-carry", "ex:t1-euclid1071",
                    "pb:valuation"):
            self.assertEqual(source.count(r"\label{" + key + "}"),1)
            self.assertEqual(source.count(r"\begin{hint}{" + key + "}"),1)
            self.assertEqual(source.count(r"\begin{solution}{" + key + "}"),1)
        before_exercises=source.split(r"\section{Exercises}",1)[0]
        self.assertIn(
            "a complete run for $899$ and $372$", before_exercises)
        self.assertNotIn(
            "a complete run for $1071$ and $462$", before_exercises)


if __name__=="__main__":
    unittest.main()
