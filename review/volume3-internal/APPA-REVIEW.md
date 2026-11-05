# V3-014 — Positive Matrices, complete internal mathematical reconstruction

Solo internal AI review, not independent human refereeing or formal verification.
Read the entire appendix, all eight named arguments, every unnamed paragraph,
both examples, both actual figure sources and all twelve complete triples.
APPA-PROMPT-FIRST.md records first solutions before any supplied hint or answer
was opened. Then compare every prompt/hint/finding idea/full write-up and perform
the adversarial checks below. Research metadata and final pixels remain separate
gates; the mathematical status does not certify those gates.

Standing domain: real n-by-n matrices, n>=1; complex eigenvalues/eigenvectors.
The characteristic polynomial has positive degree and splits over C by the
actual V1 ch03 thm:dalembert and C7 thm:jordan. No empty spectral maximum is
taken. Positivity is entrywise; an eigenvector is nonzero. A walk of length0
is allowed for reachability. A primitive power has exponent>=1. The one-by-one
zero matrix is irreducible, has simple eigenvalue0 and positive eigenvector1,
has no positive period and is not primitive. The periodic/peripheral and
primitive-equivalence statements now explicitly exclude this case and the
preceding paragraph supplies its complete behavior. The old unqualified
equivalence is not certified.

## Actual earlier tools read

- V1 ch05 prop:seqcrit, lines246–265: monotone/supremum, peak-subsequence
  Bolzano–Weierstrass and Cauchy proofs were actually reopened. Each extraction
  preserves all earlier coordinate limits; finitely many coordinates suffice.
  V1 ch05 thm:evt lines435–445 actually proves only a closed interval statement.
  Its maximizing-sequence method is extended locally to Delta/K, rather than
  importing a general compactness theorem from a future volume.
- V1 ch03 thm:dalembert lines151–166: actual real/imaginary subsequence step and
  minimum argument read; FTA full proof was read in earlier main-route work.
- V1 ch07 thm:spectral lines378–403, complete real proof reopened: conjugating
  z*Sz makes eigenvalues real; real/imaginary parts give a real eigenvector;
  its orthogonal complement is stable and induction gives an orthonormal basis.
  This suffices for BB^T in the bipartite exercise. No future singular-value
  theorem is assumed. Gram–Schmidt/projection lines350–365 also reopened.
- C7 thm:jordan actual cyclic-module construction lines795–825 reopened;
  full existence/uniqueness already reconstructed at its own source checkpoint.
  The local binomial power formula handles zero eigenvalues separately.
- Actual V2 ch01 Bezout proof was read in the earlier prerequisite record.
  Here finite-cycle decomposition and decreasing positive gcds justify every
  use of a finite Bezout identity, including the closed-walk semigroup proof.
- Probability means finite nonnegative weights summing to1, as actually taught
  in V1 ch09; row-vector evolution is defined here. No V4 convergence theorem
  or coupling premise is imported. The V4 reference is an outlook.

## Named results: reconstruction A and adversarial B

