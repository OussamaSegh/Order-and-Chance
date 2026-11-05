# V3-015 — Symmetry Diagonalises: complete internal mathematics

Solo internal AI review, not human refereeing or formal verification. Read the
entire appendix, all eleven named proofs, every unnamed argument, all twelve
prompts, hints, finding ideas and full solutions, both actual figure sources
and every bibliography entry. APPB-PROMPT-FIRST.md records all twelve first
derivations before any supplied hint/solution was opened. Compare the actual
answers afterward and perform the independent/adversarial reconstructions
below. Global history/voice/context and final pixels remain separate gates.

Exact standing domain is finite abelian G and complex matrices/functions until
the explicitly multiplicative finite nonabelian determinant section. Circulant
size n>=1; binary length n>=0. The Hermitian product is linear first as in C11;
the appendix's forward Fourier transform is unnormalized, explicitly differing
from C11's normalized forward transform. Simple undirected cycles use n>=3.
Paley main theorem uses primes p=1mod4, hence p>=5, not all prime powers.
Code bounds use integer d>=1 and pairwise distance at least d, allowing empty/
one-word codes. Distance distributions divide only for nonempty C. n0 and d>n
give maximum size1; d0 separately gives2^n, outside the stated LP.

## Earlier tools actually read

Actual C11 complex Gram–Schmidt, projection and finite-order unitary proof,
lines50–118, were read in the main review and the linear-first definition
reopened here. C11 matrix-unit averaging proof thm:orth293–368 and full regular
multiplicity/square-sum cor:mult397–443 were reopened for the nonabelian route.
Its proof uses a complete irreducible list earned in that earlier source, not
the later polynomial factorization. C11 actual radix-two split at676 was
reopened; it proves the count only for power-of-two lengths. Local padding to
m>=2n-1,m<4n now earns the arbitrary-length cyclic convolution count without
assuming any bit-complexity or rounding theorem.

Actual C6 lem:gauss619–639, prop:gaussirr644–699 and thm:gaussufd702–787 were
reopened, including content, reduction modulo a prime, denominator descent,
prime irreducibles and induction in the number of variables. They really
prove the finite multivariable UFD result needed for generic determinant
irreducibility. C7 Jordan/minimal-polynomial proof supplies the squarefree
diagonalization criterion; its finite abelian decomposition supplies a distinct
check of character count. V1 FTA/root bound, real spectral theorem and bounded
subsequence/Cauchy proofs were actually read/reopened as recorded for appendix A.
Appendix A's local finite-coordinate compactness is now earlier on the printed
route. Actual V2 Euler/Legendre/primitive-root proofs were read at their earlier
proof sites; no quadratic-residue property is inferred from a chapter title.
No Volume8 spectral ratio theorem or future analysis theorem supplies a premise.

## Named results: exact claims, A and B

