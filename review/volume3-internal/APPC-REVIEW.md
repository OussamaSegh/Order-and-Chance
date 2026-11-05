# V3-016 — Linear Algebra Method, complete internal mathematics

Solo internal AI review, not independent human refereeing or formal verification.
Read the entire original and revised main appendix, every one of18 named
arguments, all ten prompts/hints/finding ideas/full solutions, both actual
figure sources and every bibliography entry. APPC-PROMPT-FIRST records all
ten first solutions before opening any supplied hint/answer. The supplied
Fano, zero-denominator quadric and cap-plane arguments were already sound;
the record distinguishes those facts from actual new repairs. Mathematical
acceptance is separate from the global history/context/voice and final pixels.

## Contract and actual earlier imports

Ground-set/Euclidean/cube dimension n>=0 unless stated otherwise; Fisher n>=1,
Chevalley–Warning n>=1, EGZ n>=1 and Kakeya n>=1. Fields have0!=1. The dot
product here is bilinear without conjugation, including over C or F2, and is
not the preceding appendix's positive Hermitian product. Two-distance means
at most two positive distances between distinct points. Polynomial total/
individual degree, homogeneous part and affine-linear are defined before use.
F^A, delta basis, support and zero slice rank are defined before invocation.

Actual V1 main order was reopened: sequences is printed3, polynomials6,
linear7, differentiation/integrals8, probability10. See V3-016-SOURCE-ORDER.
Actual V1 ch09-probability ex:ramsey full solution812–824 read: finite expected
monochromatic count, floor parameter, factorial ratio and existence step.
Actual V1 ch05-sequences prop:early-differentiation346–386 and thm:mvt479–505
were reopened in full, including quotient/chain limit proofs, Fermat, extreme
value/Rolle and the secant subtraction. These earn the local rational-cube
optimization without future analysis. The rational estimate itself uses no
derivative. Actual V1 ch02-counting prop:counts(b)60–79 and ex:stars581–586
were read in full: the multiplicity-to-stars-and-bars bijection supplies the
monomial count with n+1 labels after adjoining a slack exponent. Actual V1
ch07 exchange56–72 and rank-nullity97–104 were reopened; division only by
nonzero coefficients makes the coordinate proofs valid over any field.
The full root-bound proof in C1 ex:fieldcyclic's solution was reopened:
F(X)-F(a) is divisible by X-a by the difference-of-powers identity;
cancel nonzero b-a at every other root and induct on degree. This is a
field-general proof, not an inference from a real-polynomial title.
The C6 K[X] example originally asserted Euclidean division without its
general-field algorithm. Add CH06-U-FIELD-DIVISION before quotient-ring
uses: cancel the leading term by its nonzero leading coefficient,
strictly lower a nonnegative integer degree, and prove uniqueness by
the degree-of-product identity. B: subtract two proposed remainders;
a nonzero quotient difference has degree at least deg Q, contradicting
both remainder bounds. Zero dividend, constant divisor and positive
characteristic are included; X divided by2X over Z shows the field
hypothesis. CN's monic coordinate reductions now have this actual
earlier proof, rather than an unproved algorithm premise.
Actual earlier V1 FTA/root-bound, real basis/Gram–Schmidt and
rank-nullity proofs were read in earlier records; C1 explicitly extends
coordinate/rank/determinant arguments to arbitrary fields. Actual V2 integer
factorization and finite-field group/primitive results were read previously;
the powersum B below also avoids importing cyclicity. C9 actually proves finite
field existence/size/characteristic and units, not just a field-name convention.
The new source reconstructs all finite polynomial/field facts locally where
needed. No essential result is borrowed from later V4 or V9.

## Named arguments: A and substantive independent/adversarial B

