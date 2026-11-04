# Conceptual prerequisite and story ledger

V3-006. This ledger is incremental. Chapters1–6 have complete mathematical
readings recorded; Chapters7–12 and all appendix argument routes remain pending.
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
