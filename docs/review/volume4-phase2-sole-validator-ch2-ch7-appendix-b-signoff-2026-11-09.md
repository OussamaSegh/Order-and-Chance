# Volume 4 Phase 2 — sole-validator claim-level signoff: Chapters 2, 7, Appendix B

**Date:** 9 November 2026. **Mathematical validator:** ChatGPT GPT-6 (author-designated sole validator; external referee not required).
**Source baseline:** main cf1965d18ebb142ddb4f159d9d4b07a3c92a18d2, merged PR #124.
**Outcome:** PASS for the 22 labelled theorem/lemma/proposition proof arguments and 19 exercise/hint/solution triples enumerated below on these exact immutable source blobs. This does not pass any other mathematical chapter or entire Phase 2.

## Printed Chapter 2: Random Variables and Their Laws

**Exact file:** volume4-chance/chapters/ch02-discrete.tex, blob SHA 921ea590d21af564a636dbcce53a73f7ee6cc61b.

**7 proof-bearing assertions all checked, PASS:**

| Stable source label | Independent mathematical check |
| --- | --- |
| thm:poissonlimit | Fixed-k binomial finite product and log(1-p)/p limit; lambda=0 separately, no infinite limit exchange |
| prop:fixedpoisson | Permutations with m fixed labels: choose labels, derange remainder, then use finite alternating sum for e^-1 |
| prop:cycles | Count permutations carrying a distinguished k-cycle: binom(n,k)(k-1)!(n-k)!/n!=1/k |
| thm:coupon | Fresh coupon stage has conditional geometric success rate (n-i+1)/n; finite means sum to nH_n and integral squeeze gives n log n |
| lem:geovar | Nonnegative geometric tail sum yields E[G(G-1)]=2(1-p)/p², Var G=(1-p)/p² including p=1 |
| prop:couponvar | Stage laws factor conditional on earlier lengths; independent stage variances sum to n² sum k^-2 − nH_n |
| prop:empty | Empty-box indicator and ordered-pair factorial moment counts correctly use (1-1/n)^m and (1-2/n)^m |

**8 exercise/hint/solution triples all checked, PASS:** ex:records (1/k record indicator); ex:fixedvar (diagonal + off-diagonal covariance yields variance 1 for n>=2); ex:quicksort (uniform pivot recurrence yields 2(n+1)H_n−4n); ex:factorial (shifted Poisson factorial moment lambda^m); ex:reservoir (uniform retained **input position** despite repeated item values); ex:prisoners (unique long cycle event yields H_2n−H_n, and 100-prisoner success 1−(H_100−H_50)); ex:birthdaywait (Gaussian-scale logarithmic product bounds together with separately controlled tail yield E[W_N]/sqrt N -> sqrt(pi/2)); ex:twopoisson (convolution and binomial theorem). Verified the stated hints support the solutions and hypotheses match their conclusions.

**Independent computational corroboration:** previous PR #122 exact coupon first/second moments, full small-permutation enumeration, and Quicksort recurrence. The unrestricted statements above were reviewed as proofs, not inferred from finite examples.

## Printed Chapter 7: Entropy, Codes and Typical Sequences

**Exact file:** volume4-chance/chapters/ch07-entropy.tex, blob SHA 25330e7046f0b585bef9ebffb1408bc907c109df.

**8 proof-bearing assertions all checked, PASS:**

| Stable source label | Independent mathematical check |
| --- | --- |
| prop:gibbs | ln t<=t−1 on full positive support with exact equality iff m uniform masses |
| thm:aep | Independent bounded information and Chebyshev, fixed epsilon, both typical-set count bounds from mass-per-word |
| thm:kraft | Disjoint descendant count plus sorted-length greedy construction, including empty-word exception |
| thm:shannon | Rounding information to ceil, Kraft and Gibbs bound [H,H+1) even for one-symbol case |
| prop:chain | Conditional joint-mass factorization and finite sum of logarithms |
| thm:kl | ln(q/p)<=q/p−1 and full support equality, with q=0 convention |
| thm:mutual | KL relative to product marginals equals H(X)+H(Y)−H(X,Y), zero iff independent |
| thm:huffman | Optimal full-tree deepest-leaf exchanges place two smallest masses as siblings, reduce to m−1 induction |

