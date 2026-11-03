# Volume 2 continuity implementation plan

**Edition:** Order and Chance, Volume 2 — *The Integers: Primes, Patterns and Proofs*
**Approved:** 2026-11-03. **Working branch:** `editorial/volume2-continuity-foundations-20261103`.
**Status:** Implementation in progress; not a publication sign-off.

## Editorial contract and invariants

- The only prerequisite for the first-reading route is **Volume 1**. The text must define, motivate and prove any new machinery before its first necessary use. No silent dependencies on Volumes 3, 6 or 13.
- Preserve the mathematical ambition, all eleven source chapters, the main theorems, and the **144 existing graded exercises with their matching hints and full solutions**, subject to a documented, mathematically justified correction.
- Advanced material remains available, but must be marked as a second-reading section or an optional exploration when it is not needed to prove later first-route results.
- Respect `docs/WRITING-STYLE.md`: concrete cases first, complete proofs, explicit hypotheses and small checks; new transitions should explain the mathematical need, not announce the outline.
- Keep the book's approved typography, cover identity, figures, subtitle, volume number, and paperback ISBN **9798167208650**. Manuscript reflow changes the page count, so rebuild the *matching* paperback wrap from the new exported print interior.

## Approved four-part reading order

| Reader-facing position | Chapter source | Chapter theme |
| --- | --- | --- |
| Part I — The Arithmetic of Integers / 1 | `ch01-divisibility.tex` | Divisibility and the Euclidean algorithm |
| 2 | `ch02-primes.tex` | Primes and factorisation |
| 3 | `ch03-congruences.tex` | Congruences and Chinese remainders |
| 4 | `ch04-arithmetic-functions.tex` | Multiplicative functions and Möbius inversion |
| Part II — Patterns in Remainders / 5 | `ch05-primitive-roots.tex` | Orders, cyclic groups and primitive roots |
| 6 | `ch06-quadratic-reciprocity.tex` | Quadratic residues and reciprocity |
| Part III — Equations in Integers / 7 | `ch07-sums-of-squares.tex` | Two and four squares |
| 8 | `ch09-diophantine.tex` | Diophantine methods and infinite descent |
| 9 | `ch08-continued-fractions.tex` | Continued fractions and Pell's equation |
| 10 | `ch10-gaussian-eisenstein.tex` | Gaussian and Eisenstein integers |
| Part IV — The Hidden Structure / 11 | `ch14-characters.tex` | Characters, Euler products and the sieve |

File stems are deliberately **not renamed**. Their historical numbers do not define the printed chapter numbers; `main.tex` does. Stable labels avoid invalidating references throughout the series.

## Step-by-step implementation

### Step 1 — Establish the baseline and chapter sequence [completed]

- Inventory all eleven chapter inputs, the existing exercise/hint/solution corpus, and references. Save the approved TOC here.
- Apply the approved `main.tex` part and chapter order and update the preface to match it.
- Add regression tests that lock the exact chapter order, part headings and the existing 144-exercise count.
- **Exit gate:** source order matches this table; all eleven source chapters appear exactly once; no accidental deletion of exercises; tests run in CI.

### Step 2 — Build the bridges from Volume 1 [completed]

- Explicitly connect inclusion–exclusion to divisor counting and Möbius inversion in Chapter 4.
- Connect Volume 1's roots of unity and elementary cyclic groups to multiplicative orders in Chapter 5.
- Connect complex multiplication and norms to Gaussian integers in Chapter 10.
- Connect roots-of-unity filters to character orthogonality in Chapter 11.
- Add smaller transitions in divisibility, primes, quadratic residues and integer equations as needed.
- **Exit gate:** every bridge accurately identifies what Volume 1 actually proves and does not use an undefined Volume 2 result as a premise.

### Step 3 — Separate foundation and exploration routes [completed]

