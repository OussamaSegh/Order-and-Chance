# V7-R1-003 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `7ef6228b02e45ff1ad86001aad7a06b610f50238`.

## What was checked

The issue is real. Exercise `ex:notR2` shows that \([0,1]\) is not homeomorphic to \([0,1]^2\), by deleting one point: the segment falls into two pieces, and the square remains path-connected. A continuous bijection is a homeomorphism only after the compact-to-Hausdorff fact.

The solution of `ex:square` builds a bijection between \([0,1]^2\) and \([0,1]\). The new sentences separate the two claims. The exercise is cited for "not a homeomorphism". Proposition `prop:compactbasic`(d) says that a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism. The segment \([0,1]\) is compact by the Heine--Borel theorem in the same chapter. The square is Hausdorff because a metric space is Hausdorff and a subspace of a Hausdorff space is Hausdorff, both recorded in Chapter 3. A continuous bijection from the segment onto the square would therefore be a homeomorphism, which the exercise rules out.

The diff is one sentence in `volume7-spaces/chapters/ch01-sets.tex`. No label, caption, or diagram command changed. It does not meet the lines of V7-R1-002 or V7-R1-004. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The path-connectedness write-up inside `ex:notR2` was read and not re-derived past the straight-line detour it already gives. The space-filling surjection, deferred to Chapter 4, was not opened.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
