"""Vectorised Riemann-Siegel Z(t) with the first correction term (error O(t^{-3/4}))."""
import numpy as np
def theta(t):
    return t / 2 * np.log(t / (2 * np.pi)) - t / 2 - np.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)
def Z(t, chunk=2000):
    t = np.asarray(t, dtype=float); out = np.empty_like(t)
    for s in range(0, len(t), chunk):
        tt = t[s:s + chunk]
        a = np.sqrt(tt / (2 * np.pi)); m = np.floor(a).astype(int); M = m.max()
        n = np.arange(1, M + 1)
        th = theta(tt)
        terms = np.cos(th[:, None] - tt[:, None] * np.log(n)[None, :]) / np.sqrt(n)[None, :]
        terms[n[None, :] > m[:, None]] = 0
        main = 2 * terms.sum(axis=1)
        p = a - m
        C0 = np.cos(2 * np.pi * (p * p - p - 1 / 16)) / np.cos(2 * np.pi * p)
        out[s:s + chunk] = main + (-1) ** (m - 1) * (2 * np.pi / tt) ** 0.25 * C0
    return out
