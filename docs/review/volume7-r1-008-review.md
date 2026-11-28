# V7-R1-008 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `5c51d0995ea165da267f5a0484edbf44ec074a3a`.

## What was checked

The issue is real. On \((\pi/2,\pi/2+2\pi)\) the equation \(\sin\theta=1\) has no solution: the solutions are \(\pi/2+2\pi k\), and both endpoints of that interval are excluded. The values of sine at the two endpoints are \(1\), and the value at the midpoint is \(-1\).

The deleted sentence is not used again. The next sentences show that \(\sin([\pi/2,3\pi/2])\) is a connected image, hence an interval by Corollary `cor:ivt`, that the interval contains \(1\) and \(-1\), and that sine takes values in \([-1,1]\) only. The image is therefore \([-1,1]\). Periodicity repeats this on every \([2\pi n+\pi/2,2\pi n+3\pi/2]\). On \((0,\varepsilon)\) the quantity \(1/x\) meets infinitely many of those closed intervals, so \(\sin(1/x)\) attains every value in \([-1,1]\). That is the fact the closure argument uses.

The diff deletes one sentence in `volume7-spaces/chapters/ch03-topology.tex`. No label, caption, or diagram command changed. It does not meet V7-R1-009. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The values \(e^{i\pi/2}=i\) and \(e^{i\pi}=-1\) in Theorem `thm:exp` were not re-derived. The TikZ figure of the topologist's sine curve was not inspected.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
