# Handoff: Volume 9 rewrite

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
[mathematical review](../../review/volume9-complete-rewrite/final-mathematical-review.md),
[editorial review](../../review/volume9-complete-rewrite/final-editorial-review.md) and
[statement records](../../review/volume9-complete-rewrite/final-statement-review.json).

Both required build commands on these fixed book sources exit 0 at **511 print
pages**. The EPUB is 31,586,815 bytes, with 99 full-width 1800-pixel plates;
all 16,454 local links/media references/fragments resolve. There are no overfull
boxes or undefined references. Original numbering, complete original figure
blocks, 57 original figure files, 213 structure numbers and cover-art sources
pass preservation. All 44 added figures, both native photo pages, repaired
proof pages, covers and representative actual EPUB content were inspected.
All 20 citation tests, cross-volume citations (5,118 statements), all 12 numerical
illustration scripts and the Volume 3 register pass (1,177 accepted, 19 unchanged
pre-existing pending). See [the actual validation receipts](../../review/volume9-complete-rewrite/final-validation.md).

PR: https://github.com/OussamaSegh/Order-and-Chance/pull/243. Its delivery record
identifies the exact final-head CI, normal merge and exact-merge publication
receipts. This source handoff records local validation of the fixed book inputs;
remote delivery status is tracked on that PR. No Amazon KDP upload.

## Historical workstream log — begun 14 November 2026

The author has requested a complete rewrite beyond the earlier blueprint pass.
The old "Done" entries below describe that earlier pass only. The new work is
**not complete**. Its starting main is
`9cd86c15bd386d59e7a1c6f96fb0ea5ed808c26b`, on branch
`codex/volume9-complete-rewrite`.

Read [the new baseline and unit ledger](../../review/volume9-complete-rewrite/README.md)
before editing. It records 22 printed units, 200 original exercises, 55 printed
figures, all 544 built labels, the full section contents, and original file hashes.
Fresh PDF-only and full builds both exit 0 and export **385 print pages**. They
report no layout overflow or unresolved references. The baseline EPUB is
26,500,229 bytes; its media checks pass and all 18,199 local XHTML links and media
references resolve. The first full build failed for a missing local `pngquant`;
the complete rerun passed after installing the CI compression tools. The 12 existing numerical scripts and
20 citation tests pass; cross-volume citations match 4,991 numbered statements;
the Volume 3 register exits 0 and reports 19 pending entries. These are baseline
results, not mathematical verification of a new rewrite.

