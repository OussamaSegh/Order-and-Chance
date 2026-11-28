# V6-R1-006 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `69509de69e9dabd20543172ac7109c4255eaf410`.

## What was checked

The issue is real. After the zeros inside \(|z|<R\) are removed, the proof said \(g\) has no zeros on the closed disc, "hence none on a slightly smaller open disc \(D'\supset\{|z|\le R\}\)". A disc that contains the closed disc is larger, and the step from a compact zero-free set to a neighbourhood uses isolation.

The statement being proved assumes \(f\) is holomorphic on an open set containing \(|z|\le R\), with \(f(0)\ne 0\) and with no zero on the circle. The Blaschke factors remove the zeros in \(|z|<R\), so \(g\) is holomorphic on some open disc \(D\) strictly larger than the closed disc, \(g(0)\ne 0\), and \(g\) has no zero on \(|z|\le R\). The zeros of \(g\) are isolated, so they stay a positive distance from that compact disc. The new sentence takes a slightly larger open disc \(D'\) with \(\{|z|\le R\}\subset D'\subset D\). That disc is zero-free and convex. The logarithm on \(D'\), the citation of Volume 5, Theorem 9.9, and the mean-value step are unchanged. Jensen's displayed formula is unchanged.

The diff against `main` is one sentence in `volume6-crossroads/chapters/ch06-zeros.tex`. No other path. No numbered environment, label, or counter is added or removed. No caption and no diagram command is edited.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled. GitHub Actions was not inspected. Volume 5, Theorem 9.9 was not re-proved.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
