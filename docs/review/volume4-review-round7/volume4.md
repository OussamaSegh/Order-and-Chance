# Volume 4 — Chance, round 7

**Score: 10/10.**

**Counts.** 0 critical, 0 major, 0 minor.

**Regressions.** 0. Every passage edited in rounds 1–6 was re-read and holds, including the new sentence that subadditivity bounds the union of the covering cubes by the sum of their Gaussian masses.

**How this was read.** The chapters in `volume4-chance/main.tex`, on main at `50825dc5`, including exercises, hints, solutions, and the extremal appendix. The edited passages were checked against the repairs. No full LaTeX build was run.

## Issues

None.

## Changed passages that hold

- `ch01-counting.tex` secretary: the derivative of \(g\) changes sign at \(1/e\), and \(|y-r/n|\le 2/(n-1)\).
- `ch02-discrete.tex` geometric second moment: \((1-r)S_N\to r/(1-r)\), then divide by \(p\).
- `ch05-continuous.tex` Gaussian boundary, weak opening run, coordinate-by-coordinate simplex map, and the stick equality of probability \(0\). The probability stays \(n/2^{n-1}\).
- `ch06-clt.tex` fourth-moment signs, finite-bit gap, monotone density comparison, one-swap pointer, classical cutoff directions, both Gaussian tails, four allowances of \(\varepsilon/4\), and the split of \(\min(Q^2,M)\) into two monotone clips.
- `ch07-walks.tex` gaps \(e_k-e_{k+1}=2k+1\), and \(h(y)>0\) on a shortest path.
- `ch09-poisson.tex` block bound and the tail sum for \(\mathbb E[\tau]\).
- `ch11-brownian.tex` stopped position on \([0,R]\), level \(N\) fixed before \(A\), and the cube cover of the hitting shell. Subadditivity bounds the union of those cubes by the sum of their Gaussian masses.
- `ch12-method.tex` a face of degree \(0\) has empty boundary, so there is no edge.
- `extremal.tex` \(W(k,2)>x\) because \(W\ge N+1\) and \(N=\lfloor x\rfloor\).

## Not checked

- A LaTeX build.