PR #231 already repaired the scored review's local hyperbolic-prerequisite issue
and several editorial issues. Preserve those changes and its index. Do not repeat
the older report's findings as if the fixes had never landed. The complete manuscript has now been read in printed order; findings are in
`review/volume9-complete-rewrite/reading-findings.md`. Chapter 10 and Appendix I
have full draft rewrites, each with two new figures and four exercises, hints and
idea/writeup solutions. Their original figure blocks and labels are preserved.
One unnumbered Riemann photograph has live source metadata and adjacent credits.
The intermediate Chapter 10 PDF-only build exited 0 at 389 print pages, with
no overflow or unresolved references; all 544 old labels and 57 old figure files
passed preservation. The combined PDF-only build also exited 0, at 393 print pages, with all
preservation and layout checks passing. Rendered pages containing all four
added diagrams and the portrait were inspected. Neither unit has its
final independent review or EPUB validation. Appendix E now also has a full draft rewrite, two new diagrams and four new
exercises with complete hints/solutions. The three-unit PDF-only build exited 0
at 397 print pages, with preservation and layout checks passing, and both new
E figures were inspected. See the per-unit review records for exact scope.
Appendix H also now has a full draft rewrite, two new diagrams and four new
exercises. Preface, blurb, KDP copy and canonical About the Cover are rewritten;
the latter corrects the finite-group uniformisation error. The four-unit and
front/back matter PDF-only build exited 0 at 403 print pages. All eight new
diagrams, the credited photograph, preface, colophon and paperback wrap were
inspected. The Riemann photograph has independently inspected 1892 publication
evidence as well as live Commons metadata. All original label/caption/figure
checks still pass. These are intermediate results, not final acceptance.
Chapter 7 now also has a full draft rewrite, two new figures and four exercises.
Its unit-axis hypothesis, rotation identity exception, zero-dimensional O(n)
case and polar-decomposition prerequisite gap are repaired. The five-unit
PDF-only build exited 0 at 407 print pages; both new figures were inspected.
The preservation guard now also verifies all 213 printed part/chapter/section
numbers and both approved cover-art sources. CI found a required credit phrase
in About the Cover; it has been restored and all ten local cover tests pass.
The build predates that wording-only credit repair; a later build will verify it.
Chapter 8 now has a full draft rewrite, two diagrams and four exercises. Its
first-column n=1 atom, signed-test domination, absolute Jacobian, n=1 trace
moment and spectral-statistics qualifications are repaired. The six-unit
intermediate PDF build exited 0 at 411 pages; all twelve added diagrams and
both photographs were inspected. A tower photograph is credited beside the
first Shukhov discussion, with 1897 publication evidence. Later checks also
restored Segre's all-field scope and added the n=0 counterexample to the NEW
non-strict Minkowski exercise; those small repairs pass the full build on 66ca56fd: exit 0, 413 print pages, EPUB 29,554,897 bytes, 67 1800-pixel plates, all 18,245 local links resolved. Twenty citation tests pass. Chapter 9 now has a full rewrite, two new diagrams and four exercises; its intermediate PDF-only build exits 0 at 419 pages with layout/preservation passing. Both diagrams were inspected. Area equality, flow normal, orbifold points, reduced-form listings and closed-axis conditions are repaired; all original labels and statement order remain. Seven units now have drafts, with 14 added diagrams and 28 exercises. The shared cover-note hash invalidated Volume 3 CI inventory/ledger snapshots; only that dependency changed, and hash-only reconciliation preserves all review statuses. Inventory, global ledger and register checks pass locally. Appendix J now has a complete draft rewrite, two diagrams and four exercises. Its intermediate PDF-only build exits 0 at 425 print pages with layout/preservation passing; both figures were inspected. The Helly disk small-set counterexample, zero-dimensional cases, degenerate perimeters and Steiner limit are addressed. Eight units now have drafts, with 16 added diagrams and 32 exercises. Appendix K now has a full draft rewrite, two diagrams and four exercises. Its PDF-only build exits 0 at 433 pages with layout/preservation passing. Both figures were inspected, and one normal label was relocated pending the next build. Four-vertex plateaux/infinite extrema, local Gauss-map area, smooth periodicity, clothoid convergence and small-distance nonflattening are repaired. Nine units now have drafts, with 18 added diagrams and 36 exercises. Chapter 11 now has a full draft rewrite, two diagrams and four exercises. Its PDF-only build exits 0 at 441 pages with layout/preservation passing, and both diagrams plus K's relocated label were inspected. Motion-Haar quotient, joint count measurability, local isoperimetry and full C1 spherical Crofton are repaired. The deferred Volume 15 SU2 citation now points to Example 8.5, with no renumbering. Citation tests and cross-volume checker pass at 5,031 statements. Representative actual six-unit EPUB content and both credited photographs were inspected in Chromium. Ten units now have drafts, with 20 added diagrams and 40 exercises. The full ten-unit build on 5c094ef0 exits 0 at 441 print pages, EPUB 30,384,213 bytes, 75 1800-pixel plates, media checks passing and all 18,350 local links resolved. Chapter 4 now has a full draft, two figures and four exercises. Its PDF-only build exits 0 at 445 pages with layout/preservation passing; both figures were inspected. The Morse existence proof is now taught before the first index-definition/corollary use, while formal numbering stays fixed; Gauss lemma is proved locally and half-plane exponential coordinates no longer depend on Chapter 9. Boundary, angular-cover and shape-operator conventions are repaired. Eleven units now have drafts, with 22 added diagrams and 44 exercises. Chapter 3 now has a full draft, two diagrams and four exercises. Its PDF-only build exits 0 at 451 pages with layout/preservation passing, and both diagrams were inspected. Signed zero-dimensional points, one-dimensional boundary-chart orientation, boundary partitions and infinite-component H0 are repaired; the new torus exercise supplies full H1/H2 calculations with earlier tools. Twelve units now have drafts, with 24 added diagrams and 48 exercises. Chapter 2 now has a full draft, two diagrams and four exercises. Its PDF-only build exits 0 at 455 pages with layout/preservation passing; both diagrams were inspected. Compact Lipschitz bounds precede their use; C0 variational equations, finite escape, zero-dimensional cases and projective flows are repaired. A clarification of the new escape caption awaits the next build. Thirteen units now have drafts, with 26 added diagrams and 52 exercises. Chapter 5 now has a full draft, two figures and four exercises. Its PDF-only build exits 0 at 463 pages with layout/preservation passing, and both diagrams were inspected. Van Kampen boundary/grid issues, the bouquet prerequisite, arbitrary-rank graph compactness and original solution gaps are repaired. An enlarged new b-loop awaits the next build. Fourteen units now have drafts, with 28 added figures and 56 exercises. Chapter 6 now has a full draft, two figures and four exercises. Its PDF-only build exits 0 at 471 pages, with layout/preservation passing and both new diagrams plus the enlarged Chapter 5 loop inspected. Empty reduced conventions, geometric subdivision depths, zero-dimensional endpoints, top transfer-map qualifications, Euler polyhedron hypotheses and empty-set solutions are repaired. All 20 citation tests and the Volume 3 register pass. Main cfc7b20a (Volume 15 PR #244) is integrated by normal merge 2de21df0, preserving the SU2 citation fix. Fifteen units now have drafts, with 30 added figures and 60 exercises. The fixed-source full fifteen-unit build on 57f9e4ee exits 0 at 471 pages: EPUB 30,607,901 bytes, 85 1800-pixel plates, passing media checks, all 17,666 local links resolved, with actual homology EPUB samples inspected. Chapter 1 now has a full draft, two figures and four exercises. Its PDF-only build exits 0 at 477 pages with preservation/layout passing, both diagrams inspected, and the existing credited Riemann portrait moved to its first substantive discussion. Zero-dimensional mean-value/Sard/Whitney cases, matrix-size hypotheses and a crossing-curve prerequisite are repaired. Sixteen units now have drafts, with 32 added figures and 64 exercises; all eleven chapters are rewritten. Appendix A now has a full draft, two diagrams and four exercises. Its PDF-only build exits 0 at 483 pages with preservation/layout passing; both diagrams were inspected. Fagnano equality, ellipse-chord direction, corner-free billiards, identity glide roots, Routh vectors and the lattice prerequisite are repaired. Seventeen units now have drafts, with 34 added figures and 68 exercises. Appendix B now has a complete draft, two diagrams and four exercises. Its PDF-only build exits 0 at 491 print pages, with preservation/layout passing and both diagrams inspected before the exercises. Descartes line branches, Ptolemy coincidences, Steiner first return, Feuerbach equality and generalized-sphere hexlet conditions are repaired. Eighteen units now have drafts, with 36 added figures and 72 exercises. Appendix C now has a complete draft, two diagrams and four exercises. Its PDF-only build completes at 493 print pages with preservation/layout passing and both diagrams inspected. Field characteristics, finite-plane hypotheses, spatial Desargues, division-ring Pappus and the complex ordinary-line counterexample are repaired. Nineteen units now have drafts, with 38 added figures and 76 exercises. Appendix D now has a complete draft, two diagrams and four exercises. Its PDF-only build exits 0 at 499 print pages with preservation/layout passing and both diagrams inspected; two new label backdrops await the next rendering. Poncelet smoothness/orientation, the clockwise convention, empty conics, oriented reflection and a local Fuss proof are repaired. Twenty units now have drafts, with 40 added figures and 80 exercises. Appendix F now has a complete draft, two diagrams and four exercises. Its PDF-only build exits 0 at 505 print pages with preservation/layout passing and both diagrams inspected; one relocated cusp annotation awaits the next rendering. The repaired D labels are clear. Singular-bound prerequisites, characteristic-two conics, actual polars, coefficient extension and all projective parametrization endpoints are repaired. Twenty-one units now have drafts, with 42 added figures and 84 exercises. Appendix G now has a complete draft, two diagrams and four exercises. The twenty-two-unit PDF-only build exits 0 at 511 pages, with preservation/layout passing and both G diagrams plus the repaired F annotation inspected. Geometric versus rational neutral elements, small-characteristic cases, exact Bachet arithmetic, local denominator-growth infinitude and Hesse affine incidence are repaired. All 22 units now have drafts, with 44 added figures, 88 added exercises and two credited photographs. The full additions audit preserves all 302 original formal environments in order and all 200 original exercises before the additions, with every new difficulty/hint/idea/writeup present. All 20 citation tests, 12 numerical illustration scripts, 5,118-statement cross-volume checker and Volume 3 register pass; its 19 pending entries remain unchanged. Separate final review/validation, ready PR, exact-head green CI, normal merge and exact-merge publication verification remain outstanding. PR #243 remains a draft. No KDP upload occurred.

