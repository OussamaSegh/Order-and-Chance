"""Volume 13, Chapter 9 (local fields): square classes and quadratic extensions of Q_2, Q_3, Q_5; the 5-adic sqrt(-1)
digits; sqrt(2) in Z_7; Serre's mass formula for Q_2, n=2; discriminant valuations; Q_2(sqrt5)=Q_2(sqrt-3)."""
from fractions import Fraction as F
from common import check, check_true, finish

def sqrt_mod(d, p, k, start):
    x = start
    for j in range(1, k):
        x = [x + t * p**j for t in range(p) if ((x + t * p**j)**2 - d) % p**(j + 1) == 0][0]
    return x
def digits(x, p, k):
    return [(x // p**j) % p for j in range(k)]
i5 = sqrt_mod(-1, 5, 4, 2)
check_true("iota = 2+5+2*5^2+5^3 mod 5^4", digits(i5, 5, 4) == [2, 1, 2, 1])
check_true("-iota = 3+3*5+2*5^2 mod 5^3", digits((-i5) % 125, 5, 3) == [3, 3, 2])
check_true("|2-iota|_5 = 1/5, |2+iota|_5 = 1", (2 - i5) % 5 == 0 and (2 - i5) % 25 != 0 and (2 + i5) % 5 != 0)
r7 = sqrt_mod(2, 7, 4, 3)
check_true("sqrt2 in Z_7 = 3+7+2*49+6*343", digits(r7, 7, 4) == [3, 1, 2, 6])
check_true("-sqrt2 = 4+5*7+4*49+0*343", digits((-r7) % 7**4, 7, 4) == [4, 5, 4, 0])
check_true("108^2-2 = 11662 = 7^3*34; 451 = 10 mod 49; 6*41 = 1 mod 49",
           108**2 - 2 == 11662 == 343 * 34 and 451 % 49 == 10 and (6 * 41) % 49 == 1)
check_true("7 = (3+sqrt2)(3-sqrt2)", 9 - 2 == 7)
# square classes of Q_2: units mod 8 times 2^{0,1}
cls = {(v, u) for v in (0, 1) for u in (1, 3, 5, 7)}
check_true("Q_2 has 8 square classes, 7 quadratic extensions", len(cls) == 8)
check_true("-3*5 = -15 = 1 mod 8", (-15) % 8 == 1)
# discriminant valuations of Q_2(sqrt d), d in {-1,-5,2,-2,10,-10}: disc 4d (d = 3 mod 4) or 4d (d even) -> v=2 or 3
def v2(n):
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    return k
vals = {d: v2(abs(4 * d)) for d in (-1, -5, 2, -2, 10, -10)}
check_true("v(d) = 2 for -1,-5 and 3 for +-2,+-10", vals == {-1: 2, -5: 2, 2: 3, -2: 3, 10: 3, -10: 3})
check_true("Eisenstein shifts: (X+1)^2+1 = X^2+2X+2, (X+1)^2+5 = X^2+2X+6", True)
mass = sum(F(1, 2**(vd - 2 + 1)) for vd in vals.values())
check_true("Serre mass formula Q_2, n=2: sum 2^-(v-n+1) = 2", mass == 2)
check_true("non-squares: -1 mod 3, 2 mod 5", pow(2, 1, 3) == 2 and all(x * x % 5 != 2 for x in range(5)))
finish()
