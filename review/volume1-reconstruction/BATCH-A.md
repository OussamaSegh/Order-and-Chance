# Batch A — Repository and mathematical baseline

## Changes implemented
Read the 1,164-line author directive, repository instructions, all fourteen chapter/frontmatter files (4,470 lines), existing review and the available revised Volume 0. Generated source inventories and a migration skeleton before manuscript edits. Canonical entry point: `volume1-integers/main.tex`; shared infrastructure remains intact.

## Mathematical improvements
No mathematical changes in this baseline. The source has 81 numbered results with 81 proof environments, 97 exercises with 97 hints and 97 solutions, 205 explicit labels, 28 mathematical figure source files and four credited portraits. Thirty figure environments include portraits; counts are not interchangeable.

Confirmed correction: the last sentence of the solution `ex:two` incorrectly assigns norm 2 to every case, including the inert ideal `(2)`, whose norm is 4. Confirmed dependency defect: `ex:n2n` uses Fermat before its Chapter 3 proof. Stale Volume 0 citations include polynomial Chapter 3, complex Chapter 2 and series Chapter 5; these now mean Chapters 5, 4 and 3 respectively.

Candidate clarified: `prop:intcrit` is not a counterexample to the integrality criterion. Its scalar is an integer because its monic factor times that scalar is an integer polynomial. This implication is implicit in the original. Expand the monic-divisor argument and review it independently; do not report a false theorem.

## Pedagogical improvements
The plan prioritises the compressed field/ideal transition and construction of the p-adic fraction field. Existing sieve, cancellation warnings, conditional root lifting, coprime density model, Gaussian rounding, two reciprocity proofs and complete four-square descent already supply substantial requested coverage.

## Content preservation
Baseline commit: `a65d685d941b8cef2c1d41f51bff65a71f885e11`. Branch: `editorial/volume1-reconstruction-20261028`. Restorable original Git archive, directive, reading/interior PDFs, aux, toc and logs: `/workspace/volume1-checkpoints/baseline/`. No other volume is edited. Figure and portrait assets are retained.

## Verification
Executed `source /workspace/order-chance-system/activate.sh; ./build.sh --pdf-only volume1-integers`: PASS. Reading PDF 174 physical pages, interior 173; the last numbered content page is 163. Layout checker reports 169 whole boxes, maximum 277.0 pt, no overflow or unresolved references. Interior fonts/style, covered/interior identity, cover master and print preflight pass. Inventory confirms all 97 exercise/hint/solution triples. Compilation is not mathematical verification.

## Remaining issues
The mathematical review is a human-style source audit, not formal proof verification. Computational evidence and detailed second-pass records follow in later batches. Historical assertions have existing references; primary historical documents have not all been independently retrieved. Other books retain their older printed citations; produce a concordance rather than modify them.

## Next work
Batch B: early arithmetic boundary cases, a self-contained route for `ex:n2n`, modest algorithmic clarification. Complete-book build and checkpoint.
