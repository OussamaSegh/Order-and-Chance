# Series design and session record

## Approved Cormorant cover family — 29 October 2026

The fifteen fronts drawn by the TikZ generator in `tools/covergen/` were
approved and became the production covers. The series name is Cormorant
Garamond SemiBold in spaced capitals; the volume title is Cormorant Garamond
Regular at 42 pt; small lines are Fira Sans Light; the ground is charcoal with
35% grain and the original double coral frame. Volume 1 carries the Collatz
tree. The other motifs are those in `tools/covergen/arts.py`. Backs use the
same family and each volume’s existing blurb, kept clear of the barcode. Spines
share fixed positions for the series name, volume number, title and author.
Each book has a one-line cover credit on the copyright page and an About the
Cover colophon, both taken from `common/cover-notes.json`. The earlier
black/gold, Inter, exact-PNG and 3D-wireframe sessions below are history.



The slogan **Discover the patterns. Understand the proofs.** was retired on 2026-10-29 in favour of the series subtitle **The Hidden Architecture of Mathematics**. The sentences below that still name the slogan record earlier sessions.

## Latest refinement: a compromise between dense and minimal

After finding the dense edge illustrations too busy, the author also rejected the
single-tiny-motif version as over-simplified. The latest direction is a middle
ground: one substantial, coherent lower mathematical plate plus a small subtle
upper construction, with readable central typography, black paper, warm gold,
a fine border and controlled detail.

Volume 0 pairs a small Fibonacci construction with one lower wireframe surface.
Volume 1 pairs the supporting Fibonacci construction with a single lower circle,
integer lattice and 3-4-5 triangle, tied to sums of two squares in Chapter 7. These
are aesthetic design proofs; final mathematical details must be drawn and checked
as vectors before production. The new artifacts and matching KDP design wraps
live in `build/balanced-black-gold-validation/`. Dense and tiny-motif versions are
archived and are not selected. Final design validation remains pending.

## Latest refinement: simplified black and gold

The author found the black/gold edge illustrations too numerous and requested a
simpler, more beautiful composition. The current proof direction supersedes the
dense collage: a single small fine gold motif per front, a very fine border,
large serif title, generous uninterrupted black space and restrained decoration.
Volume 0 uses an inscribed triangle/circle, Volume 1 an outward-square construction
on a right triangle. Titles, slogan and author spelling are preserved. Volume 0
keeps the reference's italic subtitle **A Foundations Prelude**.

The latest pair and matching KDP design wraps live under
`build/minimal-black-gold-validation/`. Earlier illustration-rich variants remain
archived. These are visual proofs pending author validation; no all-volume rollout
or publication has occurred. Generated motif details still require final vector
redrawing and verification before production.

## Latest visual direction: black and gold

The author supplied a new black-background Volume 0 reference after viewing the
three Volume 1 illustration proposals. It supersedes the navy reference as the
current direction: black textured field, warm gold foil type, thin double border,
mathematical plates near the edges, a one-line series masthead across the upper
middle, large book title, and generous dark space around typography.

The reference's Volume 0 subtitle is **A Foundations Prelude**. The established
series slogan remains **Discover the patterns. Understand the proofs.** Volume 1
uses its title **The Integers** with number-theory-themed edge illustrations.
Image generation recreates this aesthetic for a pair of visual proofs; these are
for design validation. Generated mathematical details require vector redrawing
and verification before production. The production mathematics must remain exact.

Artifacts and proof packaging source: `build/black-gold-validation/`. KDP design
wraps use the prior, unchanged print-interior pagination (294 KDP pages for Volume
0, 214 for Volume 1), 6x9 trim and 0.125-inch outside bleed. Existing ISBN and blurb
text are preserved. No publication or all-volume rendering is authorised for this
validation round. The shared navy templates below have not yet been replaced by a
final black/gold production implementation.

The preceding navy/gold proofs and illustration candidates remain archived. They
are not the current aesthetic direction. The records below are historical.

## Current validation round: navy and gold

