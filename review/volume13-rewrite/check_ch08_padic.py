"""Volume 13, Chapter 8 (p-adic numbers): valuations of 75/14, product formulas, the 5-adic lift of sqrt(-1), the roots of
X^2+7 modulo 256 and their 2-adic lifts, Newton iterates for sqrt(-7), Teichmueller omega(2) in Z_5, digit expansions,
the local-everywhere polynomial (X^2-2)(X^2-17)(X^2-34), Haar measure of the squares."""
from fractions import Fraction as F
import random
import sympy
from common import check, check_true, finish

def v(x, p):
    x = F(x)
    if x == 0: return None
    n, d, k = x.numerator, x.denominator, 0
    while n % p == 0: n //= p; k += 1
    while d % p == 0: d //= p; k -= 1
    return k
absp = lambda x, p: F(p) ** (-v(x, p))
check_true("v_5(75/14)=2, v_7(75/14)=-1", v(F(75, 14), 5) == 2 and v(F(75, 14), 7) == -1)
x = F(75, 14)
check_true("product formula for 75/14", x * absp(x, 2) * absp(x, 3) * absp(x, 5) * absp(x, 7) == 1
           and (absp(x, 2), absp(x, 3), absp(x, 5), absp(x, 7)) == (2, F(1, 3), F(1, 25), 7))
check_true("|26-1|_5 = 5^-2, |126-1|_5 = 5^-3", absp(25, 5) == F(1, 25) and absp(125, 5) == F(1, 125))
check_true("|15|_3 = 1/3, |9|_3=1/9, |6|_3=1/3", absp(15, 3) == F(1, 3) and absp(9, 3) == F(1, 9) and absp(6, 3) == F(1, 3))
check_true("1/3 = 42 mod 125 in Z_5, digits 2,3,1", (3 * 42) % 125 == 1 and 42 == 2 + 3 * 5 + 1 * 25)
# lifting sqrt(-1) in Z_5 from 2
b, reps = 2, [2]
for k in range(1, 4):
    t = [t for t in range(5) if ((b + t * 5**k)**2 + 1) % 5**(k + 1) == 0]
    assert len(t) == 1; b = b + t[0] * 5**k; reps.append(b)
check_true("lifts 2, 7, 57, 182 with digits 2,1,2,1", reps == [2, 7, 57, 182])
roots256 = [a for a in range(256) if (a * a + 7) % 256 == 0]
check_true("X^2+7 roots mod 256: 53, 75, 181, 203", roots256 == [53, 75, 181, 203])
lift = lambda r: [a for a in range(r, 2**20, 256) if (a * a + 7) % 2**20 == 0]
check_true("only 75 and 181 are residues of 2-adic roots", [r for r in roots256 if lift(r)] == [75, 181])
check_true("53 and 203 do not lift to roots mod 512",
           all(((r + e) ** 2 + 7) % 512 for r in (53, 203) for e in (0, 256)))
a = F(1); its = [a]
for _ in range(4):
    a = a - (a * a + 7) / (2 * a); its.append(a)
check_true("Newton from 1: 1, -3, -1/3, 31/3, 449/93", its == [1, -3, F(-1, 3), F(31, 3), F(449, 93)])
check_true("a4^2+7 = 2^18/93^2", its[4] ** 2 + 7 == F(2**18, 93**2))
check_true("449/93 = 181 mod 256; 181^2+7=2^15; 181=10110101b; 75=01001011b",
           (449 * pow(93, -1, 256)) % 256 == 181 and 181**2 + 7 == 2**15 and format(181, '08b') == '10110101' and format(75, '08b') == '01001011')
a = F(3); its3 = [a]
for _ in range(3):
    a = a - (a * a + 7) / (2 * a); its3.append(a)
check_true("Newton from 3: 3, 1/3, -31/3, -449/93", its3 == [3, F(1, 3), F(-31, 3), F(-449, 93)])
check_true("omega(2) in Z_5 = 2^25 = 57 mod 125, 57^2 = -1 mod 125", pow(2, 25, 125) == 57 and (57 * 57 + 1) % 125 == 0)
def digits(x, p, n):
    out = []
    for _ in range(n):
        d = (x.numerator * pow(x.denominator, -1, p)) % p; out.append(d); x = (x - d) / p
    return out
check_true("2-adic digits of -1/3: 1,0,1,0,...", digits(F(-1, 3), 2, 6) == [1, 0, 1, 0, 1, 0])
check_true("2-adic digits of 1/3: 1,1,0,1,0,1", digits(F(1, 3), 2, 6) == [1, 1, 0, 1, 0, 1])
check_true("5-adic digits of 1/4: 4,3,3,3", digits(F(1, 4), 5, 4) == [4, 3, 3, 3] and 4 * 94 == 3 * 125 + 1)
check_true("partial sums of 4*5^k are -1 mod 5^n", all((4 * sum(5**k for k in range(n)) + 1) % 5**n == 0 for n in range(1, 10)))
# Legendre formula v_p(n!) = (n - s_p(n))/(p-1)
ok = True
for p in [2, 3, 5, 7]:
    for n in range(1, 300):
        m, s = n, 0
        while m: s += m % p; m //= p
        ok &= v(sympy.factorial(n), p) == (n - s) // (p - 1) and (n - s) % (p - 1) == 0
check_true("v_p(n!) = (n - s_p(n))/(p-1)", ok)
check_true("sum_{n<N} n*n! = N! - 1", all(sum(k * sympy.factorial(k) for k in range(N)) == sympy.factorial(N) - 1 for N in range(1, 30)))
# (X^2-2)(X^2-17)(X^2-34) has roots everywhere locally
ok = True
for p in sympy.primerange(3, 3000):
    if p == 17: continue
    ok &= any(sympy.legendre_symbol(a % p, p) == 1 for a in (2, 17, 34) if a % p)
check_true("one of 2, 17, 34 is a square mod p for odd p != 17 (p < 3000)", ok)
check_true("6^2 = 2 mod 17, 17 = 1 mod 8", 36 % 17 == 2 and 17 % 8 == 1)
# Haar measure of squares in Z_p: p/(2(p+1)); p=3: 3/8; p=2: 1/6. Monte Carlo on residues mod p^k
def square_share(p, k):
    N = p**k; cnt = 0
    for x in range(1, N):
        vv = v(x, p)
        if vv >= k - 3: continue  # skip the tiny tail
        u = x // p**vv
        if vv % 2 == 0 and ((p > 2 and sympy.legendre_symbol(u % p, p) == 1) or (p == 2 and u % 8 == 1)): cnt += 1
    return cnt / N
check("measure of squares in Z_3 (3/8)", square_share(3, 10), 3 / 8, 2e-3)
check("formula p/(2(p+1)) at p=3", 3 / (2 * 4), 0.375, 1e-12)
check("measure of squares in Z_2 (1/6)", square_share(2, 18), 1 / 6, 2e-3)
check("measure of squares in Z_5 = 5/12", square_share(5, 7), 5 / 12, 2e-3)
finish()
