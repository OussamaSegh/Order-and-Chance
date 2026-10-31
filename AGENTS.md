# Order and Chance: current author instructions

The series is fifteen volumes, numbered 1 through 15. There is no Volume 0 and
there is no nineteenth book. Sections below that say “19 books”, “19 volumes”,
“the other eighteen”, or “Volume 0” record an earlier instruction; the
structure in `docs/SERIES-STRUCTURE.md` replaces them. Cross-volume citations
in the books use the title-page numbers. The map is
`docs/plan/volume-citation-map.md`.

Read `docs/DESIGN.md` before changing design or publishing templates.

## Approved cover family — 29 October 2026

The author approved the fifteen Cormorant Garamond / Fira Sans fronts in
`docs/COVER-DESIGN.md`, including the Collatz tree on Volume 1 and the motifs in
`tools/covergen/arts.py`. This supersedes every earlier cover instruction in this
file: the Inter Display master, the exact PNG fronts, the traced Gaussian, the
shared 3D wireframe and `tools/cover_plates.py`. Regenerate with
`tools/series_cover.py`. Backs and spines use the same ground, grain and double
frame. Each book carries the cover credit and the About the Cover colophon from
`common/cover-notes.json`. Do not edit chapter files to change those notes.

## Volume 0 subtitle update — 28 October 2026

The author approved **Proof, Problem Solving and Mathematical Thinking** as
Volume 0's subtitle, including its covers. This supersedes the older
"A Foundations Prelude" wording and freeze below. Canonical metadata remains in
`common/volume-subtitles.json`. Covers wrap long subtitles within the existing shared
5.4-inch subtitle area at the existing font size, tracking and title-relative first baseline;
Volume 0 uses two lines. Earlier approval images remain historical references.

## KDP export rule — approved working files, 28 October 2026

The author confirmed the separately prepared Volume-0 KDP interior and print
cover work, while raw pipeline PDFs did not. Apply the working export process to
**all 15 volumes**. This supersedes the old identical-PDF-body-stream requirement
and the paper-only raster restriction for the final press cover.

- Pull current `main` first; preserve the latest manuscript and cover artwork.
  The author explicitly chose the latest artwork, with the working PDF settings.
- Typeset once. Build the reading PDF from the original `build/<book>/main.pdf`,
  preserving vector text, correct Unicode maps, links, bookmarks and page labels.
  Never build the reading PDF from a Ghostscript-processed print interior.
- `tools/kdp_pdf.py` must create every canonical `dist/kdp/<book>-print.pdf`:
  unencrypted PDF 1.3, no document metadata, links, annotations, bookmarks,
  startup actions, live transparency or ASCIIHex streams. Repair missing ASCIIHex
  terminators and prune unused PGF opacity/XObject resources before conversion.
  Flatten only pages that actually use transparency at **600 ppi**, without
  downsampling; retain vectors elsewhere. Images must be >=300 physical ppi.
- `tools/kdp_cover.py` must create every canonical `*-cover-wrap.pdf`: the working
  cover's opaque PDF 1.5 format, embedded vector lettering, frames and barcode,
  native paper >=300 ppi. Preserve original font programs and Unicode maps; do
  not run covers through Ghostscript font rewriting. Composite only transparent illustration regions at
  **600 ppi**, with lossless pixels and provenance. Never rasterize the whole cover,
  its title, subtitle, back text or spine, and do not redraw the artwork.
- For composited covers, compare vector regions against the original, verify exact
  source-sampled art pixels and placement, and compare the whole final cover with
  the composited reference. Do not compare dense 72 dpi vector meshes to 600 dpi
  composites and then relax thresholds; the sampling methods differ.
- Both print artifacts must pass their structural/provenance checks and visual
  comparison against the original typeset/vector source. Do not bypass a failing
  check, lower resolution, globally flatten every page, or copy raw TeX PDFs to
  the print download. Source/read navigation remains checked independently.
- Keep exactly two standard 7×10 PDFs and one EPUB under the existing filenames.
  No third public PDF edition. Internal raw sources/reports stay in `build/`.
- Derive the wrap from the **current exported print page count**, never the old
  241-page Volume-0 specimen. Keep premium colour / white paper / no interior
  bleed, and 0.125-inch cover bleed. Geometry and count must survive conversion.
