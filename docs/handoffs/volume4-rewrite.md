# Handoff: Volume 4 rewrite

Status of this file: **living handoff**. It is updated on the rewrite branch and committed with each milestone. A later agent should resume from this file and the repository, without redoing finished milestones.

## Current contract (6 November 2026)

Fourteen chapters, four parts, as in `docs/plan/book-04.md`. Title page subtitle is **The Logic of Uncertainty**. Branch `cursor/volume4-rewrite-ee7f`, draft PR 111, do not merge, do not force-push, do not edit other volumes.

The twelve-chapter number freeze is withdrawn. Live citations that still use the old numbers are listed in `docs/plan/volume4-citation-migration.md`. That list is an integration gate, not a completed repair.

Restart: read this file, then `volume4-chance/main.tex`, then the migration document. Compile with `./build.sh volume4-chance` from the repository root after the TeX toolchain is present. Do not start a second branch.

## Status

Head `d07a4e33` on `cursor/volume4-rewrite-ee7f`. The fourteen-chapter skeleton is in `volume4-chance/main.tex`. Title page subtitle is *The Logic of Uncertainty*.

Chapter 1 has a dedicated pushed commit `b267c681` and a mathematical second pass (definitions, ballot proof including `b=0`, digit cylinders, outer content, all eight exercises, hints, and solutions). Voice review of Chapter 1 is not done. No other chapter has a passed second pass. Repair commits, not acceptance: Chapter 2 `4d4c87c9` (Exercise 2.7 index shift), Chapter 3 `ebc3cd9b` (remark moved out of the extinction proof), Chapter 5 angle wording `3ab3ad32`, Chapter 7 exercise environment `62f02af4`, Chapter 8 last-visit identity `966843f6` (Theorem 8.5; the integral arcsine density is not claimed), Chapter 14 subcritical count `d07a4e33`.

One `xelatex -interaction=nonstopmode main.tex` in `volume4-chance` exited 0 and wrote `main.pdf` (131 pages) with undefined references, before the figures added after that pass. That is not `./build.sh`, not a print PDF, and not a page-count verdict. The planning range is **400–500 pages** (owner decision t67u/t68u, 6 November 2026). It replaces 260–290. Do not thin proofs to meet it, and do not pad chapters to meet it.

The owner execution contract is the section `OWNER_APPROVED_V4_CONTRACT` on draft PR 111, outside the agent body markers. Do not replace that section with a run summary. Update its checkboxes and evidence SHAs only when a subgate is actually done. `written` is not `verified`.

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
| Preface | written | Not second-passed |
| Ch. 1 From Games to Probability Spaces | math-checked | Commit `b267c681`. Bertrand and Buffon live in Chapter 5. Exercise 1.7 is still the Dyck count. Voice not checked |
| Ch. 2 Random Variables and Their Laws | repair only | `4d4c87c9` states the Exercise 2.7 shift. The chapter is not second-passed |
| Ch. 3 Generating Functions and Random Families | repair only | `ebc3cd9b` moved the Chapter 14 sentence out of the extinction proof. Not second-passed |
| Ch. 4 Concentration and the Laws of Large Numbers | drafted | Entropy removed to Chapter 7. Not second-passed |
| Ch. 5 Continuous Chance | repair only | `3ab3ad32` fixes the Buffon angle to \([0,\pi]\). Bertrand and Buffon are in `ch05-geometric.tex`. Not second-passed |
| Ch. 6 Why the Bell Curve Appears | drafted | Lindeberg still the tenth numbered environment (Theorem 6.10). Not second-passed |
| Ch. 7 Entropy, Codes and Typical Sequences | repair only | `62f02af4` restores the exercise environment. Kraft and Shannon coding are drafted. Not second-passed |
| Ch. 8 Random Walks | repair only | `966843f6` adds Theorem 8.5, the exact last-visit identity. Integral arcsine law not claimed. Not second-passed |
| Ch. 9 Markov Chains and Mixing | drafted | Not second-passed |
| Ch. 10 The Poisson Clock | drafted | Colouring lemma is the fifth numbered environment (Lemma 10.5). Not second-passed |
| Ch. 11 Martingales and Fair Games | drafted | Not second-passed |
| Ch. 12 Brownian Motion | drafted | Existence is environment 4 (Theorem 12.4); reflection is environment 12 (Theorem 12.12). Not second-passed |
| Ch. 13 The Probabilistic Method | drafted | Crossing lemma is the fourth exercise (Exercise 13.4). Not second-passed |
| Ch. 14 Random Graphs and the Search for Structure | repair only | `d07a4e33` replaces the path count by isolated trees. Giant-component exercise claims a positive lower bound for one vertex, not a high-probability giant. Not second-passed |
| Appendix B Extremal and Ramsey | drafted | Counter still starts at 1 so the appendix prints as B. Not second-passed |
| Gilmer section | removed from the book | Not included. The file `gilmer.tex` remains unused |
| Workshop `pb:*` problems | removed from the logical path | Not cited outside this volume |
| Exercises, hints, solutions | written | Interface numbers checked by order in each chapter file |
| Figures | written | New TikZ plates for Chapters 1, 2, 4, 5, 6 |
| Voice pass | not started | Next, after a compile |
| Reader pass (Volumes 1–3 only) | partial | Mean-one extinction in Chapter 3 replaced by the series expansion. Exercise 2.7 still to be re-read against the built book |
| Build | not started | |

