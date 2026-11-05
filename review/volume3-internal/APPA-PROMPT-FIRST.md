# V3-014 — Positive Matrices: prompt-first reconstructions

Internal AI working record, not acceptance or formal verification. The entire
main text (lines 1–783) and twelve prompts (784–847) of the appendix at
447ac825 were read before opening any of its hints or supplied solutions.
These first reconstructions precede that comparison. Main-proof reading is
not blindness to the tools taught in the appendix. Figure data remain unopened.

1. linear:ex:perron2. Put D=sqrt((a-d)^2+4bc). Eigenvalues are
(a+d±D)/2. rho=(a+d+D)/2>max(a,d)>0 and z=(b,rho-a)>0.
The positive trace gives rho+lambda_minus=a+d>0, while D>0 gives
rho-lambda_minus>0, hence |lambda_minus|<rho. B: substitute both roots
in (X-a)(X-d)-bc and both coordinates in Az=rho z. One star.

2. linear:ex:rowsum. A positive left Perron vector w makes rho the
weighted average sum_i w_i(row_sum_i)/sum_i w_i. Thus both bounds and
their equality cases follow, including [0]. B: apply the componentwise
minimum/maximum to A1 and multiply by w; equality has no zero weight.
One star.

3. linear:ex:minmaxcw. For x>0, rho=sum_i(w_i x_i/(w^T x))
((Ax)_i/x_i). This gives both inequalities, with equality attained at z,
so the dual minimum is rho. B: compare x with z at a largest or smallest
ratio x_i/z_i. Two stars is reasonable for recognizing the dual argument.

4. linear:ex:monotone. Avoid depending on the following exercise.
For any eigenpair Ay=lambda y, choose t=max_i |y_i|/z_i, where Bz=rho_B z.
At a maximizing coordinate, |lambda| t z_i <= (A|y|)_i <= t(Bz)_i,
so rho_A<=rho_B. If equality, use an eigenpair with |lambda|=rho_B.
The nonnegative defect B|y|-rho_B|y| has zero product with B's positive
left vector, hence is zero. Irreducible eigenspace uniqueness gives
|y|=cz>0. Then (B-A)|y|=0 implies every entry of B-A is zero.
The exceptional B=[0] forces A=[0] directly. B: weighted maximum norm
proves the bound; positive left weights force every possible strict defect
to survive. No general nonnegative Perron theorem is imported. Two stars.

5. linear:ex:nonneg. Let eps tend to zero through 1/k; choose positive
Perron vectors x_eps in the simplex and eigenvalues r_eps of A+eps J.
They are bounded by the row-sum bound. Coordinatewise Bolzano–Weierstrass
gives a common subsequence converging to x>=0, sum x=1, and r>=0.
Passing through the finite equations gives Ax=rx. Monotonicity from the
preceding reconstruction gives r_eps>=rho_A, while r is an eigenvalue
of A and therefore r<=rho_A. Thus r=rho_A. B: test triangular nilpotent
matrices, A=0, repeated spectral roots; no continuity-of-roots premise.
Two stars.

6. linear:ex:cycleperiod. A directed n-cycle, n>=1, has period n and
all nth roots of unity, with geometric-coordinate eigenvectors. A connected
undirected bipartite graph with at least one edge has period2: every closed
walk is even and traversing an edge back and forth gives length2.
In a bipartition, A=[[0,B],[B^T,0]], and conjugating by diag(I,-I) gives -A,
so multiplicities are symmetric. Its full spectrum is ±sqrt(mu) for each
positive eigenvalue mu of BB^T, plus p+q-2rank(B) zeros. Earn the finite
Hermitian spectral argument locally if no exact earlier proof is available;
alternatively the characteristic identity X^(q-p)det(X^2 I_p-BB^T), q>=p,
follows by block elimination for X!=0 and polynomial identity. Isolated
one-vertex graph is a necessary exception to the period claim. The original
unspecified graph has no unique numerical eigenvalue list; give the block
description and retain its intended full spectral target. Two stars if this
description is explicitly requested. B: paths2/3, complete bipartite graphs,
unequal part sizes and a single isolated vertex.

7. linear:ex:diagpos. A positive diagonal entry is a cycle of length1,
so irreducibility forces period1. If every diagonal entry is positive,
take a shortest i-to-j path of length<=n-1 and pad it by loops to exactly
n-1. For n=1, A^0=[1]>0, and A itself is positive. B: direct walk products,
not an assumed primitive-exponent bound. One star.

