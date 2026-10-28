# Initial audit: sums, counting and finite probability

Baseline: `3259d462860e13150fc6cb15ecb0e3109f95b5ed`. Source locations below
refer to that commit, not to the subsequently restructured manuscript. Audit only:
no chapter edits have been made by this reviewer. Read the full 758-line
`ch01-sums.tex` and 673-line `ch08-counting-probability.tex`, including every
exercise, hint, solution and challenge note; examined relevant vector figure
sources and the existing review/check script. The older review reports are
historical evidence, not a substitute for this reading.

## Existing coverage and inventory

### Original Chapter 1

| Source lines | Existing content | Prerequisites and assessment |
|---|---|---|
| 1–36 | Historical opening: Gauss legend carefully distinguished from earliest report; Nicomachus, medieval induction, Pascal triangle; two portraits | Strong opening; preserve. References are supplied, but this review did not independently retrieve their original texts. |
| 38–43 | Integer division; Bézout; coprime cancellation; Euclid's lemma; prime existence and unique factorisation | Already present, not a missing topic. Very compressed and before well ordering is stated. Needs terminology and placement repair. |
| 45–96 | Sigma notation; dummy indices; empty sums; linearity, index shifts, rectangular and triangular double sums; arithmetic/geometric progressions; odd-number sum; factored double sum; Gauss/gnomon figure and think prompt | Preserve. A good concrete route into reindexing. Clarify empty-product convention and define factorial before its first use later. |
| 98–153 | Well ordering; weak/strong induction with proofs; converse well ordering; prime-factorisation minimal counterexample; horses fallacy; strengthened induction; tromino induction and figure | Strong, necessary, at appropriate level. Avoid proving prime factorisation twice without explaining that the second proof illustrates a method. |
| 155–186 | Telescoping theorem with proof; rational telescopes; factorial sum; consecutive-product sum; square sums; telescoping products | Strong from-scratch examples. Products/factorials are used without a displayed definition. |
| 188–254 | Binomial coefficient by subsets; Pascal, factorial formula, binomial theorem with proofs; row sums; double counting; Vandermonde with counting and coefficient proofs; triangle/hockey-stick figures and think prompts | Preserve. “Any commutative ring” is premature undefined vocabulary; state real/complex cases and explain general algebraic extension as an outlook. |
| 256–322 | Finite differences; binomial polynomials; difference identity; Newton existence/uniqueness by matching degrees; coefficient formula; polynomial summation; examples and figure | Existing substantial treatment. Needs minimal polynomial vocabulary and a direct proof of the difference identity to remove a later root-counting dependency. |
| 324–353 | Lattice-path/binomial bijection, proof, path/reflection figure; alternative Pascal/Vandermonde/hockey-stick interpretations; Catalan introduction; Gauss portrait | Natural new Chapter 2 material. Preserve each object and the proof, not a second duplicate path theorem. |
| 355–382 | Pattern-versus-proof workshop; polynomial mimicking powers of 2; arbitrary sixth value; figure; mission summing k(k+1); hints, full solution and proof checklist | Preserve; substantive discovery teaching. A short proof checklist from Chapter 0 can be invoked rather than duplicated. |
| 385–704 | 17 exercises, each with a hint, “How to find it” and “Write-up” | Full inventory below. |
| 484–501, 706–735 | Three challenge items and notes: Faulhaber (general symmetry argument supplied), odd Pascal entries/Lucas, squarefree central binomials/Granville–Ramaré; closing bridges to arithmetic | Preserve and distinguish elementary challenge proof from referenced advanced theorem. |
| 737–758 | Sources: Concrete Mathematics, Engel, Benjamin–Quinn, Nelsen, Stanley, Renault, Edwards, Rashed, Rabinovitch, Nicomachus, Granville, Glaisher, Granville–Ramaré, Knuth, Golomb, Theisinger, Sigler, Hayes | Retain all references. No evidence supports deleting any of them. |

### Original Chapter 8

