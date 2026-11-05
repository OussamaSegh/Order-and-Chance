# V3-013b — complete main-chapter solutions and local analysis

Solo internal AI review, not human refereeing or formal verification. All C12
main prose, four named proofs,15 prompts/hints/finding ideas/full solutions,
two full figure sources and bibliography were read. CH12-CORE.md supplies A/B
for all four named results and the first seven problems; this report closes the
other eight and the revised ending. CH12-PROMPT-FIRST.md preserves exposure
limits and first reconstructions, including its corrected first fifth-turn
overcount. Global keyed unnamed/history/voice and actual final outputs remain
separate gates; chapter closure does not approve those automatically.

The actual earlier V1 ch05 prop:seqcrit (monotone/adjacent/Bolzano–Weierstrass/
Cauchy), thm:heine and mean-value arguments were reopened, as were V2 ch06
thm:eulercrit/cor:two and V2 ch07 thm:foursq. C7 cor:abelian's full primary/
invariant-factor/count proof was reopened. The new local arguments use those
actual proofs, not a promised theorem in a later volume.

## Remaining exercises, reconstruction A and adversarial B

| Key | Exact hypotheses/domain and claim | Reconstruction A and supplied-answer comparison | Independent/adversarial B, boundaries and grade |
| --- | --- | --- | --- |
| pb:sylvester | Rational0<a/b<1; greedy distinct unit fractions terminate; recurrence s0=2,snext=s²−s+1 gives telescoping/coprimality and E>1 with the exact rounding law for every k>=0. | Ceiling n>=2 gives numerator0<=an−b<a even before reducing; positive remainders<1/n force larger denominators. Recompute4/13=1/4+1/18+1/468. Recurrence s_next−1=s(s−1) telescopes, gives product of all earlier terms and hence gcd1. For the constant, shifted u=s−1/2 squares upward while s squares downward: normalized logs bracket a common adjacent-sequence limit, strictly between each finite pair. Exponentiating gives s−1/2<Epower<s, earning the floor for all k. Full hints/idea/answer now guide this shorter derivation. | Reconstructed the old supplied logarithmic-tail derivation separately: its increments are positive and bounded by2^(-k−1)/(4u²); the tail bounds Epower/u by exp(1/(4u²)). The local derivative inequality exp(t)−1<=t/(1−t) gives displacement<=3/16<1/2, independently yielding the same rounding. Exact greedy probes for all fractions with denominator<=40, all first13 telescoping/coprime terms, and1000-digit independent upper/lower root sequences bracket E and verify floors through k10. Those numerics support the general inequalities, not replace them. Zero remainder, a=1, unreduced fractions,k0 included. Grade2→3 for three-part discovery/convergence/rounding work. |
| pb:jensen | n>=1 integer,x/theta real; polynomial product. Proper logarithmic integrals for abs(x)!=1 and nonzero complex P without unit-circle roots; new partd earns improper extension to all nonzero P and the complete integer zero-mean classification. | Factor into nth-root polynomials and conjugates, including zero factors algebraically. Before the first integral prompt, define/prove Lipschitz tagged-sum convergence by common refinements and Cauchy completeness, plus linearity, finite additivity, shifts and primitive rule by MVT. Bound log derivative by2abs(x)/(abs(x)−1)², so the exact finite product yields the proper mean. Shift each root factor, half the squared logarithm, add leading logabs(a). Strip zero roots before actual Kronecker. For unit roots, compare logsin with logt, control epsilon logepsilon tails, derive I=int0..pi/2 logsin=−pi log2/2 by doubling, and obtain zero unit-root mean. Finite translated singularity tails justify all improper shifts/additions. Every original target and the formerly unproved last remark are earned, with full partd/hint. | A different general check differentiates the mean in r on0<=r<=R<1: bounded second r-derivative gives a uniform O(h²) Taylor estimate, so finite integral inequalities justify differentiating. Its derivative is the real part of−2 exp(it)/(1−r exp(it)); finite geometric truncation has cosines of zero mean and remainder<=2R^N/(1−R), giving derivative0 and mean0. Invert r for abs(r)>1. For unit roots, independently use product_(k1..n−1)abs(1−zeta_n^k)=n; monotone near-endpoint sum/integral comparison and the earned log-tail bound make (log n)/n vanish, also giving mean0. Numerically recompute all products n1..15 including x0/±1, proper quadrature of3X(X−1/2)(X+2)(X−2i) with mean log12, and logsin. Constant degree0,zero roots,repeated/unit roots,negative x and leading sign checked. P0 excluded. Under the original no-unit-root contract zero mean iff±X^m; extended case iff±X^r product Phi_m^e. Grade2→3, new partd disclosed. |
| pb:mersennediv | Odd prime p; prime q dividing2^p−1 has q1mod2p and q±1mod8. Ifp3mod4 and2p+1 prime, it divides; stated three examples composite. | Order of2 moduloq dividesp and cannot be1, so equalsp; q odd supplies factor2. The congruence2=(2^((p+1)/2))² gives quadratic residue, then actual V2 supplementary law. For q2p+1=7mod8, Euler criterion gives the divisibility. Hints and all write-up steps match. | Independently factor every M_p for odd prime p<=31 and check each actual prime factor; separately trial-prime23/47/167 and exact modular powers for p11/23/83. p3 yields equality M3=7, not compositeness; p2 would have factor3 and violate the supplementary conclusion, so oddness essential. No converse from congruence restrictions alone. Grade1 retained. |
| pb:dice | Labels1..6 each once on cube faces; rotations identify dice; standard opposite pairs sum7, mirrors distinct. | Trivial stabilizer follows because the six face normals span R3.720/24=30. Standard assignments3!*2³=48 give2 rotational classes. If a mirror and rotation have the same numbering, injective labels force equal face permutations, hence equal matrices, contradicting determinant sign. Reflection conjugates rotations into rotations, so pairs of classes are well-defined. | Independently enumerate all24 proper signed-coordinate permutations, every720 labeling, all free24-element orbits, all48 standard labelings and their two orbits. Explicit reflection has no fixed rotational class, giving15 mirror pairs; standards one mirror pair. Distinctness of labels is essential and never replaced by a nonfree count. Grade1 retained. |
| pb:ksubsets | Integer n>=0,integer0<=k,l<=n/2; permutation-character Gram=min+1, distinct irreducible differences/binomial degrees, subgroup orbit counts nondecreasing. | Burnside on ordered pairs of subsets gives intersection sizes0..min(k,l), with four-region bijection proving orbit completeness. Finite differences of Gram give delta. Define virtual characters as integer combinations; squared coefficient norm1 leaves one±irreducible, positive degree gives plus. Restriction is explicitly the same representing matrices on a subgroup, hence actual representations; invariant multiplicities nonnegative give monotonicity. | Different general proof constructs an actual Maschke complement inductively: each earlier chi_j occurs once in pi_k by the min formula, so subtract those actual summands, then norm1 proves irreducibility. Exact brute permutations/subset masks for every S_n n0..7 independently recompute all Gram entries, differences and degrees. n0,empty subset,k0,binom(n,−1)=0 and middle k included. Positive norm alone is not asserted for arbitrary class functions. Grade3 retained. |
| pb:egz | Prime p,m>=1 variables,nonnegative degree bounds d_j with sum<m; zero polynomials/empty systems allowed. Then p divides common-zero count. For every n>=1,2n−1 integer entries have n indices with divisible sum, threshold sharp. | Product indicator has degree bound(p−1)sumd_j<m(p−1); some variable exponent<p−1 in every monomial, so its power sum0 even at exponent0. Zero f contributes1; empty system counts p^m. Prime construction has degree bounds2(p−1), even if first form0; a nonzero common solution has exactlyp supported indices. Composite extraction leaves2n−1 before the last of2m−1 blocks; divide sums byn and apply m theorem. n1 sharpness handled as empty list; n>=2 uses n−1zeros/n−1ones. | Reconstruct every monomial factor and support count in characteristic2/3, with no nonzero-polynomial shortcut. Enumerate every pair of affine linear forms on F2³/F3³, all F3^5 common zeros for every coefficient5-tuple, and all residue multisets for EGZ n1..6. Independent subset-sum dynamic programming verifies existence/sharpness, not the general proof. Old degree−infinity summation even admits the system0=0,X=0 in one variable, with one common zero, since−infinity+1<1. It also admits a zero equation in dimension0. Nonnegative degree bounds exclude these false cases while retaining every intended application and all zero polynomials in positive dimension under the genuine total-degree condition. Old/new disclosed. Grade2 retained after C9 power-sum methods. |
| pb:abelian | Positive n; number A(n) of finite abelian groups. Real s>1 Dirichlet product; real x>=1 average cx+O(sqrt x),c=product_(k>=2)zeta(k). | Actual C7 uniqueness gives partition counts and A1=1. Define zeta before prompt, prove dyadic convergence/zeta tail, bounded positive products, and cofinal finite-sum rearrangements locally. Finite prime/geometric products earn Euler and partition products before use. Define g,h by finite factorizations, so no Dirichlet-series uniqueness theorem is assumed. Split perfect squares: summatory g<=Hsqrt x,H=product_(k>=3)zeta(k/2)<infinity. Floor error<=Hsqrt x; dyadic tail O(x^-1/2) earns the full claimed error without future partial summation. | Different tail proof: sum g(m)/m over m>x by m=r²j. For j<=x, R=floor sqrt(x/j)>=1 and sum_(r>R)r^-2<=1/R<=2sqrt(j/x) by telescoping1/(r(r−1)); for j>x, sumr^-2<=2 and1/j<=1/sqrt(xj). Hence tail<=2H/sqrt x and total error<=3Hsqrt x. Exact finite coefficient generation vs prime-factor partitions agrees for every n<=4096; both square-split/floor identities recomputed. Independent rational Euler-transform bounds and zeta-factor tail certify the stated decimal prefix2.2948, compared with80-digit mpmath. These finite checks are not asymptotic proof. Prime exponents0,trivial group,s>1 threshold,H's first zeta3/2 term and all nonnegative reorderings checked. Grade2→3 for convergence plus full error term. |
| pb:dodecaturns | Finite G,central probability mu,integer t>=0 and start e; full character inversion. For A5 uniform20 three-cycles, shorter return/fifth-turn formulas requiret>=1; sharp absolute spectral rate4^-t. | Schur-average each class operator, trace its scalar; finite convolution multiplies operators. Conjugated character basis supplies the exact normalized inversion, no undefined induction theory. At t0 every scalar zeroth power is1, including0, from matrix identity. For t>=1 ratios1,0,0,1/4,−1/5 give return formula. A fifth turn means one12-element class of±72-degree rotations, giving(1/5)(1−4^(1−t)); two-fifths-turns are the other12. Character bounds give uniform/TV upper bound and identity asymptotic gives sharp base. | Independently enumerate all60 even permutations, both disjoint12-element5-cycle classes, all20 steps, and every state's exact rational distribution for t0..10. Compare every state with all five Fourier terms, all totals and TV bounds. t2 return1/20,fifth-turn3/20. The old unqualified short return formula gives42/60 at t0 instead of1; the fifth-turn formula gives−3/5 instead of0. Prompt requests both probabilities for every integer t>=0, with the original short expression qualified fort>=1. Full answer retains the missing18*0^t return and3*0^t per-fifth-class modes, so it earns all times with the explicit zeroth matrix-power convention instead of weakening the whole target to positive times. My first derivation incorrectly used24 for the requested event; supplied answer's12 was correct. The old numeric Theorem12.5 and Exercise11.7 were in fact correct in the opened PDF; replacing them with stable labels is robustness, not evidence of a stale numerical reference. Grade3 retained. |

