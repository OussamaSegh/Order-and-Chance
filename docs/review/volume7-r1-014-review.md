# V7-R1-014 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `368ac06253ce45d58255e02131e6934228f65111`.

## What was checked

The issue is real. Theorem `thm:riemanncont` says that a continuous function on a segment is Riemann integrable, and that the integral is linear, monotone, additive over adjacent intervals, and normalised on constants. It does not mention Lebesgue measure.

Theorem `thm:lebesguecriterion` says that a bounded function is Riemann integrable if and only if its discontinuities form a null set, and that the Riemann integral then equals the Lebesgue integral. The integrand \(x/(2-x)\) is continuous on \([0,1]\), since \(2-x\in[1,2]\). The criterion applies.

The derivative of \(-2\ln(2-x)-x\) is \(2/(2-x)-1=x/(2-x)\). The evaluation is
\[
(-2\ln 1-1)-(-2\ln 2)=2\ln 2-1.
\]
The paragraph after `thm:riemanncont` says that the fundamental theorem was derived in Volume 1 from those four rules. The new sentence cites the criterion for the identification and `thm:riemanncont` for that evaluation. The numerical value stays a separate computation from the citation.

The diff is one sentence in `volume7-spaces/chapters/ch07-integral.tex`. No label, caption, or diagram command changed. It does not meet the other edits in this file. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The derivation of the fundamental theorem in Volume 1 was not re-read. The series \(\sum 1/(2^n(n+1))\) was not summed by hand beyond the integral identity already in the solution.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
