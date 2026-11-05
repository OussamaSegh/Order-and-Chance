# V3-004 — Chapter 3 internal double reconstruction

Read the entire chapter, all seven named proofs,14 prompt/hint/idea/write-up
sets and the actual necklace plate. CH03-PROMPT-FIRST.md records solutions made
before opening supplied hints/solutions. This is internal AI review, not formal
verification or independent human assessment. Bibliography metadata and final
rendered pages remain separate.

| Key | Domain/claim | Reconstruction A | Adversarial B / boundaries |
| --- | --- | --- | --- |
| thm:cayley | Any group G embeds in permutations of its underlying set; finite ordern embeds inSn | L_g bijective with inverseL_g^-1; L_gh=L_g L_h; L_g(e)=g gives trivial kernel | Construct image inverse L_g->g and verify the multiplication directly. Trivial and infinite groups work. The finite labelling step needs no additional permutation theorem. |
| thm:orbstab | Any group action/set, orbit partition, coset-orbit bijection and conjugate stabilizers; cardinal formula whenG finite | Reachability is equivalence relation; stabilizer passes difference test; gG_x=hG_x iff g.x=h.x. Expand stabilizer ofg.x by conjugating | Reconstruct the orbit map's equal fibres gG_x, each with |G_x| members. Nonfree singleton/one-dark-bead cases give orbit1/6. EmptyX gives empty partition; point clauses requirex inX. G/G_x is a coset set even for nonnormalG_x, explicitly stated. |
| thm:burnside | Finite group acting on finiteX, number of orbits equals average fixed counts | Double count(g,x) withg.x=x. Each orbit contributes|O||G_x|=|G| | Independently sum1/|O_x| overx: each orbit contributes1; substitute|G_x|/|G| and exchange finite sums. EmptyX gives0; trivialG gives|X|. No division by a zero orbit: only nonempty orbits used. |
| thm:polya | FiniteG acting on finiteX, positive numberk of colours; unweighted and formal-weighted orbit counts | Fixed colouring is constant on each cycle; fixed monomial sum is product of sum_c w_c^j. Weighted pair counting gives one orbit weight after division|G| | Reconstruct coefficients by fixing a colour multiplicity vector: apply ordinary Burnside to that invariant subset of colourings, giving the identical coefficient. EmptyX has one empty colouring and empty product1. Cycles/disjoint decomposition now proved locally before use; weight independence is not an assumption of free action. |
| thm:classeq | FiniteG, representatives of nonsingleton conjugacy classes; n=z+sum[G:C(x_i)] | Conjugation action stabilizer=C(x); orbit size index. Singleton iff central. Sum class partition | Independent partition by equal conjugates shows centralizer fibres; each size dividesn. Abelian/trivial groups have empty noncentral sum. Exact D4/Q8 class enumeration supports1+1+2+2+2, not a merged singleton. |
| cor:pgroup | Nontrivial finite group of orderp^k, k>=1; center at leastp | Each noncentral index is a nontrivial prime-power divisor, hence0modp. Class equation makes positive center size divisiblebyp | Reconstruct the congruence as counting fixed points of conjugation: all nonsingleton orbits size divisiblep. k1 gives wholegroupcenter. Definition now allows the trivial p-group (k0), while this corollary explicitly excludes it; its actual asserted domain is unchanged. |
| thm:cauchy | FiniteG, primep divides|G|; element of exact orderp | Product-one p-tuples count|G|^(p-1). Cyclic shift preserves product-one by conjugation even noncommutatively. Orbits1/p; fixed count positive multiplep, so a nonidentity constanttupleg withg^p=e | Reconstruct reverse rotation and fixed-tuple equivalence; all nonidentity fixed elements have orderp by earlier order lemma, not a converse of Lagrange. p2 inverse-pair proof independently checks the boundary. No Sylow/circular prime-order existence used. |

## Exercises: second check against the prompt-first record

