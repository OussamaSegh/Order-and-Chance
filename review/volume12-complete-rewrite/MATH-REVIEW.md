# Mathematical verification register — Volume 12

This register does **not** claim external mathematical certification. Verification classes are:

- **Proved in source, author-side proof inspection required:** the central Brownian, stochastic-calculus, SDE, network, matrix and spectral results.
- **Numerically recalculated:** the new 12-unit deterministic examples in `check_new_examples.py` and original numerical scripts in `review/volume12-rewrite/`, subject to actual CI execution.
- **Stated as admitted or quoted:** universality/Tracy–Widom (random matrix edges); Novikov under general integrability assumptions; full generality of Dyson motion from coincident eigenvalues; `thm:cuemax` on extrema.
- **Conjectural or observational rather than theorems:** zeta-zero/eigenvalue analogies, Montgomery's conjectural extension, Fyodorov–Hiary–Keating extremal zeta predictions, and finite numerical spacing comparisons.

Priority theorem labels for an independent full proof reading:
`thm:levymodulus`, `thm:dds`, `thm:tanaka`, `thm:girsanov`, `thm:yamada`, `thm:dyson`, `thm:levyito`, `thm:kesten`, `thm:spiked`, `thm:sinekernel`, `thm:logclt`, `prop:cuelogcorr`, `thm:gmc`, `spectral:thm:dirmatrixtree`, `spectral:thm:best`.

**Completed author-side spot checks during this implementation (not a complete independent review):** Lévy's modulus Gaussian-tail lower/upper steps; Itô's quadratic variation correction and a time-changed martingale; bounded-drift Girsanov normalization; Dyson gap/Bessel-3 reduction; Kesten's free-group values; GOE rank-one outlier formula; sine-kernel Taylor expansion and Keating–Snaith second moment; the log-field $L^2$ threshold; three-vertex matrix-tree and BEST examples.

**Unresolved work that blocks final acceptance:** independent verification of **every** original theorem, proof and solution; comprehensive historical/source fact-check; visual inspection and accessibility checks on actual production assets. An automated or spot-check PASS must never be reported as completion of these proof-level duties.


## Confirmed original mathematical correction

**Chapter 7, Lévy--Itô decomposition (\`thm:levyito\`), zero-diffusion boundary case.** The pre-existing theorem claimed a standard Brownian motion $W$ independent of the jump measure on the *original probability space* even when $\sigma=0$. The canonical probability space of a deterministic zero Lévy process can be a one-point space, on which no non-degenerate Brownian motion exists. This is a false existence claim. The theorem now asserts the invariant correct result: the residual $R$ is independent of the jump measure and has law $\sigma B$; for $\sigma>0$, $W=R/\sigma$ exists on the original space, while for $\sigma=0$ the residual is zero and an independent standard Brownian motion may only be added on a product extension. The proof now handles this case explicitly and also specifies one-sided endpoint neighbourhoods in its jump-measurability construction. Numbering, theorem label, and the remaining Brownian/Poisson claims are unchanged.

This is an author-side analytical correction, **not** an externally certified proof of the entire Lévy--Itô decomposition.


## Further independently identified proof repairs

**Chapter 5, Cameron--Martin (corollary \`cor:cameronmartin\`).** The original proof equated an expectation of $F(W+h)$ under the original measure $P$ with an expectation under $Q$, without the necessary change of measure. The revised identity explicitly reads $\mathbb E_PF(B+h)=\mathbb E_QF(W+h)=\mathbb E_QF(B)=\mathbb E_P[F(B)Z_T]$; it follows because $W$ is a $Q$-Brownian motion. The theorem statement and hypotheses remain unchanged.

**Chapter 11, branching-random-walk speed (\`thm:brwspeed\`).** The original lower-bound proof chose a surviving lineage using an infinite-horizon event, then asserted its next $\rho$ Gaussian increments were independent of that choice. Infinite survival can depend on those future increments, so the assertion was not justified. The corrected argument selects the lexicographically first qualifying **finite $L$-step good path**, measurable with respect to the increments through depth $r+LK$. Its further increments are genuinely fresh, conditional Gaussian variables; its finite-path failure event is bounded by the infinite-survival failure probability. The Gaussian lower-tail estimate now explicitly assumes $0<b<c^*$, sufficient for the speed limit. This fills a nontrivial dependence gap without weakening the lower bound.

These are mathematical author-side repairs, not a statement that every other proof was independently certified.


## Historical and conceptual precision checks

**Robert Brown's 1827 observations.** Brown examined tiny particles *within and released from pollen grains*, not simply moving intact pollen grains. The Chapter 1 opening already said this correctly, but the preface and marketing text had repeated the familiar oversimplification. Those are now aligned with the primary 1828 account, *A brief account of microscopical observations made ... on the particles contained in the pollen of plants* (https://www.physik.uni-augsburg.de/theo1/hanggi/History/Brownian.pdf), and the American Physical Society's historical discussion (https://www.aps.org/apsnews/2016/08/robert-brown-molecular-motion-pollen). Dates 1827 for observation and 1828 for publication are preserved.

**Conformal invariance.** Planar Brownian paths transform under analytic conformal maps after an appropriate *random time change*. The preface and paperback description now state this qualification instead of suggesting exact equality of time-parametrized Brownian laws.