| Key | Exact domain/claim | Reconstruction A | Independent/adversarial B and boundary probes |
| --- | --- | --- | --- |
| combinatorial:thm:oddtown | n>=0, finite family of odd subsets, off-diagonal even intersections: m<=n. | Incidence vectors over F2 have Gram identity; take dot product of a zero relation with each vector to recover each coefficient. Singleton family attains bound. | Matrix version MM^T=I_m gives a right inverse for M, so rank M=m<=n. n0 permits no odd club; empty family valid. Repeated odd sets cannot satisfy the intersection hypothesis. All small binary families checked exactly, without real positive-definiteness. |
| combinatorial:lem:perp | Any field F, W<=F^n,n>=0: bilinear perpendicular space dimension n-dim W. | Basis rows of W form rank-d matrix M; Wperp=ker M and rank-nullity gives n-d. | Independently row-reduce the d independent equations: d pivots leave exactly n-d free coordinates. No positivity or direct-sum-with-W premise. W0/full space/n0 and isotropic(1,1) over F2 or(1,i) over C handled; coordinate bilinear form is nondegenerate even when self-products vanish. |
| combinatorial:thm:eventown | Distinct even subsets of[n], all intersections even: m<=2^floor(n/2). | Span W of incidence vectors is self-orthogonal, so d<=n-d by preceding dimension lemma; distinct vectors in W number at most2^d. Couples construction attains it. | Different matrix check: put a basis in systematic form[I_d B] by column permutation/row operations. Self-orthogonality gives I_d+BB^T=0, so B has rank d and d<=n-d. Count binary vectors afterward. n0 family{empty}, n1 only empty, odd n unused inhabitant and repeated-set hypothesis checked. All binary subspaces through dimension4 and14-plane/16-club model recomputed. |
| combinatorial:thm:fisher | n>=1,lambda>=1, distinct subsets with each off-diagonal intersection lambda: m<=n. | m<=1 direct. For m>=2, Gram G=diag(d_i)+lambda J, d_i=\|Ai\|-lambda>=0. At most one d_i vanishes; positive quadratic form forces kernel0 and rank m<=n. | Different determinant expansion: det(diag d+lambda J)=product d+lambda sum_i product_(j!=i)d_j, because any two selected J-columns are proportional. If all d positive this is positive; if exactly one iszero it is lambda times the other positive factors. This independently proves rank. m0/1 are direct and do not require d_i>=0. lambda0 fails for empty plus n singleton sets; n0 is outside stated domain. Crop/block prose now maps varieties to distinct incidence sets explicitly. |
| combinatorial:thm:twodist | Any subset of R^n,n>=0, at most two positive distances: size<=(n+1)(n+4)/2. | For finite points use f_i=(norm(x-ai)^2-b²)(norm(x-ai)^2-c²): diagonal evaluation b²c². Expand into norm^4,n cubic norm²xk,n(n+1)/2 quadratic monomials,n linear and constant, countD. Any infinite set would contain D+1 finite points. | Independently form the separated feature/evaluation matrices; their product is diagonal nonzero, so rank m cannot exceed the explicitD features. Check every homogeneous degree and that omitted norm² is already sum xk². One actual distance can be padded; empty/singleton/n0 allowed. The stronger affine-function bound is separately earned below, not falsely substituted for the original statement. Pentagon and simplex geometry checked. |
| combinatorial:thm:fwmod | Prime p, L subset Fp of size s, set sizes avoid L, off-diagonal intersection residues lie in L: m<=sum_i0^s binom(n,i). | Product over L of(v_i dot x-ell) is zero at other incidence vectors and nonzero at its own. Boolean multilinear reduction preserves values and degree<=s; diagonal evaluation gives independent polynomials in the stated monomial span. | Matrix feature check: coefficients in multilinear monomials and their evaluations multiply to the nonsingular diagonal matrix, so m<=feature count directly. Empty L gives at most one set; L all residues gives no sets. n0/m0/1, s>n binomial zeros, characteristic2 and repeated-set contradiction checked. For Oddtown the products have no constant, recovering n rather than n+1. |
| combinatorial:thm:fw | Distinct sets, finite L of s nonnegative integers, off-diagonal intersections in L, no individual-size restriction: same sum-binomial bound. | Sort sizes nondecreasing, use only factors ell<\|Ai\|. Own value is positive, and for j<i distinctness prevents Ai contained in Aj, so intersection is a selected root. Evaluation matrix is upper triangular with nonzero diagonal; multilinear reduction preserves it. | Adversarially check tied sizes, empty first set, size belonging to L, L0 and irrelevant large L-values. Evaluate a coefficient relation at columns in reverse order, recovering coefficients successively from the triangular diagonal. No mistaken symmetric/diagonal evaluation or modular collision is assumed. All small families are independently checked. |
| combinatorial:thm:explicitramsey | Prime p>=2; vertices are k=p²-1 subsets of[p³], adjacency intersection not -1modp: clique and independent-set sizes<=t_p. | Clique uses modular FW with L0..p-2, since own size=-1. Independent family uses actual intersection sizes p-1,2p-1,...,p²-p-1, exactly p-1 possibilities, then nonuniform FW. | Reconstruct the residue-to-integer list from0<=intersection<k and distinguish the two theorem hypotheses. p2 gives k3,8 ground points,t2=9. At p3, exact binom(27,8)=2220075 and t3=379. Separate elementary binomial product bounds prove superpolynomial vertex count in t_p; no equality/asymptotic lower bound for largest cliques or current extractor-record theorem is inferred. |
| combinatorial:lem:grid | Field F; finite coordinate sets, individual degrees below their sizes; vanishing on product grid implies polynomial0. | Nonzero f cannot meet a bound for an empty Si; zero f direct. n0 is a constant on the single empty tuple. Otherwise induct on variables: fix first coordinates and apply univariate root bound to every last-variable coefficient, then induct. | Different tensor-Lagrange reconstruction: for nonempty Si, products of one-variable Lagrange basis polynomials interpolate every polynomial below the individual bounds, so all grid values0 forces all coefficients0. Denominators are differences of distinct field elements, never the possiblyzero grid cardinality. F2/F4, n0 and empty grids explicit; exact F4 evaluation matrix has full rank16. |
| combinatorial:thm:cn | Field F,n>=0, nonnegative integer t_i, total degree sum t_i and nonzero target coefficient; each Si has size>t_i: some nonzero grid value. | Choose and rename finite(t_i+1)-point grids; replace each monomial by coordinatewise remainder modulo monic grid polynomials. Values preserved and individual degrees bounded. Any out-of-bounds monomial loses total degree, so target top coefficient cannot cancel; grid lemma gives a nonzero value. | Independent coefficient formula below uses product Lagrange functionals; it equals the top target coefficient and would vanish if all grid values did. Check n0, t_i0, finite fields and high exponents in other monomials. The exact coefficient formula is tested over F2/F3/F4/F5. No algebraic closure or characteristic-zero factorial assumption. |
| combinatorial:thm:cd | Prime p; nonempty A,B<=Fp: sumset size>=min(p,a+b-1). | Singletons direct. If a+b>p, A and c-B intersect for every c. Otherwise assume small sumset, enlarge to C of size a+b-2, product(X+Y-c) has target coefficient binom(a+b-2,a-1) nonzero because all factorial indices<p. CN contradicts vanishing on AxB. | Adversarial second reconstruction uses the explicit coefficient functional rather than the monic remainder proof to obtain the contradiction. Check factorial endpoints, singleton, a+b=p/p+1 and wrapping APs. Exhaustive nonempty pairs over p2/3/5/7 agree. Composite Z4 subgroup{0,2} gives2 rather than required3, so primality is essential. |
| combinatorial:lem:powersum | Prime p, integer0<=e<p-1: sum_Fp y^e=0, interpreting y0 as constant1. | e0 gives p ones. For e>0 root bound supplies a with a^e!=1; scaling the finite field sum gives S=a^e S and invertibility forces zero. | Different finite-difference proof: sum_y((y+1)^(e+1)-y^(e+1))=0 by permutation. Induction on e annihilates all lower power sums, leaving(e+1)S_e0; e+1<p is a unit. p2 only e0. e=p-1 gives-1, demonstrating the strict endpoint. General Fq extension uses the actual root/scaling argument and characteristic p, not this prime-specific finite difference induction. |
| combinatorial:thm:cw | Prime p,n>=1; polynomials with nonnegative degree bounds d_j,sum<n, zero polynomials and empty system allowed: p divides numberN of common zeros; origin implies another. | Indicator Q=product(1-P_j^(p-1)) has degree bound(p-1)sum d_j<n(p-1). Every occurring monomial has a coordinate exponent<p-1; its grid sum factors and that power sum vanishes, so N0modp. Positive N is at leastp. | Substantive adversarial reconstruction checks indicator values, expansion/cancellation, existence of a deficient coordinate, exponent0, integer-versus-field sum and every zero/constant/empty-system case. Original equations0,X in one variable (and zero equation at n0) falsify the degree-minus-infinity interpretation. Finite counts exhaust all ternary/binary3-variable quadratic forms. New finite-field outlook states exactly characteristic-p divisibility earned by the indicator, not unsupported q-divisibility. Original unqualified zero-equation domain is not certified. |
| combinatorial:thm:egz | Integer n>=1, any2n-1 integers, positions may repeat values: some n have sum0modn. | Prime case applies corrected CW to two forms of bounds p-1, uses nonzero solution and support size exactly p. Composite step extracts2m-1 disjoint n-blocks, divides each sum byn and applies m theorem to block sums; prime factorization terminates, n1 direct. | Genuinely different prime proof from Cauchy–Davenport below avoids CW entirely. Composite capacity is checked separately: before last block there are exactly at least2n-1 entries, after all blocks n-1 remain, and selected m blocks have mn distinct original positions. All residue multisets for n1..5 and sharp lists checked exactly. Negative input residues and all-zero coefficients do not change the proof. |
| combinatorial:lem:support | Finite A, any field F, dim-d subspace V of F^A: some vector has >=d nonzero coordinates. | Sum all d echelon basis rows; every pivot column has one1 and all other entries0, so all d pivots survive even in a small field. d0 choose0. | Independent coordinate projection onto d independent columns is an isomorphism V->F^d; lift the all-ones vector. Do not use a union-of-supports or generic-scalar choice invalid over small finite fields. All binary subspaces through dimension4, counts1/2/5/16/67, pass. |
| combinatorial:lem:diag | Finite A, field F, every c_a!=0: diagonal three-variable tensor has slice rank N=\|A\|. | Upper boundN coordinate slices. For r<N proposed slices, kill first-kind functions by h in an annihilator of dimension>=N-r1; support lemma gives h with that many nonzero coordinates. Contraction is diagonal rank>=N-r1, but remaining r2+r3 rank-one terms give rank<=r-r1<N-r1. | Adversarially reconstruct arbitrary coefficients/small fields and all three orientations. Contracting a y-slice really is f(y) times a z-function; likewise z-slices. Each c_a h(a) is nonzero exactly on h's support. No division by a zero coordinate, no infinite-field genericity and no false flattening-rank bound. Empty A/zero tensor rank0 are explicit, and r1<N follows from r<N. |
| combinatorial:thm:capset | n>=0,A<=F3^n with no three distinct zero-sum points: size<=3M_n. | In characteristic3, a repeated-point zero-sum triple is diagonal. The indicator product(1-(xj+yj+zj)²) has total degree<=2n and each exponent<=2. Priority partition puts every monomial into the first group with degree<=2n/3; collecting equal monomials gives at mostM_n slices per group. Diagonal rankN gives bound. | Reconstruct coefficient expansion and the priority assignment separately: total degree forces at least one deficient group and no term is assigned twice. Restriction to A³ preserves the decomposition. n0/empty A, diagonal coefficient1, cancellation and floor threshold checked. A different odd-characteristic AP extension is earned locally with x-2y+z, not the invalid reuse of x+y+z outside characteristic3. |
| combinatorial:prop:mn | n>=0,0<x<=1: M_n<=((1+x+x²)/x^(2/3))^n, hence M_n<=2.7552^n and cap size<=3 times that. | For counted a, x^(degree-2n/3)>=1; sum over all ternary exponent vectors factorizes. At x59/100 compare rational cubes exactly to(1722/625)³. | Independent generating-coefficient count of(1+z+z²)^n agrees with direct vectors n0..10; exact cubed inequalities verify the bound. Optimizing the rational cube gives r=(sqrt33-1)/8 and exact algebraic base c_*, bracketed by rational interval arithmetic, about2.755104613. Original named2.7552/.59 calculation already valid and is independently rechecked, not falsely claimed newly repaired. n0,x1 and x0 exclusion explicit. |

