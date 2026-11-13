"""Volume 12, Chapter 5 (Brownian motion and analysis): Cameron--Martin's (cosh)^{-1/2} (ODE and Karhunen--Loeve product),
the annulus and ball-exit formulas, the finite-horizon maximum with drift, the strip decay rate, and the Cauchy exit law."""
import math
import numpy as np
from scipy import stats, integrate
from common import check, check_true, finish

lam, t = 1.3, 0.8
b = lambda s: lam * math.tanh(lam * s)
# b' = lam^2 - b^2 and a'/a = -b/2 with a = cosh^{-1/2}
h = 1e-6
check("b' = lam^2 - b^2", (b(t + h) - b(t - h)) / (2 * h), lam ** 2 - b(t) ** 2, 1e-6)
a = lambda s: math.cosh(lam * s) ** -0.5
check("a'/a = -b/2", (a(t + h) - a(t - h)) / (2 * h) / a(t), -b(t) / 2, 1e-6)
# KL product at t=1: prod (1 + lam^2/((n-1/2)^2 pi^2))^{-1/2} = cosh(lam)^{-1/2}
n = np.arange(1, 2_000_001)
check("prod (1+lam^2/((n-1/2)pi)^2) = cosh lam", float(np.exp(np.sum(np.log1p(lam ** 2 / ((n - 0.5) * math.pi) ** 2)))), math.cosh(lam), 1e-6)
# Monte Carlo of E exp(-lam^2/2 int_0^1 B^2)
rng = np.random.default_rng(5)
N, m = 20000, 1000
B = np.cumsum(rng.normal(scale=math.sqrt(1 / m), size=(N, m)), axis=1)
I = (B ** 2).mean(axis=1)
check("MC E exp(-lam^2/2 int B^2) vs cosh^{-1/2}", np.exp(-lam ** 2 / 2 * I).mean(), math.cosh(lam) ** -0.5, 0.01)
# annulus d=3: P_x(T_r<T_R) = (|x|^-1 - R^-1)/(r^-1 - R^-1); transience (r/|x|)^{d-2}
r, R, x = 1.0, 4.0, 2.0
check("d=3 annulus at R->infinity gives r/|x|", (x ** -1 - 0) / (r ** -1 - 0), r / x, 1e-15)
check("d=2 annulus formula at |x|=sqrt(rR) is 1/2", (math.log(R) - math.log(math.sqrt(r * R))) / (math.log(R) - math.log(r)), 0.5, 1e-15)
check_true("n^{2(2-d)} <= n^-2 for d>=3", all(k ** (2 * (2 - d)) <= k ** -2 for k in range(2, 50) for d in range(3, 7)))
# finite-horizon maximum with drift, against simulation
mu, A, T = -0.4, 0.7, 2.0
form = stats.norm.sf((A - mu * T) / math.sqrt(T)) + math.exp(2 * mu * A) * stats.norm.sf((A + mu * T) / math.sqrt(T))
steps = 2000
X = np.cumsum(rng.normal(scale=math.sqrt(T / steps), size=(20000, steps)) + mu * T / steps, axis=1)
check("P(max_{t<=T}(B_t+mu t) >= a) formula vs simulation", np.mean(X.max(axis=1) >= A), form, 0.02)
check("T -> infinity limit e^{2 mu a}", stats.norm.sf((A - mu * 1e6) / 1e3) + math.exp(2 * mu * A) * stats.norm.sf((A + mu * 1e6) / 1e3), math.exp(2 * mu * A), 1e-9)
# strip: v = e^{-pi^2 t/8a^2} cos(pi x/2a) solves v_t = v''/2
aa = 1.5
v = lambda t, x: math.exp(-math.pi ** 2 * t / (8 * aa ** 2)) * math.cos(math.pi * x / (2 * aa))
t0, x0 = 0.3, 0.4
vt = (v(t0 + h, x0) - v(t0 - h, x0)) / (2 * h)
vxx = (v(t0, x0 + 1e-4) - 2 * v(t0, x0) + v(t0, x0 - 1e-4)) / 1e-8
check("heat equation for the first strip mode", vt, vxx / 2, 1e-5)
check_true("sin x >= 2x/pi on [0, pi/2]", all(math.sin(u) >= 2 * u / math.pi - 1e-15 for u in np.linspace(0, math.pi / 2, 1000)))
# ball exit time E tau = (R^2-|x|^2)/d: d=2, R=1, x=0 -> 1/2 (simulation)
d, dt = 2, 1e-3
pos = np.zeros((4000, d)); alive = np.ones(4000, bool); T_ = np.zeros(4000)
while alive.any():
    pos[alive] += rng.normal(scale=math.sqrt(dt), size=(alive.sum(), d)); T_[alive] += dt
    alive &= (pos ** 2).sum(axis=1) < 1
check("E tau for the unit disc = 1/2", T_.mean(), 0.5, 0.03)
# half-plane exit point from (0,1): Cauchy; E exp(-xi^2 tau/2) = e^{-|xi|}
xi = 0.9
dens = lambda s: 1 / math.sqrt(2 * math.pi * s ** 3) * math.exp(-1 / (2 * s))
check("E exp(-xi^2 tau_1/2) = e^{-|xi|}", integrate.quad(lambda s: math.exp(-xi ** 2 * s / 2) * dens(s), 0, np.inf)[0], math.exp(-xi), 1e-8)
finish()
