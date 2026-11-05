# V3-016 — Linear Algebra Method: first reconstructions before answers

Internal AI working record, not acceptance. At1b94857e read the entire main
appendix(lines1–917) and all ten prompts(918–961) before opening any of this
appendix's hints or supplied solutions. No hint/answer exposure yet. Actual
figure sources and bibliography remain unread. The following first solutions
precede comparison; earlier main/appendix mathematics is already known.

1. combinatorial:ex:eventown. Pair the first2floor(n/2) inhabitants and use
every union of complete pairs; all intersections are unions of pairs and all
sizes even, giving2^floor(n/2) clubs.
On F2³, the affine planes are{a·x=b} for the7 nonzero a and b0/1. Each has4
points by rank/nullity, all14 are distinct. Equal normals with different b
give empty intersection; different normals are independent over F2, so the
two equations have rank2 and exactly2 solutions. Empty and whole space keep
all intersections even. Thus16 clubs attain Eventown2^4. A couples family
has size2 clubs, while this family has nonempty sizes4/8, so cannot come from
pairs, even after relabelling. B: these are exactly the16 affine truth tables
in appendix B, with distances4/8; use |A intersect B|=(|A|+|B|-distance)/2
for two planes to get0/2 and verify all120 pairs exactly. Tentative grade1/2:
the plane count needs its local kernel description; reassess after answer.

2. combinatorial:ex:nearpencil. For n>=3, the n-1 pairs{i,n} intersect
each other in{n}, and the final[n-1] intersects{i,n} in{i}. All n sets are
distinct, hence m=n,lambda1. Do not borrow Fano from future V9. Define its
seven points as F2³\{0}, and lines{u,v,u+v} for distinct nonzero u,v.
There are42 ordered distinct point pairs,6 per line, hence7 lines. Their
spans have dimension2 in dimension3; two different such subspaces intersect
in dimension1, hence exactly one nonzero point. Thus all line pairs meet
in exactly one point, giving m=n7. B: enumerate the7 triples and21 line
intersections; every point lies on3 lines and every pair on one. n0 is
outside Fisher; explicit n>=3 avoids degenerate near-pencil nomenclature.
One star once the construction is supplied locally.

3. combinatorial:ex:simplexdist. Every e_i+e_j has coordinate sum2, an
affine hyperplane of dimension n; translate by2/(n+1) times the all-ones
vector and choose an orthonormal basis to identify it isometrically with R^n.
For distinct two-subsets I,J, squared distance is4-2|I intersect J|, hence
2 or4. There are binom(n+1,2) distinct points. For n3, translate by(1/2,...,1/2):
complementary pairs give opposite unit vectors on3 mutually perpendicular
axes, the regular octahedron. B: Gram matrix/difference coordinates and all
six points/15 distances. Need define two-distance as *at most* two values:
n1 gives one point and n2 equilateral triangle has only one distance.
n0 gives no edges/empty set. One star.

4. combinatorial:ex:sdistance. For finite points a_i with allowed positive
distances b1,...,bs, attach f_i(x)=product_l(||x-a_i||²-b_l²). Degree<=2s,
zero at every other point and nonzero on a_i, so independent. Polynomials
in n variables of total degree<=2s have binom(n+2s,n) monomials: add a
slack exponent to total2s and use stars-and-bars. If fewer actual distances,
pad the list by arbitrary positive values; if s0, an empty product is1
and at most one point exists. Infinite sets are excluded by applying the
finite argument to any D+1 points, where D is the bound. B: direct evaluation
matrix diagonal and independent rank argument; n0 gives one possible point.
Two stars.

5. combinatorial:ex:fwmodthree. Use p3,L{1,2}, size residue0 outside L;
modular Frankl–Wilson gives sum_i0² binom(n,i)=1+n+binom(n,2).
B: directly form (v_A·x-1)(v_A·x-2) in F3; its own value2 is nonzero,
other values0; multilinear reduction degree<=2 gives that dimension.
n0/1 and m0/1, repeated sets ruled out by the intersection condition.
One star.

6. combinatorial:ex:cdsharp. Write A=a0+d{0,...,a-1},
B=b0+d{0,...,b-1}, d!=0,1<=a,b<=p. Every index0..a+b-2 is a sum of
the two ranges; when a+b<=p+1 these are a+b-1 distinct residues, so
the bound is attained, including a+b=p+1 and singleton cases. Over Z4,
A=B{0,2} have sumset{0,2}, size2<3=min(4,2+2-1). B: translate and
scale to reduce to literal intervals and enumerate small primes/all lengths.
One star.