The independent CN coefficient functional is
sum_(s in grid) f(s)/product_i product_(a in Si,a!=si)(si-a).
For each coordinate, univariate Lagrange interpolation shows the analogous
functional is0 on powers below t_i and1 on power t_i. If a monomial of
total degree<=sum t_i exceeds one t_i, it must be deficient in another,
whose factor vanishes. Thus only the target monomial contributes, giving
its coefficient. All denominators are nonzero field elements. This proves
CN anew and independently checks the target-coefficient argument in CD.

For the independent prime EGZ proof, sort the residues b1<=...<=b_(2p-1).
Pair b_i with b_(i+p-1),i1..p-1, leaving b_(2p-1) alone. An equal pair
would give p consecutive equal residues and an immediate zero-sum p-block.
Otherwise each pair gives a two-element set. Iterated Cauchy–Davenport
makes their sumset, plus the singleton, all of Fp, so0 is obtained by
choosing one element from each pair and the singleton: exactly p distinct
positions. For p2 the same argument works directly. This does not reuse
the CW proof; the multiplicative block step afterward is reconstructed
adversarially with its exact capacity/termination checks.

## All exercises after actual answer comparison

Every first derivation is in APPC-PROMPT-FIRST. Supplied hints/ideas/write-ups
are each read after that record; there is no inherited mathematical sign-off.

