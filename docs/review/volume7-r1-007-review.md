# V7-R1-007 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `6277012d107bca4844d58bcffa854286e1a9b8c5`.

## What was checked

The issue is real. Here \(k=\frac15\) and \(d(2,T(2))=|20|_5=\frac15\), so the a priori bound is
\[
\frac{k^n}{1-k}\,d(2,T(2))=\frac54\cdot 5^{-n-1},
\]
which is larger than \(5^{-n-1}\).

The solution already shows that \(T\) is a \(\frac15\)-contraction of \(D=\{x:|x-2|_5\le\frac15\}\) into itself, and that a fixed point lies in \(D\). So \(|2-x|_5\le\frac15\), and \(|T(y)-x|_5\le\frac15|y-x|_5\) for \(y\in D\). The iterates of \(2\) stay in \(D\), and
\[
|T^n(2)-x|_5\le 5^{-n}|2-x|_5\le 5^{-n-1}.
\]
That is the congruence modulo \(5^{n+1}\). The sentence now names this contraction.

The digit arithmetic was recomputed: \(T(2)=2-20=-18\equiv 7\pmod{25}\), \(T(7)=7-200=-193\equiv 57\pmod{125}\), and \(57^2+1=3250=26\cdot 125\). Those checks stay after the bound. The diff is one sentence in `volume7-spaces/chapters/ch02-metric.tex`. No label, caption, or diagram command changed. It does not meet the other edits in this file. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. Further \(5\)-adic digits, past \(2,1,2\), were not computed. The construction of \(\Z_5\) was not re-read.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
