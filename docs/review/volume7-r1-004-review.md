# V7-R1-004 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `590a12562b12d24ceeac4951daf9e0febe66d5e4`.

## What was checked

The issue is real. A \(d\)-dimensional vector space over \(\Q\) is in bijection with \(\Q^d\), by coordinates in a basis. It is not a finite union of copies of \(\Q^d\).

The new sentence says that. Countable means an injection into \(\N\). Proposition `prop:countable` gives that for \(\Q\). If \(A\) and \(B\) inject into \(\N\), then \(A\times B\) injects into \(\N\times\N\). The pairing \((m,n)\mapsto 2^m 3^n\), already proved injective in that proposition, then injects \(\N\times\N\) into \(\N\). Iterating gives an injection of \(\Q^d\) into \(\N\). A finite Hamel basis would make \(\R\) countable. The rest of the additive-function argument is unchanged.

The citation is to the statement of `prop:countable`. The gap inside that proposition's own proof is V7-R1-002, on a different line. The two diffs do not overlap, and the nineteen branches merge onto `main` with no conflict. The diff is one sentence in `volume7-spaces/chapters/ch01-sets.tex`. No label, caption, or diagram command changed.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The existence of a Hamel basis, which this solution takes from `thm:basis`, was not re-proved.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