## New local arguments, source changes and narrative

The actual V1 integration toolkit explicitly postpones construction of general
integrals. The new Lipschitz tagged-sum argument proves exactly the existence
and elementary operations this chapter invokes, using MVT and actual Cauchy
completeness. Its common-refinement estimate is M(B−A)(meshP+meshQ), independent
of all tags; this gives arbitrary-partition convergence, not only one sequence
of equally spaced sums. Empty/reversed intervals are defined. Telescoping MVT
tags prove the primitive rule used for the log tail; no future FTC premise.
Unit-root improper integrals control every deleted tail independently, so finite
root multiplicities/translated zeros cause no unproved interchange of limits.

The positive-product bound and finite-family supremum argument earn every
infinite Euler-product reordering. At s1 the g expansion and at s1/2 the h
expansion are justified by the same nonnegative bounds, rather than by analytic
continuation. No complex zeta theory, partial summation or Volume6 supplies a
premise. The numerical constant check uses a separate finite rational method:
the jth difference of(n+1)^-k is the iterated integral of(1−product x_i)^j over
the unit k-cube, hence lies in[0,1]. Expanding1/(1+t) in powers of(1−t)/2
gives a transformed eta tail<=2^-J. Elementary one-variable polynomial integrals
justify these finite iterated integrals; no measure/Fubini theorem is needed.
With J32 and k<=24, the remaining zeta-factor tail is bounded by4*2^-24 and
its positive product by1/(1−4*2^-24). Both exact rational endpoints have
floor(10000c)=22948. Mpmath is a separate numerical comparison, not formal proof.

