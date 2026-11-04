"""Exact corroboration of the four remaining named Chapter 3 results.

DEP-025 independently reconstructs the CRT via an explicit inverse-based
affine solution, linear-congruence fibers by gcd cosets, the totient
divisor identity by gcd partition and Hensel uniqueness by comparing
two candidate digits. Tests probe non-coprime boundaries and p=2.
"""
import math
import unittest
from pathlib import Path

CH3=(Path(__file__).resolve().parents[1] /
     "volume2-integers" / "chapters" / "ch03-congruences.tex")


def egcd(a,b):
    old_r,r=a,b
    old_u,u=1,0
    old_v,v=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_u,u=u,old_u-q*u
        old_v,v=v,old_v-q*v
    return old_r,old_u,old_v


def totient(n):
    return sum(math.gcd(a,n)==1 for a in range(1,n+1))


class TestRemainingChapterThreeNamedResults(unittest.TestCase):
    def test_crt_bezout_formula_and_direct_affine_route(self):
        cases=0
        for m in range(1,35):
            for n in range(1,35):
                if math.gcd(m,n)!=1:
                    continue
                d,u,v=egcd(m,n)
                self.assertEqual(d,1)
                self.assertEqual(m*u+n*v,1)
                for a in range(m):
                    for b in range(n):
                        x=(a*n*v+b*m*u)%(m*n)
                        self.assertEqual(x%m,a)
                        self.assertEqual(x%n,b)
                        if n>1:
                            t=((b-a)*pow(m,-1,n))%n
                            affine=(a+m*t)%(m*n)
                        else:
                            affine=a%(m*n)
                        self.assertEqual(x,affine)
                        cases+=1
        self.assertGreater(cases,25000)
        self.assertEqual((7%1,7%5),(0,2))
        # Non-coprime pairs need compatibility; uniqueness mod mn fails.
        self.assertNotEqual(math.gcd(2,4),1)
        self.assertFalse(any(x%2==0 and x%4==1 for x in range(8)))

    def test_linear_congruence_exact_number_of_residue_solutions(self):
        cases=0
        for n in range(1,51):
            for a in range(-27,28):
                for b in range(-11,12):
                    d=math.gcd(a,n)
                    valid=(b%d==0)
                    xs=[x for x in range(n) if (a*x-b)%n==0]
                    self.assertEqual(bool(xs),valid,(n,a,b))
                    self.assertEqual(len(xs),d if valid else 0,(n,a,b))
                    if valid:
                        x0=xs[0]
                        predicted={(x0+j*(n//d))%n for j in range(d)}
                        self.assertEqual(predicted,set(xs))
                    cases+=1
        self.assertGreater(cases,60000)
        self.assertEqual([x for x in range(6) if (0*x-0)%6==0],
                         list(range(6)))

    def test_gauss_totient_divisor_sum_and_independent_gcd_fibers(self):
        for n in range(1,1001):
            ds=[d for d in range(1,n+1) if n%d==0]
            self.assertEqual(sum(totient(d) for d in ds),n)
            fibers={}
            for k in range(1,n+1):
                d=math.gcd(k,n)
                m=n//d
                fibers[m]=fibers.get(m,0)+1
            self.assertEqual(sum(fibers.values()),n)
            for m,count in fibers.items():
                self.assertIn(m,ds)
                self.assertEqual(count,totient(m))
        self.assertEqual(sum(totient(d) for d in (1,2,3,6)),6)
        self.assertEqual(totient(1),1)

    def test_hensel_unique_digit_with_square_and_cubic_polynomials(self):
        polys=(
            (lambda x:x*x+1, lambda x:2*x),
            (lambda x:x*x-x, lambda x:2*x-1),
            (lambda x:x*x*x+2*x+3, lambda x:3*x*x+2),
            (lambda x:x*x-5, lambda x:2*x))
        cases=0
        for p in (2,3,5,7,11,13):
            for k in (1,2,3):
                modulus=p**k
                for f,df in polys:
                    for a in range(modulus):
                        if f(a)%modulus!=0 or df(a)%p==0:
                            continue
                        good=[t for t in range(p)
                              if f(a+t*modulus)%(modulus*p)==0]
                        self.assertEqual(len(good),1,(p,k,a,good))
                        digit=good[0]
                        self.assertEqual(
                            (f(a)//modulus+digit*df(a))%p,0)
                        cases+=1
        self.assertGreater(cases,60)
        self.assertEqual([t for t in range(5) if
                          ((2+5*t)**2+1)%25==0],[1])
        # Singular roots must NOT be claimed unique:
        self.assertEqual([t for t in range(5)
                          if (5*t)**2%25==0],[0,1,2,3,4])
        self.assertEqual([t for t in range(5)
                          if ((5*t)**2-5)%25==0],[])

    def test_lemma_order_and_21_solution_structure(self):
        text=CH3.read_text(encoding="utf-8")
        keys=("thm:crt","prop:lincong","prop:phisum","thm:hensel")
        for key in keys:
            self.assertEqual(text.count(r"\label{"+key+"}"),1)
        self.assertEqual(
            [text.index(r"\label{"+k+"}") for k in keys],
            sorted(text.index(r"\label{"+k+"}") for k in keys))
        self.assertIn("corresponding ring has one element",text)
        self.assertIn("This also handles $a=0$",text)
        self.assertEqual(text.count(r"\begin{exercise}"),21)
        self.assertEqual(text.count(r"\end{exercise}"),21)
        self.assertEqual(text.count(r"\begin{hint}{"),21)
        self.assertEqual(text.count(r"\begin{solution}{"),21)


if __name__=="__main__":
    unittest.main()
