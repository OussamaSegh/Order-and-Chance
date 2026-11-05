# Conceptual prerequisite and story ledger

Current V3-038: all twelve main chapters and four appendices have fresh core
A/B evidence and855 global item decisions. All393 label occurrences and all88
literal earlier contexts are classified. All120 first-use chains reviewed;
all120 whole-volume later-use chains remain pending.All855 global rows now have explicit domain/claim and fullCORE fields;the strict
accepted-evidence gate rejects missing substantive fields. The historical
table below does not override current keyed source/evidence records.

| Concept | Definition/example before invocation | Actual proof location read | First valid use / correction |
| --- | --- | --- | --- |
| Group, subgroup, cyclic, element order | V1 complex-roots def:elementary-group, square turns and integer subgroup; V3 def:group and subsequent definitions | V1 roots prop:roots; V2 divisibility prop:subgroups, full minimal-positive-element proof | V3 C1 first rules and cosets. Opening no longer says the earlier volumes avoided the word group. |
| Residue ring, unit, field, Fp, phi(1)=1 | V2 congruences definitions before prop:ringZn and prop:units | Actual proofs of representative independence, integer laws, Bezout inverse criterion, field iff prime and modulus1 exception | C1 numerical groups, Wilson and matrix exercises. New field reminder precedes the first arbitrary-K matrix example. |
| Integer division, Bezout and Gauss cancellation | V2 divisibility thm:div, thm:bezout and thm:gauss | Read complete nonnegative-remainder existence/uniqueness, subgroup generator argument and Bezout multiplication proof | C1 least positive period/subgroup exponents, order-of-power formula; negative exponents and zero exponent retained. |
| Basis, dimension, invertible matrix, determinant | V1 linear algebra vector-space/exchange/rank-nullity definitions/proofs; thm:det | Read exchange substitution, basis extension, kernel/image basis count, alternating determinant formula/pair cancellation, product and invertibility proofs | C1 explicitly explains why the algebraic proofs transfer to arbitrary fields. Geometry/inner products remain real. |
| Eigenvector, characteristic polynomial, similarity | V1 linear algebra reduction reminder, prop:charpoly, thm:diag | Read determinant root criterion and Lagrange-polynomial eigenspace decomposition; they use only field algebra when the polynomial splits | C1 pb:matrices2 supplies its own 2x2 Cayley-Hamilton, cyclic basis, commuting matrices and equal-coset count. No later CRT, finite extension or orbit-stabilizer premise remains. |
| Roots of unity/geometric orthogonality | V1 complex-roots prop:roots and prop:orth | Read exponential parametrization, distinct-root count and finite geometric sum including n divides j | C1 dihedral vertex average and local cycle-walk detector. n1 and zeroth powers treated explicitly. |
| Polynomial root bound in a field | V1 polynomials prop:polydiv and prop:rootsfactor(a,b) | Read degree descent, division uniqueness, cancellation of distinct root factors | C1 ex:fieldcyclic also gives the short root-factor induction locally. Repeated roots/positive characteristic do not invalidate a distinct-root bound. |
| Finite probability, independence, expectation | V1 probability independence definition and prop:varsum(a) | Read joint mass factorization and the actual finite double sum proving product expectation | C1 random-walk prompt now defines independent symmetric increments and multiplication convention; local derivation never invokes infinite probability. |
| Cauchy-Schwarz/Euclidean norm | V1 inequalities thm:cs | Read the nonnegative quadratic/discriminant proof, zero list and equality cases | C1 sum-of-squares/translation contraction. Finite norms are defined in the solution. |
| Fibonacci gcd | V1 sums ex:fibgcd complete solution | Read addition-identity induction, consecutive gcd descent, index gcd descent and n0 boundary | C1 pb:fibdivides may legitimately use this proved earlier exercise, not merely its prompt. |
| Homomorphism / kernel | V3 C1 isomorphism definition now names operation-preserving maps first; C2 introduces kernel/image | C1 f(e), inverse and inverse-map checks read/reconstructed | C1 cube exercise proves equal-image injectivity directly; no undeclared kernel or later first isomorphism theorem. |
| Sign, normality, quotient operations and later concepts | Actual V1 sign and full C2 local proofs read; first-use chains recorded in concepts.json | No availability inferred from historical rewrite status; every later occurrence remains subject to global continuation | C2 representative independence before iso1/23; actions and later concepts have full named/exercise readings, with global closure pending. |

Story checkpoint: the merged V2 field guide ends with powers modulo7, Gaussian
factorization and chi4's multiplication rule, then names V3's exact title/subtitle.
V3's preface begins with that chi4 example and C1 asks what rotations and residues
share. C1 earns equal-sized cosets and cyclic groups; C2's incoming question is
which operation-preserving maps can forget entire cosets while retaining a group.
The current V3 afterword derives the two-state walk and names V4 *Chance: The Logic
of Uncertainty*. The actual V4 preface and counting/probability-space opening were
read; its own admitted later analysis is not permission for a missing V3 premise.

Source drift is guarded by the hashes in `prerequisite-sources.json`. A changed
earlier file reopens the affected proof-site evidence; it does not inherit review
from a title, citation, exercise prompt or prior audit.

## V3-003–005 additions

- C2 defines kernel/image and normality before quotient operations; quotient
  representative independence precedes every isomorphism-theorem use. Aut(N) now
  has a defined operation/group proof before semidirect products. Infinite cyclic
  characteristic-subgroup argument uses generator images +/-1, not order counts.