## Last completed milestone

**Chapter 1 mathematical second pass**, commit `b267c681`, pushed. The pass recomputed the ballot count (including `b=0`), the cylinder probabilities, the eight exercise solutions, and `365\ln 2=252.9987\ldots`. It did not review the TikZ of `figures/ch01-ballot.tex` as a drawing, and it did not sign the voice box.

## Current WIP

Next unfinished step: the same two-pass read of Chapter 2, starting from the Poisson limit through Exercise 2.7. The binomial/Poisson bars are a computed illustration, not that pass. Do not mark Chapter 2 complete because of a repair commit or a figure. Independent review of every chapter is pending: no second reviewer has reported.

## Decisions already made

1. **Foundation.** Volume 1 already proves finite probability, countable nonnegative sums, geometric and Poisson masses, Markov, Chebyshev, the weak law, inclusion–exclusion, Catalan paths as a counting exercise, Stirling with constant \(\sqrt{2\pi}\), the Gaussian integral, one-variable calculus, Jensen, Cauchy–Schwarz, and the spectral theorem for real symmetric matrices (`thm:spectral`). Volume 4 cites these and does not pretend they were not taught. It does not lean on Volume 3’s Perron appendix; finite Markov chains are done by averaging and coupling.
2. **No silent measure theory.** Lebesgue measure on \(\mathbb R^d\), a general Fubini–Tonelli theorem, and an unconstructed infinite product are not used as proof steps. Infinite sequences of fair bits are built from the binary digits of one uniform on \([0,1]\), with probabilities of finite-bit events equal to lengths of intervals. Almost-sure statements are outer-content zero. Iterated integrals are proved for continuous functions on rectangles. A dominated-convergence theorem is proved for continuous integrands. Volume 5 already proves the continuous form it uses and only *mentions* a Lebesgue theorem in Volume 4; that mention will become slightly stale and is recorded under blockers. Volume 7 still constructs the general theory.
3. **Fourteen chapters.** The owner plan of 6 November 2026 replaced the twelve-chapter number freeze. The map of live citations that now point at the wrong number is `docs/plan/volume4-citation-migration.md`. Do not edit other volumes to hide those lines. Do not revert to twelve chapters.
4. **Numbers that are still true, and numbers that moved.** Lindeberg is still Theorem 6.10. Do not insert a numbered environment before it. Colouring is Lemma 10.5. Brownian existence is Theorem 12.4 and reflection is Theorem 12.12. Crossing is Exercise 13.4. Last visit is Theorem 8.5. `examplex` and `definitionx` do not use the shared counter. Inversion, the seven-shuffle profile, and van der Waerden are not theorems of this manuscript.
5. **Workshop problems `pb:*`.** They leave the reader’s path. Many of their old solutions use Fourier analysis, representation theory, or later-volume inequalities. They are not cited from other volumes. Techniques that belong to this book (moment method, Hoeffding, ballot, coupon collector, electrical networks for reversible walks) stay in the main exercises.
6. **Cover.** Do not redesign the Galton cover. About the Cover stays accurate if Chapter 6 is still the central limit theorem.
7. **Volumes 1–3 are immutable.** Do not edit them to make an audit pass.

## Unresolved

