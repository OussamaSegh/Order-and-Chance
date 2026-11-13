"""Volume 10, Chapter 4 (Noetherian rings): the Groebner basis of ex:groebnerhand and the other computed examples."""
import sympy as sp, itertools, cmath
from common import check_true, finish
X, Y, Z = sp.symbols("X Y Z")
G = sp.groebner([X**2 - Y, X**3 - X], X, Y, order="lex")
check_true("reduced lex basis {X^2-Y, XY-X, Y^2-Y}", set(G.exprs) == {X**2 - Y, X*Y - X, Y**2 - Y})
sols = sp.solve(list(G.exprs), [X, Y], dict=True)
check_true("V(I) = {(0,0),(1,1),(-1,1)}", {(s_[X], s_[Y]) for s_ in sols} == {(0, 0), (1, 1), (-1, 1)})
# Each S-polynomial printed in the solution
g1, g2, g3, g4 = X**2 - Y, X**3 - X, X*Y - X, Y**2 - Y
check_true("S(g2,g1) = XY - X", sp.expand(g2 - X*g1) == X*Y - X)
check_true("S(g1,g3) = X^2 - Y^2", sp.expand(Y*g1 - X*g3) == X**2 - Y**2)
check_true("S(g1,g4) = X^2 Y - Y^3", sp.expand(Y**2*g1 - X**2*g4) == X**2*Y - Y**3)
check_true("g2 = X g1 + g3", sp.expand(X*g1 + g3 - g2) == 0)
# ex:radicals: radical of (X^2 Y, X Y^2) is (XY)
check_true("(XY)^2 = X * XY^2", sp.expand((X*Y)**2 - X*(X*Y**2)) == 0)
# ex:colouring: the triangle is 3-colourable; K4 is not (ideal is the unit ideal)
def ideal(edges, n):
    xs = sp.symbols(f"x0:{n}")
    return [x**3 - 1 for x in xs] + [xs[u]**2 + xs[u]*xs[v] + xs[v]**2 for u, v in edges], xs
I3, xs3 = ideal([(0, 1), (1, 2), (0, 2)], 3)
I4, xs4 = ideal([(i, j) for i in range(4) for j in range(i + 1, 4)], 4)
check_true("triangle: ideal proper", sp.groebner(I3, *xs3).exprs != [1])
check_true("K4: ideal is (1)", sp.groebner(I4, *xs4).exprs == [1])
w = cmath.exp(2j * cmath.pi / 3)
check_true("x^2+xy+y^2 = 0 for distinct cube roots", all(abs(a*a + a*b + b*b) < 1e-12 for a, b in itertools.permutations([1, w, w*w], 2)))
finish()
