# Production paperback migration: 7 × 10 inches

This note records the 7×10 migration. The current series is Volumes 0–14 plus
Crossroads. The page-count table below measures the catalog as it stood then,
including titles that are not books now.

All volumes in that catalog use 7 × 10 inch paperback
trim. This implements the author's approval following the local Volume 0 comparison.
The 11 pt Palatino body, mirrored margins, recto chapter openings, first-edition copy
policy, ISBNs and approved black/gold cover illustrations are preserved.

## Implementation

- `common/print-layout.json` is the shared print specification; its generated TeX
  is checked for consistency before builds. Reading A4/Kindle PDF and EPUB formats
  retain their existing dimensions.
- Paperback interiors are 504 × 720 PDF points without bleed. Wraps are
  (14.25 + actual spine) × 10.25 inches, including 0.125 inch outside bleed.
  Front illustrations scale uniformly; back text reflows for the wider page.
- Spines use the actual rebuilt interior, rounded up to an even KDP page count,
  multiplied by 0.002252 inch/page for black ink on white paper. Spines under
  80 pages have no text. Volume 0's existing ISBN barcode retains its physical size.
- `./build.sh --print-only [volume...]` produces paperback interiors, wraps, listings
  and per-book print metadata. Full builds continue to produce all reading formats.
- CI validates the configuration and runs publishing tests. Cache schema 2 and
  `library-v2` force complete regeneration; missing print metadata invalidates caches.
  Download labels, KDP listing trim fields and publishing instructions agree.
- Long inline formulas that overflowed at the new measure were moved into displays
  or given line breaks. Edited manuscripts retain their labels and exercise/hint/
  solution counts. Volume 14's pointer and roadmap promise to an absent
  Davenport–Heilbronn chapter were removed; the theorem attribution is retained.

## Local verification

- All **19 interiors and 19 actual-page-count wraps** passed exact dimensions and
  embedded vector font checks. Every interior page was checked, including front
  matter and inserted figures. All print metadata agrees with the actual PDFs.
- All **95 front proofs** passed dimensions, embedded fonts and complete title,
  subtitle and slogan extraction. No front text extends outside its page.
- Every production wrap's front panel independently passed complete title/subtitle/
  slogan extraction. No extracted text crosses an interior or wrap page boundary.
- No unresolved references or citations remain in the final print logs. The largest
  remaining overfull box is under 4 pt and stays inside the physical safety margins;
  these minor paragraph warnings do not indicate clipped content.
- All **20 publishing tests** passed locally. All nineteen edition-copy guards pass.
  `bash -n build.sh`, Python compilation and `git diff --check` pass.
- A complete Volume 9 build passed: A4, Kindle PDF, EPUB, reader, ebook cover,
  paperback interior, wrap and listing. Its reading PDF sizes remain A4 and
  303.307 × 402.520 pt respectively.
- Visually inspected all front and wrap contact sheets, the ISBN wrap, long-title
  covers, thin problem-book wraps and representative interior pages/formula reflows.

This is a format and typesetting audit, not a new mathematical peer review of every
chapter. Scientific figure colours retain their existing distinctions; the earlier
Volume 0 review's suggested monochrome figure refinements remain separate work.

## Rebuilt production dimensions

Page counts include front matter. The KDP count includes any final blank page;
wrap widths below include both outside bleeds.

| Volume | Title | PDF pages | KDP pages | Spine (in) | Wrap width (in) |
|---|---|---:|---:|---:|---:|
| 0 | Mathematical Maturity | 233 | 234 | 0.5270 | 14.7770 |
| 1 | The Integers | 173 | 174 | 0.3918 | 14.6418 |
| 2 | Structures | 372 | 372 | 0.8377 | 15.0877 |
| 3 | Chance | 249 | 250 | 0.5630 | 14.8130 |
| 4 | The Art of Calculation | 178 | 178 | 0.4009 | 14.6509 |
| 5 | Where It All Meets | 176 | 176 | 0.3964 | 14.6464 |
| 6 | Spaces | 177 | 178 | 0.4009 | 14.6509 |
| 7 | Analysis in Depth | 178 | 178 | 0.4009 | 14.6509 |
| 8 | Shapes | 336 | 336 | 0.7567 | 15.0067 |
| 9 | Higher Structures | 148 | 148 | 0.3333 | 14.5833 |
| 10 | Chance II | 191 | 192 | 0.4324 | 14.6824 |
| 11 | Random Motion | 228 | 228 | 0.5135 | 14.7635 |
| 12 | Arithmetic | 250 | 250 | 0.5630 | 14.8130 |
| 13 | Primes in Depth | 211 | 212 | 0.4774 | 14.7274 |
| 14 | Order and Chance (count below is the earlier manuscript) | 192 | 192 | 0.4324 | 14.6824 |
| — | workshop, then not a separate book | 309 | 310 | 0.6981 | 14.9481 |
| P1 | Crossroads | 442 | 442 | 0.9954 | 15.2454 |
| — | harder problems, then in Volumes 6 and 7 | 72 | 72 | 0.1621 | 14.4121 |
| — | harder problems, then in Volume 10 | 43 | 44 | 0.0991 | 14.3491 |

All wraps are 10.25 inches high. Production PDFs and print metadata are in
`dist/kdp/`. Local visual proofs: `build/7x10-series-fronts.pdf`,
`build/7x10-covers/contact-sheet.jpg`, `build/7x10-wrap-contact-sheet.jpg`,
`build/7x10-interior-samples.jpg`; machine audit: `build/7x10-print-audit.json`.

Source push and GitHub release/Pages publication are verified separately. GitHub
publication does not upload books to the author's Amazon KDP account.
