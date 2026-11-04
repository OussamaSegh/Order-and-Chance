# Conceptual prerequisite and story ledger

V3-002. This ledger is incremental. Only Chapter 1 has its current complete
mathematical reading; all other chapter/appendix argument routes remain pending.
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
