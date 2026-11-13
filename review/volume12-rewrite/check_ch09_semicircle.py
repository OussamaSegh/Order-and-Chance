"""Chapter 9 numbers: semicircle and Marchenko-Pastur moments, spike location, simulations."""
import numpy as np, mpmath as mp
from math import comb, sqrt
from common import check, check_true, finish

# semicircle moments are Catalan numbers
for k in range(0, 7):
    m = mp.quad(lambda x: x**(2*k)*mp.sqrt(4-x*x)/(2*mp.pi), [-2, 2])
    check(f"semicircle moment 2k={2*k}", m, comb(2*k, k)//(k+1), 1e-8)

# plane trees: enumerate as Dyck words; even vertices = root + vertices at even depth
def trees(k):
    def rec(word, up, down):
        if up == k and down == k: yield word; return
        if up < k: yield from rec(word+'U', up+1, down)
        if down < up: yield from rec(word+'D', up, down+1)
    yield from rec('', 0, 0)
def m_poly(k):
    coeff = {}
    for w in trees(k):
        d = 0; e = 1
        for c in w:
            if c == 'U':
                d += 1
                if d % 2 == 0: e += 1
            else: d -= 1
        coeff[e] = coeff.get(e, 0) + 1
    return coeff
check_true("m_2 = 1 + g", m_poly(2) == {1: 1, 2: 1})
check_true("m_3 = 1 + 3g + g^2", m_poly(3) == {1: 1, 2: 3, 3: 1})
for k in range(1, 9):
    check_true(f"Narayana k={k}", m_poly(k) == {r: comb(k, r)*comb(k, r-1)//k for r in range(1, k+1)})

# MP density moments match m_k(gamma)
for g in [mp.mpf('0.25'), mp.mpf('0.6')]:
    a, b = (1-mp.sqrt(g))**2, (1+mp.sqrt(g))**2
    for k in range(0, 6):
        mom = mp.quad(lambda x: x**k*mp.sqrt((b-x)*(x-a))/(2*mp.pi*g*x), [a, b])
        target = 1 if k == 0 else sum(c*g**(r-1) for r, c in m_poly(k).items())
        check(f"MP moment k={k} g={float(g)}", mom, target, 1e-8)
check("MP edges g=1/4", float((1-mp.sqrt(0.25))**2), 0.25, 1e-12)
check("MP edges g=1/4 upper", float((1+mp.sqrt(0.25))**2), 2.25, 1e-12)
th, g = 1.5, 0.25
check("BBP location", (1+th)*(1+g/th), 2.92, 0.005)
check_true("theta above threshold sqrt(gamma)", th > sqrt(g))

# spiked Wigner: G(theta+1/theta) = 1/theta; overlap 1 - 1/theta^2
for th in [1.2, 2.0, 3.5]:
    z = th + 1/th
    G = (z - sqrt(z*z-4))/2
    check(f"G(z_theta)=1/theta th={th}", G, 1/th, 1e-12)
    Gp = (1 - z/sqrt(z*z-4))/2
    check(f"overlap th={th}", G*G/(-Gp), 1-1/th**2, 1e-12)

# simulations behind the captions (several seeds)
rng = np.random.default_rng(12)
ok1 = ok2 = True
for s in range(5):
    n = 1000
    A = rng.standard_normal((n, n)); W = (A + A.T)/np.sqrt(2)
    ev = np.linalg.eigvalsh(W/np.sqrt(n)); ok1 &= abs(ev[0]+2) < 0.05 and abs(ev[-1]-2) < 0.05
    n = 2000
    B = rng.choice([-1.0, 1.0], size=(n, n)); B = np.triu(B) + np.triu(B, 1).T
    ev = np.linalg.eigvalsh(B/np.sqrt(n)); ok2 &= abs(ev[0]+2) < 0.05 and abs(ev[-1]-2) < 0.05
check_true("GOE n=1000 extremes within 0.05 of +-2 (5 seeds)", ok1)
check_true("signs n=2000 extremes within 0.05 of +-2 (5 seeds)", ok2)
# spiked covariance simulation: p=500, N=2000, theta=1.5
p, N = 500, 2000
X = rng.standard_normal((p, N)); X[0] *= sqrt(2.5)
top = np.linalg.eigvalsh(X @ X.T / N)[-1]
check("spiked covariance top eigenvalue near 2.92", top, 2.92, 0.15)
# GOE Lipschitz constant sqrt(2/n) gives e^{-n t^2/4}
check("concentration exponent", 1/(2*(2/1)), 1/4, 1e-15)
finish()
