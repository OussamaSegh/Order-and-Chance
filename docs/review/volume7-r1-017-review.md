# V7-R1-017 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `5c37d4a16156a5f2dd2362dd6596654705527764`.

## What was checked

The issue is real. If the finite subcover never uses the index \(i\), then \(W_i=\varnothing\). The distance from the empty set is not a positive real, and the Urysohn quotient is then undefined.

The shorthand \(g\prec V\) means that \(g\) is continuous, takes values in \([0,1]\), and has support inside \(V\). The zero function meets that, and the empty support sits inside \(V_i\). The fix sets \(g_i=0\) in the empty case and uses the distance formula only when \(W_i\) is nonempty and \(V_i\ne K\). Then \(\overline{W_i}\) is a nonempty compact subset of \(V_i\), and \(K\setminus V_i\) is a nonempty closed set, so the two distances in the denominator are distances to nonempty sets and the denominator is positive. If \(V_i=K\) and \(W_i\) is nonempty, the proof still takes \(g_i=1\).

The chosen balls cover \(C\), so \(C\) sits in the union of the nonempty closures \(\overline{W_i}\). At each point of \(C\) some \(g_i\) equals \(1\). The telescoping sum is therefore \(1\) on \(C\), and an unused index contributes the zero summand. The label `lem:pou` is unchanged.

The diff is `volume7-spaces/chapters/ch11-metricmeasures.tex` only. No caption or diagram command changed. It does not meet V7-R1-018. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The Riesz theorem that calls this lemma was not re-derived. Proposition `prop:urysohn` was not re-proved.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
