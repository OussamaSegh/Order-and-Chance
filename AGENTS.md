# Order and Chance: current author instructions

Read `docs/DESIGN.md` before changing design or publishing templates.

## Approved series identity (27 October 2026)

The author approved the **balanced black-and-gold** Volumes 0/1 proofs, then asked:
“apply the same style for all covers, kdp covers, even content colors themes make
it coherent” and “Generate new illustration for each volume, that reflects its
content and [is] beautiful”. This authorises the all-volume implementation and
build. Earlier restrictions to two-volume validation are superseded.

- Series: **Order and Chance**. Author: **SEGHAIER Oussama**.
- Slogan: **Discover the patterns. Understand the proofs.**
- References: `docs/reference/approved-balanced-volume-0.png` and
  `docs/reference/approved-balanced-volume-1.png`.
- Near-black textured paper, warm gold serif lettering, fine double border,
  one-line masthead, clear central book title, **one substantial lower plate and
  one small supporting construction at the top**. No four-corner collage and no
  tiny isolated motif surrounded by excessive empty space.
- Every volume has its own meaningful vector illustration. The approved Volume 0
  uses a Gaussian surface, Volume 1 a lattice circle and 3–4–5 triangle. Volume 0
  keeps the decorative subtitle **A Foundations Prelude**.
- `tools/cover_plates.py` generates every `cover-motif.tex` and `cover-motif-mark.tex`.
  `tools/cover_motifs.py` supplies mathematical geometry algorithms; its command
  entry point delegates to the approved generator. Commit generator and outputs.
- Each volume has an explanatory subtitle in the spirit of **A Foundations Prelude**.
  Canonical text is `common/volume-subtitles.json`; run `tools/series_metadata.py`
  to sync its TeX lookup. Covers, PDF title pages, EPUB metadata, KDP listings and
  reader/library pages must agree.
- Covers are vector type/diagrams/borders on the generated blank black paper asset.
  No raster cover-art exception remains. Preserve correct mathematics and labels.
- Interior and online themes use charcoal, neutral paper and readable deep gold;
  dark themes use near-black and warm gold. Black-ink print interiors remain gray.
  Preserve scientific figure distinctions rather than recolouring every curve.
- Preserve ISBNs, volume identifiers, editions, author spelling, mathematical text,
  figure meanings, cross-volume references, library search and reader controls.

## Build and publication

- Inspect git status and fetch current main before edits; preserve concurrent work.
- Activate this workspace's toolchain with `source /workspace/order-chance-system/activate.sh`.
- `python3 tools/cover_plates.py` regenerates all 19 pairs of mathematical plates.
- `python3 tools/preview_covers.py` checks all fronts in five proportions. Inspect
  the contact sheet, long titles, full wraps and representative interior pages.
- `./build.sh [tome...]` builds A4/Kindle PDFs, EPUB, reading covers, KDP interior,
  page-count-derived wrap, listing and HTML reader. Phone PDFs are retired and
  notebook execution is manual; preserve both decisions.
- Never invent a page count for a production wrap. Preserve 0.125-inch outside
  bleed and ISBN/barcode handling. Keep all fonts embedded and page bounds exact.
- Shared assets participate in `tools/build_plan.py` fingerprints. Check new shared
  dependencies and never publish incomplete cached-library assemblies.
- Run relevant tests and `git diff --check`; commit the intended design changes.
  Pushing main triggers all-volume Actions builds and release/Pages publication.
  Verify the exact run and report completion accurately. GitHub publication does
  not upload files to Amazon KDP; that requires the author's Amazon account.
- Record implementation, verification and any actual limitations in docs/DESIGN.md.
  Superseded conversations/designs are in docs/DESIGN-HISTORY.md.

## Revised series structure (27 October 2026)

The latest structural decision is recorded in `docs/SERIES-STRUCTURE.md`. There
are sixteen main volumes and three problem books. Do not recreate computing or
companion shelves. Volume 0 is Mathematical Maturity; Volume 9 is Higher Structures.
Supporting mathematics has been integrated as appendices of the main volumes.