The latest author request supersedes the earlier rust design and slogan. The exact
slogan is **Discover the patterns. Understand the proofs.** The current authority is
[reference/navy-gold-cover.jpg](reference/navy-gold-cover.jpg), supplied with that request.
Only **Volume 0: Back in Shape** and **Volume 1: The Integers** are being rendered for
validation, including front covers and KDP paperback wraps. Nothing is published.

- Volume 0 embeds the original JPEG unchanged so the reference artwork, lettering,
  borders and composition remain exact. At its native ratio it is a direct reproduction.
  Other page ratios contain the entire artwork, centred on navy paper without cropping
  or stretching. A 6-inch-wide print uses the source at approximately 151 ppi; obtain
  a higher-resolution original before calling this a final press-quality master.
- Volume 1 recreates the reference layout with vector TeX Gyre Termes small capitals,
  gold lettering, a single-line italic slogan, gold rules and corner ornaments. Its
  computed Sacks prime spiral is unchanged and remains mathematically meaningful.
- `tools/assets/navy-paper.png` is a blank texture extracted/recreated from the latest
  reference with the image generation tool; no generated lettering or mathematics.
- Cover-only aliases in `tools/cover-colors.tex` provide navy and gold. Interior and
  website palettes remain unchanged in this cover-only validation round.
- Shared slogan text is updated in title/front matter, listing and web templates,
  preparing later builds for consistency. No other volume outputs were rebuilt.
- Wraps retain 6 x 9-inch trim, 0.125-inch outer bleed, existing blurbs and ISBN handling.
  Spine widths come from freshly compiled print interiors, not sample page counts.
- `tools/preview_covers.py volume0-back-in-shape volume1-integers --out build/validation-covers`
  renders only these volumes in native-reference, ebook, A4, Kindle and print-front
  proportions. Volume 0's raster lettering is inspected visually; Volume 1 is also
  checked through PDF text extraction. Historical all-vector claims below do not
  describe Volume 0's latest exact-artwork exception.

The remaining sections are the historical record of the prior design and build.
They do not override this request. All-volume validation/publication is deferred.

## Archived earlier identity (superseded)

On 27 October 2026 the author selected the slogan **Beautiful mathematics through
problems and proofs.** and requested its application everywhere. That replacement
was committed as `6725bb52012ab1746596cbe635a8c9fc1e063860` across all 28 book title
pages, shared front matter, covers, website/reader templates, KDP listing generator,
publishing handoff and README.

The author initially selected **D — Engraved**, then explicitly changed the reference
on the same day to the attached cover now stored at
[reference/approved-cover.jpg](reference/approved-cover.jpg). **This was the authority for the earlier rust design and is now superseded by the navy/gold reference above.** The author also requires
every illustration to be meaningful to its book's contents. The volume-by-volume
mapping is in [COVER-MOTIFS.md](COVER-MOTIFS.md).

Series name: **Order and Chance**. Author spelling: **SEGHAIER Oussama**.
The earlier prohibition on navy/gold is superseded by the latest author request.

## Archived rust cover system

- Rich burnt-orange/rust paper texture, matching the attached reference.
- Large two-line cream serif masthead, ORDER / AND CHANCE.
- Cream two-line slogan, VOLUME and its existing identifier, fine rules and diamonds.
- Fine cream double border and corner ornaments, based on the reference.
- Each volume has its own mathematically meaningful illustration, rendered as crisp
  vector linework, cream with dark-ink contrasts where helpful. Do not repeat the
  reference's ornamental circles as mathematical content for unrelated volumes.
- Large dark serif book title. Short titles use 60-point type; long titles use
  readable 36-point type on multiple lines with word hyphenation disabled.
- Cream author line and rule; matching paper, rules and typography on paperback
  backs and spines. Internal Volume identifiers and bibliographic titles stay unchanged.
- Fonts are TeX Gyre Pagella; type, diagrams, border and ornaments are vector.
  Only the paper texture is raster.

