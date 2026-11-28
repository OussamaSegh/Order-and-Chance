# V7-R1-013 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `7c58ea3eca897d8f032d655709c3db3526faa433`.

## What was checked

The issue is real. For \(f=\mathbf 1_{]0,\infty[}\), the restriction to \([1,2]\) is identically \(1\).

On \([0,1]\), \(f(0)=0\) and \(f=1\) on \((0,1]\), so the only discontinuity is at \(0\). The function is bounded, and a single point is null. Theorem `thm:lebesguecriterion` therefore makes \(f\) Riemann integrable on \([0,1]\). The distance \(g(x)=\operatorname{dist}(x,K)\) for \(x\in[0,1]\) and nonempty \(K\subseteq[0,1]\) takes values in \([0,1]\), so the composition only evaluates \(f\) on that segment. The rest of the argument, that \(f\circ g\) is discontinuous on a fat Cantor set of measure \(\frac12\), is unchanged.

The diff is one sentence in `volume7-spaces/chapters/ch07-integral.tex`. No label, caption, or diagram command changed. It does not meet the other edits in this file. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The construction of a fat Cantor set of measure \(\frac12\) in `ex:fatcantor` was not re-read.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
