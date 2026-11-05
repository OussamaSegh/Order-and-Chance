# V3-025 — reopened complete C7 exercise triples

Solo internal AI review, no new blinded first-solve claim. Original C7 exposure
chronology remains CH07-RECONSTRUCTION. Every full prompt/hint/idea/writeup read.

## ex:unitsmodn

Domain: Integers k>=3, j>=0; unit group modulo2^k and360; least positive universal exponent.

Claim: 5^(2^j)=1+2^(j+2)t_j with t_j odd; order5 mod2^k exactly2^(k-2), units direct product of<5>and<-1>. Units360 invariant factors2,2,2,12 and least exponent12.

A: Start t0=1. Squaring gives t_(j+1)=t_j+2^(j+1)t_j², odd. Thus valuation exactlyj+2. Order is a power of2 by earlier Lagrange and group size2^(k-1); congruence atj=k-2 and failure atj=k-3 force exactorder. Powers5 are1mod4, while-1 is3mod4, so intersectionidentity; commuting product has full unit-group size. CRT8*9*5 restricts to unit groups, explicit powers2 mod9/5 give orders6/4. Splitprimepowers/right-align:2,2,2,12. Largest factor kills every coordinate, contains elementorder12, so least exponent12.

B/boundaries: Adversarial second reconstruction uses filtration of units1mod4: it has exactly2^(k-2) classes, and the proved order5 fills it; sign separates the other coset. Exact enumeration k3..13 and all96units360 agrees. Recompute powers2mod9=(2,4,8,7,5,1), mod5=(2,4,3,1). Characteristic2 field assertion is not used for integer residues2^k. New formal exponent definition before exercise earns both existence byLagrange and largest-factor formula; trivial group exponent1 distinguished.

Correction/comparison: Explicit j>=0 in prompt; all original claims, hint, full writeup and two-star grade retained. Negative j was not an intended integer valuation assertion; k3/j0 boundaries work.

## ex:nilpotent

Domain: Any field K; n>=0; nilpotentN onK^n means some positive powerzero.

Claim: Similarity classes correspond to partitions ofn, recovered from kernel powers; all five n4 classes and kernel rows.

A: N^m=0 gives minimal polynomial dividingX^m, so all monic positive-degree invariant factors are X^a_i. Degree sum n yields partition; actual earlier Jordan/structure proofs give existence/uniqueness, no assumption splitting before deriving these factors. A block shift ofsizea has kth kernel dimensionmin(k,a). First differences countblocks>=k; second differences count exactk. Forn4 rows are(1,2,3,4),(2,3,4,4),(2,4,4,4),(3,4,4,4),(4,4,4,4).

B/boundaries: Independently reconstruct chain-length counts from image filtration: rankN^(k-1)-rankN^k equals number chains oflength>=k, the same first-difference invariant. Exact explicit block matrices for all partitions n0..7 overF2/F3/F5 reproduce sizes by field row reduction. At n0 the partition/block list is empty and mu1; at N0 in positive dimension there are n blocks1. Two rows with initialkernel2 are specifically3+1 and2+2, distinguished atsecondpower.

Correction/comparison: Idea now uses annihilation rather than inferring factorization from eigenvalue wording. The closing comparison names the actual two partitions. Full original prompt/hint/answer/grade2 retained; entire changed triple reconstructed.

## ex:diagonalisable

Domain: Field K, n>=0, A inM_n(K); complex field for finite-order conclusion, k>=1.

Claim: A diagonalizable overK iff minimal polynomial is a product of distinct K-linear factors. Idempotents diagonalizable in every characteristic; finite-order complex matrices diagonalizable.

A: If diagonal, f(A)=0 iff f vanishes at every diagonal entry, so minimal polynomial is product over distinct entries. Conversely for nonzero dimension, mu haspositive degree, split distinct factors permit CRT idempotents e_i. (X-lambda_i)e_i is divisible by every distinct factor, hence mu, so rangee_i(A) is eigenspace. On an eigenvector forlambda_j, e_i(A) acts as delta_ij. Sum e_i(A)=I, giving spanning; apply projections to a zero sum for directness. Basis in each eigenspace diagonalizes. Handle n0 before applying CRT: empty matrix/basis, mu1. A²=A impliesmudivX(X-1), distinct over everyfield. A^k=I overC impliesmudivX^k-1, splitting by earlier complex roots and simple roots because derivative kX^(k-1)nonzero there.

