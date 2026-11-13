#!/usr/bin/env python3
"""Volume 14, Chapter 1 (zeros and short intervals): printed numbers."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from common import check, check_true, finish, record_gaps
recs = record_gaps(10**9)
check("last record start below 1e9", recs[-1][0], 436273009, 0)
check("last record gap", recs[-1][1], 282, 0)
check("next prime after 436273009", recs[-1][0] + recs[-1][1], 436273291, 0)
check("first record", recs[0][1], 1, 0)
check_true("p=3 has gap 2", (3, 2) in recs)
check("(log p)^2 at the last record", math.log(436273009) ** 2, 396, 0.5)
check_true("(log p)^2 > gap for every record from p=23", all(math.log(p) ** 2 > g for p, g in recs if p >= 23))
check_true("(log p)^2 < gap at p=7 (gap 4)", math.log(7) ** 2 < 4)
print(len(recs), "records:", recs)
# Exercise carlsonnum / text: 4 sigma (1-sigma) at sigma = 0.9
check("4*0.9*0.1", 4 * 0.9 * 0.1, 0.36, 1e-12)
check("Ingham theta from c=1/6", (1 + 4 / 6) / (2 + 4 / 6), 5 / 8, 1e-12)
check("Huxley theta", 1 - 5 / 12, 7 / 12, 1e-12)
check("Guth-Maynard theta", 1 - 13 / 30, 17 / 30, 1e-12)
finish()
