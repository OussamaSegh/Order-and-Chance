# V3-012b — finite complex representations, characters and signed involutions

Solo internal AI review; neither independent human refereeing nor formal
verification. Read the entire main chapter, every definition/example/remark,
all ten named proofs, all eleven prompts, hints, finding ideas and complete
solutions, the actual 59-cell figure source and all bibliography entries.
CH11-PROMPT-FIRST.md records all eleven first solutions before opening any
supplied Chapter11 answer. Its proposed signed model also predates reading
Adin/Postnikov/Roichman. After comparison, reconstructed each actual argument
adversarially. CH11-FOUNDATIONS.md remains an explicitly partial older checkpoint.

The chapter's exact standing contract is finite G and finite-dimensional complex
representations. Dimension zero is permitted; irreducibles are nonzero. Results
about another field say so explicitly. No general modular or real scalar version
of Schur/Maschke is inferred from the complex statements.

## Named arguments: exact domains, reconstruction A, adversarial B

| Key | Domain and conclusion | Reconstruction A | Adversarial B, boundaries and repair |
| --- | --- | --- | --- |
| thm:maschke | Finite G, finite complex V; invariant positive Hermitian form, stable complements and irreducible direct sum. | Average a positive Hermitian form; right multiplication reindexes. For v perpendicular to W, use h(gv,w)=h(v,g^-1w). Local complex Gram–Schmidt gives direct sum and positive integer dimensions terminate recursion. | Independently average conjugates of a projection: each maps into W and is identity there, so the average is idempotent; reindexing makes its kernel stable. Zero V gives empty sum, W=0/V works. New unipotent examples show failure in characteristic p for Cp, and for infinite Z over C. Earlier V1 real spectral theorem was insufficient; complex geometry and finite-order unitary diagonalization are now proved locally. |
| lem:schur | Nonzero finite complex irreducibles V,V'; intertwiner zero or isomorphism, endomorphism scalar. | Stable kernel/image force bijectivity if nonzero. FTA/C7 characteristic polynomial supplies eigenvalue; f−lambda I intertwines and is noninjective, hence zero. | Independently any eigenspace of an endomorphism commuting with G is stable, so it is all V. Check d1/trivial G, f0 and unequal dimensions. Explicit real irreducible C4 rotation has nonscalar commuting J; algebraic closure matters. No eigenvalue claim over arbitrary fields. |
| cor:abelianirr | Finite abelian G, complex irreducible; degree1. | Each rho(h) commutes with G, so Schur makes it scalar; every line is stable, forcing d1. | Independently take an eigenline of one commuting operator and restrict the other commuting operators to its eigenspaces successively; a common eigenline exists and irreducibility makes it all V. Positive dimension essential; trivial G has its one-dimensional irreducible. |
| prop:charbasic | Finite G and any finite complex representation, including zero; degree, class constancy, inverse conjugation, absolute bound, direct sums and fixed-point counts. | Similarity invariance of trace; finite-order matrices diagonalize with unit roots; triangle inequality; block traces and permutation diagonals. | Recompute trace invariance as sum_i,j Aij Bji=tr(BA), count inverse eigenvalues and diagonal fixed basis vectors directly. Empty X/V gives character0; G regular action has no fixed point for g!=e by cancellation. Bound remains valid at d0, inverse eigenvalues never zero. |
| thm:orth | Nonzero finite complex irreducibles; character inner product delta on isomorphism classes. | Average Hom(V,V') matrix units. Nonisomorphic case average0; same case trace/d times identity. Sum diagonal coefficients to obtain character inner product. | Separate projection argument on Hom: conjugation action has character chi' times conjugate chi, average projects onto intertwiners, and its trace is their dimension0/1 by Schur. Coordinate check verifies indices rho'ij rho^-1_kl, identification of isomorphic representations, and division only by d>=1 and positive order. |
| cor:mult | Any finite complex V and any initial partial list of pairwise distinct irreducibles; multiplicity, character criterion, regular multiplicities and square sum. | Orthogonal irreducible characters are independent in the finite class-function space, so first earn finiteness and extend the initial list. Decompose V, pair with each character, then apply to regular character. | Independently Hom multiplicity equals dimension of invariant maps from each irreducible into the direct sum. Regular coefficient is d; dimensions give sum d²=order. Zero representation has norm0 and is not irreducible. Fixed the formerly implicit complete-list assumption, without using the later character-basis theorem circularly. |
| thm:classes | Finite G, complex class functions; irreducible characters are an orthonormal basis and number equals class count. | If f is orthogonal to all irreducibles, central operator sum conjugate(f(g))rho(g) is scalar with trace0 on each irreducible, hence zero on regular representation. Evaluate at e_e to recover every f(g)=0. | Independently treat central linear combination of left translations; on each regular irreducible summand its trace forces scalar0, while the regular basis recovers coefficients injectively. Check conjugation reindex, conjugate placement, finite-dimensional perpendicular-complement conclusion, trivial group. Does not assume already square table. |
| cor:columns | Finite G, full irreducible list; column inner product centralizer order for conjugate elements, else0. | Weight column j by sqrt(classsize/order). Row Gram is identity and table is square by prior theorem, so right inverse is left inverse. Undo weights and use conjugation orbit–stabilizer. | Independently expand normalized class-indicator functions in the orthonormal character basis and take their inner products. Complex conjugation order agrees after swapping g,h. Identity column yields square sum, central element gives order, no zero class size. |
| thm:fourier | Finite abelian A, every complex function; normalized inversion, Parseval and dual sum. | Every function is class function, irreducibles are one-dimensional, so apply basis coordinate expansion/Pythagoras; column orthogonality at identity gives delta sum. | Independently character cancellation by translation proves orthogonality, then number of characters=order gives basis; expand both sides and cancel finite sums. Normalization is 1/order; singleton group gives identity formulas. No analytic series or measure limit. |
| prop:dirichletorth | q>=1 integer, gcd(a,q)=1, any integer n; finite character filter for n=a mod q. | Nonunit n gives all zeros. Otherwise conjugate chi(a)chi(n)=chi(a^-1n), and prior dual-sum identity selects identity unit. | Independently enumerate generator characters for q5/8/12 and all residues; general cancellation proof translates a nonidentity unit. q1 has trivial unit group and phi1=1, including n0; negative n periodic. Finite prime-sum filter now precedes explicitly later analytic outlook. |

## Exercises: actual answer comparison and second reconstruction

Each first derivation is separately recorded in CH11-PROMPT-FIRST.md. The rows
below compare all actual prompt/hint/idea/write-up parts after that first record;
the source contains complete answers throughout. Grades are reassessed, not
inherited from the historical editorial rewrite ledger.

| Key | Actual domain/claim and adversarial second check | Grade |
| --- | --- | --- |
| ex:pairs | S4 action on six unordered pairs. Directly enumerate fixed pairs for every class to obtain(6,2,2,0,0); weighted inner products give 1+degree2+standard3. Independently sum those three actual table rows, all five values and dimensions agree. Hint's fixed-pair path and full decomposition are complete. | 1 retained |
| ex:onedim | Finite G; one-dimensional representations factor uniquely through abelianization, count index(G:G'). First proof kills each commutator; second reconstructs both directions of pullback and uses finite abelian dual count. Sn n>=2 gives2 (including S2), A4 gives3, A5 gives1 by actual earlier derived-subgroup proofs. No unproved perfection premise. | 1 retained |
| ex:a4 | Four classes sizes1,3,4,4; quotient C3 gives three linear rows, permutation4 minus trivial is(3,-1,0,0), squared norm1. Independently exact arithmetic in Q(omega), omega²+omega+1=0 verifies every row Gram and square-map indicators(1,0,0,1). Inverses interchange the two3-cycle classes. Four distinct irreducibles exhaust class count; no guessed table existence. | 2 retained |
| ex:centralchar | Finite G, irreducible complex degree d>=1; center acts by unit scalars, hence d²<=index(center). Reconstruct inequality from row norm1 and contributions of every central element. Q8's four linear rows and(2,-2,0,0,0) follow from five classes and sum of squares; second check constructs i=diag(i,-i), j=[[0,1],[-1,0]], verifies ij=-ji and no common line. Trivial/abelian group forces d1; no false Q8 class equation inherited. | 2 retained |
| ex:circulant | n>=1, complex c; circulant eigenvectors and finite normalized convolution. First derivation changes sum variables; second uses a nonsymmetric c(k)=2k−3 and actual matrix action, checking Fourier sign and factor n. Walk starts at delta0, t>=0; actual largest nontrivial absolute eigenvalue for odd n>=3 is cos(pi/n), and even n has−1. Singleton stationary, t0 and holding h0/1/interior checked. Rational direct distributions for n1..17,t0..20 agree with independent Fourier sums. Existing decay corrected earlier is independently earned. The log-cos estimate now has a four-Rolle local proof and bounded fourth derivative; no later analysis theorem supplies it. | 2 retained |
| ex:dirichlet8 | Units8 and12 are C2²; all four sign rows on generators, zero on nonunits. Recompute every actual table entry, all eight/twelve filter residues and arbitrary period translation. All characters real, principal row included. Finite sums only; complete requested residue-class detector. | 2 retained |
| ex:a5 | Finite A5 classes1,15,20,12,12. First derive actual degree4 and5 constituents; corrected proof checks both trivial and degree4 multiplicities before taking a Maschke complement, so norm1 is not applied to an unearned virtual character. Completeness leaves two degree3 representations. Independently all row/column Gram values in Q(sqrt5), total60, square-map indicators and exact cycle classes agree. Five-cycle inverse remains in its own class; squaring swaps the two. Values phi and phi'=1−phi are real algebraic conjugates, not complex conjugates; misleading bar notation removed. Geometry is a later interpretation, not a premise. | 3 retained |
| ex:divides | Finite complex irreducible degree d>=1; prove algebraic-integer criterion, closure, rational criterion, class-sum integrality and d divides order. First reconstruction uses integer regular matrices whose eigenvalues include each central scalar. Actual write-up uses finite Z-spans of class sums and integer multiplication constants, with no free-module basis assumption. Recheck coefficient orientation A^T, a nonzero generator vector, determinant monicity and nonzero module. The rational denominator is positive; monic relation forces denominator1. Roots of unity give integral characters, and order/d is an integral rational. Zero ring/unit/zero generator families cannot be substituted for the required nonzero span. | 3 retained |
| pb:glnz | m>=1, integer matrices; finite orders in GL2Z are1,2,3,4,6, odd-p principal congruence kernel torsion-free, finite subgroup order<=12. First cyclotomic degree route; second trace/conjugate-root route plus explicit order matrices. General binomial proof reduces to prime order and checks every p-adic valuation including last term k(p−1)−1>=1. p2 counterexample−I. For n0 GL0 trivial, reduction injective. Real averaging plus local O2 matrix calculation earns cyclic/dihedral classification, including one reflection and V4. Exact R,S yield12 elements, SRS=R^-1 and mod3 injectivity; no future C12 classification premise. | 3 retained |
| pb:commutators | Finite G, ordered pairs, [x,y]=xyx^-1y^-1. First Schur-average rho(y), multiply rho(y^-1), trace/sum; second class-function coefficient directly recomputes conjugation and uses inverse characters. Gives N(g)=order sum chi(g)/degree, identity order times class count. All3600 A5 pairs independently counted: values300,32,63,65,65, weighted sum3600. Positivity proves every element attained; no inference from parity or density alone. Trivial G gives1. | 2 retained |
| pb:frobschur | Finite G, nonzero complex irreducible, root-count r; all original indicator/root-count/Q8/real-form/Sn conclusions retained. A uses average on concrete Mat_d, transpose and irreducible dual (annihilator proof supplied), with Tr(F T_g)=chi(g²). B expands matrix units independently for arbitrary Gaussian-integer matrices d1..4 and checks dual/intertwiner orientation and fixed-space dimension. Real-valued iff indicator nonzero; real matrices iff+1, with locally proved antilinear J and positive scalar J². Q8 indicator−1 prevents a real2 model. For Sn n>=0, actual signed involution representation earns all indicators+1: orientation cocycle, cancellation on single even cycles, positive paired-cycle shifts, then independent square-root cycle count. Checked every permutation through n7 against direct squaring and signed trace, full cocycle through n4; n0/1, odd unpaired even cycles and degree sums covered. Symmetric/exterior character formulas retained via concrete matrix subspaces. No Young/Specht theorem or undefined tensor product supplies a premise. Full old/new scope and source hashes in V3-012b-frobenius-schur-augmentation.json. | 3 retained, expanded five-part guided challenge with complete solution |

## Unnamed reasoning, prerequisites, story and actual visual defect

Read every intervening paragraph, including all five initial representation
examples, the two concrete S3/S4 tables, every table entry/caption, abelian dual
group closure, twisting/pullback irreducibility, radix-two algorithm, all finite
prime filters, outlook remarks and ending. Direct decomposition of permutation
space supplies the trivial constituent before subtraction. Empty finite sets and
zero-dimensional representations are now consistent. For the triangle, complex
rotation eigenlines are swapped by reflection, so absence of real eigenvectors
alone is not incorrectly used as complex irreducibility.

Actual V1 real Gram–Schmidt/spectral proofs do not establish complex unitary
geometry. The new local construction explicitly earns conjugate linearity,
positive norms, complements and orthonormal eigenbases. Actual V1 Taylor and
integration-toolkit text was read; integration existence there is a named
contract with construction in V7. The required finite log-cos remainder is now
derived by Rolle alone, so that construction is no prerequisite. C7 supplies
squarefree annihilators, eigenvalues/trace and finite vector-space reasoning;
C5 supplies derived groups, C9 finite subgroups of field units, and C10 the
fully worked general cyclotomic degree proof before GL2Z uses it. Every new dual,
antilinear and symmetric/skew-space concept in the last solution is defined
and proved before invocation. The figure previews A5 and now points explicitly
to the exercise that earns its table.

For S4, independently map edge/face/vertex rotations to diagonal permutations
and use axis-plus-plane trace 1+2cos(theta) to identify the cube character as
(3,-1,-1,0,1); the tetrahedron acts on the sum-zero hyperplane. Thus the spatial
identifications are checked, not merely inferred from equal dimensions.

The final prompt formerly quoted Young's real-form theorem as an essential
unproved premise. The supplied answer also invoked undefined tensor/dual/Specht
constructions. The augmentation preserves every mathematical target and supplies
a finite signed-model proof, plus the converse real-form criterion. The primary
Adin/Postnikov/Roichman proof sections were actually read only after the independent
record; our route does not import their preliminary Sn real-form premise and
thus avoids circularity. The source gives attribution without calling this a
new research result. Historical bibliography details remain separately pending
in the whole-book research register.

The opening asks why group orders are sums of squares; the main route answers
through averaging and regular multiplicities, then turns characters into finite
Fourier coordinates and arithmetic filters. The new ending checks a cube quarter
turn directly and motivates the actual C12 quaternion/rotation question. A
separate marked shuffle outlook uses independent uniform positions, hence a
holding probability1/n. Actual V4 Chance and V11 Randomness source agree with
that model. Distinct-transposition parity would prevent the old unqualified
mixing claim. Burnside/Frobenius structural theorems are marked outlook; no
essential proof uses them. Removed an unsupported categorical current assertion
about absence of character-free proofs; no claimed new research proof is certified.

Actually opened preliminary2ee605fd print physical317 in colour and grayscale.
White labels on pale coral cells were weak, especially in grayscale. The source
now uses black labels on all27 positive70-percent cells, preserving the approved
inks/geometry/type. Every actual source cell, coordinate, fill intensity and
foreground is recomputed. This records a real visual finding, not approval of
the corrected output: the new page and changed pagination must be reopened after
a new immutable build. Other PDF/EPUB/reader/global-history gates remain pending.

check_chapter11.py provides finite support and regression gates, never general
proof certification. Old foreground source fails the corrected contrast gate;
old final-solution source fails the local-prerequisite gate. Unit integration
also checks all indicators, tables and walk endpoints. Source hashes and all
proof/hint/solution identities are refreshed separately in the keyed registers.
