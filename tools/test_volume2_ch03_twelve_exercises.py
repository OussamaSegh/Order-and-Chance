"""Independent exact probes for twelve Chapter 3 residue exercises.

DEP-026 contains two symbolic routes for each exercise, including a
distinct newly assigned CRT puzzle. Finite exhaustive checks confirm
edge cases; they do not replace the general proofs.
"""
import math
import unittest
from pathlib import Path

CH3=(Path(__file__).resolve().parents[1] /
     "volume2-integers" / "chapters" / "ch03-congruences.tex")


def prime_divisors(n):
    result=[]
    q=2
    while q*q<=n:
        if n%q==0:
            result.append(q)
            while n%q==0:
                n//=q
        q+=1
    if n>1:
        result.append(n)
    return result


def lucas_digit_product(n,k,p):
    ans=1
    while n or k:
        n,a=divmod(n,p)
        k,b=divmod(k,p)
        ans*=math.comb(a,b) if b<=a else 0
    return ans


class TestChapterThreeTwelveExercises(unittest.TestCase):
    def test_last_two_digits_by_direct_and_crt_routes(self):
        x=pow(7,2026,100)
        self.assertEqual(x,49)
        self.assertEqual(pow(7,2026,4),1)
        self.assertEqual(pow(7,2026,25),24)
        self.assertEqual([v for v in range(100)
                          if v%4==1 and v%25==24],[49])

    def test_sunzi_full_family_by_two_crt_routes(self):
        # The historical worked example remains 23; the exercise now uses
        # fresh remainders 1,2,3 so its answer has not already been supplied.
        self.assertEqual([x for x in range(105)
                          if x%3==2 and x%5==3 and x%7==2],[23])
        self.assertEqual(23%15,8)
        self.assertEqual(23%21,2)
        self.assertEqual([x for x in range(105) if
                          x%15==8 and x%7==2],[23])
        self.assertEqual([x for x in range(105)
                          if x%3==1 and x%5==2 and x%7==3], [52])
        self.assertEqual([x for x in range(105) if x%15==7 and x%7==3], [52])
        self.assertEqual((70+2*21+3*15)%105, 52)
        for k in range(-100, 101):
            x = 52+105*k
            self.assertEqual((x%3, x%5, x%7), (1, 2, 3))
        text = CH3.read_text(encoding="utf-8")
        solution = text.split(r'\begin{solution}{ex:sunzi}', 1)[1].split(r'\end{solution}', 1)[0]
        self.assertIn('x=52+105k', solution)

    def test_decimal_digit_rules_including_negative_and_zero(self):
        values=(0,1,9,10,12,99,101,1001,10001,918273645,
                -1,-9,-12,-99,-101,-1001,-918273645)
        values+=tuple(range(-12345,12346,137))
        for n in values:
            ds=[int(x) for x in reversed(str(abs(n)))]
            sign=-1 if n<0 else 1
            self.assertEqual(n%9,(sign*sum(ds))%9,n)
            self.assertEqual(n%11,(sign*sum(
                (-1)**i*d for i,d in enumerate(ds)))%11,n)
        self.assertEqual((-12)%9,(-3)%9)
        self.assertEqual((-12)%11,(-1)%11)

    def test_roots_of_one_for_every_small_odd_modulus(self):
        for n in range(1,302,2):
            roots=[x for x in range(n) if (x*x-1)%n==0]
            expected=2**len(prime_divisors(n))
            self.assertEqual(len(roots),expected,n)
            for p in prime_divisors(n):
                power=1
                while n%(power*p)==0:
                    power*=p
                self.assertEqual([x for x in range(power)
                                  if (x*x-1)%power==0],
                                 [1%power,(-1)%power] if power>2 else [])
        self.assertEqual([x for x in range(1) if (x*x-1)%1==0],[0])

    def test_wilson_converse_and_square_edge(self):
        for n in range(2,301):
            rem=math.factorial(n-1)%n
            prime=len(prime_divisors(n))==1 and (
                n==prime_divisors(n)[0])
            self.assertEqual(rem==(-1)%n,prime,n)
            if not prime and n>4:
                self.assertEqual(rem,0,n)
        self.assertEqual(math.factorial(3)%4,2)
        self.assertEqual(math.factorial(8)%9,0)

    def test_all_hensel_roots_through_125(self):
        roots5=[x for x in range(5) if (x*x+1)%5==0]
        roots25=[x for x in range(25) if (x*x+1)%25==0]
        roots125=[x for x in range(125) if (x*x+1)%125==0]
        self.assertEqual(roots5,[2,3])
        self.assertEqual(roots25,[7,18])
        self.assertEqual(roots125,[57,68])
        self.assertEqual((57*57+1)//125,26)
        self.assertEqual((68*68+1)//125,37)

    def test_tower_two_independent_residue_routes(self):
        exponent=3**27
        self.assertEqual(pow(3,exponent,100),87)
        self.assertEqual(exponent%40,27)
        self.assertEqual(exponent%20,7)
        self.assertEqual(pow(3,exponent,4),3)
        self.assertEqual(pow(3,exponent,25),12)
        self.assertEqual([x for x in range(100)
                          if x%4==3 and x%25==12],[87])

    def test_korselt_all_residues_including_zero_and_nonunits(self):
        for n,factors in ((561,(3,11,17)),(1105,(5,13,17))):
            self.assertEqual(math.prod(factors),n)
            self.assertTrue(all((n-1)%(p-1)==0 for p in factors))
            for a in range(n):
                self.assertEqual(pow(a,n,n),a%n,(n,a))
            self.assertEqual(len(prime_divisors(n)),3)

    def test_lucas_every_small_binomial_and_out_of_range_k(self):
        for p in (2,3,5,7,11,13):
            for n in range(0,151):
                for k in range(0,n+5):
                    actual=math.comb(n,k) if k<=n else 0
                    predicted=lucas_digit_product(n,k,p)
                    self.assertEqual(actual%p,predicted%p,(p,n,k))
        self.assertEqual(lucas_digit_product(5,3,2),0)

    def test_toy_rsa_all_55_messages_not_just_units(self):
        for m in range(55):
            cipher=pow(m,3,55)
            restored=pow(cipher,27,55)
            self.assertEqual(restored,m,(m,cipher,restored))
            self.assertEqual(pow(m,81,5),m%5)
            self.assertEqual(pow(m,81,11),m%11)
        self.assertEqual(pow(12,3,55),23)
        self.assertEqual(pow(23,27,55),12)
        self.assertEqual(math.gcd(5,55),5)

    def test_2power_square_roots_entire_small_moduli(self):
        for k in range(1,14):
            n=2**k
            roots=[x for x in range(n) if (x*x-1)%n==0]
            if k==1:
                expected=[1]
            elif k==2:
                expected=[1,3]
            else:
                expected=sorted({
                    1%n,(-1)%n,(1+2**(k-1))%n,(-1+2**(k-1))%n})
            self.assertEqual(roots,expected,k)

    def test_new_nonduplicated_crt_exercise(self):
        moduli=((4,1),(9,3),(11,4))
        self.assertEqual([x for x in range(1,397)
                          if all(x%m==r for m,r in moduli)],[345])
        self.assertEqual(4*9*11,396)
        self.assertEqual((297+3*352+4*144)%396,345)
        self.assertEqual((345%4,345%9,345%11),(1,3,4))

    def test_first_use_and_21_exercise_structure(self):
        text=CH3.read_text(encoding="utf-8")
        keys=("ex:last2","ex:sunzi","ex:digits","ex:sqrt1",
              "ex:wilsonconv","ex:hensel","ex:tower","ex:korselt",
              "ex:lucas","ex:t1-toy-rsa","ex:t1-two-power-roots",
              "ex:t1-sunzi23")
        for key in keys:
            self.assertEqual(text.count(r"\label{"+key+"}"),1)
            self.assertEqual(text.count(r"\begin{hint}{"+key+"}"),1)
            self.assertEqual(text.count(r"\begin{solution}{"+key+"}"),1)
        self.assertIn("A second remainder puzzle.",text)
        self.assertIn(r"$n,k\ge0$",text)
        self.assertIn("Here $e(u)=",text)
        self.assertIn("some nonzero $u$ satisfies $u^t",text)
        self.assertEqual(text.count(r"\begin{exercise}"),21)
        self.assertEqual(text.count(r"\end{exercise}"),21)
        self.assertEqual(text.count(r"\begin{hint}{"),21)
        self.assertEqual(text.count(r"\begin{solution}{"),21)


if __name__=="__main__":
    unittest.main()
