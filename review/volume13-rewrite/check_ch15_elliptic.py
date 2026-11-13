"""Volume 13, Chapter 15 (elliptic curves): the triangles of area 6 and 5, the congruent points of E_5, E_7, doubling on
E_6, torsion of y^2=x^3+1 and of y^2=x^3-43x+166, Bachet's duplication, point counts for p = 2 mod 3, Mazur's list."""
from fractions import Fraction as F
import sympy
from common import check, check_true, finish

def add(P, Q, a):
    if P is None: return Q
    if Q is None: return P
    (x1, y1), (x2, y2) = P, Q
    if x1 == x2 and y1 == -y2: return None
    lam = (3 * x1 * x1 + a) / (2 * y1) if P == Q else (y2 - y1) / (x2 - x1)
    x3 = lam * lam - x1 - x2
    return (x3, lam * (x1 - x3) - y1)
def order(P, a, nmax=20):
    Q = P
    for k in range(1, nmax):
        if Q is None: return k
        Q = add(Q, P, a)
    return None
def tri_from_point(x, y, n):
    a = abs((x * x - n * n) / y); b = abs(2 * n * x / y); c = abs((x * x + n * n) / y)
    return a, b, c
def is_tri(a, b, c, n): return a * a + b * b == c * c and a * b / 2 == n
check_true("7/10, 120/7, 1201/70: right triangle of area 6", is_tri(F(7, 10), F(120, 7), F(1201, 70), 6))
check_true("3/2, 20/3, 41/6: right triangle of area 5", is_tri(F(3, 2), F(20, 3), F(41, 6), 5))
# point of 3,4,5 on E_6: x = n(a? ) use x = c^2/4 ; P=(12,36)? check (12)^3-36*12 = 1296 = 36^2
P = (F(12), F(36)); check_true("(12,36) on E_6", P[1]**2 == P[0]**3 - 36 * P[0])
P2 = add(P, P, -36)
t2 = tuple(sorted(tri_from_point(P2[0], P2[1], 6)))
check_true("doubling (12,36) gives the triangle 7/10, 120/7, 1201/70", t2 == tuple(sorted((F(7, 10), F(120, 7), F(1201, 70)))))
P4 = add(P2, P2, -36)
t4 = tri_from_point(P4[0], P4[1], 6)
check_true("doubling again gives a third triangle of area 6", is_tri(*sorted(t4)[:2], sorted(t4)[2], 6) and tuple(sorted(t4)) != t2)
check_true("E_5 at x=-4: y=6; E_7 at x=25: y=120", (-4)**3 + 100 == 36 and 25**3 - 49 * 25 == 120**2)
for n, x, y in [(5, F(-4), F(6)), (7, F(25), F(120))]:
    a, b, c = tri_from_point(x, y, n); check_true(f"triangle of area {n} from the point", is_tri(*sorted([a, b]), c, n))
check_true("(2,3) has order 6 on y^2=x^3+1", order((F(2), F(3)), 0) == 6)
check_true("(3,8) has order 7 on y^2=x^3-43x+166", order((F(3), F(8)), -43) == 7)
xx, yy = F(3), F(5)
check_true("Bachet: x(2P) = (x^4-8cx)/(4y^2) for (3,5) on y^2=x^3-2", add((xx, yy), (xx, yy), 0)[0] == (xx**4 + 16 * xx) / (4 * yy**2))
x2 = add((xx, yy), (xx, yy), 0); check_true("2(3,5) = (129/100, 383/1000)", x2 == (F(129, 100), F(-383, 1000)) or x2 == (F(129, 100), F(383, 1000)))
ok = all(sum(1 for x in range(p) for y in range(p) if (y * y - x**3 - c) % p == 0) + 1 == p + 1
         for p in sympy.primerange(5, 120) if p % 3 == 2 for c in range(1, p))
check_true("y^2=x^3+c has p+1 points for p = 2 mod 3", ok)
check_true("Mazur: 15 groups", len(list(range(1, 11)) + [12]) + 4 == 15)
finish()
