#!/usr/bin/env python3
"""Numerical checks for Volume 5, Chapter 8 (The Fourier Transform and Poisson Summation)."""
from mpmath import mp, mpf, mpc, pi, exp, sqrt, cos, sin, quad, quadosc, nsum, inf, coth, zeta, gamma, floor, log10, sinc, diff, jacobi

mp.dps = 160
ok = True
def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)
def close(a, b, tol=mpf(10) ** -12):
    return abs(a - b) <= tol * max(1, abs(b))
def ft(f, xi, pts):
    return quad(lambda x: f(x) * exp(-2j * pi * x * xi), pts)

# the opening sum
th = lambda t: nsum(lambda n: exp(-pi * n * n * t), [-inf, inf])
S = th(mpf(1) / 100)
err = S - 10
print("     theta(0.01) - 10 =", mp.nstr(err, 5))
check("theta(0.01) = 10 theta(100), error 20 e^(-100 pi) ~ 7e-136, 135 zeros", close(err, 20 * exp(-100 * pi), mpf(10) ** -8) and floor(-log10(err)) == 135 and abs(err / mpf('7e-136') - 1) < 0.05)
check("theta(100) - 1 is about 1e-136", mpf('1e-137') < 2 * exp(-100 * pi) < mpf('1e-135'))
mp.dps = 30
for t in (mpf('0.3'), mpf(2), mpf('7.5')):
    check(f"theta(1/t) = sqrt(t) theta(t), t={t}", close(th(1 / t), sqrt(t) * th(t)))
check("terms beyond |n| = 40 are below 1e-21 for t = 0.01", exp(-pi * 1600 / 100) < mpf(10) ** -21)

# Gaussian transforms
for a in (mpf('0.5'), 1, 2):
    for xi in (mpf('0.3'), mpf('1.1')):
        check(f"transform of exp(-pi x^2/a^2), a={a}, xi={xi}", close(ft(lambda x: exp(-pi * x * x / a**2), xi, [-inf, 0, inf]), a * exp(-pi * a * a * xi * xi)))
t = mpf('0.2'); H = lambda x: exp(-x * x / (4 * t)) / sqrt(4 * pi * t)
check("heat kernel: integral 1, transform exp(-4 pi^2 t xi^2)", close(quad(H, [-inf, 0, inf]), 1) and close(ft(H, mpf('0.4'), [-inf, 0, inf]), exp(-4 * pi**2 * t * mpf('0.16'))))
x0 = mpf('0.7')
check("heat kernel solves the heat equation", close(diff(lambda tt: exp(-x0**2 / (4 * tt)) / sqrt(4 * pi * tt), t), diff(H, x0, 2), mpf(10) ** -10))

# triangle function and the sin^2 sum
for xi in (mpf('0.37'), mpf('2.2')):
    check(f"transform of the triangle at {xi}", close(ft(lambda x: 1 - abs(x), xi, [-1, 0, 1]), (sin(pi * xi) / (pi * xi)) ** 2))
x = mpf('0.23')
check("sum 1/(x+n)^2 = pi^2/sin^2(pi x)", close(nsum(lambda n: 1 / (x + n) ** 2, [-inf, inf]), pi**2 / sin(pi * x) ** 2, mpf(10) ** -10))
check("cotangent partial fractions", close(pi * cos(pi * x) / sin(pi * x), 1 / x + nsum(lambda n: 2 * x / (x * x - n * n), [1, inf]), mpf(10) ** -10))

# Fresnel integral and Gauss sums
# u = v^2 turns the integral into 2 int_0^oo exp(i v^2) dv, a pair of Fresnel integrals
J0 = 2 * sqrt(pi / 2) * (mp.fresnelc(inf) + 1j * mp.fresnels(inf))
J0num = 2 * (quadosc(lambda v: cos(v * v), [0, inf], zeros=lambda n: sqrt(pi * n)) + 1j * quadosc(lambda v: sin(v * v), [0, inf], zeros=lambda n: sqrt(pi * n)))
check('Fresnel integrals by direct quadrature', close(J0num, J0, mpf(10) ** -8))
check("int u^(-1/2) e^(iu) = sqrt(pi) e^(i pi/4)", close(J0, sqrt(pi) * exp(1j * pi / 4), mpf(10) ** -8))
check("K(0) = Gamma(1/2) t^(-1/2)", close(quad(lambda u: exp(-t * u) / sqrt(u), [0, 1, inf]), gamma(mpf(1) / 2) / sqrt(t), mpf(10) ** -10))
zz = mpc(t, -1)
check("int u^(-1/2) e^(-zu) = sqrt(pi)/sqrt(z) for z = t - i", close(quad(lambda u: exp(-zz * u) / sqrt(u), [0, 1, 10, inf]), sqrt(pi) / sqrt(zz), mpf(10) ** -10))
good = True
for n in range(1, 60):
    G = sum(exp(2j * pi * k * k / n) for k in range(n))
    val = [(1 + 1j) * sqrt(n), sqrt(n), 0, 1j * sqrt(n)][n % 4]
    good &= abs(G - val) < mpf(10) ** -15 and abs(G - (1 + 1j) * (1 + mpc(0, 1) ** (-n)) / 2 * sqrt(n)) < mpf(10) ** -15