7. combinatorial:ex:egzsharp. For n>=2 take n-1 zeros and n-1 ones.
Any chosen n terms have between1 and n-1 ones, hence nonzero sum modn.
For n1 the zero-term list cannot supply one term. B: every possible
number of ones and all small subset selections; same valid sharpness
target already appears earlier in the C12 workshop but is freshly checked.
One star.

8. combinatorial:ex:quadric. Homogeneous degree<=2 in n>=3 has origin0;
corrected Chevalley–Warning with nonnegative degree bound2<n gives another
zero, including characteristic2 or the zero form. For x²+y²+z², a nontrivial
zero with z!=0 gives(x/z)²+(y/z)²=-1. If z0, at least one of x,y nonzero;
say y!=0 gives(x/y)²=-1, hence add square0; if only x nonzero the equation
x²0 is impossible in a field. For p2,1²+0²=-1 directly. B: for odd p,
the square set including0 has(p+1)/2 elements, so it intersects-1 minus
itself, giving two squares summing-1 without a quadratic-form classification.
Reopen the actual V2 pigeonhole proof if importing it, not just the title.
Two stars; division by z must not be assumed.

9. combinatorial:ex:capplane. Any five-point cap has at most2 points in
each line. In any parallel class of3 lines, the5 points must distribute2,2,1,
so exactly2 pairs have that direction. There are4 directions, giving at most
8 pairs, contrary to binom(5,2)=10. Any larger cap contains5, so upper4.
Construction{0,1}² has no distinct zero-sum triple: each coordinate's number
of ones is0 or3, forcing all three words equal. B: affine-normalize any
three cap points to0,e1,e2 (they are noncollinear); forbidden third points
on their lines exclude(2,0),(0,2),(2,2). The remaining candidates are
(1,1),(1,2),(2,1), any two of which form a line with one of0,e1,e2.
Thus only one can be added, giving4 again. Enumerate all126 five-subsets
and both explicit affine arguments. Two stars.

10. combinatorial:ex:dvir. State n>=1 and q a prime power>=2.
If |K|<D=binom(q+n-1,n), rank/nullity gives nonzero f of total degree
d<=q-1 vanishing on K. For every direction v!=0 choose a+tv subset K;
h(t)=f(a+tv) has q roots and degree<q, so vanishes identically.
Its leading t^d coefficient is the top homogeneous part f_d(v).
For d>0, f_d also vanishes at0, so it vanishes on the entire Fq^n grid.
Each variable degree<=d<q, and the earlier grid lemma forces f_d0,
contradiction. If d0, a nonzero constant cannot vanish on even one such
line; existence of a direction uses n>=1. B: reconstruct the evaluation
linear map and line-leading coefficient separately, check n1 (K must be
the full field), q2 and both constant/nonconstant cases. Original prompt
without n>=1 is false at n0: the direction condition is vacuous, empty K
qualifies but bound is1. No genuine positive-dimensional target need be lost.
Three stars.

## Main-proof findings and second-check leads before answer comparison

All main proofs have been read once, but no acceptance is assigned here.
Oddtown, perpendicular dimension and Eventown reconstruct over every stated
field, including characteristic2; make bilinear dot/no conjugation explicit
after the prior appendix's Hermitian product. Fisher's Gram proof is sound
including its one possible zero correction; m0 is trivial, handle m<=1.
lambda0 counterexample is empty set plus n singletons. Clubs construction
already repeats the opening proof; trim repetition in later voice pass.

Two-distance polynomial span bound is valid, including n0 with a loose bound.
The quoted Blokhuis refinement can be earned locally for n>=1: any relation
sum c_i f_i+linear=0 has degree4 coefficient sum c_i=0 and degree3 part
sum c_i a_i=0. Evaluate at a_j and multiply by c_j then sum: the linear
terms cancel and b²c² sum c_j²=0 forces all c_j0 over R, then the linear
polynomial0. Thus adding n+1 affine functions gives the stronger bound
binom(n+2,2); n0 direct max1. Exact plane/space classification claims in
the caption/prose remain unearned and should be proved, attributed as a
nonpremise research limit, or removed with disclosed loss; do not certify
them from the weaker general proof. Midpoints use at-most-two distances.

