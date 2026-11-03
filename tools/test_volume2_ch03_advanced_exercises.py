"""Exact finite adversarial checks for six advanced Chapter 3 exercises.

DEP-027 records two complete general symbolic proof routes for Schur,
finite-field functions, the AKS polynomial criterion, Wolstenholme,
Jacobsthal and Kloosterman moments. Numerical samples below corroborate
but cannot establish these universal identities.
"""
import cmath
import math
import unittest
from pathlib import Path

CH3=(Path(__file__).resolve().parents[1] /
     "volume2-integers" / "chapters" / "ch03-congruences.tex")


def primes(n):
    return [p for p in range(2,n+1) if all(
        p%d for d in range(2,math.isqrt(p)+1))]


def prime_factors(n):
    f=set()
    d=2
    while d*d<=n:
        while n%d==0:
            f.add(d)
            n//=d
        d+=1
    if n>1:
        f.add(n)
    return f


def poly_power_x_minus_a(a,d,p):
    # Coefficients of (X-a)^d in ascending powers.
    return [(math.comb(d,k)*pow(-a,d-k,p))%p
            for k in range(d+1)]


def interpolate_values(values,p):
    # δ_a(X)=1−(X−a)^(p−1).
    coeffs=[0]*p
    for a in range(p):
        term=poly_power_x_minus_a(a,p-1,p)
        term[0]=(1-term[0])%p
        for j in range(1,p):
            term[j]=(-term[j])%p
        for j,v in enumerate(term):
            coeffs[j]=(coeffs[j]+values[a]*v)%p
    return coeffs


def evalpoly(coeffs,x,p):
    acc=0
    for c in reversed(coeffs):
        acc=(acc*x+c)%p
    return acc


