"""Shared helpers for the Volume 10 number checks."""
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
