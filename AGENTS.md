# Order and Chance: current author instructions

Read `docs/DESIGN.md` before changing design or publishing templates.

## Approved series identity (27 October 2026)

The author's latest selection is the **left-aligned charcoal/coral editorial**
cover, `docs/reference/approved-charcoal-coral-volume-0.png`. This supersedes the
previous black/gold identity, centered layouts, serif covers and top supporting
marks. The author explicitly requested implementation across all books, paperback
wraps, content accents, HTML readers and the GitHub Pages library.

- Series: **Order and Chance**. Author: **SEGHAIER Oussama**.
- Slogan: **Discover the patterns. Understand the proofs.**
- Matte charcoal #191919, coral #F28B79, ivory #F5F1E9. Clean sans-serif cover
  typography, left-aligned series/slogan/volume/title/subtitle/author, bold book
  title, fine double rectangular coral border without corner ornaments.
- Exactly one substantial content-specific mathematical illustration in the lower
  right; no supporting mark at the top. Preserve each volume's mathematical subject.
- Vector type, diagrams, borders and background in production. The approved image
  is a visual reference, never a raster production cover. Use TeX Gyre Heros for
  cover lettering and retain readable Palatino mathematics in the body.
- `tools/cover_plates.py` generates the 19 `cover-motif.tex` files and the manifest;
  `tools/cover_motifs.py` supplies geometry. Commit the generator and its outputs.
- Canonical explanatory subtitles are `common/volume-subtitles.json`; keep covers,
  PDF title pages, EPUB metadata, KDP listings, readers and library cards in sync.
  Volume 0 keeps **A Foundations Prelude**.
- Interior/online light themes use neutral paper and accessible deep coral
  #A34232; dark themes use charcoal, ivory and bright coral. Keep semantic boxes
  distinguishable and preserve scientific figure distinctions. The sole standard
  PDF is also the paperback manuscript: keep its black-ink grayscale overrides.
- Preserve ISBNs, identifiers, editions, author spelling, mathematical text,
  figure meanings, cross-volume references, library search and reader controls.

## Standard book formats

The author approved **7 × 10 inches for all 19 paperbacks** after the Volume 0
comparison. `common/print-layout.json` is canonical; regenerate its TeX with
`python3 tools/print_layout.py`. Rebuild each wrap from its actual new interior
page count. Each volume has exactly one canonical `dist/<tome>.pdf`, using this
7 × 10 layout for both reading and paperback manuscript upload, plus one EPUB.
A4, Kindle PDF, phone PDF and duplicate `-print.pdf` editions are retired.
Covers, listings and print metadata remain separate publishing assets. Historical
comparison records do not override this decision.

Adapt source to this final page size. Framed exercises, problems, reminders,
beauty notes, pause-and-think prompts and challenges must stay on one page.
Reorganise any box taller than the text area into logically complete units;
do not reduce the body type to fit. Reflow long inline mathematics as displays.
The shared preamble records box heights and rejects split/oversized frames;
`tools/check_book_layout.py` rejects overflow and unresolved references after the
final TeX pass. Keep exercise labels and hyperlink anchors inside the moved box.

## Build and publication

- Inspect git status and fetch current main before edits; preserve concurrent work.
- Activate this workspace's toolchain with `source /workspace/order-chance-system/activate.sh`.
- `python3 tools/cover_plates.py` regenerates all 19 main mathematical plates.
- `python3 tools/preview_covers.py` checks fronts in standard-book and EPUB proportions. Inspect
  the contact sheet, long titles, full wraps and representative interior pages.
- `./build.sh [tome...]` builds the standard 7×10 PDF, EPUB, eBook cover,
  page-count-derived paperback wrap, listing, metadata and HTML reader. Phone PDFs are retired and
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

## First-edition copy policy

Do not mention or promise accompanying Python/Jupyter notebooks in the books,
including prefaces, chapters, appendices, captions, exercises, hints, solutions,
back covers and KDP descriptions or keywords. Numerical examples must stand on
their own and must not direct readers to unpublished companion files. Historical
handwritten notebooks and personal research journals are distinct mathematical
content and may retain their proper names. This policy applies to all first-edition
formats and future writing sessions.
