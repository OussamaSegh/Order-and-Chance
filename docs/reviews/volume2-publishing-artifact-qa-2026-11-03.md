# Volume 2 publishing-artifact inspection — 3 November 2026

**Scope:** Post-build inspection of the published GitHub Actions ZIP artifact from [run 41556183082](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41556183082), commit `178fe9affc5aad25099a46e101608cb0e24604a3`. Artifact `books-volume2-integers`, GitHub artifact ID **13193869440** (33,179,497-byte compressed download). This is **not** the final or latest revision of PR #97: a subsequent back-cover editorial correction and other fixes require a new build and reinspection.

## Files opened

- Reading PDF: `dist/Volume 2 - The Integers.pdf`, **308 pages**, 7 × 10 inches, including its front-cover page.
- KDP interior: `dist/kdp/Volume 2 - The Integers - Print.pdf`, **307 pages**, 7 × 10 inches.
- KDP full paperback wrap: `dist/kdp/Volume 2 - The Integers - Paperback Cover.pdf`, one 14.9729 × 10.25-inch page.
- EPUB: `dist/Volume 2 - The Integers.epub`, including its EPUB 3 navigation document and compatibility NCX.
- Print layout metadata, the PDF print preflight and the paperback-cover preflight.

## Confirmed checks

1. **ISBN.** The interior copyright page contains **9798167208650**. The back-cover barcode label is `ISBN 979-8167208650`; its visible EAN-13 digits are `9 798167 208650`, agreeing with that ISBN. The mathematical ISBN-13 check digit is **0**, matching the final digit. This verifies source/raster text and the check digit, **not** a physical scanner read.
2. **Cover geometry.** The print metadata declares 7 × 10-inch trim, 0.125-inch bleed, white premium-color paper, 307 interior PDF pages, **308 pages used for the cover/spine calculation**, 0.7229-inch spine, and a 14.9729 × 10.25-inch wrap. The cover page geometry and the arithmetic `308 × 0.002347 = 0.7229` (rounded) agree. Why the uploaded odd-page PDF becomes an even KDP count must be confirmed with KDP Print Previewer.
3. **Automated print export.** The archived print-export preflight reports 307 pages and a 600-PPI flattening target; the cover-export preflight reports embedded fonts, no live transparency, exact artwork placement and a passing source cover preflight. The CI build job also reports success for its print-export tests and PDF/print/EPUB publishing step.
4. **Navigation and sequence.** The PDF contents and sampled part-opening pages show the approved four-part structure and the revised chapter order: arithmetic functions precedes primitive roots, Diophantine equations precede continued fractions, and characters/sieves closes the main text.
5. **EPUB links.** All **121** links in `EPUB/nav.xhtml` were checked against actual EPUB archive members and anchor IDs: **zero** missing files and **zero** missing anchor targets.
6. **Rendered pages.** Inspected the complete cover wrap, a barcode close-up, 17 sampled reading-PDF pages and 10 sampled print-interior pages, including title/front matter, contents, part dividers, chapter openings and back matter. These samples showed no obvious missing art, overprint, clipping or misplaced section headings. Sampled impressions do **not** certify the remaining pages.
7. **Print text sanity.** No literal `??`, `FIXME`, `TODO`, `\\ref{` or `Error!` strings were found in text extracted from the 307-page print PDF.

## Editorial mismatch discovered and fixed after the archived build

The actual printed back-cover copy previously said to study primitive roots and reciprocity **before** counting divisors with Möbius inversion. That contradicted the newly approved printed sequence, which puts arithmetic functions in Chapter 4, ahead of primitive roots (Chapter 5) and reciprocity (Chapter 6). The source `volume2-integers/blurb.tex` was edited to follow the approved sequence and to mention descent, characters and sieves. This means the archived cover still carries the previous blurb and **must not be used as the final cover**.

## Remaining acceptance steps

- Wait for a successful **newest-head** workflow run after the blurb edit; retrieve that run's Volume 2 artifact.
- Inspect the rebuilt full wrap and interior together for matching spine/page count and updated wording, and check additional detailed spreads, mathematical figures, widows/orphans, font embedding and ebook device rendering.
- Complete the independent proof and 144-exercise solution audit; the visual inspection cannot certify mathematical truth.
- Confirm upload-compatible page parity, paper/ink specification, cover/ISBN association and all warnings in KDP Print Previewer; finally inspect a physical proof.

**Status: automated production checks and limited sampled visual review passed on the cited earlier SHA; latest-head publishing approval remains open.**
