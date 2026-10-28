# Order and Chance: current author instructions

Read `docs/DESIGN.md` before changing design or publishing templates.

## Latest decision: one locked Volume-0 master for all 19 covers

The author now requires **100% series coherence**, with only the title (including
its own subtitle), volume number and illustration varying. The subtitle must stay
at Volume 0's position. This supersedes the earlier separate concept-image fronts
and the sixteen flat-plate/glow variants below. All production fronts, including
Volumes 0, 1 and 2, use `tools/cover-editorial-front.tex` and one configuration,
`tools/assets/series-template.json`; regenerate its TeX with `tools/series_cover.py`.

- The exact Volume-0 frame, masthead and author form is reused on every front/back.
- Every title uses the same bundled Inter Display Bold 700 face, 54.8 pt, fixed
  leading and width. No title/subtitle autosizing or volume-specific text offsets.
- Subtitles retain their own words, with one italic face/size/tracking. Their fixed
  baseline is source y=632.36, placing capitals at y=600 on the 1500-pixel reference.
  Base anchors prevent glyph-dependent text-box shifts. Titles reserve two lines.
- Volume 0 keeps its traced Gaussian illustration. The other eighteen use one
  world-space 3D mathematical illustration each, with a shared orthographic camera,
  fine coral mesh, opaque surface cells and selective crown bloom. Regenerate using
  `tools/cover_plates.py`; no per-volume drawing-material overrides are permitted.
- Earlier PNG approvals and full-cover traces remain unmodified archival references;
  they must never bypass the shared title/layout in reading PDFs, EPUB or the site.
  Live covers now render from the common master, rather than copying those PNGs.
- `tools/check_cover_template.py` enforces the shared identity, font/size, subtitle
  position and asset manifest, plus matching EPUB/reader images. The cache assembly
  checks reading fronts and print wraps. Font substitutions, missing glyphs and
  overflow fail cover builds; a separately checked back blurb uses fixed type.
- Preserve print preflight (native muted grain >=300 ppi), premium-colour paper,
  actual-page-derived spines, interior fonts, semantic colours and all book content.

## Approved version C interiors

The author approved **version C** and requested it for all 19 volumes. The selected
proof is `build/typography-review/Volume-0-Cover-Matched-Proof.pdf`: the cover's
exact Inter display faces for headings, STIX Two Text/Math for body/mathematics,
11 pt with 1.065 line spacing, tracked chapter labels, 24/29 pt chapter titles,
small Inter running heads and labels, and thin 1 pt coral box rules with pale
fills. Charcoal headings and coral accents replace the earlier multicolour box
roles. Scientific figure colours retain their meaning. This supersedes the older
Libertinus/Inter Text interior policy below. Preserve the cover thread's `c839bba`
artwork/material update. Both PDFs, EPUB and readers follow version C; cache schema
6 forces regeneration. Keep all existing whole-box, font/glyph, PDF-pair and print
cover checks. Do not alter the approved cover artwork or typography.

## Concurrent cover and typography work

Read `docs/WORKSTREAM-COORDINATION.md` before further cover or publishing edits.
The typography work incorporates the cover thread's `788fb50` update unchanged;
its final implementation is `895d25d`. Cover work owns the cover templates,
artwork and `tools/assets/print/`. Interior fonts live separately in `common/fonts/`.
Preserve the premium-colour paper setting, its 0.002347 spine coefficient and
actual print-PDF page counts when updating wraps. Fetch and integrate current
`main` before every push; retain both workstreams' checks in shared build files.

## Latest cover-vibrancy correction

The author found that Volumes 3 onward looked flatter and noisier than the approved
Volumes 0–2. All sixteen remaining covers now use the same restrained 35% charcoal
grain and luminous coral vector material. `tools/cover_finish.py` adds nested
coral/ember strokes and warm highlights without changing any mathematical paths,
coordinates, values or labels. `tools/cover_plates.py` applies this finish on
regeneration. This latest correction updates those sixteen digital fronts as well
as their paperback wraps; the three approved PNG masters and print traces stay
unchanged. Keep the common back/spine/front grain identical across the series.
Print preflight now permits only the native muted paper tile, still >=300 ppi.
Interior colours, fonts, premium-colour paper and page-count-derived spines stay
under the typography workstream's existing rules.

## Latest print-quality authorization

The author subsequently approved **vector paths traced from the approved cover**
for sharp paperback printing. This print-only decision supersedes the older
raster-only wrap rules below and the terminology task's cover freeze. Keep the
approved PNG files and every digital front unchanged. Print fronts and common
back identity use the reviewed source-derived PDF paths in `tools/assets/print/`;
never substitute newly typeset common lettering or enlarged cover bitmaps.
`tools/print_cover_vectors.py` regenerates these assets; its manifest records the
source and output hashes. Contour fitting smooths existing boundaries; it cannot
recover missing original detail. The only print raster is native paper grain,
tiled at approximately 360 ppi. `tools/check_print_cover.py` enforces >=300 physical ppi,
embedded fonts, vector master hashes and a strict paper-only raster whitelist.
Import the PDF masters outside TikZ before placing the cached forms, to avoid
XeTeX's picture-transform import shift. Inspect actual fronts and full wraps.

## Approved series identity (27 October 2026)

The author's latest selection is the **left-aligned charcoal/coral editorial**
cover, `docs/reference/approved-charcoal-coral-volume-0.png`. This supersedes the
previous black/gold identity, centered layouts, serif covers and top supporting
marks. The author explicitly requested implementation across all books, paperback
wraps, content accents, HTML readers and the GitHub Pages library.

