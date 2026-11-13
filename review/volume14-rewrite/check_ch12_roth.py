#!/usr/bin/env python3
"""Volume 14, Chapter 12 (Roth): r_3(N) for N <= 70, Behrend figure, constants of the proof."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish

# r_3(N): largest 3-AP-free subset of {1..N}, by the usual recursion
r = [0, 1]
sys.setrecursionlimit(10000)
def exists(N, k):
    """Is there a 3-AP-free subset of [1,N] of size k containing 1 and N?"""
    chosen = [1]
    bad = set()           # numbers that would complete a 3-AP
    def dfs(i, cnt, bad):
        if cnt == k - 1:
            return N not in bad and all(2 * a - N not in chosen for a in chosen) and ((1 + N) % 2 or (1 + N) // 2 not in chosen)
        if i >= N: return False
        # bound: elements still possible in [i, N-1] plus N
        if cnt + r[N - i] + 1 < k: return False
        if i not in bad:
            nb = set(bad)
            for a in chosen:
                nb.add(2 * i - a)
            chosen.append(i)
            if dfs(i + 1, cnt + 1, nb): return True
            chosen.pop()
        return dfs(i + 1, cnt, bad)
    return dfs(2, 1, bad)
for N in range(2, 71):
    k = r[-1] + 1
    r.append(k if exists(N, k) else k - 1)
check("r_3(70)", r[70], 20, 0)
# greedy set (ternary digits 0,1) shifted to start at 1
G = [n + 1 for n in range(70) if '2' not in __import__('numpy').base_repr(n, 3)]
check_true("greedy set 3-AP free", all(2 * b - a not in set(G) for a in G for b in G if b > a))
check_true("greedy optimal for N <= 4", all(len([g for g in G if g <= N]) == r[N] for N in range(1, 5)))
check_true("greedy falls behind at 70", len([g for g in G if g <= 70]) < r[70])
# Behrend, n=2, d=20
from collections import Counter
C = Counter(x * x + y * y for x in range(20) for y in range(20))
m = max(C.values())
best = [s for s, c in C.items() if c == m]
check_true(f"most populated circle is 325 only ({best})", best == [325])
check("points on it", m, 6, 0)
imgs = sorted(x + 40 * y for x in range(20) for y in range(20) if x * x + y * y == 325)
check_true(f"images {imgs}", imgs == [58, 257, 415, 610, 686, 721])
S = set(imgs)
check_true("no 3-AP in images", all(2 * b - a not in S for a in imgs for b in imgs if b > a))
# proof constants
check_true("log(1792*7225) < 17", math.log(1792 * 7225) < 17 and 1792 * 7225 < 1.3e7)
check_true("226 log 2 / 500 < 0.32", 226 * math.log(2) / 500 < 0.32)
check_true("log2(y)+1 <= 2y for y >= 1 (sampled)", all(math.log2(y) + 1 <= 2 * y for y in [1 + i / 10 for i in range(1000)]))
check("log2/log3", math.log(2) / math.log(3), 0.63, 0.005)
finish()
