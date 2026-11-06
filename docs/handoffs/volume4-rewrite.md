# Handoff: Volume 4 rewrite

Status of this file: **living handoff**. It is updated on the rewrite branch and committed with each milestone. A later agent should resume from this file and the repository, without redoing finished milestones.

## Current contract (6 November 2026)

Fourteen chapters, four parts, as in `docs/plan/book-04.md`. Title page subtitle is **The Logic of Uncertainty**. Branch `cursor/volume4-rewrite-ee7f`, draft PR 111, do not merge, do not force-push, do not edit other volumes.

The twelve-chapter number freeze is withdrawn. Live citations that still use the old numbers are listed in `docs/plan/volume4-citation-migration.md`. That list is an integration gate, not a completed repair.

Restart: read this file, then `volume4-chance/main.tex`, then the migration document. Compile with `./build.sh volume4-chance` from the repository root after the TeX toolchain is present. Do not start a second branch.

## Status

Manuscript skeleton is the fourteen-chapter book: parts and inputs in `main.tex`, Bertrand and Buffon in `chapters/ch05-geometric.tex`, entropy in `chapters/ch07-entropy.tex` (Kraft and Shannon coding included), random graphs in `chapters/ch14-graphs.tex`. Chapters 1–3 are the earlier drafts, reused, not yet re-audited line by line. No native PDF has been produced on this contract. Page count against 260–290 is unknown until that build.

Named checks still open: Exercise 2.7 Riemann-sum shift; Exercise 6.4 Cauchy characteristic function; local-limit expansion in Chapter 6; giant-component exercise in Chapter 14 (first-moment path bound is the proved statement; the Poisson survival probability is marked as the heuristic); crossing-number small-graph estimate; Pólya integral in the walk chapter. Arcsine is not a numbered theorem. Inversion is not a numbered theorem. Shuffle profile labels 8.10, 8.22, 8.23, 8.24 are not in this manuscript.

## Task and acceptance

Rebuild `volume4-chance/` as a complete replacement of *Chance: The Logic of Uncertainty*. The reader has finished Volumes 1–3 only. The book must be followable at that boundary, including exercises, hints, and solutions. Do not merge.

Acceptance, from the authoring brief:

1. Complete replacement LaTeX manuscript, then the reading PDF and the required production outputs.
2. Updated `docs/plan/book-04.md` and an old-to-new map.
3. Source-backed prerequisite register. Every missing dependency is taught in this volume before use, or kept off the logical path.
4. Exercises, hints, solutions, examples, and figures checked, with uncertainties named.
5. Change summary, source commit, artifact hashes, and the commands that actually ran.
6. One focused unmerged PR.
7. This handoff, current on the remote branch.

The work is **not** complete while any of those is still open. An outline is not the book.

## Canonical instructions

Read these before editing prose or mathematics:

- `docs/agents/mathematician-writer.md`
- `docs/WRITING-STYLE.md` (including Sound human, and the prerequisite contract)
- `AGENTS.md`
- `docs/design/interior.md` (design 5e; caption style stays as it is)
- `docs/SERIES-STRUCTURE.md`
- `common/series-catalog.json` (Volume 4 title *Chance*, subtitle *The Logic of Uncertainty*)
- `docs/plan/book-04.md` (rewritten with this project)
- `docs/plan/volume4-prerequisites.md`
- `docs/plan/volume4-old-to-new.md`
- `docs/plan/volume-citation-map.md` (later books cite Volume 4 by chapter and exercise **number**)

Do not invent a second style guide. First-edition copy: reader-facing text does not describe the book as a revision. No notebooks.

## Branch, base, PR

- Branch: `cursor/volume4-rewrite-ee7f`
- Base: `origin/main` at `28db77df` (the commit this branch was cut from).
- PR: draft, https://github.com/OussamaSegh/Order-and-Chance/pull/111 — do not merge.
- Do not force-push. Do not rewrite pushed history.

## How to resume

1. Check out `cursor/volume4-rewrite-ee7f` and pull it. Do not restart from `main` and do not re-audit finished chapters.
2. Read this file, then the prerequisite register and the old-to-new map.
3. Continue at **Exact next actions**. Do not rewrite a file whose ledger row says `written` unless a named defect says to.
4. After each coherent chapter or audit milestone: update this file, commit, and push the branch.
5. Before a long build, and before stopping, update this file and push.

## Ledger

Legend: `planned` means designed and not yet the manuscript. `written` means a fresh manuscript file is in the tree. `verified` means a human-style mathematical read of that file has been recorded, not merely that a compiler succeeded. A build passing is not mathematical verification.

