# V7-R1-015 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `4fb7f248e59eb69309331f62538e7b4a37ab96b6`.

## What was checked

The issue is real. The essential supremum is
\[
\|f\|_\infty=\inf\{M\ge 0:|f|\le M\text{ almost everywhere}\},
\]
and the chapter records that \(\{|f|>\|f\|_\infty\}\) is null, while \(|f|\le\|f\|_\infty\) almost everywhere. A representative can still be unbounded on that null set. If every term equals one function that is unbounded on a null set and zero elsewhere, the differences vanish almost everywhere, the old null set \(N\) can be empty, and the pointwise values are unbounded.

The new \(N\) also contains \(\{|f_n|>\|f_n\|_\infty\}\) for every \(n\). That is a countable union of null sets. Off \(N\), \(|f_n|\le\|f_n\|_\infty\) and \(|f_m-f_n|\le\|f_m-f_n\|_\infty\). A Cauchy sequence in \(L^\infty\) has bounded norms, by the first sentence of the case, so the functions share one bound off \(N\). The uniform limit is bounded. Setting the representative to \(0\) on \(N\) keeps it bounded, measurable, and essentially bounded. For large \(n\), \(|f_n-f|\le\varepsilon\) off \(N\), so the essential-norm bound is unchanged.

The diff is `volume7-spaces/chapters/ch09-lp.tex` only. No label, caption, or diagram command changed. This file is not edited by another fix branch. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The finite-\(p\) half of the Riesz--Fischer proof was not re-derived.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
