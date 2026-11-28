# Volume 5 — Calculation, round 2

**Score: 8/10.**

**Counts.** 0 critical, 0 major, 4 minor. `V5-R2-001` through `V5-R2-004`.

**Regressions.** 0. The ten passages repaired in #302, #303, and #304 hold.

**How this was read.** The chapters in `volume5-calculation/main.tex`, on main at `337b1230`, including the included Borwein file, exercises, hints, and solutions. The repaired lines were opened. No full LaTeX build was run.

## Issues

Paths are relative to `volume5-calculation/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V5-R2-001 | `chapters/ch06-fourier.tex:270` | minor | “The sum is a Riemann sum for \(\frac{\sin t}t\). … It tends to \(\frac2\pi\operatorname{Si}(\pi)\).” | The factor \(\pi/N\) makes the inner sum the Riemann sum, and that sum tends to \(\operatorname{Si}(\pi)\). The factor \(2/\pi\) stands outside it in the display. The partial sum is what tends to \(\frac2\pi\operatorname{Si}(\pi)\). |
| V5-R2-002 | `chapters/ch10-zeta.tex:546` | minor | “The integral is (b).” | The integral in the error display is \(\int_0^1(-\log t)\,\mathrm dt=1\). Part (b) is \(\int_0^1\frac{-\log t}{1+t}\,\mathrm dt=\frac{\pi^2}{12}\). The main term divides that value by \(\log 2\). |
| V5-R2-003 | `chapters/ch02-generating.tex:1519` | minor | “Then \(u_{2n}\to\frac2\mu\) instead.” | The limit is right for span 2. Both simple roots \(\pm 1\) contribute \(1/\mu\), and the two contributions add on even indices. That residue is not written. |
| V5-R2-004 | `chapters/ch02-generating.tex:988` | minor | “The third identity of Proposition `prop:explog` … gives \(\hat C=\log\sum\).” | The third identity is \(\exp(\log(1+F))=1+F\). From \(\exp(\hat C)\) equal to the all-graphs series, the second identity gives \(\log(\exp(\hat C))=\hat C\). |

## Changed passages that hold

- `ch07-fft.tex`: \(2n-1\) roots of unity, and the wrapped index \(k-l+n\ge n-d>e\).
- `ch12-agm.tex`: blocks sorted by exponent; small-block weight \(<2^{-h}\); classical central limit theorem with a \(\delta/\eta\) sandwich.
- `ch04-integrals.tex`: continuity uses \(g\) alone; the derivative uses \(h\); both Wallis factors sit inside the product.
- `ch06-fourier.tex`: the Gibbs height is a limit, and the first partial sum reaches \(4/\pi\).
- `ch10-zeta.tex`: the Mellin substitution includes \(\mathrm dt=\mathrm du/(\pi n^2)\); absolute convergence of \(\sum\sigma(n)n^{-s}\) on \(\operatorname{Re}s>2\) is \(\zeta(s)\zeta(s-1)\).
- `ch11-asymptotics.tex`: \(\frac{m+1}2\le m\) for \(m=\lfloor\sqrt n\rfloor\ge 1\).
- `ch02-generating.tex` Motzkin: the minus branch has vanishing constant term and vanishing linear term.

## Not checked

- A LaTeX build.