- C3 now proves finite cycle decomposition before weighted Burnside. Matrix
  exercises quantify over a given finite field, not assumed existence at everyq.
  Quotient vector operations, basis dimension and subspace correspondence are
  proved locally. Fitting stabilization, GL0 and nilpotency-index bounds are earned.
  Landau's small-case classification now proves the order-six case using Cauchy,
  a normal index-two subgroup and conjugation; no later classification premise.
- C4 uses the actual earlier V1 sign proof, C2 normal quotients and C3 orbit counts.
  The fifteen-puzzle enlargement argument uses earlier A4/no-order6 and local
  ordered-pair transitivity, not the later An theorem. The simplicity proof uses
  only its earlier generation/conjugacy arguments and explicit commutators.
- C4 prime cyclotomic field reminder uses actual V1 polynomial prop:gausspoly,
  thm:eisenstein, ex:eisen(b) full solution and prop:polynomial-bezout proof. It
  earns Q(zeta), inverses and sigma_a directly before the discriminant prompt.
  V2 thm:eulercrit's actual generator/square/half-power proof was read for sign
  checking; V1/V2 roots/finite-unit field arguments remain the earlier foundation.
- C4 probability product needs only nonnegative real series and finite partitions;
  finite-subsum exhaustion replaces any unproved later measure-theory theorem.
  Explicit elementary exponential/logarithm bounds and finite geometric tails
  control the decimal. The stronger asymptotic is outlook only.

These rows do not close the still-pending exact forward-context register or
later chapters. All qualifying changes in printed order must reopen relevant
first-use/context evidence; reference distance alone cannot approve a premise.

## V3-006 additions

- C5 finite G, prime p, p-adic factorization and a0 case now precede the Sylow
  definition. Mod-p polynomial arithmetic and characteristic are explained before
  the binomial argument. Normalizer is earned as a conjugation stabilizer.
- Existence is proved before containment/conjugacy, which precedes the congruence.
  Applying conjugacy within a normalizer in the congruence proof uses the already
  proved part(b), not the congruence itself. Cauchy/center come from actual C3.
- C5 pq classification uses V2 ch05-primitive-roots thm:cyclic, whose actual proof
  was reread: root counts N(d)=0 orphi(d), summed deficits force equality. This is
  now hashed in prerequisite-sources.json. C1 subgroup-of-cyclic and C2 semidirect
  construction earn action classification/existence/uniqueness.
- Solvability is defined before closure proofs and derived-series exercise. A5
  perfectness is defined only after A5'=A5. Simple abelian C3 is distinguished.
  Characteristic-zero radical criterion and deep finite-group results are outlooks,
  never premises. No future theorem used to obtain the order12 classification.

Story: C4 asks which permutations admit normal reductions and proves alternating
simplicity. C5 uses actions to force prime-power subgroups, then tests whether
normal reductions reach abelian pieces. C6 changes the operation: congruences
and polynomial remainders lead from quotient groups to quotient rings. The actual
C6 opening/prerequisite route is the next reading; this bridge is provisional.

## V3-007 additions

- C6 ring/domain/field explicitly distinguishes the zero ring. Additive quotient
  tools from C2 earn all-ideal quotient rings including the unit ideal; prime and
  maximal tests still require proper ideals. Product-ring example has its needed
  both-nonzero factors, with zero-factor isomorphism described.
- C6 fraction field is constructed and verified locally: equivalence relation,
  operations, representative independence, laws, inverses and injection of R.
  Gcd prime-exponent/content scaling facts are proved before primitive rescaling;
  no circular appeal to the product-content lemma. PID factorisation termination
  uses ascending ideals and a union generator, never a Euclidean norm on allPIDs.
- Actual V1 ch03 thm:lagrange construction/uniqueness, prop:gausspoly least-index/
  denominator proof, thm:eisenstein least-index proof and prop:reduction leading
  coefficient proof reread. Stale Chapter7 pointers corrected to3. General UFD
  Eisenstein earned locally.
- Actual V1 ch05 prop:early-differentiation product/linearity/chain proofs read;
  C6 repeated-factor interpolation uses only polynomial division and derivative,
  not an unstated Taylor theorem. V1 ch06 derivative rule source was followed to
  its actual earlier proof, not accepted solely by its backreference.
- Actual V2 ch10 prop:eucl rounding proof read forGaussian/Eisenstein/sqrt(-2)
  rings; V2 ch06 thm:eulercrit multiplicativity proof reread for X4+1 reduction.
  Given-field polynomial division and degree descent earnK[X]Euclidean; no new
  future theorem. Pointwise all-function example avoids a continuity premise.

Story: C6 diagnoses the failedfactorizationof6, then ideals/quotients translate
prime/maximal questions, then distinguishes ED/PID/UFD and earns polynomial
factorisation. C7 can now ask what a matrix of relations over a PID can encode.
Its actual full route is next; no C7 prerequisite approval inherited.

## V3-008 additions and curricular migration

- C7 now defines module subobjects/scalar quotients, finite direct sums and
  polynomialP(A)action before invocation. Rank proof explicitly concerns finite
  bases and extends actual inverse matrices to C6's proved fraction field.
- Smith uses PIDBezout and finite irreducible-factor descent (or C6ascending-ideal
  termination), not a general Euclidean norm. Minors' invariance covers arbitrary
  invertible row combinations, including Bezout2rowchanges. Delta0/zerorank
  and matrixdimension0 explicitly handled.
- Torsionclosure and R/p scalar structure of layers are earned before uniqueness.
  Presentation byXI-A precedes local annihilator-ideal/minimal-polynomial
  definition, companion form and Cayley–Hamilton; no use in own proof. Jordan
  notation is introduced before invocation. n0meansmu=chi1andemptyblocks/basis.