check("Gauss sums G(n), n < 60, all four cases", good)
def leg(a, p):
    r = pow(a % p, (p - 1) // 2, p); return -1 if r == p - 1 else r
good = True
primes = [3, 5, 7, 11, 13, 17, 19, 23]
for p in primes:
    for q in primes:
        if p != q:
            Gq_p = sum(exp(2j * pi * q * k * k / p) for k in range(p)); Gp_q = sum(exp(2j * pi * p * k * k / q) for k in range(q))
            Gpq = sum(exp(2j * pi * k * k / (p * q)) for k in range(p * q))
            good &= abs(Gpq - Gq_p * Gp_q) < mpf(10) ** -12 and leg(p, q) * leg(q, p) == (-1) ** ((p - 1) // 2 * ((q - 1) // 2))
            good &= abs(Gq_p - leg(q, p) * sum(exp(2j * pi * k * k / p) for k in range(p))) < mpf(10) ** -12
check("G(pq) = G_q(p) G_p(q), G_a(p) = (a/p) G(p), reciprocity", good)

# sampling theorem on a band-limited function: f = sinc^2 (band 1, W = 1)
f = lambda x: sinc(pi * x) ** 2 if False else (sin(pi * x) / (pi * x)) ** 2 if x != 0 else mpf(1)
W = 1; xx = mpf('0.3')
ser = nsum(lambda n: f(n / mpf(2 * W)) * (sin(pi * (2 * W * xx - n)) / (pi * (2 * W * xx - n))), [-inf, inf])
check("Shannon series reproduces sinc^2 at x = 0.3", close(ser, f(xx), mpf(10) ** -6))
check("aliasing figure: 9 cycles sampled 10 times = -1 cycle", all(close(sin(2 * pi * 9 * mpf(k) / 10), sin(-2 * pi * mpf(k) / 10)) for k in range(10)))

# Heisenberg equality
A = quad(lambda x: x * x * exp(-2 * pi * x * x), [-inf, 0, inf]); B = quad(lambda x: exp(-2 * pi * x * x), [-inf, 0, inf])
check("Gaussian: int x^2 f^2 = 1/(4 pi sqrt 2), int f^2 = 1/sqrt 2, equality", close(A, 1 / (4 * pi * sqrt(2))) and close(B, 1 / sqrt(2)) and close(A * A, B * B / (16 * pi**2)))

# exercises
a = mpf('0.8'); xi = mpf('0.6')
check("transform of exp(-2 pi a |x|)", close(ft(lambda x: exp(-2 * pi * a * abs(x)), xi, [-inf, 0, inf]), a / (pi * (a * a + xi * xi))))
check("transform of 1/(1+x^2) is pi exp(-2 pi |xi|)", close(2 * quadosc(lambda x: cos(2 * pi * x * xi) / (1 + x * x), [0, inf], omega=2 * pi * xi), pi * exp(-2 * pi * xi), mpf(10) ** -8))
check("transform of x exp(-pi x^2) is -i xi exp(-pi xi^2)", close(ft(lambda x: x * exp(-pi * x * x), xi, [-inf, 0, inf]), -1j * xi * exp(-pi * xi * xi)))
check("sum 1/(n^2+a^2) = (pi/a) coth(pi a)", close(nsum(lambda n: 1 / (n * n + a * a), [-inf, inf]), pi / a * coth(pi * a), mpf(10) ** -10))
sm = mpf('0.001')
check("limit a -> 0 gives zeta(2)", abs(pi / (2 * sm) * coth(pi * sm) - 1 / (2 * sm * sm) - zeta(2)) < 1e-5)
L = mpf(3); g = lambda x: exp(-pi * x * x); xs = mpf('0.4')
check("Poisson with period L", close(nsum(lambda n: g(xs + n * L), [-inf, inf]), nsum(lambda m: g(m / L) * exp(2j * pi * m * xs / L), [-inf, inf]) / L))

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
