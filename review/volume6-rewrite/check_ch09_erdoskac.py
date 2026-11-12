"""Number checks for Volume 6, Chapter 9 (Erdos-Kac)."""
import math
import numpy as np
from common import primes_upto, check, check_true, finish

X = 10 ** 7
om = np.zeros(X + 1, dtype=np.int8)
P = primes_upto(X)
for p in P:
    om[p::p] += 1
w = om[1:].astype(np.float64)
L = math.log(math.log(X))
check("log log 10^7", L, 2.78, 5e-3)
check("mean of omega up to 10^7", w.mean(), 3.01, 5e-3)
check("variance of omega up to 10^7", w.var(), 1.10, 5e-3)
check("1/sqrt(log log 10^7)", 1 / math.sqrt(L), 0.6, 5e-3)
check("proportion with omega(n) <= log log x", (w <= L).mean(), 0.32, 5e-3)
check("log log 10^9", math.log(math.log(1e9)), 3.0, 0.05)
check("log log 10^99 (a hundred digits)", math.log(99 * math.log(10)), 5.4, 0.05)
check("1.4 log 2", 1.4 * math.log(2), 0.9704, 5e-5)
check("1/log 2", 1 / math.log(2), 1.4427, 5e-5)
# model skewness with all primes up to 10^7
pf = P.astype(np.float64)
v = (1 / pf) * (1 - 1 / pf)
m3 = (1 / pf) * (1 - 1 / pf) * (1 - 2 / pf)
check("model skewness, primes up to 10^7", m3.sum() / v.sum() ** 1.5, 0.49, 5e-3)
# multiplication table
for N, printed in ((100, 0.29), (1000, 0.25), (2000, 0.24)):
    a = np.arange(1, N + 1, dtype=np.int64)
    D = len(np.unique(np.outer(a, a)))
    check("D(%d)/N^2" % N, D / N ** 2, printed, 5e-3)
check("Ford's exponent", 1 - (1 + math.log(math.log(2))) / math.log(2), 0.086, 5e-4)
check("log 2", math.log(2), 0.693, 5e-4)
# Gaussian moments
check("m_6 = 15", 5 * 3 * 1, 15, 0)
finish()