- Volume 5, `chapters/ch04-integrals.tex`, says Volume 4, Chapter 5 proved dominated convergence for the Lebesgue integral. After the rewrite, Chapter 5 proves it for continuous functions and names the boundary. The Volume 5 sentence is then historically stale. Do not edit Volume 5 unless a later instruction allows a one-line citation repair.
- Volume 7 says it discharges an “admitted fact (A1)” of the old Chapter 5. The new Chapter 5 constructs countable products of uniforms from one uniform, so that particular admission is no longer needed. Volume 7’s sentence is a pointer, not a false theorem.
- Exercise 11.3 in later citations uses the zero set of Brownian motion and a Fubini/Tonelli sentence. The new solution must prove Lebesgue measure of the zero set is almost surely zero using only the integral theorems proved in this volume, and must say so without calling the tool Tonelli if Tonelli is not proved.
- Gilmer’s frequency bound \((1-\ln 2)/2\) is a numerical value of that expression. The comparison is not proved in this volume, and `gilmer.tex` is not included.
- Downstream citation repairs are listed in `docs/plan/volume4-citation-migration.md`. Editing those other volumes needs an explicit instruction. The PR checklist was not patched in this turn: `update_pr` replaces the whole description and would move or drop the owner contract that sits outside the agent markers. The evidence to record, when a line-level edit is safe, is Chapter 1 written and math-checked at `b267c681`; title page checked in `main.tex`; repair SHAs `4d4c87c9`, `ebc3cd9b`, `3ab3ad32`, `62f02af4`, `966843f6`, `d07a4e33` with those boxes left open.

## Exact next actions

1. Second-pass Chapter 2 in full. Commit that chapter alone and push. Then Chapter 3, and so on. A repair commit does not check the mathematical box.
2. On the PR, edit evidence SHAs inside `OWNER_APPROVED_V4_CONTRACT` only. Do not delete or rewrite that section. Transient status goes inside the `CURSOR_AGENT_PR_BODY` markers.
3. After the manuscript passes are further along, run `./build.sh volume4-chance` from the repository root. Record the command, the exit code, and the page count. Do not call that an all-volume CI run. The planning range is 400–500 pages. Do not delete flagship proofs, and do not add filler, to land inside it.

## Independent review

Owner rule t71u, 6 November 2026. Each chapter needs a second reviewer who is not the writer. The writer's own reconstruction and critical re-read are self-checks. They are never an independent review, and they never check the independent-review box.

An independent-review record must name the reviewer, the pushed commit that was read, the date, the scope, and a log of findings with file, section, theorem or exercise, severity, fix commit, and what is still open. If no distinct reviewer has done that work, the gate stays **pending**. Do not invent a signoff. A chapter with an open mathematical or prerequisite defect is not accepted.

| Chapter | Writer self-check | Independent review |
| --- | --- | --- |
| 1 | Mathematical self-pass recorded at `b267c681` by the writing agent on 6 November 2026. Voice not done. The digit figure added later is not part of that pass. | **Pending.** No distinct reviewer. |
| 2–14, preface, appendix | Not second-passed, except the named repair commits in the ledger above. | **Pending.** No distinct reviewer. |

No independent-review report exists. Nothing in this book has been accepted under t71u.

## Tests and builds actually run

- `xelatex -interaction=nonstopmode main.tex` in `volume4-chance`, log `/tmp/v4-xelatex-2.log`, exit 0, `main.pdf` 131 pages, undefined references (one pass). Not `./build.sh`. The PDF was not committed.
- A later pass, log `/tmp/v4-xelatex-3.log`, exit 0, 135 pages, still with undefined references. It includes the digit diagram, the computed binomial/Poisson bars, the reflection step, and the Galton-board photograph. Not `./build.sh`. Still far below 400 pages because the manuscript is unfinished, not because proofs were cut.
- Python: `22/365 = 0.0602739\ldots`, `365\ln 2 = 252.99872\ldots`, so `253/365>\ln 2` and `\exp(-253/365)<1/2`.

Earlier session checks, not re-run as a book test:

- \(\sum_{k=600}^{1000}\binom{1000}{k}/2^{1000} \approx 1.364\times 10^{-10}\) (log-gamma summation).
- Chernoff information bound at the same point: \(\exp(-1000 D(0.6\|0.5)) \approx 1.800\times 10^{-9}\), with \(D(0.6\|0.5)\approx 0.02014\).
- Hoeffding’s \(\exp(-20)\approx 2.061\times 10^{-9}\).
- \(H_{52}\approx 4.538\). \(1-(H_{100}-H_{50})\approx 0.3118\).
- \((1-\ln 2)/2 \approx 0.1534\).

## Artifacts

Uncommitted local `volume4-chance/main.pdf`, 131 pages, from the single XeLaTeX pass above. Not a release file. Production targets remain `dist/volume4-chance.pdf`, `dist/kdp/volume4-chance-print.pdf`, the EPUB, and the wrap, from `./build.sh volume4-chance`.

## Remaining validation

Everything in the ledger marked `planned` or `written` but not `verified`. Independent mathematical reading, layout, and the production build are all still open.