`tools/cover-front.tex` is shared by all fronts; `tools/cover.tex` supplies the canvas;
`tools/cover-wrap.tex` adds the paperback back, spine and bleed.
`tools/cover-colors.tex` loads fonts, texture and palette aliases. Motifs use `accent`
for cream linework; `ocInk` provides contrasting lines, and legacy `navy` supplies
background knockouts. Generator changes and generated motifs must be committed together.

### Reference and asset provenance

- `docs/reference/approved-cover.jpg`: the author's attached design, preserved as a
  visual reference, not used as a finished cover for unrelated books.
- `tools/assets/burnt-orange-paper.jpg`: a blank paper texture recreated from the
  attachment using image generation; text, diagrams and borders were removed by
  the image tool. Converted to JPEG for efficient TeX/PDF embedding. The original
  generated PNG is preserved in the session workspace. No generated mathematical
  illustration or generated lettering is used in the production covers.
- Mathematical illustrations come from deterministic algorithms in
  `tools/cover_motifs.py`, with their meaning documented in `docs/COVER-MOTIFS.md`.

## Palette and interiors

Canonical TeX values live in `common/design-colors.tex`:

| Token | Hex | Use |
|---|---|---|
| ocTerracotta | A63D16 | Cover field |
| ocInk | 17110F | Cover masthead, title, mathematical drawing |
| ocCream | F9E9B5 | Cover slogan, volume, author, fine details |
| ocRust / ocReminder | 8A3F2B | Screen links, reminders, solution labels |
| ocSepia / ocExercise | 785B3B | Exercise frames |
| ocOlive / ocBeauty | 55634C | Beauty boxes, restrained natural contrast |
| ocUmber / ocThink | 755344 | Think boxes and hint labels |

PDF screen pages retain dark body text on white with very pale tinted boxes. Printed
interior box/label colours are explicitly grayscale. Links are hidden in print.
Scientific diagrams retain any existing colours needed to distinguish mathematical
objects; avoid blindly mapping all blues/reds/greens to a single colour.

`common/preamble.tex` applies the palette to every volume. The three problem books'
`pbook.tex` overrides and Volume 0's challenge box also use these semantic tokens.
`tools/epub.css` and `tools/reader.css` mirror the warm box colours; EPUB leaves page
and body colours to the reading device. `tools/site-template.html` supplies the download page palette. The web reader and download page have
coordinated warm light and dark themes. Their hex values are maintained alongside
TeX values; update both if the approved palette changes.

## Production and validation

In the managed workspace, the installed toolchain is activated with:

```sh
source /workspace/order-chance-system/activate.sh
```

This path is environment-specific. Elsewhere install the dependencies documented in
README and `tools/PUBLISHING.md`. To build one volume, then all volumes:

```sh
./build.sh volumeC5-learning
./build.sh
python3 tools/site.py dist build/site
# Fast all-volume cover preview and text verification:
python3 tools/preview_covers.py
```

`build.sh` regenerates each cover in ebook, A4 and Kindle page proportions;
PNG/JPEG ebook images; the paperback interior and wrap; EPUB; KDP listing; and HTML
reader. Wrap spine width must use the newly built paperback's page count. Preserve
ISBN/barcode handling and KDP's 0.125-inch outside bleed. Never publish a preview
wrap with an invented page count as a production wrap.

Before publishing a design change:

1. Compile the fronts for every volume in ebook, A4 and Kindle proportions.
2. Inspect a contact sheet and the longest titles; check for text overlap and clipping.
3. Compile representative paperback wraps, including long titles and an ISBN barcode.
4. Build at least one complete book through PDF, EPUB, KDP and HTML pipelines; inspect
   colour and grayscale interior pages and the full wrap at readable resolution.
5. Check the generated website and reader themes and EPUB stylesheet. Retain dark-mode
   contrast, distinct box labels, and existing diagram meanings.
6. Inspect git diff and whitespace; commit the intended files to current `main`.
7. Verify the Actions run. Report queued/running/failed/successful publication accurately;
   source commits alone do not replace live release assets or Amazon account uploads.

