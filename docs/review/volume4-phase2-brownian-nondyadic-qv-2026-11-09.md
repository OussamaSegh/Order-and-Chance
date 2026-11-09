# Volume 4 Phase 2 — V4-P2-013 Brownian quadratic variation at non-dyadic time

Date: 2026-11-09. Sole validator GPT-6. Confirmed mathematical proof gap; source correction pending exact-head CI.
Source: volume4-chance/chapters/ch11-brownian.tex, thm:qv, original Git blob 115a61c8a67023668b77cf365c8259bde5720718.

## Defect
For fixed t in [0,1], thm:qv sums squared Brownian increments on dyadic intervals wholly inside [0,t] and one final shorter interval ending at t. The first-paragraph L2 proof was correct. But its almost-sure argument treated the FULL deviation event as the inverse image of a finite independent-normal-coordinate event in the original uniform sample space. For nondyadic t, B_t depends on infinitely many Levy midpoint coordinates. A finite Gaussian-cube cover for this whole event was not justified within the elementary outer-content model. No counterexample to the theorem is asserted; the finite-event premise of this proof was false.

## Repair

Set h=2^-n and t_n=h floor(t/h). Let
V_n=sum_(k=1)^(t_n/h) (B_(kh)-B_((k-1)h))^2.
Every increment of V_n is determined at the finite dyadic level n and hence is a linear function of finitely many independent Gaussian construction coordinates. Its deviation is a finite-coordinate event. Each increment is independent N(0,h), so E V_n=t_n, Var V_n=2t_n h<=2t h.

For this *finite-coordinate* event, open polynomial deviation sets in the finitely many underlying independent normals may be covered in an increasingly fine grid by products of intervals, after controlling Gaussian tails. Quantile preimages of those products in the actual independent uniforms have their stated finite-product probabilities from Chapter 5's constructed digits and outer-content subadditivity. Thus P*(|V_n-t_n|>eps)<=2t*2^-n/eps^2. The bound is summable in n, and the outer-content Borel-Cantelli argument proves V_n-t_n->0 almost surely for each fixed t, hence V_n->t.

The full thm:qv sum equals V_n+(B_t-B_(t_n))^2. Since all Brownian sample paths are continuous almost surely and t_n->t, that final squared increment tends to zero *pathwise*. Thus the full sum->t almost surely even for non-dyadic t. Its already-correct L2 variance bound remains valid, including the final interval.

This is a pointwise-in-t assertion, not one event holding simultaneously for all uncountably many times.

## Exact regression / scope

New tools/test_volume4_brownian_nondyadic_qv.py tests the finite-prefix proof guard, exact Fraction computations of prefix/full Gaussian square-sum expectations and variances at t=0,1/3,5/7,7/11,1 and dyadic refinements, and deterministic continuous-function endpoint control. These are corroboration, not general a.s. theorem proof.

Prior #120 source-fixed independent Gaussian covariance, and #124 source-fixed L2 partition model, remain untouched. Published Volumes 1-3 and all other chapters remain unchanged. A separate whole-Chapter12 mathematical audit must use this corrected blob, not the pre-fix source. Phase2 final mathematics, figures, all downstream citation references and production acceptance remain OPEN. Merge only after exact-head Build books and native V4 production QA succeed.
