# V3-013a — quaternion and rotation core, partial chapter closure

Solo internal AI review, not human refereeing or formal verification. The entire
C12 source, all15 prompts/hints/solutions, both figure sources and bibliography
have now been read. This checkpoint closes only the four named results and first
seven quaternion problems. The other eight workshop problems remain pending
corrections/second-check closure, as do global keyed unnamed/history records and
actual new C12 output inspection. CH12-PROMPT-FIRST.md discloses that all hints,
the first supplied answer and the second answer opening were seen before its
record. The other thirteen first solutions predate their supplied answers.

## Named results, actual hypotheses and two reconstructions

| Key | Exact domain and conclusion | Reconstruction A | Adversarial B and boundaries |
| --- | --- | --- | --- |
| prop:quat | Real four-coordinate quaternion matrix algebra; closure, associative division ring, conjugation/norm, pure dot-cross product formula. | Multiply the actual complex2 matrices, identify lower entries as conjugates, use conjugate transpose and multiplicative determinant, then positive norm gives two-sided inverse. Bilinearity reduces pure product to nine basis pairs. | Independently expand Hamilton's four real product coordinates and conjugate in reverse order; mixed norm terms cancel in pairs. Check all basis signs ij=k,ji=-k,ik=-j,ki=j, identity/zero and arbitrary real coefficients. The division is only by N(q)>0 for q!=0. Locally define cross product and prove determinant/triple/norm identities rather than silently importing absent vector-calculus material from V1. Fields stay commutative by series convention; H is called a division ring, not an unqualified field. |
| lem:euler | Real3 orthogonal A, determinant1; fixed unit axis and planar rotation. | Compute det(A−I)=det(I−A)=−det(A−I), so real characteristic0 gives determinant0 and fixed axis. Orthogonality preserves its perpendicular plane; restricted determinant1 gives planar cosine/sine matrix. | Independent eigenvalue route: real odd-degree characteristic polynomial has a real eigenvalue; orthogonality forces±1 and remaining conjugate pair product1, so determinant1 forces a+1 eigenvalue (three real±1 also has+1). Check identity admits arbitrary axis, nonidentity planar rotation fixes no plane vector, so exactly an axis. No complex spectral theorem or infinite-dimensional claim. SO3 notation is now defined before this lemma. |
| thm:su2so3 | Real unit quaternion q, pure vectors; surjective homomorphism into SO3, kernel±1 and half-angle formula. | Conjugation preserves purity/norm, associativity proves composition order; perpendicular expansion gives axis and cos(theta),sin(theta); Euler supplies every rotation. Commuting with every pure vector forces imaginary part0, so unit kernel±1. | Independently compute all three image columns to get the full real rotation matrix, trace4a²−1, skew4a(b,c,d), orthogonality and determinant1. Every unit q is explicitly parametrized, including q±1, before orientation is inferred; continuity alone without connectedness is no longer an unsupported shortcut. Kernel checked by commuting with i,j,k and every vector, not by a single axis. Explicit local inverse charts below earn the stronger topological cover statement as well. |
| thm:finiteso3 | Every finite G<=SO3, including trivial; cyclic, dihedral2n n>=2, A4,S4,A5. | Double-count nonidentity rotation/pole pairs, obtain sum(1−1/n_i)=2−2/N and exactly two/three orbits. Solve all numerical possibilities; cyclic case fixes poles, dihedral case earns involution/inversion, A4 action4 points, S4 faithful action4 lines, A5 simple/pair-count then five Sylow2 action. | Reconstruct every stabilizer as an earned finite cyclic circle subgroup (C9). r1 impossible since RHS<1 but LHS>=1; r4 impossible since RHS>=2. n2 Klein and n>=3 dihedral separated. In S4 case prove any linewise kernel half-turn would put all lines in one plane, contradicted by an order3 axis inside that plane. A5 normal subgroup contains full pole-type sets15/20/24; none of six proper sums+1 divides60. Its involution centralizer4 equals each containing Sylow2, proving uniqueness and exactly five such subgroups. No counting upper bound is mistaken for attainability; explicit examples and geometric uniqueness are earned separately below. |

## First seven exercises, complete supplied-answer comparison

The first reconstructions, exposure limits and exact statements are recorded in
CH12-PROMPT-FIRST.md. These rows reconstruct each complete actual write-up
adversarially after comparison with its hint/finding idea.