## Implementation session: 27 October 2026

Concurrent commits `8c32680` and `589cc01` retired phone PDFs, made notebook execution
manual, and redesigned the library with search and filters. Those changes are
preserved. The new library template receives the warm palette without losing its
features. The leftover retired Phone PDF link was also removed from the shared
reader sidebar. A4 and Kindle PDFs plus EPUB are the current production reading formats.

The attached-reference implementation changes shared templates and styles, the three problem-book
styles and Volume 0's challenge palette. It adds this design record and root
`AGENTS.md` so future sessions discover the decision immediately.

The reusable `tools/preview_covers.py` renders every front in ebook, A4 and Kindle
proportions and checks that complete book titles and the slogan survive PDF text
extraction. It writes preview files under `build/cover-previews/` and does not
publish assets. Long-title measurement happens before entering the TikZ picture;
measuring inside it yields null-font widths and can silently clip long titles.
Disable hyphenation with the node's `execute at begin node` hook.

Validation results and publication handoff are recorded below after rendering.

### Completed validation

- All **28 volumes × 3 production front-cover proportions = 84 PDFs** compiled,
  with complete title and slogan text verified by `tools/preview_covers.py`.
- All **28 paperback wrap layout previews** compiled at a clearly hypothetical
  320-page spine; Volume 0's barcode placement was included. These previews stay in
  `build/design-d/` and are not production release files.
- Text bounding boxes were checked across all 84 fronts and 28 wraps; none crosses
  the page boundary. Long-title and representative motif layouts were visually reviewed.
- A complete **C5 build** succeeded: A4 and Kindle PDFs, 62-page paperback interior,
  wrap with its actual page-count-derived spine, PNG/JPEG covers, EPUB and HTML reader.
- Problem-book grayscale box fills verified; screen interior colours visually reviewed.
- Rebuilt EPUB ZIP integrity and warm stylesheet verified.
- **Fourteen tests passed**, covering EPUB conversion, library generation and
  build-cache planning, including shared paper-texture invalidation.
- Chromium checks passed for library search, reader titles and warm light/dark themes;
  representative screenshots reviewed. Search/filter library features are preserved.
- `git diff --check` passed.

Local preview artifacts: `build/reference-covers/series-preview.png` (six examples)
and `build/reference-covers/all-28-covers.pdf` (seven-page catalogue). They are
reproducible build artifacts, excluded from git. The design reference, texture,
mathematical source and session instructions are committed, so future sessions do
not depend on the original attachment path.

### Publication handoff

Publishing this change to `main` triggers the existing all-volume build and release/
Pages publication workflow. A queued or running Actions job means the updated
sources are available while live downloads may still show the last successful build.
Concurrent commit `23b8999` introduced per-book build fingerprints and complete-library
cache assembly. That implementation is preserved. Shared `tools/assets/` files now
participate in fingerprints, with the shared-input regression case extended to a
JPEG, so texture-only changes invalidate all book outputs.
The authoritative run is the Actions run for the design commit. No Amazon account
upload is performed by this repository's pipeline.

## Latest navy/gold validation results (local, unpublished)

- Only Volumes 0 and 1 rendered: **10 front PDFs** across native-reference, ebook,
  A4, Kindle and print-front proportions, plus **2 paperback wraps**.
- Both new print interiors were compiled three times for stable pagination.
  Volume 0: 293 interior pages, 294 for KDP spine calculation, **0.6621 in** spine;
  Volume 1: 214 pages, **0.4819 in** spine. Wrap sizes are respectively
  **12.9121 x 9.25 in** and **12.7319 x 9.25 in**.
- Front and wrap page sizes verified numerically. A pre-existing standalone TeX
  whitespace contribution added roughly 2.49 points to page width; selecting the
  `tikz` standalone mode fixes the exported canvas to the actual TikZ bounds.
- Full new slogan verified through text extraction on Volume 1 fronts and both
  backs; Volume 0's embedded source is byte-for-byte identical to the attachment.
