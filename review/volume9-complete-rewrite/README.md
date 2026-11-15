# Volume 9 complete rewrite: baseline and acceptance record

The immutable baseline below describes starting main. Current review and production
results are recorded separately; the baseline is never replaced by rewritten material.

## Current checkpoint — manuscript and local validation complete

Book sources: `fb4502e3acda521b598c5bc3cd5e46e2f0e028d0`.
All eleven chapters and eleven appendices are fully rewritten and reviewed,
with 44 new figures, 88 fully solved exercises and two credited public-domain
photographs. All 302 original numbered statements were compared with starting
main; the review accounts for 245 proofs, 288 hints and 288 solutions.
R01–R20 are repaired and linked to their fixing commits.

The author explicitly instructed **“You review and merge.”** Codex performed
the separate final mathematical/editorial review phase itself. No independent
second reader or different review agent is claimed. See the
[mathematical review](final-mathematical-review.md),
[editorial review](final-editorial-review.md) and
[statement records](final-statement-review.json).

Both required build commands on these fixed book sources exit 0 at **511 print
pages**. The EPUB is 31,586,815 bytes, with 99 full-width 1800-pixel plates;
all 16,454 local links/media references/fragments resolve. There are no overfull
boxes or undefined references. Original numbering, complete original figure
blocks, 57 original figure files, 213 structure numbers and cover-art sources
pass preservation. All 44 added figures, both native photo pages, repaired
proof pages, covers and representative actual EPUB content were inspected.
All 20 citation tests, cross-volume citations (5,118 statements), all 12 numerical
illustration scripts and the Volume 3 register pass (1,177 accepted, 19 unchanged
pre-existing pending). See [the actual validation receipts](final-validation.md).

PR: https://github.com/OussamaSegh/Order-and-Chance/pull/243. Its delivery record
identifies the exact final-head CI, normal merge and exact-merge publication
receipts. This source handoff records local validation of the fixed book inputs;
remote delivery status is tracked on that PR. No Amazon KDP upload.

## Provenance