| Key | Reconstructed A / answer | Adversarial B, hint and grade |
| --- | --- | --- |
| ex:cubefaces | Five face-cycle types give(3^6+6*3³+3*3⁴+8*3²+6*3³)/24=57 | Independent actual signed-coordinate rotations on six normals yield57 colour orbits. Check all24 rotations, not axes. All table entries match. One star retained. |
| ex:fermatnecklace | Prime-length nonconstant colourings have orbitp; k constants leave p dividingk^p-k | Distinct derivation from integer( k^p+(p-1)k )/p. k0 andp2 included; general integerk follows reduction modulo p, while colourcount uses k>=0. One star. |
| ex:classesD | D4 andQ8 both have class sizes1,1,2,2,2; full classes as prompt-first record | D4 conjugation by generatingr,s preserves reflection exponent parity; Q8 centralizers ofi,j,k size4 exclude merging. Distinct explicit singleton classes kept. Equal class equations do not imply isomorphic groups. One star. |
| ex:p2 | Center cannot have orderp because cyclic quotient forcesG abelian; fullcenter. EitherC_p² orC_p xC_p | Independently count a^i b^j for independent orderp elements: equality puts a power in the trivial intersection, forcing both exponents0modp. Source's subgroup-product cardinality now explained by this argument. p2 agrees withC1 order4. Two stars. |
| ex:smallestprime | Coset-action kernelK<=H, image divides|G| andp!, so image has order1orp; indexp excludes1 and forcesK=H | Reconstruct inclusion/indices without assuming coset action faithful. Atp2 recovers index2; inS3 an index3 subgroup is nonnormal and smallest prime is2, demonstrating necessity. FiniteG now explicit in prompt. Two stars. |
| ex:bracelets | Rotation sum84 plus reflection sum72 gives13; reversal pair001011/001101 | All64 words give14 rotational and13 dihedral orbits. The actual figure contains exactly these14 representatives and correct orbit labels. Source claimed the pair was marked, but it was not; two outer rust circles now identify precisely that pair. Two stars. |
| ex:graphs4 | Edge-action cycle index(t1^6+9t1²t2²+8t3²+6t2t4)/24 gives11 graphs and3 with3edges | Independently classify all64 edge subsets under24 vertex permutations; three-edge representatives have degree sequences2220,2211,3111. Coefficient(20+36+16)/24=3 and all induced edge cycles checked. Two stars. |
| ex:commuting | Probabilityk/n; center fraction<=1/4 and noncentral classes>=2 givek<=5n/8 | Separate centralizer sum gives z/n+(1-z/n)/2<=5/8. D4 exact commuting-pair count40/64 confirms equality; Q8 also40/64. Uses earlier cyclic-central quotient proof, not simple-group machinery. Three stars. |
| pb:sieving | Recurrence with outside-range terms0 gives polynomial. Root evaluation binom(n/m,k/m) or0; average gives fixed-weight necklaces andn6k3 answer4 | Distinct generating-product proof: product(1+q^r t) at primitive mth root is(1-(-t)^m)^(n/m); coefficient sign cancels q^(k(k-1)/2), including evenm. Exact integer polynomial remainders modulo cyclotomic polynomials check all n1..12,k0..n andm|n. Independent subset-weight coefficients checked throughn9. Source limit is now cancellation of finite geometric sums, not unproved complex analysis. Three stars. |
| pb:patterns | Cycle constraintf(gx)=s f(x), choicesfixed(s^ell), yields productsum_{j|ell}j c_j(s). Binaryexchange necklaces8; cubepatterns15 | Independently enumerate cube face-colour orbits under24 rotations and6 renamings; also count partitions into<=3blocks. Burnside rows(729,1,0),(27,3,0),(81,9,0),(9,1,9),(27,27,0), weighted1,3,2 and1,6,3,8,6, give2160/144=15. Unused colours handled by fullpaletteaction. Two stars. |
| pb:landau | Normalizeclass equation intoEgyptianfractions, remainder>=inverse earlierdenominatorproduct and<=k/nextdenominator; yields|G|<=k^(2^(k-1)). Atmost3classes gives1,C2,C3,S3 | Different product-bound inductionP_i<=k^(2^i-1) yieldssameorderbound. Enumerate reciprocal tuples for k2/3: (2,2);(3,3,3),(2,4,4),(2,3,6). Original source appealed to unproved order6classification; added Cauchy,index2C3,involution andconjugation proof. Explicitly exclude denominator1 for k>1. Two stars retained. |
| pb:nilpotent | Fitting unique decomposition gives sumN_k/GLk=q^(n²)/GLn; subtract successive equations to obtainN_n=q^(n²-n); identity shift givesunipotents | Source's different telescoping rational induction checks sameformula. Exact exhaustiveA^n tests forq2,n0..3 andq3,n2..3 match. All factorsq^j-1 nonzero sinceq>=2. Kernelstabilization and nilpotencyindex bound now justified locally; n0 map/inverse treated separately. Three stars. |
| pb:flags | Firstline recursion gives[n]_q!; complements aregraphs oflinear maps henceq^(k(n-k)); flagstabilizeruppertriangular givesGLn formula | Independent ordered-basis count product(q^n-q^j), factorq^binom(n,2)(q-1)^n[n]_q!. Extremek0,kn,n0 giveuniquecomplement/emptyflag. Quotientvectoroperations/basis/correspondence now taught beforeuse. q1 isformal and(c) requiresremove(q-1)^n first; no oneelementfield asserted. Raised fromone totwostars foractual multisteppath. |
| pb:touchard | Rotatepnewlabels; fixedpartitions either allnewlabelsinoneblock orallsingletons, countedB_(n+1)+B_n | Followblockorbit: anoninvariantblock haspdisjointtranslates, oldpoints cannotoccurinall, soallnewblocks mustbesingletons. Extendedshiftformula provenonlyonBellsequence andits shifts, withfull binomialoperator induction. ExactBellrecurrence checks primes2,3,5,7 andallaccessible p^m<=125; n0 included. Twostars. |

No target is weakened. Definitions/zero conventions are made explicit, the
order-six classification and quotient-vector-space proof are supplied locally,
and the original source's asserted Touchard extension is now fully justified.
All local computations support the written proof reconstructions, not vice versa.

The rest of the complete chapter was read for first-use/story: action-on-cosets
well-defined because changingx toxh leavesgxH unchanged; colouring action requires
g^-1, checked by composition. Transitivity requiresoneorbit (emptyset hasnone).
The necklace rotation lengths are n/gcd(n,r) by the earlier element-order formula,
so the gcd-cyclecount is earned. The opening's ternary130 and binary14 are different
stated questions, both correct; repetitive binary calculation after Burnside can
be compressed without deleting the one concrete worked count. Formalcolourweights
are commuting variables over rationalcoefficients; no characteristic-p division
by|G| is attempted. Pgroup/Fqconventions and allzero-dimensional cases are recorded.

Incomingquestion: how many descriptions correspond to one object? Outgoing:
finitegroup actions turn divisibility into forced prime-ordersubgroups; the next
chapter studies permutations themselves and parity before Sylow. The future Sylow
and character-table references are outlooks, not premises in these proofs.

Actual all14 drawn bitstrings and their orbit sizes were independently parsed
from the figure and matched to all64binarywords. New exactGaussian,nilpotent,
Bell/Touchardchecks and the historicalcheckerpass. Native-size/grayscale/final-page
visualreview and bibliography/history reconciliation remain outstanding.