- ActualV1 ch03 thm:dalembert global-minimum/first-nonconstant-term proof read
  for complex splitting. Its closed-disc argument explicitly derives a convergent
  subsequence in real and imaginary coordinates, rather than assuming a later
  multivariable compactness theorem.
- Kronecker triple pb:kronecker moves intact C7->C10 after ex:phin, whose actual
  solution was read: prime raising via reduction/squarefreeX^n-1 forces all
  primitive roots into the minimal polynomial. Full C8–10 dependency audit still
  pending; this read is not whole-chapter approval. Partc now elementary C6Gauss
  divisibility/leading coefficient, eliminating C11closure premise. All old/new
  syntheticIDs mapped in V3-008-curricular-migration.json; no approval transferred.

Story: C7 answers the two opening questions through integer/polynomial modules,
then distinguishes rational form from Jordan's splitting requirement. C8 asks how
to obtain fields in which irreducible polynomials gain roots. The moved Kronecker
problem will join that later field route after cyclotomic irreducibility has
actually been earned. No mathematical part was removed to avoid the dependency.

## V3-009 — field route and constructive/inseparable boundaries

- C8 finite tower proof first derives finite bases/spanning sets when M/Kfinite,
  so it does not silently use arbitrary infinite-basis existence. The conditional
  assertion for given bases remains valid. R/Qinfinite earned from arbitrarily
  largeEisenstein degrees after simple extensions, not a cardinality premise.
- Characteristic0/p and the rational/prime-field embeddings taught before first
  general characteristic invocation. Formal derivative/productrule are local;
  X^p-tirreducibility earned by C6generalUFD-Eisenstein, not a future theorem.
- Splitting-field existence precedes extension lemma, which precedes counting/
  uniqueness. Countstrictlysmallerthan degree ininseparablecase is explicitly
  probed. Primitive theorem uses priorchar0distinctroots andbase-fieldBezoutgcd,
  not general Galois correspondence. Degree1/emptygeneratorlist handled.
- ActualV1 ch00 Cantor power-set challenge/fullanswer read. It proves no set
  surjects onto its power set, but does not itself connect that result to reals.
  C8supplies convergentternarysubsetencoding/injectivity and the diagonal
  argument, plus explicitinteger-polynomialenumeration for countability.
- Straightedge/compass rules explicitly require distinctpoints/isolated
  intersections; perpendicular construction uses already known radii, no
  circular large-distance assumption. Tower criterion covers tangency/parallel/
  coincident cases and emptyquadratic towers. Prime polygons use actualV1
  primecyclotomicshiftEisenstein, staleChapter7 pointer corrected3.
- ex:primitive old duplicate theorem is retained as the complete named theorem;
  new three-star exercise asks a finitecandidatebound, explicitrecovery and
  positivecharcounterexample. Monomialbasis and an independentdoubleEisenstein
  tower provep²degree; everyelement'sp-thpowerinK bounds simpledegree<=p. All
  fractionfield/UFD/binomial/prime-unit tools already earned, no C9premise.

Story: C8 constructs rootfields before discussing their symmetries, counts
embeddings with the repeated-root limitation visible, and relates quadratic
towers to actual geometry. C9 now asks what these constructions produce over
finite fields; characteristicpbehaviour has an earned example and a boundary.

## V3-010 — finite fields and local coding/trace tools

Read actual V2 ch04 definition and multiplicativity of μ, `prop:conv` full
finite-factor-pair/triple proof, and `thm:mobius` prime-power cancellation and
convolution inversion. C9 count inversion therefore uses an actual proved tool.
Read V2 ch06 `thm:gausslemma`, `cor:two`, `lem:eisenstein`, `thm:qr` including
the signed-residue, factorial cancellation, parity and lattice-count arguments;
the Euler-criterion proof was read earlier. These earn the precise Fibonacci
and Lucas–Lehmer applications. Added the arithmetic-function source hash;
reciprocity was already hash guarded. No exercise prompt or bibliography entry
was treated as a proof.

C9 distinguishes field-generating and multiplicatively primitive elements.
Relative q-Frobenius and its degree/order/count are now explicit before use;
the characteristic remains p. Finite-field existence precedes irreducible-count
positivity, so those arguments are not circular. All n≥1 restrictions and the
RS1≤k≤n≤q contract are stated; t=0 and fewer-than-t errors are earned.

The Moore solution explains independent indeterminates and the fraction field
of the C6 polynomial domain before using it. Empty determinant and zero subspace
are handled. Binary trace values are proved to lie in F2 before being bits;
the nonzero-polynomial proof works when Tr(1)=0. No future trace theorem supplies
a premise. AES irreducibility is proved locally using the already earned
factorization theorem and a complete polynomial identity.

Story: finite root fields answer C8's construction question, then polynomial
root bounds earn error correction. C10 will generalize the observed finite
symmetry/subfield pattern; its correspondence is mentioned here only as outlook.

## V3-011 — Galois route, real-root tools and complete radical steps

Read actual V1 ch05 `prop:seqcrit` peak/subsequence and adjacent-sequence proofs,
elementary differentiation, IVT bisection, EVT subsequence and Fermat/Rolle/MVT
proofs. These supply exactly the sign-change/root-count arguments in both
quintics; no later analysis volume supplies a premise. The source was already
hash guarded. Reopened actual C5 `cor:pk` full central-quotient induction and
`prop:solv` full subgroup/quotient/extension proofs and S4 series for the group
steps. Earlier C8 splitting-isomorphism extension proves each conjugate exists
in the radical envelope; it is not inferred from the word normal.

