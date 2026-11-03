"""Independent finite tests for Chapter 3's first four named claims.

Ledger DEP-024 has separate symbolic proof routes:
direct divisibility versus canonical-remainder quotient for ring operations;
Bezout versus injective multiplication for units;
product permutation versus cyclic-orbit counting for Euler;
inverse pairs versus polynomial-root identity for Wilson.
"""
import math
import unittest
from pathlib import Path

CH3 = (Path(__file__).resolve().parents[1] /
       "volume2-integers" / "chapters" / "ch03-congruences.tex")


def primes_up_to(N):
    return [p for p in range(2,N+1) if all(p%d for d in
            range(2,math.isqrt(p)+1))]


def poly_times_linear(coeffs,a,p):
    new=[0]*(len(coeffs)+1)
    for i,c in enumerate(coeffs):
        new[i]=(new[i]-a*c)%p
        new[i+1]=(new[i+1]+c)%p
    return new


class TestFirstFourNamedCongruenceResults(unittest.TestCase):
    def test_ring_operations_respect_any_integer_representatives(self):
        for n in range(1,51):
            for a in range(-10,11):
                for b in range(-8,9):
                    for k,l in ((0,0),(1,-1),(-4,7)):
                        ap=a+k*n
                        bp=b+l*n
                        self.assertEqual((ap+bp-(a+b))%n,0)
                        self.assertEqual((ap*bp-a*b)%n,0)
            for a in range(min(n,8)):
                for b in range(min(n,8)):
                    for c in range(min(n,8)):
                        self.assertEqual(((a+b)%n+c)%n,(a+(b+c)%n)%n)
                        self.assertEqual(((a*b)%n*c)%n,(a*(b*c)%n)%n)
                        self.assertEqual((a*(b+c))%n,
                                         (a*b+a*c)%n)
        self.assertEqual({a%1 for a in range(-50,51)}, {0})

    def test_inverses_and_phi_include_the_zero_ring(self):
        for n in range(1,151):
            phi=sum(math.gcd(a,n)==1 for a in range(1,n+1))
            units=0
            for a in range(n):
                g=math.gcd(a,n)
                witness=next((u for u in range(n)
                            if (a*u-1)%n==0),None)
                self.assertEqual(witness is not None,g==1,(n,a))
                if witness is not None:
                    units+=1
                    self.assertEqual((a*witness)%n,1%n)
                if g==1:
                    seen={(a*x)%n for x in range(n)}
                    self.assertEqual(len(seen),n)
            self.assertEqual(units,phi,n)
            if n>=2:
                field=all(math.gcd(a,n)==1 for a in range(1,n))
                self.assertEqual(field,n in primes_up_to(151))
        self.assertEqual(sum(math.gcd(a,1)==1 for a in range(1,2)),1)
        self.assertEqual(0,1%1)

    def test_euler_theorem_and_orbit_divisibility(self):
        for n in range(1,401):
            phi=sum(math.gcd(a,n)==1 for a in range(1,n+1))
            for a in range(0,n):
                if math.gcd(a,n)!=1:
                    continue
                self.assertEqual(pow(a,phi,n),1%n,(n,a))
                x=1%n
                order=0
                while True:
                    x=(x*a)%n
                    order+=1
                    if x==1%n:
                        break
                    self.assertLessEqual(order,n)
                self.assertEqual(phi%order,0,(n,a,phi,order))
        self.assertEqual(pow(0,1,1),0)

    def test_wilson_factorial_and_polynomial_independent_proof(self):
        for p in primes_up_to(211):
            self.assertEqual(math.factorial(p-1)%p,(p-1)%p)
        for p in primes_up_to(31):
            poly=[1]
            for a in range(1,p):
                poly=poly_times_linear(poly,a,p)
            target=[0]*p
            target[0]=(-1)%p
            target[-1]=1
            self.assertEqual(poly,target,(p,poly,target))
        self.assertEqual(math.factorial(1)%2,1)

    def test_first_use_and_source_invariants(self):
        text=CH3.read_text(encoding="utf-8")
        expected=("prop:ringZn","prop:units","thm:eulerthm","thm:wilson")
        for key in expected:
            self.assertEqual(text.count(r"\label{"+key+"}"),1)
        pos=[text.index(r"\label{"+k+"}") for k in expected]
        self.assertEqual(pos,sorted(pos))
        self.assertLess(text.index("Euler's \\emph{totient}"),
                        text.index(r"\label{prop:units}"))
        self.assertIn(r"$\varphi(1)=1$",text)
        self.assertIn(r"For every integer $n\ge1$",text)
        self.assertIn("Starting at $0$, repeated addition of $4$",text)
        self.assertEqual(text.count(r"\begin{exercise}"),21)
        self.assertEqual(text.count(r"\end{exercise}"),21)
        self.assertEqual(text.count(r"\begin{hint}{"),21)
        self.assertEqual(text.count(r"\begin{solution}{"),21)


if __name__=="__main__":
    unittest.main()
