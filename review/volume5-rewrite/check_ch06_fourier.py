#!/usr/bin/env python3
"""Numerical checks for Volume 5, Chapter 6 (Fourier Series)."""
import random
from math import comb
from mpmath import mp, mpf, pi, sin, cos, exp, log, quad, si, sqrt, zeta, mpc, fsum, floor

mp.dps = 25
ok = True
def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)
def close(a, b, tol=1e-10):
    return abs(a - b) <= tol * max(1, abs(b))
def coef(f, n, pts):
    re = quad(lambda t: f(t) * cos(n * t), pts)
    im = quad(lambda t: -f(t) * sin(n * t), pts)
    return mpc(re, im) / (2 * pi)

# opening experiment
def saw(x, N):
    return fsum(sin(n * x) / n for n in range(1, N + 1))
vals = [saw(1, N) for N in (10, 100, 1000)]
print("     partial sums at x=1:", [mp.nstr(v, 6) for v in vals], "limit", mp.nstr((pi - 1) / 2, 6))
check("x=1: 1.1245, 1.0604, 1.0707 -> 1.0708", all(abs(v - mpf(c)) < 6e-5 for v, c in zip(vals, ('1.1245', '1.0604', '1.0707'))) and abs((pi - 1) / 2 - mpf('1.0708')) < 5e-5)
check("x=2: -> (pi-2)/2 = 0.5708", abs(saw(2, 20000) - (pi - 2) / 2) < 1e-3 and abs((pi - 2) / 2 - mpf('0.5708')) < 5e-5)

# sawtooth coefficients
f_saw = lambda t: (pi - t) / 2
for n in (1, 2, 5):
    check(f"sawtooth c_{n} = -i/(2n)", close(coef(f_saw, n, [0, 2 * pi]), mpc(0, -mpf(1) / (2 * n))))
check("Leibniz at x = pi/2", abs(saw(pi / 2, 4001) - pi / 4) < 1e-3)

# kernels
u, N = mpf('0.37'), 8
D = fsum(cos(n * u) for n in range(-N, N + 1))
check("Dirichlet kernel closed form", close(D, sin((N + mpf(1) / 2) * u) / sin(u / 2)))
F = fsum(sin((k + mpf(1) / 2) * u) / sin(u / 2) for k in range(N)) / N
check("Fejer kernel closed form", close(F, (sin(N * u / 2) / sin(u / 2)) ** 2 / N))
check("Fejer kernel has mean 1", close(quad(lambda t: (sin(N * t / 2) / sin(t / 2)) ** 2 / N, [-pi, 0, pi]) / (2 * pi), 1))

# x and x^2, zeta(2), zeta(4)
for n in (1, 2, 3):
    check(f"c_{n}(x) = i(-1)^n/n", close(coef(lambda t: t, n, [-pi, pi]), mpc(0, mpf((-1) ** n) / n)))
    check(f"c_{n}(x^2) = 2(-1)^n/n^2", close(coef(lambda t: t * t, n, [-pi, pi]), mpf(2 * (-1) ** n) / n**2))
check("zeta(2) from x^2 at pi", close(pi**2, pi**2 / 3 + 4 * zeta(2)))
check("zeta(2) from Parseval for x", close(pi**2 / 3, 2 * zeta(2)))
check("zeta(4) from Parseval for x^2", close(pi**4 / 5, pi**4 / 9 + 8 * zeta(4)) and close(zeta(4), pi**4 / 90))

# Gibbs
G = 2 / pi * si(pi)
print("     Si(pi) =", mp.nstr(si(pi), 8), " (2/pi) Si(pi) =", mp.nstr(G, 8))
check("Si(pi) = 1.85194, limit 1.17897, overshoot 0.179 = 8.95% of the jump", abs(si(pi) - mpf('1.85194')) < 5e-6 and floor(G * 10**5) == 117897 and abs(G - 1 - mpf('0.179')) < 5e-4 and abs((G - 1) / 2 - mpf('0.0895')) < 5e-5)
def sq(x, N):
    return 4 / pi * fsum(sin((2 * k - 1) * x) / (2 * k - 1) for k in range(1, N + 1))
check("square wave coefficients 2/(i pi n), n odd", close(coef(lambda t: 1 if t > 0 else -1, 3, [-pi, 0, pi]), mpc(0, -2 / (3 * pi))))
check("S_{2N-1}(pi/2N) -> 1.17897", abs(sq(pi / 4000, 2000) - G) < 1e-5)
x = mpf('0.3'); Nn = 7
dnum = (sq(x + mpf(10) ** -10, Nn) - sq(x - mpf(10) ** -10, Nn)) / (2 * mpf(10) ** -10)
check("derivative = (2/pi) sin(2Nx)/sin x", close(dnum, 2 / pi * sin(2 * Nn * x) / sin(x), 1e-8))
check("sawtooth overshoot Si(pi) - pi/2 = 0.281 = 0.0895 pi", abs(si(pi) - pi / 2 - mpf('0.281')) < 5e-4 and abs(si(pi) / pi - mpf(1) / 2 - mpf('0.0895')) < 5e-5)
check("sawtooth S_N(pi/N) -> Si(pi)", abs(saw(pi / 3000, 3000) - si(pi)) < 1e-3)

# Weyl / Benford
al = float(log(2, 10)); cnt = {1: 0, 7: 0}; Nb = 100000
for n in range(1, Nb + 1):
    d = int(10 ** ((n * al) % 1))
    if d in cnt: cnt[d] += 1
