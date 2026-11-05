# V3-015 — Symmetry Diagonalises: first solutions before answers

Internal AI working record, not acceptance. Read the entire main appendix
(lines1–797) and twelve prompts(798–859) at e00b5836. No hint or supplied
solution from this appendix has been opened. The first derivations below
precede comparison. Actual figure sources and research metadata remain unread.

1. linear:ex:circalg. For n>=1 over C, I,S,...,S^(n-1) have independent
first rows and span the circulants, giving dimension n. Polynomial products
reduce modulo S^n-I and commute. Adjoints replace c_k by conjugate c_k and
S^k by S^(-k), still in the span. Invertible elements have inverse in the
algebra by Fourier interpolation, or Cayley–Hamilton constant term nonzero.
(I-tS)^-1=(I+tS+...+t^(n-1)S^(n-1))/(1-t^n), t^n!=1.
B: multiply the geometric polynomial on each side; inspect n1/t0 and both
complex conjugation and shift orientation. One star.

2. linear:ex:circ3. Write s=a+b+c and Q=a²+b²+c²-ab-bc-ca, so N=sQ.
Modulo3, Q=s², hence3|N forces3|s and3|Q, so9|N. Thus residues±3mod9
are impossible. Conversely N=3m+1 uses(m+1,m,m), N=3m-1 uses(m-1,m,m),
and N=9m uses(m+1,m-1,m), for every integer m, including negatives and0.
B: direct expand all three parameter families; exact residue enumeration
checks necessity. Main example's sign claim is false at a=b=c!=0: N0
but s!=0. State the equality case rather than certify the old assertion.
Two stars retained.

3. linear:ex:fourier. F²_jk=(1/n)sum_l omega^((j+k)l)=1 if k=-jmodn,
else0. Thus F²=R, R²=I and F4I. Any eigenvalue lambda obeys lambda4=1;
no claim every fourth root occurs for every n. B: act on each Fourier basis
vector and compare reversal. n1/n2 endpoints, no0 denominators because n>=1.
One star.

4. linear:ex:dualgroup. Restrict a character of GxH to Gx{0} and{0}xH;
the pair reconstructs it since(g,h)=(g,0)+(0,h). This proves inverse maps,
homomorphism and bijection, including trivial factors. For Z/n, send a to
chi_a(x)=omega^(ax); equality is tested at1, all characters arise from the
nth-root value there. B: compare orders and evaluations on generating
coordinates. Finite abelian contract made explicit. One star.

5. linear:ex:convolution. Substitute x=y+z in the finite transform sum:
sum_x,y f(y)h(x-y)bar(chi(x)) factors into hat f hat h.
Expand f in the orthogonal character basis to get sum|f|²=(1/N)sum|hat f|².
For M_xy=m(x-y), (Mf)(x)=sum_y m(x-y)f(y)=m*f after renaming the summation
variable. B: direct expand sum_chi|hat f|² and use dual orthogonality;
test nonsymmetric kernels to catch transform signs. Singleton group and
zero functions included. Two stars.

6. linear:ex:walsh. Order word/character pairs by their first bit; its
character factor is(-1)^(x1 t1), giving blocks[[H,H],[H,-H]]. Compute Hf0
and Hf1 recursively, then their sum/difference. T(n)=2T(n-1)+2^n,
T0=0 gives T(n)=n2^n scalar additions/subtractions. B: butterfly order
can instead add/subtract f0/f1 first and apply H to each. H0=[1] and
n0 zero operations. Two stars.

7. linear:ex:krawgen. Expand the t negative and n-t positive factors of
(1-z)^t(1+z)^(n-t); choosing j negatives for degree k gives exactly K_k(t).
Replace t by n-t and z by-z to get K_k(n-t)=(-1)^k K_k(t). Put z1:
2^n when t0 (the empty factor is1), otherwise0. B: elementary subset
sign sum gives the same coefficient and total. Integer0<=t<=n, n0 allowed.
One star.

