"""Volume 10, Chapter 9 (Semisimple algebras and induction): Wedderburn dimension counts, Mackey and double cosets,
the Heisenberg group, the affine group, Q_8, dihedral groups, and the paqb theorem's integrality lemma on small cases."""
import itertools, math
from fractions import Fraction
from common import check, check_true, finish

def compose(p, q):            # p after q, permutations as tuples
    return tuple(p[i] for i in q)
def closure(gens, mul, e):
    G, frontier = {e}, [e]
    while frontier:
        new = []
        for g in frontier:
            for s in gens:
                h = mul(g, s)
                if h not in G: G.add(h); new.append(h)
        frontier = new
    return G
def classes(G, mul, inv):
    seen, out = set(), []
    for g in G:
        if g in seen: continue
        C = {mul(mul(x, g), inv(x)) for x in G}
        seen |= C; out.append(C)
    return out
pinv = lambda p: tuple(sorted(range(len(p)), key=lambda i: p[i]))

# S3, S4: number of classes and sum of squares of the degrees (Wedderburn)
for n, degs in [(3, [1, 1, 2]), (4, [1, 1, 2, 3, 3])]:
    G = set(itertools.permutations(range(n)))
    check_true(f"S{n}: {len(degs)} classes and sum of d^2 = {math.factorial(n)}", len(classes(G, compose, pinv)) == len(degs) and sum(d * d for d in degs) == len(G))

# Dihedral D_n: classes and degrees 1 (2 or 4 of them) and 2 (Ind psi_j)
for n in range(3, 11):
    rot = tuple((i + 1) % n for i in range(n)); ref = tuple((-i) % n for i in range(n))
    G = closure([rot, ref], compose, tuple(range(n)))
    ones = 2 if n % 2 else 4; twos = (n - 1) // 2 if n % 2 else (n - 2) // 2
    check_true(f"D_{n}: {ones} + {twos} classes, {ones}*1 + {twos}*4 = 2n", len(G) == 2 * n and len(classes(G, compose, pinv)) == ones + twos and ones + 4 * twos == 2 * n)

# Heisenberg group mod p: p^2+p-1 classes, p^2*1 + (p-1)*p^2 = p^3
for p in (3, 5):
    mul = lambda A, B: ((A[0] + B[0]) % p, (A[1] + B[1]) % p, (A[2] + B[2] + A[0] * B[1]) % p)   # (a,b,c) = [[1,a,c],[0,1,b],[0,0,1]]
    inv = lambda A: ((-A[0]) % p, (-A[1]) % p, (A[0] * A[1] - A[2]) % p)
    G = set(itertools.product(range(p), repeat=3))
    check_true(f"Heisenberg p={p}: inverse formula", all(mul(A, inv(A)) == (0, 0, 0) for A in G))
    check_true(f"Heisenberg p={p}: p^2+p-1 = {p*p+p-1} classes, degrees sum p^3", len(classes(G, mul, inv)) == p * p + p - 1 and p * p + (p - 1) * p * p == p ** 3)

# Affine group of F_q (q prime): q classes, q-1 linear characters and one of degree q-1
for q in (5, 7, 11):
    mul = lambda A, B: ((A[0] * B[0]) % q, (A[0] * B[1] + A[1]) % q)       # x -> ax+b
    inv = lambda A: (pow(A[0], -1, q), (-pow(A[0], -1, q) * A[1]) % q)
    G = {(a, b) for a in range(1, q) for b in range(q)}
    check_true(f"Aff(F_{q}): q classes, (q-1)*1 + (q-1)^2 = q(q-1)", len(classes(G, mul, inv)) == q and (q - 1) + (q - 1) ** 2 == q * (q - 1))
    # Frobenius group: the elements fixing no point, with 1, are the translations
    check_true(f"Aff(F_{q}): Frobenius kernel = translations, of order q", {g for g in G if g[0] == 1} == {g for g in G if g == (1, 0) or all((g[0] * x + g[1]) % q != x for x in range(q))})

# Q_8: five classes, degrees 1,1,1,1,2
qmul = lambda a, b: (a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3], a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2], a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1], a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0])
qinv = lambda a: (a[0], -a[1], -a[2], -a[3])
Q8 = closure([(0, 1, 0, 0), (0, 0, 1, 0)], qmul, (1, 0, 0, 0))
check_true("Q_8: 8 elements, 5 classes, 4*1 + 4 = 8", len(Q8) == 8 and len(classes(Q8, qmul, qinv)) == 5)

# Exercise ex:doublecosets: S_n on n points is doubly transitive, 2 double cosets of the stabiliser
for n in (4, 5):
    G = list(itertools.permutations(range(n))); H = [g for g in G if g[n - 1] == n - 1]
    dc = {frozenset(compose(compose(h, s), k) for h in H for k in H) for s in G}
    check_true(f"S_{n}: point stabiliser has 2 double cosets", len(dc) == 2)

# Burnside's lemma: |C| chi(g)/chi(1) is an algebraic integer; S4 check with the character table of Volume 3
sizes = [1, 6, 3, 8, 6]   # classes e, (12), (12)(34), (123), (1234)
table = [[1, 1, 1, 1, 1], [1, -1, 1, 1, -1], [2, 0, 2, -1, 0], [3, 1, -1, 0, -1], [3, -1, -1, 0, 1]]
check_true("S4: |C| chi(g)/chi(1) are integers", all(Fraction(sizes[j] * row[j], row[0]).denominator == 1 for row in table for j in range(5)))
check_true("S4 table: row orthogonality", all(sum(sizes[j] * a[j] * b[j] for j in range(5)) == (24 if a is b else 0) for a in table for b in table))
# Burnside's theorem applies to orders p^a q^b; A5 (order 60 = 2^2*3*5) is the smallest non-solvable group
check_true("60 has three prime factors", sorted({p for p in range(2, 61) if 60 % p == 0 and all(p % d for d in range(2, p))}) == [2, 3, 5])
finish()