| Key | Exact claim/domain | Reconstruction A | Adversarial reconstruction B and probes |
| --- | --- | --- | --- |
| linear:thm:perron | A>0, n>=1: positive rho, positive right/left vectors, algebraic simplicity, strict peripheral dominance, uniqueness of nonnegative eigenvectors, max r(x)=rho. | On Delta, r bounded by max row sum and r(Ax)>=r(x). The normalized image K has every coordinate>=alpha/(n beta)>0. Finite-coordinate subsequences and continuity attain max r. A nonzero defect Az-rz>=0 becomes strictly positive under A, contradicting maximality at Az. For any complex eigenpair A|y|>=|lambda||y| gives |lambda|<=r. Equality forces common phases. A boundary-touching positive-vector subtraction gives geometric simplicity; a positive left vector rules out a Jordan chain. | Independently challenge each strict inequality and boundary: Delta alone does not make the boundary-defined r continuous, while K resolves all denominators. r>0 because Az>0. A nonzero defect gives a strict inequality in every coordinate, not just one. Triangle equality is earned by rotating the nonzero sum and comparing real parts. A^T uses only the already proved existence part, not simplicity circularly. Rescale the chain's bottom nonzero multiple of z before multiplying by w^T; w^Tz>0. Complex eigenspace reduces to real/imaginary parts. n1 and rank1 positive matrices pass; reducible triangular and periodic swap matrices explain why positivity is essential. |
| linear:lem:oscillation | A>0, x,y>0, c=min_i,j,k aij/akj in(0,1]: ratio intervals nest and their length contracts by<=1-c². | my<=x<=My gives the nested interval. For q=A(My-x), beta_i=q_i/(Ay)_i: q_i>=c q_k and (Ay)_i<=c^-1(Ay)_k give beta_i>=c² beta_k, bounding their oscillation by(1-c²)(M-m). | Different proof: normalized row weights p_ij=aij yj/(Ay)_i satisfy p_ij>=c² p_kj. Their overlap s=sum_j min(p_ij,p_kj)>=c². Remove the common overlap; each remaining row has mass1-s, so its expectation of xj/yj lies in an interval of length(1-s)(M-m). No division by M-m or q is needed. Equal rays, n1 and c1 give zero oscillation, not a division by0.240 exact rational probes support the general inequalities. |
| linear:thm:powerconv | A>0, w^Tz=1, x>=0 nonzero: A^kx/rho^k -> (w^Tx)z and matrix -> zw^T geometrically. | Nested ratio intervals shrink by the preceding lemma. The constant weighted average sum_i wi zi (u_i/zi)=w^Tx lies in every interval, identifying its limit. Boundary x becomes positive after one multiplication; standard basis columns give the matrix limit. | Independent spectral proof: P=zw^T satisfies P²=P and AP=PA=rho P. The complement ker w^T is stable and contains exactly the other Jordan blocks. Their eigenvalue moduli are<rho; the locally proved binomial/Jordan bounds make their normalized powers vanish geometrically. This independently identifies P for every vector. Handle c1 after one step, no0^0; no non-Perron eigenvalues means r0; zero blocks vanish in finitely many steps. The normalized-vector limit is z/||z||, not arbitrarily scaled z. |
| linear:prop:levels | Finite strongly connected directed graph with an edge, period h>=1: path length modulo h is well-defined, all h classes occur, every edge advances one. | Append the same return path to two paths from v0 to j; h divides both closed lengths and their difference. Appending an edge advances the residue. Follow edges for h-1 steps to exhibit all residues. | Reconstruct using any alternate basepoint: a path between bases changes all labels by a fixed residue, so the partition and edge rule do not depend on an accidental choice. Repeated visited vertices among the first h residues would force two distinct residues equal; hence h<=n. A one-vertex positive loop has h1; [0] is expressly outside the hypothesis. The proposition is now printed before the Frobenius proof invokes it. |
| linear:thm:frobenius | Nonzero irreducible A>=0: rho>0 algebraically simple with positive vectors, nonnegative eigenvector uniqueness; h peripheral values rho omega^k, each simple, full spectrum invariant under omega. | For n>=2, B=(I+A)^(n-1)>0. Commutation puts Az on B's Perron line; transpose gives w and w^TAz identifies the same scalar. Positive left weights bound every |lambda| by rho. Spectral mapping and Perron simplicity of B earn algebraic simplicity of rho for A. Peripheral triangle equalities transport phase along each edge; finite-cycle Bezout forces hth-root phase. Earlier levels give D^-1AD=omega A, producing all h simple peripheral values with multiplicity. | Adversarially rederive orientation: support i->j gives theta_j=phi+theta_i; D_j/D_i=omega, so conjugation gives omega A with the correct sign. The nonnegative defect has zero w-product and must vanish coordinatewise. Spectral mapping is justified by triangular Jordan blocks, including coincident polynomial images; rho's multiplicity cannot disappear. r0 with z>0 would force A0, impossible in this nonzero domain. Check positive1-by-1, directed cycles, bipartite graphs, reducible Jordan block, and 149 nonzero irreducible Boolean matrices through size3. No later cyclic-class lemma supplies a premise. |
| linear:thm:primitive | Nonzero irreducible A>=0: positive power iff h1 iff unique peripheral eigenvalue; normalized powers converge to zw^T. | Perron on a positive power excludes a second peripheral eigenvector. With h1, closed lengths at a base have gcd1; finite decreasing-gcd selection plus Bezout gives two nonnegative combinations P=N+1. For m>=N², m=rP+(q-r)N, proving all sufficiently large return lengths. Add fixed paths and maximize finitely many thresholds for a positive power. Write k=mq+s for convergence from A^q>0. | Different check of the semigroup step: residues of sums of return lengths modulo any fixed return length form a subgroup of the finite cyclic group; gcd1 makes every residue reachable. Choose a finite nonnegative representative sum per residue, then add multiples of that fixed length to cover every sufficiently large integer. This proves eventual positivity without signed walks. The supplied consecutive-length proof checks N0 separately, q>=N>r, and finitely many ordered pairs/remainders. Positive power also gives reachability; [0] would falsely satisfy the old sole-peripheral clause, so is explicitly separated. |
| linear:thm:wielandt | Primitive real A>=0, n>=2: A^((n-1)^2+1)>0. | A positive power gives strong connectivity and period1. A shortest cycle has s<=n-1, since otherwise cycle decomposition gives period n. B=A^s is primitive by eventual positivity, with loops at each vertex c of that cycle. A shortest B-path c->j padded to n-1 gives A^(s(n-1))_cj>0. Reach the cycle from i in<=n-s steps, then move along it to exactly n-s. Thus exponent N=n+s(n-2) works and N<=(n-1)^2+1. A has no zero row, so every later power stays positive. | Reconstruct the path concatenation with weights: each chosen walk contributes a strictly positive product, and the matrix product contains that product with no cancellation. The first-hit path has at most n-s outside vertices; padding happens on the cycle, not at an assumed loop of A. B connectivity follows from its positive powers, not from A connectivity alone. n2 forces s1 and exponent2. The sharp W walk obstruction works for every n>=2; exact Boolean tests n2..12 and all small irreducible supports corroborate the bound but do not prove it. |
| linear:cor:markov | Row-stochastic P>=0, irreducible h1: unique positive stationary probability row pi, P^k ->1 pi and every probability mu converges to pi. | P1=1 gives eigenvalue1 and the maximum-coordinate bound gives rho<=1. Positive left Perron vector normalizes to pi; simplicity gives uniqueness. Primitive matrix convergence with z1 and w pi yields1 pi. Multiply by mu with mu1=1. | Independently the invariant direct sum span1 plus ker pi and the Jordan power bounds give the same limit. Check that probability rows multiply on the right and normalization pi1=1 makes the rank-one limit idempotent. P[1] is stationary immediately; the two-state swap is irreducible but h2 and oscillates. Absolute eigenvalues and possible Jordan polynomial factors, rather than an unspecified signed lambda2, determine decay. |

