"""Number checks for Volume 6, Chapter 3 (Dirichlet characters and L-functions)."""
import math
from common import check, check_true, finish

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

# L(1, chi) for chi_{-3}, chi_{-4}, chi_5: closed forms against the series.
def L1(chi, q, periods=200000):
    s = 0.0
    for k in range(periods):          # sum whole periods, so the tail is O(1/N^2)-small after pairing
        base = k * q
        s += sum(chi[a] / (base + a) for a in range(1, q))
    return s

chi3 = {1: 1, 2: -1}
chi4 = {1: 1, 2: 0, 3: -1}
chi5 = {1: 1, 2: -1, 3: -1, 4: 1}
phi = (1 + math.sqrt(5)) / 2
check("L(1,chi_-3) = pi/(3 sqrt 3)", math.pi / (3 * math.sqrt(3)), 0.6046, 5e-5)
check("L(1,chi_-4) = pi/4", math.pi / 4, 0.7854, 5e-5)
check("L(1,chi_5) = (2/sqrt5) log phi", 2 / math.sqrt(5) * math.log(phi), 0.4304, 5e-5)
check("series for chi_-3", L1(chi3, 3), math.pi / (3 * math.sqrt(3)), 1e-5)
check("series for chi_-4", L1(chi4, 4), math.pi / 4, 1e-5)
check("series for chi_5", L1(chi5, 5), 2 / math.sqrt(5) * math.log(phi), 1e-5)
check("sin(2pi/5)/sin(pi/5) = golden ratio", math.sin(2 * math.pi / 5) / math.sin(math.pi / 5), phi, 1e-12)

# Figure: the walk of the Legendre symbol modulo 1019.
p = 1019
S, walk = 0, [0]
for n in range(1, p):
    S += legendre(n, p)
    walk.append(S)
check_true("1019 = 3 mod 4", p % 4 == 3)
check_true("walk symmetric: S(p-1-N) = S(N)", all(walk[p - 1 - N] == walk[N] for N in range(p)))
check("maximum of the walk", max(walk), 39, 0)
check("value at N = 509", walk[509], 39, 0)
h = -sum(legendre(a, p) * a for a in range(1, p)) / p
check("class number h(-1019) from the formula", h, 13, 1e-12)
check("(2 - (2/p)) h", (2 - legendre(2, p)) * h, 39, 1e-12)
check("L(1,chi) = pi h / sqrt p against the series",
      sum(legendre(n, p) / n for n in range(1, 400 * p + 1)), math.pi * 13 / math.sqrt(p), 1e-4)

# Exercise on primitive roots modulo 7 (solution, part (c)).
import cmath
w = cmath.exp(2j * math.pi / 6)
idx = {pow(3, k, 7): k for k in range(6)}
def indicator(n):
    tot = 0
    for e, mu in ((1, 1), (2, -1), (3, -1), (6, 1)):
        inner = sum(w ** (j * idx[n]) for j in range(6) if j % (6 // e) == 0)
        tot += mu / e * inner
    return tot.real
prim = {n for n in range(1, 7) if len({pow(n, k, 7) for k in range(6)}) == 6}
check_true("primitive roots mod 7 are 3 and 5", prim == {3, 5})
for n in range(1, 7):
    check("indicator at n=%d" % n, indicator(n), 1 if n in prim else 0, 1e-12)

finish()
