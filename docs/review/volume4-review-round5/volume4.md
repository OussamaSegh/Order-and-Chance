# Volume 4 — Chance, round 5

**Score: 7/10.**

**Counts.** 0 critical, 1 major, 1 minor. `V4-R5-001`, `V4-R5-002`.

**Regressions.** 2. Both sit in sentences added by the repairs. No earlier repair was found to have broken a neighbouring argument that was already correct.

**How this was read.** Every passage changed between `88bf6c02` and `1b17516d` in `volume4-chance/`, opened at the new lines. No full LaTeX build was run.

## Issues

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V4-R5-001 | `chapters/ch11-brownian.tex:347` | major | “Integrate the deterministic bound for the levels \(a-\omega_n-x\) and \(a-x\). … In every piece the content tends to \(0\).” | The reflection bound prices each tail \(\{M^U\ge\ell\}\). The shell is the difference of two tails. A bound on the difference of two outer contents does not price the shell; the same chapter says that subtracting half-line contents does not price a strip. Cover the shell by the cubes of Theorem `thm:levy`. Their Gaussian mass is the integral of the walk density over a slightly wider shell, and that integral is what the reflection bound makes small. |
| V4-R5-002 | `chapters/ch06-clt.tex:781` | minor | “The clips are bounded and monotone, so Proposition `prop:indepproduct` gives \(\mathbb E[W_i^{(M)}W_j^{(M)}]=(\mathbb E[W_1^{(M)}])^2\).” | \(\min(Q^2,M)\) is not monotone. The same solution says so a few lines later. One of \(Q_+\) and \(Q_-\) is zero at each point, so the clipped square is the sum of two monotone clips. The product of two copies expands into four products of those clips. |

## Changed passages that hold

- `ch01-counting.tex` secretary: the derivative of \(g\) changes sign at \(1/e\), and \(|y-r/n|\le 2/(n-1)\).
- `ch02-discrete.tex` geometric second moment: \((1-r)S_N\to r/(1-r)\), then divide by \(p\).
- `ch05-continuous.tex` Gaussian boundary, weak opening run, coordinate-by-coordinate simplex map, and the stick equality of probability \(0\).
- `ch06-clt.tex` fourth-moment signs, finite-bit gap in the strong law, monotone comparison for the density, the one-swap pointer, the classical cutoff directions, the two Gaussian tails, and the four allowances of \(\varepsilon/4\).
- `ch07-walks.tex` gaps \(e_k-e_{k+1}=2k+1\), and \(h(y)>0\) on a shortest path.
- `ch09-poisson.tex` block bound and the tail sum for \(\mathbb E[\tau]\).
- `ch11-brownian.tex` stopped position on \([0,R]\), with level \(N\) fixed before \(A\). The two-sided tail does not grow with \(n\).
- `ch12-method.tex` a face of degree \(0\) has empty boundary, so there is no edge.
- `extremal.tex` \(W(k,2)>x\) because \(W\ge N+1\) and \(N=\lfloor x\rfloor\).

## Not checked

- A LaTeX build.
- Chapters that #291–#301 did not edit.
