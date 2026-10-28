# First-edition copy — 28 October 2026

## Batch identifier
First-edition presentation, following the author's clarification.

## Changes implemented
Rephrased the Volume 0 preface's explanation of chapter prerequisites without
referring to an original edition. Removed the field guide's entire
“Finding a citation from the earlier arrangement” section and comparison table.
Recorded the author's series-wide first-edition rule in AGENTS.md.

## Mathematical improvements
No mathematical claims, proofs or calculations changed.

## Pedagogical improvements
The reader sees the book's learning path without comparisons to unpublished
development versions or instructions to reconcile former numbering.

## Content preservation
All ten chapters, 155 exercises with their hints and solutions, and 299 semantic
labels remain. Development and migration history stay in internal reports.
Baseline commit: 222f151. A restorable source checkpoint is at
/workspace/volume0-checkpoints/first-edition-copy/source-before.tar.

## Verification
Source structure and identifier-preservation checks pass. A targeted source
scan finds no edition-comparison language in Volume 0's reader-facing TeX.
The existing first-edition companion-copy check passes for all 19 books.
The full production rebuild passes, including layout, font, navigation and KDP
interior/cover export checks. Reading PDF: 296 pages; print interior: 295 pages.
Text checks confirm the old-edition references are absent and the first-edition
explanation is present in PDF, EPUB and HTML. EPUBCheck 5.3.0 reports zero fatals,
errors, warnings or infos. Digital validation verifies 299 labels, 496 explicit
references and all 155 exercise/hint/solution triples in both EPUB and HTML,
with no missing local resources or targets. git diff --check passes.
Logs and the restorable checkpoint are under
/workspace/volume0-checkpoints/first-edition-copy/.

## Remaining issues
No mathematical review is claimed for this copy-only change.

## Next work
Push the verified source and check the exact publication run. Local production
verification does not establish that the public site has deployed the change.
