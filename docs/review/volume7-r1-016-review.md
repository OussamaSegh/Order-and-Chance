# V7-R1-016 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `f8c2c660c917e41b96e843502002045ba9eb7973`.

## What was checked

The issue is real. For one fixed \(\varepsilon>0\), summability and the Borel--Cantelli lemma give only
\[
\limsup_{n\to\infty}\Bigl|\frac1n\sum_{k\le n}B_k-p\Bigr|\le\varepsilon
\]
almost surely. The null set depends on \(\varepsilon\).

The fourth-moment bound used in the display was checked as an inequality: \(n+3n(n-1)=3n^2-2n\le 3n^2\). Markov's inequality then gives the probability at most \(3/(\varepsilon^4 n^2)\). Proposition `prop:measureprops`(e) is the first Borel--Cantelli lemma: a summable sequence of measures meets almost every point only finitely often. Eventually the average is strictly inside \(\varepsilon\), so the limsup is at most \(\varepsilon\).

Intersecting the null sets for \(\varepsilon=1/m\) is a countable intersection. Off that null set the limsup is at most \(1/m\) for every \(m\), hence is \(0\), and the averages converge to \(p\). The proof of Theorem `thm:borelnormal` uses the same intersection over \(m\). The moment count stays separate from this quantifier repair.

The diff is `volume7-spaces/chapters/ch10-radon.tex` only. No label, caption, or diagram command changed. This file is not edited by another fix branch. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The fourth-moment expansion was not rewritten term by term. The two-variable identity \(\mathbb E[(Y+Z)^4]=\mathbb E[Y^4]+\mathbb E[Z^4]+6\mathbb E[Y^2]\mathbb E[Z^2]\), for independent centred factors, was used as a check of the coefficient \(3n(n-1)\). The singularity argument after the strong law was not re-derived.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
