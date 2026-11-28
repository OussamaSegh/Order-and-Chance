# V6-R1-005 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `4e5e9f9b39eeb2512d2dbeaab38981d85fed4f61`.

## What was checked

The issue is real. The solution of `ex:xi2` said that at the trivial zeros the pole of \(\Gamma(s/2)\) cancels a zero of the polynomial factor. This chapter defines
\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\Bigl(\frac s2\Bigr)\zeta(s).
\]
The factor \(\frac12 s(s-1)\) is zero only at \(0\) and \(1\). At \(s=-2k\) for an integer \(k\ge 1\) it equals \(k(2k+1)\ne 0\). Those points are poles of \(\Gamma(s/2)\) and zeros of \(\zeta\).

The new sentence names \(\zeta\) as the function whose zero is cancelled, and it says the polynomial factor does not vanish there, so \(\xi\) stays non-zero. That is the repair the issue asked for. The value \(\xi(2)=\pi/6\) is unchanged and is right: \(\Gamma(1)\zeta(2)/\pi=\pi/6\). The identity \(\xi(-1)=\xi(2)\) is unchanged.

The diff against `main` is one sentence in `volume6-crossroads/chapters/ch06-zeros.tex`. No other path. No numbered environment, label, or counter is added or removed. No caption and no diagram command is edited. The evaluation \(\xi(2)=\pi/6\) stays a separate calculation from the cancellation sentence.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled. GitHub Actions was not inspected. The product formula for \(\Gamma\) was not re-derived. The poles used above are the poles at the non-positive integers.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
