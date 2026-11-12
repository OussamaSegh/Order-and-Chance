#!/usr/bin/env python3
"""Numerical checks for Volume 5, Chapter 7 (The Discrete Fourier Transform and the FFT)."""
import cmath, itertools, math, random
from fractions import Fraction
import numpy as np
from sympy import isprime, primitive_root

ok = True
def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)
def dft(a):
    n = len(a); w = cmath.exp(2j * cmath.pi / n)
    return [sum(a[k] * w ** (-j * k) for k in range(n)) for j in range(n)]
def near(u, v, tol=1e-9):
    return all(abs(x - y) < tol for x, y in zip(u, v))
random.seed(7)

# worked example n = 4
h = dft([1, 2, 3, 4])
check("DFT of (1,2,3,4) = (10, -2+2i, -2, -2-2i)", near(h, [10, -2 + 2j, -2, -2 - 2j]))
check("Parseval: 30 = (100+8+4+8)/4", abs(sum(abs(x) ** 2 for x in h) / 4 - 30) < 1e-9)

# inversion, Parseval, convolution, agreement with numpy convention
for n in (5, 8, 12):
    a = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(n)]
    b = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(n)]
    A, B = dft(a), dft(b); w = cmath.exp(2j * cmath.pi / n)
    check(f"n={n}: same convention as numpy.fft", near(A, np.fft.fft(a)))
    check(f"n={n}: inversion", near([sum(A[j] * w ** (j * k) for j in range(n)) / n for k in range(n)], a))
    check(f"n={n}: Parseval", abs(sum(abs(x) ** 2 for x in a) - sum(abs(x) ** 2 for x in A) / n) < 1e-9)
    conv = [sum(a[l] * b[(k - l) % n] for l in range(n)) for k in range(n)]
    check(f"n={n}: convolution theorem", near(dft(conv), [x * y for x, y in zip(A, B)]))

