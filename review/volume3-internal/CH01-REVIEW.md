# V3-002 — Chapter 1 internal mathematical reconstruction

Read the entire current chapter, including all prompts, hints, ideas, write-ups,
caption and bibliography. This is an internal AI reconstruction. Chapter 1's
solutions were encountered before this permanent record was written; the checks
below are fresh derivations and adversarial reconstructions, not a claim of a
blinded experiment. Subsequent chapters will have recorded prompt-first solutions.
Bibliographic metadata and actual final-page inspection remain separate gates.

## Named results: A and B

| Key | Hypotheses/domain and claim | Reconstruction A | Separate check B and boundary probes |
| --- | --- | --- | --- |
| prop:rules | Any group, including the trivial group; uniqueness, cancellation, reversed inverse and unique left/right division | Compare identities by ee'; compare inverses b=b(ac)=(ba)c=c. Multiply on the appropriate side; verify both products with b^-1 a^-1. Solve ax=b directly. | Treat left and right translations as inverse bijections. This independently gives cancellation and each Latin-table row/column. Noncommuting permutations show why the inverse order cannot be retained. No finiteness until the table sentence. |
| prop:dihedral | Regular complex n-gon, integer n>=3; exactly 2n isometries and the three relations | Subtract f(0), use polarization and an orthonormal basis to get linearity. Vertex average fixes the origin. Adjacent independent vectors have n*2 possible images, all realized by rotations/reflections. Evaluate srs on z. | Compose any symmetry with a rotation to fix v0=1. Its orthogonal matrix then fixes e1 and sends e2 to +/-e2; hence only identity or conjugation remains. n=3 works; n=2 is excluded because adjacent vectors become dependent. |
| prop:cube | Geometric rotations preserving [-1,1]^3; order 24 and axes/angle list | Midpoints of vertex pairs force columns to signed distinct coordinate vectors. There are 48 signed permutations, exactly 24 with det1, giving an upper bound. Exhibit identity plus 9 face/8 vertex/6 edge rotations. | Count oriented face frames: image of the top face (6), then its marked adjacent edge (4); each frame is realized by the exhibited rotations. Signed permutation enumeration checks 24 independently. Removed the implication that every det1 isometry is already known to have an axis; the complete exhibited list earns it here. |
| prop:subgroup | Nonempty H subset of any group; difference test; arbitrary intersections; words generate <S> | Test a=a gives e; e,b gives b^-1; a,b^-1 gives ab. Words close by concatenation and reversal. Every subgroup containing S contains every word. | Verify universal minimality both ways. Empty S gives {e}; the empty intersection is the whole ambient G. Infinite groups/intersections require no finite closure shortcut. |
| prop:order | g in any group; infinite powers or least positive period n; residues/count/order of g^k | Repeated powers give a positive period. Divide every integer exponent by n. Minimality kills the remainder. Cancel gcd(n,k) using earlier Gauss. | Exponent map has kernel an additive subgroup of Z, which the actual Volume 2 proof classifies as nZ; this gives the same residue and order formulas by another route. Test k=0, negative k, n=1 and an infinite-order translation. |
| thm:lagrange | Finite G and subgroup H; equal disjoint left cosets, |G|=[G:H]|H| | Translation H->gH has inverse. An intersection gh1=kh2 implies gH=kH. Every g lies in gH. | Independently count the equivalence relation a~b iff a^-1 b in H. Reflexivity/symmetry/transitivity use subgroup laws; its classes are precisely the left cosets. H={e}, H=G and nonnormal S3 subgroup all work. No converse asserted. |
| cor:lagrange | Finite group of order n>=1; element order divides n; Euler for m>=1; prime-order cyclicity | Pigeonhole n+1 powers first earns finite order. Apply Lagrange to <g>. For units mod m>=2 use its phi(m) elements. m=1 congruence is separately immediate. Prime n leaves only element orders1,n. | Re-derive g^n=e by permutation of cosets of <g>; verify trivial group, modulus1, modulus2 and prime2. The old proof silently skipped finite-order existence and excluded m1 only inside its proof; both steps now explicit. |
| thm:cyclic | Cyclic group, finite order n>=1 or infinite; Z/Zn models, all subgroups and generator counts | Powers give the operation-preserving bijection. For nontrivial H choose the least positive allowed exponent m; divide all allowed exponents by m. In finite case divide n too. Apply n/gcd(n,k). | Pull back H to an additive subgroup of Z and use actual Volume 2 prop:subgroups. Verify H trivial separately, n1 phi(1)=1, negative exponents, infinite subgroups mZ and unique order-d subgroup. Sum of totients follows from disjoint order classes, without assuming the theorem being proved. |