8. linear:ex:gausssign. For a square a=r², substitution x->r x gives
g(a)=g1. For a nonsquare, aD is the set of nonsquares; since
sum_nonzero zeta^u=-1, 1+2sum_nonsq zeta^u=-g1.
Equivalently g(a)=sum_u eta(u)zeta^(a u)=eta(a)g1 after u->a^-1u,
with eta0=0. Under p=1mod4 and g1>0 the square-indexed eigenvalues
are(-1+sqrt p)/2. B: exact cyclotomic coefficient comparison for each
nonzero a, without numerically choosing a square-root sign. Two stars.

9. linear:ex:paleyself. Require p prime=1mod4. A nonsquare multiplier
bijection swaps the square/nonsquare nonzero differences, thus adjacency
and nonadjacency. B: permutation similarity gives same spectrum; in the
character basis J-I-A has degree p-1-k=k on constants and eigenvalues
-1-lambda on nonconstants, swapping the two nontrivial values with their
equal multiplicities. One star.

10. linear:ex:paleyramsey. Squares mod17 are{1,2,4,8,9,13,15,16}.
Any edge(u,v) maps by x->(x-u)/(v-u) to(0,1), preserving adjacency
because v-u is a square. Common neighbours of0/1 are{2,9,16}; none
are adjacent to each other (differences3 or10 up to sign are nonsquares).
Thus no4-clique exists, while{0,1,2} is a triangle, so clique number3.
Self-complementarity gives independence number3. Colour K17 by Paley
edges/nonedges: no monochromatic K4, hence R(4,4)>=18.
B: enumerate all triples/quadruples exactly and verify both colours.
The sqrt17 bound gives at most4 and does not itself exclude a4-clique.
Define Ramsey number locally; if existence is needed, earn the elementary
R(a,b)<=R(a-1,b)+R(a,b-1) recurrence by splitting a vertex neighbourhood.
Two stars.

11. linear:ex:plotkinsharp. Equality in the k1 Delsarte chain forces
all positive A_i with i>=d to have i=d. It also forces
sum_|T|1(sum_x in C chi_T(x))²=0, so for each coordinate the0/1 counts
are equal. B: sum ordered distances by coordinates: if M=|C| and r_j
ones in coordinate j, d M(M-1)<=sum_j 2r_j(M-r_j)<=nM²/2.
Equality forces both all nonzero pair distances d and r_j=M/2 for all j.
n0 gives a one-word equality case with no coordinates; otherwise balance
forces M even. Empty C cannot achieve a positive bound. Two stars.

12. linear:ex:lpthree. For n8, K1(t)=8-2t, K2(t)=2t²-16t+28.
f(t)=(t-4)(t-8)=2K0+2K1+(1/2)K2. It is<=0 at all integer t4..8,
and f0=32. Thus 2|C|<=sum_i A_i f(i)<=32, giving16 using exactly
the k1/k2 inequalities. Construct16 codewords by evaluating all affine
Boolean functions a0+a1x1+a2x2+a3x3 on the8 points of F2³. Differences
are constant1 (weight8) or a nonconstant affine function (balanced by a
translation, weight4); all16 functions are distinct. Its distribution is
A0=1,A4=14,A8=1. B: fix one coordinate in at least half the code, then
delete it. Plotkin at(7,4) bounds that half by8, hence |C|<=16.
Verify the16 words and all120 distances exactly. Three stars.

Main-source findings before answer comparison: an essential Hoffman bound is
imported from future Volume8 and must be proved locally; the sign example omits
the a=b=c equality case; simple cycles need n>=3; normal/adjoint terminology
and strongly regular parameters need definitions before use; Hermitian
conventions must match C11's linear-first convention. Code distributions divide
by|C| despite allowing the empty code, d0/n0/singleton conventions are unstated,
LP maximum needs finite boundedness/attainment earned, equal numerical distance
eigenvalues need multiplicities combined, polynomial generalized binomials/
leading coefficient and Bose–Mesner closure need proofs. FFT claim for arbitrary
n needs padding beyond the earlier radix-two result, and the actual future
Fourier chapter is V5ch06. Nonabelian group-determinant factorization is a
separate unproved outward claim; preserve it only if actually earned rather
than mistaking C11's square-sum result for a proof of polynomial irreducibility.