| Key | Exact domain/claim | Reconstruction A | Independent/adversarial B, boundaries and repair |
| --- | --- | --- | --- |
| linear:thm:circulant | C=p(S), complex size n>=1, Sx_j=x_(j+1): Fourier eigenvalues p(omega^a), common orthonormal basis, normality and determinant product. | Sv_a=omega^a v_a, including the wrapped coordinate; polynomial evaluation gives C eigenvalues. Finite geometric sums give the orthonormal basis. U*CU diagonal, hence CC*=C*C and determinant product. | Independently S has n distinct eigenvalues, so its one-dimensional eigenspaces must be preserved by every commuting polynomial. Direct entry sum verifies the same values for nonsymmetric coefficients; product agrees with an exact rational determinant for n1..9 at70-digit precision. Correct first-linear Hermitian exponent from b-a to a-b; either gives orthogonality but only the latter matches the declared convention. n1, repeated values, singular C and complex coefficients allowed. Define adjoint/unitary/normal before use; no real spectral theorem applied to arbitrary complex matrices. |
| linear:prop:commutant | Complex size n>=1: MS=SM iff M_jk depends only on k-j. | Entry products give M_j,k-1=M_j+1,k, hence simultaneous index shifts; shift j to0 to recover c_(k-j). Converse polynomial in S commutes. | Different cyclic-vector proof: e0,S e0,...,S^(n-1)e0 form a basis. A commuting M is determined by M e0, and exactly one polynomial in S has that image; hence M equals it on the entire cyclic basis. n1 all scalar matrices, no invertibility of M assumed. Both checks preserve the stated shift orientation. |
| linear:lem:commuting | Arbitrary, possibly infinite, family of pairwise commuting diagonalizable operators on finite complex V, dim>=0: common eigenbasis. | Induct dimension. Choose a nonscalar operator; its distinct eigenspaces are nonzero proper invariant subspaces for the family. Restricted minimal polynomials divide squarefree split polynomials, so remain diagonalizable. Induct and concatenate. | Adversarial spectral-projector reconstruction: each eigenspace projector is a Lagrange polynomial in the chosen operator and commutes with the family. Refine subspaces only when some restriction is nonscalar. Each refinement increases the number of nonzero summands, bounded by dim V, so no enumeration of an infinite family is needed. Zero V/empty family/all scalars handled; nondiagonalizable commuting operators are deliberately excluded. |
| linear:thm:characters | Finite abelian G: N distinct characters, orthogonality with norm²N, exact common translation eigenvectors are nonzero multiples of characters. | Cancel a nontrivial character sum by translation. For common eigenfunction f, f(g)=c(g)f0 forces f0!=0; group multiplication gives c homomorphism, with c(g)c(-g)=1. Commuting finite-order translations have a common eigenbasis, so there are at least N characters and orthogonality gives at most N. | Different completeness check: actual C7 finite abelian decomposition into cyclic factors; each factor C_m has precisely m root-valued characters, and arbitrary characters restrict/reconstruct independently on products. Their count is the product N. Recheck cancellation separately, and evaluate any common eigenfunction at0 to exclude a missing zero-coordinate case. Trivial group, repeated finite cyclic factors, and N-th roots over C are included; no positive-characteristic analogue claimed. |
| linear:thm:invariant | M_xy=m(x-y) on finite abelian G: eigenvalue hat m(chi)=sum m(u)bar chi(u), determinant product. | Substitute u=x-y and use chi(x-u)=chi(x)bar chi(u); the already complete character basis diagonalizes M. | Independent expansion M=sum_u m(u)T_(-u) makes the same eigenvalue and sign immediate. Explicit entry multiplication earns equivalence of simultaneous invariance/commutation and convolution kernels before use. Singleton G, m0, singular/nonsymmetric/complex kernels checked; no symmetry or positivity assumption. |
| linear:thm:paley | Prime p=1mod4: degree(p-1)/2 once, two values(-1±sqrt p)/2 each(p-1)/2 times, srg parameters(p,(p-1)/2,(p-5)/4,(p-1)/4). | Quadratic Gauss sum satisfies g(a)=1+2lambda_a. The x=y+t change of variables gives the squared modulus of g is p since2at!=0; a square root of-1 makes g real. Trace0 gives equal sign counts. (A-theta I)(A-tau I) vanishes on constants' orthogonal complement and equals((p-1)/4)J, giving all common-neighbour entries. | Different quadratic-character count below derives srg directly, then the two eigenvalues/multiplicities. This avoids evaluating the sign of g1. Exact matrix identities for p5/13/17/29/37; all39 actual P13 figure edges/colours/coordinates checked. Prime p>=5, distinct vertices and nonzero differences explicit. Define strongly regular parameters before caption/theorem. No prime-power generalization borrowed from the later Paley appendix. |
| linear:thm:krawtchouk | Binary length n>=0,0<=k<=n: D_k eigenbasis by character weights, weighted character sum, full orthogonality. | Count support intersections j to get K_k(t); interchange roles for the weighted character sum. Standard-basis trace(Dk Dl) counts ordered distance pairs, while the character-basis trace gives the weighted K table Gram. | Independent orthogonality: sum over words z of the products of weight-k and weight-l character sums; character cancellation leaves exactly identical subsets, giving2^n binom(n,k)[k=l]. Direct distance-matrix action/sign sums check the eigenvalue and all coinciding values. n0 yields D0=[1]. Repeated numerical values from different weights have combined multiplicities; this clarifies the indexed spectrum, not a weaker spectral target. Polynomial binomials/leading coefficients and distance-algebra closure are now earned locally. |
| linear:thm:delsarte | Nonempty binary C, n>=0, every0<=k<=n: sum_i A_i K_k(i)>=0. | Expand K_k(d(x,y)) into weight-k real characters and interchange finite sums to get(1/M)sum_T(sum_C chi_T)². | Gram/projection check: E_k=H_k H_k^T is positive semidefinite; orthogonal columns give E_k²=2^n E_k. The indicator quadratic form divided by M equals the stated left side. Every diagonal/normalization factor is checked. All274 nonempty codes through length3 satisfy exact SOS identities, including nonlinear sets. Empty C is not assigned an undefined distribution; its size bounds are handled directly. n0/k0/singleton cases pass. |
| linear:cor:lp | Integers n>=0,d>=1: A(n,d) bounded by the stated finite maximum over nonnegative a_i and K inequalities. | Any nonempty code yields a feasible distance distribution with objective M. Sum inequalities using sum_k K_k(i)=0 for i>=1 to obtain sum a_i<=2^n-1; feasible0 and finite-coordinate subsequences attain the maximum. | Adversarial check all constraints/indices: k0 is not needed, Kk0=binom nk, d>=1 is essential, and the coefficient bound makes each coordinate bounded. Limits preserve finite closed inequalities and the linear objective. d>n has no variables and value1; n0 also value1. Independent exact dual certificate f=2K0+2K1+K2/2 for(8,4) bounds every feasible distribution by16, agreeing with the actual16-word construction. No unproved strong LP duality theorem is invoked. |
| linear:cor:plotkin | Integer n>=0,d>=1,2d>n: any code with pair distances>=d has M<=2d/(2d-n). | For n>=1 and nonempty code, k1 Delsarte gives0<=n+(n-2d)(M-1); divide only by positive2d-n. Empty code direct, n0 one possible word. | Different coordinate count: dM(M-1)<=sum_ordered distance=2sum_j r_j(M-r_j)<=nM²/2. For M>0 rearrange to the same bound. Equality forces all distinct distances d and each r_j=M/2; even M requires n>=1, with n0 singleton exception explicit. No missing all-zero/one-word case or division by M0. |
| linear:thm:groupdet | Finite abelian G, independent variables x_g over C: det(x_(g-h)) equals product_chi sum_g chi(g)x_g. | Evaluate at arbitrary complex assignments, diagonalize using earlier invariant theorem, then earn polynomial identity by induction on variable count and the univariate root bound. Reindex conjugate characters; variables themselves are not conjugated. | Independent formal calculation over C[x_g]: the constant invertible character matrix diagonalizes the symbolic matrix entrywise, so determinants give the identity directly without evaluation or an infinite-set inference. Recheck g-h versus h-g and conjugation permutation. Trivial group factor x_e; V4/C3 examples exact. No real-variable-only or finite-field polynomial-identity argument imported. |