- Both front designs and wraps reviewed visually. Text bounds remain inside the
  PDF pages; vector fonts are embedded Type 1. Volume 0 retains ISBN 9798165526770;
  Volume 1 has no assigned ISBN and leaves space for KDP's barcode.
- Two 1600 x 2560 ebook JPEGs, front PNGs, wrap PNGs, a three-page review PDF and a
  ZIP package are in `build/validation-covers/`. Exact dimensions and pagination are
  in its `manifest.json`; print-resolution limitations are in `READ-ME.txt`.
- `git diff --check` passed. No push, release build, website publication or KDP
  upload was performed. Other volumes remain unrendered under the new template.

## Volume 1 illustration proposals after author feedback

The author rejected the Sacks prime spiral and requested a more meaningful, vibrant
illustration. Three alternatives were prepared using the same cover layout, with
teal and copper accents alongside gold:

- A: sums of squares, Chapter 7. An exact 3-4-5 triangle with outward squares of
  areas 9, 16 and 25, subdivided into their correct unit grids.
- B: Gaussian factorisation, Chapter 10. Conjugate vectors 2+i and 2-i, their
  area-5 squares, and the real product (2+i)(2-i)=5.
- C: modular arithmetic, Chapter 3. Multiplication by 3 modulo 7, with the exact
  six-cycle 1,3,2,6,4,5 and a fixed node 0.

An image-generated concept sheet explores richer illumination and texture; the
separate vector cover proposals use checked geometry and arithmetic and are the
reference for mathematical details. The generated sheet is an aesthetic concept,
not production mathematical artwork. Geometry/area, conjugate product and modular
cycle were checked, and complete cover titles/slogans survive PDF text extraction.

Artifacts and source fragments: `build/integer-illustration-proposals/`. The
comparison PDF, concept PNG and vector/source ZIP are copied to the workspace
Library files. No proposal is selected or applied to production templates yet.

### Black/gold design proof completion

Both revised fronts were generated and visually reviewed. The three-page review
PDF contains the pair of fronts and the two matching paperback design wraps.
Wrap dimensions were checked numerically: 12.9121 x 9.25 inches (Volume 0),
12.7319 x 9.25 inches (Volume 1). Volume 0's barcode is preserved. The PDF and ZIP
are copied to `/workspace/library-files/` with `Black-and-Gold-Volumes-0-and-1`
filenames. These are aesthetic proofs; the mathematical details in the generated
front art have not been certified as final production diagrams. `git diff --check`
passed. Production source design and live books have not been rolled out.

### Balanced proof completion

The revised pair was generated and reviewed, with a substantial lower illustration
and a small upper supporting construction on each front. Both KDP design wraps
were regenerated and their page dimensions verified against the existing interior
pagination. The three-page review PDF and ZIP are copied to the Library under
`Balanced-Black-and-Gold-Volumes-0-and-1` filenames. These remain visual proofs for
author validation; nothing was published. `git diff --check` passed.


# Black-and-gold implementation record, superseded 27 October 2026

The author selected the left-aligned charcoal/coral cover after this record.
The current guide is DESIGN.md. The following is preserved as historical evidence.

# Approved black-and-gold series design

The author approved the balanced black-and-gold Volumes 0/1 proofs and requested
application to **all 19 volumes**, their KDP covers, interiors and online themes.
This supersedes every prior two-volume-only restriction and earlier rust, navy,
dense-edge and tiny-motif design. See [DESIGN-HISTORY.md](DESIGN-HISTORY.md) for the
archived sequence of proposals; it does not override this document.

## Current book formats (27 October 2026)

The author now requires **one standard 7 × 10 inch PDF and one EPUB per volume**.
`dist/<volume>.pdf` is the canonical PDF for reading and paperback manuscript upload.
A4, Kindle PDF, phone PDF and duplicate `-print.pdf` downloads are retired. Separate
paperback wraps, eBook covers, listings and print metadata remain production assets.
The PDF starts with its half-title; the EPUB has its own front cover. Earlier
validation and comparison records below describe their formats at the time and
are superseded by this decision.

