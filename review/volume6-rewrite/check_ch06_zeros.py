"""Number checks for Volume 6, Chapter 6 (the zeros of zeta)."""
import math
import mpmath as mp
from common import GAMMA, check, check_true, finish

mp.mp.dps = 20
zeros = [float(mp.zetazero(n).imag) for n in range(1, 81)]
check("first ordinate", zeros[0], 14.13, 5e-3)
check("number of zeros up to 100", sum(g <= 100 for g in zeros), 29, 0)
check("last ordinate below 100", max(g for g in zeros if g <= 100), 98.83, 5e-3)
check("N(200)", sum(g <= 200 for g in zeros), 79, 0)
check_true("80th zero is above 200", zeros[79] > 200)
# first gaps
for k, printed in enumerate((6.9, 4.0, 5.4)):
    check("gap %d" % (k + 1), zeros[k + 1] - zeros[k], printed, 0.05)

# S(T) = N(T) - alpha(T)/pi - 1, alpha the Riemann-Siegel phase
alpha = lambda T: float(mp.siegeltheta(T))
worst = 0.0
T = 1.0
while T <= 100:
    N = sum(g <= T for g in zeros)
    worst = max(worst, abs(N - alpha(T) / math.pi - 1))
    T += 0.001
# also just before and at each zero (the jumps)
for g in zeros:
    if g <= 100:
        for T in (g - 1e-9, g):
            N = sum(z <= T for z in zeros)
            worst = max(worst, abs(N - alpha(T) / math.pi - 1))
check("max |S(T)| on [1,100] is below 0.83", worst, 0.83, 0.83 - 0.0 if worst < 0.83 else -1)
print("   (max |S(T)| = %.4f)" % worst)
# main term asymptotic of alpha
for T in (50.0, 1000.0):
    approx = T / 2 * math.log(T / (2 * math.pi)) - T / 2 - math.pi / 8
    check("alpha(T) against its expansion at T = %g" % T, alpha(T), approx, 2 / T)

# B and the sum over zeros
B = 0.5 * math.log(4 * math.pi) - 1 - GAMMA / 2
check("B", B, -0.0230957, 5e-8)
check("1/2 log 4 pi", 0.5 * math.log(4 * math.pi), 1.2655121, 5e-8)
check("gamma/2", GAMMA / 2, 0.2886078, 5e-8)
check("-2B", -2 * B, 0.0461914, 5e-8)
part = sum(2 / (0.25 + g * g) for g in zeros)           # 1/|rho|^2 over the first 80 conjugate pairs
check_true("partial sum over 80 pairs stays below -2B, within the tail (about log(T/2pi)/(pi T) = 0.006)", 0 < -2 * B - part < 8e-3)
psi_half = float(mp.digamma(0.5))
check("psi_Gamma(1/2) = -gamma - 2 log 2", psi_half, -GAMMA - 2 * math.log(2), 1e-12)

# constants used in the proofs
check_true("2 - zeta(2) > 0.35", 2 - math.pi ** 2 / 6 > 0.35)
check_true("Gamma(1/4) < 4", math.gamma(0.25) < 4)
check_true("1/0.35 < 3", 1 / 0.35 < 3)
check_true("4/(7 log 2) < 1 and 16/(49 log 2) < 1", 4 / (7 * math.log(2)) < 1 and 16 / (49 * math.log(2)) < 1)

# exercise ex:nthzero
check("log(10^6/2pi)", math.log(1e6 / (2 * math.pi)), 11.98, 5e-3)
check("average gap at 10^6", 2 * math.pi / math.log(1e6 / (2 * math.pi)), 0.525, 5e-4)
check("log(14/2pi)", math.log(14 / (2 * math.pi)), 0.80, 5e-3)
check("formula near the first zero", 2 * math.pi / math.log(14 / (2 * math.pi)), 7.8, 0.05)
finish()