- Chapter 2: retain Chebyshev-type bounds and Bertrand's theorem as a guided deeper route after Euclid/Euler; do not require them for congruences.
- Chapter 3: teach modular inverses and the CRT first; make Hensel lifting a marked extension.
- Chapter 8 (Diophantine source `ch09-diophantine.tex`): lead with congruence obstructions, Pythagorean triples and infinite descent; identify advanced Mordell/Markov cases and Vieta jumping as exploration.
- Apply the same signposting to deeper sections and high-star exercises wherever they have later prerequisites.
- **Exit gate:** skipping marked extensions does not invalidate a proof or a regular exercise on the main route.

### Step 4 — Perform a prerequisite and chapter-order audit [completed]

- In *printed* chapter order, record the first occurrence and proof location of each non-elementary term, theorem and tool: Bézout, unique factorisation, modular inverses, residue rings, field language, totients, Dirichlet convolution, multiplicative order, cyclic structure, Legendre/Jacobi symbols, descent, norms, characters, sieves and convergence facts.
- For every forward reference, classify it as harmless preview, optional challenge, or a genuine dependency. Resolve all genuine forward dependencies by moving a proof, adding a self-contained lemma, or changing the first-route explanation.
- Review hypotheses at their point of use, especially coprimality, finite/infinite counts, convergence, prime versus composite moduli, and assumptions in norm arguments.
- **Exit gate:** no main-route theorem, worked example or one-star exercise requires an unproved later result.

### Step 5 — Audit mathematics and examples [completed]

- Check every theorem and proof end-to-end (not only syntax), with explicit edge cases and computations.
- Verify prime-distribution estimates, the reciprocity sign and lifting conditions, complete Pell-solution arguments, sum-of-squares criteria, Euclidean norms in the two quadratic rings, and Euler-product convergence.
- Independently check numerical examples, captions, historical claims where used as factual statements, and equation domains.
- Keep a dated review ledger in `docs/reviews/` with each repaired statement, evidence and any open risk.
- **Exit gate:** every first-route proof is independently justified using Volume 1 or earlier Volume 2 material; remaining outside-scope theorems are clearly identified as previews.

### Step 6 — Audit all exercises, hints and solutions [completed]

- Check the exact 144 existing exercise IDs, one matching hint and one full solution for each, and no duplicate IDs.
- Verify mathematical correctness, difficulty stars, first-use definitions, solution prerequisites, edge cases and the separate discovery note/formal write-up.
- Challenges involving later-volume ideas must identify those requirements at the exercise itself; the foundational sequence may not depend on them.
- **Exit gate:** full exercise-key parity, no dangling references, and an audited record of any deliberately changed exercise.

### Step 7 — Finish the reader-facing progression [completed]

- Reconcile each chapter opening and ending with its actual printed neighbours; update manuscript transitions that still assume the former sequence.
- Separate Volume 13's ideal and p-adic notation from Volume 2's usable field guide; place it in a clearly labelled later-volume preview and remove unearned p-adic problem-solving instructions from the main toolbox.
- End Chapter 11 and the field guide with a concrete handoff to **Volume 3 — Symmetry**: residue unit groups, Gaussian integer rings, and character homomorphisms. Keep Volumes 6 and 13 as later destinations, not the immediate sequel.
- Update `kdp.md`, `blurb.tex`, or publication handoff **only if** the changed reading route makes their claims inaccurate.
- **Exit gate:** introductory contract, TOC, chapter bridges, field guide, back cover and listing agree on prerequisites and outcomes.

### Step 8 — Rebuild, test and inspect every output [started]

- Run the Python unit suite including Volume 2 manuscript regression tests, and check document references and chapter/figure assets.
- Run `./build.sh volume2-integers` to regenerate the reading PDF, EPUB, online reader, print interior and current-page-count paperback wrap.
- Verify no unresolved labels, missing fonts, bad line breaks, pagination overflows, broken references or missing exercise solutions in the PDF/EPUB.
- Run canonical KDP structural/provenance and cover checks. Review pages with mathematical formulas and the chapter transitions, and verify the correct ISBN line and EAN-13 barcode in the **new** wrap.
- **Exit gate:** successful CI build and independent proof/render checks; the print cover's spine matches the freshly exported page count.