| Key | Actual comparison and adversarial B | Grade |
| --- | --- | --- |
| combinatorial:ex:eventown | Supplied affine-plane kernel/direction proof matches first derivation; all14 clubs and120 intersections checked. Independent affine-word distance method uses earlier B16-word code and intersection identity to get0/2/4/8 counts. General couples construction includes odd n/n0; actual old write-up only specialized eight people, so retain general justification explicitly. No relabelling can create a two-person club. | 1 retained after concrete plane model is taught before the exercise |
| combinatorial:ex:nearpencil | Supplied Fano answer already defines/proves the vector-space model; the prompt's future V9 reference was unnecessary and is removed. Current prompt teaches points/lines locally. Count42 ordered pairs/6 per line and dimension1 intersections; independent exact seven-triple/21-pair enumeration agrees. Near-pencil n>=3 direct; n1 empty single block and n2 two nested blocks are explicitly included as degenerate cases. | 1 retained |
| combinatorial:ex:simplexdist | Actual answer correctly notes at-most-two and small n; adopt that convention in main definition. Squared distances4-2overlap, affine hyperplane sum2 and orthonormal identification earn all n. Independent centred six vectors for n3 are opposite unit vectors on three perpendicular axes, proving regular octahedron rather than inferring shape from a drawing. | 1 retained |
| combinatorial:ex:sdistance | Supplied product over actual distances gives diagonal nonzero evaluation and degree<=2s; stars-and-bars counts monomials. Independent feature-matrix rank bound agrees. r0/n0/empty/one-point/s0 and infinite-set reduction checked; final answer must explicitly extend the finite proof to infinite subsets. | 2 retained |
| combinatorial:ex:fwmodthree | Supplied p3,L1/2 substitution is correct. Independent direct degree-two polynomials(v dot x-1)(v dot x-2) have diagonal2, off-diagonal0; multilinear feature count1+n+binom n2. n0/1 and automatic distinctness included. | 1 retained |
| combinatorial:ex:cdsharp | Supplied interval-sum argument matches first derivation; nonzero difference gives no repeats beforep. Independently translate/dilate and enumerate all small lengths including full-field boundary k+l=p+1 and singleton. Z4 subgroup counterexample exact. | 1 retained |
| combinatorial:ex:egzsharp | Supplied zeros/ones proof is correct for n>=2. At n1 an empty list cannot provide one entry, so its sharpness also holds directly; replace vacuity language that suggested omitting it. Independently enumerate possible number of ones and exact small lists. | 1 retained |
| combinatorial:ex:quadric | Supplied solution already handles z0 before dividing and includes p2; no new denominator repair is claimed. Corrected CW uses bound2<n even for zero form. Independent odd-prime pigeonhole of square sets gives -1 as two squares, p2 direct. All64 binary/729 ternary coefficient forms in three variables have at leastp zeros and divisible counts. | 2 retained |
| combinatorial:ex:capplane | First parallel-class pair count(10 pairs vs8) and affine-normalization method are both independent of supplied answer. Actual answer gives third method: each line through a cap point contains another; lines through an outside point force an even total, contradict5. Every five-subset of nine points and the four-corner cap checked. | 2 retained |
| combinatorial:ex:dvir | Supplied rank-nullity/top-homogeneous argument is sound in positive dimension and already treats constant degree. Explicit n>=1 now earns K nonempty from a nonzero direction, fixing original n0 counterexample(empty K but claimed lower1). Reconstruct evaluation-map kernel, line root bound, leading coefficient and individual-degree grid lemma separately. Exact plane Kakeya enumeration over F2/F3/F4 gives minima3/7/10, satisfying the respective general bounds3/6/10; n1 full field and q2 covered. | 3 retained |

