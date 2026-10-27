# Series design and session record

## Approved identity

On 27 October 2026 the author selected the slogan **Beautiful mathematics through
problems and proofs.** and requested its application everywhere. That replacement
was committed as `6725bb52012ab1746596cbe635a8c9fc1e063860` across all 28 book title
pages, shared front matter, covers, website/reader templates, KDP listing generator,
publishing handoff and README.

The author initially selected **D — Engraved**, then explicitly changed the reference
on the same day to the attached cover now stored at
[reference/approved-cover.jpg](reference/approved-cover.jpg). **This attachment is the
current authority and supersedes the first D mock-up.** The author also requires
every illustration to be meaningful to its book's contents. The volume-by-volume
mapping is in [COVER-MOTIFS.md](COVER-MOTIFS.md).

Series name: **Order and Chance**. Author spelling: **SEGHAIER Oussama**.
Do not restore the former navy/gold design or the old "all proved" slogan.

## Current cover system

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
  backs and spines. Internal Tome identifiers and bibliographic titles stay unchanged.
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
./build.sh tomeC5-learning
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