### Post-draft review checkpoint

All units are drafted, but final acceptance remains open. A fresh writer reread of Chapters 1–3 is recorded separately from independent verification. The source prose comparison includes short sentences, excludes protected quotations/figures/bibliography, and leaves no normalized explanatory sentence of two or more prose words unchanged. Conventional one-word formula introducers are listed separately. This is coverage evidence, not proof or prose certification.

The first all-unit full build passed its 511-page PDF/print checks but exited 1 during EPUB formula rendering on an unbraced hat-C expression. Its failed log is preserved; that EPUB is not a deliverable. Two accent arguments are now braced. The follow-up also clarifies nonempty connected graphs for the tree edge count, replaces editorial process wording with direct mathematics, renames a transverse parameter, keeps the unassigned Volume 9 paperback ISBN blank, and holds the cubic closing paragraph after its figure batch. The full rebuild on repaired book sources 612854ac exits 0 at 511 print pages: EPUB 31,551,162 bytes, 99 1800-pixel plates, and all 16,412 local references resolved. A later writer pass clarified the quoted genus-height construction and sphere charts, added nonemptiness to the new root-count exercise, and made connectedness explicit in the Euler comparison (30cbe592). Its PDF-only rebuild exits 0 at 511 pages; a full rebuild for these latest changes is running. The fresh post-draft writer pass has covered all 22 units; it is not independent review. The master plan requires a reviewer other than the writer; explicit authorization for a separate review agent has been requested and remains pending. PR #243 stays a draft. No merge or KDP upload has occurred.