## Exercises: complete reconstruction and second check

| Key | Independently reconstructed answer / method | Adversarial check, hint and grade |
| --- | --- | --- |
| ex:square | (xy)^-1=xy=y^-1 x^-1=yx. | Alternative: xyxy=e, multiply left by x and right by y to get yx=xy. Works for infinite/trivial groups. Hint and write-up match; one star. |
| ex:dihedralcentre | Rotation subgroup index2. Center={e} for odd n, {e,r^(n/2)} for even n. | Commuting with r excludes reflections since n>=3; commuting with s forces 2k=0 mod n. Direct affine permutations on n vertices give the same list. No n2 claim. One star retained. |
| ex:order4 | Lagrange gives cyclic C4 or all three nonidentity elements involutions. Cancellation forces the displayed V4 table. Rectangle and three coordinate half-turns realize it. | Compute diagonal matrices diag(1,-1,-1), diag(-1,1,-1), diag(-1,-1,1); products give the third. Two distinct geometric examples supplied, not the hint's arithmetic example alone. One star. |
| ex:union | h outside K and k outside H force hk in neither. V4's three order2 subgroups cover it. | If one subgroup contains the other, a proper union cannot be G; this case is explicitly treated. Works noncommutatively. Two stars. |
| ex:gl2 | First column p²-1, second p²-p; determinant fibres have equal size by explicit diagonal scaling, giving p(p²-1) for SL2. | Enumerate every matrix for p=2,3,5,7; both counts agree. Multiply the two actual p2 shears in both orders; they differ. Removed future first-isomorphism premise and undeclared kernel terminology. Two stars. |
| ex:cubeS4 | A diagonal-fixing signed permutation T has all signs equal; fixing lines (1,1,-1),(1,-1,1) fixes its coordinate permutation, and detT1 excludes -I. | An equal-image pair U,V has V^-1 U diagonal-fixing, hence identity, proving injectivity directly. Independently the 24 signed det1 matrices give 24 distinct permutations on the four lines. Removed later kernel/isomorphism theorem use. Two stars. |
| ex:prodorder | If (ab)^k=e, a^k=b^-k has order dividing both coprime m,n, so both are identity and mn divides k. Converse power mn is identity. | Raise equality a^k=b^-k to m and n and use Bezout on m,n as a separate route. S3 example (12)(123)=(23) verifies failure without commutation; m1/n1 and noncommutativity checked. Two stars. |
| ex:fieldcyclic | For each d|n, either no order-d element exists or exactly phi(d), since one such cyclic subgroup exhausts roots of X^d-1. Equal sums force order n. | Alternate: choose an element whose order has maximal p-adic exponent for each p|n, isolate prime powers, then multiply commuting coprime-order pieces. Root bound rules out an exponent below |G|. Trivial subgroup n1 and characteristic dividing exponents cause no root-multiplicity assumption. Actual earlier root proof was read; local root cancellation also supplied. Two stars replaces three. |
| ex:wilson | Pair inverses in an abelian group. Remaining involutions give stated zero/one-involution cases; Fp has only roots +/-1 of X²-1. | p2 checked separately because +/-1 coincide. Empty involution product=e; abelian assumption needed for an unordered product. Direct small primes and V4 product support the reconstruction. One star replaces three; no harder multiple-involution classification is asked. |
| pb:matrices2 | Counts: p; p²(p²-1)/2; p²(p-1)²/2; p(p²-1). Cyclic basis exists for nonscalar C. Its commutant is aI+bC; a 2x2 determinant counts invertible commutants; equal cosets count each similarity class. | Completely enumerate matrices for p=2,3,5,7, classify by actual characteristic-polynomial roots, verify all four totals and the local Cayley-Hamilton identity. Counts sum symbolically to p4. The two diagonalizable types give the stated half-limits. Replaced all later orbit/CRT/extension tools with local proofs. Three stars replaces two. |
| pb:fibdivides | Finite state update (u,v)->(v,u+v) is bijective, so returns from the initial pair. Minimal divisible index z divides every other using Fibonacci gcd; converse follows likewise. Jacobsthal update loses invertibility mod2. | A repeated state at i<j can be pulled back i times, explicitly giving return time j-i; no tail assumed. Actual Volume 1 ex:fibgcd full solution read: addition identity, consecutive coprimality, Euclidean descent of indices. m1,n0 and z1 work. One star retained with that already-proved tool. |
| pb:ruzsa | Choose one representation x=b_x-c_x. Inject (a,x)->(a-b_x,a-c_x); subtract output to recover x then a. Maximal disjoint translates yield |X|<=K and cover B by X+(A-A). | Reconstruct recovery/order of signs independently. Empty A allowed in triangle, empty B/C immediate; covering explicitly needs A nonempty. Finite maximality terminates; nonintegral K is harmless since |X| integer. Two stars. |
| pb:returnbound | Inverse-reversal preserves the increment law, hence symmetry of p_t. Convolution at 2t gives sum p_t²; Cauchy-Schwarz gives maxima/lower bound. An average of translations contracts Euclidean norm. Odd block split gives upper bound; deterministic Z2 shows zero odd returns. | Noncommutative S3 exact rational convolution checks all assertions through even time12. Cycle formula now derived by finite root filter and independence, independently compared with exact binomial counts for n1..12/t0..6. n1,n2, periodic even n, t0 and zero eigenvalues handled. Hint and full solution agree after local derivation. Three stars replaces two. |