### Step 9 — Editorial acceptance and publishing gate [pending]

- Document a release checklist and remaining limitations in the review ledger; inspect the Kindle EPUB and KDP Print Previewer separately.
- Do not mark the manuscript publication-ready solely because static tests or CI are green. KDP ISBN association, upload, final Print Previewer and physical proof remain publisher-side verifications.
- Do not merge the editorial PR until the required audit and production gates have passed. Do not tag an edition or publish to KDP as part of this planning PR.

## Implementation batches and review policy

1. **Structure:** source order, preface, regression tests.
2. **Teaching route:** Volume 1 bridges, foundation/exploration markers.
3. **Mathematical accuracy:** prerequisite ledger, theorem/proof repairs, all 144 exercises.
4. **Reader handoff:** transitions, Volume 3 epilogue, field guide, metadata consistency.
5. **Production:** reproducible build, PDF/EPUB/print proof and final editorial review.

The single draft PR is a work container: it can receive these batches as further commits. Mark a step complete only after its stated exit gate is met. A green initial source check is **not** a mathematical or KDP release sign-off.

## Audit progress note — 3 November 2026

The first PR CI run failed at the canonical part catalog check (before TeX). The catalog and cover-source SHA-256 have since been synchronized. A source-level reference scan found 266 distinct labels, no duplicate or unresolved local reference targets, and 144 matching exercise/hint/solution IDs. Obsolete printed chapter numbers and two misleading mathematical destination claims were corrected. Five arithmetic-functions challenges now explicitly identify their later prerequisites; the rest of the exercise corpus is **not yet independently mathematically audited**. See `docs/reviews/volume2-continuity-source-audit-2026-11-03.md`. The full production build and mathematics gates remain open.

## Build and proof-audit checkpoint — 3 November 2026

Run [41556183082](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41556183082) passed on its own SHA, including Volume 2 production export tests. Later commits on the branch repaired two mathematics boundary cases, completed both Hensel lifts, and improved advanced-prerequisite labels. Seven new finite arithmetic sanity checks were committed. **The earlier green CI result does not cover those later commits.** Full independent mathematics review, current-head build, and manual PDF, EPUB and KDP proof checks remain open. See docs/reviews/volume2-continuity-source-audit-2026-11-03.md.

## Step 2 acceptance checkpoint — 3 November 2026

**Source-level gate passed.** The four primary bridges now demonstrate the
specific mathematical operation carried forward from Volume 1 rather than
merely announcing a theme:

- Chapter 4: the finite inclusion--exclusion count $\varphi(6)=6-3-2+1=2$
  becomes the divisor-sign identity for the M\"obius function, whose proof and
  inversion theorem are then given in Chapter 4.
- Chapter 5: the cyclic fourth roots of unity are compared explicitly with
  the powers of $2$ modulo $5$; prime-field cyclicity is still proved afresh
  in Chapter 5 instead of being assumed.
- Chapter 10: a concrete complex product illustrates
  $N(zw)=N(z)N(w)$; the new Euclidean-lattice division estimates and
  factorisation theory remain to be established within Volume 2.
- Chapter 11: the Volume 1 roots-of-unity filter is compared with an exact
  $\chi_4$ residue-class filter, before the general Dirichlet-character
  orthogonality theorem is proved in that chapter.

The supporting routes in Chapters 1, 2, 6 and 8 now identify, respectively,
the already introduced subgroup test, proof by contradiction/series,
pairing and polynomial root bounds, and the well-ordering principle behind
infinite descent. Chapter 3's existing totient bridge was checked.
The underlying Volume 1 proofs were verified directly against the
Volume 1 counting, complex-roots, and sums chapter source files. New source
and small-arithmetic regression tests are in tools/test_volume2_manuscript.py.

This acceptance concerns **only the Step 2 instructional bridges**.
The independent first-use prerequisite audit (Step 4), theorem and example
audit (Step 5), 144-solution review (Step 6), and end-to-end production
acceptance (Steps 8--9) remain open. The new GitHub Actions head must complete
its own CI run; an older successful run does not validate these commits.

