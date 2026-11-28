# V7-R1-006 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `ee5f9171d08a71eca4acb8840be180bfdb1ae34c`.

## What was checked

The issue is real. Exercise `ex:newton` is \(N(x)=\frac12(x+a/x)\). Its solution derives \(e_{n+1}=e_n^2/(2x_n)\) for square roots. That exercise does not treat \(x-(x-\cos x)/(1+\sin x)\).

The map in the example is Newton's method for \(f(x)=x-\cos x\). Then \(f'(x)=1+\sin x\). At the fixed point of cosine on \([0,1]\), \(f(x^*)=0\) and \(f'(x^*)=1+\sin x^*\ne 0\), since \(x^*\in(0,1)\) and \(\sin x^*>0\). Also \(f''(x^*)=\cos x^*=x^*\ne 0\). The root is simple, so the Newton derivative vanishes there. The new sentence says that, and it says the exercise is the square-root case of the doubling. It no longer cites the exercise as a proof of the cosine iteration.

The numerical bounds \(\sin 1\le 101/120<0.85\) and the Dottie digits are unchanged and sit in the example, apart from the contraction argument. Figure `fig:cobweb` is named and not edited. No caption or font command is in the diff. The diff is one sentence in `volume7-spaces/chapters/ch02-metric.tex`. It does not meet V7-R1-005 or V7-R1-007. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The general quadratic error formula for Newton's method was not re-derived. No cosine Newton iterates were computed. The series bound for \(\sin 1\) was not recomputed.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