| Item | State | Notes |
| --- | --- | --- |
| Instruction inventory | verified | Writer brief, style, series structure, design 5e, catalog, old book plan, Volume 1–3 actual theorems cited below |
| Prerequisite register | written | `docs/plan/volume4-prerequisites.md` |
| Old-to-new map | written | `docs/plan/volume4-old-to-new.md` |
| Content plan `docs/plan/book-04.md` | written | Replaces the keep-and-admit-measure plan |
| Preface | written | Fresh. Not yet read against the built PDF |
| Ch. 1 Counting and Paradoxes | written | Fresh manuscript, three figures, eight exercises with hints and solutions. Not yet a reader pass |
| Ch. 2 Discrete Random Variables | written | Fresh. Exercise 2.6 is the long cycle and the hundred prisoners. Birthday-wait solution (Exercise 2.7) uses a Riemann-sum comparison; re-read the shift by 2 on the reader pass |
| Ch. 3 Generating Functions | written | Fresh. Exercise 3.7 is the series for $(1-4x)^{-1/2}$ and the Catalan formula |
| Ch. 4 Inequalities, Large Numbers and Entropy | written | Hoeffding, Borel–Cantelli, bounded strong law, Bernstein–Weierstrass, finite entropy. Gilmer left out on purpose |
| Ch. 5 Continuous Probability Done Properly | written | Riemann densities, continuous Fubini on rectangles, polar rectangles, inverse distribution functions, continuous dominated convergence, Box–Muller. Exercise 5.7 is the Cantor distribution. Not Lebesgue theory |
| Ch. 6 Convergence and the Central Limit Theorem | written | Lindeberg is the tenth numbered formal environment. Exercises 6.1 and 6.7 are Slutsky and the cycle CLT |
| Ch. 7 Random Walks | written | Reflection, ruin, Pólya. Exercise 7.8 is the electrical network |
| Ch. 8 Markov Chains | written | Coupling convergence. Exercises 8.6 and 8.8 are top-to-random and rising sequences |
| Ch. 9 Poisson Processes | written | Colouring lemma is the fifth numbered formal environment |
| Ch. 10 Conditional Expectation and Martingales | written | Optional stopping, the unit-win counter-example, ABRACADABRA |
| Ch. 11 Brownian Motion | written | Existence is formal environment 4; reflection is formal environment 12. Exercise 11.3 is the zero set |
| Ch. 12 The Probabilistic Method | written | Exercise 12.4 is the crossing lemma. Euler is proved before it |
| Appendix Extremal and Ramsey | written | Turán, Ramsey, Schur, sunflower, Erdős–Ko–Rado |
| Gilmer section | removed from the book | Not included. The file `gilmer.tex` remains unused |
| Workshop `pb:*` problems | removed from the logical path | Not cited outside this volume |
| Exercises, hints, solutions | written | Interface numbers checked by order in each chapter file |
| Figures | written | New TikZ plates for Chapters 1, 2, 4, 5, 6 |
| Voice pass | not started | Next, after a compile |
| Reader pass (Volumes 1–3 only) | partial | Mean-one extinction in Chapter 3 replaced by the series expansion. Exercise 2.7 still to be re-read against the built book |
| Build | not started | |

## Last completed milestone

**Milestone 7 — manuscript drafted through the appendix**, not yet compiled. Chapters 1–12 and the extremal appendix are the new text. Next: compile, fix errors, reader pass, voice pass, full `./build.sh volume4-chance`.

## Current WIP

Compile of `volume4-chance` is the next action. Known soft spots to re-read after the log is clean: the Cauchy characteristic-function limit in Exercise 6.4, the local-theorem expansion in Theorem 6 (local), the giant-component sketch in Exercise 12.7, and the Riemann-sum shift in Exercise 2.7.

## Decisions already made

