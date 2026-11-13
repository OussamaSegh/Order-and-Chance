"""Volume 10, Chapter 5 (Localisation and Dimension): the examples and solutions that compute something."""
import sympy as sp
from sympy import groebner, symbols, sqrt, expand, Poly
from common import check_true, finish
x, y, t = symbols("x y t")

# (12) = (4) cap (3), and the primary example (x^2, xy) = (x) cap (x^2, y): intersection by elimination of t
def intersect(I, J, gens):
    G = groebner([t * f for f in I] + [(1 - t) * g for g in J], t, *gens, order="lex")
    return [g for g in G.exprs if not g.has(t)]
inter = intersect([x], [x**2, y], [x, y])
check_true("(x) cap (x^2,y) = (x^2, xy)", set(groebner(inter, x, y, order="lex").exprs) == set(groebner([x**2, x*y], x, y, order="lex").exprs))
check_true("lcm(4,3) = 12", sp.ilcm(4, 3) == 12)

# Theorem thm:speczx and the figure: x^2+1 mod p splits iff p = 1 mod 4, double root at 2
for p in sp.primerange(3, 200):
    nf = len(sp.factor_list(x**2 + 1, modulus=p)[1])
    if (nf == 2) != (p % 4 == 1): check_true(f"x^2+1 mod {p}", False)
check_true("x^2+1 splits mod p iff p = 1 (4), p < 200", True)
check_true("x^2+1 = (x+1)^2 mod 2", Poly(x**2 + 1 - (x + 1)**2, x, modulus=2).is_zero)
check_true("chain 0 < (x^2+1) < (5, x-2): 2^2+1 = 0 mod 5", (2**2 + 1) % 5 == 0)

# ex:golden
phi = (1 + sqrt(5)) / 2
check_true("phi^2 - phi - 1 = 0", sp.simplify(phi**2 - phi - 1) == 0)
s_ = sqrt(2) + sqrt(3)
check_true("(sqrt2+sqrt3)^4 - 10(...)^2 + 1 = 0", sp.simplify(expand(s_**4 - 10 * s_**2 + 1)) == 0)
# ex:hyperbola: y^2 - (x+y)y + 1 = 1 - xy
check_true("y^2-(x+y)y+1 = 1-xy", expand(y**2 - (x + y) * y + 1 - (1 - x * y)) == 0)
# Lemma lem:noethervar: base-r exponents distinct
import itertools
r, n = 4, 3
es = {a[2] + a[0] * r + a[1] * r * r for a in itertools.product(range(r), repeat=n)}
check_true("e(alpha) injective on exponents < r", len(es) == r**n)
finish()
