"""Volume 13, Chapter 13 (class field theory): x^2+27y^2 and cubes, eta(6z)eta(18z), x^2+14y^2 and X^4+2X^2-7,
x^2+5y^2 modulo 20, h(-56)=4, density 1/6 for x^2+27y^2, and the Hilbert class field of Q(sqrt-5) (PARI)."""
import sympy, cypari2
from common import check, check_true, finish
pari = cypari2.Pari()
def rep(p, n):
    return any(((p - n * y * y) >= 0 and sympy.ntheory.primetest.is_square(p - n * y * y)) for y in range(0, int((p / n) ** .5) + 1))
ps1 = [p for p in sympy.primerange(5, 200) if p % 3 == 1 and rep(p, 27)]
check_true("first primes x^2+27y^2: 31, 43, 109, 127, 157", ps1[:5] == [31, 43, 109, 127, 157])
ok = all(rep(p, 27) == (pow(2, (p - 1) // 3, p) == 1) for p in sympy.primerange(5, 20000) if p % 3 == 1)
check_true("p = 1 mod 3: x^2+27y^2 iff 2 is a cube (p < 20000)", ok)
def nroots(p): return sum(1 for x in range(p) if (x**3 - 2) % p == 0)
ok = all((nroots(p) == 3) == rep(p, 27) and (nroots(p) == 1) == (p % 3 == 2) for p in sympy.primerange(5, 3000))
check_true("X^3-2: three roots iff x^2+27y^2, one iff p = 2 mod 3", ok)
ps = list(sympy.primerange(5, 200000))
check("density of x^2+27y^2 (1/6)", sum(1 for p in ps if p % 3 == 1 and pow(2, (p - 1) // 3, p) == 1) / len(ps), 1 / 6, 0.005)
# eta(6z) eta(18z) = q prod (1-q^6n)(1-q^18n)
N = 2000
c = [0] * (N + 1); c[0] = 1
for n in range(1, N // 6 + 1):
    for m in (6 * n, 18 * n):
        if m > N: continue
        for k in range(N, m - 1, -1): c[k] -= c[k - m]
a = lambda k: c[k - 1]
ok = all(a(p) == (0 if p % 3 == 2 else (2 if rep(p, 27) else -1)) for p in sympy.primerange(5, N))
check_true("a_p of eta(6z)eta(18z) = 2, -1, 0 as in the text (p < 2000)", ok)
# x^2 + 5y^2
ok = all(rep(p, 5) == (p % 20 in (1, 9)) for p in sympy.primerange(3, 20000) if p != 5)
check_true("p = x^2+5y^2 iff p = 1, 9 mod 20", ok)
check_true("h(-20) = 2, h(-56) = 4", int(pari("qfbclassno(-20)")) == 2 and int(pari("qfbclassno(-56)")) == 4)
# x^2+14y^2
p14 = [p for p in sympy.primerange(3, 200) if p != 7 and rep(p, 14)]
check_true("x^2+14y^2 below 200: 23, 127, 137, 151", p14 == [23, 127, 137, 151])
def crit(p):
    return sympy.legendre_symbol((-14) % p, p) == 1 and any(((x*x + 1)**2 - 8) % p == 0 for x in range(p))
check_true("criterion for x^2+14y^2 for p < 20000", all(rep(p, 14) == crit(p) for p in sympy.primerange(3, 20000) if p != 7))
check_true("(3^2+1)^2 = 100 = 4*23 + 8; 127, 137, 151 decompositions", 100 == 4 * 23 + 8 and 127 == 1 + 14 * 9 and 137 == 81 + 14 * 4 and 151 == 25 + 14 * 9)
check_true("alpha = sqrt(2 sqrt2 - 1) is a root of X^4+2X^2-7", abs((2 * 2**.5 - 1)**2 + 2 * (2 * 2**.5 - 1) - 7) < 1e-12)
rel = pari("rnfinit(nfinit(y^2+14), x^4+2*x^2-7)")
check_true("K(alpha)/K unramified for K = Q(sqrt-14): relative discriminant trivial",
           int(pari("(r)->idealnorm(r.nf, r.disc[1])")(rel)) == 1)
check_true("Q(i, sqrt5)/Q(sqrt-5) unramified", int(pari("idealnorm(nfinit(y^2+5), rnfdisc(nfinit(y^2+5), x^2+1)[1])")) == 1)
finish()
