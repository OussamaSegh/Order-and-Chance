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

### Step 1 — Establish the baseline and chapter sequence [started]

- Inventory all eleven chapter inputs, the existing exercise/hint/solution corpus, and references. Save the approved TOC here.
- Apply the approved `main.tex` part and chapter order and update the preface to match it.
- Add regression tests that lock the exact chapter order, part headings and the existing 144-exercise count.
- **Exit gate:** source order matches this table; all eleven source chapters appear exactly once; no accidental deletion of exercises; tests run in CI.

### Step 2 — Build the bridges from Volume 1 [started]

- Explicitly connect inclusion–exclusion to divisor counting and Möbius inversion in Chapter 4.
- Connect Volume 1's roots of unity and elementary cyclic groups to multiplicative orders in Chapter 5.
- Connect complex multiplication and norms to Gaussian integers in Chapter 10.
- Connect roots-of-unity filters to character orthogonality in Chapter 11.
- Add smaller transitions in divisibility, primes, quadratic residues and integer equations as needed.
- **Exit gate:** every bridge accurately identifies what Volume 1 actually proves and does not use an undefined Volume 2 result as a premise.

### Step 3 — Separate foundation and exploration routes [started]

- Chapter 2: retain Chebyshev-type bounds and Bertrand's theorem as a guided deeper route after Euclid/Euler; do not require them for congruences.
- Chapter 3: teach modular inverses and the CRT first; make Hensel lifting a marked extension.
- Chapter 8 (Diophantine source `ch09-diophantine.tex`): lead with congruence obstructions, Pythagorean triples and infinite descent; identify advanced Mordell/Markov cases and Vieta jumping as exploration.
- Apply the same signposting to deeper sections and high-star exercises wherever they have later prerequisites.
- **Exit gate:** skipping marked extensions does not invalidate a proof or a regular exercise on the main route.

### Step 4 — Perform a prerequisite and chapter-order audit [started]

- In *printed* chapter order, record the first occurrence and proof location of each non-elementary term, theorem and tool: Bézout, unique factorisation, modular inverses, residue rings, field language, totients, Dirichlet convolution, multiplicative order, cyclic structure, Legendre/Jacobi symbols, descent, norms, characters, sieves and convergence facts.
- For every forward reference, classify it as harmless preview, optional challenge, or a genuine dependency. Resolve all genuine forward dependencies by moving a proof, adding a self-contained lemma, or changing the first-route explanation.
- Review hypotheses at their point of use, especially coprimality, finite/infinite counts, convergence, prime versus composite moduli, and assumptions in norm arguments.
- **Exit gate:** no main-route theorem, worked example or one-star exercise requires an unproved later result.

### Step 5 — Audit mathematics and examples [pending]

- Check every theorem and proof end-to-end (not only syntax), with explicit edge cases and computations.
- Verify prime-distribution estimates, the reciprocity sign and lifting conditions, complete Pell-solution arguments, sum-of-squares criteria, Euclidean norms in the two quadratic rings, and Euler-product convergence.
- Independently check numerical examples, captions, historical claims where used as factual statements, and equation domains.
- Keep a dated review ledger in `docs/reviews/` with each repaired statement, evidence and any open risk.
- **Exit gate:** every first-route proof is independently justified using Volume 1 or earlier Volume 2 material; remaining outside-scope theorems are clearly identified as previews.

### Step 6 — Audit all exercises, hints and solutions [started]

- Check the exact 144 existing exercise IDs, one matching hint and one full solution for each, and no duplicate IDs.
- Verify mathematical correctness, difficulty stars, first-use definitions, solution prerequisites, edge cases and the separate discovery note/formal write-up.
- Challenges involving later-volume ideas must identify those requirements at the exercise itself; the foundational sequence may not depend on them.
- **Exit gate:** full exercise-key parity, no dangling references, and an audited record of any deliberately changed exercise.

### Step 7 — Finish the reader-facing progression [started]

- Reconcile each chapter opening and ending with its actual printed neighbours; update manuscript transitions that still assume the former sequence.
- Separate Volume 13's ideal and p-adic notation from Volume 2's usable field guide; place it in a clearly labelled later-volume preview and remove unearned p-adic problem-solving instructions from the main toolbox.
- End Chapter 11 and the field guide with a concrete handoff to **Volume 3 — Symmetry**: residue unit groups, Gaussian integer rings, and character homomorphisms. Keep Volumes 6 and 13 as later destinations, not the immediate sequel.
- Update `kdp.md`, `blurb.tex`, or publication handoff **only if** the changed reading route makes their claims inaccurate.
- **Exit gate:** introductory contract, TOC, chapter bridges, field guide, back cover and listing agree on prerequisites and outcomes.

### Step 8 — Rebuild, test and inspect every output [pending]

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
