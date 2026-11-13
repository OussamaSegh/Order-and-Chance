"""Shared helpers for the Volume 14 number checks."""
import sys

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

def primes_upto(n):
    """All primes <= n, as a numpy array (simple sieve; fine up to a few 10^8)."""
    import numpy as np
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]: s[p * p::p] = False
    return np.nonzero(s)[0]

def record_gaps(limit, seg=10**7):
    """Maximal prime gaps (start prime, gap) for primes below `limit`, by a segmented sieve."""
    import numpy as np
    small = primes_upto(int(limit ** 0.5) + 1)
    recs, last, best = [], None, 0
    for lo in range(0, limit, seg):
        hi = min(lo + seg, limit)
        s = np.ones(hi - lo, dtype=bool)
        if lo == 0: s[:2] = False
        for p in small:
            if p * p >= hi: break
            st = max(p * p, ((lo + p - 1) // p) * p)
            s[st - lo::p] = False
        ps = np.nonzero(s)[0] + lo
        if len(ps) == 0: continue
        if last is not None:
            ps = np.concatenate(([last], ps))
        g = np.diff(ps)
        for i in np.nonzero(g > best)[0]:
            if g[i] > best:
                best = int(g[i]); recs.append((int(ps[i]), best))
        last = int(ps[-1])
    return recs
