#!/usr/bin/env python3
"""Volume 14, Chapter 9 (bounded gaps): every printed number not proved on the page.

Includes the certificate for Proposition prop:mk582 (M_582 > 4 from Lemma lem:productF
with A=7, T=39) and the admissible tuple of Theorem thm:explicitgap.
"""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish
from fractions import Fraction as Fr
from math import factorial as fa, comb
from mpmath import mp, mpf, log, sqrt, matrix, eig, lu_solve
import sympy

mp.dps = 50
def product_bound(k, A, T):
    A, T = mpf(A), mpf(T); V = 1 + A * T
    g = T / V; L = log(V) / A
    mu = (log(V) - 1 + 1 / V) / (g * A**2)
    m2 = (V - 2 * log(V) - 1 / V) / (g * A**3)
    var = m2 - mu**2; d = k - T - (k - 1) * mu
    return dict(V=V, g=g, L=L, LL=L * L / g, mu=mu, m2=m2, var=var, d=d,
                r=(k - 1) * var / d**2, bound=L * L / g * (1 - (k - 1) * var / d**2))

# --- Proposition mk582 and Exercise mk581
b = product_bound(582, 7, 39)
check("log 274", log(274), 5.6131281, 1e-7)
check("gamma=39/274", b["g"], 0.1423357, 1e-7)
check("L", b["L"], 0.8018754, 1e-7)
check("L^2/gamma", b["LL"], 4.5175168, 1e-7)
check("mu", b["mu"], 0.6619555, 1e-7)
check("m2", b["m2"], 5.3822984, 1e-7)
check("sigma^2", b["var"], 4.9441132, 1e-7)
check("delta", b["d"], 158.40381, 1e-5)
check("(k-1)sigma^2/delta^2", b["r"], 0.1144809, 1e-7)
check("1-ratio", 1 - b["r"], 0.8855190, 1e-7)
check("bound k=582", b["bound"], 4.000347, 1e-6)
check_true("M_582 > 4 with margin > 3e-4", b["bound"] - 4 > mpf("3e-4"))
b581 = product_bound(581, 7, 39); b600 = product_bound(600, 7, 39)
check("delta k=581", b581["d"], 158.0657, 1e-4)
check("ratio k=581", b581["r"], 0.11477, 1e-5)
check("1-ratio k=581", 1 - b581["r"], 0.88523, 1e-5)
check("bound k=581", b581["bound"], 3.99903, 1e-5)
check("delta k=600", b600["d"], 164.4886, 1e-4)
check("ratio k=600", b600["r"], 0.10946, 1e-5)
check("bound k=600", b600["bound"], 4.02304, 1e-5)
check("sigma", sqrt(b["var"]), 2.22, 0.005)

# --- Theorem explicitgap: the tuple
ps = []; p = 582
while len(ps) < 582:
    p = sympy.nextprime(p); ps.append(p)
check("H_582 first", ps[0], 587, 0); check("H_582 last", ps[-1], 5167, 0)
check("diameter", ps[-1] - ps[0], 4580, 0)
check_true("H_582 admissible", all(len({h % q for h in ps}) < q for q in sympy.primerange(2, 600)))

# --- Proposition mklower: where log k - 2 log log k - 2 passes 4
f = lambda k: math.log(k) - 2 * math.log(math.log(k)) - 2
k = 100
while f(k) <= 4: k += 1
check_true(f"log k - 2loglog k - 2 passes 4 at k={k}, near 4*10^4", 3e4 < k < 5e4)

# --- Figure chance, k=200
k = 200; A = math.log(k) - 2 * math.log(math.log(k)); T = (math.exp(A) - 1) / A
check("fig chance A", A, 1.964, 5e-4); check("fig chance T", T, 3.119, 5e-4)
bb = product_bound(k, A, T)
check("fig chance mu", bb["mu"], 0.654, 5e-4)
check("fig chance mean of sum", 199 * bb["mu"], 130.1, 0.05)
check("fig chance sd of sum", sqrt(199 * bb["var"]), 9.9, 0.05)
check("fig chance threshold", k - T, 196.9, 0.05)