## Step 3 acceptance checkpoint — 3 November 2026

**Instructional route and source-level gate passed.** First-reading
workshops now occur before optional sections in Chapters 2, 3, 4, 7, 8
(Diophantine Equations, source ch09) and 11; the intervening optional
sections carry explicit skip/resume guidance.

- **Chapter 2:** Euclid's and Euler's proofs, plus the Euclid-number
  workshop, form the main route. Chebyshev's quantitative bounds and
  Bertrand's theorem are optional; their dependent exercises
  `ex:gaps`, `ex:factorial` and `ex:t1-prod11` explicitly say so.
  Optional alternative proofs and topology challenges are distinguished.
- **Chapter 3:** units, cancellation, CRT and the cancellation workshop
  precede optional Hensel lifting. The Hensel exercise remains optional.
  All regular first-route exercises use only the earlier core results.
- **Chapter 4:** convolution and M"obius inversion, perfect numbers and
  the inversion workshop precede optional analytic average orders.
- **Chapter 7:** two- and four-square results and the obstruction
  workshop precede the optional lattice-disc estimate; the exercise
  admitting the unproved three-square converse is labelled optional.
- **Chapter 8:** modular obstructions, Pythagorean parametrisation,
  infinite descent and a full nonexistence workshop come first.
  Rational conics are a further route; specialised Mordell/Markov
  equations, Vieta jumping and their dependent exercises are marked
  optional. The next chapter's continued fractions and Pell arguments
  do not require them.
- **Chapter 11:** characters, orthogonality, absolutely convergent
  Euler products, the finite sieve and the finite character workshop
  come before an optional analytic boundary-series section. The
  exercises requiring that section and the powerful-number analytics
  are marked optional.
- **Other boundaries:** the Chapter 1 one-star valuation/independence
  solution no longer presents the later CRT as a prerequisite; its
  fixed-divisibility argument is elementary. Advanced Miller--Rabin
  and prime-power-square challenges in Chapter 6 now disclose their
  optional status, and previously identified Volume 3/5/6/13
  prerequisites remain labelled at their exercises.

**Structural validation:** 11 original manuscript chapters, 144
unchanged exercise IDs in matching exercise/hint/solution order, 266
unique source-local labels, no missing local cross-references, and no
unbalanced checked LaTeX environments. Step 3 tests in
`tools/test_volume2_manuscript.py` guard the relative location of
each foundational workshop, the opt-in labels of dependent exercises,
and absence of citations to selected advanced theorems in the main
section of Chapters 2, 3, 8 and 11.

This sign-off is **editorial route acceptance**, not the separate
independent prerequisite/proof/solution audit (Steps 4--6). CI for the
latest head, current PDF/EPUB/print visual proof and KDP Previewer
remain separate gates. The PR stays draft and unmerged.

## Step 4 acceptance checkpoint — 3 November 2026

**First-use and order gate passed at source level.** The independent
ledger docs/reviews/volume2-prerequisite-order-audit-2026-11-03.md
records definitions and local proof sites for all core tools and
theorem chains in the eleven *printed* chapters, not in file-stem order.
It classifies all cross-chapter forward references as explicit
outlooks, optional exercise returns or actual dependencies requiring
repair.

The review resolved the following prerequisite leaks:

- Chapter 1's one-star valuation problem now explicitly obtains
  independence by divisibility counting; the Chapter 3 CRT is mentioned
  only as a later alternative.
- Chapter 3's illustrative first-order calculation avoids using the
  group-order theorem of Chapter 5. The optional Morley congruence
  now identifies its Chapter 11 Fermat-quotient prerequisite.
  Glaisher's challenge identifies both Volume 5 and Chapter 11 tools.
- The Chapter 4 Euclid--Euler proof no longer cites an exercise not
  yet presented, and the optional Euler-liar solution proves the
  proper-subgroup size bound directly instead of borrowing Volume 3.
