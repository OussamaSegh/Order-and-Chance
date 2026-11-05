# V3-017 — Hadamard matrices, complete internal mathematics

Solo internal AI review, not independent human refereeing/formal verification.
Read every original/revised line, all six named proofs and both complete
prompt/hint/finding-idea/solution triples. APPD-PROMPT-FIRST was written before
opening hints/answers. Both supplied full solutions were already mathematically
correct and match the independent first constructions. No figure/table/bibitem
environment occurs in this appendix; every displayed matrix is fully in scope.
Global keyed exposition/context/history/voice closure remains separate.

## Actual earlier tools and order

Reopened C9 thm:cyclicmult133–187 in full: abelian invariant factors, all roots
of X^d-1 and field root bound force one cyclic factor, with trivial group direct.
Reopened thm:fq245–289 in full: splitting field of X^q-X, derivative -1 and
Frobenius close its exactly q roots under field operations; uniqueness follows
because every finite field of that size splits/generates the same polynomial.
Those proofs and their actual earlier tools are already in CH09-REVIEW, not
inferred from theorem titles. This appendix uses neither a later analysis
volume nor a future character-sum theorem. C1/V1 coordinate matrix multiplication,
transpose and dot products are sufficient. Define the Kronecker indices and
prove both identities locally before invoking them. Explicitly distinguish the
real-valued sign character/matrix arithmetic from field arithmetic inside chi.
Field orders are genuine odd prime powers p^d,d>=1; q1/characteristic2 excluded.
Hadamard order is a positive integer; no vacuous order0 convention is used.

## Six named arguments, full A and substantive B

| Key | Exact hypotheses/claim | Reconstruction A | Different/adversarial reconstruction B and boundaries |
| --- | --- | --- | --- |
| prop:hadamard-four | Real n-by-n sign matrix H,HHT=nI,n>2 implies4 divides n. | Negate columns to normalize first row. Other two rows have n/2 positives. Four column-type counts a,b,c,d give b=c,a+d=b+c and n=4b. | Instead permute columns to put second row's plus half first. Third row has zero sum on each half because both its total and its dot with second row vanish; each half therefore has equal signs, so n/2 even. n1/2 examples verified; n3 impossible, empty order excluded. Column negations/permutations preserve every pairwise dot. Original proof sound. |
| conjectures:prop:kron | Positive Hadamard orders m,n: H tensor K is Hadamard order mn; recursively S_(2^k) has order2^k,k>=0. | Entry products are signs; local index identities give Gram(H tensor K)=(mI) tensor(nI)=mnI; induction from1. | Direct row-pair factorization: (h_i tensor k_r) dot(h_j tensor k_s)=(h_i dot h_j)(k_r dot k_s), zero unless both row indices agree. Independently binary-index formula(-1)^(i dot j), prove recursion from leading bits and orthogonality by pairing columns differing in a nonzero row-difference coordinate. k0/m1/n1 checked. Correct original sentence's ambiguous/wrong S_(2^(k+1))-versus-order2^k indexing; full original intended family preserved. |
| conjectures:lem:chi | Odd prime-power q, real quadratic character: parity of generator exponents, multiplicativity, half squares, chi(-1), zero sum and every nonzero-shift correlation -1. | Even-order cyclic units give squares/even powers and unique order-two element -1. Half signs cancel. For c!=0, x!=0 gives chi(x)chi(x+c)=chi(1+c/x), and x->1+c/x bijects nonzero field onto field without1. | Genuinely different correlation proof: number N of pairs u²=t(t+c) is q+sum chi(t(t+c)), since a square has1+chi square roots, including zero. The invertible change U=2t+c,V=2u gives(U-V)(U+V)=c². Each nonzero first factor determines exactly one second, so N=q-1; correlation=-1. Verify inverse t=(U-c)/2,u=V/2 and invertibility of2/c. For chi(-1), X²-1=(X-1)(X+1) and odd characteristic identify the unique nontrivial square root of1. q3/5 and nonprime9/25/27/49 checked exactly; no sum is evaluated in characteristicp. Original proof sound. |
| conjectures:lem:jacobsthal | Qxy=chi(x-y), real sizeq: zero row/column sums,Q transpose=chi(-1)Q,QQT=qI-J. | Translation permutations yield sums0. Gram diagonal q-1, offdiagonal shifted correlation -1. Negating difference yields transpose sign. | Reconstruct Gram from the independent conic count rather than source inversion, track t=x-y,c=z-x, and verify both orientations of each offdiagonal. On constants Qzero; on vectors with coordinate sum0, QQT acts asqI, independently checking coefficientq and missing-J signs. No diagonalization theorem is needed. Every row/column dimension isq; q3skew/q5symmetric and extension fields checked. Original proof sound. |
| conjectures:thm:paley1 | Prime-power q=3mod4, S=[[0,jT],[-j,Q]], H=I+S: Hadamard orderq+1. | Qskew and zero sums give Sskew,SST=qI, hence S²=-qI. Every diagonal0 becomes1; offdiagonal remains signs. (I+S)(I-S)=(q+1)I. | Direct row proof avoids squaring S: top row(1,jT); other row(-1,Q_i+e_i). Norm²1+(q-1)+1=q+1; top dot other -1+0+1=0; distinct lower dot1+(-1)+Qij+Qji=0 by skewness. This checks every border and cross sign. q3 explicit full matrix agrees with prompt-first; nonprime27 exact. q1 impossible and wrong q1mod4 branch fails orthogonality. Original proof sound. |
| conjectures:thm:paley2 | Prime-power q=1mod4, symmetric S=[[0,jT],[j,Q]]; H=[[S+I,S-I],[S-I,-S-I]] is Hadamard order2(q+1). | Local zero sums/Gram give symmetricS,S²=qI. S±I are sign matrices. Square H: diagonal2(S²+I)=2(q+1)I and cross commutators0. | Different tensor derivation: A=[[1,1],[1,-1]],B=[[1,-1],[-1,-1]], H=A tensor S+B tensor I. Direct multiplication gives A²=B²=2I,AB+BA=0; therefore H²=2I tensor(S²+I)=2(q+1)I. Full sign/shape check separately, q5order12,9order20,25order52,49order100. Real signs remain distinct even when underlying field has small characteristic. Original proof sound; no weaker construction substituted. |

