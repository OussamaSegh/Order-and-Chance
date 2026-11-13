"""Volume 13, Chapter 7 (cyclotomic fields, Fermat, polynomial Fermat and three cubes): irregular primes below 160 and
their Bernoulli indices, the regular primes below 2000, Sophie Germain primes, cyclotomic discriminants, class
numbers h_p for p <= 23 (PARI), the norm-47 search, the cubic identities, sigma_infinity, local densities, the record
representations of 3, 33 and 42."""
import math
from fractions import Fraction
import sympy
import cypari2
import mpmath
from common import check, check_true, finish
pari = cypari2.Pari()
pari.allocatemem(2 * 10**9)

def irregular_indices(p):
    return [k for k in range(2, p - 2, 2) if sympy.bernoulli(k).p % p == 0]

irr = {p: irregular_indices(p) for p in sympy.primerange(3, 160)}
irr = {p: v for p, v in irr.items() if v}
check_true("irregular primes < 160 and indices",
           irr == {37: [32], 59: [44], 67: [58], 101: [68], 103: [24], 131: [22], 149: [130], 157: [62, 110]})
check_true("irregular primes < 100 are 37, 59, 67", [p for p in irr if p < 100] == [37, 59, 67])
# regular primes among the odd primes below 2000 (Bernoulli numerators, in PARI)
cnt = pari('(N)->my(c=0,t=0);forprime(p=3,N,t++;my(r=1);forstep(k=2,p-3,2,if(numerator(bernfrac(k))%p==0,r=0;break));c+=r);[c,t]')(2000)
check_true("181 of the 302 odd primes below 2000 are regular", [int(cnt[0]), int(cnt[1])] == [181, 302])
check("e^{-1/2}", math.exp(-0.5), 0.61, 0.005)
check_true("Sophie Germain list 3,5,11,23,29,41", all(sympy.isprime(2 * p + 1) for p in [3, 5, 11, 23, 29, 41])
           and [p for p in sympy.primerange(3, 42) if sympy.isprime(2 * p + 1)] == [3, 5, 11, 23, 29, 41])
check_true("disc Q(zeta_8) = disc(X^4+1) = 256", int(pari("nfdisc(polcyclo(8))")) == 256 == int(pari("poldisc(x^4+1)")))
check_true("disc Q(zeta_12) = 144 = d(Q(i))^2 d(Q(sqrt-3))^2", int(pari("nfdisc(polcyclo(12))")) == 144 == (-4)**2 * (-3)**2)
for p in [3, 5, 7, 11, 13, 17, 19]:
    check_true(f"h(Q(zeta_{p})) = 1", int(pari(f"bnfinit(polcyclo({p}),1).no")) == 1)
check_true("h(Q(zeta_23)) = 3", int(pari("bnfinit(polcyclo(23),1).no")) == 3)
check_true("47 splits completely in Q(zeta_23): 47 = 1 mod 23", 47 % 23 == 1)
check_true("no a^2+23b^2 = 188", not any(a * a + 23 * b * b == 188 for a in range(0, 14) for b in range(0, 3)))
# Mason, polynomial Fermat
t = sympy.symbols('t')
check_true("(2t)^2+(t^2-1)^2=(t^2+1)^2", sympy.expand((2*t)**2 + (t**2 - 1)**2 - (t**2 + 1)**2) == 0)
check_true("(t+1)^p = t^p+1 mod p, p=5,7", all(sympy.Poly((t + 1)**p - t**p - 1, t, modulus=p).is_zero for p in [5, 7]))
# three cubes
for tt in range(-20, 21):
    assert (1 + 6*tt**3)**3 + (1 - 6*tt**3)**3 + (-6*tt**2)**3 == 2
    assert (9*tt**4)**3 + (3*tt - 9*tt**4)**3 + (1 - 9*tt**3)**3 == 1
check_true("Verebrusov and Mahler identities (t in [-20,20], symbolic)",
           sympy.expand((1 + 6*t**3)**3 + (1 - 6*t**3)**3 + (-6*t**2)**3) == 2
           and sympy.expand((9*t**4)**3 + (3*t - 9*t**4)**3 + (1 - 9*t**3)**3) == 1)
check_true("cubes mod 9 are 0, +-1", sorted({x**3 % 9 for x in range(9)}) == [0, 1, 8])
check_true("4^3+4^3-5^3 = 3; 7^3-5^3-6^3 = 2; 7^3+10^3-11^3 = 12", 64 + 64 - 125 == 3 and 343 - 125 - 216 == 2 and 343 + 1000 - 1331 == 12)
R = range(-3, 4)
small = {n for n in range(1, 21) if any(x**3 + y**3 + z**3 == n for x in R for y in R for z in R)}
check_true("n<=20 not +-4 mod 9 and not reachable with |x|<=3: only 12",
           [n for n in range(1, 21) if n % 9 not in (4, 5) and n not in small] == [12])
check_true("excluded n<=20: 4,5,13,14", [n for n in range(1, 21) if n % 9 in (4, 5)] == [4, 5, 13, 14])
check_true("x^3+y^3+z^3=1 mod 5 has 25 solutions",
           sum(1 for x in range(5) for y in range(5) for z in range(5) if (x**3 + y**3 + z**3 - 1) % 5 == 0) == 25)
for p in [2, 5, 11]:
    for k in [1, 2]:
        q = p**k
        cubes = [x**3 % q for x in range(q)]
        from collections import Counter
        c = Counter(cubes)
        cnt = sum(c[a] * c[b] * c[(7 - a - b) % q] for a in c for b in c)
        check_true(f"sigma_{p}(7) ratio at k={k} equals 1", cnt == q**2)
s_int = 4 * mpmath.quad(lambda x: (x**3 + 1)**(-mpmath.mpf(2) / 3), [1, mpmath.inf])
s_gam = 2 * mpmath.gamma(mpmath.mpf(1) / 3)**2 / (3 * mpmath.gamma(mpmath.mpf(2) / 3))
check("4 int_1^inf (t^3+1)^(-2/3) = 2Gamma(1/3)^2/(3Gamma(2/3))", float(s_int), float(s_gam), 1e-9)
check("sigma_infinity", float(s_gam), 3.533, 0.0005)
a, b, c = 569936821221962380720, -569936821113563493509, -472715493453327032
check_true("Booker-Sutherland third representation of 3 (21-digit coordinates)", a**3 + b**3 + c**3 == 3 and len(str(a)) == 21)
a, b, c = 8866128975287528, -8778405442862239, -2736111468807040
check_true("Booker's 33 (16-digit cubes)", a**3 + b**3 + c**3 == 33 and len(str(a)) == 16 and len(str(-b)) == 16 and len(str(-c)) == 16)
a, b, c = -80538738812075974, 80435758145817515, 12602123297335631
check_true("Booker-Sutherland 42", a**3 + b**3 + c**3 == 42)
finish()
