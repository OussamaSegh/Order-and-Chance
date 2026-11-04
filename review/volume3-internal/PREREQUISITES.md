# Conceptual prerequisite and story ledger

V3-006. This ledger is incremental. Chapters1–8 have complete mathematical
readings recorded; Chapters9–12 and all appendix argument routes remain pending.
A backward-reference scan is not a conceptual audit.

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
| Sign, normal subgroups, quotients, actions and all later tools | Pending actual C2 onward audit | Do not infer availability from historical rewritten statuses | Later ledgers must read and earn each premise before acceptance. |

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
