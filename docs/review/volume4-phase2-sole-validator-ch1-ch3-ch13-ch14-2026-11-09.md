# Volume 4 Phase 2 — sole-validator exact-source mathematics: Chapters 1, 3, 13, 14

**Date:** 2026-11-09. **Validator:** ChatGPT GPT-6 (sole, per author). **Manuscript baseline:** main aec73b6b36779611a6f5cd0c539d0241cb26fd66 after merged PR #126. **Scope:** all named proof-bearing assertions and every exercise/hint/solution triple in the four specified chapter blobs. This is a substantive mathematical audit, not a compile check. No external reviewer claimed.

Pinned actual file blobs (SHA of the exact read TeX):
- Printed Ch. 1: volume4-chance/chapters/ch01-counting.tex, **ef5b5ac00bb5f137f4f8cb9934a41c3422984a01**.
- Printed Ch. 3: volume4-chance/chapters/ch03-generating.tex, **10c1ebdc486ca82ec335654bbacc8cfa6ad0ae76**.
- Printed Ch. 13: volume4-chance/chapters/ch12-method.tex, **7bb8f4a676a46524817beb217d04f18ad6317a21**.
- Printed Ch. 14: volume4-chance/chapters/ch14-graphs.tex, **a494b82eee49bc1ed43d43b9b74894ed821706d4**.

## Chapter 1 — From Games to Probability Spaces

**Four proof-bearing assertions: mathematical PASS at pinned blob.**

| Label | Independent reasoning, assumptions and edge cases |
| --- | --- |
| prop:bits | For fixed prefix epsilon of n bits, remainder recurrence identifies precisely one dyadic half-open interval of width 2^-n; n-bit cylinder lengths 2^-n. For positions k_1..k_r, number of prefixes with prescribed positions is 2^(n-r); product 2^-r confirms mutual rather than pairwise independence. Dyadic endpoints are assigned consistently by terminating-zero convention. |
| prop:subadd | Given outer interval covers of A_n within η 2^-n of each infimum, their union covers A and sums to ≤sum P*(A_n)+η. Infimum then η→0 proves countable subadditivity even though no full probability measure was assumed. |
| prop:infdigits | An eventually-zero binary sequence is specified by finite prefix and hence corresponds to one dyadic point. Eventual-one expansions do not occur in the selected terminating-zero convention except as discarded alternatives at dyadics. Each singleton fits arbitrary small cylinders; a countable union of them has outer content zero. |
| thm:ballot | Strictly leading paths start +1; reflect the prefix of a path from +1 until first hit at zero to obtain a path from −1. Reflection is invertible and handles a>b≥1. Good count C(n−1,a−1)−C(n−1,a)=(a−b)/n C(n,a). The b=0 case is treated separately, preventing factorial of −1. Exhaustive ballot checks in PR #122 give independent finite confirmation. |

**Eight exercise/hint/solution triples: mathematical PASS at pinned blob.**

| Label | Independent verification |
| --- | --- |
| ex:mybirthday | With a fixed person's birthday, 22 independent misses give exact P(shared with that person)=1−(364/365)^22 ≤22/365≈0.06027397. By contrast all pair collisions among 23 persons are a different event, with no-collision product ∏(1−k/365)≤e^(−253/365)<1/2 since 365 ln2≈252.99872. Hint matches solution. |
| ex:twochildren | Ordered equally likely BB,BG,GB,GG restricted to at least one boy gives 1/3. Independent seven-day child types yield 14²−13²=27 eligible and 7+6=13 all-boy types; exactly 13/27. The model explicitly defines observation, not a biased reporting mechanism. |
| ex:penney | HHH can win against THH only if tosses 1..3 are HHH; any later HHH is preceded by a tail whose next two heads finish THH first. Event HHH-first has P=1/8; disjoint triples equal THH independently with probability 1/8, so probability never terminating is ≤lim(7/8)^m=0. |
| ex:montyn | Conditional on offered door j, P(H=j|C_1)=1/(n−1), P(H=j|C_j)=1; with uniform prior P(H=j)=1/(n−1). Bayes gives original 1/n and switched (n−1)/n, including n=3 boundary. |
| ex:pairwise | For two dice, parity events A,B,C each have mass 18/36=1/2; all three pair intersections mass 9/36=1/4, triple zero, product of marginals 1/8. Distinguishes pairwise from mutual independence. |
| ex:aces | Without replacement joint=(4/52)(3/51)=1/221, conditional second-ace 3/51=1/17. With independent replacement joint=1/169 and conditional=1/13. Both solution assumptions explicit. |
| ex:catalan | Add leading X to nonnegative n-up/n-down Dyck path to biject strictly positive (n+1)-up/n-down ballot words; removal inverse. Count [1/(2n+1)] C(2n+1,n) = C(2n,n)/(n+1). Exact n≤7 path enumeration in PR #122 independently supports count. |
| ex:smallballot | Four 3A/1B orders AAAB,AABA,ABAA,BAAA; only first two stay >0, 2/4=(3−1)/(3+1). |

