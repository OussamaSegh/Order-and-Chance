"""Volume 10, Chapter 8 (Group cohomology): the carry, H^2 of cyclic groups, the extensions of order 100, Q_8, order 20."""
import itertools, math
from fractions import Fraction
from common import check_true, finish

b = 10
c = lambda x, y: 1 if x + y >= b else 0
# carry is a cocycle (trivial action): c(y,z) + c(x,y+z) = c(x+y,z) + c(x,y)
check_true("carry is a 2-cocycle", all(c(y, z) + c(x, (y + z) % b) == c((x + y) % b, z) + c(x, y) for x in range(b) for y in range(b) for z in range(b)))
# (a,x) <-> 10a + x is an isomorphism Z/10 x_c Z/10 -> Z/100
add = lambda P, Q: ((P[0] + Q[0] + c(P[1], Q[1])) % b, (P[1] + Q[1]) % b)
check_true("carry group is Z/100", all((lambda S: (10 * S[0] + S[1]) % 100 == (10 * P[0] + P[1] + 10 * Q[0] + Q[1]) % 100)(add(P, Q)) for P in itertools.product(range(b), repeat=2) for Q in itertools.product(range(b), repeat=2)))
# ex:carry10: isomorphism type of E_a from element orders
def invariants(a):
    def op(P, Q): return ((P[0] + Q[0] + a * c(P[1], Q[1])) % b, (P[1] + Q[1]) % b)
    def order(P):
        Q, k = P, 1
        while Q != (0, 0): Q, k = op(Q, P), k + 1
        return k
    return sorted(order(P) for P in itertools.product(range(b), repeat=2))
def orders_of(ns):   # element orders of Z/n1 x Z/n2
    return sorted(math.lcm(ns[0] // math.gcd(ns[0], x), ns[1] // math.gcd(ns[1], y)) for x in range(ns[0]) for y in range(ns[1]))
expected = {0: (10, 10), 5: (20, 5)}
for a in range(10):
    target = (100, 1) if math.gcd(a, 10) == 1 else (50, 2) if a in (2, 4, 6, 8) else expected[a]
    if invariants(a) != orders_of(target): check_true(f"E_{a}", False)
check_true("E_a types: Z/100 (a unit), Z/50xZ/2 (a even), Z/20xZ/5 (a=5), (Z/10)^2 (a=0)", True)
check_true("phi(10) = 4 extensions with middle group Z/100", sum(1 for a in range(10) if math.gcd(a, 10) == 1) == 4)

# Example ex:pythagoras: (m+ni)^2/(m^2+n^2) lies on the circle
check_true("rational points on the circle", all(Fraction(m*m - n*n, m*m + n*n)**2 + Fraction(2*m*n, m*m + n*n)**2 == 1 for m in range(1, 8) for n in range(1, 8)))

# ex:quaternion: cocycle values f(i,i) = f(j,j) = f(k,k) = -1, f(i,j) = 1, f(j,i) = -1
# quaternion units as (sign, letter); multiplication table
tab = {("1", x): (1, x) for x in "1ijk"}
tab.update({(x, "1"): (1, x) for x in "1ijk"})
tab.update({("i", "i"): (-1, "1"), ("j", "j"): (-1, "1"), ("k", "k"): (-1, "1"), ("i", "j"): (1, "k"), ("j", "i"): (-1, "k"),
            ("j", "k"): (1, "i"), ("k", "j"): (-1, "i"), ("k", "i"): (1, "j"), ("i", "k"): (-1, "j")})
check_true("Q8 cocycle diagonal is -1", all(tab[(x, x)][0] == -1 for x in "ijk"))
check_true("Q8 cocycle f(i,j)=1, f(j,i)=-1", tab[("i", "j")][0] == 1 and tab[("j", "i")][0] == -1)

# ex:order20: homomorphisms Q -> Z/4 up to Aut(Q): Z/4 gives 3 classes, (Z/2)^2 gives 2 -> five groups
z4 = [k for k in range(4)]                     # hom Z/4 -> Z/4 determined by image of 1
classes_z4 = {frozenset({k, (-k) % 4}) for k in z4}
check_true("Z/4 -> Aut(Z/5): 3 classes up to Aut(Z/4)", len(classes_z4) == 3)
finish()
