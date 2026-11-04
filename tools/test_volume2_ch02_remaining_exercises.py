"""Independent exact finite probes for Chapter 2's seven remaining exercises.

Symbolic Pass A and Pass B for each item are fully documented in DEP-023;
these tests are adversarial finite corroboration, not universal proofs.
"""
import math
import unittest
from pathlib import Path

CH2 = (Path(__file__).resolve().parents[1] / "volume2-integers"
       / "chapters" / "ch02-primes.tex")


def sieve(n):
    prime=[True]*(n+1)
    prime[:2]=[False,False]
    for d in range(2,math.isqrt(n)+1):
        if prime[d]:
            for j in range(d*d,n+1,d):
                prime[j]=False
    return [p for p in range(2,n+1) if prime[p]]


def only_factors_from(n,allowed):
    for p in allowed:
        while n%p==0:
            n//=p
    return n==1


class TestRemainingChapterTwoExercises(unittest.TestCase):
    def test_arbitrarily_long_composite_runs(self):
        for length in range(1,41):
            M=math.factorial(length+1)
            run=[M+j for j in range(2,length+2)]
            self.assertEqual(len(run),length)
            self.assertTrue(all(y-x==1 for x,y in zip(run,run[1:])))
            for j,z in zip(range(2,length+2),run):
                self.assertGreater(z,j)
                self.assertEqual(z%j,0)
            self.assertLess(length,M+1)
        self.assertEqual(
            [math.factorial(4)+j for j in range(2,5)],
            [26,27,28])

    def test_factorial_not_perfect_power_using_prime_appearing_once(self):
        primes=sieve(1000)
        for n in range(2,501):
            m=n//2
            p=next(p for p in primes if m<p<=2*m)
            self.assertGreater(2*p,n,(n,p))
            self.assertLessEqual(p,n)
            f=math.factorial(n)
            self.assertEqual(f%p,0)
            self.assertNotEqual(f%(p*p),0,(n,p))
            self.assertEqual(sum(n//(p**k) for k in range(
                1,math.ceil(math.log(n,p))+2)),1)
        self.assertEqual(math.factorial(2),2)

    def test_erdos_squarefree_square_decomposition(self):
        primes=(2,3,5,7,11,13)
        for k in range(7):
            allowed=primes[:k]
            for N in (16,100,333,1000,4000):
                smooth=0
                for n in range(1,N+1):
                    if only_factors_from(n,allowed):
                        smooth+=1
                        # Independent squarefree-square decomposition.
                        a,b=1,1
                        c=n
                        d=2
                        while d*d<=c:
                            if c%d==0:
                                e=0
                                while c%d==0:
                                    e+=1
                                    c//=d
                                a*=d**(e%2)
                                b*=d**(e//2)
                            d+=1
                        if c>1:
                            a*=c
                        self.assertEqual(n,a*b*b)
                        self.assertTrue(only_factors_from(a,allowed))
                        self.assertLessEqual(b,math.isqrt(N))
                self.assertLessEqual(smooth,2**k*math.sqrt(N)+1e-9)
        self.assertEqual(sum(1 for n in range(1,20)
            if only_factors_from(n,())),1)

    def test_furstenberg_progressions_have_open_complements(self):
        for b in range(1,19):
            for a in range(-6,7):
                for x in range(-32,33):
                    in_class=(x-a)%b==0
                    in_complement=any((x-a-j)%b==0
                                      for j in range(1,b))
                    self.assertNotEqual(in_class,in_complement)
            if b==1:
                self.assertEqual(list(range(1,b)),[])
        # x + bc Z is contained in both x+b Z and x+c Z.
        for b in range(1,12):
            for c in range(1,12):
                for x in (-14,-1,0,7):
                    for j in range(-8,9):
                        y=x+j*b*c
                        self.assertEqual((y-x)%b,0)
                        self.assertEqual((y-x)%c,0)

    def test_factorial_plus_one_excludes_every_smaller_prime(self):
        primes=sieve(160)
        for n in range(2,151):
            value=math.factorial(n)+1
            self.assertGreater(value,n)
            self.assertTrue(all(value%p==1 for p in primes if p<=n))
        self.assertEqual(math.factorial(5)+1,11*11)

    def test_euclid_recursive_sequence_is_pairwise_coprime(self):
        sequence=[2]
        for _ in range(7):
            sequence.append(math.prod(sequence)+1)
        self.assertEqual(sequence[:5],[2,3,7,43,1807])
        self.assertEqual(sequence[4],13*139)
        for j,E in enumerate(sequence):
            if j>0:
                self.assertEqual(E,math.prod(sequence[:j])+1)
            for before in sequence[:j]:
                self.assertEqual(math.gcd(E,before),1)
                self.assertEqual(E%before,1)
        self.assertEqual(math.gcd(
            math.prod(sequence[:5]),sequence[5]),1)

    def test_prime_product_under_eleven_and_logs(self):
        primes=sieve(11)
        self.assertEqual(primes,[2,3,5,7,11])
        P=math.prod(primes)
        self.assertEqual(P,2310)
        self.assertEqual(4**11,4194304)
        self.assertLess(P,4**11)
        logsum=sum(math.log(p) for p in primes)
        self.assertAlmostEqual(logsum,math.log(P),places=12)
        self.assertAlmostEqual(logsum,7.745002803515839,places=12)
        self.assertAlmostEqual(11*math.log(4),15.249237972318797,places=11)
        self.assertLess(logsum,11*math.log(4))

    def test_printed_exercise_hint_solution_complete_structure(self):
        source=CH2.read_text(encoding="utf-8")
        keys=("ex:gaps","ex:factorial","ex:erdosdiv","ex:furstenberg",
              "ex:t1-factorial-new-prime","ex:t1-euclid-sequence",
              "ex:t1-prod11")
        for key in keys:
            self.assertEqual(source.count(r"\label{"+key+"}"),1)
            self.assertEqual(source.count(r"\begin{hint}{"+key+"}"),1)
            self.assertEqual(source.count(r"\begin{solution}{"+key+"}"),1)
        self.assertIn(r"A \emph{topology} is a choice of open sets",source)
        self.assertEqual(source.count(r"\begin{exercise}"),11)
        self.assertEqual(source.count(r"\end{exercise}"),11)
        self.assertEqual(source.count(r"\begin{hint}{"),11)
        self.assertEqual(source.count(r"\begin{solution}{"),11)
        self.assertEqual(source.count(r"\section{Hints}"),1)
        self.assertEqual(source.count(r"\section{Solutions}"),1)
        self.assertTrue(source.rstrip().endswith(r"\end{itemize}"))


if __name__=="__main__":
    unittest.main()
