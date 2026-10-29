# Order and Chance — Volume 0: revised delivery

The local reconstruction is complete through batches A--J. The final book has ten
chapters, 155 fully solved exercises (all 130 originals retained), ten selected
bridge problems, a new proof-language chapter and a final integrative investigation.
Its reading PDF has 296 physical pages; the print interior has 295, ending at
numbered page 283 after 12 roman front-matter pages.

## Final files

- [Validated EPUB](/workspace/Order-and-Chance/dist/volume0-mathematical-maturity.epub)
- [Validated HTML reader preview](/workspace/Order-and-Chance/build/digital-review/site/read/volume0-mathematical-maturity/index.html)
- [EPUB/HTML validation follow-up](DIGITAL-VALIDATION.md)

- [Complete reading PDF](/workspace/Order-and-Chance/dist/volume0-mathematical-maturity.pdf)
- [Print interior](/workspace/Order-and-Chance/dist/kdp/volume0-mathematical-maturity-print.pdf)
- [Matching print wrap](/workspace/Order-and-Chance/dist/kdp/volume0-mathematical-maturity-cover-wrap.pdf)
- [Complete revised source archive](/workspace/Order-and-Chance/dist/volume0-revision/Order-and-Chance-Volume0-source.zip)
- [Original source archive](/workspace/Order-and-Chance/dist/volume0-revision/Order-and-Chance-original-source.zip)
- [Editorial and QA report archive](/workspace/Order-and-Chance/dist/volume0-revision/Volume0-reports.zip)
- [Artifact hashes and exact source commit](/workspace/Order-and-Chance/dist/volume0-revision/manifest.json)

The source archive contains the complete tracked project, including shared assets
and build configuration. The original eight-chapter source is separately restorable.
The reconstruction's editorial changes are confined to Volume 0, its review tools
and reports; pre-existing upstream publishing changes were integrated before edits.
No other-volume mathematical text was independently revised.

## Required editorial and mathematical records

- [Initial evidence-based plan and prerequisite analysis](PLAN.md)
- [Final table of contents](TABLE-OF-CONTENTS.md)
- [Final dependency map and explicit return problems](DEPENDENCIES.md)
- [Content migration summary](CONTENT-MIGRATION.md) and [unit ledger](migration-units.json)
- [Mathematical corrections](MATHEMATICAL-CORRECTIONS.md)
- [Every exercise's verification record](EXERCISE-VERIFICATION.md)
- [Numbering concordance for all original labels](NUMBERING-CONCORDANCE.md)
- [Other-volume citation inventory](OTHER-VOLUME-CITATIONS.md)
- [Independent skeptical review](independent-review.md)
- [Final editorial review](FINAL-EDITORIAL-REVIEW.md)
- [Compilation and test report](COMPILATION-AND-TESTS.md), with exact logs in `final-logs/`
- [Outstanding issues and scope limits](OUTSTANDING-ISSUES.md)

All four mathematical/source scripts passed 10,894 checks in total (with overlapping
examples), alongside 17 publishing regression tests. These computations support
the source reviews and written proofs; they are not a formal proof certificate.
The complete build has no overflow, unresolved references, missing glyphs or
automatically shrunken displays. Two package compatibility warnings and fifteen
underfull-line warnings remain disclosed.

## Cumulative checkpoints

Working branch: `editorial/volume0-reconstruction-20261028`.
Recoverable tags: `volume0-batch-A` through `volume0-batch-J`.
Each batch report uses the requested changes/mathematics/pedagogy/preservation/
verification/issues/next-work structure.

| Batch | Report | Cumulative PDF |
|---|---|---|
| A | [Audit](BATCH-A.md) | [Original baseline](/workspace/volume0-checkpoints/A/Volume0-baseline.pdf) |
| B | [Language](BATCH-B.md) | [PDF](/workspace/volume0-checkpoints/B/Volume0.pdf) |
| C | [Discrete](BATCH-C.md) | [PDF](/workspace/volume0-checkpoints/C/Volume0.pdf) |
| D | [Analysis](BATCH-D.md) | [PDF](/workspace/volume0-checkpoints/D/Volume0.pdf) |
| E | [Algebra](BATCH-E.md) | [PDF](/workspace/volume0-checkpoints/E/Volume0.pdf) |
| F | [Calculus/inequalities](BATCH-F.md) | [PDF](/workspace/volume0-checkpoints/F/Volume0.pdf) |
| G | [Probability](BATCH-G.md) | [PDF](/workspace/volume0-checkpoints/G/Volume0.pdf) |
| H | [Integration](BATCH-H.md) | [PDF](/workspace/volume0-checkpoints/H/Volume0.pdf) |
| I | [Verification](BATCH-I.md) | [PDF](/workspace/volume0-checkpoints/I-final/Volume0.pdf) |
| J | [Production](BATCH-J.md) | [Final PDF](/workspace/volume0-checkpoints/J/Volume0.pdf) |

## Rebuild

In the current environment, activate
`/workspace/order-chance-system/activate.sh`, then run
`./build.sh --pdf-only volume0-mathematical-maturity` from the repository root.
Elsewhere, supply XeLaTeX and the repository's documented TeX packages, Poppler,
Python and `tools/requirements-build.txt`; the approved font files are bundled.
Mathematical verification additionally uses numpy, scipy, sympy and mpmath.
The PDF-boundary scan used PyMuPDF; that optional diagnostic is distinct from the
standard production checks. Archive validation verifies CRCs and source file content.

The next coordinated series task is to reconcile hardcoded numeric citations in
other volumes using the concordance. Historical retrieval was targeted, not
exhaustive; a physical proof was not validated. Revised EPUB/HTML were subsequently
built and validated as recorded in DIGITAL-VALIDATION.md. Remaining limits are
recorded explicitly and were not counted as successful tests.
