"""Independent periodic-residue validation of reduced random fractions.

For a positive reduced a/b, p stays downstairs iff v_p(b)>v_p(a).
The separate proof in the ledger counts exact finite residue classes,
whereas the printed solution uses limiting geometric valuation laws.
"""
import math
import unittest
from fractions import Fraction
from pathlib import Path

CH1=(Path(__file__).resolve().parents[1] / "volume2-integers"
     / "chapters" / "ch01-divisibility.tex")


def valuation(n,p):
    assert n>=1
    result=0
    while n%p==0:
        result+=1
        n//=p
    return result


def truncated_pair_count(p,K):
    """Number of (a,b) modulo p^K with v_p(a)<K, v_p(b)>v_p(a)."""
    return (p-1)*sum(p**(2*j) for j in range(K))


class TestReducedFractionValuations(unittest.TestCase):
    def test_cancellation_equivalence_without_approximations(self):
        for a in range(1,151):
            for b in range(1,151):
                d=math.gcd(a,b)
                reduced_a,reduced_b=a//d,b//d
                self.assertEqual(math.gcd(reduced_a,reduced_b),1)
                for p in (2,3,5,7):
                    self.assertEqual(reduced_b%p==0,
                                     valuation(b,p)>valuation(a,p),
                                     (a,b,p))

    def test_exact_truncated_residue_counts_one_prime(self):
        trials=0
        for p,Kmax in ((2,8),(3,6),(5,4),(7,3)):
            for K in range(1,Kmax+1):
                modulus=p**K
                expected=truncated_pair_count(p,K)
                actual=sum(
                    1
                    for a in range(1,modulus+1)
                    for b in range(1,modulus+1)
                    if valuation(a,p)<K and
                       valuation(b,p)>valuation(a,p))
                self.assertEqual(actual,expected,(p,K))
                exact=Fraction(expected,modulus*modulus)
                target=Fraction(1,p+1)*(
                    1-Fraction(1,p**(2*K)))
                self.assertEqual(exact,target)
                trials+=1
        self.assertEqual(trials,21)

    def test_simultaneous_events_exact_two_prime_period(self):
        requirements=((2,3),(3,2))
        modulus=math.prod(p**K for p,K in requirements)
        expected_prob=Fraction(1,1)
        for p,K in requirements:
            expected_prob*=Fraction(1,p+1)*(
                1-Fraction(1,p**(2*K)))
        exact_count=0
        for a in range(1,modulus+1):
            for b in range(1,modulus+1):
                if all(valuation(a,p)<K and
                       valuation(b,p)>valuation(a,p)
                       for p,K in requirements):
                    exact_count+=1
        self.assertEqual(exact_count,420)
        self.assertEqual(Fraction(exact_count,modulus**2),
                         expected_prob)

    def test_three_reduced_parity_types(self):
        # No even/even case survives reduction.
        for a in range(1,131):
            for b in range(1,131):
                d=math.gcd(a,b)
                aa,bb=a//d,b//d
                self.assertNotEqual((aa%2,bb%2),(0,0))
                self.assertEqual((bb%2==0),
                                 valuation(b,2)>valuation(a,2))
        self.assertEqual(Fraction(1,2+1), Fraction(1,3))

    def test_problem_hint_and_solution_remain_consistent(self):
        source=CH1.read_text(encoding="utf-8")
        key="pb:parity"
        self.assertEqual(source.count(r"\label{"+key+"}"),1)
        self.assertEqual(source.count(r"\begin{hint}{"+key+"}"),1)
        self.assertEqual(source.count(r"\begin{solution}{"+key+"}"),1)
        body=source.split(r"\begin{solution}{"+key+"}",1)[1].split(
            r"\end{solution}",1)[0]
        self.assertIn("12/18=2/3",body)
        self.assertIn(r"\frac1{p+1}",body)


if __name__=="__main__":
    unittest.main()
