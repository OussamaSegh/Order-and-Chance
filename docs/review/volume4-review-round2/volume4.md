# Volume 4 — Chance, round 2

**Score: 8/10.**

**Counts.** 0 critical, 0 major, 6 minor. `V4-R2-001` through `V4-R2-006`.

**Round-1 follow-up.** 2 critical, 1 major, and 14 minor resolved. 0 regressed.

**How this was read.** Every chapter in `volume4-chance/main.tex`, on main at `fcedde66`, including exercises, hints, solutions, and captions. Each new row was opened at the cited line. No full LaTeX build was run.

## Issues

Paths are relative to `volume4-chance/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V4-R2-001 | `chapters/ch06-clt.tex:141` | minor | “each of those products contains the factor \(\mathbb E[Y]=0\)”. | After the split \(Y=Y_+-Y_-\), one piece need not have mean \(0\). Grouping the signs for the index that appears once recovers the factor \(\mathbb E[Y_j]=0\). |
| V4-R2-002 | `chapters/ch06-clt.tex:425` | minor | “The linear terms have mean zero and the quadratic terms match, because the two summands share a mean and a variance and are independent of \(W_k\).” | Proposition `prop:indepproduct` factors a bounded monotone function, or a finite-bit function, against a monotone factor. \(f'(W_k)\) need not be monotone. The proof of Theorem `thm:lindeberg` replaces \(f'\) and \(f''\) by clips and finite-bit steps before multiplying. The example should name that step. |
| V4-R2-003 | `chapters/ch06-clt.tex:539` | minor | “Their normal expectations lie between \(\Phi(x-\delta)\) and \(\Phi(x+\delta)\) in the required directions.” | \(f_-\) equals \(1\) on \((-\infty,x-\delta]\), so \(\mathbb E[f_-(Z)]\ge\Phi(x-\delta)\). \(f_+\) equals \(0\) on \([x+\delta,\infty)\), so \(\mathbb E[f_+(Z)]\le\Phi(x+\delta)\). Monotone expectation gives \(\mathbb E[f_-(S_n)]\le F_n(x)\le\mathbb E[f_+(S_n)]\). |
| V4-R2-004 | `chapters/ch07-walks.tex:529` | minor | “\(I>0\), which it is because \(h\) is not identically zero on a connected graph”. | On a shortest \(a\)–\(b\) path, the neighbour \(y\) of \(a\) can follow the rest of the path and hit \(b\) before \(a\). That event has positive probability, so \(h(y)>0\) and \(I>0\). |
| V4-R2-005 | `chapters/ch09-poisson.tex:303` | minor | “one run of at most \(L\) steps hits \(\{0,L\}\) with probability at least \((1/3)^L\), so \(\tau_L\) has finite mean”. | Failed blocks of \(L\) steps are at most geometric with success probability \((1/3)^L\), so \(\mathbb E[\tau_L]\le L/(1/3)^L\). |
| V4-R2-006 | `chapters/ch09-poisson.tex:303` | minor | “The position stays between \(0\) and \(L\), so its expectation passes to the limit.” | On \(\{\tau_L\le n\}\) the position has stopped. The expectations differ by at most \(L\,P(\tau_L>n)\), which tends to \(0\). |

## Read as holding

The round-1 repairs, including the finite-bit gap in the strong law, the sum of the clipped squares, the fixed-level Brownian sample, the secretary ratio, and the van der Waerden integer. Chapters 1–4, entropy, Markov chains, martingales, Brownian motion aside from the repaired tail, and the graph and extremal chapters were read again and no further issue was opened.

## Not checked

- A LaTeX build.
- `gilmer.tex`, which `main.tex` does not include.
