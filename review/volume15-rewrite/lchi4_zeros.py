"""Zeros of L(s, chi_{-4}) on the critical line up to height T, by sign changes of the Hardy function and refinement."""
import mpmath, numpy as np
L = lambda s: mpmath.dirichlet(s, [0, 1, 0, -1])
def Zh(t):
    th = t / 2 * mpmath.log(4 / mpmath.pi) + mpmath.im(mpmath.loggamma((mpmath.mpf(1.5) + 1j * t) / 2))
    return float(mpmath.re(mpmath.exp(1j * th) * L(mpmath.mpc(0.5, t))))
def zeros(T, step=0.05):
    ts = np.arange(0.5, T, step); vals = [Zh(t) for t in ts]; out = []
    for a, b, va, vb in zip(ts[:-1], ts[1:], vals[:-1], vals[1:]):
        if va * vb < 0: out.append(float(mpmath.findroot(Zh, (a, b), solver='anderson')))
    return out
if __name__ == "__main__":
    import sys; z = zeros(float(sys.argv[1])); print(len(z), z[:7])
