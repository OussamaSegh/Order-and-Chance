"""Volume 13, Chapter 16 (curves over finite fields): Gauss's counts on x^3+y^3=1, the Hasse figure for y^2=x^3-x+1
(667 primes, max ratio 0.977), the 78 496 primes below 10^6, the F_5 zeta example, the Klein quartic, the moment identity."""
import cypari2, sympy
from common import check, check_true, finish
pari = cypari2.Pari(); pari.allocatemem(2 * 10**8, silent=True)

def fermat3(p):  # projective points of X^3+Y^3=Z^3... text uses x^3+y^3=1 with three points at infinity
    cubes = [pow(x, 3, p) for x in range(p)]
    from collections import Counter
    c = Counter(cubes)
    aff = sum(c[a] * c[(1 - a) % p] for a in range(p))
    inf = sum(1 for t in range(p) if (t ** 3 + 1) % p == 0)
    return aff + inf
for p, L, N in [(7, 1, 9), (13, -5, 9), (31, 4, 36)]:
    M2 = (4 * p - L * L) // 27
    check_true(f"4*{p} = L^2+27M^2 with L={L}, L=1 mod 3", 4 * p - L * L == 27 * M2 and sympy.sqrt(M2).is_integer and L % 3 == 1)
    check(f"x^3+y^3=1 over F_{p}: N", fermat3(p), N, 0)
    check(f"N = p+1+L for p={p}", p + 1 + L, N, 0)

E = pari.ellinit([-1, 1])
check_true("only odd bad prime of y^2=x^3-x+1 is 23 (conductor 92)", int(pari.ellglobalred(E)[0]) == 92)
ps = [p for p in sympy.primerange(3, 5000) if p != 23]
check("primes 3<=p<5000, p!=23", len(ps), 667, 0)
ratios = [abs(int(pari.ellap(E, p))) / (2 * p ** 0.5) for p in ps]
check_true("Hasse holds for all 667", max(ratios) < 1)
check("max |a_p|/2sqrt p", round(max(ratios), 3), 0.977, 0)
check("odd primes below 10^6 other than 23", int(sympy.primepi(10**6)) - 2, 78496, 0)

# Exercise ellNr: F_5
a = int(pari.ellap(E, 5)); check("a_5", a, -2, 0)
E5 = pari.ellinit([-1, 1], pari.ffgen(5 ** 2))
check("N_2 over F_25", int(pari.ellcard(E5)), 32, 0)
E125 = pari.ellinit([-1, 1], pari.ffgen(5 ** 3))
check("N_3 over F_125", int(pari.ellcard(E125)), 104, 0)

# Klein quartic over F_2, F_4, F_8
def klein(r):
    g = pari.ffgen(2 ** r) if r > 1 else None
    if r == 1: F = [pari.Mod(0, 2), pari.Mod(1, 2)]
    else: F = [pari(0) * g] + [g ** k for k in range(2 ** r - 1)]
    pts = 0
    for X in F:
        for Y in F:
            if X ** 3 * Y + Y ** 3 + X == 0: pts += 1   # Z = 1
    for X in F:   # Z = 0: X^3 Y = 0 -> (1:0:0),(0:1:0)
        pass
    return pts + 2
for r, N in [(1, 3), (2, 5), (3, 24)]:
    check(f"Klein quartic N_{r}", klein(r), N, 0)
check_true("N_3 = 8+1+3*5 (Serre bound, floor(2 sqrt 8)=5)", 8 + 1 + 3 * 5 == 24 and int(2 * 8 ** 0.5) == 5)

# moment identity sum s(a,b)^2 = p^2(p-1)
for p in [5, 7, 11, 13]:
    tot = 0
    for A in range(p):
        for B in range(p):
            s = sum(int(sympy.legendre_symbol((x ** 3 + A * x + B) % p, p)) if (x ** 3 + A * x + B) % p else 0 for x in range(p))
            tot += s * s
    check(f"moment identity p={p}", tot, p * p * (p - 1), 0)

# maximal Fermat curve X^{q+1}+Y^{q+1}=Z^{q+1} over F_{q^2}, q=2,3: q^3+1 points
def fermat_max(q):
    g = pari.ffgen(q ** 2); F = [pari(0) * g] + [g ** k for k in range(q * q - 1)]
    e = q + 1
    aff = sum(1 for X in F for Y in F if X ** e + Y ** e == 1)
    inf = sum(1 for t in F if t ** e + 1 == 0)
    return aff + inf
for q in [2, 3]:
    check(f"Fermat curve degree {q+1} over F_{q*q}", fermat_max(q), q ** 3 + 1, 0)

finish()