| Key | Domain, second reconstruction and boundaries | Grade |
| --- | --- | --- |
| ex:compose | Ordered quarter turns about positive z then x. Actual matrix product sends e1→e3,e2→−e1,e3→−e2; fixed axis(1,-1,1), trace0 and oriented cycle give120 degrees. Quaternion is(1+i−j+k)/2. Reversing gives(1+i+j+k)/2, neither equal nor negative, so the induced rotations differ after quotienting by the kernel. The full first answer had already been read; no blinded independence claim. | 1 retained |
| ex:euler4 | Any eight real inputs, integers as special case. Independent direct expansion of four bilinear coordinates cancels all mixed terms; actual quaternion-matrix norm proof supplies the other route. Check every j/k sign and zero factors. This proves multiplicativity, not the unearned prime representation step. Supplied-answer opening was seen before permanent first record. | 1 retained |
| ex:rotmatrix | Unit real quaternion; all nine entries, trace4a²−1=1+2cos theta. First vector triple-product derivation; second compute q i qbar,q j qbar,q k qbar separately. Exact rational samples and basis sign cases agree, including±1, three half-turns, quarter-turn products and both composition orders. Normalization essential; zero has no rotation. | 2 retained |
| ex:conjS3 | Unit quaternions conjugate iff same real part; rotations conjugate iff same unsigned angle in[0,pi]. First use surjectivity to transport imaginary axes; second use quaternion real+imaginary norm invariant and explicit local axis rotations. Imaginary0 gives singleton±1. For rotations account for both lifts before choosing nonnegative real part; theta0/pi and axis sign handled. | 2 retained |
| ex:2T | Exactly24 displayed norm1 quaternions; subgroup,12-element image A4. h³=−1, h cyclically conjugates i,j,k, so three distinct left cosets of Q8 close and exhaust all half-signs; corrected misleading right-coset wording. Independently all576 products computed exactly, inverse closure and twelve distinct real matrices checked. Image has three involutions/eight order3, excluding C12 and D6 before classification yields A4. No circular reliance on later Hurwitz ring proof. | 2 retained |
| ex:2I | Preimage of actual A5 rotation subgroup has120 elements, exactly one involution, hence neither S5 nor A5xC2. First use fibre size2; second solve(a+x)²=1:2ax=0, imaginary case gives negative square, so only±1 and only−1 has exact order2. Exhibit distinct involutions in both comparison groups. Removed incidental unproved SL2F5 identification and potentially misleading same-quotient conclusion; all requested targets remain. | 2 retained |
| ex:hurwitz | Real Hurwitz lattice, noncommutative ring, units24, one-sided division and every left ideal principal; odd prime/integer four-square norm. First reconstruct lattice basis and Euclidean argument; second explicitly check basis/omega products and all numerator parity classes. Define left ideals before use and handle zero ideal H0. Right approximation a b^-1 gives left quotient qb; left ideal closure then earns principal generator. For I=Hp+Halpha, exclude normdelta1 by right multiplication by alphabar and real coefficient1/p; exclude p² by unit quotient and alpha notinpH. All order/side choices checked. Half-to-integer conversion delta=epsilon+2mu and delta epsilonbar preserves norm; all256 residue-sign patterns checked exactly. Actual V2 thm:foursq full first-multiple/pigeonhole proof reopened, not inferred from a title. p2 and integers1/0 handled separately. | 3 retained |

## Newly earned unnamed arguments: two reconstructions

Cross product first-use: V1 real linear algebra was searched/read and did not
supply this operation. Define its three coordinates, derive perpendiculars and
scalar determinant identity, expand squared norm and the first coordinate of
the triple identity (the other two cycle). B independently expands every basis
pair/triple and verifies preservation under orientation-one orthogonal maps by
dotting against every Aw. This supplies the geometric arguments and conventions.

Double-cover charts: A uses trace4a²−1 and antisymmetric entries4a(b,c,d) to
recover the unique positive-real lift when traceA>−1; translated charts cover
every rotation. B reconstructs the nine entries, checks all denominators stay
positive, two sheets are disjoint and continuous inverses, and translations
preserve fibres/composition. Trace−1 is outside this chart, covered by another;
q±1 and identity are included. No mere kernel count is called a topological proof.

