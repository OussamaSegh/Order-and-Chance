# Volume 10 complete rewrite — working record

Starting main: `59014a9aad3454ad60786c6549c81fcac88df9df`.
Working branch: `codex/volume10-complete-rewrite`.
Actual directory: `volume10-abstraction`, resolved from fetched main and series catalog.
Printed order comes from `main.tex`: eleven chapters, three parts, no appendices.
Earlier rewrite PR #220 is merged; its handoff and scripts remain historical evidence.
PR #157 is now closed; its retained branch blueprint was read rather than assuming
that the main copy (which still describes the departed shuffle chapter) is current.
No open Volume 10 PR or successor branch was found at initial inspection.

## Immutable baseline

`starting-source.json` records all original unit labels, counts, complete figure
blocks, cross-volume reference lines, tracked Volume 10 hashes, protected shared
art hashes and printed order. `starting-statement-content.json` preserves full
mathematical text of all 252 original statement/exercise blocks (180 formal
statements, 72 exercises). `starting-statements.txt` gives their printed numbers.
`starting-printed-labels.json` and `starting-contents.tex` come from the untouched
main build and record built numbers, captions, anchors and structural numbering.
Original figure files: 12. Original printed figures: 12.

Initial PDF build failed before typesetting because pypdf was absent. This is
recorded as FAILED, not successful validation. Installed declared dependencies
using `uv pip install --python /workspace/order-chance-venv/bin/python -r tools/requirements-build.txt`
(exit 0). With the approved activation script, the repeated exact command
`./build.sh --pdf-only volume10-abstraction` exited 0 at **189 print pages**.
This paragraph records the initial baseline only. Final local validation is
separate below; no baseline EPUB was required or claimed.

## Work ownership and acceptance

Five writing agents own Chapters 1–2, 3–4, 5–6, 7–8 and 9–10 respectively.
The coordinating writer owns Chapter 11, front/back copy, photographs, handoff,
production and Git integration. A sixth agent performs a separate review; its
initial read is not final certification. No agent may modify another writer's
chapter, original figure files/blocks or protected cover artwork.

Every unit needs complete prose, proof and exercise rewriting; exactly two new
mathematical illustrations after its original figures; and four new exercises
with stars, hints and complete idea/writeup solutions after original lists.
Totals required: 22 new figures and 44 new exercises. No appendix is printed.
Original section/statement/exercise/equation/figure numbering remains protected.
No photography count is imposed; only useful verified public-domain images qualify.
Current source state: all eleven units completely rewritten and separately
reviewed; exactly 22 new figures, 44 solved exercises and one verified portrait.
Both final local builds exit 0 at 279 print pages. See [final validation](final-validation.md),
[visual inspection](final-visual-check.md), [mathematical review](final-mathematical-review.md),
[editorial review](final-editorial-review.md) and [correction index](corrections-and-review-index.md).
The source is ready for exact-head CI and normal merge. Their actual run IDs,
merge SHA and downloaded release/Pages verification belong in the
[live acceptance receipt](https://github.com/OussamaSegh/Order-and-Chance/pull/245#issuecomment-6892058253).
The 279-page result is below the 300-page aim; no padding/type changes were used.
Reviews are separate AI reviews, not human certification.
No Amazon KDP upload.