- Build dependencies include Ghostscript and pinned PyMuPDF; output/cache schema
  **7** invalidates prior raw PDFs. Cache assembly requires both export reports,
  rechecks final hashes, reading provenance, visual parity and cover geometry.
- Record successful tests and exact CI publication. A parser/visual pass is not
  itself proof of acceptance by KDP; retain the author's actual upload feedback.

See `docs/KDP-EXPORT.md` for the process, commands and future-agent checklist.

## Latest instruction: harmonise Volumes 0 and 1 to the rest

The author explicitly chose to make Volume 0's illustration look like the other
books, then requested Volume 1 be harmonised too. This supersedes preserving the
traced Gaussian in production. Volume 0 keeps its Gaussian subject but now uses
the same native mesh renderer, material, pen weights and restrained halo as all
other volumes. No illustration-renderer exception or reference-art import remains.
Volume 1 keeps its Ulam prime pattern, with lower, broader relief and finely
triangulated faces instead of sparse needles. Only these two motifs change.
Typography, identity, subtitle spacing, all other illustrations, interior work and
premium-colour print geometry are retained. Original approval images and traces
remain archival files. Apply the common manifest/material/composition guards to
Volume 0 as strictly as every other book.

## Latest instruction: individual mathematical art direction

The author now explicitly asks to review every illustration independently, replace
subjects where appropriate, and adjust illustration position and orientation.
This supersedes the earlier assumption that all geometry must keep one pose.
Fonts, title/subtitle rules, identity, palette and luminous vector material remain
shared. `tools/assets/cover-art-direction.json` records the separate rotations,
centres, scale and clearance; the shared renderer still supplies one material and
camera. See `docs/COVER-ART-DIRECTION.md` for all sixteen decisions and chapter
connections. Volume 0 and the approved Volume-2 composition remain references.

Keep the Sierpiński carpet and actual Plancherel Young diagram consistent with
references inside the books. Chance's Galton sculpture differs from Volume 0.
Crossroads uses a roots-of-unity star instead of repeated prime pyramids.
Volume 14 keeps the Steinhaus plate. Incidental obsolete cover references may be
corrected without changing mathematical content. Preserve the concurrent semantic
box-colour/frame correction from `8135b0b` and its tests.

## Latest refinement: glowing artwork and title-relative subtitles

The author approved the luminous Volume-2 preview and then explicitly changed the
subtitle rule: each subtitle belongs directly below its own title. This supersedes
the earlier demand for a fixed y=600 subtitle in every volume. Keep the same fonts,
sizes and left margin. A two-line title retains Volume 0's baseline; a one-line
title moves its subtitle up exactly one title leading. The generated macro and PDF
checker use the same title-relative rule, without per-book offsets or autosizing.

Apply the approved soft coral halo, warm cream cores and fading body wires to all
native 3D illustrations. Volume 0 retains its approved Gaussian reference. The
shared renderer depth-tests and deduplicates wires before exporting five layers of
vector radiance: broad faint halos through sharp warm cores. It must not restore
hidden rear edges or rasterize artwork. Fit complete silhouettes and their halos
inside the common illustration viewport.

Chance now uses a shallow Galton/Pascal lattice feeding exact binomial columns,
replacing its Gaussian-like hill. Volume 14 keeps the Steinhaus plate.
The rest of the cover typography, identity and all interior content stay intact.


## Latest decision: one locked Volume-0 master for all sixteen covers

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

## Current interior: design 5e

The author approved interior mock-up **5e** and asked for it in every volume. It
supersedes the version C description below (kept for history): EB Garamond and
Garamond-Math at 11.5/14.75 pt, Cormorant Garamond headings, Fira Sans labels, a
7 × 10 in page with a 0.9 in gutter and 0.8 in outside margin, a full charcoal part
page on every part recto (coral numeral, ivory title, no illustration) and a compact
chapter opener (charcoal band, coral numeral, title, rule and epigraph) with the prose
continuing on that same page, one coral accent, formal boxes (8% fill,
1.2 pt coral top rule, never split) and teaching boxes (2 pt charcoal left bar,
breakable), the figure palette and slashed inline fractions. Read
`docs/design/interior.md` before changing any of it. Covers are unaffected.