| Source lines | Existing content | Prerequisites and assessment |
|---|---|---|
| 1–27 | Historical opening: Pascal–Fermat, Huygens, Montmort/Bernoulli/Euler, weak law, birthday, coupon collector, Erdős–Szekeres, Monty Hall; portraits | Split the motivations, preserving sourced substance; new Chapter 2 may motivate hats as a finite count, Chapter 9 may retain interrupted games/weak law. |
| 29–55 | Sum/product/bijection rules; complement, circular seating, polygon diagonals, Fibonacci decomposition; maps/injections/permutations, multisets/stars-and-bars, pigeonhole with proofs; Dirichlet outlook | Already rich counting, not merely review formulas. New Chapter 2 core. |
| 57–80 | Inclusion–exclusion think prompt, theorem and indicator proof; sieve/Venn figure; probability-weighted interpretation and Bonferroni pointer | New Chapter 2. Define indicator explicitly before the product proof. Postpone expectation/probability-weighted reading to Chapter 9. |
| 82–104 | Hat prompt; exact derangement theorem and proof; e^-1 limit and factorial error; nearest integer; recurrence pointer; two-panel count/Poisson figure | Split finite formula from later analytic/probabilistic interpretation; see migration plan. |
| 106–154 | Sample space, axioms, uniform and conditional probabilities, event independence, random variables, law, mean, variance, standard deviation and product experiments in one paragraph; first rules with proofs; total probability; Monty Hall and tree; indicator expectation example | All required topics exist, but too compressed for intended readership. Sequential examples/definitions are essential. |
| 156–185 | Independence of random variables, pairwise versus joint independence, covariance; products and variance of sums with full proof and counterexample; square-root fluctuation scale | Preserve. Product-model proof could be made explicit. A covariance-matrix bridge to new Chapter 6 is justified. |
| 187–222 | Bernoulli, binomial, hypergeometric and discrete uniform laws, moments and proofs; explicit N=1 exclusion/degenerate case; finite-population correction; simulation/concentration figure | Preserve. No need to add measure-theoretic distributions. Define p∈[0,1], n∈N and 0^0 convention for endpoint mass formulas. |
| 224–254 | Markov and Chebyshev with indicator proof; coin example; pairwise-independent weak-law bound and Bernoulli corollary with proof; correct distinction between finite-sample concentration and infinite-path strong law | Already strong concentration coverage. Keep the finite model interpretation explicit rather than assuming an infinite sequence on one finite sample space. |
| 256–293 | Arithmetic/Poisson/probabilistic-method bridges; portraits; Bayesian-test workshop with exact posterior 1/6 and conditional-independent retest 99/124; figure; sample-size caution | Preserve. This is a useful workshop, not generic motivation. |
| 296–642 | 17 exercises with full hint and solution triples; includes nontrivial probabilistic-method and asymptotic problems | Full inventory below. |
| 422–424, 644–650 | Ménages/Touchard, Ramsey records and explicit construction outlook, birthday waiting asymptotic challenge and notes | Preserve as clearly referenced advanced outlooks, with scopes adjusted when counting moves. The birthday constant 2/3 is stated, not proved by the sketch. |
| 652–673 | Sources from Feller, Flajolet–Sedgewick, Mitzenmacher–Upfal, Alon–Spencer, David, original Montmort/Euler/Bernoulli/Chebyshev, von Mises, Erdős/Szekeres, Ramsey references, Selvin/vos Savant, Barner, Renault, Bertrand/André, Bonferroni/Rényi, Lucas/Touchard/Bogart–Doyle, Dirichlet | Retain valid bibliography. Dynamic October-2026 records and historical dates remain source-verification work. |

## Corrections and changes justified by evidence

