"""Volume 13, Chapter 4 (ideals and splitting): the splitting data of Examples cubesplit and zetap, the figure of cycle
types of X^5-X-1 (17 982 primes, deviation 0.003), disc(Phi_l), and Exercise stickelbergerp on Q(cbrt2)."""
from collections import Counter
from sympy import symbols, Poly, factor_list, primerange, discriminant, cyclotomic_poly, legendre_symbol, n_order, primitive_root, GF, factorint, isprime
from sympy.combinatorics import Permutation
from itertools import permutations
from common import check, check_true, finish
X = symbols("X")
def degs(f, p):
    return sorted(Poly(g, X, modulus=p).degree() for g, e in Poly(f, X, modulus=p).factor_list()[1] for _ in range(e))
check_true("X^3-2 mod 5 = (X-3)(X^2+3X+4)", sorted(str(g.as_expr()) for g, e in Poly(X**3 - 2, X, modulus=5).factor_list()[1]) == sorted([str(Poly(X - 3, X, modulus=5).as_expr()), str(Poly(X**2 + 3*X + 4, X, modulus=5).as_expr())]))
check_true("X^3-2 mod 7 irreducible", degs(X**3 - 2, 7) == [3])
check_true("roots of X^3-2 mod 31 are 4,7,20", sorted(x for x in range(31) if (x**3 - 2) % 31 == 0) == [4, 7, 20])
check_true("2 generates F_29^*", primitive_root(29) == 2)
check_true("primitive 7th roots mod 29 = powers of 16: 16,24,7,25,23,20", [pow(16, k, 29) for k in range(1, 7)] == [16, 24, 7, 25, 23, 20])
check_true("order of 13 mod 7 is 2; of 2 and 11 is 3", n_order(13, 7) == 2 and n_order(2, 7) == 3 and n_order(11, 7) == 3)
check_true("Phi_7 mod 2 = two cubics", degs(cyclotomic_poly(7, X), 2) == [3, 3])
for l in [3, 5, 7, 11, 13]:
    check_true(f"disc Phi_{l} = +-{l}^{l-2}", abs(discriminant(cyclotomic_poly(l, X), X)) == l**(l - 2))
f = X**5 - X - 1
check_true("disc X^5-X-1 = 2869 = 19*151", discriminant(f, X) == 2869 and factorint(2869) == {19: 1, 151: 1})
check_true("X^5-X-1 mod 5 irreducible", degs(f, 5) == [5])
check_true("X^5-X-1 mod 2 = (2)(3)", degs(f, 2) == [2, 3])
cnt = Counter(); n = 0
for p in primerange(2, 200000):
    if 2869 % p == 0: continue
    cnt[tuple(degs(f, p))] += 1; n += 1
check_true(f"primes < 2e5 not dividing 2869: {n}", n == 17982)
s5 = Counter(tuple(sorted(Permutation(list(q)).cycle_structure_list if False else [len(c) for c in Permutation(list(q)).full_cyclic_form])) for q in permutations(range(5)))
exp = {(1,1,1,1,1): 1, (1,1,1,2): 10, (1,1,3): 20, (1,2,2): 15, (1,4): 30, (2,3): 20, (5,): 24}
check_true("S5 cycle type counts 1,10,20,15,30,20,24", dict(s5) == exp)
dev = max(abs(cnt[k] / n - v / 120) for k, v in exp.items())
check(f"largest deviation", dev, 0.003, 0.0005)
check_true("S5: proportion with a fixed point = 76/120", sum(v for k, v in exp.items() if 1 in k) == 76)
# Exercise stickelbergerp on Q(cbrt2), d_K=-108: (d_K/p) = (-1)^{n-g}
for p, g in [(5, 2), (7, 1), (31, 3)]:
    check_true(f"p={p}: (-108/p) = (-1)^(3-{g})", legendre_symbol(-108 % p, p) == (-1) ** (3 - g))
# Exercise sqrtm10: 2+-sqrt(-10) norm 14; P=(2,sqrt-10) not principal: a^2+10b^2 != 2
check_true("a^2+10b^2 never 2 or 7", all(a*a + 10*b*b not in (2, 7) for a in range(-5, 6) for b in range(-2, 3)))
finish()
