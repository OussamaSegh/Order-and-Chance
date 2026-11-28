# V7-R1-005 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `faa907594ed4ad48e1a0debe8023f2cb639971ef`.

## What was checked

The issue is real. The second bound refers to \(x_{n-1}\). At \(n=0\) that term is not defined.

The first bound is now marked for \(n\ge 0\), and the second for \(n\ge 1\). Restarting the first bound at \(x_{n-1}\) and taking one step gives
\[
d(x_n,x^*)\le\frac{k}{1-k}\,d(x_{n-1},x_n)
\]
for \(n\ge 1\). That is the second inequality. The label `thm:banach` is unchanged.

A search of `volume7-spaces/` finds the second bound only in this theorem. The Dottie example speaks of the a posteriori bound as a stopping test after iterates have been computed, so the index there is at least \(1\). No application at \(n=0\) was found.

The diff is `volume7-spaces/chapters/ch02-metric.tex` only. No caption or diagram command changed. The other two edits in this file, V7-R1-006 and V7-R1-007, are on other lines. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The contraction proof of existence and uniqueness was read and not re-derived past the displayed estimate.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