- Starting main: `9cd86c15bd386d59e7a1c6f96fb0ea5ed808c26b`.
- Working branch: `codex/volume9-complete-rewrite`.
- Earlier rewrite: [PR #216](https://github.com/OussamaSegh/Order-and-Chance/pull/216), merged.
- Scored review: [PR #230](https://github.com/OussamaSegh/Order-and-Chance/pull/230), merged.
- Review repairs: [PR #231](https://github.com/OussamaSegh/Order-and-Chance/pull/231), merged as
  `42d2355b9305d497885a54e139e0e46edadbb1e8`. Preserve its local hyperbolic proofs,
  index, jacket corrections and additional Riemann mapping exercises.
- Controlling blueprint: `docs/plan/book-09.md` on the still-open
  [PR #157](https://github.com/OussamaSegh/Order-and-Chance/pull/157), fetched at
  `d9a1c8245fb07ba96cd81e96300b97995d014df1`. The same plan branch contains
  `docs/plan/MASTER-PLAN-V5-V15.md`, which is absent from current main.
- Known deferred review item V9-04 is a Volume 15 citation of Theorem 8.8
  for the SU(2) density; PR #231 explicitly left that external sentence untouched.
  It is not claimed fixed by this baseline.
- The old handoff's 377-page count and its original numbering file are historical.
  Use this workstream's fresh build record for the new comparison.

Read during this baseline pass: root `AGENTS.md`, `docs/WRITING-STYLE.md`,
`docs/agents/mathematician-writer.md`, `docs/SERIES-STRUCTURE.md`,
`docs/design/interior.md`, `docs/WORKSTREAM-COORDINATION.md`, Volume 9's handoff,
the controlling blueprint and the master plan's acceptance requirements.
PRs #216 and #230 have no review or discussion entries in the fetched responses.
The complete manuscript has now been read in printed order, including all
chapters, appendices and front/back matter. `reading-findings.md` records the
findings and repair plan. This initial read is not the separate final review.

## Preservation records

`starting-source.json` records the printed unit order from `main.tex`, every unit's
source labels, exercise and figure counts, and SHA-256 hashes of all 87 tracked
Volume 9 files. `starting-statements.txt` is the existing statement walker's fresh
inventory, including unlabelled statements, on starting main. Captured text and
contents records have trailing whitespace removed for `git diff --check`; numbers
and mathematical text are retained. `starting-printed-labels.json` records all 544 built labels, including all four
numbered equations and all 55 printed figures, with their printed numbers, pages,
anchors and full captions. `starting-contents.tex` records section numbering,
including unlabelled sections. There are 302 formal numbered statements and
200 exercises. All 57 original files under `figures/` are hashed, including
unprinted sources. `check_preservation.py` compares the current build, original figure and cover-art
files, and all 213 printed part/chapter/section numbers with these records; `--require-additions` also checks the per-unit
addition counts. It does not establish prose coverage or proof correctness.
Do not replace these baselines with a snapshot of rewritten material.

## Unit ledger

All units require a complete prose and mathematical pass, a separate review,
two additional illustrations and four additional exercises with hints and full
solutions. Counts below are the starting counts, not additions.

| Unit | Title | Original exercises | Original figures | New complete rewrite |
| --- | --- | ---: | ---: | --- |
| 1 | Smooth Manifolds | 7 | 2 | Complete rewrite; reviewed; both builds pass |
| 2 | Vector Fields and Flows | 7 | 2 | Complete rewrite; reviewed; both builds pass |
| 3 | Differential Forms and Stokes' Theorem | 6 | 2 | Complete rewrite; reviewed; both builds pass |
| 4 | Curvature | 6 | 2 | Complete rewrite; reviewed; both builds pass |
| 5 | The Fundamental Group and Coverings | 6 | 2 | Complete rewrite; reviewed; both builds pass |
| 6 | Homology | 6 | 2 | Complete rewrite; reviewed; both builds pass |
| 7 | Matrix Lie Groups | 6 | 1 | Complete rewrite; reviewed; both builds pass |
| 8 | Haar Measure and Weyl Integration | 6 | 1 | Complete rewrite; reviewed; both builds pass |
| 9 | The Hyperbolic Plane and the Modular Group | 6 | 3 | Complete rewrite; reviewed; both builds pass |
| 10 | The Riemann Mapping Theorem | 3 | 1 | Complete rewrite; reviewed; both builds pass |
| 11 | Integral Geometry | 6 | 1 | Complete rewrite; reviewed; both builds pass |
| A | Transformations | 16 | 4 | Complete rewrite; reviewed; both builds pass |
| B | Inversion | 12 | 3 | Complete rewrite; reviewed; both builds pass |
| C | Projective geometry | 12 | 4 | Complete rewrite; reviewed; both builds pass |
| D | Conics | 12 | 4 | Complete rewrite; reviewed; both builds pass |
| E | Quadratic forms and quadrics | 12 | 3 | Complete rewrite; reviewed; both builds pass |
| F | Plane curves | 12 | 3 | Complete rewrite; reviewed; both builds pass |
| G | Cubic curves | 12 | 4 | Complete rewrite; reviewed; both builds pass |
| H | Lattices and sphere packings | 12 | 4 | Complete rewrite; reviewed; both builds pass |
| I | Non-Euclidean geometry | 12 | 2 | Complete rewrite; reviewed; both builds pass |
| J | Convex bodies | 12 | 3 | Complete rewrite; reviewed; both builds pass |
| K | Curvature of Curves and Polyhedra | 11 | 2 | Complete rewrite; reviewed; both builds pass |

Totals: all 22 units have complete drafts, retaining 200 original exercises and 55 original figures and adding 88 exercises and 44 illustrations. Each unit has two added figures and four added exercises, with unique labels, difficulty, hints and complete idea/writeup solutions. Two photographs have adjacent credits, native resolution and public-domain source evidence. All added figure pages and both photograph placements have now been inspected in the current 511-page print build. The original 544 labels/captions, 213 structural numbers, 57 figure files and two cover-art sources pass preservation.

Production checkpoint details, including earlier failed attempts, are in the corresponding build logs and the handoff. All twelve existing numerical illustration scripts, twenty citation tests, the cross-volume checker (5,118 statements) and the Volume 3 register pass on book sources 30cbe592. The register's nineteen pending entries are unchanged. Numerical experiments are illustrations, not proofs. The current EPUB rerun and independent review are still pending; no failed or cancelled CI run is called green.

The fresh writer pass after all drafts covers all 22 units. Its findings and source hashes are recorded in postrewrite-writer-audit.md and postrewrite-review-findings.md. The 302-statement comparison packet includes unlabelled original statements and explicitly marks them as not independently reviewed. It is a comparison aid, not a verification certificate. The author has been asked to authorize a separate reviewer, as required by the master plan.

## Validation scope

Baseline numerical scripts are illustrative checks, not proof verification.
The final rewritten manuscript still needs every requested build, proof review,
numbering comparison, visual inspection, EPUB check and exact-head CI check.
Do not mark the PR ready or merge this baseline as the completed volume.
No upload to Amazon KDP is authorized or performed.

## Actual baseline results

- `./build.sh --pdf-only volume9-shapes`: exit 0, **385 print pages**;
  565 whole boxes checked, no overflow or unresolved references, reading-PDF,
  font, bleed, print-interior and cover checks passed.
- Initial attempt stopped for missing `pypdf`; installed the repository's declared
  build/test dependencies into the existing toolchain using `uv pip`. The successful
  rerun above is separate from that failed attempt.
- Citation tests: `python3 -m unittest discover -s tools -p '*citation*.py'`,
  exit 0; 20 tests passed.
- `python3 tools/cross_volume_citations.py`: exit 0; 4,991 numbered statements.
- `python3 review/volume3-internal/registers.py`: exit 0; 1,177 accepted-internal,
  **19 pending**. Pending entries are not claimed resolved.
- All 12 `review/volume9-rewrite/check_*.py` scripts: exit 0.
- `python3 review/volume9-complete-rewrite/check_preservation.py`: exit 0;
  544 labels and 57 original figure files preserved, original captions unchanged.
- Visually inspected baseline interior PDF pages 13, 14, 158, 180, 240 and 383
  as a six-page contact sheet. No collision was visible in that sample. This is
  not a complete visual review or an inspection of new material.

Captured command output is in the adjacent `baseline-*.txt` files. The first full build exited 1 at EPUB compression because `pngquant` was absent;
its output is retained in `baseline-full-build-FAILED.txt`. Installed Debian
`pngquant` 2.18.0 into the workspace-local toolchain and oxipng 9.1.5 from the
release URL specified in CI. The workspace activation script now includes their
local binary directories. No repository build rule or validation threshold changed.
The complete `./build.sh volume9-shapes` rerun subsequently exited **0**.
Its output is retained in `baseline-full-build.txt`. It exports 385 print pages,
55 full-width EPUB plates at 1,800 pixels, and baseline-scaled formula images.
The final EPUB is **26,500,229 bytes**. A separate XML package audit checked
31 XHTML documents and resolved all **18,199** local href/src references.
`baseline-artifacts.json` records output sizes, page counts and SHA-256 hashes.
Representative EPUB text was inspected in the part opener, Chapter 9 and Appendix D;
no rendered EPUB or physical Kindle inspection is claimed.

The parser was also exercised with nested and escaped caption braces, duplicate
labels and an unclosed group: captions were retained and invalid input rejected.
The preservation check's `--require-additions` mode exits **1**, as it should at
this stage: all 22 units lack their two new figures and four new exercises. Its
44 diagnostics are retained in `baseline-additions-NOT-PASSED.txt`. This is an
explicit unfinished acceptance gate, not a passing rewrite check.

The baseline cover wrap was also rendered and inspected. No text collision or
visible frame/artwork defect was seen in the sample rendering.

## CI and delivery state

[Run 43603022842](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43603022842)
succeeded on intermediate head `a21bc61055d1f168b2c6fa1493cc9598b63db74d`.
Its `list` and `site` jobs passed; `build` and `debs` were skipped because this
workstream has no book-source changes. This is **not** an exact-final-head book
build or publication certificate. Later validation-record commits need their own
CI result. PR #243 remains a draft; no merge or merge-commit publication exists
for this request. The additions gate is still failed. At that earlier checkpoint, sixteen unit rewrites and all separate final reviews remained outstanding; the current checkpoint is recorded at the top.

`git diff --check` passed after removing trailing whitespace from captured text.
No new figures, exercises or photographs were added; no new mathematical
correction is claimed. No Amazon KDP upload was made.

Post-review checkpoint: the full build on book sources 30cbe592 exits 0 at 511 print pages. Its EPUB is 31,553,132 bytes, has 99 1800-pixel plates, passes the media check and resolves all 16,416 local references. The writer follow-up covers all 22 units. R12 supplies a direct cosine-law step in Appendix I and requires a new PDF/full rebuild; it does not change any statement, label or figure. Independent review and final CI/merge/publication remain pending.
