# Volume 2 continuity: initial source and prerequisite audit

Date: 2026-11-03. Branch: editorial/volume2-continuity-foundations-20261103.
Status: partial source audit, **not** a theorem-by-theorem mathematical sign-off.

## CI failure and repair

The initial PR #97 run, https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41551781706, passed the earlier source and export unit tests but failed before typesetting at the series metadata check. The new four-part main.tex disagreed with the old Volume 2 part names in common/series-catalog.json.

Repaired the canonical catalog and its cover-source SHA-256 in tools/assets/series/manifest.json. The original catalog checksum matched the existing manifest before the update. The common metadata file is a shared build input, so this change may cause CI to rebuild all fifteen volumes.

## Source-level baseline

Reviewed the eleven chapters in the approved printed order plus the preface and field guide. The inspection counted:

| Check | Result |
| --- | --- |
| Chapter sources and parts | Eleven chapters, four approved parts |
| Exercise identifiers | 144 |
| Hint identifiers | 144, in matching order |
| Solution identifiers | 144, in matching order |
| Distinct manuscript-local labels | 266 |
| Duplicate local labels | Zero |
| Missing local reference targets | Zero |
| Main-body forward reference occurrences | 15 |
| Exercise, hint, solution and other forward reference occurrences | 18 |

The 15 main-body forward references were examined in their surrounding text. They concern previews of modular inverses, continued fractions, Gaussian integers, characters and sieves; none was an explicit invocation of a later theorem as an earlier displayed proof premise. This is a **reference-context scan**, not a certification that every implicit theorem prerequisite has been found.

The 18 exercise-area forward references warrant a separate challenge audit, notably links to character-problem machinery introduced only in the final chapter.

## Repairs made during this audit

1. **Canonical book parts.** Synchronized the new part names with the series metadata and cover-manifest checksum.
2. **CRT versus sieve.** Replaced a statement incorrectly identifying the Chinese remainder theorem with the exact sieve identity. The manuscript now distinguishes CRT's reconstruction of compatible residue information from the Möbius/inclusion-exclusion formula for finite sieving.
3. **Unproved ring claim.** The Diophantine chapter referred to the Gaussian/Eisenstein chapter as though it developed arithmetic in the ring Z[sqrt(-2)]. It does not. The revised prose treats the example as beyond the local toolkit, verifies only the displayed examples, and directs broader theory to Volume 13.
4. **Stale printed numbers.** Replaced the advanced reciprocity solution's old Volume 2 Chapter 4/5 numbers with stable references to the actual orders, reciprocity and characters chapters.
5. **Wrong destination for CRT.** A challenge in divisibility incorrectly sent the reader to Volume 3 Chapter 2 for Chinese remainders; it now points to Volume 2's congruences chapter.
6. **Gauss-sum cross-reference.** An arithmetic-functions challenge now points directly to the Gauss-sum exercise instead of an obsolete numerical chapter.
7. **Regression tests.** Added source checks that require book parts and the canonical catalog to match and that find duplicate/missing manuscript-local reference targets.

## Reordering prerequisite spot-check

Arithmetic functions follows prime factorisation and congruences, and its references to characters are previews. Primitive roots uses earlier congruences and does not invoke quadratic reciprocity as a premise. The quadratic-residue chapter precedes sums-of-squares applications. The moved Diophantine chapter does not explicitly invoke results from the now-later continued-fractions chapter.

Searches through subsequent main chapter bodies did not find Hensel lifting or Chebyshev/Bertrand material being invoked as a stated prerequisite. This is only a spot-check: every implicit dependency still needs review.

## Remaining gates

- Independently audit every theorem, lemma, corollary and full proof for hypotheses, definitions and edge cases.
- Check arithmetic examples and non-elementary analytic constants, especially the Basel evaluation in coprime density, prime estimates, quadratic reciprocity signs, Pell solutions, sum-of-squares descents, norm division and Euler products.
- Review all 144 exercises, hints and solutions, including explicit signposts on challenges needing later chapters.
- Confirm every chapter-opening and transition reflects the reordered neighbours and first-reading route.
- Run complete tests and regenerate the reading PDF, EPUB and new-page-count paperback cover. Verify the ISBN 9798167208650 and matching barcode in final artifacts, not only source.
- Conduct author-side KDP title association, Print Previewer and physical proof reviews separately.