| ID | Classification | Evidence | Required or recommended repair |
|---|---|---|---|
| D01 | Structural improvement | Ch1 38–43 uses least positive integer before well-ordering axiom at 102 | Place arithmetic bridge after induction/well ordering, or explicitly declare well ordering in Chapter 0 foundational contract. Teach divisibility, prime, gcd, lcm, congruence, floor and factorial before use. |
| D02 | Essential correction of dependency | Ch1 273–276 proves difference identity by infinitely many roots, citing later polynomial theorem | Factor common product directly: for k≥2, Δ binom(X,k)=X(X-1)…(X-k+2)[(X+1)-(X-k+1)]/k!=binom(X,k-1); check k=1 separately. No root theorem needed. |
| D03 | Essential correction of dependency | Ch1 ex:kbinom 395–397, solution 575–581 requires differentiation | Make double counting primary. Retain differentiation as explicitly optional return after calculus, or supply an algebraic k binom(n,k)=n binom(n-1,k-1) route. n=0 requires separate treatment of the derivative formula. |
| D04 | Essential correction of dependency | Ch1 ex:squares solution 600–607 uses Cauchy–Schwarz, now much later | Use (n+1)Σb_k²−(Σb_k)²=Σ_{i<j}(b_i−b_j)²≥0, derive directly, then point to later general Cauchy–Schwarz. |
| D05 | Essential correction of boundary case | Ch1 ex:intpoly 469–473 admits P=0, but solution 692 starts d=deg P | Dispose of P=0 explicitly (all coefficients zero), then take nonzero P. Do not silently assign deg(0) a finite degree. |
| D06 | Essential clarification of domain | Ch1 Fibonacci gcd exercise 416–422 does not specify admissible m,n for (c); arithmetic bridge defines gcd only when not both zero | State m,n≥0 and m+n>0, or adopt/prove gcd(0,0)=0 convention explicitly. Handle n=0 in (b) instead of descending to F_-1. |
| D07 | Essential clarification of boundary | Ch1 Catalan reflection 475–482, 697–700 uses endpoint (n−1,n+1) and factorial manipulations at n=0 | Set C0=1; perform reflection for n≥1; verify final formula separately for n=0. All Catalan mathematics otherwise sound. |
| D08 | Pedagogical enhancement | Ch1 binomial theorem 207 uses undefined “commutative ring”; Newton proof 286 calls family a basis before linear algebra | Explain minimal coefficient/degree language; matching leading coefficients already proves what is needed. Preserve generality in a short explicitly identified later-algebra comment. |
| D09 | Essential clarification of domain | Ch8 ex:stars 298–300, solution 484–485 permits k=0 and uses binom(n−1,k−1) for n<k without negative-top convention | State n≥0,k≥1. Positive solutions are 0 for n<k and binom(n−1,k−1) for n≥k. Optionally treat k=0 separately by the unique empty tuple when n=0. |
| D10 | Essential correction of foundational gap | Ch8 coupon 533 identifies expectation with an infinite indicator sum; only finite expectation and linearity were defined; existence of infinite sequence is granted but interchange is not justified | Prove finite tail identity for min(T,M), define countable nonnegative expectation as limit of truncations, and justify this particular tail-sum rearrangement via nonnegative rectangular partial sums. Or use finite truncated coupon experiments and define expected unlimited wait by their limit. Keep any admitted infinite experiment existence explicit. |
| D11 | Essential addition to explanation | Ch8 109 introduces roughly a dozen new definitions in one paragraph | Separate finite spaces/events and masses; conditional probability and Bayes; independence/product model; variables and distributions; expectation; variance. Give one short concrete example for each conceptual step. No need for conditional expectation detour. |
| D12 | Essential clarification | Ch8 87–102 uses D_(10−k), including D0 in figure law, without specifying D0 | Define empty permutation, D0=1, D1=0, D2=1. Retain exact formula at n=0. |
| D13 | Pedagogical enhancement | Ch8 ex:multinomial labelled one star at 362 but part(c) derives multinomial local asymptotics with Stirling | Give two stars, or mark part(c) as a challenging bridge; retain full exercise in Chapter 9 to avoid a Chapter 2 probability/calculus dependency. |
| D14 | Essential domain clarification | Ch8 surjection formula 375–381 permits zero source/target sizes and has (n−j)^k | State the combinatorial convention 0^0=1 for maps from the empty set, or give zero-size cases separately. n=0,k=0 yields 1; n=0,k>0 yields 0. |
| D15 | Essential domain clarification | Ch8 Ramsey expectation 416, solution 637 sums disjoint all-red/all-blue events; they overlap for k=0,1 | State integers n≥k≥2 for the formula and k≥3 for exponential lower bound. This does not weaken the intended theorem. |
| D16 | Pedagogical enhancement | Ch8 cycles exercise 327 introduces cycles of permutations without teaching cycle decomposition | Add a brief elementary permutation-cycle explanation in new Chapter 2, including a concrete cycle and orbit partition. This also prepares derangement recurrence. |
| D17 | Essential correction of claim scope | Ch8 birthday challenge 423 and note 650 state sqrt(pi N/2)+2/3+o(1) but supply only a leading-term heuristic and say the constant comes from “next terms” | Clearly identify the refinement as an advanced referenced result, not a proved exercise conclusion, or provide a genuine uniform error analysis. Do not claim the sketch is a complete proof. |
| D18 | Structural improvement | Ch1 limit exercises and Ch8 derangement exponential limit now precede rigorous limits/Taylor | Retain exact finite identities first; flag limits as a return after Chapter 3/7, and give their proofs there or a clear semantic reference. Do not treat numerical agreement as proof. |
| D19 | Pedagogical enhancement | Ch8 Monty exercise 353–360 presumes uniform car location and host constraints from earlier worked model | Restate inherited assumptions concisely, including 0≤q≤1 and informed host revealing a goat. |
| D20 | Editorial refinement | Ch1 560 says “nothing to discover” when a theorem is supplied | Replace with actual strategy: inspect the difference of proposed right sides, factor rather than expand. Supplied statements can still require discovery. |

