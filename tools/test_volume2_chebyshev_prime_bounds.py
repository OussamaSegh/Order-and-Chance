"""Independent integer and real-boundary checks for Chebyshev's prime bounds.

Finite probes support the two fully symbolic proofs recorded in DEP-020:
an induction on dyadic prime intervals (not the printed odd-induction)
and central-binomial prime valuations via digit carries. Nothing in this
file substitutes for the proof over all integers or all real x.
"""
import bisect
import math
import unittest
from pathlib import Path

CH2 = (Path(__file__).resolve().parents[1] /
       "volume2-integers" / "chapters" / "ch02-primes.tex")


def sieve(N):
    composite = bytearray(N+1)
    for p in range(2,math.isqrt(N)+1):
        if not composite[p]:
            for j in range(p*p,N+1,p):
                composite[j]=1
    return [p for p in range(2,N+1) if not composite[p]]


def valuation(n,p):
    e=0
    while n%p==0:
        e+=1
        n//=p
    return e


class TestChebyshevPrimeEstimates(unittest.TestCase):
    def test_exact_integer_primorial_bound_and_half_interval(self):
        primes=sieve(1200)
        product=1
        for N in range(1,1201):
            if N in primes:
                product*=N
            self.assertLess(product,4**N,N)
            if N>=3:
                m=N//2
                if N%2==0:
                    high=[p for p in primes if m<p<=N]
                    bound=math.comb(N,m)
                else:
                    high=[p for p in primes if m+1<p<=N]
                    bound=math.comb(N,m)
                hprod=math.prod(high)
                self.assertEqual(bound%hprod,0,N)
                self.assertLessEqual(hprod,bound,N)

    def test_real_x_floor_and_strict_product(self):
        primes=sieve(1100)
        for N in range(1,1101):
            product=math.prod(p for p in primes if p<=N)
            for x in (N, N+0.1, N+0.5, N+0.999):
                self.assertEqual(product,math.prod(p for p in primes if p<=x))
                self.assertLess(math.log(product),x*math.log(4))
        self.assertEqual(math.prod(p for p in primes if p<=1),1)

    def test_binomial_lower_bound_and_prime_power_obstruction(self):
        primes=sieve(10000)
        for n in range(1,251):
            B=math.comb(2*n,n)
            self.assertLessEqual(4**n,2*n*B,n)
            product=1
            for p in primes:
                if p>2*n: break
                q=valuation(B,p)
                pp=p**q
                self.assertLessEqual(pp,2*n,(n,p,q))
                product*=pp
            self.assertEqual(product,B)
            self.assertLessEqual(B,(2*n)**bisect.bisect_right(primes,2*n))
        # Check the full logarithmic conclusion without huge binomials.
        for n in range(1,5001):
            counted=bisect.bisect_right(primes,2*n)
            lb=(n*math.log(4)-math.log(2*n))/math.log(2*n)
            self.assertGreaterEqual(counted+1e-11,lb,n)
        self.assertEqual(
            (math.log(4)-math.log(2))/math.log(2),1.)

    def test_explicit_asymptotic_constants_and_endpoints(self):
        primes=sieve(10000)
        self.assertEqual(bisect.bisect_right(primes,100),25)
        self.assertEqual(bisect.bisect_right(primes,1000),168)
        for x in (16,16.5,17,32,100,1000,9999):
            self.assertGreaterEqual(
                x*math.log(2)/2-math.log(4*x),0)
            pi=bisect.bisect_right(primes,x)
            self.assertGreaterEqual(pi,
                (math.log(2)/2)*x/math.log(x)-1e-10)
            self.assertLess(pi,
                (1+2*math.log(4))*x/math.log(x))
        self.assertEqual(math.prod(p for p in primes if p<=11),2310)

    def test_named_result_comes_after_lemma(self):
        txt=CH2.read_text(encoding="utf-8")
        self.assertEqual(txt.count(r"\label{thm:cheb}"),1)
        self.assertEqual(txt.count(r"\label{lem:binom}"),1)
        self.assertLess(txt.index(r"\label{lem:binom}"),
                        txt.index(r"\label{thm:cheb}"))
        self.assertLess(txt.index(r"\label{thm:cheb}"),
                        txt.index(r"\label{thm:bertrand}"))
        self.assertIn("empty product equal to",txt)
        self.assertIn("For any real $x",txt)
        self.assertIn("if $x\\ge16$",txt)
        self.assertEqual(txt.count(r"\section{Exercises}"),1)
        self.assertEqual(txt.count(r"\section{Hints}"),1)
        self.assertEqual(txt.count(r"\section{Solutions}"),1)


if __name__=="__main__":
    unittest.main()