- Series: **Order and Chance**. Author: **SEGHAIER Oussama**.
- Use **Volume/Volumes** in English book text, titles, cross-references, metadata
  and public pages. Existing `tome…` directory/file identifiers and TeX macro names
  remain stable. The author explicitly excluded the already approved covers from
  this terminology change; do not edit their artwork, templates or back-cover text.
- Slogan: **Discover the patterns. Understand the proofs.**
- The author rejected the vector recreation and explicitly requested **exactly the
  same image**. `tools/assets/approved-volume-0.png` is an immutable byte-for-byte
  copy of the approved reference; use it unchanged as Volume 0's visible front.
  Do not retype, redraw, recolor, regenerate, stretch or crop that front.
- Volume 1 now uses the separately approved immutable Ulam-inspired image
  `tools/assets/approved-volume-1.png` for every front, including the reading PDF,
  EPUB, HTML/library PNGs and 7 × 10 paperback wrap. Do not redraw or retype it.
  Its reference/hash are `docs/reference/approved-charcoal-coral-volume-1.png` and
  `tools/assets/approved-cover-1.json`; verify with `--number 1`.
- Volume 2 uses the approved fine coral symmetry-wireframe image unchanged:
  `tools/assets/approved-volume-2.png`. Its reference and hash record are
  `docs/reference/approved-charcoal-coral-volume-2.png` and
  `tools/assets/approved-cover-2.json`; verify with `--number 2`. This replaces
  the previous vector plate for all digital fronts and the 7 × 10 print wrap.
- The other sixteen fronts reuse the original frame, header, slogan and author
  directly from the approved image. Only their volume label, title, subtitle and
  content-specific illustration change. Bundled licensed Inter light/semibold/italic
  supplies variable text; the common visible lettering is the original image.
- This explicit exact-image request supersedes previous vector-only restrictions.
  Volumes 0, 1 and 2 have raster visible art/type and a transparent searchable text layer.
  Preserve the original 1049 × 1500 pixels (about 150 ppi at 7 × 10); never claim
  that enlarging this image adds print detail. The remaining sixteen illustrations remain vectors.
- Preserve the approved aspect ratio in EPUB, reader and library thumbnails.
  EPUB fronts use the same 7:10 composition as print, not the old stretched 1:1.6
  version. Each approved volume’s EPUB/reader/library PNG is its original file unchanged.
- Back covers reuse the front’s actual frame, masthead, slogan and author image
  regions. Use the same charcoal fill with restrained grain for approved-image
  wraps. Keep the wider left-aligned Inter blurb, generous leading and reserved
  barcode area; do not reinstate the old untracked heading or thin dim frame.
- Covers, interiors and standalone figures compile with XeLaTeX. Interiors use bundled
  STIX Two Text/Math, the cover’s Inter display headings and DejaVu Sans Mono for code. The shared
  template uses an image XObject to reuse the approved identity without re-encoding
  multiple copies. `tools/check_cover_reference.py` verifies exact master hashes,
  actual embedded PDF pixels, and unchanged EPUB/reader/website PNGs when supplied.
- `tools/cover_plates.py` regenerates sixteen vector plates and records the approved
  masters for Volumes 0, 1 and 2 in the manifest. Do not recreate Volume 0's discarded diagram.
- Canonical explanatory subtitles are `common/volume-subtitles.json`; keep covers,
  PDF title pages, EPUB metadata, KDP listings, readers and library cards in sync.
  Volume 0 keeps **A Foundations Prelude**; changing its visible text requires a
  newly approved master, never a silently retyped replacement.
- Interior/online light themes use neutral paper and accessible deep coral
  #A34232; dark themes use charcoal, ivory and bright coral. Keep semantic boxes
  distinguishable and preserve scientific figure distinctions. Both PDFs use the same version C body: charcoal headings, coral accents and
  pale boxes with thin coral rules. Keep body text/maths dark on white.
  The author's colour-print instruction supersedes the old grayscale overrides.
- Preserve ISBNs, identifiers, editions, author spelling, mathematical text,
  figure meanings, cross-volume references, library search and reader controls.

## Standard book formats

The author approved **7 × 10 inches for all 19 paperbacks** after the Volume 0
comparison. `common/print-layout.json` is canonical; regenerate its TeX with
`python3 tools/print_layout.py`. Rebuild each wrap from its actual new interior
page count. The latest author decision requires two distinct PDFs per volume:
`dist/<tome>.pdf` for downloading/reading, with the approved front cover first;
`dist/kdp/<tome>-print.pdf` for paperback manuscript upload, without that cover.
Both use the final 7 × 10 layout, plus one reflowable EPUB. Typeset the interior
once and attach the front without changing its body, links, bookmarks or printed
page labels. Derive wraps and metadata from the print PDF's page count only.
A4, fixed-page Kindle and phone PDF editions remain retired.
Production paperback setting: **Premium color ink, white paper**, 7 × 10 inches,
no bleed. Its spine coefficient is **0.002347 inch per even-rounded print page**.
Premium colour accommodates the short problem books (24-page minimum); standard
colour has a 72-page minimum. `common/print-layout.json` governs these settings.
Body size remains 11 pt with 1.065 line spacing. Font files, licences and hashes
are in `common/fonts/`; do not substitute machine fonts. `build.sh` supplies extra
XeTeX token memory for dense plots. Missing glyphs, incorrect font families and
lost colour accents fail the build as well as the existing pagination checks.

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
- `python3 tools/cover_plates.py` regenerates sixteen plates and records all three unchanged approved masters.
- `python3 tools/preview_covers.py` checks fronts in standard-book and EPUB proportions. Inspect
  the contact sheet, long titles, full wraps and representative interior pages.
- `./build.sh [tome...]` builds the 7×10 reading PDF with cover, print PDF, EPUB, eBook cover,
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
