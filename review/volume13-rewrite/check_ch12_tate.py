"""Volume 13, Chapter 12 (Tate's thesis): the functional equation of Corollary dirichletFE checked numerically for
primitive characters modulo 3, 4, 5, 7, 8 (including complex ones), the root numbers of Exercise rootnumber, the local
integral (1-1/p)/(1-p^{-1-s}), the Hecke residue normalisation, the constant C_K of the adelic Minkowski lemma."""
import cmath, math
import mpmath as mp
from common import check, check_true, finish
mp.mp.dps = 30
def make_chars(N):
    import sympy
    units = [a for a in range(1, N) if math.gcd(a, N) == 1]
    res = []
    if N == 8:
        tabs = [{1: 1, 3: -1, 5: -1, 7: 1}, {1: 1, 3: 1, 5: -1, 7: -1}]  # (8/.) even? and (-8/.)
        for t in tabs: res.append([t.get(a % 8, 0) for a in range(N)])
        return res
    g = sympy.primitive_root(N); phi = len(units)
    for k in range(1, phi):
        w = cmath.exp(2j * math.pi * k / phi)
        tab = [0] * N
        for e in range(phi): tab[pow(g, e, N)] = w**e
        # primitive iff not induced from a divisor: for prime N or N=4 every nontrivial char is primitive
        res.append(tab)
    return res
def Lam(s, chi, N):
    a = 0 if abs(chi[N - 1] - 1) < 1e-9 else 1
    L = mp.dirichlet(s, [mp.mpc(c) for c in chi])
    return mp.pi**(-(s + a) / 2) * mp.gamma((s + a) / 2) * L, a
ok = True
for N in [3, 4, 5, 7, 8]:
    for chi in make_chars(N):
        cb = [complex(c).conjugate() for c in chi]
        tau_cb = sum(cb[c] * cmath.exp(2j * math.pi * c / N) for c in range(N))
        for s in [mp.mpf('0.3') + 2j, mp.mpf('0.7') - 1j, mp.mpf('2.5')]:
            lhs, a = Lam(s, cb, N)
            rhs, _ = Lam(1 - s, chi, N)
            rhs = (-1j)**a * tau_cb * mp.power(N, -s) * rhs
            if abs(lhs - rhs) > 1e-15 * max(1, abs(lhs)): ok = False; print("FE fails", N, chi, s, lhs, rhs)
check_true("Lambda(s, chibar) = (-i)^a tau(chibar) N^-s Lambda(1-s, chi) for all primitive chi mod 3,4,5,7,8", ok)
# root numbers of real characters
def tau(chi, N): return sum(chi[c] * cmath.exp(2j * math.pi * c / N) for c in range(N))
real = {3: [0, 1, -1], 4: [0, 1, 0, -1], 5: [0, 1, -1, -1, 1], 8: [0, 1, 0, -1, 0, -1, 0, 1]}
for N, chi in real.items():
    a = 0 if chi[N - 1] == 1 else 1
    eps = tau(chi, N) / (1j**a * math.sqrt(N))
    check(f"root number of the real character mod {N}", abs(eps - 1), 0, 1e-12)
check("tau mod 3 = i sqrt3", abs(tau(real[3], 3) - 1j * math.sqrt(3)), 0, 1e-12)
check("tau mod 8 = sqrt8", abs(tau(real[8], 8) - math.sqrt(8)), 0, 1e-12)
check("cos(2pi/5) = (sqrt5-1)/4", math.cos(2 * math.pi / 5), (math.sqrt(5) - 1) / 4, 1e-15)
# local integral
p, s = 3, 0.7
lhs = sum(p**(-k * s) * p**(-k) * (1 - 1 / p) for k in range(200))
check("int_{Z_p} |x|^s dx = (1-1/p)/(1-p^{-1-s})", lhs, (1 - 1 / p) / (1 - p**(-1 - s)), 1e-12)
check("Gamma_R(1)=1, Gamma_C(1)=1/pi", float(mp.pi**-0.5 * mp.gamma(0.5)) * math.pi * float(2 * (2 * mp.pi)**-1), 1, 1e-12)
check_true("C_K exponent: 2^{n-r1-r2} pi^{-r2} = (2/pi)^{r2} for n = r1 + 2 r2",
           all(abs(2**(r1 + 2 * r2 - r1 - r2) * math.pi**(-r2) - (2 / math.pi)**r2) < 1e-12 for r1 in range(4) for r2 in range(4)))
finish()
