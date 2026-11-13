"""Volume 10, Chapter 3 (Tensors and Exactness): the finite computations of the examples and solutions."""
import math, sympy as sp
from common import check_true, finish

# ex:zmzncomp: Hom(Z/m, Z/n) has gcd(m, n) elements; Z/m (x) Z/n = (Z/n)/m(Z/n) has gcd(m, n) elements
ok_hom = all(sum(1 for x in range(n) if m * x % n == 0) == math.gcd(m, n) for m in range(1, 25) for n in range(1, 25))
ok_ten = all(n // len({m * x % n for x in range(n)}) == math.gcd(m, n) for m in range(1, 25) for n in range(1, 25))
check_true("|Hom(Z/m,Z/n)| = gcd(m,n)", ok_hom); check_true("|Z/m (x) Z/n| = gcd(m,n)", ok_ten)

# ex:whichsplit: section 1 -> 4 in Z/6 has order 3 and maps to 1 mod 3
check_true("4 in Z/6 has order 3 and is 1 mod 3", (3 * 4) % 6 == 0 and 4 % 6 != 0 and 4 % 3 == 1)
check_true("Z/9 has an element of order 9", any(all(k * x % 9 for k in range(1, 9)) for x in range(9)))

# ex:tensoralgebra: X^2 - 3 irreducible over Q(sqrt 2); X^2 + 1 splits over C
x = sp.symbols("x")
check_true("x^2-3 irreducible over Q(sqrt2)", len(sp.factor_list(x**2 - 3, extension=sp.sqrt(2))[1]) == 1)
check_true("x^2+1 = (x-i)(x+i)", sp.expand((x - sp.I) * (x + sp.I)) == x**2 + 1)
a, b = sp.symbols("a b", rational=True)
check_true("no rational a+b sqrt2 with square 3", sp.solve([a**2 + 2*b**2 - 3, 2*a*b], [a, b]) == [] or all(not (s[0].is_rational and s[1].is_rational) for s in sp.solve([a**2 + 2*b**2 - 3, 2*a*b], [a, b])))
finish()