## Visual identity

- Series **Order and Chance**, author **SEGHAIER Oussama**.
- Slogan **Discover the patterns. Understand the proofs.**
- Approved visual references: [Volume 0](reference/approved-balanced-volume-0.png)
  and [Volume 1](reference/approved-balanced-volume-1.png).
- Black subtly textured paper; warm gold serif typography; fine double border;
  a single-line masthead and large central book title. One substantial, coherent
  lower illustration and one small supporting construction above the masthead.
- Short titles are large; long titles wrap cleanly and fit the title region without
  hyphenation. No plate, border or text is stretched to a different aspect ratio.
- Every title, mathematical plate and border is a vector. The background alone is
  raster: `tools/assets/black-paper.png`, recreated as a blank texture from the
  approved reference using image generation. Original generated image is retained
  in the session workspace. Approved concept PNGs are references, not print masters.
- All 19 fresh main/secondary illustrations are generated from mathematical data
  and deterministic algorithms by `tools/cover_plates.py`. Underlying constructions
  are in `tools/cover_motifs.py`; the old command delegates to the new generator.
  Parameters, seeds and sampling density are fixed for reproducible output.
- Volume 0: exact sampled graph z=exp(-(x²+y²)); a Fibonacci construction above.
  Volume 1: exact integer circle a²+b²=25 and 3–4–5 triangle; Fibonacci mark above.
  Other plates follow their own manuscripts; see [COVER-MOTIFS.md](COVER-MOTIFS.md)
  and [the machine-readable manifest](cover-art-manifest.json).

## Explanatory subtitles

After approving the style the author requested an explanatory subtitle for every
volume, following **A Foundations Prelude**. All 19 unique subtitles are stored in
`common/volume-subtitles.json`; `tools/series_metadata.py` generates the TeX lookup
and supplies Python consumers. Subtitles appear below book titles on all front
cover formats, on PDF title pages, in EPUB subtitle metadata, KDP listing subtitle
fields, web reader title pages and library cards. The series slogan remains a
separate, unchanged series line. Bibliographic book titles and volume IDs remain
unchanged. Every cover preview verifies both the title and its full subtitle.

## Coherent colour system

`common/design-colors.tex` is the source of TeX colours. Cover gold is #EFC779 on
#080808; cover secondary text is #F5DDA9. Readable deep gold #806023, charcoal
#191815 and neutral paper tones coordinate the interior boxes, labels and links.
Semantic box types keep distinguishable gold/stone/olive-gray shades. Printed
interiors override these with grayscale and hidden link colours for black ink.
Existing scientific diagrams retain the colours needed to distinguish objects.

`tools/reader.css`, `tools/epub.css` and `tools/site-template.html` mirror the palette.
Light reading pages retain dark text on light paper; dark reader/library themes
use near-black with warm gold accents. EPUB body colours remain device-controlled.
The library's black/gold hero, search, collection filters and file links are kept;
reader navigation, theme switching and mathematical overflow handling are kept.

## Source and build

Shared front: `tools/cover-front.tex`; canvas: `tools/cover.tex`; paperback wrap:
`tools/cover-wrap.tex`; font/texture setup: `tools/cover-colors.tex`. Fonts are TeX
Gyre Termes on covers and Palatino in the mathematical text. Volume identifiers,
book titles, author, ISBNs, edition metadata and mathematical content are preserved.

```
source /workspace/order-chance-system/activate.sh
python3 tools/cover_plates.py
python3 tools/preview_covers.py --out build/gold-covers
./build.sh
python3 tools/site.py dist build/site
python3 -m unittest discover -s tools -p 'test_*.py'
```

`build.sh` creates the standard 7 × 10 PDF, EPUB, eBook covers, paperback wraps,
listings, print metadata and HTML readers. Wraps use 7x10 trim, 0.125-inch outside bleed and
white-paper spine width = even-rounded interior pages × 0.002252 inches. ISBN
barcodes remain intact; books without an ISBN reserve the lower-right back area
for KDP. No hypothetical page counts are valid production inputs.