None of these findings licenses deleting established arithmetic, spectral,
concentration or combinatorial material on an assumption of absence.

## Exercise-by-exercise findings and destination

Each row refers to a complete statement/hint/strategy/write-up triple, not merely
an exercise box. All 34 triples are present exactly once in the assigned baseline
files. “Sound” below means that the written argument was inspected and no defect
was identified apart from the stated domain/dependency items; it is not formal
verification or an assertion that every historical side remark was checked.

| Label | Baseline statement / solution lines | Destination | Review |
|---|---|---|---|
| ex:cubes | Ch1 387 / 559 | 1 | Sound induction; n=0 can be included explicitly. Retain. |
| ex:tel3 | Ch1 391 / 567 | 1 | Exact telescope sound; limit is an explicit Chapter 3 return. |
| ex:kbinom | Ch1 395 / 575 | 1 | Sound for n≥1; D03 and n=0 boundary. |
| ex:hockey | Ch1 399 / 583 | 1 | Sound Pascal/double-count proof and cube expansion. |
| ex:squares | Ch1 404 / 600 | 1 | Identity sound; D04 avoids unproved inequality. |
| ex:fermat | Ch1 408 / 609 | 1 | Sound cancellation and induction once arithmetic definitions supplied. |
| ex:fibgcd | Ch1 416 / 617 | 1 | Sound Euclidean reduction for admissible indices; D06. |
| ex:cubesgeo | Ch1 425 / 631 | 1 | Sound double-sum/L partition proof; three stars arguably generous but preserve familiar landmark unless full difficulty rebalance is done. |
| ex:harmonic | Ch1 431 / 641 | 1 | Sound unique maximal power-of-two denominator argument; define lcm. |
| ex:sumsq | Ch1 438 / 649 | 1 | Sound and excellent strengthened-induction example. |
| ex:odds | Ch1 443 / 655 | 1 | Sound block/triangular number argument. |
| ex:telprod | Ch1 448 / 660 | 1 | Sound finite products and factorial telescope; define empty product and return to limits. |
| ex:pascalmod2 | Ch1 452 / 666 | 1 | Sound coefficient parity induction and Pascal walk. |
| ex:fibsums | Ch1 460 / 674 | 1 | Sound telescopes and tiling account. |
| ex:binomfrac | Ch1 465 / 681 | 1 | Sound index shift, including n=0. |
| ex:intpoly | Ch1 469 / 690 | 1 | Sound Newton/negative binomial method; D05. |
| ex:catalan | Ch1 475 / 695 | 2 | Sound reflection and first-return recurrence; D07. Move fig:paths too. |
| ex:stars | Ch8 298 / 482 | 2 | Sound stars-and-bars for stated intended ranges; D09. |
| ex:birthday | Ch8 302 / 488 | 9 | Sound exact injection probability and exponential upper bound; valid n>365 treatment already supplied. |
| ex:pigeon | Ch8 314 / 495 | 2 | Sound consecutive-pair and odd-part box choices. State n≥1. |
| ex:phi | Ch8 318 / 502 | 2 | Sound prime-factor inclusion–exclusion; n=1 empty product yields 1 and should be stated. |
| ex:fixedvar | Ch8 323 / 511 | 9 | Sound factorial second moment; n≥2 explicitly supplied. |
| ex:cycles | Ch8 327 / 521 | 9 | Sound uniform cycle length/share argument; D16 prerequisite and n≥1. |
| ex:coupon | Ch8 335 / 530 | 9 | Finite phase calculation right; D10 foundational tail-sum gap. Specify n≥1. |
| ex:erdos | Ch8 340 / 539 | 2 | Sound injection of endpoint-length pairs into n² boxes; strong discovery example. Move fig:erdos too. |
| ex:monty | Ch8 353 / 547 | 9 | Correct distinction between unconditional 99/100 and evidence-conditioned posterior; D19. |
| ex:multinomial | Ch8 362 / 560 | 9 | Sound count, expansion and Stirling computation; D13 difficulty and a natural existing bridge. |
| ex:derangrec | Ch8 371 / 577 | 2 | Sound splice bijection and alternating correction recurrence; teach cycles. |
| ex:surj | Ch8 375 / 584 | 2 | Sound inclusion–exclusion and finite-difference connection; D14. |
| ex:bonferroni | Ch8 383 / 593 | 9 | Sound pointwise truncation; independence unnecessary, correctly observed. |
| ex:records | Ch8 391 / 598 | 9 | Sound combinatorial pairwise independence and finite-sum Chebyshev enclosure. Explicitly assume exchangeable continuous sample or uniformly random permutation, as text does in statement. |
| ex:poll | Ch8 400 / 617 | 9 | Sound 5556 sufficiency and three-point sharpness; normal estimate explicitly later outlook. |
| ex:ballot | Ch8 409 / 626 | 9 | Sound strict-positivity reflection; b=0 already handled. Good count/probability bridge. |
| ex:ramsey | Ch8 413 / 635 | 9 | Sound expectation bound and R(3,3) proof; D15. Floor-to-strict-real inequality is valid because Ramsey number is integer. |