These finite checks support the general arguments above; they do not replace them.
The corrected exercise targets retain their original claims, with the cycle formula
now explicitly earned. No weaker replacement is certified as the old theorem.

## Unnamed arguments and first-use evidence

The complete chapter reading covers its definitions, power rules, field/matrix
transfer, isomorphism consequences, motivating counts and summaries. Powers with
mixed signs follow by cancelling inverse factors after proving the positive rule;
no commutation between different group elements is assumed. The Dn normal form
comes from sr^k=r^-k s, with s²=e cancelling adjacent reflections. SL is a subgroup
by determinant multiplicativity and det(A^-1)=det(A)^-1. An operation-preserving
bijection transports identities, inverses, generated powers and subgroup laws;
that proves the listed isomorphism invariants, not just the names. A4's missing
order6 subgroup is a forward illustration only, with proof to be checked in C4.

The actual D4 plate's 64 entries were parsed and compared with independent
permutation composition on four vertices. All pass; the axes arithmetic is
1+9+8+6=24. Native-size, grayscale and final-page legibility remain unreviewed.
The Pascal plate is used in Chapter 9 and is not silently approved here.

Actual earlier sources read: Volume 1 `ch02-complex-roots.tex`, elementary group,
roots and geometric-sum orthogonality proofs; `ch07-linear-algebra.tex`, exchange,
rank-nullity, determinant, characteristic polynomial and diagonalization proofs;
`ch03-polynomials.tex`, field division/root-bound proofs; `ch01-sums.tex`, full
Fibonacci gcd solution; `ch04-inequalities.tex`, full Cauchy-Schwarz proof;
`ch09-probability.tex`, product-expectation/independence definitions and proof.
Volume 2 `ch01-divisibility.tex`, actual division, subgroup-of-Z, Bezout and Gauss
proofs. Hash/site records belong in the prerequisite ledger. The general field
extension of linear algebra is justified by the actual operations in those proofs,
not inferred from the chapter title. No analytic geometry theorem is imported.

Validation: 463 existing unit tests pass, zero skips, 49.218s. The inherited
Volume 3 checker passes. New Chapter 1 exact checks pass; the tools-context
regression rejects the baseline Chapter11 premise and passes the correction.
Actual typeset output, full bibliography/source validation and final frozen-head
evidence remain outstanding.