- Chapter 6's optional Miller--Rabin count cites the Volume 2 cyclic
  prime-power unit groups already proved in Chapter 5. The optional
  square-count solution no longer invokes an unproved existence of
  special nonresidue primes: its last claim now has a direct modular
  obstruction, using an odd valuation or congruence modulo 4.

**Evidence:** a source scan of all pre-exercise proof environments found
**zero future local-label dependencies**; 41 then-one-star question/hint/
required-solution chains have **zero dependencies on later chapter
labels** and no same-chapter future-exercise dependencies. The full
manuscript still has 144 matching exercise/hint/solution IDs, 266
unique local labels and no missing local refs. Automatic regression
tests now enforce the proof-order check, one-star boundary, the
curated cross-chapter preview inventory and the Morley warning.
Finite regression checks exercise the replacement modular-square
argument for small positive and negative nonsquares.

**Scope limit:** this is an editorial prerequisite-order sign-off,
not an independent proof of every theorem, worked example or exercise
solution. Step 5 and Step 6 remain essential; final-output build,
visual inspection and KDP proof remain open. Any exact-head CI failures
must be addressed separately. Keep PR #97 draft and unmerged.

## Step 5 acceptance checkpoint — 3 November 2026

**Source-level mathematics review completed.** The detailed
review ledger is
docs/reviews/volume2-mathematics-examples-audit-2026-11-03.md.
In the eleven chapters, the pre-exercise manuscript contains
**72** named results (theorems, propositions, lemmas and corollaries),
**72** proof environments, and **99** worked example blocks. Their
statement/proof chains, numerical assertions, hypotheses, and
mathematical figure-caption claims have undergone an independent
internal source pass in printed order.

**Repairs made in the manuscript:**

- Corrected the disc count **N(2)=13** (the four points on the circle
  had been omitted) and the ten-term Möbius sum, including the signs
  **μ(6)=+1, μ(7)=−1**.
- Corrected the Eisenstein prime split:
  **N(2−ω)=7, N(2+ω)=3,
  7=(2−ω)(2−ω²)**.
- Replaced false mod-4 deductions for
  **y²=x²+x+1** with the exact classes
  **1,3,3,1**; the equation has actual integer solutions.
- Corrected two descriptions of Fermat's descent:
  **n=2u²v²** is twice a square, not itself necessarily a square.
  Clarified which Vieta jump grows and which descends. Fixed
  the descent figure caption and historical numeric theorem
  references.
- Removed the unjustified inference from bounded Abel-weighted
  prime sums to convergence of a signed sum of reciprocals;
  the optional character discussion now uses the correct
  non-negative sum/difference comparison.
- Explicitly stated missing positive-modulus/real-asymptotic/
  nonzero-square/gcd-domain hypotheses. Tightened the half-open
  square geometric explanation, a π approximation and the
  Eisenstein lattice caption. Made Bertrand's historical
  attribution precise without choosing a disputed proof year.

**Independent finite regression checks** now cover the corrected
disc counts, Eisenstein norm and product, ten-term Möbius series,
mod-4 obstructions, and Markov triples. The existing arithmetic
suite already covers quadratic reciprocity, Hensel, two/four
squares, prime roots, and selected difficult finite sums.
Proof-reference scanning now also recognises titled proof
environments. A fresh cross-chapter scan showed **144 aligned
exercise/hint/solution IDs**, **266 unique labels**, no missing
local references, and balanced checked LaTeX environments.

**Strict boundary:** This is an *internal mathematical/editorial
source review*, not proof-assistant certification or outside
refereeing. It **does not** certify the individual 144 exercise
solutions (Step 6), nor replace latest-head CI, actual rendered
PDF/EPUB/print inspection or KDP's publisher-side/physical proof.
Keep PR #97 draft and unmerged.

## Step 6 acceptance checkpoint — 3 November 2026

**All 144 exercise keys have a documented source-level review record.**
The per-key inventory, mathematical audit notes, difficulty adjustments,
return-route classifications and independently computed finite checks live in
docs/reviews/volume2-exercise-solution-audit-2026-11-03.md.