# aliasing for |x|: coefficients and error bound pi^2 C / n^2
cm = lambda m: 0 if m % 2 == 0 else -2 / (math.pi * m * m)
num = np.trapezoid(np.abs(np.linspace(-math.pi, math.pi, 200001)) * np.cos(3 * np.linspace(-math.pi, math.pi, 200001)), np.linspace(-math.pi, math.pi, 200001)) / (2 * math.pi)
check("c_3(|x|) = -2/(9 pi)", abs(num - cm(3)) < 1e-8)
check("sum 1/(l-1/2)^2 = pi^2/2", abs(sum(1 / (l - 0.5) ** 2 for l in range(1, 10**6)) - math.pi ** 2 / 2) < 1e-5)
for n in (16, 32, 64):
    xs = [2 * math.pi * k / n for k in range(n)]
    f = [abs(x if x <= math.pi else x - 2 * math.pi) for x in xs]
    A = dft(f)
    err = max(abs(A[j % n] / n - (math.pi / 2 if j == 0 else cm(j))) for j in range(-n // 2, n // 2 + 1))
    check(f"aliasing error for |x|, n={n}: {err:.2e} <= pi^2 C/n^2 = {math.pi**2 * (2/math.pi) / n**2:.2e}", err <= math.pi ** 2 * (2 / math.pi) / n ** 2)

# FFT with operation counts
def fft(a, cnt):
    n = len(a)
    if n == 1: return a
    E, O = fft(a[0::2], cnt), fft(a[1::2], cnt)
    w = cmath.exp(-2j * cmath.pi / n); out = [0] * n
    for j in range(n // 2):
        t = w ** j * O[j]; cnt[0] += 1
        out[j] = E[j] + t; out[j + n // 2] = E[j] - t; cnt[1] += 2
    return out
for r in range(0, 9):
    n = 2 ** r; a = [random.random() for _ in range(n)]; cnt = [0, 0]
    res = fft(a, cnt)
    check(f"FFT n=2^{r}: correct, {cnt[0]} mults = n/2 log n, {cnt[1]} adds = n log n", near(res, dft(a), 1e-7) and cnt[0] == n // 2 * r and cnt[1] == n * r)

# polynomial multiplication
A = [random.randint(-9, 9) for _ in range(13)]; B = [random.randint(-9, 9) for _ in range(9)]
n = 32
prod = np.fft.ifft(np.fft.fft(A + [0] * (n - 13)) * np.fft.fft(B + [0] * (n - 9))).real.round().astype(int).tolist()
check("polynomial product by FFT", prod[:21] == list(np.convolve(A, B)) and not any(prod[21:]))

# NTT primes
cands = [q for q in range(81001, 200000) if q % 2048 == 1 and isprime(q)]
check("smallest prime > 81000 that is 1 mod 2048 is 83969 = 41*2^11+1", cands[0] == 83969 == 41 * 2 ** 11 + 1)
check("998244353 = 119*2^23+1, prime, primitive root 3", 998244353 == 119 * 2 ** 23 + 1 and isprime(998244353) and primitive_root(998244353) == 3)
check("coefficients of a product of two 1000-digit numbers are at most 81000", 1000 * 9 * 9 == 81000)

# NTT example modulo 17
p = 17
check("powers of 3 mod 17", [pow(3, k, p) for k in range(1, 9)] == [3, 9, 10, 13, 5, 15, 11, 16] and pow(9, 8, p) == 1 and pow(9, 4, p) != 1)
check("9*2 = 1 mod 17, 8*15 = 1 mod 17", 9 * 2 % p == 1 and 8 * 15 % p == 1)
pts = [pow(2, j, p) for j in range(8)]
check("evaluation points 1,2,4,8,16,15,13,9", pts == [1, 2, 4, 8, 16, 15, 13, 9])
Av = [(1 + 2 * x + 3 * x * x) % p for x in pts]; Bv = [(4 + 5 * x) % p for x in pts]
check("values of A: 6,0,6,5,2,9,7,7", Av == [6, 0, 6, 5, 2, 9, 7, 7])
check("values of B: 9,14,7,10,16,11,1,15", Bv == [9, 14, 7, 10, 16, 11, 1, 15])
Cv = [x * y % p for x, y in zip(Av, Bv)]
check("products: 3,0,8,16,15,14,7,3", Cv == [3, 0, 8, 16, 15, 14, 7, 3])
c = [15 * sum(Cv[j] * pow(9, j * k, p) for j in range(8)) % p for k in range(8)]
check("inverse transform gives 4,13,5,15,0,0,0,0", c == [4, 13, 5, 15, 0, 0, 0, 0])
check("true product 4+13X+22X^2+15X^3", list(np.convolve([1, 2, 3], [4, 5])) == [4, 13, 22, 15])

# DCT
N = 6; x = [random.random() for _ in range(N)]
Y = dft(x + x[::-1])
X = [sum(x[k] * math.cos(math.pi * j * (2 * k + 1) / (2 * N)) for k in range(N)) for j in range(2 * N)]
check("DCT through the even extension", near(Y, [2 * cmath.exp(1j * math.pi * j / (2 * N)) * X[j] for j in range(2 * N)]))

# Gauss sums
for q in (3, 5, 7, 11, 13, 17, 19, 23):
    chi = [0] + [1 if pow(k, (q - 1) // 2, q) == 1 else -1 for k in range(1, q)]
    w = cmath.exp(2j * cmath.pi / q)
    g = sum(chi[k] * w ** k for k in range(q))
    good = near(dft(chi), [chi[(-j) % q] * g for j in range(q)]) and abs(abs(g) ** 2 - q) < 1e-9 and abs(g - sum(w ** (a * a) for a in range(q))) < 1e-9
    good &= abs(g - (math.sqrt(q) if q % 4 == 1 else 1j * math.sqrt(q))) < 1e-9
    check(f"Gauss sum p={q}: transform of chi, |g|^2 = p, sum of w^(a^2), exact value", good)

# eigenvalues of F_n / sqrt n
def eigs(n):
    F = np.array([[cmath.exp(-2j * cmath.pi * j * k / n) for k in range(n)] for j in range(n)]) / math.sqrt(n)
    ev = np.linalg.eigvals(F)
    return [sum(abs(e - t) < 1e-6 for e in ev) for t in (1, -1, 1j, -1j)]
check(f"n=4 eigenvalues 1,1,-1,-i: multiplicities {eigs(4)}", eigs(4) == [2, 1, 0, 1])
check("all four eigenvalues occur for 5 <= n <= 40", all(min(eigs(n)) >= 1 and max(eigs(n)) - min(eigs(n)) <= 2 for n in range(5, 41)))
n = 7; F = np.array([[cmath.exp(-2j * cmath.pi * j * k / n) for k in range(n)] for j in range(n)])
R = np.array([[1 if (j + k) % n == 0 else 0 for k in range(n)] for j in range(n)])
check("F^2 = nR", np.allclose(F @ F, n * R))

# circulant
c = np.random.rand(6); C = np.array([[c[(k - l) % 6] for l in range(6)] for k in range(6)])
check("det of a circulant = product of the transform", abs(np.linalg.det(C) - np.prod(np.fft.fft(c))) < 1e-9)

# Karatsuba table
kar = [3 ** r for r in range(1, 10)]; ff = [3 * 2 ** r * (r + 1) + 2 ** (r + 1) for r in range(1, 10)]
check("Karatsuba row", kar == [3, 9, 27, 81, 243, 729, 2187, 6561, 19683])
check("FFT row", ff == [16, 44, 112, 272, 640, 1472, 3328, 7424, 16384])
check("crossover between n=256 and n=512", kar[7] < ff[7] and kar[8] > ff[8] and abs(math.log2(3) - 1.585) < 5e-4)

# Bluestein
n = 7; a = [complex(random.random(), random.random()) for _ in range(n)]; z = cmath.exp(1j * cmath.pi / n)
blu = [z ** (-j * j) * sum(a[k] * z ** (-k * k) * z ** ((j - k) ** 2) for k in range(n)) for j in range(n)]
check("Bluestein identity", near(blu, dft(a)))

# midpoint polygon, Napoleon, Petr-Douglas-Neumann
n = 7; zv = np.array([complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(n)]); zv -= zv.mean()
w = cmath.exp(2j * cmath.pi / n); zh = np.fft.fft(zv) / n; cur = zv.copy(); t = 60
for _ in range(t): cur = (cur + np.roll(cur, -1)) / 2
cur = cur - cur.mean()   # rounding leaves a tiny mode 0, whose eigenvalue is 1
lim = [zh[1] * cmath.exp(1j * math.pi * t / n) * w ** k + zh[n - 1] * cmath.exp(-1j * math.pi * t / n) * w ** (-k) for k in range(n)]
check("midpoint polygons: limit shape", near(cur / math.cos(math.pi / n) ** t, lim, 1e-6))
tri = [complex(0, 0), complex(4, 0.5), complex(1, 3)]
w3 = cmath.exp(2j * cmath.pi / 3)
area = lambda pts: 0.5 * sum((pts[k].conjugate() * pts[(k + 1) % len(pts)]).imag for k in range(len(pts)))
out = [(tri[k] - w3 * tri[(k + 1) % 3]) / (1 - w3) for k in range(3)]
inn = [(tri[k] - w3 ** 2 * tri[(k + 1) % 3]) / (1 - w3 ** 2) for k in range(3)]
sides = lambda pts: [abs(pts[k] - pts[(k + 1) % 3]) for k in range(3)]
check("Napoleon: both triangles equilateral, same centroid", max(sides(out)) - min(sides(out)) < 1e-9 and max(sides(inn)) - min(sides(inn)) < 1e-9 and abs(sum(out) - sum(tri)) < 1e-9 and abs(sum(inn) - sum(tri)) < 1e-9)
check("Napoleon: difference of areas = area of ABC", area(tri) > 0 and abs(abs(area(out)) - abs(area(inn)) - area(tri)) < 1e-9)
check("centre for the side from 0 to 1 is 1/2 - i/(2 sqrt 3)", abs(-w3 / (1 - w3) - complex(0.5, -1 / (2 * math.sqrt(3)))) < 1e-12)
for n in (4, 5, 7):
    pts = np.array([complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(n)]); cen = pts.mean()
    order = list(range(1, n - 1)); random.shuffle(order)
    for k in order:
        e = cmath.exp(2j * cmath.pi * k / n)
        pts = (pts - e * np.roll(pts, -1)) / (1 - e)
    d = pts - cen
    check(f"Petr-Douglas-Neumann n={n}", abs(pts.mean() - cen) < 1e-9 and np.allclose(d[1:] / d[:-1], d[1] / d[0]) and abs(abs(d[1] / d[0]) - 1) < 1e-9)

# Chung-Diaconis-Graham
for p_ in (7, 31, 101):
    L = math.ceil(math.log2(p_)) + 1
    law = [Fraction(0)] * p_; law[0] = Fraction(1)
    good = True
    for n_ in range(1, 4 * L + 1):
        new = [Fraction(0)] * p_
        for x_, pr in enumerate(law):
            if pr:
                for e in (-1, 0, 1): new[(2 * x_ + e) % p_] += pr / 3
        law = new
        d = sum(abs(q - Fraction(1, p_)) for q in law) / 2
        good &= float(d) >= 1 - 3 ** n_ / p_ - 1e-12 and float(d) <= 0.5 * math.sqrt(p_) * 3.0 ** (-(n_ // L)) + 1e-12
        tt = 3
        ft = sum(float(q) * cmath.exp(2j * cmath.pi * tt * x_ / p_) for x_, q in enumerate(law))
        good &= abs(ft - math.prod((1 + 2 * math.cos(2 * math.pi * 2 ** j * tt / p_)) / 3 for j in range(n_))) < 1e-9
    for tt in range(1, p_):
        for j0 in range(0, 3 * L):
            good &= any(math.cos(2 * math.pi * 2 ** j * tt / p_) <= 1e-12 for j in range(j0, j0 + L))
    check(f"CDG walk p={p_}: bounds, product formula, window property", good)

# Newman
s2 = lambda m: bin(m).count("1")
good = True
for k in range(1, 11):
    for j in range(3):
        good &= sum(1 for m in range(2 ** k) if s2(m) % 3 == j) == round((2 ** k + 2 * math.cos(math.pi * (k - 2 * j) / 3)) / 3)
for k in range(1, 8):
    good &= sum((-1) ** s2(m) for m in range(0, 4 ** k, 3)) == 2 * 3 ** (k - 1)
    good &= sum((-1) ** s2(m) for m in range(0, 2 * 4 ** k, 3)) == 3 ** k
check("Newman: counts modulo 3 and the two sums", good and abs(math.log(3) / math.log(4) - 0.79) < 5e-3)

# bent functions
m = 3; n = 2 * m
pts = list(itertools.product((0, 1), repeat=n))
f = {x: (-1) ** sum(x[i] * x[m + i] for i in range(m)) for x in pts}
fh = {a: sum(f[x] * (-1) ** sum(u * v for u, v in zip(a, x)) for x in pts) / 2 ** n for a in pts}
check("inner product function is bent", all(abs(abs(v) - 2 ** (-n / 2)) < 1e-12 for v in fh.values()))
dist = min(min(sum(1 for x in pts if f[x] != sg * (-1) ** sum(u * v for u, v in zip(a, x))) for sg in (1, -1)) for a in pts)
check("nonlinearity = 2^(n-1) - 2^(n/2-1)", dist == 2 ** (n - 1) - 2 ** (n // 2 - 1))
check("number of -1 values is 2^(n-1) +- 2^(n/2-1)", sum(1 for x in pts if f[x] == -1) in (2 ** (n - 1) - 2 ** (n // 2 - 1), 2 ** (n - 1) + 2 ** (n // 2 - 1)))

# uncertainty principle
good = True
for n in (6, 8, 9, 12):
    for _ in range(300):
        s = random.randint(1, n)
        S = random.sample(range(n), s); a = [0] * n
        for k in S: a[k] = complex(random.gauss(0, 1), random.gauss(0, 1))
        A = dft(a); nz = [abs(v) > 1e-9 for v in A]
        good &= s * sum(nz) >= n
        good &= all(any(nz[(j0 + i) % n] for i in range(s)) for j0 in range(n))
    for d in (d for d in range(1, n + 1) if n % d == 0):
        a = [1 if k % d == 0 else 0 for k in range(n)]; A = dft(a)
        good &= near(A, [n // d if j % (n // d) == 0 else 0 for j in range(n)])
check("uncertainty principle: no run of s zeros, product >= n, equality for combs", good)

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
