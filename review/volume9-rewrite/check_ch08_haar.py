#!/usr/bin/env python3
"""Volume 9, Chapter 8: check the numbers printed in the chapter (Haar measure, Weyl, Dyson)."""
import itertools, math
import numpy as np, sympy as sp
from scipy import integrate
from common import check, check_true, finish

rng = np.random.default_rng(1)

def haar(n, size):
    Z = (rng.normal(size=(size, n, n)) + 1j*rng.normal(size=(size, n, n)))/np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    d = np.diagonal(R, axis1=1, axis2=2)
    return Q*(d/abs(d))[:, None, :]          # Q Lambda, the phase fix of Theorem qrhaar

# ax+b group: det Ad(h^{-1}) = 1/a
a, b, x, y = sp.symbols('a b x y', positive=True)
h = sp.Matrix([[a, b], [0, 1]]); X = sp.Matrix([[x, y], [0, 0]])
Mx = h.inv()*X*h
A = sp.Matrix([[sp.diff(Mx[0, 0], v), sp.diff(Mx[0, 1], v)] for v in (x, y)]).T
check_true("ax+b: h^{-1}Xh = [[x,(xb+y)/a],[0,0]]", sp.simplify(Mx - sp.Matrix([[x, (x*b+y)/a], [0, 0]])) == sp.zeros(2))
check_true("ax+b: det Ad(h^{-1}) = 1/a", sp.simplify(A.det() - 1/a) == 0)

# Vandermonde: prod(t_k - t_j) = det(t_k^{j-1}); integral of |V|^2 over the torus = (2pi)^n n!
for n in (2, 3, 4):
    t = sp.symbols(f't1:{n+1}')
    V = sp.Matrix(n, n, lambda j, k: t[k]**j).det()
    check_true(f"Vandermonde n={n}", sp.expand(V - sp.prod([t[k]-t[j] for j in range(n) for k in range(j+1, n)])) == 0)
for n in (2, 3):
    th = rng.uniform(0, 2*np.pi, size=(400000, n)); z = np.exp(1j*th)
    V2 = np.prod([abs(z[:, k]-z[:, j])**2 for j in range(n) for k in range(j+1, n)], axis=0)
    check(f"mean of |V|^2 on T, n={n} (= n!)", V2.mean(), math.factorial(n), 0.05*math.factorial(n))

# Weyl's formula against Gaussian sampling: E|tr U|^4 = 2 for n >= 2
n = 3
U = haar(n, 200000)
tr = np.trace(U, axis1=1, axis2=2)
th = rng.uniform(0, 2*np.pi, size=(400000, n)); z = np.exp(1j*th)
V2 = np.prod([abs(z[:, k]-z[:, j])**2 for j in range(n) for k in range(j+1, n)], axis=0)
weyl = (abs(z.sum(1))**4*V2).mean()/math.factorial(n)
check("E|tr U|^4, U(3), Haar sampling", (abs(tr)**4).mean(), 2, 0.05)
check("E|tr U|^4, U(3), Weyl integral", weyl, 2, 0.05)

# Exercise tracemoments: E|tr U^k|^2 = min(k, n)
n = 4; U = haar(n, 100000); P = U.copy()
for k in range(1, 7):
    if k > 1: P = P @ U
    check(f"E|tr U^k|^2, n=4, k={k}", (abs(np.trace(P, axis1=1, axis2=2))**2).mean(), min(k, n), 0.06*min(k, n))

# Exercise firstcolumn: P(|U11|^2 > x) = (1-x)^{n-1}
n = 5; U = haar(n, 200000); u = abs(U[:, 0, 0])**2
for xx in (0.1, 0.3):
    check(f"P(|U11|^2>{xx}), n=5", (u > xx).mean(), (1-xx)**(n-1), 0.005)

# Exercise su2weyl: rotation angle density (1-cos phi)/pi, mean pi/2 + 2/pi, 126.5 degrees
check("int_0^pi (1-cos)/pi", integrate.quad(lambda p: (1-np.cos(p))/np.pi, 0, np.pi)[0], 1, 1e-12)
mean = integrate.quad(lambda p: p*(1-np.cos(p))/np.pi, 0, np.pi)[0]
check("mean rotation angle = pi/2 + 2/pi", mean, np.pi/2+2/np.pi, 1e-12)
check("pi/2 + 2/pi printed 2.207", np.pi/2+2/np.pi, 2.207, 5e-4)
check("in degrees, printed 126.5", np.degrees(np.pi/2+2/np.pi), 126.5, 0.05)
q = rng.normal(size=(200000, 4)); q /= np.linalg.norm(q, axis=1)[:, None]   # Haar on SU(2) = S^3
phi = 2*np.arccos(abs(q[:, 0]))
check("Monte Carlo mean angle of a random rotation", phi.mean(), np.pi/2+2/np.pi, 0.01)
check("alpha density (2/pi) sin^2 integrates to 1", integrate.quad(lambda t: 2/np.pi*np.sin(t)**2, 0, np.pi)[0], 1, 1e-12)

# Exercise gap, n = 2: P(no eigenvalue in (-alpha, alpha)) = (1 - alpha/pi)^2 - sin^2(alpha)/pi^2
U = haar(2, 300000); ang = np.angle(np.linalg.eigvals(U))
for al in (0.5, 1.5):
    check(f"gap probability n=2, alpha={al}", (abs(ang) >= al).all(1).mean(), (1-al/np.pi)**2-np.sin(al)**2/np.pi**2, 0.005)
al = sp.symbols('alpha')
check_true("alpha^2 - sin^2 alpha = O(alpha^4)", sp.series(al**2-sp.sin(al)**2, al, 0, 4).removeO() == 0)

# Exercise repulsion: (eps - sin eps)/pi ~ eps^3/(6 pi); ratio about 600 at eps = 0.1
e = 0.1
check("ratio (eps/pi)/((eps - sin eps)/pi) at 0.1, printed 600", e/(e-np.sin(e)), 600, 1)

# Dyson: 1 - (sin pi u/(pi u))^2 ~ pi^2 u^2 / 3; kernel |K_n|^2 = sin^2(nx/2)/sin^2(x/2)
u = sp.symbols('u')
check_true("1 - (sin pi u / pi u)^2 = pi^2 u^2/3 + O(u^4)", sp.simplify(sp.series(1-(sp.sin(sp.pi*u)/(sp.pi*u))**2, u, 0, 4).removeO() - sp.pi**2*u**2/3) == 0)
xs = np.linspace(0.1, 3, 7); nn = 6
K = np.array([abs(sum(np.exp(1j*a*x0) for a in range(nn)))**2 for x0 in xs])
check_true("|K_n(x)|^2 = sin^2(nx/2)/sin^2(x/2)", np.allclose(K, np.sin(nn*xs/2)**2/np.sin(xs/2)**2))

# Dyson's limit for U(n): pair density from Theorem correlations, against Haar samples, n = 20
n = 20; U = haar(n, 4000); ang = np.angle(np.linalg.eigvals(U))
d = (ang[:, :, None]-ang[:, None, :]); d = (d+np.pi) % (2*np.pi)-np.pi
iu = ~np.eye(n, dtype=bool); s = n/(2*np.pi)*abs(d[:, iu])
emp = (s < 0.5).sum()/(n*len(U))
theory = 2*integrate.quad(lambda v: 1-np.sin(np.pi*v)**2/(n*np.sin(np.pi*v/n))**2 if v else 0, 0, 0.5)[0]
check("pairs at rescaled distance < 1/2 per eigenvalue, n=20", emp, theory, 0.01)
finish()
