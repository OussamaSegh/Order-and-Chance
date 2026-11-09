# Volume 4 Phase 2 — sole-validator mathematical acceptance, printed Chapter 9

**Validator:** GPT-6, author-designated sole mathematics validator, 9 November 2026 (not a distinct independent external referee).
**Exact source:** volume4-chance/chapters/ch08-markov.tex git blob **ddfc2e52756052755a0d26437b782f104c069a3f** from baseline main 045eb0c58b8d9d8b5486284ba1a4fd6ea37516a7.
**Scope:** all **ten** named proof-bearing assertions and **nine** complete exercise statements, hints and solutions. Source mathematical validity, not figure semantics or reader/release review.

## Ten proof-bearing assertions — mathematical PASS

| Label | Independent proof check |
|---|---|
| lem:period | For irreducible x,y, paths x→y of length r and y→x of length s give x-return r+s and r+m+s for any y-return m; d(x) divides m. Symmetric argument forces d(x)=d(y), including one-state chains. |
| thm:stationary | Cesàro averages (1/N)∑μP^n lie in finite probability simplex and have a coordinatewise convergent subsequence; ν_NP−ν_N=(μP^N−μ)/N→0, so limit stationary. Irreducibility makes every stationary coordinate >0. For two π,π', r=max π/π' and h=rπ'−π≥0 stationary with a zero coordinate: irreducibility forces h≡0, normalization r=1, hence uniqueness. |
| lem:coupling | For any finite event A, mass difference μ(A)−ν(A) =P(X∈A,Y∉A)−P(Y∈A,X∉A), absolute value ≤P(X≠Y); maximise over A to obtain TV bound. |
| thm:ergodic | Aperiodic gcd 1 at a reference state yields a *finite* collection of return lengths with gcd 1. Bézout integer combination 1=A−B where A,B are nonnegative sums of actual return lengths; B and B+1 lie in the semigroup (or 1 does), giving all sufficiently long returns by division algorithm. Combined with irreducible paths into/out of s, one P^m has strictly positive entries. Minorise each row by ε U, ε=m min K(u,v)>0; couple two block chains via shared uniform endpoint with chance ε, so TV≤(1−ε)^k, and contract TV by the residual P^r. Periodic two-state counterexample correctly excluded. |
| prop:hit3 | From states 1,2 chance to hit 3 within two steps ≥1/6, hence geometric block tail ensures finite mean. First-step equations e1=1+e1/2+e2/2, e2=1+e1/3+e2/3 give e2=5,e1=7, unique finite solution. |
| thm:top | The marked block below original bottom card grows when top card inserted in one of k+1 eligible slots with chance (k+1)/n. Conditional success insertion rank uniform; waiting time depends only on k, and uniform block-relative order is preserved inductively. At k=n−1 original bottom is next top card; independent uniform reinsertion yields uniform full deck conditional on stopping time τ. Stage geometric means n/k reversed yield nH_n. Uniform is stationary by n incoming preimages, so TV at fixed t≤P(τ>t)≤n(1−1/n)^t≤ne^(−t/n); t=ceil(n ln n+cn) gives ≤e^(−c). This is strong stationary time, not arbitrary optional stopping. |
| lem:tvcontract | L1 triangle inequality and stochastic row sums Σ_y P(x,y)=1 imply half-L1 contraction; stationarity makes successive distances nonincreasing. |
| thm:bayerdiaconis | Each a-shuffle word partitions original deck into a ordered packets. For fixed output permutation σ with r rising sequences (descents in inverse order), r−1 required boundaries and a−r freely repeated boundaries. Weakly increasing cut-boundary positions count C(a+n−r,n) possible words; divide by total a^n. Probability zero when r>a, consistent with at most a rising sequences. Inverse stable sorting formulation and n=2, a=2 check show correct σ-vs-inverse notion. |
| prop:rifflecompose | Inverse b-shuffle then inverse a-shuffle corresponds to stable sorting by second then first independent uniform labels, equivalently stable sorting by lexicographic pairs of cardinality ab. Thus composition of forward a then b shuffles has law ab, and k standard riffles law 2^k. |
| prop:untouched | Each card missed in 2t independent selections with mass (1−1/n)^(2t), so E U=n(1−1/n)^(2t). Distinct indicators have nonpositive covariance because (1−2/n)≤(1−1/n)^2, hence Var U≤EU. Every untouched card is a fixed point. With K=EU/2, Chebyshev P(U<K)≤4/EU, uniform Markov P(F≥K)≤1/K=2/EU; therefore TV≥1−6/EU. For t=floor((n ln n)/2−cn), ln(1−1/n)≥−1/n−1/n² for large n and 2t/n²≤1 give EU≥e^(2c−1), hence TV≥1−6e^(1−2c). Boundary c and large-n t≥0 constraints correctly stated. |