1. **Foundation.** Volume 1 already proves finite probability, countable nonnegative sums, geometric and Poisson masses, Markov, Chebyshev, the weak law, inclusion–exclusion, Catalan paths as a counting exercise, Stirling with constant \(\sqrt{2\pi}\), the Gaussian integral, one-variable calculus, Jensen, Cauchy–Schwarz, and the spectral theorem for real symmetric matrices (`thm:spectral`). Volume 4 cites these and does not pretend they were not taught. It does not lean on Volume 3’s Perron appendix; finite Markov chains are done by averaging and coupling.
2. **No silent measure theory.** Lebesgue measure on \(\mathbb R^d\), a general Fubini–Tonelli theorem, and an unconstructed infinite product are not used as proof steps. Infinite sequences of fair bits are built from the binary digits of one uniform on \([0,1]\), with probabilities of finite-bit events equal to lengths of intervals. Almost-sure statements are outer-content zero. Iterated integrals are proved for continuous functions on rectangles. A dominated-convergence theorem is proved for continuous integrands. Volume 5 already proves the continuous form it uses and only *mentions* a Lebesgue theorem in Volume 4; that mention will become slightly stale and is recorded under blockers. Volume 7 still constructs the general theory.
3. **Chapter numbers stay.** Later volumes cite “Volume 4, Chapter \(n\)” and specific exercise numbers. The twelve chapters and the extremal appendix stay in the same order and keep the cited exercise slots. See the register for the list.
4. **Formal-environment numbers that later books name.** Chapter 6’s tenth formal box is Lindeberg’s theorem. Chapter 9’s fifth is the colouring lemma. Chapter 11’s fourth is existence of Brownian motion; the twelfth is the reflection principle. Do not insert an extra `definition`/`theorem`/`proposition`/`lemma`/`corollary`/`example` ahead of those boxes. `examplex` and `definitionx` do **not** use the shared counter.
5. **Workshop problems `pb:*`.** They leave the reader’s path. Many of their old solutions use Fourier analysis, representation theory, or later-volume inequalities. They are not cited from other volumes. Techniques that belong to this book (moment method, Hoeffding, ballot, coupon collector, electrical networks for reversible walks) stay in the main exercises.
6. **Cover.** Do not redesign the Galton cover. About the Cover stays accurate if Chapter 6 is still the central limit theorem.
7. **Volumes 1–3 are immutable.** Do not edit them to make an audit pass.

## Unresolved

- Volume 5, `chapters/ch04-integrals.tex`, says Volume 4, Chapter 5 proved dominated convergence for the Lebesgue integral. After the rewrite, Chapter 5 proves it for continuous functions and names the boundary. The Volume 5 sentence is then historically stale. Do not edit Volume 5 unless a later instruction allows a one-line citation repair.
- Volume 7 says it discharges an “admitted fact (A1)” of the old Chapter 5. The new Chapter 5 constructs countable products of uniforms from one uniform, so that particular admission is no longer needed. Volume 7’s sentence is a pointer, not a false theorem.
- Exercise 11.3 in later citations uses the zero set of Brownian motion and a Fubini/Tonelli sentence. The new solution must prove Lebesgue measure of the zero set is almost surely zero using only the integral theorems proved in this volume, and must say so without calling the tool Tonelli if Tonelli is not proved.
- Gilmer’s frequency bound \((1-\ln 2)/2\) is correct as a numerical value of that expression. It returns at the end of Chapter 4 only after a fresh proof of the entropy inequality. Until that proof is written and checked, the section is absent on purpose.
- Numeric theorem numbers other than 6.10, 9.5, 11.4, and 11.12 are not a series contract. Do not chase old numbers beyond those four.

## Exact next actions

1. Chapters 1–5 are written. Next write Chapter 6 with Lindeberg as formal environment 6.10, then Chapters 7–12 and the appendix.
2. Update this ledger to `written` for each finished file. Commit and push.
3. Write Chapters 5–8, then 9–12 and the appendix, under the same rule.
4. Reader pass, then voice pass. Fix what those passes find.
5. Build Volume 4 only, with the repository’s `./build.sh` path. Record the command and the result. Do not call a Volume 4 build an all-volume verification.
6. Update the draft PR body at each manuscript milestone. Do not merge.

## Tests and builds actually run

None yet on this branch. The numerical checks below were done in a Python session while fixing constants for the plan; they are not a book test.

- \(\sum_{k=600}^{1000}\binom{1000}{k}/2^{1000} \approx 1.364\times 10^{-10}\) (log-gamma summation).
- Chernoff information bound at the same point: \(\exp(-1000 D(0.6\|0.5)) \approx 1.800\times 10^{-9}\), with \(D(0.6\|0.5)\approx 0.02014\).
- Hoeffding’s \(\exp(-20)\approx 2.061\times 10^{-9}\).
- \(H_{52}\approx 4.538\). \(1-(H_{100}-H_{50})\approx 0.3118\).
- \((1-\ln 2)/2 \approx 0.1534\).

## Artifacts

No new PDF. Rebuild, when the manuscript is ready, from the repository root after `source /workspace/order-chance-system/activate.sh`, using `./build.sh volume4-chance` (confirm the selector in `build.sh` before launching). Outputs expected by `AGENTS.md`: `dist/volume4-chance.pdf`, `dist/kdp/volume4-chance-print.pdf`, EPUB, wrap. Do not invent a page count.

## Remaining validation

Everything in the ledger marked `planned` or `written` but not `verified`. Independent mathematical reading, layout, and the production build are all still open.