For the independent Paley check, let eta be the quadratic character, eta0=0.
Count v²=u(u-1). The substitution U=2u-1,V=2v makes U²-V²=1;
choose r=U-V in Fp* and U+V=r^-1 to give p-1 solutions. Thus
sum_u eta(u)eta(u-1)=-1. For nonzero delta, expand the two square indicators
(1+eta(t)-[t0])/2 and(1+eta(t-delta)-[t=delta])/2.
The product sum is(p-3-2eta(delta))/4, since eta(-1)=1. This is lambda
or mu as asserted, independently of Gauss sums. The resulting matrix identity
A²+A-((p-1)/4)I=((p-1)/4)J yields the two nonconstant eigenvalues; the real
spectral theorem and trace0 give equal multiplicities. This is a general proof,
not an enumeration of selected primes.

## Exercises after actual answer comparison

All first derivations are in APPB-PROMPT-FIRST. All supplied mathematical
solutions reconstruct correctly after the explicit boundary repairs below;
the incomplete main-prose sign/domain/forward-premise issues are not inherited
as mathematical approval.

| Key | Actual prompt/hint/idea/write-up comparison and B | Grade |
| --- | --- | --- |
| linear:ex:circalg | Independent first polynomial/geometric inverse matches full supplied commutant proof. Recheck inverse by multiplying on both sides, t0/n1 and t^n!=1 denominator; S*=S^-1 gives complex adjoint. Closure under inverses means inverse of an invertible element. | 1 retained |
| linear:ex:circ3 | Supplied constructions(3k+1,3k+2,9k) match the independently found(3m+1,3m-1,9m) families after index changes. Mod3 forces both the sum and quadratic factor divisible by3, hence N divisible by9. All729 residues and negative/zero parameter values exact. The main sign error at a=b=c!=0 is corrected, not blamed on this correct answer. | 2 retained |
| linear:ex:fourier | Supplied geometric sum yields F²R,F4I. Independently act on normalized character vectors and check reversal;70-digit products n1..9. The answer correctly says possible eigenvalues, not every fourth root for every n. | 1 retained |
| linear:ex:dualgroup | Restriction and product give explicit inverse homomorphisms. Independent cyclic generator/root count agrees, including trivial factors and n1. Actual answer makes finite abelian hypotheses explicit. | 1 retained |
| linear:ex:convolution | Supplied change x=y+u factors the unnormalized transform; expand both inversion sums for exact1/N Parseval. Independent dual-orthogonality expansion checks all conjugates and the kernel action m*f. Complex nonsymmetric functions and singleton group included. | 2 retained |
| linear:ex:walsh | Supplied first-bit character factor gives correct block order. Both butterfly orders compute the same result; recurrence2T(n-1)+2^n,T00 gives n2^n. n0 base is H0=[1]; main now defines tensor/block notation and earns the count before using it. | 2 retained |
| linear:ex:krawgen | Two finite binomial expansions give coefficients; z->-z gives reflection; z1 gives total with t0 empty factor1, not an undefined0^0. Independent signed-subset counting and all n0..7 K-table Gram checks agree. | 1 retained |
| linear:ex:gausssign | Supplied scaling by square classes plus total sum0 proves nonsquare sign reversal for every odd prime. Independent direct square/nonsquare complement sum or eta-substitution proves it again. Conditional p1mod4,g1>0 eigenvalue assignment retained. Fixed zeta determines the sign; wording no longer suggests it is a free choice. | 2 retained |
| linear:ex:paleyself | Supplied coset bijection and permutation similarity checked; independent complementary adjacency J-I-A swaps theta/tau on nonconstant characters and preserves degree. Distinct vertices and prime p1mod4 are explicit in actual solution. | 1 retained |
| linear:ex:paleyramsey | Supplied affine normalization of an edge to0/1 and common neighbours{2,9,16} exactly exclude4-cliques; triangle0,1,2 exists. Independent enumeration gives68 triangles,zero4-cliques/independent4-sets. sqrt17 alone permits4 and does not prove the result. Define Ramsey number in prompt; locally earn existence via finite recurrence. No unproved exact R4,4=18 upper bound retained. | 2 retained |
| linear:ex:plotkinsharp | Supplied independent coordinate count proves both equality conditions. Compare with equality in k1 SOS: all weight-one character sums vanish. Fix the claim that M must be even without a length restriction: n0 singleton attains bound1 and all coordinate/pair assertions are vacuous. Nonempty achieving code makes division by M valid. | 2 retained |
| linear:ex:lpthree | Supplied k1 inequality plus quarter of k2 gives a4+(5/2)a5+3a6+(5/2)a7+a8<=15, all coefficients>=1. Independent polynomial certificate(t-4)(t-8)=2K0+2K1+K2/2 gives same16 bound. First independent construction and supplied RM(1,3) agree: all16 affine truth tables,14 distance4 and1 distance8 from every word. Another B fixes one coordinate in at least half the code, deletes it and applies earlier Plotkin(7,4), so the categorical claim that Plotkin cannot see the answer is removed. All120 pair distances checked. | 3 retained |

