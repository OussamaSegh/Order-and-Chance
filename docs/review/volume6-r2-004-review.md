# V6-R2-004 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `7165866949265c4b04ed9eb59a2ef044a6293cf6`.

## What was checked

The issue is real. \(P(x)=\prod_{p\le x}(1-1/p)\) was computed as an exact rational, and the ratio is \(P(x)\log x\cdot e^{\gamma}\).

For the primes up to \(1000\), \(P(1000)=0.0809652635068\ldots\), so the unchanged prefix \(0.08096526\ldots\) and the rounding \(P(1000)=0.0810\) are right. With the full value \(e^{-\gamma}=0.561459483566885\ldots\),
\[
\frac{P(1000)}{e^{-\gamma}/\log 1000}=0.99613283375\ldots.
\]
The same ratio with the solution’s given truncation \(e^{-\gamma}=0.56145948\) is \(0.99613284008\ldots\). Either value begins \(0.996132\), and the fifth decimal digit is \(3\), so four decimal places remain \(0.9961\). The old prefix \(0.996133\ldots\) does not match either value.

The same arithmetic reproduces the neighbouring lines that this solution already prints: \(P(30)=442368/2800733=0.15794722\ldots\), the ratio \(0.95680935\ldots\) against the given \(e^{-\gamma}=0.56145948\), \(P(100)=0.12031729\ldots\), and the ratio \(0.986859\ldots\). Those lines were not edited.

The diff against `main` at `24ef1a84c134be92500e6704775cdc074298ae3f` is the one prefix in `volume6-crossroads/chapters/ch01-mertens.tex`. No numbered environment, label, or counter is added or removed. Mertens’s theorem is not used in the arithmetic.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled. No GitHub Actions log was read. The proof of Theorem `thm:mertens3` was not re-read for this note.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The prefix stands. This note is the only addition. |