The front preview checks two proportions (7×10 book front and EPUB front); PDF text extraction verifies every title and the slogan,
including Volume 0. Production PDFs preserve vectors instead of embedding the
low-resolution concept PNGs. Book fingerprints include all shared assets and the
new generators; generated per-volume TeX files are tracked with their generator.

## Validation and rollout record

Implementation and validation results are recorded here as checks complete.
GitHub source publication, successful Actions/release publication and Amazon KDP
account uploads are distinct. This repository does not upload to Amazon accounts.

### Completed source and representative-output checks

- Generated and visually reviewed all **28 main illustrations and 28 supporting
  marks**; the seven-page catalogue is `build/gold-covers/catalogue.pdf`.
- **140 front PDFs** compiled across five output types; complete titles, unique
  explanatory subtitles and the series slogan survive text extraction. Numeric
  page-size and text-boundary checks passed, allowing zero-width math overlays.
- Actual-interior-based KDP dimensions and embedded vector font types were checked
  on five wraps, including Volume 0's existing ISBN barcode and long computing
  titles. Volume 0 uses 294 KDP pages and a 0.6621-inch white-paper spine.
- Full representative book pipelines produced reading PDFs, paperback interiors,
  wraps, EPUB, KDP listings and HTML readers. Light/dark library themes, subtitle
  search, collection filters, reader subtitles and mobile navigation passed real
  Chromium checks. Interior reading/print pages and full wraps were inspected.
- All **14 tests passed**, including an extended EPUB regression ensuring subtitles
  are encoded as EPUB 3 subtitle titles without replacing the main title and that
  repeated repair is idempotent. Pandoc otherwise omits the subtitle from OPF.
- `bash -n build.sh`, Python compilation and `git diff --check` passed.
- The Companion's generated index/citation snapshot was refreshed from the existing
  manuscripts as its normal build requires; its citation-map plate was regenerated
  from that refreshed dataset. No authored mathematical chapters were rewritten.

Production completion is determined by a clean all-volume build from the published
commit, not by partially refreshed local outputs. All-volume build and deployment
results are recorded below once available. Earlier in-progress local builds were
restarted for subtitle integration; clean CI is the authoritative final validation.

## Subsequent structural revision

The author subsequently removed the computing and companion shelves and renamed
Volumes 0 and 9. The current nineteen-book catalog and integrated mathematical
appendices are documented in [SERIES-STRUCTURE.md](SERIES-STRUCTURE.md). Earlier
all-volume validation counts above describe the library before this revision.
The approved black-and-gold visual system is preserved.

### Final font correction and clean-build guard

The first clean all-volume run succeeded at `e0839a5`, with all 28 builds and
release/Pages deployment successful. Subsequent checks of all cover fonts found
that Geometry's small sans-serif curvature labels used a Type 3 fallback. Covers
now explicitly select vector TeX Gyre Heros for sans-serif labels. The same
setting is applied to interior and standalone figure labels, since the Geometry
interior used the same fallback.
`tools/check_cover_pdf.py` checks physical dimensions and rejects Type 3 or
unembedded fonts, in every front preview, paperback interior and production wrap pipeline.
A final clean release run validates this correction across all volumes.

## Cover review after the structural revision (27 October 2026)

- Reviewed all nineteen current front covers as a contact sheet, with the renamed
  titles checked individually. No title/subtitle/illustration collisions were found.
- All **19 × 5 = 95 front PDFs** passed complete title/subtitle/slogan extraction,
  physical-size and embedded-vector-font checks. No extracted text crossed a page
  boundary. The latest vector-font correction from main is incorporated.
- Inspected Higher Structures' production paperback wrap, including its spine,
  back-cover text, barcode reserve and bleed. Its actual 184-page interior gives a
  0.4144-inch spine. Other integrated-volume paperback wraps will be regenerated
  from their own rebuilt interiors by the normal publishing workflow.
