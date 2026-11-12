#!/usr/bin/env python3
"""Numeric checks for Volume 5, Chapter 2 (Generating Functions).

Every number printed in the chapter is recomputed here from its definition.
Run: python3 review/volume5-rewrite/check_ch02_generating.py
"""
from fractions import Fraction as Fr
from itertools import permutations, product, combinations
from math import comb, factorial, gcd, pi, sqrt, cosh, exp, log, gamma
from functools import lru_cache

ok = True


def check(name, cond):
    global ok
    print(("ok   " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


# --- opening: Naude's question -------------------------------------------
def distinct_parts(n, k, m=1):
    if k == 0:
        return 1 if n == 0 else 0
    return sum(distinct_parts(n - j, k - 1, j + 1) for j in range(m, n + 1))


check("50 as a sum of 7 distinct parts: 522", distinct_parts(50, 7) == 522)

# --- Fibonacci, merge sort, quicksort ------------------------------------
F = [0, 1]
for _ in range(40):
    F.append(F[-1] + F[-2])
phi = (1 + sqrt(5)) / 2
check("Binet nearest integer", all(F[n] == round(phi**n / sqrt(5)) for n in range(40)))
check("Cassini", all(F[n - 1] * F[n + 1] - F[n] ** 2 == (-1) ** n for n in range(1, 40)))
t = [Fr(3)]
for m in range(1, 12):
    t.append(2 * t[-1] + 2**m)
check("merge sort t_m = t_0 2^m + m 2^m", all(t[m] == 3 * 2**m + m * 2**m for m in range(12)))
C = [Fr(0)]
for n in range(1, 60):
    C.append(n - 1 + Fr(2, n) * sum(C))
H = lambda n: sum(Fr(1, k) for k in range(1, n + 1))
check("quicksort C_n = 2(n+1)H_n - 4n", all(C[n] == 2 * (n + 1) * H(n) - 4 * n for n in range(1, 60)))
g_euler = 0.5772156649015329
check("0 <= H_n - ln n - gamma <= ln(1+1/n)",
      all(0 <= float(H(n)) - log(n) - g_euler <= log(1 + 1 / n) for n in range(1, 200)))

# --- exponential formula examples -----------------------------------------
N = 12
bell = [1]
for n in range(N):
    bell.append(sum(comb(n, k) * bell[k] for k in range(n + 1)))
check("Bell numbers 1,1,2,5,15,52,203,877", bell[:8] == [1, 1, 2, 5, 15, 52, 203, 877])
check("Dobinski", all(abs(sum(k**n / factorial(k) for k in range(80)) / exp(1) - bell[n]) < 1e-6 * bell[n]
                      for n in range(1, 10)))
D = [sum(Fr((-1) ** k, factorial(k)) for k in range(n + 1)) * factorial(n) for n in range(N)]
check("derangements nearest n!/e", all(D[n] == round(factorial(n) / exp(1)) for n in range(1, N)))
inv = [1, 1]
for n in range(1, 8):
    inv.append(inv[n] + n * inv[n - 1])
check("involutions 1,1,2,4,10,26,76,232", inv[:8] == [1, 1, 2, 4, 10, 26, 76, 232])
check("involutions brute force n=5", sum(1 for p in permutations(range(5)) if all(p[p[i]] == i for i in range(5))) == 26)


def series_log(f, n):  # f[0] = 1, ordinary coefficients (Fractions)
    L = [Fr(0)] * (n + 1)
    for k in range(1, n + 1):
        L[k] = f[k] - sum(Fr(j, k) * L[j] * f[k - j] for j in range(1, k))
    return L


g = [Fr(2 ** comb(n, 2), factorial(n)) for n in range(8)]
Lg = series_log(g, 7)
check("log of graph series: 1, 1/2, 2/3, 19/12, 91/15",
      Lg[1:6] == [Fr(1), Fr(1, 2), Fr(2, 3), Fr(19, 12), Fr(91, 15)])
check("connected graphs 1,1,4,38,728", [int(Lg[n] * factorial(n)) for n in range(1, 6)] == [1, 1, 4, 38, 728])
Mz = [1, 1]
for n in range(2, 9):
    Mz.append(Mz[n - 1] + sum(Mz[k] * Mz[n - 2 - k] for k in range(n - 1)))
check("Motzkin 1,1,2,4,9,21,51,127,323", Mz == [1, 1, 2, 4, 9, 21, 51, 127, 323])

# --- partitions -------------------------------------------------------------
P = 260
p = [1] + [0] * P
for k in range(1, P + 1):
    for n in range(k, P + 1):
        p[n] += p[n - k]
check("p(4) = 5", p[4] == 5)
check("p(200) = 3972999029388", p[200] == 3972999029388)
pent = {}
j = 1
while j * (3 * j - 1) // 2 <= P:
    pent[j * (3 * j - 1) // 2] = (-1) ** j
    pent[j * (3 * j + 1) // 2] = (-1) ** j
    j += 1
E = [0] * (P + 1)
E[0] = 1
for k in range(1, P + 1):
    for n in range(P, k - 1, -1):
        E[n] -= E[n - k]
check("pentagonal number theorem to x^260", all(E[n] == pent.get(n, 0) for n in range(1, P + 1)))
check("first pentagonal exponents 1,2,5,7,12,15,22,26", sorted(pent)[:8] == [1, 2, 5, 7, 12, 15, 22, 26])
check("Euler's recurrence", all(p[n] == -sum(s * p[n - g_] for g_, s in pent.items() if g_ <= n) for n in range(1, P + 1)))
sig = [0] + [sum(d for d in range(1, n + 1) if n % d == 0) for n in range(1, P + 1)]
check("sigma recurrence with sigma(0) = n",
      all(sig[n] == -sum(s * (sig[n - g_] if g_ < n else n) for g_, s in pent.items() if g_ <= n) for n in range(1, P + 1)))
check("sigma(5) = 7 + 4 - 5 = 6", sig[5] == 6 and sig[4] == 7 and sig[3] == 4)
check("n p(n) = sum sigma(k) p(n-k); n=4 gives 20",
      all(n * p[n] == sum(sig[k] * p[n - k] for k in range(1, n + 1)) for n in range(1, 100)) and 4 * p[4] == 20)
dist = [0] * 61
odd = [0] * 61
dist[0] = odd[0] = 1
for k in range(1, 61):
    for n in range(60, k - 1, -1):
        dist[n] += dist[n - k]
    if k % 2:
        for n in range(k, 61):
            odd[n] += odd[n - k]
check("distinct parts = odd parts", dist == odd)
check("conjugate of 6+4+4+2+1 is 5+4+3+3+1+1",
      [sum(1 for x in [6, 4, 4, 2, 1] if x > i) for i in range(6)] == [5, 4, 3, 3, 1, 1])

# --- exercises --------------------------------------------------------------
ways = [1] + [0] * 100
for c in [1, 2, 5, 10, 20, 50, 100]:
    for n in range(c, 101):
        ways[n] += ways[n - c]
check("ways to pay 1 euro: 4563", ways[100] == 4563)

s2 = lambda n: bin(n).count("1")
A = [n for n in range(16) if s2(n) % 2 == 0]
B = [n for n in range(16) if s2(n) % 2 == 1]
check("Prouhet sets", A == [0, 3, 5, 6, 9, 10, 12, 15] and B == [1, 2, 4, 7, 8, 11, 13, 14])
check("Prouhet sums 8, 60, 620, 7200",
      [sum(a**k for a in A) for k in range(4)] == [8, 60, 620, 7200] == [sum(b**k for b in B) for k in range(4)])
check("Prouhet k=N value", all(sum((-1) ** s2(n) * n**Nn for n in range(2**Nn)) == (-1) ** Nn * factorial(Nn) * 2 ** (Nn * (Nn - 1) // 2)
                               for Nn in range(1, 8)))


def polymul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j_, y in enumerate(b):
            r[i + j_] += x * y
    return r


def polydiv(a, b):
    a = a[:]
    q = [0] * (len(a) - len(b) + 1)
    for i in range(len(q) - 1, -1, -1):
        q[i] = a[i + len(b) - 1] // b[-1]
        for j_, y in enumerate(b):
            a[i + j_] -= q[i] * y
    assert not any(a)
    return q


@lru_cache(None)
def cyclo(n):
    f = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            f = polydiv(f, list(cyclo(d)))
    return tuple(f)


check("Phi_105 coefficient of x^7 is -2", cyclo(105)[7] == -2)
okpq = True
for (pp, qq) in [(3, 5), (3, 7), (5, 7), (5, 11), (7, 13), (11, 13)]:
    co = [c for c in cyclo(pp * qq) if c]
    okpq &= set(co) <= {1, -1} and all(co[i] == -co[i + 1] for i in range(len(co) - 1))
check("Phi_pq coefficients in {-1,0,1} and alternating", okpq)
check("Schur: coefficient of x^7 in Phi_{3*5*7} is 1 - t with t = 3", cyclo(105)[7] == 1 - 3)


def commuting_tuples(n, k):
    perms = list(permutations(range(n)))
    comp = lambda a, b: tuple(a[b[i]] for i in range(n))
    com = {(a, b) for a in perms for b in perms if comp(a, b) == comp(b, a)}
    if k == 2:
        return len(com)
    return sum(1 for (a, b) in com for c in perms if (a, c) in com and (b, c) in com)


def prod_series(expo, n):  # prod_j (1-x^j)^(-expo(j)) up to x^n
    r = [1] + [0] * n
    for j_ in range(1, n + 1):
        for _ in range(expo(j_)):
            for m in range(j_, n + 1):
                r[m] += r[m - j_]
    return r


h3 = prod_series(lambda j_: sig[j_], 4)
check("commuting pairs h_2(n) = n! p(n), n <= 4", all(commuting_tuples(n, 2) == factorial(n) * p[n] for n in range(1, 5)))
check("commuting triples h_3(n) from the product, n <= 4",
      all(commuting_tuples(n, 3) == factorial(n) * h3[n] for n in range(1, 5)))


def roots_of_unity_count(n, k):
    idn = tuple(range(n))
    cnt = 0
    for q in permutations(range(n)):
        r = idn
        for _ in range(k):
            r = tuple(q[i] for i in r)
        cnt += r == idn
    return cnt


okr = True
for pr in (2, 3, 5):
    a = [1] * pr
    for n in range(pr, 30):
        a.append(a[n - 1] + factorial(n - 1) // factorial(n - pr) * a[n - pr])
    okr &= all(a[n] % (pr * (pr - 1)) == pr % (pr * (pr - 1)) for n in range(pr, 30))
    okr &= all(a[n] == roots_of_unity_count(n, pr) for n in range(1, 7))
check("a_n(p): recurrence, brute force, a_n = p mod p(p-1)", okr)


def cycle_type(q):
    n = len(q)
    seen = [False] * n
    ct = []
    for i in range(n):
        if not seen[i]:
            l, j_ = 0, i
            while not seen[j_]:
                seen[j_] = True
                j_ = q[j_]
                l += 1
            ct.append(l)
    return ct


def is_square_type(ct):
    return all(ct.count(l) % 2 == 0 for l in set(ct) if l % 2 == 0)


NS = 801
# exponential generating function of squares, as floats: sqrt((1+x)/(1-x)) prod cosh(x^{2m}/2m)
sq = [0.0] * NS
sq[0] = 1.0
for l in range(1, NS):
    new = [0.0] * NS
    term = 1.0
    m = 0
    while m * l < NS:
        if l % 2 == 1 or m % 2 == 0:
            for i in range(NS - m * l):
                new[i + m * l] += sq[i] * term
        m += 1
        term /= (l * m)
    sq = new
brute = {n: sum(1 for q in permutations(range(n)) if is_square_type(cycle_type(q))) for n in range(1, 8)}
sqsets = {n: len({tuple(q[q[i]] for i in range(n)) for q in permutations(range(n))}) for n in range(1, 8)}
check("squares: cycle-type criterion equals actual squares, n <= 7", brute == sqsets)
check("squares: generating function matches brute force", all(abs(sq[n] * factorial(n) - brute[n]) < 1e-6 for n in range(1, 8)))
check("s_{2m+1} = (2m+1) s_{2m}", all(abs(sq[2 * m + 1] - sq[2 * m]) < 1e-12 for m in range(0, 300)))
blum = 1.0
for m in range(1, 200000):
    blum *= cosh(1 / (2 * m))
check("Blum constant 1.2218", abs(blum - 1.2218) < 5e-5)
ratio = sq[800] / (blum * sqrt(2 / (pi * 800)))
check("ratio at n = 800 is 1.002", abs(ratio - 1.002) < 6e-4)
print("     (Blum constant %.5f, ratio at 800: %.4f)" % (blum, ratio))

# random polynomials over F_q
def squarefree_count(q, n):
    # count monic squarefree of degree n over F_q (q prime) by brute force via gcd(f, f')
    def trim(a):
        while a and a[-1] == 0:
            a.pop()
        return a

    def pmod(a, b):
        a = a[:]
        while len(a) >= len(b):
            c = a[-1] * pow(b[-1], -1, q) % q
            for i in range(len(b)):
                a[len(a) - len(b) + i] = (a[len(a) - len(b) + i] - c * b[i]) % q
            trim(a)
            if not a:
                break
        return a

    def pgcd(a, b):
        while b:
            a, b = b, pmod(a, b)
        return a

    cnt = 0
    for coeffs in product(range(q), repeat=n):
        f = list(coeffs) + [1]
        df = trim([(i * f[i]) % q for i in range(1, len(f))])
        if df and len(pgcd(f, df)) == 1:
            cnt += 1
    return cnt


check("squarefree monic polynomials: q^n - q^(n-1)",
      all(squarefree_count(q, n) == q**n - q ** (n - 1) for q, n in [(2, 2), (2, 5), (3, 3), (3, 4), (5, 3)]))
mu = lambda n: 0 if any(n % (d * d) == 0 for d in range(2, n + 1)) else (-1) ** sum(1 for d in range(2, n + 1) if n % d == 0 and all(d % e for e in range(2, d)))
Mq = lambda n, q: sum(mu(d) * q ** (n // d) for d in range(1, n + 1) if n % d == 0) // n
check("|n M(n,q) - q^n| <= 2 q^(n/2)", all(abs(n * Mq(n, q) - q**n) <= 2 * q ** (n / 2) for q in (2, 3, 4, 5, 7) for n in range(1, 25)))
check("Gauss: sum d M(d,q) = q^k", all(sum(d * Mq(d, q) for d in range(1, k + 1) if k % d == 0) == q**k for q in (2, 3, 5) for k in range(1, 20)))
check("mu sum divisible by n for negative a",
      all(sum(mu(d) * a ** (n // d) for d in range(1, n + 1) if n % d == 0) % n == 0 for a in range(-6, 7) for n in range(1, 25)))
check("Metropolis-Rota", all(Mq(n, a * b) == sum(gcd(i, j_) * Mq(i, a) * Mq(j_, b) for i in range(1, n + 1) for j_ in range(1, n + 1)
                                                 if i * j_ // gcd(i, j_) == n) for a in (2, 3) for b in (2, 5) for n in range(1, 13)))

# parts 1,2,3
a3 = [1] + [0] * 200
for k in (1, 2, 3):
    for n in range(k, 201):
        a3[n] += a3[n - k]
check("a(n) - a(n-6) = n", all(a3[n] - a3[n - 6] == n for n in range(6, 201)))
check("a(n) nearest (n+3)^2/12", all(a3[n] == round((n + 3) ** 2 / 12) for n in range(201)))
check("a(0..5) = 1,1,2,3,4,5", a3[:6] == [1, 1, 2, 3, 4, 5])
tri = lambda n: sum(1 for x in range(1, n) for y in range(x, n) for z in [n - x - y] if z >= y and x + y > z)
check("integer triangles", all(tri(2 * m + 3) == a3[m] for m in range(40)) and all(tri(2 * m) == a3[m - 3] for m in range(3, 40)))

# self-conjugate partitions
def partitions_of(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions_of(n - k, k):
            yield (k,) + r


conj = lambda lam: tuple(sum(1 for x in lam if x > i) for i in range(lam[0])) if lam else ()
sc = [sum(1 for lam in partitions_of(n) if conj(lam) == lam) for n in range(26)]
do = [0] * 26
do[0] = 1
for k in range(1, 26, 2):
    for n in range(25, k - 1, -1):
        do[n] += do[n - k]
check("self-conjugate = distinct odd parts, parity of p(n)", sc == do and all((p[n] - sc[n]) % 2 == 0 for n in range(26)))
rhs = [0] * 26
for k in range(0, 6):
    if k * k > 25:
        break
    part = [1] + [0] * 25
    for j_ in range(1, k + 1):
        for n in range(2 * j_, 26):
            part[n] += part[n - 2 * j_]
    for n in range(k * k, 26):
        rhs[n] += part[n - k * k]
check("Durfee square identity", rhs == do)

# Glaisher example
lam = [7, 2, 2, 2, 2, 1, 1, 1]
img = []
for part in set(lam):
    m, i = lam.count(part), 0
    while m:
        img += [part * 3**i] * (m % 3)
        m //= 3
        i += 1
check("Glaisher image of 7+2+2+2+2+1+1+1 is 7+6+3+2 (sum 18)", sorted(img, reverse=True) == [7, 6, 3, 2] and sum(lam) == 18)

# Catalan parity
cat = lambda n: comb(2 * n, n) // (n + 1)
v2 = lambda n: (n & -n).bit_length() - 1
check("v_2(C_n) = s(n+1) - 1", all(v2(cat(n)) == s2(n + 1) - 1 for n in range(1, 300)))

# Stern
st = [0, 1]
for n in range(2, 1 << 11):
    st.append(st[n // 2] if n % 2 == 0 else st[n // 2] + st[n // 2 + 1])


@lru_cache(None)
def hyper(n):
    if n == 0:
        return 1
    return hyper((n - 1) // 2) if n % 2 else hyper(n // 2) + hyper(n // 2 - 1)


def hyper_brute(n):
    cnt, bits = 0, max(1, n.bit_length())
    for e in product(range(3), repeat=bits):
        cnt += sum(d << i for i, d in enumerate(e)) == n
    return cnt


check("hyperbinary count = s(n+1)", all(hyper_brute(n) == st[n + 1] for n in range(0, 60)))
check("Stern row sums 3^k", all(sum(st[2**k:2 ** (k + 1)]) == 3**k for k in range(10)))
check("Stern consecutive coprime", all(gcd(st[n], st[n + 1]) == 1 for n in range(2000)))
check("Calkin-Wilf start 1/1,1/2,2/1,1/3,3/2,2/3,3/1",
      [(st[n], st[n + 1]) for n in range(1, 8)] == [(1, 1), (1, 2), (2, 1), (1, 3), (3, 2), (2, 3), (3, 1)])

# binary partitions
bp = [1] + [0] * 3000
k = 1
while k <= 3000:
    for n in range(k, 3001):
        bp[n] += bp[n - k]
    k *= 2
check("b(0),b(1),b(2) = 1,1,2", bp[:3] == [1, 1, 2])
check("b(n) even for n >= 2, never divisible by 8 below 3000", all(bp[n] % 2 == 0 and bp[n] % 8 for n in range(2, 3001)))
check("b(2n) = b(0)+...+b(n)", all(bp[2 * n] == sum(bp[:n + 1]) for n in range(1, 1500)))

# arcsin squared
def series(x, T=600):
    tot_, term_ = 0.0, 0.5 * (2 * x) ** 2 / 2  # n = 1 term of (1/2) sum (2x)^(2n)/(n^2 C(2n,n))
    for n in range(1, T):
        tot_ += term_
        term_ *= x * x * (2 * n) ** 2 / ((2 * n + 1) * (2 * n + 2))
    return tot_


from math import asin
check("arcsin^2 series at 1/2 and 0.9", abs(series(0.5) - asin(0.5) ** 2) < 1e-12 and abs(series(0.9) - asin(0.9) ** 2) < 1e-12)
check("sum 1/(n^2 C(2n,n)) = pi^2/18", abs(sum(1 / (n * n * comb(2 * n, n)) for n in range(1, 60)) - pi**2 / 18) < 1e-14)
term, tot = 1.0, 0.0
okb = True
for n in range(1, 2000000):
    tot += term
    if n < 2000:
        okb &= term <= n ** -1.5 + 1e-15 and comb(2 * n, n) ** 2 * 4 * n >= 16**n
    term *= (2 * n) ** 2 / ((2 * n + 1) * (2 * n + 2))
check("C(2n,n) >= 4^n/(2 sqrt n) and c_2n <= n^(-3/2)", okb)
check("sum 4^n/(n^2 C(2n,n)) -> pi^2/2 (partial sums)", abs(2 * tot - pi**2 / 2) < 3e-3)

# law of {1/U}
check("g(0) = zeta(2), odd floor has probability log 2",
      abs(sum(1 / k**2 for k in range(1, 10**6)) - pi**2 / 6) < 2e-6 and
      abs(sum(1 / k - 1 / (k + 1) for k in range(1, 10**6, 2)) - log(2)) < 2e-6)
check("P({1/U} < 1/2) = 2 - 2 log 2", abs(sum(1 / k - 1 / (k + 0.5) for k in range(1, 10**6)) - (2 - 2 * log(2))) < 2e-6)
X = 10**6
check("proportion of n <= x with floor(x/n) odd near log 2", abs(sum((X // n) % 2 for n in range(1, X + 1)) / X - log(2)) < 2e-3)

# zigzag
Az = [1, 1]
for n in range(1, 12):
    Az.append(sum(comb(n, k) * Az[k] * Az[n - k] for k in range(n + 1)) // 2)
check("alternating permutations 1,1,1,2,5,16,61,272,1385 and A_10 = 50521", Az[:9] == [1, 1, 1, 2, 5, 16, 61, 272, 1385] and Az[10] == 50521)
check("A_5 brute force", sum(1 for q in permutations(range(5)) if all((q[i] < q[i + 1]) == (i % 2 == 0) for i in range(4))) == 16)
r10 = Az[10] / factorial(10)
check("A_10/10! = 0.0139222, 2(2/pi)^11 = 0.0139223, relative error -5.6e-6",
      abs(r10 - 0.0139222) < 5e-8 and abs(2 * (2 / pi) ** 11 - 0.0139223) < 5e-8 and abs(r10 / (2 * (2 / pi) ** 11) - 1 + 5.6e-6) < 1e-7)

# birthdays
def expected_wait(n, m):
    # E[T] = sum_k k! [x^k] e_m(x)^n / n^k, exact
    e = [Fr(1, factorial(j)) for j in range(m)]
    poly = [Fr(1)]
    base, k = e, n
    while k:
        if k & 1:
            poly = [sum(poly[i] * base[t - i] for i in range(max(0, t - len(base) + 1), min(t, len(poly) - 1) + 1)) for t in range(len(poly) + len(base) - 1)]
        k >>= 1
        if k:
            base = [sum(base[i] * base[t - i] for i in range(max(0, t - len(base) + 1), min(t, len(base) - 1) + 1)) for t in range(2 * len(base) - 1)]
    return poly


def expected_wait_float(n, m):
    # dynamic programme on floats: P(T > k) via distribution of (number of values seen j times)
    from collections import defaultdict
    state = {tuple([n] + [0] * (m - 1)): 1.0}
    tot, k = 0.0, 0
    while state:
        tot += sum(state.values())
        new = defaultdict(float)
        for stt, pr in state.items():
            for j in range(m - 1):
                if stt[j]:
                    s_ = list(stt)
                    s_[j] -= 1
                    s_[j + 1] += 1
                    new[tuple(s_)] += pr * stt[j] / n
        state = {s_: v for s_, v in new.items() if v > 1e-18}
        k += 1
    return tot


e2, e3 = expected_wait_float(365, 2), expected_wait_float(365, 3)
check("birthday waits 24.62 (pair) and 88.74 (triple)", abs(e2 - 24.62) < 5e-3 and abs(e3 - 88.74) < 5e-3)
Q = sum(factorial(365) // factorial(365 - k) / 365**k for k in range(1, 366))
check("E[T] = 1 + Q(n) for pairs", abs(e2 - 1 - Q) < 1e-9)
check("Gamma(4/3)(6 n^2)^(1/3) = 82.9 and sqrt(pi n/2) = 23.9 at n = 365",
      abs(gamma(4 / 3) * (6 * 365**2) ** (1 / 3) - 82.9) < 0.05 and abs(sqrt(pi * 365 / 2) - 23.9) < 0.05)
small = expected_wait(6, 3)
check("exact formula against the float programme (n=6, m=3)",
      abs(float(sum(factorial(k) * small[k] / Fr(6) ** k for k in range(len(small)))) - expected_wait_float(6, 3)) < 1e-9)

# die
import numpy as np
u = [1.0]
for n in range(1, 200):
    u.append(sum(u[n - j] for j in range(1, 7) if n - j >= 0) / 6)
check("u_n -> 2/7", abs(u[199] - 2 / 7) < 1e-12)
rts = np.roots([-1 / 6] * 6 + [1.0])
others = sorted(abs(z) for z in rts if abs(z - 1) > 1e-9)
check("other roots of 1 - D: smallest modulus 1.3694, rate 0.7302", abs(others[0] - 1.3694) < 5e-5 and abs(1 / others[0] - 0.7302) < 5e-5)

# Flory
V = [Fr(0), Fr(1)]
for n in range(2, 40):
    V.append(Fr(2, n - 1) * sum(V[:n - 1]))
check("V_n closed form", all(V[n] == sum(Fr((n - k) * (-2) ** k, factorial(k)) for k in range(n)) for n in range(40)))
check("|V_n - (n+2)e^-2| <= 2^(n+1)/(n+1)!", all(abs(float(V[n]) - (n + 2) * exp(-2)) <= 2 ** (n + 1) / factorial(n + 1) + 1e-13 for n in range(40)))
check("e^-2 = 13.5%", abs(exp(-2) - 0.135) < 5e-4)

# fixed points and Bell numbers (moved here from Chapter 1)
def stirling2(k, j):
    return sum((-1) ** (j - i) * comb(j, i) * i**k for i in range(j + 1)) // factorial(j)


okf = True
for n in range(1, 7):
    perms = list(permutations(range(n)))
    for k in range(1, 9):
        mom = Fr(sum(sum(1 for i in range(n) if q[i] == i) ** k for q in perms), len(perms))
        okf &= mom == sum(stirling2(k, j) for j in range(0, n + 1))
        if k <= n:
            okf &= mom == bell[k]
        if k == n + 1:
            okf &= mom == bell[k] - 1
check("moments of the number of fixed points", okf)

print("\nALL CHECKS PASSED" if ok else "\nSOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