Moved the entire ex:phin prompt/hint/solution into the cyclotomic section before
the general degree, full polygon converse and later problems. Stable keys and
all three parts remain. Its Gauss/reduction/squarefree proof uses only C6–9;
later work no longer treats an exercise prompt as a proved tool. A focused
ordering regression fails on the old location and passes on the move.

The correspondence is proved under the existing K⊆L⊆C contract. An explicit
Fp(t^(1/p)) example shows why the same splitting-field equivalence would fail
without separability outside that contract. Restriction maps are earned before
quotient claims. Radical envelope ordering supplies every previous conjugate;
successive Galois steps need not all be normal over the initial field. Empty
towers, repeated group-series terms and termination are now explicit.

Niven's full prompt/solution remains, with monic cosine recurrence/rational-root
proof replacing future C11 algebraic-integer closure. Ramanujan's heptagon cubic
is derived locally; a false claim that it was derived earlier in C10 is removed.
Kronecker now explicitly earns eigenvalue multiplicities of companion powers
through the actual C7 triangular/Jordan result. Main future Dedekind reduction
comparison is a marked outlook after the complete local finite-field argument.

Story: C10 answers which splitting fields admit radical towers, including the
precise quintic obstruction, then asks how arbitrary groups act by matrices and
what traces remember. This matches the actual C11 opening, which was read.
Langlands/Shafarevich/current-open-status catalog is replaced by that earned
transition plus a posed inverse-Galois further-reading question; no theorem lost.

## V3-012b — closure of the Chapter11 prerequisite repairs

Read all remaining actual hints/answers and the full figure, then reconstructed
the revised arguments twice; CH11-REVIEW.md records every key. The final problem
now earns the full original Sn real-form and degree-sum claims with a signed
involution representation and independent square-root cycle count. Locally
define dual space/action and prove irreducibility by annihilators, construct the
symmetric/skew matrix spaces, and prove the real-form criterion using an
antilinear involution. No undefined tensor/Specht construction or quoted Young
theorem supplies a premise. The complete original/new target disclosure is in
V3-012b-frobenius-schur-augmentation.json; no mathematical conclusion is lost.

Reopened V1 ch03 thm:dalembert's actual minimum/subsequence proof for complex
eigenvalue existence in Schur, not just its title. Earlier whole-file hashes
already guard it. C7 squarefree-annihilator diagonalization, C5 derived-subgroup
proofs, C9 thm:cyclicmult and C10 worked ex:phin supply the remaining finite
linear/group/cyclotomic tools. Read actual V1 ch06 Taylor proof and the integral
toolkit: the latter explicitly names integration existence as a contract whose
construction is in V7. Supply the required fourth-order log-cos estimate locally
with four applications of earned Rolle, avoiding that future construction.

The S4 cube character is checked from the actual edge/face/vertex rotation
angles and permutations; A5's figure is an explicit preview of its fully worked
exercise. Its degree5 character is an actual Maschke complement after both
multiplicities are computed. Algebraic conjugate phi' is real; complex bar notation
was misleading and is removed. GL2Z's finite O2 classification is proved locally,
including one-reflection and Klein cases, before the C12 spatial classification.

Actual V4 Chance main/opening and ch08-markov model/cutoff text, and V11 Randomness
shuffling model/cutoff source, were read for the marked outlook. Both use two
independent uniform positions with a holding step1/n. They supply no V3 premise.
The revised ending motivates actual C12 rotations/quaternions. Whole-book first-use,
unnamed/dependency occurrence and history registers still have a separate gate.

## V3-013a — rotation core, with analysis workshop still pending

All C12 source/hints/answers/figures are now read. CH12-PROMPT-FIRST.md discloses
hint/first-answer exposure and one first-reconstruction event-count mistake;
CH12-CORE.md closes four named results and first seven exercises. Actual V1
linear algebra does not introduce cross products. Define their coordinates
locally, prove scalar/triple/norm identities, and earn SO3 preservation before
quaternion rotation arguments use them. Define SO3, quaternion length and left
ideals at their first local use; distinguish division rings from fields.

The kernel-two homomorphism is upgraded to an actual topological double cover
by explicit positive-real trace/skew inverse charts and translations. Path and
square-family lifting are constructed with a finite uniform grid. Actual V1
ch05 prop:seqcrit and thm:heine proofs were read; their finite-coordinate square
extension is supplied locally. S3 simple connectedness is proved by short-chord
approximation, a puncture outside finitely many proper planes, stereographic
coordinates and contraction; endpoint signs then earn pi1SO3=C2. No later topology
or unproved connectedness supplies a premise. Original loop/plate conclusion
is preserved, with an additional explicit based two-turn contraction.

Earn regular-solid attainability using explicit tetrahedral12 and icosahedral
60 rotations; checking an upper bound alone is insufficient. Exact vertex,
supporting-plane and order5 computations support the general finite argument.
Earn geometric conjugacy with actual C11 character tables/Schur and real
intertwiner normalization, rather than invoking an unproved polar decomposition.
D2/Klein, zero and antipodal cases are explicit. Reopen actual V2 ch07
thm:foursq full pigeonhole/first-multiple proof for Hurwitz's prime step; its
whole-file hash is now guarded. Correct noncommutative left/right coset and
ideal wording. No named mathematical target removed or weakened.