## Concrete migration plan

### New Chapter 1

Retain original Ch1 opening, sums, induction, telescoping, binomial coefficients,
Vandermonde, finite differences/Newton and polynomial summation, workshop, sixteen
remaining exercise triples, all associated challenge notes and all pertinent
references. Move the complete lattice-path section (324–353) and complete Catalan
triple (statement 475–482; hint 553–555; solution 695–704) to Chapter 2. The Gauss
portrait at 353 may stay with Chapter 1; record its chosen location. Retain the
closing link to Catalan with semantic reference into Chapter 2.

### New Chapter 2

1. New concise motivating question; use Montmort's hats as a counting question
   with sourced historical attribution. Retain history rather than manufacture a
   different historical origin story.
2. Import original Ch8 29–80: three counting rules, worked examples, basic counts,
   pigeonhole, inclusion–exclusion and Venn/sieve figure. Replace later
   probability language by a precise forward note.
3. Import original Ch1 324–351: lattice paths and fig:paths. Existing Pascal and
   Vandermonde interpretations are new proofs, useful as alternate languages,
   not needless duplication of theorem statements.
4. Import Ch8 82–95 finite derangement count, with D0 convention. The limit in
   statement line 89, last sentence line 94, error and nearest-integer passage
   97 and figure 99–104 rely on later limits/Taylor or probability. Prefer putting
   the two-panel figure and full return in Chapter 9, where the Poisson panel can
   be an explicitly referenced outlook. A Chapter 2 forward note is acceptable.
5. Add only a small generating-function method section: coefficient encoding,
   product as convolution, a worked Fibonacci recurrence via coefficients, and
   its limits. Treat formal series coefficientwise (each coefficient is a finite
   sum); do not silently use analytic convergence or recreate Volume 4.