Volume 9, *Shapes*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-09.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-k4hv7k`, one pull request for the whole volume, as Volumes 5–8 each landed on their own pull request. The master plan and the blueprints stay on PR #157 (branch `claude/project-thread-khh5pi`), which remains open and is not merged. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-09.md`. Where it differs from the copy on `main`, the blueprint on PR #157 wins.

## What "rewrite" means here

The blueprint keeps the structure of Volume 9 ("Structure: unchanged"; "Preserve. All chapters and appendices, in their order"): eleven chapters in three parts and eleven appendices A–K. `main.tex` already matches the blueprint's table, so no chapter moves and no chapter number changes. The work is one pass per chapter with the list used for Volumes 5–8:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. Opens with a question, ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number or formula that is not proved on the page is recomputed by a script in `review/volume9-rewrite/`, one per chapter (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's "Sources" section.
5. **References.** Citations of other volumes checked against their printed order today (Volume 5 after its renumbering, `docs/plan/volume-citation-map.md`; Volume 7 after Chapters 2, 6, 13 changed; Volume 8 after its restructure into sixteen chapters and Appendices A–F; Volume 6 `thm:fundamental` after D-20).
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses a later chapter or a later volume (10–15) as a premise.
8. **Build.** The volume builds with no undefined reference.

Numbering inside each chapter is preserved: new statements and exercises go at the end of a list, because Volumes 10–15 cite Volume 9 by hand-typed numbers. `review/volume9-rewrite/baseline-numbering.txt` is the printed order before the rewrite.

