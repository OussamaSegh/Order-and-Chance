# Volume 2 — current PR #103 review candidate

**State:** draft, open, unmerged and unpublished. This supersedes the publishing
dimensions and repository acceptance recorded for the earlier PR #97 edition.
It does not approve Amazon upload, a release tag or publication.

**Manuscript and publishing source:**
`b67f700f0e14c62c961d9813a9ca1d48e3290c04`. Subsequent documentation-only
commits require matching publishing-input fingerprints before using these
artifacts. The [strict ledger](volume2-independent-verification-ledger-2026-11-03.md)
and [plan](../plan/volume2-independent-verification-and-rewrite-2026-11-03.md)
define the acceptance gates; this handoff does not close them automatically.

## Evidence for the reviewer

All 72 named results and 144 keyed solutions have two internal mathematical
checks, with separate whole-source records for unnamed arguments, 97 worked
examples and 39 figure datasets. The actual Volume 1 proof-site crosswalk,
conceptual first-use/story ledger, 319 references and 85 classified forward
contexts are recorded. All 62 bibliography paragraphs and 23 historical
groups have source records and explicit access/research-proof limits.
These are internal model checks, not independent human refereeing.

All 333 paired print/reading pages were actually opened and read. Five
corrected full pages were reopened on source `434d620b`; all 333 pairs from
the later EPUB-only fix have matching native 144dpi RGB hashes in both PDFs.
The reading front, full paperback wrap and grayscale wrap were inspected.
All 39 EPUB plates were viewed in narrow, grayscale and fitted wide comparison
panels. Actual generated reader checks cover all 20 pages at 390/1280px.

The latest complete source suite passes **463 tests, zero skips, 52.452s**.
Three before-failing regressions cover natural equation width, proportional
height and the media guard. Actual corrected EPUB passes EPUBCheck with zero errors/warnings and all44 browser checks; all605 displays per width meet aspect bounds. Navigation/cross-format/site checks pass. Current artifact checks and hashes belong in
the machine-readable reports; a successful schema/loading check alone does
not establish mathematical or visual correctness.

## Matched candidate files and dimensions

| Item | Current value |
| --- | --- |
| Title / subtitle | The Integers / Primes, Patterns and Proofs |
| Series / author / edition | Order and Chance, Volume 2 / SEGHAIER Oussama / First edition, 2026 |
| Paperback ISBN | 9798167208650 |
| Reading PDF | `dist/Volume 2 - The Integers.pdf`, 334 pages including front cover |
| Print PDF | `dist/kdp/Volume 2 - The Integers - Print.pdf`, 333 interior pages |
| KDP-counted pages / spine | 334 / 0.7839 inches |
| Paperback wrap | `dist/kdp/Volume 2 - The Integers - Paperback Cover.pdf`, 15.0339 × 10.25 inches including bleed |
| Print settings | 7 × 10 inches, premium colour, white paper, no interior bleed, 0.9-inch inner margin |
| EPUB / eBook cover | `dist/Volume 2 - The Integers.epub` / `dist/kdp/Volume 2 - The Integers - eBook Cover.jpg` |
| Listing / metadata | `dist/kdp/Volume 2 - The Integers - Publishing Listing.md` / `dist/kdp/Volume 2 - The Integers - Print Metadata.json` |
| Reader | `dist/html/volume2-integers/` |

The actual wrap barcode decodes to the stated ISBN on nine raster scanlines
at 300/450/600dpi, including guard/parity/check-digit checks. This does not
verify a physical scan, account ownership or ISBN assignment. Keep the
interior and cover together from this same build. The old 313-page interior
and 0.737-inch cover belong to the previous edition evidence.

## Required external evidence

- An independent mathematical/editorial reader must review the proof-heavy
  chapters and advanced routes, using the keyed proof/exercise/whole-source
  records and actual Volume 1 crosswalk. Record concrete objections and
  their resolution against an exact source revision. Unresolved review
  blocks merge under P13.
- Complete the human read-aloud/first-reader pass required by P10: prose,
  proofs, captions, exercise/solution commentary, preface, field guide and
  back-cover copy. Record actual coverage; model text review is separate.
- Run native Kindle Previewer and inspect the EPUB on the intended
  Paperwhite, including every diagram and formula at narrow/wide settings,
  baseline alignment, long displays and all exercise navigation. Chromium
  checks do not replace the native renderer. Kindle Previewer is unavailable
  in this Linux execution environment.
- The author must verify the correct KDP title/edition/ISBN account record,
  listing fields, rights/disclosures and the matched publishing files;
  complete KDP Print Previewer and inspect a physical paperback proof,
  including gutter, registration, contrast, binding and barcode scan.
  These account and physical acts remain unperformed and are not authorized
  by this handoff.
- After all findings are resolved, record independent review and author
  approval, exact-head successful CI and final artifact identities before
  considering repository acceptance or publication.

Reviewer comments can arrive while repository checks continue. A new content,
style or publishing change reopens affected evidence and requires rebuilt
matched files. Internal counts and hashes never substitute for the missing
external reviews.

**Artifact evidence:** [matched file manifest](volume2-current-artifact-manifest-2026-11-04.json), [final PDF transfer](volume2-final-pdf-comparison-2026-11-04.json), [actual EPUB browser measurements](volume2-epub-browser-review-2026-11-04.json), [EPUB schema evidence](volume2-epub-schema-evidence-2026-11-04.json), [navigation](volume2-digital-navigation-review-2026-11-04.json), [real site assembly](volume2-site-navigation-review-2026-11-04.json), [raster barcode](volume2-barcode-raster-review-2026-11-04.json). Terminal exact-final-documentation-head CI remains pending at this committed checkpoint.
