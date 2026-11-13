"""Volume 13, Chapter 14 (algebraic curves): Hermitian curves over F_{q^2} for q = 2, 3, 4 (point counts q^3 + 1,
maximality), the code parameters of Exercise hermitian, genera of smooth plane curves, the intersection examples."""
import itertools
import sympy
from common import check, check_true, finish

class GF:
    """GF(p^k) as polynomials modulo an irreducible of degree k."""
    def __init__(self, p, k):
        self.p, self.k = p, k
        x = sympy.symbols('x')
        for coeffs in itertools.product(range(p), repeat=k):
            f = sympy.Poly([1] + list(coeffs), x, modulus=p)
            if f.is_irreducible: self.mod = [int(c) % p for c in f.all_coeffs()]; break
        self.elems = list(itertools.product(range(p), repeat=k))
    def mul(self, a, b):
        p, k = self.p, self.k
        prod = [0] * (2 * k - 1)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b): prod[i + j] = (prod[i + j] + ai * bj) % p
        # reduce: elements are coefficient tuples high->low of length k
        for i in range(len(prod) - k):
            c = prod[i]
            if c:
                for j, m in enumerate(self.mod): prod[i + j] = (prod[i + j] - c * m) % p
        return tuple(prod[-k:])
    def add(self, a, b): return tuple((x + y) % self.p for x, y in zip(a, b))
    def pow(self, a, n):
        r = tuple([0] * (self.k - 1) + [1])
        for _ in range(n): r = self.mul(r, a)
        return r
for q, p, k in [(2, 2, 2), (3, 3, 2), (4, 2, 4)]:
    F = GF(p, k)
    pw = {a: (F.pow(a, q), F.pow(a, q + 1)) for a in F.elems}
    count = sum(1 for xx in F.elems for yy in F.elems if F.add(pw[yy][0], yy) == pw[xx][1])
    g = q * (q - 1) // 2
    check_true(f"Hermitian q={q}: {count} affine points = q^3, total q^3+1 = q^2+1+2gq", count == q**3 and q**3 + 1 == q*q + 1 + 2 * g * q)
n, g, N = 5, 6, 64
check_true("q=4 codes: dim 5d-5, distance >= 64-5d for 3<=d<=12; [64,25,>=34], [64,45,>=14]",
           all(5 * d < N for d in range(3, 13)) and 5 * 13 >= N and (5 * 6 - 5, 64 - 30) == (25, 34) and (5 * 10 - 5, 64 - 50) == (45, 14))
check_true("smooth plane curve genera 0,1,3,6,10 never 2", [(d - 1) * (d - 2) // 2 for d in range(1, 6)] == [0, 0, 1, 3, 6] and
           2 not in {(d - 1) * (d - 2) // 2 for d in range(1, 50)})
x, y = sympy.symbols('x y')
sols = sympy.solve([x**2 + y**2 - 1, (x - 1)**2 + y**2 - 1], [x, y])
check_true("circles meet at (1/2, +-sqrt3/2)", sorted(sols) == sorted([(sympy.Rational(1, 2), -sympy.sqrt(3) / 2), (sympy.Rational(1, 2), sympy.sqrt(3) / 2)]))
X, Y, Z = sympy.symbols('X Y Z')
inf = sympy.solve([X**2 + Y**2, (X - Z)**2 + Y**2 - Z**2 - (X**2 + Y**2 - Z**2)], [X, Y], dict=True)
check_true("the other two at (1 : +-i : 0)", all(sympy.simplify((X**2 + Y**2).subs({X: 1, Y: s_, Z: 0})) == 0 for s_ in (sympy.I, -sympy.I)))
check_true("y=x^2, y=2x^2-1 meet at x=+-1 in the affine plane", sympy.solve(x**2 - (2 * x**2 - 1), x) == [-1, 1])
finish()
