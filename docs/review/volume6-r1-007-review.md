# V6-R1-007 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `bc259a0714c97849c2954ca15623574e8f5c786b`.

## What was checked

The issue is real. The argument principle is displayed as
\[
N(T)=\frac1{2\pi i}\int_{\partial D}\frac{\xi'}{\xi},
\]
and the next sentence said the integral is real. From the display the integral equals \(2\pi i\,N(T)\). The count \(N(T)\) is a number of zeros, so it is real, the integral is purely imaginary, and its imaginary part is \(2\pi N(T)\). The new sentence says that. The identity \(2\pi N(T)=\operatorname{Im}\int_{\partial D}\xi'/\xi\) was already the right one. The reason was wrong.

The next sentences are unchanged. The bottom side contributes nothing to the imaginary part, the two halves agree, and each contributes \(\pi N(T)\). That is the identity the theorem uses. The splitting was not weakened, and no term was dropped.

The diff against `main` is one sentence in `volume6-crossroads/chapters/ch06-zeros.tex`. No other path. No numbered environment, label, or counter is added or removed. No caption and no diagram command is edited.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled. GitHub Actions was not inspected. The bound on \(S(T)\) later in the same proof was not re-worked.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