Eight C12 workshop problems still need full prerequisite/correction closure.
In particular V1's integral existence contract does not prove their Riemann-sum
limits, and a tool merely deferred to V6 cannot justify the abelian-group error
term. Supply finite/local convergence and integral arguments next. The C4/C12
smallest-simple claim also exposes an unproved finite-order assertion in C5;
earn the finite proof during global closure. Those are pending findings, not
approved outlook premises. Whole-book keyed occurrence/history/voice gates remain.

## V3-013b — main workshop and finite minimum-order closure

CH12-REVIEW.md closes all eight workshop problems with final exact domains and
separate A/B. Actual V1 thm:mvt and prop:seqcrit are reopened again; local Lipschitz
tagged sums construct every needed proper integral, and explicit logarithmic
tail estimates construct the unit-circle improper cases. New Jensen partd earns
the previously unproved extension and all integer zero-mean factors. No later
integral construction is a premise. Exact old/new statements and lost connections
are in V3-013b-curricular-disclosure.json, with all original targets retained.

Finite geometric/positive-family estimates earn Euler products and square-root
average error without future partial summation. Reopen actual C7 cor:abelian
full proof; source coefficient comparisons are finite factorizations, not an
unproved Dirichlet-series uniqueness theorem. Sylvester uses actual adjacent
sequences; an independent tail proof and high-precision bounds recheck rounding.
Reopen C9 ex:powersums actual proof before the general systems argument. Correct
zero-equation degree arithmetic by nonnegative bounds/m>=1, and n1 sharpness.

The full central-walk formulas now retain all zero modes at t0, so the target
is every nonnegative integer time; only shorter corollaries require positive
time. Old zero-time failures and all60-state exact checks are permanent. The
first24-vs12 event error belongs to the initial reviewer reconstruction, not
the original supplied answer. Old printed Theorem12.5 was correct; stable-label
changes are not a claimed numerical-reference defect.

V3-013b-SMALL-SIMPLE.md reconstructs the complete new finite C5 proof twice,
including all27 table orders/six exceptions and simple-order60 actions. It uses
only the actual earlier S4 series, Sylow/count/coset and extension proofs. C4's
minimum-order remark is a preview, C12's use is now earned earlier. Category/
functor examples are defined/proved locally; normalization/interpolation earns
its nonzero denominator. Unproved outward homology/polytope links are removed
with explicit loss disclosure, while every named/exercise target remains.

All four appendices and global keyed unreferenced/concept/history/voice evidence
still remain. This ledger distinguishes available proofs from inventory approval.


## V3-014: actual finite analysis and spectral appendix contract

Reopened actual V1 ch05 prop:seqcrit246–265 and thm:evt435–445, V1 ch03
thm:dalembert151–166, V1 ch07 full thm:spectral378–403 and projection350–365,
and C7 Jordan cyclic construction795–825. Earlier whole-file hashes remain
identical. APPA-REVIEW records the actual argument, not availability inferred
from a title. Supply coordinatewise finite Delta/K sequential compactness
before the variational maximum; supply the finite-minimum continuity and
triangle equality case. Jordan binomial powers and polynomial/geometric
absorption are earned before rate claims. Zero blocks and empty non-Perron
spectra are explicit. No Banach/Birkhoff sharp contraction premise is imported;
prove the metric on positive rays and disclose removed incidental catalog.

The full cyclic-level proposition is moved before its first Frobenius use.
Closed walks decompose by strictly decreasing length into finitely many simple
cycle lengths, earning Bezout; finite gcd selection also strictly decreases a
positive integer. Define period only when a positive cycle exists. Handle [0]
separately rather than certifying the original unqualified primitive equivalence.
A positive power proves reachability before any use of irreducibility.

PageRank's main1-norm contraction now precedes its numerical use, without
borrowing the later exercise. The exercise adds arbitrary possiblyzero v and
Cauchy existence/uniqueness. Leslie's main Euler–Lotka equation is derived from
survival rows before the later full characteristic-polynomial exercise. Its
last positive fertility block earns existence without Descartes or a future
analysis theorem. Bipartite full spectrum uses the actual earlier *real*
spectral theorem, all kernels/ranks/zeros supplied. Uniform shuffle conclusion
requires the explicitly stated fixed random position-permutation model.
Global keyed context/first-use/exposition closure still remains a separate gate.


## V3-015: finite Fourier/spectral/code route and full nonabelian determinant

Reopened actual C11 Hermitian/orthogonality/regular-decomposition and radix-two
proof sites, plus C6 Gauss primitive/denominator/UFD/multivariable proofs.
APPB-REVIEW lists exact reads and reconstructs the imports. Define normal,
adjoint and unitary before invoking them; align Hermitian convention linear
first, and explicitly distinguish the appendix unnormalized transform from
C11. Earn arbitrary-n FFT count by local padding/folding, no stale future V5
premise. Character completeness is checked both by commuting translations and
actual earlier finite abelian structure; dual row orthogonality uses the square
matrix inverse, not an unearned bidual identification.

Replace essential future Volume8 Hoffman premise by the full finite local
indicator/eigenvalue proof; square coset multiplication earns clique bound
before use. Define strong regularity before its caption. Prove generalized
binomial degree/leading term, generating identity and K totals before LP
boundedness invokes them; closure of distance algebra comes from actual pair
orbits. Nonempty distributions/d>=1/n0/singleton/empty conventions make every
division and finite maximum valid. Full nonabelian factorization and polynomial
irreducibility are now actually earned by algebra-block coordinates and generic
determinant induction from earlier Gauss, rather than assumed from C11's square
sum. The report independently reconstructs Phi inverse from actual matrix-unit
orthogonality. No future optional route supplies an essential premise.