The new C5 finite minimality/uniqueness proof is recorded separately in
V3-013b-SMALL-SIMPLE.md. It earns an earlier unsupported claim without invoking
Burnside or Feit–Thompson. C4 now marks minimality as a future outlook, and C12
uses the earned earlier proof. The new subsection label gives an actual section
number, rather than accidentally reusing a preceding proposition's counter.

Rewrote the ending around an actual fifth-turn trace phi in both spatial and
quaternion coordinates; replacing q by−q changes the complex2 trace but preserves
the spatial rotation. Define/prove abelianization and coefficientwise polynomial
functors and the dual's reversed composition, rather than call q→R_q an
unexplained object-level functor. Normalizing an approximation is explicitly
r/sqrt(N(r)) for r!=0. A sign-chosen interpolation has squared length>=1/2,
so its normalization never divides by0; antipodal representatives are handled.

The unproved incidental homology-sphere/600-cell and SL2F5 identifications, broad
current-research flourish and Klein-special-function analogy are removed from
the teaching route. What is lost is those outward connections, not any named
result, exercise target or binary-group order/kernel/involution statement. The
full loop topology and rotation classification are instead earned locally.
V3-013b-curricular-disclosure.json records old/new statements, target preservation,
new Jensen partd, domain correction, star changes and affected copy scan. Cover
art and canonical identity are unchanged; cover-note history/generator wording
still needs global publishing reconciliation through common/cover-notes.json.

Actually opened preliminary87bad3df print354–364 in colour and354/358 grayscale.
All text, displays, figures and margins in those11 distinct pages were read.
Page354's small angle/output labels were light in grayscale; strengthen only
their text to charcoal, retaining strokes/geometry/approved palette. Corrected
output and all new pagination remain pending. Old87 pages also contain the
subsequently corrected norm wording and replaced ending; they do not approve
current source. Actual theorem number12.5 confirms the old reference was correct.
No reading-PDF, EPUB/reader or later-build approval transfers from these views.

The mathematical registers accept these eight keys only after the authored A/B
records and source reconciliation. Inventory/tests assign no approval. All43
named results and36 exercises in the four appendices, global keyed unnamed/
dependency/history records and the final written voice/render/artifact gates
still remain. No claim of a human or spoken read-aloud review is made.
