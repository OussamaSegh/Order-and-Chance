"""Volume 10, Chapter 6 (Dedekind domains): Z[sqrt-5], the cubic of the figure, the circle and the cubic exercises."""
import itertools, sympy as sp
from common import check_true, finish
x, y, w = sp.symbols("x y w")  # w = sqrt(-5), w^2 = -5

# Ideals of Z[sqrt-5] as Z-lattices: Hermite normal form of the Z-span of generators times {1, w}
def lattice(gens):
    vecs = []
    for g in gens:
        a, b = g
        vecs += [(a, b), (-5 * b, a)]          # g*1 and g*w
    M = sp.Matrix(vecs)
    from sympy.matrices.normalforms import hermite_normal_form
    H = hermite_normal_form(M.T).T
    return sorted(tuple(r) for r in H.tolist() if any(r))
def mul(g, h): return (g[0] * h[0] - 5 * g[1] * h[1], g[0] * h[1] + g[1] * h[0])
def prod(I, J): return [mul(g, h) for g in I for h in J]
p, q, qb = [(2, 0), (1, 1)], [(3, 0), (1, 1)], [(3, 0), (1, -1)]
check_true("p^2 = (2)", lattice(prod(p, p)) == lattice([(2, 0)]))
check_true("q qbar = (3)", lattice(prod(q, qb)) == lattice([(3, 0)]))
check_true("p q = (1+w)", lattice(prod(p, q)) == lattice([(1, 1)]))
check_true("p qbar = (1-w)", lattice(prod(p, qb)) == lattice([(1, -1)]))
check_true("a^2+5b^2 = 2 has no solution", not any(a * a + 5 * b * b == 2 for a in range(-2, 3) for b in range(-2, 3)))
# integral closure: A^2 + B^2 = 0 mod 4 forces A, B even
check_true("A^2+5B^2 = 0 mod 4 => A, B even", all((A % 2 == 0 and B % 2 == 0) for A in range(8) for B in range(8) if (A * A + 5 * B * B) % 4 == 0))

# Figure fig:cubicclass: y^2 = x^3 - x + 1, line y = 1 - 2x
E = lambda X, Y: Y**2 - (X**3 - X + 1)
for P in [(0, 1), (1, -1), (3, -5), (3, 5)]: check_true(f"{P} on E", E(*P) == 0)
check_true("line meets E at x = 0, 1, 3", sp.factor(sp.expand((1 - 2 * x)**2 - (x**3 - x + 1))) == -x * (x - 3) * (x - 1))

# ex:circle: (x-1)^2 + y^2 = -2(x-1) on the circle
check_true("circle identity", sp.expand(((x - 1)**2 + (1 - x**2)) + 2 * (x - 1)) == 0)
# ex:cubicnotprincipal: x = x^3 - y^2 on y^2 = x^3 - x; omega for Z[sqrt-3]
check_true("x = x*x^2 - y^2", sp.expand(x * x**2 - (x**3 - x) - x) == 0)
om = (1 + sp.sqrt(-3)) / 2
check_true("omega^2 - omega + 1 = 0", sp.simplify(om**2 - om + 1) == 0)
check_true("(1+sqrt-3)^2 = 2(-1+sqrt-3)", sp.expand((1 + sp.sqrt(-3))**2 - 2 * (-1 + sp.sqrt(-3))) == 0)
finish()
