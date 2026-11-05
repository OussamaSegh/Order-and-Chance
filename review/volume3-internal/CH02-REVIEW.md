# V3-003 — Chapter 2 internal reconstruction and second check

Complete chapter read: all prose, eight named proofs, eight prompt/hint/solution
sets, two figure sources and bibliography. Prompt-first evidence and its actual
exposure limits are in CH02-PROMPT-FIRST.md. This is internal AI review.

| Key | Exact domain/claim | Reconstruction A | Adversarial B and boundaries |
| --- | --- | --- | --- |
| prop:kerim | Any homomorphism f:G->G'; kernel/image subgroups, fibres b kerf and conjugation invariance | Apply the difference subgroup test to kernel and image. f(a)=f(b) iff f(b^-1 a)=e iff a in b kerf. Expand f(gkg^-1). | Reconstruct preimages of identity directly, including non-surjective f: only nonempty fibres are cosets. Trivial map/identity map and infinite Z->Zn verify extremal cases. No assumption of finite groups. |
| prop:normal | N subgroup of arbitrary G; inclusion/equality conjugation and left-right coset equivalences; kernels, abelian groups and index2 | Apply inclusion to g^-1 and conjugate back; multiply the set equality by g. For index2 use inversion's bijection between left and right cosets, so each complement is the unique other coset. | Conjugation has an inverse; inclusion for all g earns both directions without cardinalities. Old index2 prose appealed to equal cardinalities, inadequate for infinite groups. Corrected without weakening domain. Example: even Z; also nonnormal transposition subgroup S3. |
| thm:quotient | Arbitrary G, N normal; representative-independent product and all laws/projection; converse forces normality | a'=an,b'=bm imply a'b'=ab(b^-1 nb)m in abN. Associativity/identity/inverses descend. Kernel of projection=N. Conversely gnN=gN multiplied by g^-1 N forces gng^-1 inN. | Test the precise failed product for H=<(12)> inS3 using two representatives; independence fails. N={e},N=G and infinite Z/3Z work. Count formula used only for finite G; no normality inferred merely from equal coset sizes. |
| thm:iso1 | Any homomorphism, G/kerf isomorphic to imf; finite size formula | Equal cosets iff equal images, giving well-defined injection; product rule and onto its image give isomorphism. | Construct inverse y=f(g)->g kerf and check choice independence as a second route. Image codomain essential: f need not be surjective onto G'. Trivial kernel/all kernel and infinite source checked. |
| thm:iso23 | N normal inG, correspondence; N<=M normal inG third theorem; H any subgroup second theorem | Images/preimages undo for subgroups containingN and transport normality by conjugation. gN->gM has kernelM/N. Difference of two HN elements is inHN using normality; restriction H->HN/N has kernelH intersectN. | Check every quotient is legal before applying iso1: M/N normal; H intersectN normal inH; N normal inHN. Explicit multiplication hh'^-1[h'(nn'^-1)h'^-1] has correct order. Tests H={e},H<=N,H=G,N=G and N={e}; no assumption H normal. |
| thm:crt | Positive m,n; additive Z/mn isomorphic to product iff gcd1 | Reduction map has zero kernel by Gauss, same finite cardinality makes it onto. Bezout constructs inverse residues. If gcd d>1, every product element order divides mn/d<mn, so product is not cyclic. | Compare exponents independently, including m1/n1. The necessity excludes every possible abstract group isomorphism, not just failure of the canonical reduction map. Domain made explicit in statement. |
| prop:internal | H,K both normal, trivial intersection and HK=G; factors commute and product isomorphism | Commutator hkh^-1k^-1 is in both factors, hence identity. Move k past h' for homomorphism; kernel trivial, HK=G onto. | Independently show unique hk factorization: hk=h'k' gives h'^-1h=k'k^-1 in intersection. This yields the same bijection/product law for infinite factors too. Dropping normality permits dihedral twisting; no universal splitting claimed. |
| prop:semidirect | Groups N,H, homomorphism phi:H->AutN; twisted group law/normal factor/conjugation; recognition from normal factor+complement | Expand both triple products with phi_hh'=phi_h phi_h'. Identity uses phi_e=id; inverse=(phi_h^-1(n^-1),h^-1), checked both orders. Coordinate maps/projection give embeddings/kernel. Recognition maps(n,h)->nh. | Reconstruct the law from unique factorization nh and conjugation; composition order agrees. Explicit finite dihedral probes n1..9 check every associativity triple and inverse. Infinite groups/trivial factor/trivial action require no cardinal step; numerical order formula now restricted to finite factors. AutN group defined before using it. |

## Exercises: comparison and B pass