8. linear:ex:twostate. Set s=a+b, r=1-s and pi=(b/s,a/s).
With Pi=1 pi, P=Pi+r(I-Pi), Pi^2=Pi and Pi(I-Pi)=0. Thus for k>=1,
P^k=Pi+r^k(I-Pi); P^0=I separately, including r=0. The exact decay
factor is |1-a-b|<1, with stationarity after one step if a+b=1.
B: diagonalize on 1 and (a,-b), or check the four entries by induction.
One star.

9. linear:ex:pagerankrate. State 0<=alpha<1 and v>=0, sum v=1.
For every complex row y with y1=0, yG=alpha yP and
||yP||_1<=||y||_1. A left eigenvector for lambda!=1 has y1=0, so
|lambda|<=alpha. The same finite inequality gives contraction on
probability rows: ||mu G^k-nu G^k||_1<=alpha^k||mu-nu||_1.
Existence can be obtained by the Cauchy sequence of iterates, since
successive differences have summable geometric bounds; uniqueness follows
from contraction. For a stationary pi, total variation <=alpha^k and each
coordinate error <=alpha^k. Thus .85^50 is about .000296, not six-digit
accuracy;86 steps guarantee coordinate error below1e-6. B: quotient by
the invariant constants for the eigenvalue bound, direct zero-sum row
recurrence for the error estimate, including alpha=0 and zero entries of v.
Two stars. Eigenvalue moduli alone do not remove Jordan polynomial factors.

10. linear:ex:leslie. Take n>=1, s_i>0 and at least one f_i>0,
ell_1=1 and ell_i=product_{j<i}s_j. Expand the first row of XI-L to get
X^n-sum_i f_i ell_i X^(n-i). Let m=max{i:f_i>0}; the first m-by-m block
is irreducible, giving a positive root rho. The Euler–Lotka function
F(t)=sum_i f_i ell_i t^(-i) is strictly decreasing on t>0, so F(t)=1 has
exactly that root. The vector z_i=ell_i rho^(-(i-1)) z_1 is strictly
positive even when f_n=0; a weighted maximum-coordinate argument shows
that every eigenvalue has modulus<=rho. F(1)>1 iff rho>1.
B: use the eigenvector recurrence rather than determinant expansion,
and split the characteristic polynomial into the first m block and
the remaining zero eigenvalues. Include n=1, f_n=0 and all f=0
(the latter is nilpotent and excluded from the positive-root assertion).
Two stars. Convergence in the main application requires x0>=0, x0!=0,
and the stable proportions are z/sum z.

11. linear:ex:doublystoch. Column sums1 make the uniform probability
row stationary; primitivity gives uniqueness and convergence to J/n.
For a shuffle, explicitly require a state-independent random permutation
of the d positions: each deterministic position permutation induces a
permutation of all d! orders, hence its matrix is doubly stochastic, as
is their fixed probability mixture. Primitivity then gives the uniform
law on orders. B: invert each position permutation to count exactly one
preimage per destination; do not infer double stochasticity from
primitivity alone. A two-state positive matrix with both rows(3/4,1/4)
is the counterexample to the overly broad wording. Two stars.

12. linear:ex:wielandtsharp. Assume n>=2 and a positive-length walk.
Every departure from1 must first follow1,2,...,n; before its return to1
it may take the n->2 detour any number of times. Concatenating visits
to1 gives length an+b(n-1), a>=1,b>=0. If this equalled(n-1)^2,
reduction modulo n-1 would make a a positive multiple of n-1, forcing
an>=n(n-1)>(n-1)^2. For n=2 the same conclusion says no length1
loop at1. Upper positivity is the proved Wielandt bound, so the exponent
is exactly(n-1)^2+1. B: enumerate Boolean walk supports for small n,
including n2, and independently check the modular obstruction. Three stars.

Main-proof findings before answer comparison: [0] is irreducible under
length-zero reachability but has no positive period; the primitive theorem
therefore needs an explicit domain exception. The cyclic-level proposition
is used before it is printed. The variational argument needs its finite
compactness step earned; the power-method limit needs unit normalization.
The graph-cycle gcd must be reduced to finitely many cycle lengths before
using Bezout. Sharp-exponent proof otherwise reconstructs correctly.
