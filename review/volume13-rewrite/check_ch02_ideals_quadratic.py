"""Volume 13, Chapter 2 (ideals in quadratic fields): e^{pi sqrt163}, the class-number-one list, the first irregular prime,
the splitting data of Exercise factor5, the forms of discriminant -20 and Exercise fermat5."""
import math
from mpmath import mp, mpf, exp, pi, sqrt
from sympy import bernoulli, primerange, legendre_symbol, isprime
from common import check, check_true, finish

mp.dps = 50
v = exp(pi * sqrt(163))
check_true("e^{pi sqrt163} = 262537412640768743.99999999999925...", str(v).startswith("262537412640768743.99999999999925"))

def classno(D):
    """number of reduced primitive positive definite forms of discriminant D<0"""
    h = 0
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if c < a or math.gcd(math.gcd(a, b), c) != 1: continue
            if b < 0 and (a == c): continue
            h += 1
        a += 1
    return h
def fund_disc(d): return d if d % 4 == 1 else 4 * d
sqfree = [d for d in range(-1, -400, -1) if all(d % (q * q) for q in range(2, 21))]
one = [d for d in sqfree if classno(fund_disc(d)) == 1]
check_true(f"class number one d in [-400,-1]: {one}", one == [-1, -2, -3, -7, -11, -19, -43, -67, -163])
check_true("h(Q(sqrt-5)) = 2", classno(-20) == 2)
irr = [p for p in primerange(3, 200) if any(bernoulli(k).p % p == 0 for k in range(2, p - 2, 2))]
check_true(f"first irregular prime is 37 (irregular <200: {irr})", irr[0] == 37)
# Exercise factor5
check_true("-5 = 2 = 3^2 mod 7", (-5) % 7 == 9 % 7)
check_true("13^2 = 169 = 5*29+24 = -5 mod 29", 169 == 5 * 29 + 24 and 169 % 29 == (-5) % 29)
check_true("(-5/11) = -1", legendre_symbol(-5 % 11, 11) == -1)
check_true("3+2sqrt-5 = 29 - 2(13 - sqrt-5)", (29 - 26, 2) == (3, 2))
f = lambda u, v: 2 * u * u + 2 * u * v + 3 * v * v
check_true("f(1,0),f(0,1),f(1,-1),f(1,1) = 2,3,3,7", (f(1, 0), f(0, 1), f(1, -1), f(1, 1)) == (2, 3, 3, 7))
check_true("f never 1", all(f(u, v) != 1 for u in range(-20, 21) for v in range(-20, 21)))
rep1 = lambda n: any(n - 5 * y * y >= 0 and math.isqrt(n - 5 * y * y) ** 2 == n - 5 * y * y for y in range(0, math.isqrt(n // 5) + 1))
check_true("29=9+20, 41=36+5, 61=16+45", rep1(29) and rep1(41) and rep1(61))
check_true("6=1+5, 14=9+5, 46=1+45, 86=81+5", all(rep1(2 * p) for p in (3, 7, 23, 43)))
for p in primerange(3, 3000):
    if p == 5: continue
    check_true(f"p={p}: x^2+5y^2 iff p=1,9 mod 20", rep1(p) == (p % 20 in (1, 9))) if p < 60 else None
bad = [p for p in primerange(3, 20000) if p != 5 and rep1(p) != (p % 20 in (1, 9))]
check_true("x^2+5y^2 iff p=1,9 mod 20, all p < 20000", not bad)
# split/second form for split primes
bad2 = [p for p in primerange(3, 5000) if p != 5 and legendre_symbol((-5) % p, p) == 1 and
        rep1(p) == any(f(u, v) == p for u in range(-80, 81) for v in range(-80, 81))]
check_true("each split prime is represented by exactly one of the two forms (p<5000)", not bad2)
check_true("x^2+5 = y^3: no solution |x| < 10^5", all(round((x * x + 5) ** (1 / 3)) ** 3 != x * x + 5 for x in range(100000)))
finish()