## Exercises after comparison, in printed order

The first complete derivations are in APPA-PROMPT-FIRST.md. Supplied answers
for monotonicity and nonnegative existence were already mathematically sound;
they do not use each other circularly. Reconstructed both independently.

| Key | Actual answer comparison and adversarial B | Grade/repair |
| --- | --- | --- |
| linear:ex:perron2 | Quadratic discriminant is strictly positive; rho>max(a,d), z=(b,rho-a). Directly substitute each coordinate and use positive trace to compare a possibly negative second root. b,c cannot vanish in this domain. Hint now gives a discriminant discovery path rather than the answer. | 1 retained |
| linear:ex:rowsum | Supplied max/min coordinate proof and propagation along every positive edge earn both equality cases. Independent left-vector weighted average makes equality force every row sum equal. Zero1-by-1 handled directly; no irreducibility-free equality claim. | 1 retained |
| linear:ex:minmaxcw | Left-vector inequalities earn both sides and z attains the minimum, not just an infimum. Independent coordinate comparison against z gives the same bounds. All xi>0, w^Tx>0; scalar multiples are allowed. | 2 retained |
| linear:ex:monotone | Supplied w-product chain uses an arbitrary maximal-modulus complex eigenvector, not the following general nonnegative-Perron exercise. Equality forces B|y|=rho_B|y| and |y|>0, then a positive weighted sum of B-A vanishes only if A=B. Independent maximum-weighted-coordinate argument proves the non-strict bound; adversarial equality checks every nonnegative defect. B0 forces A0. | 2 retained |
| linear:ex:nonneg | Approximation A+eps J is positive. Monotonicity bounds rho_eps below by rho_A; bounded normalized vectors have a common subsequence, and the limit equation makes the eigenvalue limit an actual eigenvalue of A, giving the reverse inequality. Independent joint extraction works without monotonicity of the full sequence. Includes nilpotent and zero A, boundary vectors and repeated roots; no root-continuity theorem imported. | 2 retained |
| linear:ex:cycleperiod | Supplied directed-cycle Fourier vectors and bipartite period2/sign similarity are correct, but original request for full bipartite eigenvalues was not answered. Add the full positive BB^T eigenvalue construction, its kernel/rank argument and all zero multiplicities. B: for q>=p, block determinant gives X^(q-p)det(X²I_p-BB^T) for X!=0, hence identically, corroborating every multiplicity. The one-vertex edgeless graph has no positive period. | 1->2 for the completed full spectrum; no original spectral target lost |
| linear:ex:diagpos | A loop makes gcd1. With every loop, shortest paths padded at their destination give all entries of A^(n-1)>0. Independent walk-weight multiplication verifies strictness. n1 uses A0=I1 and A itself positive. | 1 retained |
| linear:ex:twostate | Supplied pi and complementary projections E,F have all four relations E²E,F²F,EF=FE0,E+FI. Direct matrix induction corroborates P^k=E+(1-a-b)^kF. State k0 separately when a+b1, rather than unexplained0^0. Exact rate |1-a-b| includes negative alternating mode and one-step convergence at zero. | 1 retained |
| linear:ex:pagerankrate | Original eigenvalue proof is correct for its implicit damping interval but does not by itself justify a sharp O(alpha^k) error in the presence of Jordan blocks. State alpha in[0,1), extend the prompt/hint/idea/write-up to unique stationary row even with zero v, and prove contraction/Cauchy convergence with complete finite geometric bounds. B: quotient the column action by constants to recover the eigenvalue bound independently; the zero-sum row argument directly earns the error. alpha0 is one step, n1 trivial, alpha1 periodic examples excluded. | 2 retained; original eigenvalue target retained, convergence target added |
| linear:ex:leslie | Determinant expansion now explains every sign and zero-root multiplicity. The last positive fertility defines an irreducible leading block, earning positive-root existence even when f_n0. Strictly decreasing Euler–Lotka sum earns uniqueness and threshold at1. B: solve survival rows and use a maximum ratio against the resulting positive vector to bound every complex eigenvalue. All f0 gives nilpotent L and no positive root, explicitly outside that clause. n1 and empty survival product included. Hint no longer suggests unearned Descartes as an alternative. | 2 retained |
| linear:ex:doublystoch | Uniform row stationary, primitive limit J/n. The supplied permutation-law proof actually assumes a fixed state-independent random position permutation; the prompt now states it and independence of repeated choices. B: every deterministic position permutation bijects all d! deck orders, so its transition matrix is a permutation matrix and a fixed probability mixture is doubly stochastic. Primitive alone fails for positive matrix with both rows(3/4,1/4). One configuration is trivial; deterministic shuffles on more configurations cannot approach uniform. | 2 retained; intended random-permutation model made explicit |
| linear:ex:wielandtsharp | Supplied excursion decomposition and converse realize exactly an+b(n-1), a>=1,b>=0 for positive closed walks. Mod n-1 forces a>=n-1 at forbidden exponent(n-1)², so an is already too large. Independent walk supports n2..12 check the obstruction and next exponent. Explicit n>=2 and positive-length hypotheses exclude n1 nonexistent vertex2 and the empty walk. | 3 retained |