B/boundaries: Separate Lagrange-polynomial route e_i(X)=product_(j!=i)(X-lambda_j)/(lambda_i-lambda_j); nonzero denominators from distinctness. These operators give explicit eigenvector decomposition and directness without guessing basis. Actual formal polynomial product/divisibility and derivative rules are earlierV1; no later separability theorem used. Exact all104 matrices n0..2 overF2/F3 compare polynomial factorization with rank of the full eigenspace span, including nonsplitting quadratic and repeated-root cases. Square-free alone is insufficient overR (rotationX²+1); incharp, I+nonzeroN withN²0 canhave orderp butis not diagonalizable, explaining C restriction.

Correction/comparison: Expanded every nontrivial projection implication in full reader-facing solution; handle n0 before invoking CRT theorem stated for at leastone factor. All original targets/hint/full answer/grade2 retained.

## ex:cyclicvector

Domain: Any field K, n>=0; empty vector family/C(1) conventions for n0.

Claim: muA=chiA iff a cyclic vector basis exists iff A similar to a companion matrix.

A: n0:mu=chi1, empty familybasis, uniqueemptyA=C(1). Forn>=1, invariant factors eachpositive degree and chi=product,mu=last. Equality iff onefactor, because earlier degreeswouldaddpositiveamount. In singlecyclicquotient degree n, generator1 givesbasis1..X^(n-1). A cyclic basis makeslastcolumn minuscoefficients of expressionA^nv, hencecompanion. Companion actsbyXonK[X]/f andannihilator(f), so minimal=char=f; similarity preservesboth.

B/boundaries: Independent direct cyclic-vector annihilator reconstruction: a degree<n annihilator ofv would contradictbasis independence; unique degree-n relation exists, commutation with powersA makes it annihilateallbasisvectors. Thus mu hasdegreen and equalsmonicchi. Exact104 small-field matrices independently compare minimal/characteristic polynomials and existence of full-rank Krylovbasis. Old unqualifiedhint r=1 fails atn0, where mu=chi1 butr0; explicit countermodel recorded, not disguised by excluding zero dimension.

Correction/comparison: Prompt and hint now state n0 conventions before last-factor argument. Full solution already treatedzero; it is reread/reconstructed, with original equivalence and two-star grade preserved.

## ex:sublattices

Domain: Positive integern; subgroups L<=Z² of finite indexn.

Claim: Unique L=Z(a,0)+Z(b,c), a,c>=1, ac=n,0<=b<a; exactlysigma(n)=sum_(a|n)a suchsubgroups.

A: Projectionsecondcoordinate is cZ; c0would give surjectionZ²/LontoZ, contradict finiteindex. Lagrange inquotient gives n(1,0)∈L, so horizontal sliceaZnonzero. Choose(b,c), reduceb moduloa. Any(x,y)∈L hasy=tc and subtractt(b,c) leaveshorizontal multiple(a,0), provinggeneration. Slice/projection determinea,c, andtwo choicesb differbya multiplea; chosenrangegives uniqueness. Determinant oftriangularbasisac givesindexbyprovedcor:index. Converse everytriple definesindexn, counta choices foreachdivisora.

B/boundaries: Separate direct coset reduction: subtract multiples(b,c) to puty in0..c-1, thenmultiples(a,0) toputx in0..a-1; two reducedpairs differinL onlyif bothcoordinates equal, givingexactac cosets without determinant theorem. Thus count also independent ofSmith/minors. n1 givesonlyZ²; n2 gives3 distinct kernels of nonzeroF2-valuedlinearforms. Infiniteindex excluded explicitly, not silently dividedbyzeroa/c.

Correction/comparison: Prompt now states n>=1. All intended finite-index classification/count/complete answer and three-star grade retained.