## Chapter 3 — Generating Functions and Random Families

**Seven proof-bearing assertions: mathematical PASS at pinned blob.**

| Label | Independent verification |
| --- | --- |
| prop:pgfcoeff | The differentiated n-th term n^(underlined k) p_n s^(n−k) has derivative dominated on compact s≤r<1 by n^(underlined k+1) r^(n−k−1), a summable ratio-test majorant with asymptotic ratio r. Both one-sided quotient limits justified, and k-th derivative at zero isolates k!p_k. |
| prop:pgfmean | Nonnegative terms k p_k s^(k−1) increase to k p_k as s↑1; finite partial sums establish lower bound and the full sum is upper bound even when infinite. |
| prop:pgfvar | Identical nonnegative monotone-limit argument gives E[X(X−1)] from f''(1−). Finite moments ensure endpoint derivative, then X²=X(X−1)+X algebra gives variance formula. |
| prop:pgfsum | Independent joint mass product p_i q_j and nonnegative absolutely summable double series permit regrouping s^(i+j) and factorization; extends by induction to finite sums. |
| prop:randomsum | Condition on integer N=n, with fixed conditional law independent across n-indexed summands: f(s)^n. Mixing against P(N=n) gives g(f(s)); countable finite records have total mass one, so no unjustified infinite product. |
| prop:genmean | At generation size k the next generation has expectation km; summation and induction give E Z_n=m^n when finite m, and Z_1 already has infinite mean in infinite case. |
| thm:extinction | Iterate q_0=0, q_{n+1}=f(q_n). Monotonicity and continuity imply limit fixed; compare iterates with any fixed point to obtain least root. First-extinction events disjoint, so q_n rises to their nonnegative-series probability. For m>1 the left secant at 1 tends >1 and creates root <1; for m<1 the secant stays <1; for m=1 and p_1<1, some k≥2 has positive mass and makes strict secant <1. The deterministic-one-child exception f(s)=s is explicitly handled. |

**Eight exercise/hint/solution triples: mathematical PASS at pinned blob.**

| Label | Independent verification |
| --- | --- |
| ex:thinning | Conditional binomial PGF (1−p+ps)^N, Poisson mixing exp(λp(s−1)), hence Poisson(λp), including p=0/1. |
| ex:golden | f(1/2)=1/3+(2/3)(1/4)=1/2, offspring mean 2p=4/3, thus critical root below 1. |
| ex:lotka | f=(1+s)^2/4, f'(1)=1, f(s)−s=(1−s)^2/4 so only fixed root 1 and extinction certain. |
| ex:randomsumvar | Conditional mean Nμ, conditional variance Nσ²; E S²=σ² E N + μ² E N² and subtract (μE N)². Second moment assumptions ensure justified operations. |
| ex:progeny | Conditional on founder's k children, finite tree iff all independent child trees are finite. Multiply h(s)^k with founder factor s; sum p_k to get h(s)=sf(h(s)). At zero children, empty product one. |
| ex:firstpassage | First + step contributes ps; first − step requires two successive independent upward climbs, contributing qsF(s)^2. Quadratic small root at s=0 is [1−sqrt(1−4pqs²)]/(2qs); taking s↑1 yields min(1,p/q), including p=q. |
| ex:binseries | Exact a_n/a_(n−1)=2(2n−1)/n implies (1−4x)g'=2g, integrate normalized solution g(0)=1. Generalized binomial coefficient matches C(2j,j); derivative of x c(x) recovers (n+1)C_n=C(2n,n). Source explicitly justifies termwise differentiation for |x|<1/4. |
| ex:poissongw | f=e^{c(s−1)} leads 1−ρ=e^(−cρ). Strict convexity gives one positive root for c>1, and only zero at c=1. Uniform second-order expansion plus ρ(c)→0 and c−1=(c²/2)ρ+O(ρ²) gives ρ∼2(c−1). |

