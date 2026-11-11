"""Shared helpers for the Volume 6 number checks."""
import math, sys
import numpy as np

GAMMA = 0.57721566490153286061

def primes_upto(n):
    """All primes <= n, as a numpy int64 array (simple sieve)."""
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)

_fail = []
def check(name, value, printed, tol):
    """Compare a computed value with the number printed in the book."""
    ok = abs(value - printed) <= tol
    print(f"{'ok  ' if ok else 'FAIL'} {name}: computed {value!r}, printed {printed!r}")
    if not ok: _fail.append(name)

def check_true(name, cond):
    print(f"{'ok  ' if cond else 'FAIL'} {name}")
    if not cond: _fail.append(name)

def finish():
    if _fail:
        print(f"\n{len(_fail)} check(s) failed: {_fail}"); sys.exit(1)
    print("\nall checks pass")
