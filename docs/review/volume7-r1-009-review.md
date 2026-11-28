# V7-R1-009 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `bdd7723bb6df60d0181dd986510ac2b966791fee`.

## What was checked

The issue is real. A constant map is a continuous image of \(S^1\), and its image is a one-point interval. Exercise `ex:notR2` asks for the failure of a homeomorphism between the circle and any interval.

The new sentence says "homeomorphic image". A homeomorphism is bijective, and \(S^1\) is not a single point, so the interval contains two points \(a<b\). The interval property puts every point between them into \(I\). Deleting one such point splits \(I\) into two nonempty relatively open pieces. The previous paragraph shows that the punctured circle is connected. A homeomorphism would carry that connected set onto the split interval. The rest of the solution was already written for homeomorphisms, and it was read through that last sentence.

The diff is one sentence in `volume7-spaces/chapters/ch03-topology.tex`. No label, caption, or diagram command changed. It does not meet V7-R1-008. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The identification of \(S^1\) with the image of \((\cos,\sin)\) was not re-derived from Theorem `thm:exp`.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
