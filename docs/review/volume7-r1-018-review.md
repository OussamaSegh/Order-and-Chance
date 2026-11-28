# V7-R1-018 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `b7de0f1adfad1d95ef59de9db9bb020f0821e0bb`.

## What was checked

The issue is real. Tightness, as defined in this chapter, says: for every \(\varepsilon>0\) there is one compact set that carries mass at least \(1-\varepsilon\) for every measure in the family. One pair \((M,\varepsilon)\) gives only \(\lim_{t\to-\infty}F(t)\le\varepsilon\) and \(\lim_{t\to+\infty}F(t)\ge 1-\varepsilon\).

The exercise asks for the limits \(0\) and \(1\) when the laws are tight. The new write-up fixes \(\varepsilon>0\) first. A compact subset of \(\R\) is bounded, so it sits in some \([-M,M]\), and \(\mu_n([-M,M])\ge 1-\varepsilon\). Distribution functions in this book are \(F(t)=\mu(]-\infty,t])\), so \(F_n(-M-1)\le\varepsilon\) and \(F_n(M)\ge 1-\varepsilon\).

Part (a) puts \(F_{n_k}(t)\to F(t)\) at continuity points, and \(0\le F\le 1\). For a continuity point \(t<-M-1\), monotonicity gives \(F_n(t)\le F_n(-M-1)\le\varepsilon\), hence \(F(t)\le\varepsilon\). For a continuity point \(t>M\), \(F(t)\ge 1-\varepsilon\). Continuity points of a monotone function are dense, so the limits at \(\pm\infty\) satisfy the same bounds. Since \(\varepsilon>0\) is arbitrary and \(0\le F\le 1\), the limits are \(0\) and \(1\).

The escape example \(F_n=\mathbf 1_{[n,\infty[}\) is unchanged. Along rationals the limit is identically \(0\), which is not a distribution function. That numerical pattern stays outside the quantifier repair.

The diff is `volume7-spaces/chapters/ch11-metricmeasures.tex` only. No label, caption, or diagram command changed. It does not meet V7-R1-017. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. Helly's diagonal extraction in part (a) was read and not re-run on a sample sequence. The figure of the laws \(\delta_n\) was not inspected.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