- Verified the **16 + 11 + 21 + 13 + 15 + 17 + 8 + 8 + 8 + 8 + 19**
  problem counts in actual printed order, **144 unique exercises**, and
  one hint plus one full \idea/\writeup solution for each, with matching
  keys and matching source order. The longer pb: problems also have
  \tools and \leads sections.
- Corrected the **IMO 1988 Vieta-jumping proof**, which previously did
  not validly establish that the new integer root is positive.
  The replacement shows f(-1)>0>f(b), forcing
  1≤a'<b≤a for a hypothetical counterexample with nonsquare k.
- Made the **mean-gcd problem's average-order derivation self-contained**:
  A(t)=Σ_{d≤t}φ(d)/d=t/ζ(2)+O(log(2t)), followed by
  Σ_{d≤N}φ(d)/d²=(log N)/ζ(2)+O(1). Previously an unstated
  Volume 6 mean-value theorem was effectively assumed.
- Regraded four multi-part or higher-prerequisite exercises from
  **one star to two stars**: pb:valuation, pb:parity,
  pb:fermatnum and pb:artin. Updated overall distribution:
  **37 one-star, 80 two-star, 20 three-star, 7 Journey**;
  no problem statement, hint or solution was removed.
- Screened the exercise text for undisclosed later-chapter/volume
  dependencies. The seven Journey problems and advanced return problems
  retain their explicit optional/later-volume signposting.
- Added tools/test_volume2_exercise_keys.py to lock exact per-chapter
  problem counts, grades and key parity, and independently test
  Vieta samples, gcd means, Diophantine and Markov examples,
  quadratic symbols, Waring power sums, Fermat/pseudoprime/Proth
  certificates, local four-square counts, powerful numbers and the
  **exact Monier strong-liar count** on odd composites below 400.
  These are finite tests supporting the full proofs, not substitutes.

**Internal Step 6 manuscript source gate:** completed, subject to
latest-head CI confirmation. The ledger records every one of 144 keys;
this internal review is not proof-assistant verification or outside
refereeing. The editorial/checker sign-off does not waive Step 7
transitions, Step 8 rendered PDF/EPUB/print/wrap QA or Step 9
publisher-side KDP and physical proof. Keep PR #97 draft and unmerged.

**Historical grading note (Step 6, 3 November 2026):** This earlier Step 4 audit covered all 41 problems that were graded one-star at that checkpoint. Step 6 regraded four mathematically more demanding problems to two stars. The current first-route regression checks all **37** one-star problems; no problem statement, solution or prerequisite was deleted.

## Step 7 acceptance checkpoint — 3 November 2026

**Reader-facing/source metadata gate completed.** The detailed matrix is
docs/reviews/volume2-reader-continuity-metadata-audit-2026-11-03.md.

- Added a mathematical **outgoing bridge** before exercises in each of
  the **eleven printed chapters**, and an **incoming bridge** before the first
  section in Chapters 2–11. The explicit printed route now follows:
  divisibility → primes → congruences → arithmetic functions →
  primitive roots → quadratic reciprocity → sums of squares →
  Diophantine equations → continued fractions and Pell →
  Gaussian/Eisenstein integers → characters and sieve.
  Legacy source filenames are irrelevant to the reader's numbering.
- The last character chapter now hands off directly to **Volume 3,
  Symmetry: Groups, Rings and Fields** using the concrete unit group modulo
  7, the ring $\Z[i]$ and the multiplicative character $\chi_4$.
  Volume 6's prime distribution and Volume 13's ideals and $p$-adics
  remain later destinations and explicitly do not become prerequisites.
- Reordered the field-guide flow so ordinary valuations, inverses,
  residues and proof checks form the main toolbox. The later Volume 13
  notation ($v_p(0)$, general ideals, $N(I)$, $|x|_p$, $\Z_p$, $\Q_p$)
  is confined to a labelled **optional later-volume preview**.
  Ended the guide with a direct character-homomorphism check for Volume 3.