6. Add permutation-cycle language needed later and a decomposition workshop.
7. Collect the complete triples for ex:stars, ex:pigeon, ex:phi, ex:derangrec,
   ex:surj, ex:erdos from Ch8 and ex:catalan from Ch1. Preserve labels and
   all hints/strategy/write-up content. Appropriate figures are fig:venn,
   fig:paths and fig:erdos. Ch8 exact ranges for moved triples are recorded above.
8. A graph-theory survey is unnecessary. The concrete complete-graph definition
   can remain immediately before Ramsey in Chapter 9. Trees are optional
   enrichment and currently have no prerequisite justification for expansion.

### New Chapter 9

Retain original Ch8 106–293, sequentially expand the compressed vocabulary,
retain eleven remaining exercise triples including full multinomial problem,
all probability figures and Bayesian workshop. Keep full existing figure
`ch08-derangements.tex` here to preserve its probability panel; attach the exact
formula's semantic Chapter 2 reference. Preserve `ch08-birthday.tex` here because
its second panel is coupon expectation. The first two challenge topics may be
cross-referenced from Chapter 2; do not duplicate full boxes. All three advanced
challenge statements must be labelled as partial elementary tasks plus referenced
outlook, with no claim that the birthday refinement is proved. An elementary
arithmetic-probability closing example and a covariance-matrix bridge would
connect the established series themes without advanced expansion.

## Dependencies

- Chapter 0 logic/functions/relations → Chapter 1 precise induction statements.
- Well ordering → Bézout/minimal positive combination and minimal counterexamples.
- Finite sums + distributivity → Pascal/binomial/Vandermonde → Newton summation.
- Direct product identity → difference of binomial polynomials (no root bound).
- Chapter 1 binomials → Chapter 2 paths/stars-and-bars/inclusion–exclusion.
- Bijections + finite pigeonhole → Catalan, derangement recurrence and Erdős–Szekeres.
- Coefficientwise finite convolution → introductory generating functions.
- Finite counts → Chapter 9 uniform models; event algebra → conditional probability/Bayes.
- Finite sums → expectation → covariance → variance sum → Markov/Chebyshev → weak law.
- Chapter 3 limits/series + Chapter 7 exp Taylor → derangement e^-1 limit/error.
- Chapter 7 Stirling + Chapter 2 multinomial counts → Chapter 9 local probability bridge.
- Chapter 8 exponential tangent inequality → birthday bound.
- Countable nonnegative expectation/truncation must be explicitly proved or
  assumed only where unlimited coupon waiting is discussed.

## Verification actually executed

The reviewer ran an independent Python script using exact integers and rational
arithmetic, with **759 successful finite checks**. Checks included:

- All 17 original Ch1 and 17 original Ch8 statement/hint/solution label triples
  match as multisets.
- Cube sums, central-binomial square sums, weighted binomial sums and both
  binomial-fraction identities for n=0,…,20.
- Enumeration of every permutation for n=1,…,7 checking derangements, fixed-point
  expectation/variance, record expectation/variance.
- Direct strict-ballot enumeration for 1≤a≤6 and 0≤b<a.
- Surjection enumeration for source size 1,…,5 and target size 0,…,6.
- Hypergeometric mean and variance by enumerating every subset for 2≤N≤8,
  every K and every admissible n.
- The word-count integer 7,797,275 and the retest posterior 99/124.
- Independent floating evaluations: 23-birthday exponent exceeds log 2 by
  0.0000035043715616023263; n=600 multinomial Stirling main term is
  2.475289241831164×10^-7; two-sided fair-coin tail outside [31,69] is
  0.0000785013964559367. These support the rounded claims, not universal proofs.

Figure-source inspection checked matching values and geometric claims in Gauss,
finite-difference, path-reflection, hockey-stick, tromino, derangement, sieve/Venn,
Monty Hall, Erdős–Szekeres, Bayesian and birthday/concentration sources. The
Monte Carlo averages in the birthday/coupon and running-frequency figures were
not regenerated; no claim of reproducible simulation provenance is made. This
reviewer did not compile or render the whole book; full layout/PDF review belongs
to the integrating batch. Historical sources and dynamic Ramsey records were
not independently fetched in this audit. Existing citations should be preserved
and their status recorded accurately.
