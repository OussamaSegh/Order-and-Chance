# Final mathematical and technical QA

Date: 28 October 2026. Canonical entry:
`tome0-mathematical-maturity/main.tex`. Build command:
`source /workspace/order-chance-system/activate.sh` then
`./build.sh --pdf-only tome0-mathematical-maturity`.
The production build ran locally, with the existing XeLaTeX infrastructure and
bundled approved fonts. Its exact stdout is `/workspace/volume0-checkpoints/J-build.txt`.

| Executed check | Actual result |
|---|---|
| Complete production PDF build | Passed, three interior TeX passes |
| Covered reading PDF | 296 physical pages: front cover + unchanged 295-page interior |
| Print interior | 295 physical pages; 12 roman front-matter pages, final printed page 283 |
| Every interior page size | 504 × 720 pt, 7 × 10 inches |
| KDP even-rounded count | 296; premium colour, white paper, no interior bleed |
| Generated spine/wrap | 0.6947 in spine; 14.9447 × 10.25 in wrap |
| Whole framed boxes | 233; maximum height 337.6 pt; none oversized or split |
| Overfull boxes / display shrink | 0 / 0 |
| Undefined or duplicate references | 0 |
| Missing glyphs / substituted font shapes | 0 |
| Interior/cover font and style checks | Passed: bundled STIX Two + Inter, approved semantic accents |
| Covered PDF body, destinations and labels | Assembly check passed |
| Main chapter bookmarks | All ten present, in correct order |
| Extracted text beyond page edges | 0 across all 295 interior pages |
| Original assets | All 84 original figure/photo-directory files byte-identical |
| New asset | One function/fibre vector figure |
| Embedded interior raster images | 31; minimum effective resolution 300 ppi |
| Print cover preflight | Passed: vector art/type, native grain at 360 ppi, embedded fonts |
| Original explicit labels | All 250 retained; 299 current labels unique |
| Exercises / hints / full solutions | 155 / 155 / 155; all 130 original exercise IDs retained |
| Discovery/write-up split | Present in every numbered solution |
| Original mathematical checker adapted for retained IDs | 1,371 assertions passed |
| Independent finite example checker | 6,088 assertions passed |
| Probability checker | 3,349 exact finite/source checks passed |
| Discrete checker | 86 enumeration/recurrence checks passed |
| Relevant publishing regressions | 17 tests passed |
| First-edition copy guard | Passed |
| Git whitespace check | Passed |

The four computational scripts total 10,894 checks, with overlap in their
examples. This number does not count universal theorems proved or imply formal
verification. The separate original-source audits and skeptical review explain
what arguments were actually read and repaired.

Seven extracted-text-blank interior pages are intentional recto alignment after
contents or at chapter boundaries: physical pages 12, 60, 78, 138, 170, 206 and
260. The sparse final TOC entry was moved onto its preceding page; the remaining
blank page after contents is intentional alignment, not an unfinished section.

Two unicode-math compatibility warnings and 15 underfull-line warnings remain
in the final log. They are recorded rather than suppressed or counted as a
zero-warning build. No overflow, unresolved-reference, missing-glyph or display-
shrink diagnostic remains.

Contact sheets covering the cumulative manuscript were generated. Enlarged pages
were inspected for the new language diagram, map/matrix exposition, rigorous
quadrature solution, final investigation and compact TOC; the final full wrap was
also rendered and inspected. This combines automated whole-book checks with
visual sampling. It is not a line-by-line final visual proofread of every page or
a physical printer's proof.

The final back-description wording was corrected to allow a chapter to open with
a mathematical question as well as history, then the wrap and listing were
rebuilt and preflighted again. That copy-only operation does not change the
interior or reading-PDF body. The new EPUB/HTML reader was not generated or checked;
earlier-format validation recorded in historical review files is not claimed here.

See `final-pdf-measurements.json`, `preservation-check.json`,
`structure-results.json`, `probability-check-results.json`,
`independent-example-results.json`, and `../TOME0-FACT-CHECK-RESULTS.json` for
machine-readable evidence. No remote release or KDP upload is represented by a
successful local build.

## Subsequent digital validation

The user subsequently requested EPUB/HTML validation and a push. This follow-up
is complete locally; DIGITAL-VALIDATION.md records EPUBCheck, all references
against the PDF, resource checks and actual browser rendering. Earlier statements
above that these formats had not been validated describe Batch J at its original
checkpoint, not the current delivery.
