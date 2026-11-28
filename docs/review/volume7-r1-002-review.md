# V7-R1-002 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `dd95fb34a09aa797f158621c37f7bbdcf2e1cb9e`.

## What was checked

The issue is real. Countable is defined as an injection into \(\N\). The pairing \((m,n)\mapsto 2^m 3^n\) is proved injective in the same proof, so \(\N\times\N\) injects into \(\N\). The old sentence injected \(\Q\) into \(\Z\times\Z\) and then called that a subset of a countable set. \(\Z\times\Z\) had not been shown countable.

The integers still inject into \(\N\times\N\) by \(n\mapsto(n,0)\) for \(n\ge 0\) and \(-n\mapsto(0,n)\) for \(n>0\). Those images are disjoint. Composing with the pairing injects \(\Z\) into \(\N\). Lowest terms with positive denominator inject \(\Q\) into \(\Z\times\Z\). Applying an injection \(\Z\to\N\) on each coordinate injects that product into \(\N\times\N\), and the pairing injects \(\N\times\N\) into \(\N\). The composite injects \(\Q\) into \(\N\), which is the definition of countable.

The diff is one sentence in `volume7-spaces/chapters/ch01-sets.tex`. No label, caption, or diagram command changed. The other edits in this file, V7-R1-003 and V7-R1-004, are elsewhere. The nineteen branches merge together onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. Existence of greatest common divisors, used by the phrase "lowest terms", was not re-proved. That phrase was already in the sentence.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