Keep PR #97 in draft. This source scan does not certify mathematical correctness, KDP acceptance or readiness to merge.

## Additional advanced-exercise dependency repair

Five Chapter 4 prompts have been signposted without deleting exercises or changing their identifiers: the coprime-density exercise points to Volume 1's Basel proof; Eisenstein's trigonometric reciprocity proof and the Euler--Jacobi liar problem explicitly require the later reciprocity chapter; the largest-prime-factor problem names the quantitative prime-distribution tool from Volume 6; and the finite-field sum-of-squares exercise defines its quadratic-symbol notation and marks the later quadratic Gauss sum and Volume 4 total-variation tool. These repairs preserve the corpus but do not yet constitute a full solution audit.

## Proof-focused review pass: concrete findings

This pass examined the full displayed proofs and statements of Euclid's theorem,
Chebyshev-type bounds and Bertrand's postulate, the basic modular and Hensel
arguments, the four-square descent, the Pell existence-and-classification
argument, the Euclidean-division estimate in three imaginary quadratic
integer rings, the quadratic reciprocity construction, character
orthogonality, Euler-product convergence and Legendre's finite sieve.

- **Corrected a theorem boundary case in Chapter 11 (Legendre's sieve).**
  The original printed statement assumed only $x\ge1$ and $z\ge\sqrt{x}$,
  and asserted $\Phi(x,z)=1+\pi(x)-\pi(z)$. This is false whenever
  $z>x$: for example, $x=4$, $z=10$ gives $\Phi(4,10)=1$ but the
  old right-hand side is $1+\pi(4)-\pi(10)=-1$.
  The corrected statement is
  $\Phi(x,z)=1+\pi(x)-\pi(\min\{x,z\})$, for these hypotheses.
  The proof now notes that the prime interval $(z,x]$ may be empty.
  A regression test directly compares finite sifted counts with the
  corrected formula for many small $x,z$, including $z>x$.
- **Corrected a mistaken statement about Chapter 10's scope.**
  A previous editorial change incorrectly said that Chapter 10 did not
  treat $\mathbb{Z}[\sqrt{-2}]$. It actually develops norms, units and
  Euclidean division in that ring alongside the Gaussian and Eisenstein
  integers. The Diophantine passage now acknowledges that material while
  correctly withholding a classification of $y^2=x^3-2$ that the chapter
  does not prove.
- **Caught a one-star challenge with future prerequisites.**
  The Fibonacci-coprimality exercise in Chapter 1 used the later gcd
  distribution and expected-value problem in Chapter 5. It is now
  labelled a Journey/advanced return problem, with the missing tool named
  directly in the prompt.
- **Caught a high-level quadratic-residue challenge using final-chapter
  machinery.** The two-$k$-th-powers problem now explicitly calls out
  the character-orthogonality and Jacobi-sum tools from Chapter 11 as
  prerequisites rather than leaving them hidden.
- **Numerical and logical proof spot checks:** the displayed
  four-square identity and descent reduce a positive multiplier;
  the elementary Pell argument constructs a norm-one unit and reduces
  any positive unit via the least fundamental unit; the Hensel proof
  correctly invokes invertibility of the derivative modulo $p$;
  the Euler product's nonvanishing follows from absolute convergence
  for $s>1$; the sieve boundary above was the identified failed case.
  These spot checks do not certify every claim or optional exercise.

All source-local IDs and cross-references must be rechecked by the
full CI suite after these edits. The remaining mathematical proof
and exercise audit is substantial. Do not convert this partial audit
into a proof-complete, CI-green or publication-ready sign-off.

## Further exercise-domain and numerical checks

- In Chapter 4's optional Eisenstein trigonometric reciprocity
  exercise, part (a) now specifies that $q$ is a **positive** odd integer.
  The original phrase "let $q$ be odd" included negative integers for
  which the asserted product indexed from $1$ to $(q-1)/2$ was not the
  formula proved in the solution.
- In Chapter 1, the reduced-random-fraction problem now chooses $a,b$
  independently and uniformly on $\{1,\ldots,N\}$ and explicitly takes
  $N\to\infty$. Without a specified finite experiment or limiting
  process, its statement "with probability $1/(p+1)$" was ambiguous.
- Independently enumerated small integers as sanity checks, separate
  from the source regression suite: Legendre's corrected sieve formula
  passed **8,474** pairs of $x,z$ ($1\le x\le90$,
  $\max(2,\lceil\sqrt x\rceil)\le z\le100$); the representation formula
  $r_2(n)=4\sum_{d\mid n}\chi_4(d)$ and the two-square prime-exponent
  criterion each passed **120** integers; quadratic reciprocity passed
  **650** ordered pairs of distinct odd primes at most $103$.
  Finite enumeration can find counterexamples but cannot certify a
  theorem for all inputs.

The test matrix is evidence for these specific formulas, **not** an
audit of every chapter, every exercise solution, or every proof.

## CI success and deeper exercise review — 3 November 2026

The full run [41556183082](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41556183082) passed for commit 178fe9affc5aad25099a46e101608cb0e24604a3, including the Volume 2 build, pagination checks, KDP print-export tests, and artifact upload. The generated Volume 2 GitHub Actions artifact has ID 13193869440 and size 33,179,497 bytes. This is a green **baseline**; later commits need their own checks, and human KDP preview/proof remain separate.

**Fermat quotient boundary:** The Lerch congruence in Problem pb:fermatquot was previously stated for all primes. It fails for p=2: the sum of Fermat quotients is zero, but the Wilson quotient W_2 is 1 modulo 2. The problem's final part also uses the order of 2 modulo p, undefined at p=2. The problem and solution now explicitly require an odd prime. The Lerch congruence was independently checked for 21 odd primes up to 79.

**Hensel completeness:** The solutions of x² ≡ -1 modulo 125 are exactly 57 and 68. The exercise now asks for all solutions, and the hint and solution lift both initial roots 2 and 3 modulo 5; uniqueness follows from Hensel's lemma.

**Advanced prerequisites:** The Bernoulli-denominator and Ramanujan partition-congruence exercises in Chapter 3 now disclose prerequisites from Volume 5; the cubic character challenge in Chapter 11 labels its Volume 13 algebraic-integer step; the factorial perfect-power exercise labels the optional Bertrand theorem; and the analytic gcd problem is an advanced return challenge citing earlier coprime-density work and later Dirichlet series.

**Hypotheses made explicit:** The modular-order proposition specifies coprimality and integer exponents. Euler's criterion, Gauss's lemma and the supplementary law for 2 explicitly assume an odd prime. Pell's theorem explicitly assumes a nonsquare integer d≥2, and the Pythagorean theorem explicitly specifies positive integers.

**Expanded finite verification:** Added tools/test_volume2_arithmetic_sanity.py with seven finite tests covering quadratic reciprocity, two-squares representation and criterion, primitive roots, primitive Pythagorean parametrisations, four-square existence over a bounded range, Hensel lifting, and the odd-prime Fermat quotient. Finite checks do not prove general statements.

**Open gates:** The new head must pass CI separately; every remaining proof and all 144 exercise solutions still require individual correctness review; current PDF/EPUB/print wrap need visual inspection; and publisher-side KDP Print Previewer/physical proof steps remain open.

## Printed-order transition review — further pass, 3 November 2026

The exact-head GitHub Actions build [41596025329](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41596025329) completed successfully on commit `4983ea2a281c4066bb21816922c424ca678df45a`. This is build evidence for that SHA, not for subsequent edits or a publisher proof.

A targeted review covered the Chapter 1 and Chapter 2 theorem statements and the prompts, hints and full solutions of their **26 exercises** (15 and 11 respectively). No new counterexample was established in this pass; this does **not** complete the remaining 118-exercise audit or establish proof-complete sign-off.

The printed-order pass did identify three inaccurate teaching-roadmap statements:
- Chapter 2 had said Dirichlet characters are *built in Volume 3*, although Volume 2 Chapter 11 explicitly defines and uses them. The revised closing bridge distinguishes their Volume 2 introduction, Volume 3 structural generalisation and Volume 6 analytic application.
- Chapter 3 called the definition of multiplicative order a topic of the *next chapter*. The next printed chapter is Arithmetic Functions; orders begin in Chapter 5. The example now points to the actual labelled chapter.
- Chapter 3 labelled Gauss's totient-sum identity as a counting identity for the *next chapter* and immediately described multiplicative orders. The transition now explains how the divisor sum prepares Chapter 4 and how orders use it subsequently in Chapter 5.

A manuscript regression check guards these specific transitions against reversion. This is a continuity correction, **not** a certification of the still-open proof, exercise, latest-build visual or KDP gates.

## Chapter 3 advanced-solution correction — 3 November 2026

In the solution to the Kloosterman-sum fourth-moment exercise (`pb:kloosterman`), the assertion that the bound `1.19 p^(3/4)` improves on the trivial `p-1` bound for **every odd prime** was false at `p=3`: `1.19 * 3^(3/4) > 2`. The solution now explicitly isolates that counterexample and states the improvement for odd primes `p>=5`. The function `(p-1)/p^(3/4)` is increasing, so the comparison follows from its truth at `p=5`. A new arithmetic sanity regression independently counts additive/reciprocal-compatible ordered quadruples for primes 3, 5, 7 and 11 and checks the displayed exact fourth-moment formula `2p^3 - 3p^2 - 3p`, as well as the bound comparison. The computation is a finite cross-check, not a proof of the fourth-moment identity or any other advanced exercise.

## Schur nonzero-value exercise correction — 3 November 2026

The Chapter 3 exercise `pb:primepoly` previously asked for infinitely many primes dividing one of `P(0),P(1),...` without requiring the polynomial value to be nonzero. When `P(0)=0` (for example `P(X)=X`), the statement was vacuously satisfied because every prime divides zero. The accompanying proof treated that case as finished, hiding the intended theorem about **nonzero** polynomial values.

The prompt now explicitly requests infinitely many **distinct prime divisors of nonzero values** of a nonconstant integer polynomial at nonnegative integers. The hint and proof choose `a>=0` with `c=P(a)!=0`, then use the positive arithmetic progression `a+Mt` where `M=|c| * product(primes in a purported finite list)`. The resulting nonconstant integral polynomial `H(t)` satisfies `H(t)=1 mod p_i` for every listed prime, and an arbitrarily large nonzero value produces a new prime divisor. This also handles `P(0)=0` without relying on zero's universal divisibility. A source regression guards the stronger prompt and correct shifted proof.

The mathematical proof is self-contained once polynomial root finiteness and congruence preservation are available. It is one further audited exercise, not a full check of all 144 solutions or a KDP release sign-off.

## Step 2 source-verified Volume 1 bridges — 3 November 2026

The Step 2 instruction-level exit gate was checked against the actual first
volume, not merely against the book outline. The following are **source
observations**, not independent correctness endorsements for every theorem.

| Volume 2 bridge | Verified Volume 1 source and proved fact | Added first-reading payoff |
| --- | --- | --- |
| Chapter 4: Arithmetic Functions | `volume1-first-principles/chapters/ch02-counting.tex`: the inclusion--exclusion theorem is proved by tracking the alternating contribution of each finite-set member. | `6-3-2+1=2` for $\varphi(6)$ introduces the divisor signs $\mu(1),\mu(2),\mu(3),\mu(6)$. The general coprimality identity and inversion are proved **after** their preview. |
| Chapter 5: Primitive Roots | `volume1-first-principles/chapters/ch02-complex-roots.tex`: elementary groups, cyclic groups, element order and the $n$th-root-of-unity proposition are defined and proved. | Compare the cyclic four complex roots with $1,2,4,3$ modulo $5$. No inference of cyclicity at arbitrary prime moduli from complex multiplication; Volume 2's own Gauss theorem proves it. |
| Chapter 10: Gaussian and Eisenstein Integers | Same Volume 1 complex chapter: conjugation, Brahmagupta's identity $|zw|=|z||w|$, and cube roots of unity. | $(1+i)(2+i)=1+3i$ and $10=2\cdot5$ demonstrate the integer-valued multiplicative norm. Ring Euclidean division and unique factorisation remain new proofs in Volume 2. |
| Chapter 11: Characters | Same Volume 1 complex chapter: roots-of-unity orthogonality and the coefficient filter are formally proved. | The even/odd $\chi_4$ filter isolates $1\pmod4$; the chapter next defines characters and proves their orthogonality, without presuming Volume 3's representation theory. |

**Additional transition coverage:** Chapter 1 already correctly recalls
Volume 1's additive subgroup test; Chapter 2 now distinguishes Volume 1's
proof-by-contradiction and series tools from new prime distribution
conclusions; Chapter 6 derives the count of nonzero square classes by
pairing $x$ and $-x$ and using the earlier field factorisation law; Chapter
8 invokes the well-ordering result proved in Volume 1's sums/induction
chapter to motivate descent. Chapter 3's earlier totient counting identity
and Volume 1 exercise were also checked. In Chapter 11 the phrase suggesting
that residue unit groups themselves had appeared in Volume 1 was corrected:
Volume 1 introduced **group language**, while residue unit groups were
developed in Volume 2's congruence chapter.

**Dependency classification:** The four primary bridges contain either
already-proved Volume 1 facts, arithmetic from earlier printed Volume 2
chapters, or explicitly labelled previews followed by a local proof.
No added bridge requires the reader to assume Gauss's primitive-root
theorem, Dirichlet-character orthogonality, Euclidean division in a new
ring, or general Volume 3 group theory before they are developed.
The newly added manuscript regression test checks Volume 1 source
anchors, bridge text and finite arithmetic examples (inclusion--exclusion,
powers modulo $5$, complex norms, $\chi_4$ filtering and quadratic-square
counts).

**Step 2 editorial status: complete.** GitHub CI for the newest commit is
tracked separately. Steps 4--6 still require a full first-use and
end-to-end mathematical/144-solution audit; Step 8 still requires a fresh
current-head render and proof. No release approval or merge is implied.

## Step 3: foundation and optional routes — 3 November 2026

**Editorial changes committed:** Chapter 2's Euclid-number workshop,
Chapter 3's modular-cancellation workshop, Chapter 4's M"obius-inversion
workshop, Chapter 7's two-square classification workshop, the
Diophantine chapter's nonexistence workshop, and Chapter 11's finite
character workshop were relocated before their respective optional
sections. No source exercise, hint or solution was deleted.

**First-route boundary contracts:**

| Chapter | Keep for first reading | Optional section or challenge |
| --- | --- | --- |
| 2: Primes | Infinitude, reciprocal-prime divergence, Euclid proof workshop | Chebyshev/prime-count bounds; Bertrand; dependent gap/factorial/product checks; second proofs and topology |
| 3: Congruences | Residue classes, invertible cancellation, CRT, congruence workshop | Simple-root Hensel lifting and its exercise |
| 4: Arithmetic functions | Multiplicative functions, inversion, perfect numbers and inversion workshop | Analytic average orders and error terms |
| 7: Sums of squares | Two-square criterion, four-square existence and obstruction workshop | Lattice-disc error estimate and challenge assuming the full three-square theorem |
| 8: Diophantine equations | Modular obstructions, Pythagorean parametrisation, Fermat descent, nonexistence workshop | Conic parametrisation; specialised Mordell and Markov material; Vieta jumping; matching challenges |
| 11: Characters | Character orthogonality, absolutely convergent Euler products, finite sieve, finite detector workshop | The $s=1$ analytic boundary, conditional prime-progression discussion, advanced series and powerful-number counting |

The Chapter 6 Miller--Rabin and prime-power-square counting
journeys have explicit optional wording. The Chapter 1 random
valuation exercise was found to **appear to require the later CRT**
in its discovery note, despite its full proof actually using
elementary divisibility by products of coprime prime powers and
finite inclusion--exclusion. Its discovery note and required-tools
line were corrected, making this one-star problem self-contained.

Advanced challenges involving later-volume machinery that were
already flagged in earlier passes remain optional rather than being
removed. The full mathematical validity of every claim and solution
remains subject to Steps 4--6.

**Independent source-level checks after edits:**
11 source chapters were read with their preface and field guide;
all 144 exercise labels still match 144 hint and solution labels
in chapter order; 266 unique labels were found and no local
`ref`, `eqref` or `autoref` targets were missing. Counts of
major proof/figure/exercise/enumerate/reminder environments balanced.
The six workshop-before-optional assertions passed. New repository
regressions guard those same boundaries, selected advanced-theorem
references, and optional exercise labels. **These are structural
checks, not a complete TeX build or a proof of 144 solutions.**

**CI gate:** the workflow on the final updated head must still
finish successfully; prior successful workflows cover older SHAs
only. The complete proof/exercise audit, publication visual
inspection and publisher-side KDP proof remain open. The PR
must remain draft.

## Step 4 — printed-order prerequisite audit — 3 November 2026

The separate, detailed first-use ledger is
docs/reviews/volume2-prerequisite-order-audit-2026-11-03.md.
It follows the eleven chapters in the actual main.tex reading order,
records the core definition/proof sites and the optional boundaries,
and classifies every forward label reference as a prose preview,
later-volume destination, optional exercise return or an issue repaired.

**Concrete repairs:** The Chapter 1 valuation probability proof no
longer presents the future CRT as a necessary tool. Chapter 3's
multiplicative-order worked example now explains its calculation
without citing Chapter 5's order theorem as an established premise.
The two-star Morley exercise points openly to the Chapter 11 Fermat
quotient identity used by its hint and solution; Glaisher's advanced
prompt now names the same identity in addition to Volume 5.

The Chapter 4 Euclid--Euler proof no longer cites a later exercise
inside the proof itself. Its optional Euler-liar solution proves
the half-size subgroup estimate from two disjoint cosets, removing
an apparent dependency on Volume 3's Lagrange theorem.

The Chapter 6 optional prime-power-square solution formerly asserted
that a suitable nonresidue prime exists by a vague appeal to CRT and
quadratic reciprocity; such an existence statement was not proved.
It now supplies a **self-contained obstruction**: if a nonsquare
integer has an odd prime valuation r, it is not square modulo
p^(r+1); otherwise it is negative of a square -b², which is not
square modulo 4b². The optional Miller--Rabin solution's required
tools now cite the existing Volume 2 cyclic unit-group results rather
than apparently relying on Volume 3. A finite regression checks the
local-square obstruction on small positive and negative nonsquares.

**Source gate:** all proof cross-references prior to exercise sections
target existing earlier-local or earlier-printed-chapter labels;
the **41 then-one-star problems** have no later-chapter references in
their prompts, hints or required solution portions. All exposition
forward labels are in the curated preview list. The corpus still
has 144 aligned exercise/hint/solution IDs, 266 unique local labels
and no dangling local references. These conditions now have
regression tests.

**Status: Step 4 editorial/source gate completed**, pending CI
confirmation for its latest commit. No claim is made that a complete
mathematical proof audit (Step 5), 144-solution audit (Step 6) or
publication acceptance (Steps 8--9) has occurred. Do not merge PR #97
on this evidence.

## Step 5 — independent mathematical source pass — 3 November 2026

**Completed at source-review level.** See
docs/reviews/volume2-mathematics-examples-audit-2026-11-03.md
for the printed-order chapter-by-chapter proof matrix, corrected
assertions, finite arithmetic certificates and review limits.

- Reviewed the **72 named results**, with **72 proof environments**,
  and the **99 worked example blocks** in the eleven chapters.
- Corrected mathematical/numerical errors in Chapters 7, 8, 10 and
  11: N(2) is 13; μ(6)=+1 and μ(7)=−1; N(2−ω)=7,
  not N(2+ω); the modular equation y²=x²+x+1
  excludes x≡1,2 (mod 4), not all odd x; the Fermat descent
  gives n=2u²v², not n=b². Clarified the Markov Vieta
  move and associated diagram caption.
- Removed an invalid analytic leap from Abel-weighted signed
  sums to the convergence of the unweighted χ4 prime series.
  The optional analytical bridge now states the correct
  sum/difference argument and keeps its remaining premise explicit.
- Tightened the hypothesis domains of Bézout, linear congruence,
  totient divisor sum, Euler's quadratic residue count and
  the divisor average theorem. Corrected a conic/Hasse-principle
  overstatement and other misleading mathematical captions.
- Corrected a π approximation and made the Chebyshev/Erdős
  historical attribution cautious; the large Pell(61)
  solution was externally corroborated. Step 5 added finite
  regressions for the new arithmetic corrections.
- Fresh source scan: **11** printed chapters, **144** matching
  exercise/hint/solution IDs, **266** source-local labels,
  no dangling local refs, balanced checked LaTeX environments.

**Still open:** exact-head CI, Step 6 exhaustive individual exercise
correctness and difficulty review, Step 7 reader/metadata polish,
Step 8 actual latest-head PDF/EPUB/print/KDP-wrap visual checks
and Step 9 publisher/physical proof. The PR remains draft.

## Step 6 — all exercise, hint and solution keys — 3 November 2026

**Completed at the source-level editorial gate; latest CI pending.**
The full **144-entry keyed matrix** is
docs/reviews/volume2-exercise-solution-audit-2026-11-03.md.
The manuscripts retain all **144** exercises and their **144**
matching hints and **144** matching full solutions, in the same
printed-chapter and per-chapter order as the approved baseline.
No labels were deleted or duplicated.

**Two substantive solution repairs:**

1. **ex:imo88:** The Vieta jumping proof did not justify
   positivity of its second quadratic root. It now brackets that
   integer root strictly between -1 and b using the signs of
   f(-1) and f(b), excludes a'=0 under nonsquare k, and therefore
   proves the required strictly smaller positive solution.
2. **pb:gcdmean:** The logarithmic mean-gcd argument now proves
   its own needed average order of φ(d)/d by Möbius inversion and
   finite partial summation. No later Volume 6 theorem is silently
   assumed.

**Difficulty calibration:** Four exercises were regraded from
one to two stars: pb:valuation and pb:parity (multi-part probability
and independence), pb:fermatnum (Fermat factor order/641) and
pb:artin (safe-prime primitive roots). The new distribution is
**37 one-star, 80 two-star, 20 three-star, 7 Journey**.
Every prompt, hint and full solution is retained; only these
difficulty markers changed.

The new regression suite tools/test_volume2_exercise_keys.py
checks the eleven per-chapter counts, all key/order/grade
invariants, the two repaired proof boundary markers and
independent arithmetic checks of bounded test cases across the
full curriculum. Extra mathematical spot-checks included
**Monier's exact strong-liar formula on all odd composites below
400**, with n=9 as its sole >1/4 case, and two-kth-power
exceptions for k=3,4,8 through the claimed k=8 bound at
prime 761. Advanced exercises are consistently identified as
returns or later-volume explorations.

**Limit:** Source-level editorial review and finite checks are
not external mathematical refereeing or formal proof
verification. The final latest-head CI run still needs confirmation.
Step 7 reading transitions and metadata, Step 8 rendered
reading/print PDF, EPUB and page-count-matched paperback wrap,
and Step 9 KDP/physical proof remain separate mandatory gates.
PR #97 stays draft and unmerged.

**Historical grading note (Step 6, 3 November 2026):** This earlier Step 4 audit covered all 41 problems that were graded one-star at that checkpoint. Step 6 regraded four mathematically more demanding problems to two stars. The current first-route regression checks all **37** one-star problems; no problem statement, solution or prerequisite was deleted.

## Step 7 — adjacent chapter bridges and publishing-copy alignment — 3 November 2026

**Completed at manuscript/source level.** Full 11-chapter route matrix and
metadata checks:
docs/reviews/volume2-reader-continuity-metadata-audit-2026-11-03.md.

- Every printed chapter now ends its main reading material with a
  mathematical **forward bridge**, before its exercises. Each of
  Chapters 2–11 has a specific **backward bridge** in its introduction.
  Both sides of each adjacent transition were checked against the
  actual approved main.tex order. In particular, the actual
  Diophantine → continued fractions → Gaussian/Eisenstein route no
  longer assumes the former filenames describe printed order.
- The end of the characters chapter and the end of the field guide
  now provide a three-example handoff to **Volume 3, Symmetry**:
  unit-group powers, Gaussian ring factorisation and the
  character $\chi_4$ as a multiplicative map. The later analytical
  Volume 6 and general algebraic/p-adic Volume 13 remain optional
  longer-term destinations.
- The field guide keeps its first-reading toolbox separate from a
  later **optional Volume 13 notation preview**. The $p$-adic
  convention $v_p(0)=+\infty$ moved there; elementary $v_p$ for
  nonzero integers and rationals remains in the main notation list.
- Rewrote kdp.md, which had inaccurately promised **fourteen
  chapters**, post-characters content and proof of general ideals
  and $p$-adic numbers. The new **1,922-character** listing accurately
  describes **four parts and eleven chapters**, **144** exercises
  with complete hints/solutions, the **Volume 1** prerequisite and
  immediate **Volume 3** sequel. Its seven keyword phrases meet
  KDP's length limits.
- Revised the 153-word back-cover blurb to mention the preserved
  solved-exercise count and Volume 3; the main ISBN 9798167208650,
  canonical part catalog, cover/print generator and publishing
  instructions were not altered. Harmonised the Bertrand
  epigraph's historical wording with the Step 5 source audit.
- Added tools/test_volume2_reader_route.py. A source-only scan verified
  all 11 outgoing / 10 incoming bridges, unchanged **144**
  exercise blocks and exact ordered chapter inputs.

**Still open:** exact-head CI; Step 8 full rebuild and visual inspection
of reading PDF, print PDF, EPUB, online reader and the *new*
page-count-dependent paperback wrap with its ISBN barcode; Step 9
KDP/Kindle Previewer, assignment check and physical proof. Source
completion is not a production release. PR #97 stays draft.

## Step 8 — actual production proof and post-build regression — 3 November 2026

**The real Volume 2 production artifact has been obtained and checked.**
See docs/reviews/volume2-production-proof-audit-2026-11-03.md
for evidence and publisher-side limitations.

- The Volume 2 build job of GitHub workflow #1429 passed and
  uploaded artifact `books-volume2-integers` (13232292637),
  generated on final manuscript-content commit `4d46982b`.
- Actual files: **314-page reading PDF**, **313-page KDP print PDF**
  and **314 KDP-counted pages** after odd-page rounding. The generated
  bleed wrap is **14.987 × 10.25 inches**, with an exact
  **0.737-inch spine**. The interior has the standard 7 × 10 trim.
- Verified embedded print fonts, KDP PDF 1.3 with no interactive
  annotations, correct copyright and cover ISBN
  **9798167208650**; independently decoded the printed EAN-13
  **bars** to those thirteen digits, not just their displayed text.
- Reviewed 25 rendered page samples including all eleven chapter
  openers, both TOC pages, formula-heavy pages, end matter and
  Volume 3 handoff; viewed full back/spine/front cover;
  raster-compared 20 reading/print body page pairs. No sample
  layout clipping or substantial visual mismatches observed.
- Traversed all **5,754 EPUB manifest assets** and **12,929**
  internal EPUB links/anchors; no missing EPUB targets. Verified
  all **144** exercise/hint/solution triads in EPUB and the
  separate HTML reader. Online reader has **11** chapter pages
  and **3,167** intact book-local asset links.
- Added a permanent post-build QA checker at
  `review/volume2-continuity/check_volume2_outputs.py`, executed
  successfully against the downloaded prior output, and wired
  into the Volume 2 conditional build in
  `.github/workflows/build.yml`. Future successful builds
  include `production-output-qa.json` in the artifact.
- **CI caveat:** The fully successful earlier source-content
  artifact predates the new QA integration. Latest-head CI
  remains a separate required acceptance check; the manuscript
  is not publication-ready just because a per-book build passed.

**Open:** latest full workflow green (including the new post-build
step and site), Step 9 Kindle/KDP Previewer and physical proof,
and the author's KDP association for ISBN 9798167208650.
The PR stays draft and unmerged.