## Unnamed arguments, full nonabelian target and figures

APPB-U-HOFFMAN: The old essential Volume8 premise is replaced by a local proof.
For an independent-set indicator x=(s/v)1+y, y perpendicular to1, compute
norm²y=s-s²/v and x^TAx=0. Earlier real spectral theorem gives
0>=k s²/v+tau(s-s²/v), hence s<=-v tau/(k-tau), with empty s0 direct.
B: diagonalize A and expand the indicator in its actual orthonormal basis;
the constant coefficient is s/sqrt(v), all other quadratic contributions are
>=tau times their squared coefficients, giving the same inequality with
no cross term. tau<0,k-tau>0,s>0 divisions explicit. Paley's values simplify
exactly to sqrt p; nonsquare coset multiplication earns the clique version
locally before it is used. No future optional chapter supplies a premise.

APPB-U-GROUPDET: The original nonabelian irreducible-factor claim was not
proved by C11's square-sum statement alone. Preserve and earn the full target,
not a weaker factorization. Define the finite algebra C[G] on basis e_g with
bilinear product e_g e_h=e_gh. The map Phi to all irreducible matrix blocks
preserves products, is injective because an element acting0 on every regular
summand acts0 on e_e, and is bijective by the earlier square sum. Left
multiplication by sum x_g e_g has matrix x_(g h^-1); on block M_d it is
B->A_rho B, so d separate columns give det(A_rho)^d. Thus all factors and
their exact multiplicities are earned for every finite G, including trivial.

