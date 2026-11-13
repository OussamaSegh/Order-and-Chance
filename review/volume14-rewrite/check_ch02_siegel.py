#!/usr/bin/env python3
"""Volume 14, Chapter 2 (Siegel): printed numbers.

Tatuzawa's constants (0.655, 1/11, e^{11.2}) are quoted from his 1951 paper (Sources).
The chapter's other numbers are proved on the page. This script checks the class-number
example h(-p) against L(1, chi_p) = pi h / sqrt p for small p = 3 mod 4, the identity the
chapter cites from Volume 13.
"""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish
def legendre(a, p):
    t = pow(a % p, (p - 1) // 2, p); return -1 if t == p - 1 else t
def h_forms(D):
    """Class number of the discriminant D<0 by counting reduced forms."""
    h = 0; a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a) == 0:
                c = (b * b - D) // (4 * a)
                if c >= a and math.gcd(math.gcd(a, abs(b)), c) == 1 and not (b < 0 and (a == c)):
                    h += 1
        a += 1
    return h
for p in [7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107, 127, 131, 139, 151, 163]:
    # Dirichlet: for p = 3 mod 4, p > 3: h(-p) = -(1/p) sum_{n<p} n (n/p)
    h = -sum(n * legendre(n, p) for n in range(1, p)) // p
    check(f"h(-{p}) forms vs Dirichlet", h_forms(-p), h, 0)
check("Tatuzawa threshold e^{11.2}", math.exp(11.2), 73130.4, 0.1)
finish()