Named/exercise status is separate from the810 remaining keyed global exposition/
history/voice rows and occurrence/context classifications. Unsupported incidental
research record/catalog claims are removed with explicit losses; surviving
outlooks and attributions still need global primary-source closure.

## V3-022: C4 complete conceptual/prerequisite continuation

Read actual V1 sign164–173, polynomial division/Bezout127–132, Eisenstein327–338
and **ex:eisen(b)**678–685; counting36–42/69–74; completeness85–87,seqcrit246–255,
positive-series554–585,safe-sums668–675 and Taylor168–218/exp-series772–774.
Read actual V2 primitive-root133–160,Euler55–117,supplementary2 at202–209.
Exact paths/reconstructions are in GLOBAL-CH04 and earlier-references.json.
The cyclotomic reminder constructs its particular field and exponent automorphisms
before the challenge; no later extension/Galois theorem supplies a premise.
All22 actual C4 label uses classified;5 singular earlier references classified,
including hints/full solutions. Three new first-use chains (prime cyclotomic
field, root discriminant, limit inferior) are source-anchored. Existing simplicity,
commutator, sign, cycle and convergence chains have explicit C4 continuation.
All58 whole-volume statuses remain pending. Actual V11 appendix law/theorem/
corollary located and relevant text read solely to check an outlook promise;
that result does not supply an essential premise in V3. Backward label counts do
not substitute for the full unreferenced written/proof pass.

## V3-023: C5 complete conceptual continuation

34 actual label occurrences individually classified, including figure/caption,
hints and complete solutions; one actual earlier V2cyclic-unit invocation traced
to its full proof133–160, reread and unchanged hash. Complete C1/C2/C3/C4 proof
sites specified in GLOBAL-CH05, with no inference from exercise prompts. Sylow
finite conventions includea0/m1/G1. Solvability closures and derived criterion
allow arbitrary ambient groups with finite chains. Free action, normalizer,
cyclic logarithm and perfect-group definitions/proofs/examples now have dedicated
first-use chains. Sylow/solvability priority chains closed throughC5 only; all62
whole-volume statuses pending. New prime-power projection is proved from actual
power-order and CRT results locally, not supplied by the future outlook. Full
proof and solution source items are anchors where the definition lives there.

## V3-024: C6 global conceptual continuation

All17 actual local label occurrences and6 literal earlier mentions classified
individually. GLOBAL-CH06 records precise full V1/V2 proof reads, including
integer CRT, polynomial division/interpolation/Gauss/Eisenstein/reduction,
Gaussian/Eisenstein rounding and multiplicative Legendre symbol. Unreferenced
arguments also reconstructed: arbitrary generated ideals, monic evaluation
kernels, associates/zero, I² identity, arbitrary PID ideal-chain termination,
fractionfield equivalence/laws, scalar/content uniqueness, general Eisenstein,
and bounded coefficient reconstruction. No backward-reference scan substitutes
for this reading. Two priority ring/ideal first chains plus six new chains
(PID/ED, prime/irreducible/UFD, fractionfield, content/Gauss, idealCRT/interpolation,
local four-element field) have exact hashed anchors. Smith combined-chain global
closure remains C7 work. All68 whole-volume conceptual statuses remain pending.

S proof needs only already-known complex division and integer rounding; its
four-element quotient's inverses are explicitly computed before the half-lattice
case invokes them. Its arbitrary-ideal minimality and arbitrary-Euclidean-function
obstruction are proved separately. The later abstract fractionfield, finite-field
existence/classification and number-field ideal theorems supply no premise.

## V3-025: full C7 prerequisite continuation

All17 local label occurrences and4 literal V1/V2 mentions manually classified.
Actual V1det177-204/cofactor220-230/complexFTA156-174/recurrence317-321 and
V2Bezout95-100/CRT153-161/characterrestriction54-65 full relevant proofs reread;
C6 arbitraryPID/Frac/Gauss/CRT/newcounterexample provide current local tools.
C7 supplies commutative-ring determinant/adjugate transfer explicitly. General
Smith uses proper-divisor factor-count descent, not Euclidean size; no elementary
GL-generation premise. Arbitrary relation submodule finite basis earned by
subfree induction before finite presentation; intrinsic torsion layers earn
uniqueness over infinite residue fields too. Presentation precedes CH and does
not assume it. Minimal polynomial/companion/zero dimension before use, Jordan
splitting explicit and complex case supplied by actual earlierFTA proof.

Module/Smith priority first chains and5 new torsion-filtration/annihilator-
companion/canonical-form/exponent/topology-outlook chains have precise hashes.
The topology chain reviews its explicit external-outlook role and conditional
algebra; it does not certify a locally proved geometric model or supply a premise.
All73 whole-volume concept statuses remain pending later-use closure. Preface
literal earlier mentions also remain pending despite earlier front/end prose pass.

## V3-026: actual earlier proofs and repaired first uses

Actual V1 linear algebra56–77 finite exchange/dimension and477–508 GENERAL
Cayley–Hamilton proof reread; correct our earlier special2x2-only evidence. Actual
V1 polynomial thm:dalembert156–174 full complex-root proof and ex:eisen(b)678–684
full shifted cyclotomic proof read; printed polynomial chapter is6 despite file
ch03. Actual V1 power-set full solution1156–1167 and geometric-series195–202/
monotone convergence chain read; local ternary injection earns its application
to real uncountability. Actual C5 binomial-characteristic proof and V2 Lucas/
reciprocity full arguments earn characteristic-p binomial identity before C8.
C1 primer nowp=2 until formal term is available. Generated fields exist locally
by intersection; geometry arithmetic is proved by explicit line equations. New
quartic proof uses finite generators/one-step extension/complexFTA only, so no
forward primitive-element or Galois premise. All27 C8 labels/seven earlier mentions,
three shifted C7 contexts and two preface mentions classified. Whole later-use
closure still pending.

