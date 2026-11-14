#!/usr/bin/env python3
"""Run the race pi(x;4,3) - pi(x;4,1) up to 10^9 with a segmented sieve; print the final counts, the last x up to which
4n+3 is ahead or tied, and the share of log-scale on which 4n+1 leads (x from 2 to 10^9)."""
import numpy as np, math, sys
LIM = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10 ** 9
base = np.ones(int(LIM ** .5) + 2, bool); base[:2] = False
for p in range(2, int(len(base) ** .5) + 1):
    if base[p]: base[p * p::p] = False
bp = np.nonzero(base)[0]
seg = 10 ** 7; diff = 0; c1 = c3 = 0; lead_log = 0.0; first_lead = None; prev = 2.0
for lo in range(0, LIM + 1, seg):
    hi = min(lo + seg, LIM + 1)
    s = np.ones(hi - lo, bool)
    if lo == 0: s[:2] = False
    for p in bp:
        if p * p >= hi: break
        st = max(p * p, ((lo + p - 1) // p) * p); s[st - lo::p] = False
    ps = np.nonzero(s)[0] + lo
    ps = ps[ps > 2]
    steps = np.where(ps % 4 == 3, 1, -1)
    cum = diff + np.cumsum(steps)          # pi(x;4,3)-pi(x;4,1) just after each prime
    # on [p_i, p_{i+1}) the difference is cum[i]; class 1 leads where < 0
    nxt = np.append(ps[1:], hi).astype(float)
    neg = cum < 0
    if neg.any():
        if first_lead is None: first_lead = int(ps[neg][0])
        lead_log += float(np.sum(np.log(nxt[neg] / ps[neg])))
    diff = int(cum[-1]) if len(cum) else diff
    c3 += int(np.sum(steps == 1)); c1 += int(np.sum(steps == -1))
print("c1", c1, "c3", c3, "first lead", first_lead, "lead share of log scale", lead_log / math.log(LIM / 2))