| Key | Reconstructed answer / A | Adversarial B, discovery path and boundaries |
| --- | --- | --- |
| ex:autzn | f([k])=ka; automorphism iff a unit; composition corresponds to multiplication | Reconstruct inverse via preimage1, without using cardinality to assert bijection. n1 sole unit/map works. Actual n8 example has four automorphisms and multiplication2 image4. Prompt/idea/hint/write-up match; one star. |
| ex:centre | Center closed under products/inverses, pointwise fixed by conjugation. Cyclic quotient lets x=a^m z,y=a^n w commute | Expand both xy and yx retaining order of noncentral terms; powers of one a commute. Infinite quotient and trivial quotient included. Center now defined in prompt. One star. |
| ex:phimult | Explicit CRT map preserves products and1, so restricts to unit groups; count phi | Inverse pair lifted by CRT has product1 by injectivity. Checked m1 or n1 using the sole unit of the zero residue ring; no generic additive isomorphism is asserted to preserve units. Counterexample phi4!=phi2² is correct. One star. |
| ex:commutator | Conjugation sends generators to generators, so G' normal; abelian quotient iff all commutators inN; S3'=A3 | Compute [(12),(23)]=(132) independently, proving nontriviality constructively. Source's sign-kernel plus prime-order alternative also works. Conjugation of inverses/products extends the generator check. Arbitrary/infinite/abelian groups covered. Two stars. |
| ex:quaternion | Six subgroups listed; all normal, ij=-ji, and nontrivial subgroups all contain-1, excluding proper semidirect split | Actual two matrices square to-I, anticommute, and generate eight distinct closed matrices; associativity inherited. Added that missing realization check. Nontrivial-factor argument explicitly excludes a trivial factor. Two stars. |
| ex:affine | p(p-1), normal translation kernel, multiplier complement and conjugation b->ab; p3 allS3 | Evaluate0,1 for uniqueness; compute inverse(a^-1,-a^-1b) and product order directly. At p2 multiplier factor trivial and groupC2, so formula still works. No later action theorem needed for the faithful function embedding. Two stars. |
| ex:normalnormal | <s> normal inV4 normal inD4, but r s r^-1=sr² outside<s>. Characteristic in normal implies normal by restriction of conjugation. Every subgroup of a normal cyclic group is normal | Original final paragraph was false for infinite N: 2Z and3Z are distinct subgroups of the same infinite order. New proof treats finite uniqueness and infinite generator images g or g^-1 separately; both preserve <g^m>. Claim retained in full generality. Two stars. |
| ex:order8 | C8 orC2³ if maximal order8 or2; otherwise index2 C4, with conjugation identity/inversion and b²=e/a², gives C4xC2,D4,Q8 | Reconstruct eight unique forms and full product law; added explicit generators forC2³ to avoid unexplained abstract vector-space structure. A commuting b of order4 has b²=a²; an inverting b fixes its own square, forcing exponent0/2. Distinguish all five by commutativity and element-order counts, including5/1 involutions inD4/Q8. Three stars. |

All targets are preserved. The infinite-cyclic repair is a proof correction,
not a restriction to a weaker finite statement. Named theorem/solution hashes
in the registers identify the precise reviewed revisions.

## Complete prose, figures and prerequisites

Read and reconstructed the homomorphism identities, determinant/sign examples,
real/circle exponential examples, direct-product group laws/orders, Dn
factorization, and the distinction between a quotient and a split product.
The real exponential bijection/law is the usual high-school exponential/logarithm
convention; Volume 1's calculus reminder explicitly assumes those properties.
It is not falsely recorded here as an earlier proved theorem. The complex-circle
kernel uses Volume 1's exponential-form uniqueness/root-angle argument. The actual
Volume 1 sign lemma (Vandermonde quotient over unordered pairs, multiplicativity,
conjugate transpositions and induction) was read, so A_n/its sign map is available.

The old product sentence used lcm of undefined infinite element orders. It now
treats finite orders and says explicitly that an infinite coordinate gives an
infinite-order pair. The earlier index2 proof used a cardinality shortcut that
does not establish the infinite case; inversion of cosets fixes it.

All 10 D4 subgroup nodes and15 containment-cover edges were recomputed from
actual affine permutations on four points; exactly6 nodes are normal. Independently
the seven cover edges of the six-node C12 lattice were recomputed by additive
subgroup inclusion. The actual plate labels/normal styles/edges match. All9
integer labels in the kernel-fibre plate have their indicated residue mod3.
Actual final-page and grayscale visual inspection remains outstanding.

The first-reader written pass removed the unqualified suggestion that kernel and
image determine a group; Q8 demonstrates why a complement is extra information.
The outgoing question is how a group moves other objects and how nonfree motions
affect counting. No spoken/human read-aloud is claimed. Bibliography metadata is
still pending primary-source reconciliation.

Regression: baseline ex:normalnormal fails the explicit infinite-case coverage
check; corrected source passes. All lattice and finite semidirect checks pass,
as does the historical Volume3 checker. These source/finite checks support,
and do not replace, the reconstructions above.
