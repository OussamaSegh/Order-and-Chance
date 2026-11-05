# KDP interior bleed correction — 5 November 2026

The author supplied KDP's rejection for insufficient interior bleed, citing
Volume 1 PDF page 13, and confirmed uploading `Volume 1 - First Principles - Print.pdf`.
They requested the correction for all fifteen volumes with workflow regression tests.

## Reproduction

The published Volume 1 print PDF retrieved on 5 November had 447 pages, all
504 × 720 pt (7 × 10 in). Its SHA-256 was
`ed664d77f3567245bec0f46064a5da01ba329bb5003fef038036fab7e38c8586`.
PDF pages **13, 55, 129 and 355** were the four edge-to-edge charcoal part dividers.
A rendered boundary scan of all 447 pages identified these four pages. The old
`kdp_pdf.check()` passed that file: its structure checks did not detect missing bleed.
The exact uploaded binary was not supplied; the current published file matches
KDP's cited page and the author's confirmed filename.

## Shared correction

- Every print page is **513 × 738 pt (7.125 × 10.25 in)**, for the same 7 × 10 trim.
  The 9 pt outside extension mirrors by physical PDF page parity. Top/bottom
  extensions are 9 pt each; binding edges have no added bleed.
- `kdp_bleed.py` preserves the body's trim-relative coordinates and extends
  proven opaque full-page rectangular backgrounds with a vector underlay.
  It recognises both native PDF rectangles and the actual four-line TikZ path.
  Other edge-reaching artwork without authored bleed blocks export.
- Reading PDFs still come from the original 7 × 10 typeset source, preserving
  vector type, links, bookmarks, page labels and Unicode maps. Print-only page
  expansion changes neither the typography nor visible pagination.
- The existing PDF 1.3, font, image-resolution and selective 600 ppi transparency
  checks remain. Visual parity checks compare the finished trim; actual divider
  ink is independently checked across the added bleed bands.
- Listings specify **Bleed (PDF only)**. Metadata records the new canvas.
  Print reports use schema 2; library/cache schema 9 forces all fifteen books
  to regenerate and prevents restoring the old no-bleed outputs.

## Verification

The local suite passes **468 tests, with seven skips** for unavailable Kindle PNG
tools. The actual Ghostscript export regression runs and passes. Regressions cover
the page-13 divider, odd/even trim placement, source/vector preservation, wrong
page dimensions (including incorrect binding-edge bleed), white padding around
an unextended divider and unsupported edge artwork. All fifteen generated listings
were checked for the Bleed setting. Workflow YAML, its embedded Python, generated
print-layout synchronisation and shell syntax pass validation.

The real Volume 1 production interior passes with **447 pages** and extended
backgrounds at **13, 55, 129 and 355**. Only the same five transparency pages
(106, 247, 337, 368, 408) are flattened at 600 ppi. The all-page visual comparison
passes with maximum unmatched ink fraction **0.00239**, retaining the existing
thresholds. The local corrected print SHA-256 is
`9228c135af5f63cb5f426f850a438333a2cde9a61fcfa4df36584abd3286b249`.
Typesetting reports 412 whole boxes with no overflow or unresolved references;
the reading-source navigation/body and final interior font/colour checks pass.

The build workflow runs the new bleed regressions with Ghostscript installed,
then validates each produced volume's complete export report, page boxes and
divider bleed before library assembly. The all-volume CI run and its exact source
revision are to be recorded on the correction PR; this note does not claim a
completed CI rollout or a KDP-accepted replacement.

KDP requires the whole interior to have bleed dimensions even when only one page
needs bleed. Its table explicitly specifies 7.125 × 10.25 in for a 7 × 10 book:
[Set Trim Size, Bleed, and Margins](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6).
The replacement must be uploaded with **Bleed (PDF only)** and checked in KDP's
Print Previewer. No KDP account submission or acceptance is claimed here.