Gate B of the master plan (independent verification) is not this pass.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| 1 | Smooth Manifolds | `ch01-manifolds.tex` | Done |
| 2 | Vector Fields and Flows | `ch02-flows.tex` | Done |
| 3 | Differential Forms and Stokes' Theorem | `ch03-forms.tex` | Done |
| 4 | Curvature | `ch04-curvature.tex` | Done |
| 5 | The Fundamental Group and Coverings | `ch05-coverings.tex` | Done |
| 6 | Homology | `ch06-homology.tex` | Done |
| 7 | Matrix Lie Groups | `ch07-liegroups.tex` | Done |
| 8 | Haar Measure and Weyl Integration | `ch08-haar.tex` | Done |
| 9 | The Hyperbolic Plane and the Modular Group | `ch09-hyperbolic.tex` | Done |
| 10 | The Riemann Mapping Theorem | `riemann-mapping.tex` | Done |
| 11 | Integral Geometry | `ch10-integral.tex` | Done |
| A–K | Appendices | `geometry-ch02` … `geometry-ch12` | Done |
| — | Preface, blurb, `kdp.md`, citations of Volume 9 in other volumes | | Done |

## What changed, chapter by chapter

- **1.** Opening question; closing section. The null-set lemma cited Carathéodory's extension theorem (Volume 7, Theorem 7.10) for a cover by cubes: now outer regularity (Volume 7, Proposition 7.12) and the dyadic cubes of its proof. Check: `check_ch01_manifolds.py`.
- **2.** Opening question; closing section. Equidistribution of $k\alpha$ now cites Volume 5, Corollary 6.14 (it cited Volume 6, Chapter 11). The escape lemma no longer restarts at a negative time when $\beta<\tau/2$. Check: `check_ch02_flows.py`.
- **3.** Opening question; closing section. Brouwer for the disc is Volume 7, Theorem 6.7 (the text said Volume 8); the dog on a leash is Volume 7, Proposition 6.6; Fubini cited as Volume 7, Theorem 9.6. Check: `check_ch03_forms.py`.
- **4.** Blueprint item: the two statements without a proof on the page, Corollary `cor:gaussbonnet` and Corollary `cor:chimorse`, now have proofs (the first says why it does not use itself through Theorem `thm:morseexists`; the second classifies non-degenerate critical points of a surface). Gauss's field seasons are 1821–1825 (the text said 1818–1832). Hopf's paper is 1927. The pseudosphere's volume is $\pi/3$, half the unit hemisphere (the text said half the ball, attributed to Huygens without a source). Circle problem: Volume 6, Chapter 2. Opening question; closing section. Check: `check_ch04_curvature.py`.
- **5.** The winding number is Volume 7's, not Volume 8's; $F_2$ in Volume 8, Chapter 13 is the Banach–Tarski free group. Opening question; closing section. Check: `check_ch05_coverings.py`.
- **6.** Blueprint item: one paragraph after Borsuk–Ulam states the homology of real projective space mod 2, read off the transfer sequence actually printed. The remark on Radó and the classification of surfaces now says both are quoted (blueprint "Stated without proof"). Hopf 1927. Opening question; closing section (end of Part II). Check: `check_ch06_homology.py` (the 3×3 torus triangulation, its Betti numbers, the Klein bottle).
- **7.** Opening question; closing section. Citations of Volume 8 (Proposition C.13, Theorems 3.2, 4.3) and Volume 3 (Lemma 12.3) checked. Check: `check_ch07_liegroups.py`.
- **8.** Blueprint item: the modular function is now $\delta$ and the Vandermonde product $V$ (both were $\Delta$); the uniform variable in the solution of `ex:su2weyl` is now $R$. The Vandermonde determinant is Volume 1, Proposition 7.4 (the text said Volume 3; `statements.py` prints Volume 1 one chapter too high because Volume 1 starts at Chapter 0). Andréief's lemma is dated 1886, the year the Bordeaux volume appeared (Forrester 2019 added to the sources); Mehta–Gaudin 1960 added to the sources. Closing section. Check: `check_ch08_haar.py` (Haar sampling, Weyl's formula, trace moments, gap probability, Dyson's limit).
- **9.** Blueprint items: the tiling by $F$ now rests on Volume 6, Theorem 12.2(b) (it cited Volume 13, Theorem 17.1); the pointer to Volume 13, Chapter 5 is gone; Hopf's ergodicity theorem is stated as quoted, with what it says. The reminder and the area computations cited Appendix I by stale hand-typed numbers ("Proposition J.4", "Lemma 10.5", "Theorem J.8 of Volume 9"): now `\ref`s to Appendix I. Gauss's 1812 letter to Laplace added to the sources. Opening question; closing section. Check: `check_ch09_hyperbolic.py` (including cutting sequences computed by walking the Farey triangles).
- **10.** Every citation now has its number: Volume 5, Corollary 9.12, Theorems 9.15, 9.18, 9.19, 9.38; Volume 7, Theorems 4.15 and 6.10; Volume 8, Corollary 14.3 and Proposition 14.4 (Chapter 14 after Volume 8's reorder). Sources for Weierstrass 1870 and Koebe 1912 added. Opening question; closing section. Check: `check_ch10_riemannmap.py` (Cayley, strip, slit plane, the square map).
- **11.** Hand-typed appendix numbers were stale ("Corollary K.6" for Barbier, which is J.6; "isoperimetric inequality of Volume 9"): now `\ref`s to Appendix J. Bertrand's three answers cite Volume 4, Theorem 5.11; Buffon Volume 4, Theorem 5.12; uniqueness of measures Volume 7, Theorem 7.5. The kinematic formula is marked as quoted. Closing section (end of the chapters). Check: `check_ch11_integral.py` (Bertrand, Crofton and Buffon by Monte Carlo, Laplace's grid, the cube's shadows, Poincaré's formula, Crofton on the sphere).
- **Appendices A–K.** Each opens with a paragraph "What this appendix connects, and what it assumes" (blueprint). F: Bézout's heading says the multiplicity is relative to an auxiliary point and the intrinsic form is Volume 13, Chapter 14; the choice of the point is now part of the definition. G: the associativity theorem's heading says nine distinct points; the solutions no longer use associativity for all triples (the converse of `ex:collinear` is proved directly; `ex:twotorsion`, `ex:torsionsix`, `ex:countfive` compute with the chord rule; `ex:changeorigin` and `ex:sixonconic` now ask for the statements that hold without associativity and point to Volume 13 for the rest); the Nagell–Lutz remark is a forward pointer, not a proof. H: the Hermite solution already proved its two facts; `ex:index` now cites Volume 3, Lemma 7.5; the pointer to "Volume 13, Chapter 5" is now "Volume 13". I: "Volume 9 studies this group" is now Chapter 9. The citations "Volume 1, Theorems 7.9 and 7.10" in E are correct: `statements.py` printed Volume 1 one chapter too high (it ignored `\setcounter{chapter}{-1}`); fixed. Check: `check_appendices.py`.
- **8 (later).** The remark after Dyson's formula now says that the sine-kernel limit for the Hermitian ensembles is not proved here and is a preview of Volume 12 (blueprint table "Stated without proof").