## Unnamed arguments, examples, figures and narrative

The entire source was read, not only the tabled environments. Groups for the
later keyed exposition pass are: standing notation/r-function; finite Delta/K
compactness; triangle equality; left normalization/Jordan chain; the exact
A=[[2,1],[1,2]] example; normalized directions/Jordan spectral estimate;
projective-ray metric; weighted walks/path deletion/cycle gcd; irreducibility
criterion; finite return semigroup; eventual positivity; stochastic row-norm
bound; absolute gap; PageRank contraction; Leslie recurrence/growth proportions;
rabbit adaptation; and the final story connection. Each is reconstructed here
and in the source, but no automatic bulk exposition approval is assigned.

For the2-by-2 example, diagonalize on(1,1),(1,-1); independently multiply its
displayed expression and check t0. It gives3^t/2(1,1)+1/2(1,-1). The rabbit
matrix instead has characteristic X²-X-1; direct multiplication of(1,phi)
and phi²=phi+1 earns phi and juvenile proportion1/phi²=.381966.... Its
square is[[1,1],[1,2]]>0. This is a stage model with adult retention, explicitly
an extra entry beyond the displayed Leslie form. Nonzero initial population
and normalized proportions are now stated. Taking sums of the Perron limit
gives a positive constant C; S_k/rho^k->C implies S_(k+1)/S_k->rho.