- **Rewrote the obsolete KDP listing.** It no longer claims fourteen
  chapters or a course in ideal theory/$p$-adic numbers. Its four-part,
  eleven-chapter description (1,922 characters) correctly lists what
  is proved here, the preserved **144** solved exercises, the Volume 1
  prerequisite, and immediate Volume 3 sequel. Seven keyword phrases
  fit KDP's 50-character limit.
- The back-cover blurb is **153 words**, retains the approved mathematics,
  and promises the correct exercises and sequel. The main manuscript
  ISBN **9798167208650**, canonical four-part catalog, EPUB/print
  metadata generators and publishing configuration remain unchanged.
- Harmonised the Chebyshev/Erdős historical epigraph to avoid a disputed
  exact year. The preface already accurately describes the approved
  order, the first-reading prerequisites and optional advanced route.
- Added tools/test_volume2_reader_route.py to lock all chapter
  bridge and opening placements, the metadata contract, the isolation
  of advanced notation, the back-cover text and the ISBN.
  A separate source scan found the expected **11 chapters**, **144**
  exercise blocks, all 10 incoming and 11 outgoing bridges.

**Strict exit boundary:** This closes the *editorial source/metadata*
work, not the production verification. Latest-head CI, fully rebuilt
and manually inspected PDF/EPUB/online/print and new page-count matched
cover, and the publisher's KDP/Kindle Previewer and physical proof are
still required by Steps 8–9. PR #97 remains draft and unmerged.

## Step 8 production artifact checkpoint — 3 November 2026

**The actual Volume 2 production files were downloaded, opened and reviewed.**
See docs/reviews/volume2-production-proof-audit-2026-11-03.md
for the exact artifact and independent visual/format tests.

- The **Volume 2 build passed** and uploaded `books-volume2-integers`
  (artifact 13232292637) on the last manuscript-content HEAD,
  `4d46982b5f3db88774ac3170fcbbd43926c85044`.
  The containing workflow was [run #1429](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41638786729).
- Inspected the real **314-page reading PDF**, **313-page KDP interior**,
  and the correct **314 KDP-counted pages** after odd-count rounding.
  The current matching paperback spine is **0.737 inches**, with
  a **14.987 × 10.25-inch** complete bleed wrap.
- Verified the printed copyright ISBN **9798167208650**, the matching
  paperback cover digits, and independently decoded all 95 modules of
  the rasterised **EAN-13 barcode** to the same ISBN. The cover and
  its subtitle, spine and 153-word blurb were visually reviewed.
- Rendered and inspected **25 representative reading-PDF pages**:
  copyright/front matter, TOC, the four-part route, all eleven
  chapter starts, formula-heavy pages, the field guide, end-matter
  and the Volume 3 handoff. Also compared **20** pairs of the reading
  and KDP-print body at the pixel level. No text clipping or
  noticeable mismatch was found in those samples. The build's
  independent whole-box check reported no overflow or missing refs.
- Opened the EPUB ZIP/XML, checked its **5,754 manifest entries** and
  **12,929 local links/anchors** with zero broken targets, and
  confirmed all 144 exercise/hint/solution blocks in exact chapter
  order. The separate HTML reader has the same 144 triads,
  eleven chapters and **3,167** intact local asset links; the
  collection homepage is built in the later site job.
- Added `review/volume2-continuity/check_volume2_outputs.py`,
  validated its cross-format checks against the downloaded
  production files, and integrated it as a Volume 2-only **required
  post-build CI step**. Its JSON report is now included in the
  artifact uploads on subsequent CI runs.

**Gating precision:** These results establish the **independent
artifact/render review** on the last source-content SHA, not the
new integrated step's CI success. Step 8 stays `[started]` until
the latest full GitHub workflow passes the new post-build check
and site aggregation. Step 9 also requires Kindle Previewer,
KDP's physical/Print Previewer and ISBN-account checks.
Keep PR #97 draft, not release-ready, and do not merge yet.