check("Benford: 30.1% start with 1, 5.8% with 7", abs(cnt[1] / Nb - 0.30103) < 2e-3 and abs(cnt[7] / Nb - 0.05799) < 2e-3 and abs(float(log(2, 10)) - 0.301) < 1e-3 and abs(float(log(mpf(8) / 7, 10)) - 0.058) < 1e-3)
phi = (1 + 5 ** 0.5) / 2
good = True
for n in range(2, 61):
    pts = sorted((k * phi) % 1 for k in range(1, n + 1))
    gaps = {round(b - a, 9) for a, b in zip(pts, pts[1:] + [pts[0] + 1])}
    good &= len(gaps) <= 3
check("three-gap theorem for n*phi, n <= 60", good)
good = True
pts = [phi % 1]
for n in range(2, 61):
    sp = sorted(pts); gl = [(b - a, a) for a, b in zip(sp, sp[1:] + [sp[0] + 1])]
    big = max(g for g, _ in gl); newp = (n * phi) % 1
    inside = [g for g, a in gl if (newp - a) % 1 < g]
    good &= abs(inside[0] - big) < 1e-9
    pts.append(newp)
check("each new point n*phi falls in a largest gap, n <= 60", good)

# isoperimetric: ellipse-like curve via coefficients
c = {0: mpc(0.3, 0.1), 1: mpc(1, 0), -1: mpc(0.2, 0.1), 2: mpc(0.05, -0.03)}
z = lambda s: fsum(v * exp(1j * n * s) for n, v in c.items())
dz = lambda s: fsum(1j * n * v * exp(1j * n * s) for n, v in c.items())
A = quad(lambda s: (z(s).conjugate() * dz(s)).imag, [0, 2 * pi]) / 2
check("area = pi sum n |c_n|^2", close(A, pi * fsum(n * abs(v) ** 2 for n, v in c.items())))
check("mean |z'|^2 = sum n^2 |c_n|^2", close(quad(lambda s: abs(dz(s)) ** 2, [0, 2 * pi]) / (2 * pi), fsum(n * n * abs(v) ** 2 for n, v in c.items())))

# divergent series exercise
worst = max(abs(fsum(sin(j * xx) / j for j in range(1, n + 1))) for n in (1, 2, 5, 17, 60, 200) for xx in [mpf(k) / 50 for k in range(1, 158)])
check(f"|sum sin(jx)/j| <= 1 + pi (largest seen {mp.nstr(worst, 5)})", worst <= 1 + pi)
check("3 n_k < n_{k+1} for n_k = 2^(k^3)", all(3 * 2 ** (k**3) < 2 ** ((k + 1) ** 3) for k in range(1, 30)))
check("H_n >= ln n", all(fsum(mpf(1) / j for j in range(1, n + 1)) >= log(n) for n in (1, 2, 8, 512)))

# flat polynomials
random.seed(1)
for n in (15, 63):
    eps = [random.choice((-1, 1)) for _ in range(n + 1)]
    mx = max(abs(sum(e * exp(1j * k * th) for k, e in enumerate(eps))) for th in [2 * pi * j / 400 for j in range(400)])
    check(f"random signs n={n}: sqrt(n+1) <= max {mp.nstr(mx, 4)} <= bound", sqrt(n + 1) <= mx + 1e-9 and mx <= 2 * sqrt((n + 1) * log(5 * n * (n + 1))) + pi / 2)

# Rudin-Shapiro
P, Q = [1], [1]
good = True
for k in range(0, 7):
    if k:
        P, Q = P + Q, P + [-q for q in Q]
    good &= len(P) == 2**k and all(abs(a) == 1 for a in P + Q)
    e = lambda m: bin(m & (m >> 1)).count("1")
    good &= all(P[m] == (-1) ** e(m) for m in range(2**k))
    for th in (0.1, 1.3, 2.9):
        zz = exp(1j * mpf(th))
        pv = sum(a * zz**m for m, a in enumerate(P)); qv = sum(a * zz**m for m, a in enumerate(Q))
        good &= close(abs(pv) ** 2 + abs(qv) ** 2, 2 ** (k + 1), 1e-12)
check("Rudin-Shapiro: +-1 coefficients, (-1)^e(m), |P|^2+|Q|^2 = 2^(k+1), k <= 6", good)
P2 = [1, 1, 1, -1]; P3 = [1, 1, 1, -1, 1, 1, -1, 1]
PP, QQ = [1], [1]
for k in range(3):
    PP, QQ = PP + QQ, PP + [-q for q in QQ]
    if k == 1: check("P_2 matches", PP == P2)
    if k == 2: check("P_3 matches", PP == P3)
mx = max(abs(sum(a * exp(1j * m * th) for m, a in enumerate(P))) for th in [2 * pi * j / 2000 for j in range(2000)])
check(f"|P_6| <= sqrt(128) = 11.31 (max seen {mp.nstr(mx, 5)})", mx <= sqrt(128) + 1e-9 and abs(sqrt(128) - mpf('11.31')) < 5e-3)

# Siegel, open cube: Fourier coefficients vanish
check("int_{-1/2}^{1/2} e(-kx) dx = 0 for k != 0", all(abs(quad(lambda t: exp(-2j * pi * k * t), [-0.5, 0.5])) < 1e-15 for k in (1, 2, 5)))

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