## Approved version C interiors (superseded by 5e)

The author approved **version C** and requested it for all 15 volumes. The selected
proof is `build/typography-review/Volume-0-Cover-Matched-Proof.pdf`: the cover's
exact Inter display faces for headings, STIX Two Text/Math for body/mathematics,
11 pt with 1.065 line spacing, tracked chapter labels, 24/29 pt chapter titles,
small Inter running heads and labels, and thin 1 pt left box rules with pale
fills. The author subsequently requested distinct semantic colours and consistent
framing: blue exercises/problems, coral reminders/challenges, teal beauty notes
and plum thinking prompts. Hide the full frame and draw only the left rule; a
zero-width coloured frame can expose top/bottom seams when rendered. Charcoal
headings and coral chapter/link accents retain version C. Scientific figure
colours retain their meaning. This supersedes the older
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
  and public pages. Existing `volume…` directory/file identifiers and TeX macro names
  remain stable. The author explicitly excluded the already approved covers from
  this terminology change; do not edit their artwork, templates or back-cover text.
- Series subtitle: **The Hidden Architecture of Mathematics**. The series is Order and Chance: The Hidden Architecture of Mathematics.
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
  EB Garamond/Garamond-Math, Cormorant Garamond headings, Fira Sans labels and DejaVu
  Sans Mono for code (design 5e, `docs/design/interior.md`). The shared
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
  pale boxes with thin semantic-colour left rules and no top/bottom/right rules.
  Keep body text/maths dark on white.
  The author's colour-print instruction supersedes the old grayscale overrides.
- Preserve ISBNs, identifiers, editions, author spelling, mathematical text,
  figure meanings, cross-volume references, library search and reader controls.

## Standard book formats

The author approved **7 × 10 inches for all 15 paperbacks** after the Volume 0
comparison. `common/print-layout.json` is canonical; regenerate its TeX with
`python3 tools/print_layout.py`. Rebuild each wrap from its actual new interior
page count. The latest author decision requires two distinct PDFs per volume:
`dist/<volume>.pdf` for downloading/reading, with the approved front cover first;
`dist/kdp/<volume>-print.pdf` for paperback manuscript upload, without that cover.
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
- `./build.sh [volume...]` builds the 7×10 reading PDF with cover, print PDF, EPUB, eBook cover,
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

## Revised series structure (29 October 2026)

The latest structural decision is recorded in `docs/SERIES-STRUCTURE.md`. There
are fifteen volumes, numbered 1 through 15, in six parts, and no problem book.
Volume 1 is **First Principles**. Volume 15 is **Order and Chance**. The old
numbers, and the citations of them inside chapter bodies, are recorded in
`docs/SERIES-STRUCTURE.md`. Do not recreate a problem book, Machinery, Frontiers,
or the computing and companion shelves. Supporting mathematics stays in the
appendices of the owning volumes.

## First-edition copy policy

All volumes are being prepared for their first edition. Reader-facing copy,
including prefaces, reading guides and back matter, must not describe this work
as a revision or reconstruction, compare it with a previous edition or arrangement,
or include old-to-new numbering concordances. Describe the book as it stands.
Keep development history and content-migration records in internal editorial
reports only. This does not prohibit mathematical uses of words such as
reconstruction, historical discussion or citations of editions of other works.

Do not mention or promise accompanying Python/Jupyter notebooks in the books,
including prefaces, chapters, appendices, captions, exercises, hints, solutions,
back covers and KDP descriptions or keywords. Numerical examples must stand on
their own and must not direct readers to unpublished companion files. Historical
handwritten notebooks and personal research journals are distinct mathematical
content and may retain their proper names. This policy applies to all first-edition
formats and future writing sessions.

## Mathematician writer (shared across tools)

Cursor, Claude Code, Codex, and other agents use the **same** role and voice:

- Voice: `docs/WRITING-STYLE.md`
- Role: `docs/agents/mathematician-writer.md`
- Cursor custom mode: `.cursor/skills/mathematician-writer/SKILL.md` (pointer only)
- Claude Code: `CLAUDE.md` and `.claude/agents/mathematician-writer.md` (pointers only)

Do not create tool-specific forks of the writing style or the mathematician-writer rules. Edit the files under `docs/` only.