# --- Theorem mfive: exact rationals for k=5
def bracket(k, a, b):
    """<a,b>_k of Lemma symint, exactly."""
    # coefficient of x^b in (sum_j (2j)!/j! x^j)^k
    poly = [Fr(1)] + [Fr(0)] * b
    base = [Fr(fa(2 * j), fa(j)) for j in range(b + 1)]
    for _ in range(k):
        new = [Fr(0)] * (b + 1)
        for i, c in enumerate(poly):
            if c:
                for j in range(b + 1 - i):
                    new[i + j] += c * base[j]
        poly = new
    return Fr(fa(a) * fa(b), fa(k + a + 2 * b)) * poly[b]
def inner(a, b):
    """int_0^u (u-t)^a (P2'+t^2)^b dt as {(a', b'): coeff} in (1-P1')^a' P2'^b'."""
    return {(a + 2 * j + 1, b - j): Fr(comb(b, j) * fa(a) * fa(2 * j), fa(a + 2 * j + 1)) for j in range(b + 1)}
def forms(k, mons):
    n = len(mons)
    I = [[bracket(k, mons[i][0] + mons[j][0], mons[i][1] + mons[j][1]) for j in range(n)] for i in range(n)]
    inn = [inner(*m) for m in mons]
    J = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t = Fr(0)
            for (a1, b1), c1 in inn[i].items():
                for (a2, b2), c2 in inn[j].items():
                    t += c1 * c2 * bracket(k - 1, a1 + a2, b1 + b2)
            J[i][j] = k * t
    return I, J
mons5 = [(1, 1), (2, 0), (0, 1), (1, 0)]
coef = [Fr(1), Fr(7, 10), Fr(1, 14), Fr(-3, 14)]
I, J = forms(5, mons5)
q = lambda M: sum(coef[i] * coef[j] * M[i][j] for i in range(4) for j in range(4))
check_true("I_5(F) = 29509/1222452000", q(I) == Fr(29509, 1222452000))
check_true("sum J_5(F) = 40493/838252800", q(J) == Fr(40493, 838252800))
check_true("ratio = 1417255/708216", q(J) / q(I) == Fr(1417255, 708216))
check("ratio decimal", float(Fr(1417255, 708216)), 2.00116, 5e-6)
check("theta threshold", float(Fr(2 * 708216, 1417255)), 0.99942, 5e-6)

# --- Figure mk: best polynomial of degree <= 11 in P1, P2 (42 monomials)
mons = [(a, b) for b in range(6) for a in range(12) if a + 2 * b <= 11]
check("number of monomials", len(mons), 42, 0)
def top(k):
    I, J = forms(k, mons)
    mp.dps = 80
    Im = matrix([[mpf(x.numerator) / x.denominator for x in r] for r in I])
    Jm = matrix([[mpf(x.numerator) / x.denominator for x in r] for r in J])
    E = eig(Im**-1 * Jm)[0]
    return max(e.real for e in E)
for kk, val, tol in [(2, 1.38593, 5e-6), (5, 2.0041, 5e-5), (105, 4.0021, 5e-5)]:
    check(f"degree-11 ratio k={kk}", top(kk), val, tol)
check_true("degree-11 ratio < 2 at k=4", top(4) < 2)
check_true("degree-11 ratio < 4 at k=70", top(70) < 4)
check("eigenvalue k=105 (Maynard)", top(105), 4.0020697, 1e-7)
check("2 log 2", 2 * math.log(2), 1.38629, 5e-6)

# --- Exercise mtwo
c = (-2 + math.sqrt(34)) / 3
check("c", c, 1.2770, 5e-5)
check("rho(c)", (40 + 30 * c + 6 * c * c) / (5 * (6 + 4 * c + c * c)), 1.38310, 5e-6)
finish()
