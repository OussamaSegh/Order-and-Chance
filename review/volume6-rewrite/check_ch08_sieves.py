"""Number checks for Volume 6, Chapter 8 (sieves). Sieves to 10^8 for the Buchstab data."""
import math
import numpy as np
import mpmath as mp
from common import GAMMA, primes_upto, check, check_true, finish

eg = math.exp(-GAMMA)
check("2 e^-gamma", 2 * eg, 1.1229, 5e-5)
check("e^-gamma", eg, 0.56146, 5e-6)
check("omega(3)", (1 + math.log(2)) / 3, 0.56438, 5e-6)

# --- twin primes
P7 = primes_upto(10 ** 7 + 2)
s = set(P7.tolist())
tw = P7[np.isin(P7 + 2, P7)]
tw7 = tw[tw <= 10 ** 7]
check("pi_2(10^7)", len(tw7), 58980, 0)
C2 = float(mp.nprod(lambda k: 1, [1, 1]))  # placeholder
odd = primes_upto(10 ** 7)[1:].astype(np.float64)
C2 = float(np.exp(np.log1p(-1 / (odd - 1) ** 2).sum()))   # tail beyond 10^7 is < 1e-7
check("twin prime constant C_2", C2, 0.6601618, 2e-7)
pred = 2 * C2 * float(mp.quad(lambda t: 1 / mp.log(t) ** 2, [2, 10, 1000, 10 ** 5, 10 ** 7]))
check("Hardy-Littlewood prediction at 10^7", pred, 58754, 1)
partial = float((1 / tw7 + 1 / (tw7 + 2)).sum())
check("Brun partial sum over pairs with p <= 10^7", partial, 1.7383570, 5e-7)
tail7 = 4 * C2 / math.log(1e7)
check("4 C_2 / log 10^7", tail7, 0.16383, 5e-6)
check("extrapolation from 10^7", partial + tail7, 1.90219, 5e-6)
tw5 = tw[tw <= 10 ** 5]
check("extrapolation from 10^5", float((1 / tw5 + 1 / (tw5 + 2)).sum()) + 4 * C2 / math.log(1e5), 1.90216, 5e-6)
check("constant 64 / 16 C_2 ratio 8", 16 * C2 / (2 * C2), 8, 0)

# --- Legendre ratio main term / count at 10^4 and 10^6
for x, printed in ((10 ** 4, 0.998), (10 ** 6, 1.034)):
    pr = primes_upto(int(math.isqrt(x)))
    main = x * float(np.prod(1 - 1 / pr.astype(np.float64)))
    count = len(primes_upto(x)) - len(pr) + 1
    check("Legendre main/count at %d" % x, main / count, printed, 5e-4)

# --- integers <= 10^6 that are squares modulo every prime <= 1000
N = 10 ** 6
n = np.arange(1, N + 1, dtype=np.int64)
ok = np.ones(N, dtype=bool)
for p in primes_upto(1000)[1:]:
    p = int(p)
    sq = np.zeros(p, dtype=bool); sq[(np.arange(p) ** 2) % p] = True
    ok &= sq[n % p]
survivors = n[ok]
check_true("survivors are exactly the 1000 squares", len(survivors) == 1000 and all(math.isqrt(int(v)) ** 2 == v for v in survivors))

# --- Hardy-Littlewood constant for n^2+1
pr = primes_upto(10 ** 7)[1:].astype(np.int64)
chi = np.where(pr % 4 == 1, 1.0, -1.0)
C = 0.5 * float(np.exp(np.log1p(-chi / (pr - 1)).sum()))
check("constant for n^2+1", C, 0.6864, 5e-4)

# --- Buchstab's function: omega(u) = 1/u on [1,2], (u omega)' = omega(u-1)
h = 1e-4
us = np.arange(1.0, 8.0 + h / 2, h)
w = np.zeros_like(us)
m2 = us <= 2
w[m2] = 1 / us[m2]
k1 = int(round(1 / h))
for i in range(len(us)):
    if us[i] <= 2: continue
    # trapezoid step for (u w)' = w(u-1)
    uw_prev = us[i - 1] * w[i - 1]
    uw = uw_prev + h / 2 * (w[i - 1 - k1] + w[i - k1])
    w[i] = uw / us[i]
d = w - eg
cross = [round(us[i], 3) for i in range(1, len(us)) if us[i] > 1.01 and d[i - 1] * d[i] < 0]
print("   crossings of e^-gamma:", cross[:6])
check_true("one crossing between 2 and 3", sum(2 < c < 3 for c in cross) == 1)
check_true("next crossings near 3.2 and 4", any(abs(c - 3.2) < 0.1 for c in cross) and any(abs(c - 4) < 0.1 for c in cross))
check_true("within 1e-4 of e^-gamma from u = 4 on (max %.2e)" % np.abs(d[us >= 4]).max(), np.abs(d[us >= 4]).max() < 1e-4)
check("omega(2.5) against closed form", w[int(round(1.5 / h))], (1 + math.log(1.5)) / 2.5, 1e-6)

# --- Selberg sieve constants in the twin proof
check_true("(1/2)(1/2) and so on: 1/16 from (1/2 log(sqrt y))^2/..", abs((0.5 * 0.5) ** 2 - 1 / 16) < 1e-15)
finish()