Both Frankl–Wilson polynomial/evaluation proofs reconstruct correctly; the
nonuniform sorted evaluation matrix is upper triangular because j<i entries
vanish, including empty products and sizes in L. Explicit Ramsey theorem's
two sets of residues versus actual intersection sizes are correct for all
primes including2. binom(27,8)=2220075 and t3=379 must be independently
recomputed. Growth discussion supplies an *upper bound* on clique/independence
size, not proof it is asymptotic to the bound. Its future V4 random-graph
reference is stale: actual V1 ch09 ex:ramsey has the finite expected-count
proof and must be read. Current explicit-Ramsey/Borsuk record claims require
primary-source checking or qualified/removal disclosure; no status inherited.

Grid lemma needs n0/empty-grid domain handling; CN needs explicit nonnegative
integer exponents and selected finite grids renamed clearly. Its monomial
remainder proof preserves the top coefficient correctly, with strictly lower
total degree for every out-of-bounds monomial. Cauchy–Davenport proof handles
a+b>p and the factorial-nonzero regime; a=b1 contradiction assumption would
force an impossible empty sumset, handle that trivial boundary explicitly.

Chevalley–Warning repeats the degree-minus-infinity defect already independently
found in C12: equations0 and X in one variable pass the old sum convention
but have1 zero. Require n>=1 and nonnegative degree bounds d_j with sum<n,
including zero equations/empty systems. EGZ forms have degree *at most*p-1,
not exactly when all coefficients vanish. The unqualified finite-field extension
sentence needs its exact divisibility stated: the same indicator argument in
Fq proves characteristic-p divisibility, since N*1=0 there; it does not itself
prove divisibility by q. Do not silently certify a stronger extension from
that calculation. The named prime theorem and every EGZ target can be preserved.

Support lemma correctly uses sum of echelon rows, not a union-of-supports
argument failing in small fields. Diagonal slice-rank contraction proof is
sound, including finite fields and coefficients; define rank0/empty sum and
existence explicitly. Cap tensor partition handles all repeated triples via
characteristic3, and all monomials by a priority rule, with no double count.
The numerical x=.59 bound2.7552 is rationally checkable. The purported optimum
2.7551 is a rounded approximation, not a valid exact upper base; r=(sqrt33-1)/8
gives base approximately2.755105. Differentiate the rational cube to earn the
optimum if retained. Advanced cap-size tables/current lower-record/tri-colour
claims need actual proofs/research qualification, not approval from the main bound.

The final ungraded p>=5 arithmetic-progression suggestion must use
x-2y+z=0, not x+y+z=0: only the former is identically true on the diagonal.
The same finite tensor proof then gives size<=3 times the number of exponent
vectors in{0,...,p-1}^n of degree<=(p-1)n/3. This supplies an earned optional
route without misusing characteristic3. Replace stock greatest-triumph/filler
ending with actual object/space/count and the next appendix's question.

## Subsequent comparison and source-order finding

After this first record, all C hints, all ten complete supplied solutions and
all bibliography entries were actually read. Both actual figure sources were
read in full. No C mathematical acceptance yet. The supplied Fano solution
already contains a full local vector-space definition/proof; the defect is
the prompt's future Volume9 prerequisite, not absence of that answer proof.
The supplied quadric answer already handles z0 correctly. The supplied capplane
answer gives a third valid method, parity of lines through an outside point.
Dvir's answer handles degree0 after assuming K nonempty; make n>=1 explicit
and earn nonemptiness from an actual nonzero direction. Do not misattribute
these already-correct answer arguments as new mathematical repairs.

Actually reopened V1 main.tex30–56 and V1 ch09-probability ex:ramsey full solution
812–824. Printed V1 order is0language,1sums,2counting,3sequences,4orders,
5complex,6polynomials,7linear,8integrals,9inequalities,10probability.
Filenames are NOT printed chapter numbers. New C reference must say probability
Chapter10, not9. Appendix A's new reader-facing Chapter5 sequence citations
are also wrong and must become3; global source-reference reconciliation is
still open, so reopen changed A evidence explicitly. Existing proof-file
hashes/read arguments remain valid; no theorem availability is inferred from
the wrong literal chapter number. V2 printed order1divisibility,2primes,
3congruences,4arithmetic,5primitive,6quadratic,7squares,8Diophantine(sourcech09),
9continuedfractions(sourcech08),10Gaussian,11characters(sourcech14).