Plate topology: A lifts paths by finitely many charts and families by a uniformly
fine square grid, then uses endpoint sign. It constructs simple connectedness
of S3 by short normalized-chord approximation, a point outside finitely many
proper2planes, stereographic coordinates and straight contraction. B rechecks
the interpolation's distance<1/2/nonzero norm, finite-union line argument,
stereographic inverse and fixed basepoint. S3 path connectedness is explicitly
earned by one/two normalized chords. For the grid proof, both already lifted
cell edges lie in the same sheet since they meet at a common corner; thus no
incompatible gluing is assumed. Real coordinate Heine/Bolzano–Weierstrass proofs
were actually reopened and the square version is supplied locally. Based-loop
group operations are justified by reparametrization/reversal. Sign is a
surjective homomorphism with trivial kernel, so pi1SO3=C2. Independently verify
the explicit two-turn contraction H and based normalization H(s,0)^-1H(s,t):
norm1, same endpoints, initial full circle, final constant. One-turn sign−1
cannot change through a homotopy. Spin statement is now the precise complex2
representation action−I, without claiming a physical experiment or all SU2
representations acquire that sign.

Attainability: tetrahedral signed permutations give12, C1 cube construction24.
For the icosahedron, actual twelve Q(sqrt5) coordinates and explicit matrix B
give a vertex-transitive subgroup plus order5 stabilizer. B independently
enumerates every supporting plane from all220 vertex triples, obtains exactly
20 equilateral triangular faces and all normals printed in the text, checks
five neighbours at each vertex, B orthogonal/determinant1/fixes vertex/order5
and permutes all12 vertices. This gives the60 lower bound as well as upper.
Dualization recovers both solids and their identical rotations.

Geometric uniqueness: A aligns cyclic/dihedral axes, including D2 perpendicular
half-turn axes. For A4/S4/A5 compare the actual earned complex3 characters;
kernel/determinant tests exclude reducible or wrong rows, odd A5 automorphism
swaps its two degree3 rows. B reconstructs a real nonzero part of a complex
intertwiner: Schur makes it invertible, orthogonality makes D^TD central and
positive scalar, normalized Q is orthogonal, and−Q fixes determinant if needed.
Thus conjugacy is earned without an unproved polar-decomposition theorem.

## Actual figures and limits

Read both full TikZ files. Independently recompute all73 full-circle and30
highlighted-arc points from their oblique trigonometric projection; check both
vector endpoints, axis and half-angle/±q captions. For all five solids, reconstruct
the actual50 projected vertices and90 edges, match the exact regular-solid
graphs, recover each orthographic projection, check every point to its printed
three-decimal accuracy, and independently determine every hidden-edge style
from supporting-face normals. All five orders/groups match the proved examples.
The initially suspected tetrahedral hidden edge is not a defect: its depicted
view has all six edges visible. No unsupported visual finding is recorded.

check_chapter12.py is exact finite support, not mathematical certification.
It also runs the actual noncommutative left-Euclidean construction for each of
the24 odd primes below101, checks both original ideal generators are divisible
on the correct side, and converts each norm-p result to integer coordinates.
Actual new C12 PDFs/EPUB/reader still need building and opening. Prior C11 source
snapshot9aa217f3 was built in all formats:490 reading/489 print,KDP490,spine1.15in,
same-build wrap,85 public files/report hashes; actual EPUBCheck5.3.0zero messages
and output checker pass. Actual print319 colour/grayscale and342–346 colour
opened/read. Old character contrast finding is reopened and corrected in those
actual pixels; bottom345 additionally reopened at2x to confirm the complete cases
display. These are six distinct print pages, seven full-page images, not a
whole-book or digital approval. Exact manifests are separately checkpoint-scoped.

Pending C12 workshop findings include local integral/Euler-product convergence
proofs, zero-polynomial/system domains, n1 sharpness, t0 prompt restriction and
star grades. All solutions have now been read, but none of these eight is
accepted from a rewrite status or an unfinished repair. First reconstruction
mistake: it counted24 fifth-turn rotations, conflating all nonidentity5-cycles
with the twelve rotations through±72 degrees. Actual supplied answer's12 and
probability(1/5)(1−4^(1−t)) for t>=1 are correct; recheck independently by exact
class/walk enumeration before closure. C4/C12's smallest-simple claim and C5's
unproved order<60 remark need a complete finite proof or curricular qualification
in global closure. Full closing voice/history/outlook/publishing gates remain.