## Build and citations

Full build passes with no undefined reference: 377 pages (2026-11-13). Numbering inside the volume is identical to `baseline-numbering.txt`, so the citations of Volume 9 in Volumes 10, 12 and 15 still resolve (checked by hand: V10 Theorems 7.9, 8.3, 8.8, Exercise 8.3, Lemma 6.2, Exercise 6.1; V12 Theorems 8.3, 8.13, 8.15, 10.5, Corollary 8.16; V15 Theorem 8.8). Owed by Volume 10: its `ch11-compact.tex` attributes the Vandermonde determinant to Volume 3; the proof is Volume 1, Proposition 7.4.

## Tools

`review/volume9-rewrite/statements.py <volume dir>` prints every numbered statement in printed order. `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py` lists hand-typed numbers inside the volume. `list_citations.py` lists every citation of another volume.

## How to build

`./build.sh --pdf-only volume9-shapes`, or `xelatex` in `volume9-shapes/` as `build.sh` does. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`.

Post-review checkpoint: the full build on book sources 30cbe592 exits 0 at 511 print pages. Its EPUB is 31,553,132 bytes, has 99 1800-pixel plates, passes the media check and resolves all 16,416 local references. The writer follow-up covers all 22 units. R12 supplies a direct cosine-law step in Appendix I and requires a new PDF/full rebuild; it does not change any statement, label or figure. Independent review and final CI/merge/publication remain pending.
