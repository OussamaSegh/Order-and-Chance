# Volume 4 — Chance, round 3

**Score: 7/10.**

**Counts.** 0 critical, 1 major, 2 minor. `V4-R3-001` through `V4-R3-003`.

**Round-2 follow-up.** 6 resolved, 0 regressed.

**How this was read.** The chapters in `volume4-chance/main.tex`, on main at `b0ede124`. The three rows below were opened at the cited lines. No full LaTeX build was run.

## Issues

Paths are relative to `volume4-chance/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V4-R3-001 | `chapters/ch06-clt.tex:647` | major | “because \(\mathbb E[Z_a Z_b]=\mathbf 1_{a=b}\)”. The next sentence applies Proposition `prop:indepproduct` to \(\cos(u_j Z_j)\) and \(\sin(u_j Z_j)\). | Each coordinate is \(\Phi^{-1}\) of its own uniform, unbounded. The proposition factors bounded monotone functions, or one finite-bit function against one unbounded monotone factor. Clip both normals; the clips are odd, so the off-diagonal product has mean \(0\). The tail of \(Z^2\) is removed by Cauchy--Schwarz. Cosine and sine are bounded but not monotone: approximate them by finite-bit steps on a compact subinterval of \((0,1)\) and factor the steps by the cylinder table. |
| V4-R3-002 | `chapters/ch06-clt.tex:776` | minor | “gives \(\mathbb E[W_i W_j]=(\mathbb E[W_1])^2\)”. | \(W=Q^2\) is an unbounded sum of monotone squares. Clip each copy. The proposition then applies, and Cauchy--Schwarz removes the tail because \(\mathbb E[W^2]=\mathbb E[Y^4]<\infty\). |
| V4-R3-003 | `chapters/ch06-clt.tex:782` | minor | “that average differs from the step average by at most the average gap. The three pieces \(\varepsilon/3\) then add.” | The clip is centred at \(m_M\) and the step at \(\mathbb E[L]\), and \(\lvert m_M-\mathbb E[L]\rvert\le\mathbb E[\mathrm{gap}]\). Four allowances of \(\varepsilon/4\) are needed, and the step allowance is an absolute value. |

## Not checked

- A LaTeX build.