## V3-027 — finite-fields global prerequisite pass

All37 C9 label occurrences and6 literal V1/V2 mentions manually classified.
Actual V2 arithmetic-functions mu/multiplicativity55–80, complete prop:conv
101–145 and thm:mobius179–195 reread, rather than inferred from a title. Actual
V2 reciprocity chapter Euler criterion (real label thm:eulercrit), Gauss lemma,
supplementfor2, Eisenstein floor-sum lemma and full lattice reciprocity proof
reread for Fibonacci and Lucas–Lehmer. Earlier CH09-REVIEW shorthand thm:euler
is not the actual source label. Actual V1 binomial full proof299–319, Binet
remark770–777 and determinant full proof177–204 reread; current C9 re-earns
Binet's formula for its finite-field roots and zero/empty determinant cases.

No general C10 Galois correspondence enters C9 field existence, subfield lattice,
automorphism count or decoder. New local F16 proof precedes its caption. New
inclusion iff divisibility/gcd/lcm proof earns the subfield picture directly.
V1 Boolean-lattice/order language and bounds/intersections were read, but no
abstract lattice theorem is imported: all needed operations are proved locally.
New chains cover Frobenius, multiplicative primitive elements, divisor/subfield
lattice, Hamming/evaluation code, finite-field trace, Moore/linearized polynomials
and power sums. All later-use/whole-volume statuses remain pending. Trace first
appears in m-sequence prompt; solution proves codomain and nonzero polynomial
before using the bit map. Tr(1)=0 in even degree is explicitly not a zero-map
argument. Computational support does not replace the full pairing proof.

## V3-028 — entire Galois chapter prerequisite pass

All50 C10 label occurrences and3 literal earlier contexts classified individually.
Actual V1 ch05-sequences-series full elementary differentiation346–382, IVT392–408,
extreme-values434–449 and Fermat/Rolle/MVT479–506 reread. Polynomial derivatives
follow by constant/identity difference quotients, product induction and linearity;
no admitted exponential/logarithm derivative is needed for the quintic. IVT roots
and derivative/Rolle upper count therefore have actual earlier proofs. Actual V2
ch05-primitive-roots thm:cyclic133 onward full N(d)/phi(d) deficit proof reread,
including rootbound proof andp2. Actual earlier V1 prime-cyclotomic Eisenstein
solution and earlier V3 C2/C4/C5/C6/C7/C8/C9 proofs remain hash-guarded.

The motivating cubic's existence/count is now earned locally using C8; later
ex:discr is an alternative. Constant-polynomial convention explicit. General
cyclotomic degree/irreducibility is earned in its full worked triple BEFORE polygon
converse/Kronecker/rational-trig uses. Normal/Galois equivalence stays under explicit
finite characteristic-zero contract; inseparable splitting counterexample supplied.
Both radical directions check actual roots of unity/radicands/normality before
invocation. Current reduction-mod-prime comparison to complex roots remains an
explicit V13 outlook, never a premise. General Galois and five further first chains
reviewed; all91 whole-volume/later-use statuses remain pending.

## C11 global closure, V3-029

Actual V1 ch07 real Gram-Schmidt/projection323-363 was reread; complex Hermitian
geometry is locally earned, including empty bases and nonzero norms. Actual V1
ch05 differentiation346-382, ratio-test geometric comparison and signed-series
Cauchy-product proof611-658, and ch06 inverse-function proof28-44 were reread.
The latter's reminder52-56 admits exp/trig derivatives; the actual Taylor exercise
uses that contract and cannot independently earn it. New C11 circulant solution
supplies geometric sine limit/addition-formula derivatives and a uniform-tail
exponential construction, then a global inverse log and explicit four-Rolle
log-cos remainder. No later analytic-series or integration theorem is needed.
Actual V2 ch06 Euler proof55-113 and ch14 character definition44-61/count136-142/
orthogonality163-191 were reread. Their finite homomorphism language is already
available at entry; general trace characters and complex representations are
then defined and proved locally. All28 C11 label occurrences and five literal
earlier contexts are manually classified. New conceptual chains are explicit;
whole-volume/later-use closure remains pending. Earlier source file hashes guard
drift, not approval of every theorem in those earlier volumes.

## V3-030 actual C12 imports and local tools

Actual V1 complex-roots437-456 pentagon derivation, ch05 sequences246-266 full
BW/Cauchy/adjacent and453-463 full Heine proofs read. Coordinatewise compactness
and local Frobenius norm bound earn square lifting. Actual V2 ch07-sums-of-squares
160-176 full Euler identity, oddprime two-square pigeonhole and Lagrange descent
read; C12 imports the pigeonhole fact, not quaternion factorization. C11 full
ex:circulant now earns elementary derivatives/E/log; both C12 analytic tools lists
explicitly cite it. C12 common-refinement proof earns proper Lipschitz integrals,
then full Jensen earns log singularity limits. No later integration/topology/
series-exchange theorem supplies a premise. Exact GLOBAL-CH12 domains/A/B,
31labeluses,13earliercontexts and tenfirstchain decisions are recorded in JSON.

## V3-031 actual A imports and probability/model contract