The optional unlabelled groups are also reconstructed: opening two sign rows;
row-length/Gram equivalence; real/field distinction; normalization symmetries;
full Kronecker index sum; tensor transpose; binary-index induction and character
homomorphism; divisibility/congruence compatibility; all border dimensions and
all displayed matrices. The new bridge replaces a duplicated PaleyI proof
summary: symmetric S would leave the term2S in(I+S)^2, so doubling cancels it.
It gives the next construction a concrete incoming question without filler.
These arguments will receive exact keyed exposition decisions in the global pass,
not automatic acceptance from this prose summary.

## Both exercise triples and discovery path

| Key | Comparison and second check | Grade |
| --- | --- | --- |
| ex:paley-h4 | Prompt-first gives actual16 entries and first/third dot0. Supplied hint recommends block multiplication; full finding idea/write-up has correct1->2->4 matrices and cancellation. B independently computes all six dot products and the binary-character pairing proof. Matrix source cells exactly match numerical reconstruction, every row norm4. No repair to valid original answer. | 1 retained |
| ex:paley-f3 | Prompt-first orders field0,1,2, chi0/1/-1 and builds all Q/H entries using x-y. Supplied hint/idea/full answer agree exactly, including all three lower-row products. B normalizes lower rows by -1, then the resulting three rows match Sylvester rows in order2,4,3; row permutation gives the same Gram. Direct actual-source matrix multiplication confirms4I. No transposed-character or border-sign correction needed. | 2 retained for assembling field indices and border, no new theory |

## Finite support and genuine corrections

check_appendix_d uses polynomial-coordinate arithmetic and verifies every
nonzero element's explicit inverse in each chosen quotient. Ten prime fields
and four nonprime fields9/25/27/49: all multiplicative character identities,
every nonzero-shift correlation and independent conic counts, all Q zero sums/
Gram/transpose identities, both full construction branches and wrong-branch
counterchecks. Actual source solution matrices are parsed and checked cell by
cell. All binary-index Sylvester matrices through64 and normalized small-order
obstructions through7 are checked exactly. These are finite support for the
full general proofs above, not a replacement for them. General field existence
comes from actual earlier C9, not these computations. Source contract guards
only catch domain/index/attribution drift and do not approve mathematics.

Only the Sylvester statement indexing and missing explicit conventions need
mathematical/editorial repair; preserve every six named/two exercise target,
all stars/full solutions. Add local Kronecker/Walsh justifications and teach
why the symmetric case calls for doubling. Explicit old/new/domain/addition/
research-scope disclosure is in V3-017-curricular-disclosure.json. No entire
Paley construction, extension-field case or advanced proof has been dropped.

## Research evidence and exact access limits

Access2026-11-05: actual arxiv2610.27175v1 introduction39–51 and classical
construction overview52–79 reopened, plus current abstract-page version history
showing only19October2026v1. The intro explicitly lists the twelve orders and
attributes their12August announcement; the paper's authors describe their own
checks. Source now presents a dated attributed report, rather than an unqualified
independent-verification assurance. No external new matrices downloaded/tested,
full new construction/research proof reviewed or human refereeing claimed.
This is a nonpremise outlook, not an ingredient in Sylvester/Paley proofs.

Actual Wiley Paley publisher record read: On Orthogonal Matrices, Journal of
Mathematics and Physics12(1933),311–320, firstpublishedApril1933,
DOI10.1002/sapm1933121311. Original PDF returned403, so do not claim its full text
read. Actual Sylvester primary collected-paper scan read: title/original-publication
header615, sections6–8 on619–623, especially power-of-two sign matrices and
orthogonality on621–622. It identifies Philosophical Magazine34(1867),461–475.
Text access loses some matrix images; attempted web screenshots returned textual
placeholders only, so no actual page-image inspection is claimed. Actual modern
primary construction text and our general proofs earn the stated mathematics;
this access limit concerns original-publication historical review, not an assumed
mathematical premise. No unsupported exact day-of-publication is added.

## Production scope

The immutable1fe85903 build predates these D changes and remains in progress.
No new D page/EPUB/reader visual approval is claimed. The completed1b94857e
snapshot and exactly opened pages are recorded separately. Final all-page/
grayscale/facing/narrow-wide digital/CIartifact inspection remains open.
