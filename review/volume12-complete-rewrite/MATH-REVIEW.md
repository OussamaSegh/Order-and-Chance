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