Actual period figure: all11 directed edges checked, strong connectivity earned;
classes{1,2},{3,4,5},{6,7} advance cyclically. The displayed1->3->6->1 cycle
earns gcd exactly3, not merely divisibility by3. Independent Boolean powers
confirm reachability and period. Actual PageRank figure: all15 links and all8
node diameters checked. Exact rational elimination with alpha17/20 gives
rounded ranks(A,B,C,D,E,F,G,H)=(.329,.169,.351,.029,.036,.040,.027,.019).
Independent exact iterative distributions obey the proved contraction bound
around that same rational vector. C has6 incoming links, A and B each2 with
the stated sources. Teleportation means C sends its entire *link-following*
share to A, not its entire probability. Node diameters approximate
1.30 sqrt(pi_i/pi_C) within.006cm; caption now says approximately proportional.

The old50-iteration/six-digit statement is false: P=I on two states with
uniform teleportation and start(1,0) has coordinate error .85^50/2>1e-6.
General coordinate error is<=alpha^k, .85^85>1e-6>.85^86. Main text now
earns the bound before using it, independently of the later exercise.

Actually opened full print page406 of immutable447ac825 (printed396), all text,
graph nodes/links and caption. A/C black-on-dark labels have weak contrast;
source now makes only those labels white. B remains black on its lighter fill.
No corrected-render approval yet. Its mathematical50-step claim is superseded.
The447 manifest has496 reading/495 print pages, KDP496, spine1.1641in,
same-build wrap,85 public hashes, actual EPUBCheck5.3.0 zero messages and actual
output-check pass. This snapshot predates all appendix repairs and transfers
no final visual approval.

Removed the unattributed English rabbit quotation and replaced it by a concrete
recurrence; no claim of verbatim translation or1202 surviving source is made.
Removed the unearned sharp tanh projective-contraction/fixed-point/infinite
dimension catalog; retain and prove the projective-ray metric and keep the
Birkhoff reading reference. This loses those incidental outward connections,
not any named result, original exercise target, or bound used in the appendix.
Other historical bibliography metadata still need the whole-book primary-source
pass. Full old/new/domain/grade/loss disclosure is V3-014-curricular-disclosure.json.

Incoming question is the rabbit stage ratio; the answer is a positive direction
with graph-controlled periodicity. The next appendix asks a different spectral
question: what can symmetry diagonalize? All main prerequisites here are already
earned, including local finite analysis. No future optional route supplies a
premise. Written cadence review replaces the stock personified conclusion with
the two concrete readings of the eigenvector equation; no spoken/human session
is claimed.