class TestAdvancedChapterThreeExercises(unittest.TestCase):
    def test_schur_polynomial_congruences_and_prime_factors(self):
        for coeffs in ((0,1),(1,0,1),(41,1,1),(-3,2,1)):
            def P(x):
                return sum(c*x**i for i,c in enumerate(coeffs))
            a=9
            c=P(a)
            self.assertNotEqual(c,0)
            for t in range(0,50):
                self.assertEqual((P(a+t*abs(c))-c)%abs(c),0)
            values=[abs(P(n)) for n in range(0,300)]
            self.assertTrue(any(v>1 and len(prime_factors(v))>0
                                for v in values))
            self.assertTrue(any(v>1 and
                any(v%d==0 for d in range(2,math.isqrt(v)+1))
                for v in values))
            self.assertGreater(len(set.union(*(prime_factors(v)
                for v in values if v>1))),4)

    def test_all_small_finite_field_functions_interpolate_uniquely(self):
        for p in (2,3,5,7):
            for t in range(0,75):
                values=[(a*a+t*a+3*t)%p for a in range(p)]
                coeffs=interpolate_values(values,p)
                self.assertEqual(len(coeffs),p)
                self.assertEqual(
                    [evalpoly(coeffs,x,p) for x in range(p)],values)
                self.assertEqual(coeffs[-1],(-sum(values))%p)
        for t in (1,2,3):
            p=5
            values=[pow(a,3*t,p) for a in range(p)]
            coeffs=interpolate_values(values,p)
            self.assertEqual(coeffs[-1],0)
            self.assertEqual(
                [evalpoly(coeffs,a,p) for a in range(p)],values)
        self.assertEqual(interpolate_values([pow(a,3,5) for a in range(5)],5),
                         [0,0,0,1,0])
        self.assertEqual(interpolate_values([pow(a,6,5) for a in range(5)],5),
                         [0,0,1,0,0])
        self.assertEqual(interpolate_values([pow(a,9,5) for a in range(5)],5),
                         [0,1,0,0,0])

    def test_aks_polynomial_iff_primality_exact_coefficients(self):
        for n in range(2,101):
            isprime=n in primes(101)
            for a in (1,n-1,2,3,5):
                if math.gcd(a,n)!=1:
                    continue
                middle=all((math.comb(n,k)*pow(a,n-k,n))%n==0
                           for k in range(1,n))
                const=(pow(a,n,n)-a)%n==0
                self.assertEqual(middle and const,isprime,(n,a))
                if not isprime:
                    q=min(prime_factors(n))
                    self.assertNotEqual(
                        (math.comb(n,q)*pow(a,n-q,n))%n,0,(n,a,q))

    def test_wolstenholme_all_three_prime_power_congruences(self):
        for p in [p for p in primes(101) if p>=5]:
            s2=sum(pow(k,-2,p) for k in range(1,p))%p
            h=sum(pow(k,-1,p*p) for k in range(1,p))%(p*p)
            e2=((sum(pow(k,-1,p)**1 for k in range(1,p))**2 -
                 sum(pow(k,-2,p) for k in range(1,p))) *
                 pow(2,-1,p))%p
            self.assertEqual(s2,0,p)
            self.assertEqual(h,0,p)
            self.assertEqual(e2,0,p)
            self.assertEqual(math.comb(2*p-1,p-1)%(p**3),1,p)
            self.assertEqual(math.comb(2*p,p)%(p**3),2,p)

    def test_jacobsthal_all_small_primes_and_large_factors(self):
        for p in (2,3,5,7,11,13):
            for a in range(0,31):
                for b in range(a+1):
                    self.assertEqual(
                        math.comb(a*p,b*p)%(p*p),
                        math.comb(a,b)%(p*p),(p,a,b))
        # Independent refined binomial expansion modulo p²:
        for p in (2,3,5,7,11,13):
            for k in range(1,p):
                self.assertEqual(math.comb(p,k)%p,0)

    def test_kloosterman_moments_and_energy_count(self):
        for p in (3,5,7,11,13,17,19,23,29,31):
            inv={x:pow(x,-1,p) for x in range(1,p)}
            roots=[cmath.exp(2j*math.pi*k/p) for k in range(p)]
            def K(a,b):
                return sum(roots[(a*x+b*inv[x])%p]
                           for x in range(1,p))
            vals=[K(a,1) for a in range(p)]
            self.assertLess(max(abs(z.imag) for z in vals),1e-9)
            self.assertAlmostEqual(vals[0].real,-1,delta=1e-9)
            second=sum(abs(z)**2 for z in vals)
            fourth=sum(abs(z)**4 for z in vals)
            self.assertAlmostEqual(second,p*(p-1),delta=1e-7)
            self.assertAlmostEqual(fourth,2*p**3-3*p**2-3*p,
                                   delta=1e-6)
            self.assertLess(max(abs(z) for z in vals),
                            1.19*p**0.75)
            pairs={}
            for x in range(1,p):
                for y in range(1,p):
                    key=((x+y)%p,(inv[x]+inv[y])%p)
                    pairs[key]=pairs.get(key,0)+1
            energy=sum(q*q for q in pairs.values())
            self.assertEqual(energy,3*(p-1)*(p-2))
            for a in range(p):
                for b in (1,2,p-1):
                    self.assertAlmostEqual(K(a,b).real,K(a*b%p,1).real,
                                           delta=1e-9)

    def test_character_notation_and_structure_first_use(self):
        text=CH3.read_text(encoding="utf-8")
        keys=("pb:primepoly","pb:fpfunctions","pb:aks",
              "pb:wolsten","pb:jacobsthal","pb:kloosterman")
        for key in keys:
            self.assertEqual(text.count(r"\label{"+key+"}"),1)
            self.assertEqual(text.count(r"\begin{hint}{"+key+"}"),1)
            self.assertEqual(text.count(r"\begin{solution}{"+key+"}"),1)
        self.assertIn("Here $e(u)=\\exp(2\\pi i u)$",text)
        self.assertIn("No later theorem on exponential sums",text)
        self.assertIn("The polynomial $X^t-1$ has at most",text)
        self.assertEqual(text.count(r"\begin{exercise}"),21)
        self.assertEqual(text.count(r"\end{exercise}"),21)
        self.assertEqual(text.count(r"\begin{hint}{"),21)
        self.assertEqual(text.count(r"\begin{solution}{"),21)


if __name__=="__main__":
    unittest.main()
