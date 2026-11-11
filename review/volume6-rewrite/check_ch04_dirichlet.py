"""Number checks for Volume 6, Chapter 4 (Dirichlet's theorem)."""
import math
import numpy as np
import mpmath as mp
from common import GAMMA, primes_upto, check, check_true, finish

# --- The race modulo 4 up to 60000 (think box and figure).
P = primes_upto(60000)
lead = 0            # pi(x;4,3) - pi(x;4,1)
ties, behind = [], []
for p in P:
    if p % 4 == 3: lead += 1
    elif p % 4 == 1: lead -= 1
    if p > 2 and lead == 0: ties.append(int(p))
    if lead < 0: behind.append(int(p))
check_true("class 1 leads only at the prime 26861", behind == [26861])
nxt = int(P[np.searchsorted(P, 26861) + 1])
check("next prime after 26861", nxt, 26863, 0)
check_true("26863 = 3 mod 4", nxt % 4 == 3)
check("number of primes where the race is level", len(ties), 10, 0)
check("first tie", ties[0], 5, 0)
check("last tie", ties[-1], 26921, 0)

# --- Figure for q = 3: limits of sum_{p<=x, p=a (3)} log p / p - (1/2) log x.
mp.mp.dps = 30
Lf = lambda s: mp.mpf(3) ** (-s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))
h = mp.mpf(10) ** (-8)                               # symmetric difference around the removable point s = 1
ratio = float((Lf(1 + h) - Lf(1 - h)) / (2 * h) / ((Lf(1 + h) + Lf(1 - h)) / 2))
check("L'/L(1, chi_-3)", ratio, 0.368, 6e-4)
# prime powers p^k, k >= 2, by class modulo 3
Q = primes_upto(2_000_000)
pp = {1: 0.0, 2: 0.0}
for p in Q:
    p = int(p)
    if p == 3: continue
    lp, q, k = math.log(p), p * p, 2
    while q < 10 ** 16:
        pp[q % 3] += lp / q
        q *= p; k += 1
check("prime powers: class 1 minus class 2", pp[1] - pp[2], 0.308, 6e-4)
base = -GAMMA - 0.5 * math.log(3)        # limit of sum_{n<=x, 3 does not divide n} Lambda(n)/n - log x
c1 = 0.5 * (base - ratio) - pp[1]
c2 = 0.5 * (base + ratio) - pp[2]
check("limit for a = 1", c1, -1.188, 6e-4)
check("limit for a = 2", c2, -0.511, 6e-4)
check("gap", c2 - c1, 0.677, 6e-4)
# direct sums at x = 10^6 are already close to the limits
big = primes_upto(10 ** 6); big = big[big != 3]
w = np.log(big) / big
for a, c in ((1, c1), (2, c2)):
    s = float(w[big % 3 == a].sum()) - 0.5 * math.log(10 ** 6)
    check("direct sum at 10^6, a = %d" % a, s, {1: -1.187, 2: -0.512}[a], 6e-4)

finish()