## Additional unnamed groups and disclosed curricular changes

APPC-U-BLOKHUIS earns the originally quoted affine-function refinement,
with full source proof. For n>=1 a relation sum c_i f_i+affine0 has
degree-four moment sum c_i0 and degree-three moment sum c_i a_i0.
Evaluating at all points, multiplying by c_j and summing gives
b²c² sum c_j²0, so every real coefficient0, then the affine polynomial0.
Thus adding n+1 independent affine functions to the earlier span gives
m<=(n+1)(n+2)/2. B: regard the two highest homogeneous equations as the
moment kernel; diagonal evaluation is positive definite on that kernel,
so the augmented feature columns have full rank. Check n1, repeated allowed
distance, positive b/c and real coefficients; n0 handled by its unique point.
The lower simplex-edge construction and this upper bound differ by at most
2n+1, earning their shared leading term n²/2. Exact plane/space classification
5/6 is not claimed from this general proof and is removed from caption/prose.

APPC-U-AFFINE-CODE proves the14-plane/16-word construction in full before
use. Its words are the affine functions on F2³, basis1,x1,x2,x3, so dimension4.
Even intersections give self-orthogonality and the perpendicular dimension
gives self-duality. B also identifies the conventional extended-Hamming alias:
puncture at x0. The3-by-7 matrix with columns all nonzero x in F2³ has rank3;
every affine word on those coordinates is in its kernel because sum x=0
and sum xx^T=0 over F2 (diagonal counts4, off-diagonal2). Both spaces have
16 words, so they coincide. The missing overall parity bit is a0, its value
at x0, giving the extended binary Hamming code. No later coding theorem needed.