## Chapter 13 — The Probabilistic Method

**Six proof-bearing assertions: mathematical PASS at pinned blob.**

| Label | Independent verification |
| --- | --- |
| thm:erdos | Each k-clique monochromatic with probability 2^(1−C(k,2)), so a count of violations with mean <1 must sometimes vanish. Set n=floor(2^(k/2)), bound C(n,k) ≤ n^k/k!; 2^(1+k/2)/k! <1 at k=3 and decreases thereafter; integer Ramsey number ≥n+1>2^(k/2), including n<k. |
| thm:alter | At least one colouring has X≤EX; deletion of ≤X distinct chosen vertices hits every originally bad clique; no newly bad cliques arise by deleting vertices. Remaining complete graph K_m with m≥n−EX certifies R(k,k)>m. Numerics C(33,7)=4272048 and 33−EX=1895685/65536 checked independently in PR #122. |
| thm:lll | Hypothesis is independence of the *joint collection* of all non-neighbours. Set x=1/(d+1), use (1−x)^d≥e^(−1) for d≥1, so p≤x(1−x)^d. Induction over conditioning sets splits independent remote R from at most d neighbours T, applies previous conditional-avoidance bounds for each T_j, and controls ratio by p/(1−x)^d≤x. This also establishes positive sequential avoidance. Case d=0 handled with p≤1/e. |
| prop:second | Cauchy–Schwarz applied to X 1_{X≠0} and indicator gives (EX)^2≤EX² P(X≠0). If X≥0 and EX>0 then event X=0 implies |X−EX|≥EX and Chebyshev applies. |
| prop:euler | Tree starts v−(v−1)+1=2; adding each non-tree plane edge splits a face, preserving v−e+f. Connected simple plane graph face incidence yields 3f≤2e, hence e≤3v−6. Separate components with 1, 2 or ≥3 vertices verify disconnected extension, with zero-edge exception trivial. |
| prop:crossing | Delete at most one edge per crossing pair to obtain plane graph, so cr≥m−3n (stronger m−3n+6 when n≥3). In a good drawing a crossing pair has four distinct endpoints; induced vertex sampling probability p^4 for each crossing vs p² for each edge and p for vertex. Substitute p=4n/m when m≥4n and derive cr≥m³/(64n²). |

**Six exercise/hint/solution triples: mathematical PASS at pinned blob.**

| Label | Independent verification |
| --- | --- |
| ex:carowei | K_(2,3) sum 2/4+3/3=3/2, while maximum independent set is the part of size three; K_5-cycle sum 5/3 versus α=2. |
| ex:tournament | Each labelled vertex triple has eight orientations; exactly two are directed cycles, so expectation C(n,3)/4 and at least one orientation achieves ≥ mean. |
| ex:sumfree | Choose prime p≡2 mod3 above each |a| via Euclid product argument. Interval of residues {q+1,…,2q+1}, p=3q+2, is sum-free modulo p. Uniform nonzero multiplier includes each fixed nonzero integer with probability (q+1)/(3q+1)>1/3. Thus some preimage subset has >n/3 elements and is sum-free in integers. |
| ex:crossing | Reproduce planar deletion bound, sample independent vertices, compute expected inherited crossings ≤p⁴cr, E edges p²m, E vertices pn. For p=4n/m obtain stated constant exactly, with n'<3 convention. |
| ex:propertyb | Union bound/expected monochromatic sets < number of k-sets times 2^(1−k)<1; some colouring avoids all. |
| ex:localcolour | Colour variables independent; bad event attached to F depends only on bits of F. It is jointly independent of all events attached to sets disjoint from F, not merely pairwise; degree ≤d, P(bad)=2^(1−k), apply proved symmetric LLL. |

## Chapter 14 — Random Graphs and the Search for Structure

**Two proof-bearing assertions: mathematical PASS at pinned blob.**

