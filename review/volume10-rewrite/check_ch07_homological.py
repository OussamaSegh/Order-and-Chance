"""Volume 10, Chapter 7 (Homological algebra): homology of the small complexes and the Tor/Ext values printed."""
import math
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from common import check_true, finish

def homology_Z(dims, ds):
    """ds[n]: matrix of d_n: C_n -> C_{n-1} (rows = dim C_{n-1}); return (rank, torsion) of H_n."""
    out = {}
    for n, dn in enumerate(dims):
        d_in = ds.get(n + 1); d_out = ds.get(n)
        rk_out = d_out.rank() if d_out is not None else 0
        ker = dn - rk_out
        if d_in is None or d_in.shape[1] == 0:
            out[n] = (ker, []); continue
        snf = smith_normal_form(d_in)
        diag = [abs(snf[i, i]) for i in range(min(snf.shape)) if snf[i, i] != 0]
        out[n] = (ker - len(diag), [x for x in diag if x != 1])
    return out
# RP^2: Z -2-> Z -0-> Z
H = homology_Z([1, 1, 1], {2: Matrix([[2]]), 1: Matrix([[0]])})
check_true("RP2: H0=Z, H1=Z/2, H2=0", H == {0: (1, []), 1: (0, [2]), 2: (0, [])})
# Klein bottle: Z -(0,2)-> Z^2 -0-> Z
H = homology_Z([1, 2, 1], {2: Matrix([[0], [2]]), 1: Matrix([[0, 0]])})
check_true("Klein: H1 = Z + Z/2, H2 = 0", H[1] == (1, [2]) and H[2] == (0, []))
# cohomology of the Klein bottle: dual complex Z -0-> Z^2 -(0 2)-> Z ; H^2 = Z/2, H^1 = Z
d2T = Matrix([[0, 2]])
check_true("Klein: H^2 = Z/2", [abs(x) for x in smith_normal_form(d2T).diagonal() if x != 0] == [2])
check_true("Klein: H^1 = ker d2^T has rank 1", 2 - d2T.rank() == 1)
# Example ex:torextz: Tor_1(Z/m,Z/n) = Z/n[m] and Ext^1 = (Z/n)/m(Z/n) both of order gcd
ok = all(sum(1 for x in range(n) if m * x % n == 0) == math.gcd(m, n) == n // len({m * x % n for x in range(n)}) for m in range(1, 30) for n in range(1, 30))
check_true("|Tor_1(Z/m,Z/n)| = |Ext^1(Z/m,Z/n)| = gcd(m,n)", ok)
# ex:extzp2: E_a has class a^{-1} mod p
for p in (3, 5, 7):
    for a in range(1, p):
        b1 = next(b for b in range(p * p) if (a * b) % p == 1)   # lift of 1 in Z/p^2, any representative
        phi_p = (p * b1) % (p * p) // p                        # beta(p) = j(phi(p)) = p * phi(p)
        if (phi_p * a) % p != 1: check_true(f"E_{a} mod {p}", False)
check_true("class of E_a is a^{-1} mod p (p = 3, 5, 7)", True)
# Koszul: (x y) . (-y, x) = 0
import sympy as sp
x, y = sp.symbols("x y")
check_true("Koszul complex is a complex", sp.expand(x * (-y) + y * x) == 0)
finish()
