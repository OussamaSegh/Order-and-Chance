#!/usr/bin/env python3
"""Volume 9, Chapter 10: check the explicit maps of the Riemann mapping chapter."""
import numpy as np
from mpmath import mp, quad, sqrt, exp, pi, mpc
from common import check, check_true, finish

rng = np.random.default_rng(2)
z = rng.normal(size=2000)*3+1j*np.abs(rng.normal(size=2000))*3+1e-3j     # upper half-plane
w = np.sqrt(rng.uniform(0, 1, 2000))*0.999*np.exp(2j*np.pi*rng.uniform(size=2000))  # disc
cay = lambda z: (z-1j)/(z+1j); icay = lambda w: 1j*(1+w)/(1-w)
check_true("Cayley map sends H into D", (abs(cay(z)) < 1).all())
check_true("inverse sends D into H", (icay(w).imag > 0).all())
check_true("the two maps undo each other", np.allclose(icay(cay(z)), z) and np.allclose(cay(icay(w)), w))
check_true("Im(i(1+w)/(1-w)) = (1-|w|^2)/|1-w|^2", np.allclose(icay(w).imag, (1-abs(w)**2)/abs(1-w)**2))
# disc automorphisms: |1 - a* z|^2 - |z - a|^2 = (1-|a|^2)(1-|z|^2); phi_{-a} o phi_a = id
a = 0.3-0.5j; phi = lambda a, z: (z-a)/(1-np.conj(a)*z)
check_true("|1-a*z|^2-|z-a|^2 = (1-|a|^2)(1-|z|^2)", np.allclose(abs(1-np.conj(a)*w)**2-abs(w-a)**2, (1-abs(a)**2)*(1-abs(w)**2)))
check_true("phi_{-a}(phi_a(z)) = z", np.allclose(phi(-a, phi(a, w)), w))
# strip |Im z| < pi/2 -> D by tanh(z/2), and (e^z - 1)/(e^z + 1) = tanh(z/2)
s = rng.normal(size=2000)*4+1j*rng.uniform(-np.pi/2, np.pi/2, 2000)*0.999
check_true("tanh(z/2) maps the strip into D", (abs(np.tanh(s/2)) < 1).all())
check_true("(e^z-1)/(e^z+1) = tanh(z/2)", np.allclose((np.exp(s)-1)/(np.exp(s)+1), np.tanh(s/2)))
check_true("inverse 2 artanh maps D into the strip", (abs((2*np.arctanh(w)).imag) < np.pi/2).all())
# slit plane -> D by (sqrt z - 1)/(sqrt z + 1)
sp_ = rng.normal(size=2000)*5+1j*rng.normal(size=2000)*5
f = (np.sqrt(sp_)-1)/(np.sqrt(sp_)+1)
check_true("(sqrt z - 1)/(sqrt z + 1) maps the slit plane into D", (abs(f) < 1).all())
inv = ((1+w)/(1-w))**2
check_true("and it is onto: inverse ((1+w)/(1-w))^2 lands back", np.allclose((np.sqrt(inv)-1)/(np.sqrt(inv)+1), w))
# the square map f(z) = int_0^z (1+w^4)^{-1/2} dw: the four corners f(e^{i pi/4 + i k pi/2}) form a square,
# and the arc between two corners goes to a straight side
mp.dps = 30
F = lambda zz: quad(lambda t: zz/sqrt(1+(t*zz)**4), [0, 1])
corners = [F(exp(1j*pi*(2*k+1)/4)*(1-mp.mpf(10)**-12)) for k in range(4)]
side = abs(corners[1]-corners[0])
check_true("four corners: rotations of each other by i", all(abs(corners[(k+1) % 4]-1j*corners[k]) < 1e-5 for k in range(4)))
check("|corner| = side/sqrt 2", abs(corners[0]), side/np.sqrt(2), 1e-5)
pts = [F(exp(1j*t)) for t in np.linspace(-0.7, 0.7, 9)]
check_true("image of the arc |arg z| < pi/4 is a vertical segment", max(abs(p.real-pts[4].real) for p in pts) < 1e-12)
# power series sum binom(-1/2,k) z^{4k+1}/(4k+1) agrees with the integral at z = 0.6+0.3i
from scipy.special import binom
z0 = 0.6+0.3j
ser = sum(binom(-0.5, k)*z0**(4*k+1)/(4*k+1) for k in range(200))
check("power series of the square map", abs(ser-complex(F(mpc(z0)))), 0, 1e-12)
finish()