Actually reread C7 thm:jordan828-905 and V1 ch07 full symmetric spectral378-400;
V1 ch05 O/reminder181-194/geometric195-204 and full BW/Cauchy246-266. Actual V1main
counter startschapter-1, so sequenceChapter3/linearChapter7 are correct. A supplies
its finitecoordinatecompactness and every Jordan error bound locally. Finite
Markovpath products normalize before muP^k; only distribution limits proved,
not an almost-sure empiricalvisit law. Leslie models mean populations and its
stated limit nowexplicitly requiresprimitivity. ActualV4coupling170-214is future
outlookonly, hashguarded fordrift.18labeluses/fourearliercontexts manuallyrecorded;
sevenfirstchains include Perron, period, rays, finiteMarkov, meanmodel, Jordan
rates and earlier Landau notation, with all later-useclosure stillpending.

## V3-033 actual B imports and forward-reference audit

Reopened complete current C6 Gauss747-916,C11 regular373-443,actual V1 spectral
378-401,V2 cyclic134-140 and Euler45-113. Actual V2 main has no chapter reset and
preface is unnumbered: Euler's explicit supplementary law is Chapter6, corrected
in B. Every29 B label occurrence and both literal earlier contexts classified;
no exercise pointer supplies an unearned premise. Local character count,
Hoffman bound, Walsh/Krawtchouk/LP arguments, finite compactness and the complete
nonabelian determinant/irreducibility proof were reconstructed in both directions
where available. Six new explicit chains plus the completed Paley first chain
retain pending whole-volume status. Earlier source hashes guard drift, including
main/include order. Unreferenced arguments are in all66 GLOBAL-APPB decisions.

## V3 citation reread, 5 November 2026

The teaching pass changed Volume 1, and one sentence in the circulant solution changed. Those files are the drifted prerequisite and anchor hashes. This note is the reread of the sites the gates name, not a new approval of every earlier theorem.

- `11.solution.ex:circulant` differs by one sentence. It now says the product, quotient and chain rules were proved in Volume 1, Chapter 3. Reread `prop:early-differentiation` in `ch05-sequences-series.tex`, lines 381–415: the product rule, the quotient rule and the chain rule are proved there, after the derivative has been defined. Chapter 5 of the current Volume 1 is complex numbers, so the old citation was the wrong chapter. The geometric construction of sine and cosine in that solution is unchanged. Five concept anchors and the exercise’s related-solution hash now use the new solution bytes. Their written reconstructions were left in place.
- The earlier-reference row `ch11-characters.tex::V1::2` already named that same proposition. Its context hash was updated to the corrected sentence, and the line range in the note is now 381–415.
- Volume 2’s group reminder in `ch01-divisibility.tex` now says Volume 1, Chapter 5. Reread the complex-numbers chapter: \((\Z,+)\) is introduced there as a group, with identity 0 and inverse \(-a\). Chapter 5 is the right pointer. The Basel tools line in `ch05-primitive-roots.tex` now names Exercise 6.7, which is where \(\pi^2/6\) is proved.
- Well ordering is a `definitionx` in `ch01-sums.tex`: every nonempty subset of \(\N\) has a least element. The induction proposition immediately after it still derives strong induction from that sentence. Inclusion–exclusion, the roots-of-unity proposition, the roots-of-unity filter and Brahmagupta’s identity are still the statements Volume 2’s bridge test looks up.
- Volume 2 forward references were recomputed: 85 uses, same paths, lines, targets and context hashes as the classified register. No classification was changed.
- Whole-file prerequisite hashes and the conceptual snapshot were refreshed only after the checks above. They guard drift. They do not certify the separate reading notes on Cesàro’s mis-application or the index-2 sentence for the trivial group.

## Reader-fix reread, 5 November 2026

Four manuscript passages changed. Each was reread against the argument around it before its hash was refreshed.

- Volume 2, solution of `pb:squaresmodpk` (c). The product \(\prod_{p\le y}(p+1)/(2p)\) counted squares modulo 2 as \(3/4\). Both classes modulo 2 are squares, so the factor is \(1\). Checked \(S(30)=12\) and \(12/30=2/5\), against the old product \(3/10\). The odd-prime factor \((p+1)/(2p)\) is part (a) at \(k=1\). The empty product at \(y=2\) is \(1\). The rest of (c), that a square modulo every modulus is a square in \(\Z\), was left as it stood.
- Volume 3, Gauss–Wantzel proof. Index 2 is now stated only for \(m\ge 1\), by the Chapter 5 corollary applied to order \(2^{m-1}\). The trivial group is written as a separate case with an empty chain. The polygon theorem is the same.
- Volume 3, cube rotations. The new sentences use the polarization identity already proved for the polygon, expand in the orthonormal basis \(f(e_i)\), and compute two matrices: the quarter-turn \((x,y,z)\mapsto(-y,x,z)\) has determinant \(1\), and \((x,y,z)\mapsto(-x,y,z)\) has determinant \(-1\). No new Volume 1 citation was added, so later Volume 1 occurrence numbers in the chapter did not shift; only line numbers moved.
- Volume 3, Landau solution. The classes of the order-6 group are computed from \(bab=a^{-1}\) and \(b^2=e\): identity; \(\{a,a^2\}\); and the three reflections \(b,ab,a^2b\). Cycle type is not used. Ruzsa’s exercise now defines \(A-B\) and \(A+B\) before the inequality. The solution’s bijection is unchanged.
- Dependency rows that only moved because text was inserted above them kept their role and reason. The `cor:pk` use in the Gauss–Wantzel proof was reclassified in its reason to the \(m\ge 1\) reading. Volume 2 forward-reference edges were recomputed and still match.