## Nine exercise/hint/solution triples — mathematical PASS

| Label | Independent check |
|---|---|
| ex:lazy | Q=(P+I)/2 retains π iff P retains π and all P-positive off-diagonal steps remain Q-positive. Every Q state has holding ≥1/2, so irreducible P gives irreducible aperiodic Q. |
| ex:twostate | Balance π0=q/(p+q), π1=p/(p+q). Two-state deviation δ_(n+1)=(1−p−q)δ_n, δ0=p/(p+q), and TV=|δ_n|. Includes p=q=1 periodic case, p+q=1 exact one-step mixing. |
| ex:ehrenfest | Binomial π(k)=C(d,k)/2^d normalized; π(k)(d−k)/d =π(k+1)(k+1)/d by exact binomial identity. Detailed balance on every adjacent state, even though period 2. |
| ex:pagerank | Teleportation gives every P(x,y)≥(1−α)/m>0; matrix irreducible and aperiodic, finite stationary existence and uniqueness therefore apply; converges by theorem. |
| ex:metropolis | With strictly positive π and symmetric Q, P(x,y)=Q(x,y)min(1,π(y)/π(x)) off diagonal remains nonnegative and row sum ≤1; diagonal absorbs leftover. Detailed balance π(x)P(x,y)=Q(x,y)min(π(x),π(y)) symmetric, so π is stationary; Q-positive edges stay P-positive. |
| ex:toptorandom | At n=3 stage means 3,3/2,1 sum 11/2; explicit history-relative uniform insertion proves strong stationary τ, and coupon union probability n(1−1/n)^t bounds TV as in named theorem. |
| ex:hitbefore | Boundary h1=1,h3=0, from 2 one-step h2=(1+h2+0)/3, hence h2=1/2. |
| ex:risingmean | R=1+Σ_(i=1)^(n−1)I_i with I_i indicator i+1 before i. Each E I=1/2, var 1/4. Disjoint value pairs have zero covariance; adjacent labels give P(both)=1/6 so covariance 1/6−1/4=−1/12. Thus E R=(n+1)/2, Var R=(n−1)/4−(n−2)/6=(n+1)/12. n=52 yields mean 26.5, variance 53/12; P(R≤19 or R≥34) ≤(53/12)/(7.5²)=53/675<0.079, hence >92% in 20..33. |
| ex:period | Deterministic directed n-cycle has P^n=I, period n, unique uniform stationary law by cyclic symmetry. For n>1 distance from point start at all multiples of n is (n−1)/n, so does not converge. |

## Acceptance boundary

Mathematical PASS at this exact blob for 10 theorem/lemma/proposition proofs and 9 full triples. Selected independent finite numerical corroboration: exact 3-state stationary and two-step TV in PR #122, exact 52-card riffle decimals and special shuffle cases in earlier PR #116 and tests, and detailed statement reasoning above. These are not substitutes for the unrestricted proofs.

Source-lock regression file: tools/test_volume4_phase2_signed_off_sources_ch9.py, which detects source changes to any accepted theorem/statement/hint/solution, plus performs independent exact small-state/permutation computations. No published Volume 1–3 changes and no manuscript change warranted by this scoped audit. No assumption that any of the remaining mathematics is checked.

**Phase 2 whole-book status stays IN_PROGRESS.** Candidate-SHA recheck, complete figures, Volumes 5–15 cross-dependencies and real-device/physical print/author-release gates are separate. Merge only after exact-head full Build books and native Volume 4 QA pass.
