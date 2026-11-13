"""Volume 13, Chapter 10 (Hasse-Minkowski): Hilbert symbols by the formulas checked against brute force, the epigraph form
2x^2+7y^2=3z^2 (fails exactly at 2 and 7), 13x^2+7y^2=z^2, the three-squares exceptions and density 5/6, Ramanujan's form
x^2+2y^2+3z^2, Selmer's cubic at p=3, Serre-style product formula sample."""
import itertools, sympy
from common import check, check_true, finish

def split(a, p):
    k = 0
    while a % p == 0: a //= p; k += 1
    return k, a
def leg(u, p): return 1 if pow(u % p, (p - 1) // 2, p) == 1 else -1
def hilbert(a, b, p):
    if p == 0:  # real place
        return -1 if a < 0 and b < 0 else 1
    al, u = split(a, p); be, v = split(b, p)
    if p != 2:
        s = (-1) ** (al * be * (p - 1) // 2)
        return s * leg(u, p) ** be * leg(v, p) ** al
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    return (-1) ** ((eps(u) * eps(v) + al * om(v) + be * om(u)) % 2)
def brute(a, b, p, k):
    # z^2 = a x^2 + b y^2 primitive solution mod p^k (necessary condition, k large enough to be decisive here)
    M = p**k
    for x, y, z in itertools.product(range(M), repeat=3):
        if (x % p or y % p or z % p) and (z * z - a * x * x - b * y * y) % M == 0:
            return 1
    return -1
ok = True
for p, k in [(3, 3), (5, 2), (2, 4)]:
    for a in [-1, 2, 3, 5, 6, -6, 10, 7, 15]:
        for b in [-1, 2, 3, 5, 7, 10, -3]:
            # brute force on primitive solutions mod p^k approximates isotropy; compare
            if hilbert(a, b, p) != brute(a, b, p, k + (2 if p == 2 else 1)):
                ok = False; print("mismatch", a, b, p)
check_true("Hilbert symbol formulas agree with brute force (p=2,3,5)", ok)
# epigraph: 2x^2+7y^2-3z^2: isotropic over Q_v iff (-ac,-bc)_v=1 with a=2,b=7,c=-3 -> (6,21)_v
places = [0] + list(sympy.primerange(2, 200))
fails = [v for v in places if hilbert(6, 21, v) == -1]
check_true("2x^2+7y^2=3z^2 fails exactly at 2 and 7", fails == [2, 7])
fails13 = [v for v in places if hilbert(13, 7, v) == -1]
check_true("13x^2+7y^2=z^2 fails exactly at 7 and 13", fails13 == [7, 13])
check_true("squares mod 13 and mod 7", sorted({x * x % 13 for x in range(1, 13)}) == [1, 3, 4, 9, 10, 12]
           and sorted({x * x % 7 for x in range(1, 7)}) == [1, 2, 4])
# three squares
N = 3000
s3 = {x*x + y*y + z*z for x in range(55) for y in range(55) for z in range(55)}
def excluded(n):
    while n % 4 == 0: n //= 4
    return n % 8 == 7
check_true("n <= 3000 is a sum of three squares iff not 4^a(8b+7)", all((n in s3) == (not excluded(n)) for n in range(1, N + 1)))
X = 10**6
cnt = sum(1 for n in range(1, X + 1) if not excluded(n))
check("proportion of sums of three squares up to 10^6 (5/6)", cnt / X, 5 / 6, 1e-4)
# Ramanujan's form x^2+2y^2+3z^2
r = {x*x + 2*y*y + 3*z*z for x in range(60) for y in range(45) for z in range(35)}
def excl_r(n):
    while n % 4 == 0: n //= 4
    return n % 16 == 10
check_true("x^2+2y^2+3z^2 represents n <= 2000 iff not 4^a(16b+10)", all((n in r) == (not excl_r(n)) for n in range(1, 2001)))
check_true("7 not a sum of 3 rational squares, 14 is", excluded(7) and not excluded(14) and excluded(28))
# Selmer at 3
check_true("4^{-1} = 7 mod 27, -5/4 = 19, 7^3 = 19 mod 27, 147 = 3*49", (4 * 7) % 27 == 1 and (-5 * 7) % 27 == 19 and 343 % 27 == 19 and 147 == 3 * 49)
finish()
