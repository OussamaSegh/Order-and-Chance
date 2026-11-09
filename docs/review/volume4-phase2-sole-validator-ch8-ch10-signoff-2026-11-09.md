# Volume 4 Phase 2 — mathematical sole-validator audit: Chapters 8 and 10
**Date:** 2026-11-09. **Sole validator:** ChatGPT GPT-6, at author's direction (not an independent external referee).

**Scope:** every named proof-bearing assertion and every exercise statement/hint/solution triple in the current printed Chapter 8 (random walks) and Chapter 10 (Poisson clock). Mathematical validity only; figure, pedagogy, device and cross-volume integrity are separate.

Exact immutable Git source blobs:
- \`volume4-chance/chapters/ch07-walks.tex\`: **8b64abc66f79ccbc792906fbfa9ba50e9ab3e890** (9 theorem/proposition/lemma labels; 8 complete exercise triples).
- \`volume4-chance/chapters/ch09-poisson.tex\`: **6de4e7e1fd5c6369d553e45190e54807c553a743** (13 labels; 8 complete exercise triples).
- Baseline repo main: 045eb0c58b8d9d8b5486284ba1a4fd6ea37516a7 after merged #128. Source blobs are the actual fetched full TeX, not historical plan notes.

## Printed Chapter 8 — Random Walks

**Named proof arguments: 9/9 mathematical PASS at the exact blob.**

| Label | Independent mathematical verification |
|---|---|
| thm:rwreflect | Reflection of only the post-first-hit continuation is an involution from paths to endpoint b≤a with max≥a to paths ending 2a−b≥a. Endpoint parity is preserved. Splitting according to S_n≤a and S_n>a gives P(M_n≥a)=P(S_n≥a)+P(S_n>a), without double-counting equality S_n=a. |
| thm:ruin | Hitting endpoints is a.s. finite since any consecutive N upward steps succeeds before block end with probability p^N>0; repeated independent N-block failures decay geometrically. First-step Dirichlet equation h_k=p h_(k+1)+q h_(k−1), h0=0,hN=1 gives k/N in fair case and geometric ratio (r^k−1)/(r^N−1), r=q/p, otherwise. |
| prop:duration | Finite nonnegative g solving g_k=1+p g_(k+1)+q g_(k−1) yields constant expectation g(S_{n∧τ})+(n∧τ); nonnegativity makes Eτ≤g(k), then bounded convergence of g(S_{n∧τ}) and monotone convergence of τ∧n identify Eτ. Discrete minimum principle checks g≥0. Fair g=k(N−k) and biased difference equation pδ_(k+1)−qδ_k=−1 produce exactly the printed formula. Independent rational linear-system calculations for N≤8 and p=1/3,1/2,2/3 in PR #122 corroborate. |
| prop:visits | After each first-return finite record, unused signs are fresh and give conditional chance f of another return. Thus P(V≥m)=f^(m−1) and tail-sum E V=Σ_m f^(m−1). Counting visits through N gives E V_N=Σ_(n≤N)P(S_n=0); nonnegative truncation and finite-record partition identify lim E V_N with E V, including infinity. |
| thm:polya | d=1 uses u_(2m)~(πm)^−1/2; d=2 linear change of independent sign pairs gives u_(2m)=[C(2m,m)/4^m]^2~(πm)^−1. For d≥3 Fourier orthogonality extracts u_n as integral of φ(θ)^n, φ=Σ cos θ_j/d. Crucially the proof bounds \|φ\|, not signed φ: near origin and the 2^d cube corners only, Gaussian domination e^(−n|θ|²/(4d)) applies, and on the compact remainder \|φ\|≤ρ<1. Integrating yields summable O(n^(−d/2))+O(ρ^n) and visit expectation finite, hence f<1. The corner neighbourhoods are disjoint (radius √2, d≥3). |
| thm:arcsine | First-return path is a strict ballot excursion ending back at zero; two signs give f_(2m)=u_(2m)/(2m−1)=u_(2m−2)−u_(2m). First-return decomposition gives u_(2m)=Σ_(r≤m)f_(2r)u_(2m−2r). No-return probability is telescoping u_(2m), so last-return time 2k mass is product u_(2k)u_(2n−2k). Reflection at ±1 gives staying-nonnegative probability u_(2m). All finite identities independently enumerated through n=5 in PR #122. |
| prop:harmonic | Conditioning on first neighbour gives harmonic equation. Finite connected maximum principle: positive interior maximum propagates along path to boundary a where difference must be zero; apply to negative difference for uniqueness. |
| thm:arcsinelimit | Occupation count edges above axis is even at even terminal time; first excursion splits into upper/lower equally likely sign, so induction through first-return convolution recovers the same u_(2k)u_(2n−2k) law. For fixed 0<a<b<1 both k and n−k are Θ(n), giving uniform local binomial asymptotics and a legitimate Riemann sum on compact [a,b]. Substitution t=sin² θ gives stated arcsine integral. No claim of uniform local asymptotics close to 0 or 1. |
| lem:centralbin | Exact successive ratio u_(2m)/u_(2m−2)=(2m−1)/(2m), base m=1, and inequality (2m−1)²≥4m(m−1) inductively yield u_(2m)≥1/(2√m). |

**Full exercise/hint/solution triples: 8/8 mathematical PASS at the exact blob.**

| Label | Independent verification |
|---|---|
| ex:ballotwalk | Transform remainder after initial +1 by Y_j=1−S_(j+1): forbidden return to 0 becomes first hit of positive barrier 1. Reflection yields bad count C(n−1,a), subtract from C(n−1,a−1), ratio (a−b)/(a+b), valid for b=0 with binomial-zero convention. |
| ex:maxlaw | Sum the endpoint reflection formula over b≤a to get P(M≥a,S_n≤a)=P(S_n≥a); add disjoint S_n>a, yielding exact maximum law, equality case handled. |
| ex:timepositive | Two signs of a first-return excursion of length 2m give 2 C(2m−1,m)/(2m−1) /4^m = u_(2m)/(2m−1); binomial ratio also yields u_(2m−2)−u_(2m). |
| ex:unfair | With q/p=1/2,N=3, h1=4/7 and h2=6/7; substitution in h1=(2/3)h2 and h2=2/3+(1/3)h1 confirms both. |
| ex:meet | Difference of two independent fair walks changes ±2 each probability 1/4 or 0 probability 1/2. Nonzero steps occur infinitely often a.s.; embedded walk divided by 2 is simple symmetric, from −1. Fair ruin on [-N,0] gives chance (N−1)/N to reach 0, so eventual meeting probability one. |
| ex:escape | f_(2m)~1/(2√π m^(3/2)), so 2m f_(2m)~1/√(πm) and mean first-return time infinite although first return a.s. |
| ex:exittime | Stop at ±R; candidate g(k)=R²−k² solves 1+(g(k−1)+g(k+1))/2 and vanishes on boundary. Bounded-stop argument ensures finite Eτ; uniqueness by maximum principle gives E_0τ=R². |
| ex:electric | Harmonic hitting potential satisfies Kirchhoff node balance for unit edges; total current leaving high terminal b equals Σ_(y~a)h(y), so P_a(hit b before return a)=current/deg(a)=1/(deg(a)R). Series path R=m, parallel cycle branch lengths m,k gives R=mk/(m+k). This is finite graph/electrical probability, not an unproved continuum argument. |

## Printed Chapter 10 — The Poisson Clock

**Named proof arguments: 13/13 mathematical PASS at the exact blob.**

| Label | Independent mathematical verification |
|---|---|
| prop:memoryless | Continuous survival G with G(s+t)=G(s)G(t), G(0)=1 and not-a.s.-infinite excludes G(1)=0 and 1. Rational powers determine G(q)=e^(−λq), continuity extends to t≥0. |
| lem:gamma | Independent exponential gaps have joint product density λ^n exp(−λΣe_i). Sequential one-variable substitutions t_k=Σ_(i≤k)e_i have derivative one and positive-orthant image ordered simplex; density λ^n e^(−λ t_n), no unproved general n-dimensional Jacobian formula needed. |
| thm:uniform | For n≥1, event N(t)=n needs ordered times inside t plus next independent gap>t−t_n. Multiplying joint density by exp(−λ(t−t_n)) cancels t_n, giving constant λ^n e^(−λt) over simplex of volume t^n/n!. Dividing conditional probability gives n independent uniform order-statistics. n=0 gap>t gives e^(−λt). |
| lem:colouring | Conditional multinomial counts given N=n, multiply by Poisson(μ) mass; n! cancels and e^(−μ)=∏e^(−μ p_j), proving independent Poi(μ p_j) colour counts, including μ=0 and p_j=0. |
| thm:increments | Condition on N(t_m) via uniform order statistics. Multinomial allocation to disjoint subinterval lengths ℓ_j and preceding independent colouring lemma yields jointly independent Pois(λℓ_j) increments. |
| thm:thinning | Wait to first kept point has survival E[(1−p)^N(t)] = exp(−λ p t). Finite-index fresh independent exponential gaps/marking coins give independent successive kept waits. For disjoint time bins, conditional thinning of independent original Poisson counts factorises the kept and discarded joint count distributions, establishing independence of the two processes, not merely their marginal rates. p=0,1 covered by zero counting stream. |
| thm:superpose | Minimum of two independent exponentials rate λ+μ. Conditional on first clock and waiting time, memorylessness leaves the other with original exponential residual and the ringing clock resamples, preserving independent next merged gaps. Eventual ties probability zero. |
| prop:residual | R_t>s iff interval (t,t+s] empty, probability exp(−λs) by independent increments. Tail integral gives mean 1/λ, valid for fixed t≥0. |
| prop:onesidedgap | Age A_t=min(t,backward empty interval) has density λ e^(−λa) for 0<a<t and atom e^(−λt) at t; independent forward residual R~Exp(λ). For u<t integrate exp(−λ(u−a)) over a<u, adding P(A≥u) to obtain e^(−λu)(1+λu). For u≥t, E exp(λA)=1+λt gives (1+λt)e^(−λu). Integrating tails gives (2−e^(−λt))/λ; correctly distinguishes stationary two-sided Gamma(2,λ) gap. |
| prop:race | P(min>t)=exp(−(λ+μ)t). Integrate density of E at u≥t times P(F>u) to obtain P(E<F,min>t)=[λ/(λ+μ)]exp(−(λ+μ)t); factorisation proves winner independent of time and probability λ/(λ+μ). |
| thm:lecam | Construct coupling N_i~Poi(p_i), set Bernoulli X_i=1 whenever N_i≥1 or additionally when N_i=0 with probability [p_i−(1−e^(−p_i))]/e^(−p_i). For p_i≤1 this is in [0,1]. Marginal X_i~Bern(p_i), and exact discrepancy P(X_i≠N_i)=p_i(1−e^(−p_i))≤p_i². Union bound and coupling inequality give TV bound ≤Σp_i²; independent Poissons sum to correct parameter. |
| thm:mm1 | Uniformization at Λ=λ+μ with independent arrival/departure choice, holding at 0 on invalid service, constructs the queue without explosion. Detailed balance π_(k+1)μ=π_kλ and geometric normalization π_k=(1−ρ)ρ^k yield πK=π coordinate-wise including 0; mixing over Poisson tick counts proves continuous-time stationarity. Summing kπ_k gives ρ/(1−ρ). |
| prop:emptiness | Starting at 1, embedded birth/death jump probabilities 1/3 and 2/3, rate-3 waiting time. For 0/L barrier, upper-hit probability 1/(2^L−1). Bounded-stop identity E S_τL+(1/3)E τL=1 gives E τL=3(1−L/(2^L−1)), hence E number jumps=3. Independent Exp(3) holding times yield E emptiness=3*(1/3)=1. π0λ=π1μ=1/2 and stationary tail Σ_(k≥2)2^(−k−1)=1/4. |

**Full exercise/hint/solution triples: 8/8 mathematical PASS at the exact blob.**

| Label | Independent verification |
|---|---|
| ex:twoexp | Convolution of two Exp(λ) densities yields Gamma(2) density λ²t e^(−λt), survival e^(−λt)(1+λt), mean 2/λ by linearity. |
| ex:minexp | Product of exponentials gives rate Σλ_i; integrate density of E_j at t times all other survivals: λ_j/(Σλ_i), ties a.s. absent. |
| ex:bus | Stationary two-sided rate 1/10 process has independent backward age and forward residual, each Exp(1/10), mean 10 minutes; covering gap mean 20 minutes. One-sided clock has shorter mean and is explicitly ruled out by problem. |
| ex:lecamnum | Σ_20 p_i²=20*(0.02)²=0.008, Poisson comparison mean 0.4. |
| ex:mm1mean | Σkρ^k=ρ/(1−ρ)² for 0≤ρ<1 via t−ρt=ρ/(1−ρ), stationary mean (1−ρ)t=ρ/(1−ρ). |
| ex:emptycheck | π0*arrival rate=(1/2)*1=1/2; π1*service rate=(1/4)*2=1/2; tail k≥2 equals geometric 1/4. |
| ex:superpose | If λ+μ>0, independent Poi(λ),Poi(μ) are obtained by colouring Poi(λ+μ) red/blue with probabilities λ/(λ+μ), μ/(λ+μ), hence sum has Poi(λ+μ). If λ=μ=0 the sum is identically zero. |
| ex:firstarrival | Given N(t)=n≥1, n unordered uniform positions; min>u iff all >u, giving ((t−u)/t)^n, mean integral ∫_0^t (1−u/t)^n du=t/(n+1), at n=1 t/2, n=0 has no in-window first point. |

## Acceptance decision / limits

**Sole-validator mathematical PASS:** 22 labelled proof arguments and 16 complete exercise/hint/solution triples in exactly the two pinned blobs. This is source-level reasoning with independent arithmetic corroboration, not merely structure tests. No confirmed new mathematical error in these exact claims. Read/write scripts never modify published Volumes 1–3; no manuscript change was necessary.

**Not accepted by this record:** other chapters, whole-book candidate SHA, figures at full-resolution, full Volumes 5–15 dependency graph, reader difficulty, physical print/Kindle proof, author publication permission. Do not assert that the two-chapter mathematical proof review establishes full Volume 4 Phase 2 approval.

New source-lock + exact finite calculation regression tests check both Git object hashes, all 22 proof labels, 16 exercise/hint/solution labels and numerical formula instances, but cannot serve as the general proofs.

**CI merge gate:** Both Build books and Volume 4 native production QA must be successful at the exact final PR head.
