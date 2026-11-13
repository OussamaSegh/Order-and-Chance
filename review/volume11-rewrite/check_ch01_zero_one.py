"""Volume 11, Chapter 1 (Independence and zero-one laws): the random harmonic series X = sum eps_n/n.
Its characteristic function prod cos(t/n), the bound |phi(t)| <= exp(-pi t/6) for t >= pi, the density g at 0 and its
flatness on [-1/2,1/2], g(2) close to 1/8, the tail P(X >= 4), the numbers of Exercise ex:subgauss, and the Paley-Zygmund 1/12."""
import math
import numpy as np
from scipy import integrate, special
from common import check, check_true, finish

N = 20000
n = np.arange(1, N + 1, dtype=float)
z2t = math.pi ** 2 / 6 - np.sum(1 / n ** 2)
z4t = math.pi ** 4 / 90 - np.sum(1 / n ** 4)
def phi(t):
    """prod_{n<=N} cos(t/n) times the tail exp(-t^2/2 zeta_N(2) - t^4/12 zeta_N(4)); the next tail term is below 1e-15."""
    t = np.atleast_1d(t).astype(float)
    out = np.empty_like(t)
    for a in range(0, len(t), 200):
        c = np.cos(np.outer(t[a:a + 200], 1 / n))
        sign = np.prod(np.sign(c), axis=1)
        out[a:a + 200] = sign * np.exp(np.sum(np.log(np.abs(c)), axis=1) - t[a:a + 200] ** 2 / 2 * z2t - t[a:a + 200] ** 4 / 12 * z4t)
    return out

ts = np.linspace(math.pi, 40, 400)
check_true("|phi(t)| <= exp(-pi t/6) on [pi, 40]", np.all(np.abs(phi(ts)) <= np.exp(-math.pi * ts / 6)))

T = np.linspace(0, 45, 18001); P = phi(T)
def g(x): return integrate.simpson(np.cos(x * T) * P, x=T) / math.pi
check("g(0)", g(0), 0.249994, 1e-6)
xs = np.linspace(0, 0.5, 51); gs = np.array([g(x) for x in xs])
check_true("0.2495 <= g <= 0.25 on [0, 1/2]", np.all((gs >= 0.2495) & (gs <= 0.25)))
check("g(2) close to 1/8 (Schmuland: within 1e-42; double precision here)", g(2), 0.125, 1e-9)
# P(X >= 4) = 1/2 - int_0^4 g = 1/2 - (1/pi) int sin(4t)/t phi(t) dt
sinc = np.where(T > 0, np.sin(4 * T) / np.where(T > 0, T, 1), 4.0)
tail = 0.5 - integrate.simpson(sinc * P, x=T) / math.pi
check("P(X >= 4)", tail, 2.0e-7, 0.1e-7)
check("ex:subgauss bound e^{-48/pi^2}", math.exp(-48 / math.pi ** 2), 7.7e-3, 0.05e-3)
sd = math.pi / math.sqrt(6)
check("standard deviation pi/sqrt 6", sd, 1.2825, 1e-4)
check("4/sd", 4 / sd, 3.119, 1e-3)
check("P(N(0,1) >= 3.119)", 0.5 * special.erfc(4 / sd / math.sqrt(2)), 9.1e-4, 0.05e-4)
check("Paley-Zygmund with theta=1/2 and E T^4 <= 3 sigma^4", (1 - 0.5) ** 2 / 3, 1 / 12, 1e-15)
# Polya urn: probability of a sequence with r reds among n is r! g!/(n+1)!
from fractions import Fraction
import itertools
def seqprob(seq):
    r, gg, p = 1, 1, Fraction(1)
    for x in seq:
        p *= Fraction(r if x else gg, r + gg)
        if x: r += 1
        else: gg += 1
    return p
check_true("Polya urn: P(sequence) = r! g!/(n+1)! for n <= 8", all(seqprob(s) == Fraction(math.factorial(sum(s)) * math.factorial(len(s) - sum(s)), math.factorial(len(s) + 1)) for m in range(1, 9) for s in itertools.product([0, 1], repeat=m)))
finish()
