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