**6 exercise/hint/solution triples all checked, PASS:** ex:entropymax (strict concavity), ex:prefixoptimal (prefix-free 7/4-bit code attains entropy), ex:entropychain (conditional log2(3)−2/3, joint log2(3)+1/3, fair Y), ex:entropyproduct (factorization and Y=X counterexample), ex:ambiguouscode (010 parses 0|10 or 01|0), ex:typicalcount (Bernoulli(1/4) bounded information, Chebyshev, log-cardinality squeeze as epsilon decreases). No source correction required.

**Independent computational corroboration:** PR #122 exact Huffman merging of the nine two-symbol blocks yields expected length 107/36, separately from the exchange argument.

## Appendix B: Extremal Problems and Ramsey Theory

**Exact file:** volume4-chance/chapters/extremal.tex, blob SHA 3899f21ebcc1a05e68cd545cdb96e103d215ffad.

**7 proof-bearing assertions all checked, PASS:**

| Stable source label | Independent mathematical check |
| --- | --- |
| thm:turan | Extremal Zykov twins: equal degrees across nonadjacent classes, valid whole-class clone preserves edge count and forbidden clique, balanced multipartite optimum |
| thm:ramsey | R(s,t) induction on s+t, base R(2,t)=t, pigeonhole at a vertex, K5 red/blue complementary cycles for R(3,3)=6 |
| thm:schur | Monochromatic triangle for r colours by induction, colouring edge by positive difference gives x+y=z |
| thm:sunflower | s-induction on frequent vertex or maximal disjoint petals, union size at most s(k−1), giving exact s!(k−1)^s threshold |
| thm:ekr | Katona cyclic arcs: the k−1 pairs of intersecting candidate arcs starting i and n−k+i are disjoint when n>=2k, then cycle/set double count gives binom(n−1,k−1) |
| thm:vdw3 | All 12 possible AP triples in explicit [8] colouring are non-monochromatic, and the [9] force/reversal cases exhaust alternatives |
| thm:vdw | Induction on length and bouquet size, matching block colour patterns, stretched difference d_i+D, and a final common focus for all r colours |

**5 exercise/hint/solution triples all checked, PASS:** ex:r33 (five-cycle witness and six-vertex force), ex:turanedges (balanced bipartite product floor(n²/4)), ex:ekrsharp (all k-sets through fixed point), ex:schurtwo (forced colours on [5], avoiding colouring of [4]), ex:ekrcomplement (n=2k disjoint iff complementary, any one-per-pair family extremal and intersecting). Hypotheses, proof structure and arithmetic rechecked against actual current text.

**Independent computational corroboration:** PR #119 exhaustive R(3,3)=6 and W(3,2)=9 small-case enumeration. These computations do not substitute for the checked general proofs.

## Scope and remaining gates

PASS refers only to mathematical correctness of these **22 named proof arguments and 19 named exercise/hint/solution triples on the exact three blobs above**. The validator is the sole appointed GPT-6, not a separate external referee. This ledger does not assert beginner-reader, difficulty grading, accessibility, individual full-size figure semantics, cross-volume references, PDF/KDP/Kindle physical proof, or author release authority.

**Whole Volume 4 Phase 2 remains IN_PROGRESS.** Other 105 proof-bearing assertions and 88 exercises/hints/solutions (from the acceptance-register inventory), as well as the figure-semantic and dependency checks, are not signed off by this document. All of Volumes 1–3 remain untouched.

Do not merge this documentation until its own exact-head workflow gates pass. The source blobs listed were read from main after PR #124. PR #125's Chapter 6 Fourier repair is independent and its merge does not change these three source blobs.
