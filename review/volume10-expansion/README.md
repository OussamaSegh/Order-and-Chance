# Volume 10 teaching expansion — active record

Starting main: `b005c4a0a33409f443594f3bb1efe3e955e95468` (published PR #245).
Branch: `codex/volume10-teaching-expansion`. Actual folder: `volume10-abstraction`.
The repository was fetched and branches, PRs, prior handoff/reviews and actual
printed `main.tex` order inspected before edits. No competing open Volume 10 work
was found. Baseline: 11 chapters, 116 exercises, 34 mathematical figures, one
credited portrait; 279 print / 280 reading pages. The portrait is unnumbered and
is not included in the mathematical figure count.

## Immutable baseline

`starting-source.json` captures full original formal/exercise/hint/solution/figure
blocks, source labels, cross-volume reference lines, all Volume 10 source hashes,
protected shared artwork hashes, exact starting SHA and addition counts.
`starting-main.tex` records printed order; `starting-printed-labels.json` and
`starting-structure.json` record compiled numbers. They come from the previously
reviewed complete build whose book-input fingerprint exactly matches fetched
main (`starting-book-fingerprint.txt`). Published page counts/artifact receipts
are independently documented on PR #245. They are baseline evidence, not claims
of successful expansion builds.

## Approved acceptance

Four new exercises and two unnumbered worked examples in each existing chapter.
Three new capstone chapters (12 computable resolutions, 13 cohomology through
resolutions, 14 Schur–Weyl), each with eight solved exercises and two figures.
Final counts: 14 chapters, 184 exercises, 40 mathematical figures, one portrait.
All existing numbers, mathematical statements, exercises/hints/solutions, figures,
artwork, typography and identifiers remain protected. New exercise prefixes are
`ex:v10exp-chNN-`; examples use explicit source markers. Target 380–450 print
pages, hard ceiling 600; never pad or compress typography.

Writer ownership: Chapters 1–4, 5–8, 9–11, and each of 12,13,14 are six disjoint
assignments. Parent owns front matter, main, audits, content plan, handoff, CI and
integration. Writers do not stage or commit. Separate reviews rotate after writing;
no writer is their chapter's sole reviewer. These are AI reviews, not human
certification. Current state: baseline/plan captured; writing underway. Final
builds, final review, CI, merge and publication are not yet claimed. No KDP upload.