APPC-U-ODD-CHARACTERISTIC earns the optional AP route over every odd prime
power q. Use x-2y+z=0 so the diagonal always contributes1, and invertibility
of2 makes a repeated-point solution fully diagonal. The q-1 indicator and
the same priority partition give3 times the count of exponents in0..q-1
of degree<=(q-1)n/3. B verifies each repeated-pair case, all exponents/
total degrees and Fermat/Lagrange field-unit fact separately. In characteristic2,
(0,1,0) is off-diagonal but satisfies the relation, so a no-three-distinct-AP
hypothesis cannot justify a diagonal tensor. Main source and bibliography
now state odd characteristic for this extension.

APPC-U-OPTIMUM derives the rational-cube derivative and uses the actual
earlier MVT proof on positive closed subintervals. The unique positive
quadratic root lies in(0,1), giving the global minimum; rational brackets
0.5930703308172535<r<0.5930703308172536 bound its cube without numerical
guesswork. The named2.7552 bound was already correct; unqualified exact growth
claims using the shorter rounded2.7551 are removed. Probability interpretation
uses finite uniform digits only, with Mn/3^n <=(574/625)^n and cap fraction
<=3 times that. No future Chernoff theorem supplies a premise.

Other groups actually read/reconstructed: clubs/opening independence; bilinear
field conventions; lambda0 counterexample; explicit crop-incidence map;
total/individual degree definitions; finite evaluation matrices; Boolean
multilinear reduction and monomial counts; homogeneous-set graph specification;
integer binomial growth estimates; univariate root bound/finite grids;
field-indicator integer count; matrix-rank/product/subadditivity; cap-card
coordinate/affine-line identification; finite point-basis/support; and source
counted code/geometry examples. Keyed global exposition/history/context approval
still requires its own pass; this record does not autoapprove those rows.

