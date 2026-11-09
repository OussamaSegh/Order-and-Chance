# Volume 4 Phase 2 — sole-validator mathematics: Chapters 5, 13 and 14
**Date:** 2026-11-09. **Validator:** ChatGPT GPT-6, author-designated sole mathematical validator (no separate external referee required).
**Main baseline:** df747b995bf00255f6ba989c9a1c03fdfc3e26df (merged PR #125).
**Disposition:** Source-mathematics PASS for exactly **19 labelled theorem/proposition/lemma proofs** and **21 exercise statement/hint/solution triples** on the immutable TeX blobs identified below. This is not an assessment of figure aesthetics, all-page rendering, reader comprehension, device QA or publication readiness.

## Chapter 5 — Continuous Chance (including two geometric models)

Exact source identities:
- volume4-chance/chapters/ch05-continuous.tex, git blob **4d2221df7adeb926d46c7526faa7829a77645db9**.
- volume4-chance/chapters/ch05-geometric.tex, git blob **2bc6858a1cb598473be2f233ae5ed6b05ff0e93e**, included from the former.

**11 labelled mathematical assertions, individually re-examined:**

- prop:densitymean: defines continuous expectation by absolutely convergent integral and checks compatibility with step integrals, compact approximations and tail cutoffs; not claiming all measurable functions have an expectation from Riemann sums.
- prop:gausstail: for t>=x>0 integrate comparison e^(-t²/2) <=(t/x)e^(-t²/2), giving e^(-x²/2)/x.
- prop:fubini: uniform continuity on compact rectangles makes both iterated continuous Riemann integrals equal the same double-grid limit, with continuous inner integral.
- prop:polar: true area of annular sector (rΔr+Δr²/2)Δθ and bounded uniform variation of h control the polar rectangle Riemann approximation; radial cutoffs satisfy 0<=χ<=1 and annulus area tends to zero.
- prop:manyuniforms: unique binary index factorization 2^(k−1)(2m−1) allocates disjoint infinite sets of independent fair bits. Dyadic finite-union inner/outer approximations to each interval and finite products show arbitrary finite rectangular interval probabilities factor, with all-ones exceptions outer-null.
- prop:orderpair: a rectangle separated from the diagonal has exactly two disjoint equally likely preimages under sorting two independent uniforms. Joint triangle density 2, gap survival (1−u)², mean gap 1/3.
- prop:inverse: a continuous strictly increasing CDF admits the stated generalized inverse; event equivalence Q(U)<=x iff U<=F(x) for 0<U<1 gives the required CDF, handling U=0 as null.
- thm:dct: local uniform convergence on [-A,A] plus common continuous integrable nonnegative envelope g bounds the outside tails by 2∫tail g; this is a deliberately limited Riemann form.
- thm:boxmuller: R=√(-2 ln U) has radial density r e^(-r²/2), independent Θ uniform; polar rectangles transform joint test-function integrals into product φ(x)φ(y). Gaussian tail bound controls truncation and negligible boundary curves justify rectangle probabilities, so the coordinates really are independent N(0,1).
- thm:bertrand (included file): chord >√3 iff midpoint radius D<1/2; sampling endpoints, perpendicular distance, or midpoint area gives respectively 1/3, 1/2, 1/4; the model changes, geometry does not.
- thm:buffon (included file): under independent uniform nearest-line distance [0,d/2] and angle [0,π], and ℓ<=d, integrate conditional crossing chance (ℓ/d)sin θ to 2ℓ/(πd).

**All 9 Chapter-5 exercise/hint/solution triples checked:**
- ex:counter: triangular tent integral 1, pointwise zero off origin, disjoint intervals I_m carry 1/8 per selected tent, so no single integrable dominating function.
- ex:densityunique: continuous integrands with identical interval integrals are equal by the FTC.
- ex:tail: normalize the Gaussian-integral upper bound by √(2π).
- ex:cauchy: arctan normalizes 1/[π(1+x²)], tail |x|f(x)>=1/(2π|x|) prevents finite mean.
- ex:gamma: integration by parts recurses I_(n+1)=n I_n, n>=1.
- ex:order: n*binom(n−1,k−1)t^(k−1)(1−t)^(n−k) arises by counting exactly one value in short bin, others as lower/upper; beta integral gives mean k/(n+1).
- ex:cantor: nested (2/3)^n covering, bit series uses ternary 0/2 digits, each point has probability zero; finite-stage interval masses imply CDF continuity while dense removed middle thirds disallow continuous/finite-exception density.
- ex:usquare: P(U²<=y)=√y, density 1/(2√y), mean 1/3 via improper integral.
- ex:radius: R²=-2 ln U gives exponential(rate 1/2) by exact survival calculation.

## Chapter 13 — The Probabilistic Method

Exact source: volume4-chance/chapters/ch12-method.tex, blob **7bb8f4a676a46524817beb217d04f18ad6317a21**.

**6 labelled proofs checked:**
- thm:erdos: monochromatic clique expected count binom(n,k) 2^(1−binom(k,2)) and positivity when mean<1; n=floor(2^(k/2)) with separate n<k case, factorial lower bound and integer-rounding step prove R(k,k)>2^(k/2).
- thm:alter: some finite coloring has X<=E X; removing one vertex from every original bad clique eliminates all such cliques, at most X distinct vertices removed, yields bound R>n−E X.
- thm:lll: dependency is **joint independence** outside D_i. Conditional-probability induction splits conditioned events into dependent T and independent R, product denominator >=(1−x)^|T|, with x=1/(d+1), ep(d+1)<=1 gives p<=x(1−x)^d. Final complement intersection positive by induction.
- prop:second: finite weighted Cauchy–Schwarz gives P(X!=0)>= (E X)²/E[X²], Chebyshev comparison for nonnegative positive mean justified.
- prop:euler: adding a plane edge increases e,f together; face-edge count for connected simple v>=3 yields e<=3v−6, component decomposition extends bound to disconnected simple graphs, including only K1/K2 components.
- prop:crossing: delete at most one edge per crossing pair and use planar bound. Vertex sampling retains edges with p² and crossings with p⁴; optimize p=4n/m <=1 to get m³/(64n²), with small-vertex graphs treated separately.

**All 6 exercise/hint/solution triples checked:**
ex:carowei (K2,3 expectation 3/2 vs independence 3), ex:tournament (2 of 8 directed orientations cyclic for a triple, expected binom(n,3)/4), ex:sumfree (infinitely many primes p≡2 mod3 by Euclid; interval residues I=q+1..2q+1 sum-free mod p and has (q+1)/(3q+1)>1/3, multiplier yields integer subset), ex:crossing (independent vertex sampling p^4 and exact bound), ex:propertyb (bad-set expected count <1), ex:localcolour (disjoint underlying colour-bit sets imply *joint* independence of the entire outside bad-event family; apply LLL).
Numerical independently computed examples in #122: binom(27,7)=888030, binom(28,7)=1184040, binom(33,7)=4272048, K20 crossing lower bound 267+119/128.

## Chapter 14 — Random Graphs and the Search for Structure

Exact source: volume4-chance/chapters/ch14-graphs.tex, blob **a494b82eee49bc1ed43d43b9b74894ed821706d4**.

**2 labelled proofs checked:**
- thm:subcrit: count candidate component spanning trees using Prüfer k^(k−2), multiply absence-of-outgoing-edges factor (1−c/n)^(k(n−k)), bound for k<=n^(1/3). For **all k**, breadth-first newly discovered counts are stochastically dominated by conditionally fresh Bin(n,c/n) variables: add independent missing trials at each processed vertex so conditional law does not depend on prior exploration. Exponential Markov with θ=ln(1/c) gives P(|C(v)|>=k)<=exp(-(k−1)[c−1−ln c]). Union over n vertices and k=ceil(A ln n), A>1/(c−1−ln c), gives w.h.p. logarithmic largest component.
- thm:triangles: triangle indicator mean binom(n,3)p³, covariance zero for disjoint-edge triples and p^5−p^6 for edge-sharing triples; count shared-edge pairs exactly binom(n,2)binom(n−2,2), variance O(1) at p=c/n and vanishing relative variance when np→∞. Second moment/Markov yield three correct regimes; no false exact Poisson-limit assertion.

**All 6 exercise/hint/solution triples checked:**
- ex:connectivity: isolated count I with mean n(1−p)^(n−1); for p=(ln n+ω)/n use mean→0 if ω→∞, or second moment with ratio (1−1/n)/(1−p)→1 and mean→∞ if ω→-∞, separate p=0.
- ex:giant: while fewer than δn discoveries, dominate a Bin(floor n(1−δ),c/n) supercritical Galton–Watson process from below by discarding extra fresh edge trials; extinction PGF converges uniformly to Poisson(c(1−δ)) and its smaller root stays bounded away from 1 by slope >1 and uniform second derivative, furnishing the promised fixed-vertex **positive** linear-component probability only, not a w.h.p. giant-component theorem.
- ex:trianglecount: indicator linearity gives expectation binom(n,3)p³; expectation alone cannot give lower existence probability at p=c/n.
- ex:susceptibility: breadth-first expected new layer count<=c times previous, sum geometrically E|C(v)|<=1/(1−c), Markov tail alone insufficient for union over n vertices at k~ln n.
- ex:criticalisolated: exact first two factorial moments of I at p=(ln n+t)/n yield α=e^-t and α²; Paley–Zygmund/Cauchy–Schwarz + Markov give α/(1+α) and min(1,α) bounds, not an unproved 1−exp(-α).
- ex:trianglesecond: two triangles sharing an edge use exactly five independent graph-edge indicators; c=1 gives 1/7 <=liminf P(T>0)<=limsup <=1/6.

Independent exact enumeration in PR #122 computes first/second triangle moments for every labelled graph on n<=5, and independent exact Ramsey/crossing fractions in Ch13. These *corroborate* but do not establish all parameter regimes; the above argument assesses the actual unrestricted proofs.

## Acceptance boundaries

This is a mathematical correctness review by the author's **sole GPT-6 validator**, not an independent third-party referee. Only the exact 4 source blobs and the named 19 proofs / 21 triples are covered. Their source hashes must be reverified if any file changes.

Chapter-5 and Chapter-13 figure accessibility/semantic correctness, reader pedagogy, exercise grading, physical KDP/Kindle proof, full downstream Volumes 5–15 dependency graph, and author publication authority **remain open**. No Volumes 1–3 changes and no manuscript corrections were required by the scoped audit. **Whole Phase 2 remains IN_PROGRESS**, not PASS.