Independent B: actual C11 matrix-unit orthogonality gives an explicit inverse
to a single prescribed rho block B: a_g=(d/|G|)tr(B rho(g^-1)). Averaging each
matrix entry yields Phi(a)_sigma=B if sigma=rho and0 otherwise. This separately
earns surjectivity and the independence of all block coordinates without the
regular-decomposition injection argument. Check the trace indices: averaging
sigma(g)_kl rho(g^-1)_ji leaves delta_lj delta_ki/d and therefore B_kl.

Generic determinant irreducibility is proved locally by induction: detY=D y_dd+E,
with D irreducible in the UFD of all other variables. Adjoining unused variables
cannot factor D, since degrees in each unused variable add to0. Setting an
identity block of size d-2 and swapping the last two coordinates makes D0
but E=-1, so D does not divide E and gcd(D,E)1. The linear polynomial over
the fraction field is irreducible and primitive; actual earlier Gauss brings
irreducibility back. Invertible Phi makes every block entry an independent
coordinate, so each determinant remains irreducible after adjoining other
blocks, has degree d and is not associate to another block's determinant.
Adversarially check d1/d2, the specialization, UFD/prime step, no division by a
possibly singular block, and coefficient-field C. Exact S3 regular6-by-6 and
1/1/2 blocks agree for40 signed integer assignments; all36 representation
products and nonzero determinant of the6-by-6 coordinate map are checked.
These finite checks support, not replace, the general proof. No named result
or original exercise is removed; a formerly unearned outward target is earned.

Other unnamed groups read/reconstructed: complex geometry definitions; finite
geometric sums; inverse interpolation at distinct roots; polynomial identity
over infinitely many complex assignments; FFT zero-padding/folding; spectral
equality case of the real cubic; simple-cycle endpoints; dual rows versus
columns; translation/kernel/convolution signs; Cayley real eigenvalues; square
cosets; cube metric/character/tensor definitions; generalized binomial degree;
distance-algebra closure by pair orbits; coding triangle inequality and finite
maxima; Gram projections; simplex construction; LP compactness; affine code;
and both determinant examples. These will receive explicit keyed global
exposition/context closure, not automatic approval from this file.

Actual circulant plate: all401 polyline points are recomputed at angles2pi*j/400,
independently using complex powers and trigonometric sums, tolerance.00051 per
coordinate. All7 root markers at1.2 exp(2pi ij/7), all7 image markers for
p(z)=1+2z+z³, and every exponent label are checked; tolerances reflect3-decimal
source rounding. Actual Paley plate: all13 radius2 vertex coordinates, labels,
39 distinct edges and their three difference colours are checked against the
actual square set. Matrix common-neighbour identity gives(13,6,2,3), independent
of the source caption. The actual8-word length7 list has all28 pair distances4;
its size attains Plotkin8. No final actual B figure pixels have yet been opened.

## History and written teaching pass limits

Read actual Hanson/Petridis arxiv1905.09134v3 (6May2020) introduction and
Corollary1.5 at printedpp4–5: it gives omega(omega-1)<=(p-1)/2 and explicitly
notes earlier slight improvements for certain primes and the prime-field
restriction. The original claim that improving sqrt p at all had been open
until this paper is wrong. Replace with the accurately attributed published2021
outlook, with no premise borrowed. Only the theorem/introduction and beginning
of proof were read here; no complete research-proof certification is claimed.
Remove the unsupported current-record claim for asymptotic coding and the
Bessel/magic-function/Fields-medal catalog; bibliography remains for the later
full metadata pass. This loses incidental outward claims, no finite code target.
The Weyl primary quote page was not accessible in the first Google Books attempt;
catalog metadata alone does not verify it. Gauss/Olbers chronology/quote and
remaining bibliography/history still need actual source evidence in the global
pass; they are not covered by named mathematical acceptance.

Written cadence pass reads the full main text and all answers as connected
prose, replaces stock praise/conclusion with the circulant/cube/code objects,
and explicitly contrasts normalization conventions only where it helps the
reader compute. Incoming question: which basis is fixed by translations?
Answer: characters, then finite distance-count sums of squares. Outgoing
question: can linear algebra count objects without a group action? No human
or spoken read-aloud session is claimed.

## V3-032: fresh boundary findings supersede earlier completeness claims

The complete current reread found gaps in the earlier zero-length Walsh and
empty-code coverage. V3-032-BOUNDARIES.md and V3-032-fresh-core.json give fresh
full A/B checks of all six changed items; the other seventeen full pairs/triples
are individually SHA-identical. The intended statements remain intact. Earlier
V3-015 text above describes that historical checkpoint, not a claim that its
boundary checks prevented all subsequent findings. All sixty-six global B rows,
history and current output inspection remain pending at this boundary batch.
