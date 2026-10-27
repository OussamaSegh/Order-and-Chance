# Charcoal/coral design rollout — 27 October 2026

The latest author selection is the **left-aligned** cover in
[the approved reference](../docs/reference/approved-charcoal-coral-volume-0.png).
The earlier centered choice is superseded. The clean workspace was updated with
`git pull --ff-only origin main` to `18cab2c` before editing.

## Implementation

Shared vector templates apply matte charcoal, ivory sans-serif titles, fine double
coral frames and one lower-right mathematical illustration to all nineteen books.
The main title is bold; secondary type is restrained. The small top illustrations
and their generated files are removed. Mathematical geometry stays exact and each
volume retains its own subject; Volume 0 remains a Gaussian surface. Production
covers use embedded TeX Gyre Heros and vector paths rather than concept PNGs.

Paperback backs/spines use the same palette and font. The 7 × 10 trim, bleed, actual
page-count spine calculation and ISBN/barcode behavior are unchanged. Canonical
PDFs retain their print-safe grayscale semantic accents; front matter now shares
the cover's sans-serif identity while mathematical paragraphs remain Palatino.
EPUB, HTML reader and the library use coordinated deep-coral light accents and warm
coral dark accents. The library adds a persistent light/dark switch shared with the
reader. Headings and the framed hero follow the new typography and cover colors.

## Local verification

- 38 final fronts checked: standard 7 × 10 and 6 × 9.6 EPUB image proportions.
- Every title, subtitle, slogan and author survives extraction. No extracted word
  crosses a page edge. All fonts are embedded vectors and every page size is exact.
- Entire nineteen-cover contact sheet visually inspected; long titles wrap without
  hyphenation or collisions. Generated artwork hashes match the content manifest.
- Full production pipelines succeeded for Volumes 0 and 9, including EPUB and HTML.
- Volume 0: 233 interior pages, rounded to 234 for KDP, 0.527 inch spine.
- Volume 9: 148 interior pages, 0.3333 inch spine.
- Both complete paperback wraps inspected; Volume 0's ISBN barcode is preserved.
- All 26 publishing tests passed, shell/Python syntax and whitespace checks passed.
- Chromium checked light/dark preferences, shared theme persistence, library search
  and filters, chapter mathematics, hints, and mobile navigation at 320/390 px.
  No page errors or page overflow. Primary-control contrast is 5.91:1 in light mode
  and 7.32:1 in dark mode.

Local artifacts are in `build/coral-covers-final/` (contact sheet and vector catalogue)
and `build/coral-ui-review/` (website/reader screenshots, full wraps and browser results).
The final local Volume 0 cover is applied to its EPUB, reader image, eBook JPEG and
actual-page-derived paperback wrap. The nineteen-book clean CI run is authoritative
for the complete release; source publication, successful CI and Pages deployment
are verified separately. No assets are uploaded to Amazon KDP by this repository.

## Verified publication

- Source/design commit: **5936eedb1b130bd86905cec6e828485bb3fc7bc7**.
- [Exact clean workflow run](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/40564431866):
  **all nineteen book jobs succeeded**, complete-library validation succeeded, release
  publication succeeded and the actual Pages deployment step succeeded.
- [Published books release](https://github.com/OussamaSegh/Order-and-Chance/releases/tag/books):
  **114 assets**, targeting the exact design commit.
- [Live Pages library](https://oussamasegh.github.io/Order-and-Chance/): confirmed nineteen
  books, the new theme, exact design commit and updated Volume 0 reader stylesheet.
- Downloaded the clean-run published archive and independently verified all nineteen
  paperback wraps: dimensions, embedded vector fonts, complete front text and
  page-count-derived spine metadata. The full wrap contact sheet was inspected.
  Artifacts and page/spine records: `build/ci-coral-wraps/`.