| Label | Independent verification |
| --- | --- |
| thm:subcrit | Counting isolated connected k-sets through labelled spanning trees (Cayley/Prüfer) yields EN_k≤n/(ck²) (c e^(1−c))^k exp(ck²/n); subcritical ρ=c e^(1−c)<1 makes n^(1/3) contribution small. Crucial *independent* exploration bound covers all larger sizes: augment each step's at-most-n fresh Bernoulli trials to exactly n via fresh coins, yielding i.i.d. Bin(n,c/n) dominators Z_i. If |C(v)|≥k then ∑_(i≤k−1)Z_i≥k−1. Exponential Markov with θ=ln(1/c) gives P(|C(v)|≥k)≤e^(−a(k−1)), a=c−1−ln c>0. Vertex union n e^(−a(k−1))→0 at k=ceil(A ln n), A>1/a. Thus no missing intermediate component-size regime. |
| thm:triangles | Indicators for vertex triples use 3 independent edges. Overlap of two triangles in exactly one edge requires 5 distinct edges, giving covariance p^5(1−p); disjoint edge sets have zero covariance even if the triangles share one vertex. Exactly C(n,2)C(n−2,2) unordered overlapping pairs. Variance = C(n,3)p³(1−p³)+2C(n,2)C(n−2,2)p⁵(1−p). For p=c/n, E T→λ=c³/6, Var→λ; second-moment lower λ/(1+λ), Markov upper min(1,λ). If np→0, ET→0; if np→∞, relative variance ≤7/(n³p³)+49/(n²p)→0 and P(T=0)→0. Small-graph independent exact second moment enumeration in PR #122. |

**Six exercise/hint/solution triples: mathematical PASS at pinned blob.**

| Label | Independent verification |
| --- | --- |
| ex:connectivity | E isolated vertices =n(1−p)^(n−1). For ω→+∞ it tends zero; for ω→−∞ and p>0, p≤ln n/n, log E I=−ω+o(1)→∞. Two-isolate factorial moment n(n−1)(1−p)^(2n−3) gives Var(I)/(E I)^2→0. p=0 treated separately. |
| ex:giant | Until δn vertices discovered, at least m=floor(n(1−δ)) unexplored vertices. Independent fresh-edge Bernoulli trials dominate a Bin(m,c/n) offspring count from below via discarding extra trials; coupling holds through first δn discoveries. Offspring PGFs converge uniformly to exp(c(1−δ)(s−1)); choose δ with c(1−δ)>1. Uniform bound on second derivative and f_n'(1)>1 exclude extinction roots tending to 1; fixed-point uniqueness gives η_n→η<1. Survival implies Galton–Watson total progeny ≥δn, hence a fixed vertex has ≥δn-sized component with probability bounded below. This does not claim w.h.p. unique giant. |
| ex:trianglecount | E triangles=C(n,3)p³; when np→0 Markov gives no triangles w.h.p.; bounded positive mean for p=c/n does not itself supply a positive-probability lower bound. |
| ex:susceptibility | Exposing only edges from each current BFS layer toward unseen vertices gives conditional E next-layer size ≤c L_j, hence E L_j≤c^j and E|C(v)|≤1/(1−c); Markov gives tail 1/((1−c)k). Union of n such tails at k=A ln n is asymptotically useless, explaining why the exponential bound is needed. |
| ex:criticalisolated | p=(ln n+t)/n yields E I→α=e^(−t) and E I(I−1)→α² from 2n−3 absent edges for two vertices. E I²→α+α². Cauchy–Schwarz lower α/(1+α) and Markov upper min(1,α) without falsely identifying Poisson limiting law. |
| ex:trianglesecond | Two edge-sharing triples use 5 edges; at most vertex-sharing uses disjoint edge variables. At c=1, λ=1/6 gives bound liminf≥1/7 and limsup≤1/6. |

## Mathematical validation decision and boundaries

**Sole-validator mathematical PASS:** 19 source named proof-bearing assertions and 28 full exercise/hint/solution triples in the four exact blobs above, **without claiming separate independent-referee review**. Proof mechanisms, quantifiers, domains and exceptional cases explicitly re-examined. Independent finite calculations from PR #119 (Ramsey), #121 (martingale/pattern) and #122 (ballot/Catalan, random walks, graph moments, numerics) corroborate selected cases only. No confirmed mathematical source defect was found in this specifically audited set; no gratuitous source changes.

**IN_PROGRESS:** mathematical proof audit for the other printed Chapters 4, 5, 6, 8, 9, 10, 11 and 12; currently 22 prior proof PASS +19 here = 41/127 named assertions, and 19 prior +28 here =47/107 exercise triples, **subject to a final pinned candidate recheck**. Figures and accessibility semantics, prereq/downstream citation graph and production/editorial gates are separate and not waived. Prior Chapters 2, 7 and Appendix B proofs continue to have their original blob-level signoff, as their source files are unchanged by this documentation.

**Required merge gates:** full Build books and Volume 4 native production QA green on this PR's final SHA, compare merged tree with tested head, then reconcile register. Published Volumes 1–3 untouched.
