"""Volume 10, Chapter 10 (The symmetric group): hook length formula against brute-force tableaux counts, Robinson--Schensted
(bijection, sum of squares, Schensted's theorem), the transposition character, Catalan and two-row counts, Frobenius' formula,
the small tables for n=4,5, and the Logan--Shepp--Vershik--Kerov curve."""
import itertools, math, bisect
from common import check, check_true, finish

def partitions(n, m=None):
    m = n if m is None else m
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n - k, k): yield (k,) + p
def conj(l): return tuple(sum(1 for r in l if r > j) for j in range(l[0])) if l else ()
def hooks(l):
    lc = conj(l); return [l[i] - j - 1 + lc[j] - i for i in range(len(l)) for j in range(l[i])]
def f_hook(l): return math.factorial(sum(l)) // math.prod(hooks(l))
def f_count(l):   # number of standard tableaux = paths in Young's lattice
    l = list(l)
    if sum(l) == 0: return 1
    tot = 0
    for i in range(len(l)):
        if l[i] > (l[i + 1] if i + 1 < len(l) else 0):
            m = l[:]; m[i] -= 1
            tot += f_count(tuple(x for x in m if x))
    return tot
check_true("hook length formula = number of standard tableaux, all lambda |-n, n<=9", all(f_hook(l) == f_count(l) for n in range(1, 10) for l in partitions(n)))

def rsk(w):
    P, Q = [], []
    for k, x in enumerate(w, 1):
        r = 0
        while True:
            if r == len(P): P.append([x]); Q.append([k]); break
            i = bisect.bisect(P[r], x)
            if i == len(P[r]): P[r].append(x); Q[r].append(k); break
            P[r][i], x = x, P[r][i]; r += 1
    return tuple(map(tuple, P)), tuple(map(tuple, Q))
def lis(w):
    t = []
    for x in w:
        i = bisect.bisect(t, x)
        if i == len(t): t.append(x)
        else: t[i] = x
    return len(t)
for n in range(1, 8):
    perms = list(itertools.permutations(range(1, n + 1)))
    images = [rsk(w) for w in perms]
    check_true(f"n={n}: RS is injective, shapes agree, sum (f^lambda)^2 = n!", len(set(images)) == len(perms) and all(tuple(map(len, P)) == tuple(map(len, Q)) for P, Q in images) and sum(f_hook(l) ** 2 for l in partitions(n)) == math.factorial(n))
    check_true(f"n={n}: Schensted, longest increasing subsequence = first row", all(lis(w) == len(rsk(w)[0][0]) for w in perms))

# transposition character: content sum formula, checked against the character table of S4 (Volume 3), and n=5 with Murnaghan-Nakayama by brute force
def ratio(l):
    from fractions import Fraction
    return Fraction(sum(j - i for i in range(len(l)) for j in range(l[i])), math.comb(sum(l), 2))
def chi_tau(l): return ratio(l) * f_hook(l)
s4 = {(4,): 1, (3, 1): 1, (2, 2): 0, (2, 1, 1): -1, (1, 1, 1, 1): -1}
check_true("S4: chi(tau) = 1,1,0,-1,-1 from contents", all(chi_tau(l) == v for l, v in s4.items()))
check_true("S4 dims 1,3,2,3,1", [f_hook(l) for l in partitions(4)] == [1, 3, 2, 3, 1])
check_true("S5 dims 1,4,5,6,5,4,1, squares add to 120", [f_hook(l) for l in partitions(5)] == [1, 4, 5, 6, 5, 4, 1] and sum(f_hook(l) ** 2 for l in partitions(5)) == 120)
check_true("hooks of (3,2) are 4,3,1,2,1 and of (3,1,1) are 5,2,1,2,1", hooks((3, 2)) == [4, 3, 1, 2, 1] and hooks((3, 1, 1)) == [5, 2, 1, 2, 1])
# Brute-force transposition character: chi^lambda(tau) via the Frobenius formula for characters (power sums -> Schur), using sympy
import sympy as sp
def schur_coeff_check(n):
    xs = sp.symbols(f"x1:{n+1}")
    def schur(l):
        l = list(l) + [0] * (n - len(l))
        num = sp.Matrix(n, n, lambda i, j: xs[i] ** (l[j] + n - 1 - j)).det()
        den = sp.Matrix(n, n, lambda i, j: xs[i] ** (n - 1 - j)).det()
        return sp.Poly(sp.cancel(num / den), *xs)
    p1, p2 = sum(xs), sum(x ** 2 for x in xs)
    prod = sp.Poly(sp.expand(p2 * p1 ** (n - 2)), *xs)
    # chi^lambda(tau) = coefficient of s_lambda in p2 p1^{n-2}; read it on the leading monomial x^{lambda} after subtracting
    rem, ok = prod, True
    for l in partitions(n):          # partitions come in decreasing lexicographic (dominance-compatible) order
        mono = tuple(list(l) + [0] * (n - len(l)))
        c = rem.as_dict().get(mono, 0)
        ok &= (c == chi_tau(l))
        rem = rem - schur(l) * c
    return ok and rem.is_zero
check_true("chi^lambda(tau) = coefficient of s_lambda in p_2 p_1^(n-2), n=4,5", schur_coeff_check(4) and schur_coeff_check(5))
check_true("conjugation negates contents and keeps f", all(ratio(conj(l)) == -ratio(l) and f_hook(conj(l)) == f_hook(l) for n in range(2, 10) for l in partitions(n)))

check_true("ex:catalan: f^(n,n) = Catalan", all(f_hook((n, n)) == math.comb(2 * n, n) // (n + 1) for n in range(1, 12)))
check_true("ex:standardrep: f^(n-j,j) = C(n,j) - C(n,j-1)", all(f_hook((n - j, j) if j else (n,)) == math.comb(n, j) - (math.comb(n, j - 1) if j else 0) for n in range(2, 14) for j in range(0, n // 2 + 1)))
def frob(l):
    k = len(l); L = [l[i] + k - 1 - i for i in range(k)]
    return math.factorial(sum(l)) * math.prod(L[i] - L[j] for i in range(k) for j in range(i + 1, k)) // math.prod(math.factorial(x) for x in L)
check_true("ex:frobeniusdim: Frobenius' formula = hook formula", all(frob(l) == f_hook(l) for n in range(1, 13) for l in partitions(n)))
# Erdos-Szekeres bound is sharp: some sequence of rs numbers has no increasing r+1 and no decreasing s+1
r, s = 3, 4
w = [s * (r - 1 - i) + j for i in range(r) for j in range(s)]   # r increasing blocks of length s, in decreasing order
check_true("Erdos-Szekeres: rs numbers can avoid both", lis(w) == s and lis([-x for x in w]) == r)
# the limit shape: Omega(u) = (2/pi)(u arcsin(u/2) + sqrt(4-u^2)) meets |u| at u = +-2, and Omega(0) = 4/pi
Om = lambda u: 2 / math.pi * (u * math.asin(u / 2) + math.sqrt(max(0, 4 - u * u)))
check("Omega(2) = 2", Om(2), 2, 1e-12); check("Omega(0) = 4/pi", Om(0), 4 / math.pi, 1e-12)
finish()
