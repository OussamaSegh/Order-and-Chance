#!/usr/bin/env python3
"""Recompute the printed numbers of Chapter 8 (ch08-ranks.tex) and test the alternating-matrix theorems by brute force."""
import math, itertools
from fractions import Fraction as F
from collections import Counter
from common import check, check_true, finish

def rank_mod(M, p):
    M = [r[:] for r in M]; n = len(M); r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if M[i][c] % p), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], -1, p); M[r] = [x * inv % p for x in M[r]]
        for i in range(n):
            if i != r and M[i][c] % p:
                f = M[i][c]; M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return r

def kernel_law(n, p):
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    cnt = Counter()
    for vals in itertools.product(range(p), repeat=len(idx)):
        M = [[0] * n for _ in range(n)]
        for (i, j), v in zip(idx, vals): M[i][j] = v; M[j][i] = (-v) % p
        cnt[n - rank_mod(M, p)] += 1
    tot = p ** len(idx)
    return {k: F(c, tot) for k, c in cnt.items()}

def f_exact(n, k, p):
    if k < 0 or k > n or (n - k) % 2: return F(0)
    num = math.prod(1 - F(1, p ** j) for j in range(k + 1, n + 1))
    den = math.prod(1 - F(1, p ** (2 * i)) for i in range(1, (n - k) // 2 + 1))
    return F(1, p ** (k * (k - 1) // 2)) * num / den

for n, p in [(2, 2), (3, 2), (4, 2), (5, 2), (2, 3), (3, 3), (4, 3), (2, 5), (3, 5)]:
    law = kernel_law(n, p)
    check_true(f"Theorem altlaw exact, n={n}, p={p}", all(law.get(k, 0) == f_exact(n, k, p) for k in range(n + 1)))
    check(f"E p^K_n = p+1-p^(1-n), n={n}, p={p}", float(sum(q * p ** k for k, q in law.items())), p + 1 - p ** (1 - n), 1e-12)
check_true("ex:alt3: P(K_3=3)=1/8, P(K_3=1)=7/8", kernel_law(3, 2) == {3: F(1, 8), 1: F(7, 8)})

# chain recursion holds for the formula (many n, p)
ok = True
for p in [2, 3, 5]:
    for n in range(0, 12):
        for k in range(0, n + 2):
            lhs = f_exact(n + 1, k, p)
            rhs = (f_exact(n, k - 1, p) * F(1, p ** (k - 1)) if k >= 1 else 0) + f_exact(n, k + 1, p) * (1 - F(1, p ** (k + 1)))
            ok &= lhs == rhs
check_true("formula satisfies the chain recursion", ok)

N = 400
def pi(p, k):
    return p ** -(k * (k - 1) / 2) / (math.prod(1 + p ** -j for j in range(N)) * math.prod(1 - p ** -j for j in range(1, k + 1)))
P2 = math.prod(1 + 2 ** -j for j in range(N))
check("prod (1+2^-j) = 4.7685 (hint: 4.7684...)", P2, 4.7685, 5e-5)
for k, pr in zip(range(4), [0.2097, 0.4194, 0.2796, 0.0799]):
    check(f"pi_2({k})", pi(2, k), pr, 5e-5)
for k, pr in zip(range(4), [0.210, 0.419, 0.280, 0.080]):
    check(f"pi_2({k}) rounded", pi(2, k), pr, 5e-4)
check("P(dim >= 4)", 1 - sum(pi(2, k) for k in range(4)), 0.0114, 5e-5)
for p in [2, 3, 5, 7]:
    check(f"sum pi_{p} = 1", sum(pi(p, k) for k in range(60)), 1, 1e-12)
    check(f"even mass pi_{p} = 1/2", sum(pi(p, k) for k in range(0, 60, 2)), 0.5, 1e-12)
    for m in range(1, 5):
        check(f"E p^(mK) = prod(1+p^i), p={p}, m={m}", sum(pi(p, k) * p ** (m * k) for k in range(80)), math.prod(1 + p ** i for i in range(1, m + 1)), 1e-9 * p ** (m * (m + 1) // 2))
    # limit of finite-n law
    check(f"P(K_n=k) -> 2 pi, p={p}, k=1", float(f_exact(61, 1, p)), 2 * pi(p, 1), 1e-12)
# conditional moments along each parity equal (rem:parity)
for p in [2, 3]:
    for m in range(1, 4):
        ev = sum(2 * pi(p, k) * p ** (m * k) for k in range(0, 80, 2))
        od = sum(2 * pi(p, k) * p ** (m * k) for k in range(1, 80, 2))
        check(f"even/odd moments agree, p={p}, m={m}", ev, od, 1e-9 * ev)
# ex:altsubspaces: injections average p^{k(k+1)/2}
for p in [2, 3]:
    for k in range(1, 4):
        val = sum(pi(p, K) * math.prod(p ** K - p ** i for i in range(k)) for K in range(80))
        check(f"E #Inj(F_p^{k}, K) = p^(k(k+1)/2), p={p}", val, p ** (k * (k + 1) // 2), 1e-9 * val)
# ex:altsubspaces finite n by brute force
n, p = 4, 2
idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
for k in range(1, 4):
    c = 0
    for vals in itertools.product(range(p), repeat=len(idx)):
        M = [[0] * n for _ in range(n)]
        for (i, j), v in zip(idx, vals): M[i][j] = v; M[j][i] = v
        c += all(M[i][j] == 0 for i in range(n) for j in range(k))
    check(f"P(W in ker A_4), dim W={k}", c / p ** len(idx), p ** (-n * k + k * (k + 1) // 2), 1e-15)

# prop:avgrank
for p, pr in [(2, F(3, 2)), (3, F(7, 6)), (5, F(21, 20))]:
    check(f"avg rank bound p={p}", 1 + F(1, p * (p - 1)), pr, 0)
    check_true(f"line below p^r on integers, p={p}", all(p ** r >= (p * p - p) * r - (p * p - 2 * p) for r in range(0, 40)))
# ex:rankfive
check_true("5^r >= 1+12r, even r", all(5 ** r >= 1 + 12 * r for r in range(0, 40, 2)))
check_true("5^r >= 5+20(r-1), odd r", all(5 ** r >= 5 + 20 * (r - 1) for r in range(1, 40, 2)))
bnd = max(0.5 * ((Se - 1) / 12 + 1 + (12 - Se - 5) / 20) for Se in [1 + i * 0.01 for i in range(601)])
check("ex:rankfive bound", bnd, 0.75, 1e-12)
check("ex:rankfive other extreme", 0.5 * (0 + 1 + 6 / 20), 0.65, 1e-12)

# congruent number n=5: images of torsion and of (-4,6) in (Q*/Q*^2)^2 with primes 2, 5
def sqclass(x):
    x = F(x); s = -1 if x < 0 else 1; out = s
    for q in [2, 5, 3, 7]:
        v = 0; a, b = abs(x.numerator), x.denominator
        while a % q == 0: a //= q; v += 1
        while b % q == 0: b //= q; v -= 1
        if v % 2: out *= q
    return out
check_true("(-4,6) on y^2=x^3-25x", 6 ** 2 == (-4) ** 3 - 25 * (-4))
check_true("(-4,6) -> (-1,-1)", (sqclass(-4), sqclass(-4 - 5)) == (-1, -1))
# torsion images: (0,0): x=0 -> class of (x-5)(x+5)=-25 -> -1 ; x-5 = -5. (5,0): x=5, x-5 class = x(x+5)=50 -> 2 ; (-5,0): x=-5, x-5=-10 -> -10
check_true("torsion images (1,1),(-1,-5),(5,2),(-5,-10)", [(-1, -5), (5, sqclass(5 * 10)), (-5, -10)] == [(sqclass(-25), sqclass(-5)), (5, 2), (sqclass(-5), sqclass(-10))])
G = {(1, 1), (-1, -5), (5, 2), (-5, -10)}
check_true("(-1,-1) not in the torsion image", (-1, -1) not in G)
finish()
