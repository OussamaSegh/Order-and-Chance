# V7-R1-011 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `44851861cc89e3e81ca65b214181072cb4f924dc`.

## What was checked

The issue is real. A Riemann sum lies between \(L(f,P)\) and \(U(f,P)\), and so does the integral, so the two differ by at most \(U-L\). Darboux integrability gives some partition with a small gap. It does not, by itself, give the gap for every partition of small mesh.

The added estimate was checked. Let \(|f|\le M\), and let \(P_0\) satisfy \(U(f,P_0)-L(f,P_0)<\varepsilon/2\), with \(m\) division points strictly between the endpoints. If \(m=0\), every partition refines \(P_0\), and refinement raises \(L\) and lowers \(U\). If \(M=0\), then \(f=0\). In both cases the gap of every partition is \(<\varepsilon/2\).

Otherwise take the mesh of \(P\) smaller than \(\varepsilon/(4mM)\). At most \(m\) subintervals of \(P\) contain one of those division points in their interior. Each has length less than the mesh and oscillation at most \(2M\), so each contributes less than \(\varepsilon/(2m)\) to the gap, and together they contribute less than \(\varepsilon/2\). Every other subinterval of \(P\) lies inside a subinterval of \(P_0\), and those contributions add to at most \(U(f,P_0)-L(f,P_0)<\varepsilon/2\). Thus \(U-L<\varepsilon\), and every Riemann sum is within \(\varepsilon\) of the integral.

The estimate is a proof, and it contains no numerical check. The diff is one paragraph in `volume7-spaces/chapters/ch07-integral.tex`. No label, caption, or diagram command changed. The later edits V7-R1-012, V7-R1-013, and V7-R1-014 are on other lines. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The estimate was not run on a sample function. The figure named in the previous paragraph was not inspected.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