The source removes the unproved small-dimensional cap table and exact20-card
classification, strongest/current cap lower records and extractor/Borsuk
classification/record catalog. Those are genuine disclosed losses of incidental
outward statements, not hidden weaker replacements of a named theorem.
The replacement route supplies complete general upper bounds, explicit2^n
lower cap, full plane maximum4, complete stronger two-distance refinement and
odd-characteristic extension, while preserving all18 named and10 graded targets.
The Fisher dated anecdote is replaced by its exact incidence interpretation.
All old/new losses and publishing-claim reconciliation needs are in the
curricular JSON; no exact classification or new research proof is certified.

## Actual figures, output scope and written voice

Pentagon source: all5 radius1.6 coordinates, all10 unordered edges, short/long
colour classes and distances recomputed by roots/trigonometric coordinates
and independent difference lengths, accounting for3-decimal rounding. The
caption now distinguishes five-point construction, nine-point first upper
bound and six-point proved refinement, without claiming exact classification.
Cap plate: all36 coloured points, four parallel classes of three lines,
all9 right-panel black/white points and all5 panel labels/coordinates checked.
Slope2 is read modulo3, not as unwrapped Euclidean segments. Four black corners
give the actual proved maximal cap. Narrow digital label legibility remains
an actual-output check, not approval from source/PNG generation.

The immutable1b94857e snapshot predates every C/reference repair. It has502
reading/501 print pages,KDP502,spine1.1782in and same-build wrap. Actual EPUBCheck
and output checker pass. Actually opened/read full print442/443 colour at1.65:
abelian determinant end, complete4-by-4 identity, nonabelian block map,
regular determinant and full generic irreducibility proof, all displays,
subscripts and final text fit. No grayscale/digital/all-page approval or
transfer to new pages claimed; source internal 'earn' wording remains a
global cadence cleanup item. A corrected three source chapter references
separately reopen affected A evidence; see exact source-order record.

Whole-chapter written pass follows concrete clubs to parity/rank, distances
to polynomials, explicit graph, sumsets/zeros and SET tensor counts. Replace
repetitive proof summary and stock never-estimates/greatest-triumph closing
with actual objects and spaces; the next question is constructing orthogonal
sign rows from fields. No human/spoken read-aloud claimed. Artin quotation, attribution metadata and remaining historical claims still need primary-source
closure in the global pass; bibliography read is not metadata verification.
