# Volume 5 — Calculation, round 3

**Score: 10/10.**

**Counts.** 0 critical, 0 major, 0 minor.

**Round-2 follow-up.** 4 resolved, 0 regressed.

**Regressions.** 0. The passages changed by #302, #303, #304, and #312 hold.

**How this was read.** The chapters in `volume5-calculation/main.tex`, on main at `1ccf4e18`, including the included Borwein file, exercises, hints, and solutions. The repaired lines were opened. No full LaTeX build was run.

## Issues

None.

## Repairs that hold

- Gibbs: the inner sum with the factor \(\pi/N\) tends to \(\operatorname{Si}(\pi)\), and the partial sum tends to \(\frac2\pi\operatorname{Si}(\pi)\).
- Lévy: the error integral is \(\int_0^1(-\log t)\,\mathrm dt=1\). The main term is the integral in (b), divided by \(\log 2\).
- Span 2: \(Q'(1)=-\mu\), \(Q'(-1)=\mu\), and \(s(1)=s(-1)=\mu/2\). The two simple roots each contribute \(1/\mu\), so \(u_{2n}\to 2/\mu\). Odd indices are exactly \(0\).
- Connected graphs: \(\log(\exp(\hat C))=\hat C\) is the second identity of Proposition `prop:explog`.
- FFT length \(2n-1\), and the wrapped index \(k-l+n\ge n-d>e\).
- Binary blocks sorted by exponent, with small-block weight \(<2^{-h}\).
- Domination: continuity uses \(g\); the derivative uses \(h\). Both Wallis factors sit inside the product.
- Mellin substitution includes \(\mathrm dt=\mathrm du/(\pi n^2)\). Absolute convergence of \(\sum\sigma(n)n^{-s}\) on \(\operatorname{Re}s>2\) is \(\zeta(s)\zeta(s-1)\).
- Partition bound: \(\frac{m+1}2\le m\) for \(m\ge 1\).
- Motzkin: the minus branch has vanishing constant term and vanishing linear term.

## Not checked

- A LaTeX build.