- Updated Volume 9's explanatory subtitle to **Categories, Rings and Homology**,
  making the transition beyond Volume 2 explicit. Its five front sizes were checked
  again, and its complete production pipeline succeeded. The subtitle was verified
  in the front, reading PDF, wrap, KDP listing, EPUB metadata and online reader.
- All fifteen publishing tests and `git diff --check` pass. The motif guide's
  remaining obsolete illustration count now reads nineteen.
- Local review artifacts: `build/cover-review/contact-sheet.jpg` and the vector
  `build/cover-review/current-series-covers.pdf`. These previews do not publish the
  changes or replace the live release.

## Local Volume 0 trim comparison

The author requested a detailed print review and a local 7 × 10 proof. The results,
mathematical corrections and outstanding monochrome-figure refinements are in
[the Volume 0 print review](../review/VOLUME0-PRINT-COMPARISON.md). The proofs contain
291 pages at 6 × 9 and 233 at 7 × 10 with the same 11 pt text. This is a local
comparison at the time of that review; the author has since approved 7 × 10
for every production paperback (see below).

## Production 7 × 10 migration

The author approved the comparison trim for all nineteen current books. The
interiors retain 11 pt Palatino and mirrored 0.75/0.6-inch inner/outer margins,
with 0.75/0.8-inch top/bottom margins. A gutter of 0.875 inch is selected if a
rebuilt interior exceeds 700 pages. Chapters still open on rectos.

`common/print-layout.json` and its generated TeX coordinate interior geometry,
cover wraps, front previews, KDP listings, download labels and PDF validation.
Front typography and diagrams scale uniformly from the shared design canvas;
back-cover text is reflowed for the wider trim. Outside bleed remains 0.125 inch,
and ISBN barcodes retain their physical size. Every spine uses the actual rebuilt
interior, rounded up to an even KDP page count. Reading formats are preserved.

CI checks the configuration and publishing tests before planning builds. A new
cache schema/namespace forces complete production regeneration. Per-book print
metadata is required in complete cached libraries; every interior page and wrap
is checked for exact physical size and embedded vector fonts before publication.

### Completed local migration checks

All nineteen interiors/wraps passed physical-size, embedded-vector-font, complete
front-copy and page-boundary checks. All 95 front proofs and 20 publishing tests
passed. A complete Volume 9 pipeline passed with the existing reading dimensions.
Final page counts, spine sizes, typesetting corrections and verification limits
are recorded in [the production trim audit](../review/7X10-PRODUCTION.md).

## Volume 0 mathematical and factual review (27 October 2026)

All eight chapters, 130 exercise/hint/solution sets, workshops and challenge notes
were reviewed against the mathematics and selected primary/historical sources.
Corrected proof gaps, algebraic signs, sampling assumptions, numerical error bounds,
figure captions, historical overclaims and outdated open-problem status. The full
record and reproducible calculations are in [VOLUME0-FACT-REVIEW.md](../review/VOLUME0-FACT-REVIEW.md).
The 7 × 10 trim and approved cover identity are preserved. Every Volume 0 output
and its actual-page-derived paperback wrap are rebuilt from the corrected source.

## Single standard PDF migration

The build compiles the canonical PDF once, validates every page at 504 × 720 pt,
and derives the matching wrap from its actual page count. There is no separate
reading-PDF or paperback-interior copy. `--pdf-only` refreshes this same PDF and
production assets without recompiling EPUB/HTML. Cache schema/fingerprint 3 and
`library-v3-` force all nineteen volumes to rebuild. Cache assembly removes legacy
variants; snapshot validation rejects retired files, wrong PDF sizes, unembedded
fonts and page-count metadata mismatches before any release is uploaded.

Download cards and README tables offer the standard PDF and EPUB. The paperback
interior link points to the canonical PDF. All ISBNs, titles, mathematical content,
7×10 margins, black-and-gold covers, EPUB reflow and reader controls are preserved.
Verification and rollout results are recorded in [STANDARD-FORMATS.md](STANDARD-FORMATS.md).
