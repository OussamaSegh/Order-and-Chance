# Approved charcoal/coral editorial series design

On 27 October 2026 the author selected the **left-aligned** cover shown in
[the approved Volume 0 reference](reference/approved-charcoal-coral-volume-0.png)
and requested implementation for all nineteen books, paperback covers, content
accents, HTML readers and the GitHub Pages library. This latest selection supersedes
the earlier centered charcoal/coral and black/gold designs. Historical implementation
and validation records are preserved in [DESIGN-HISTORY.md](DESIGN-HISTORY.md).

## Visual identity

- Series **Order and Chance**, author **SEGHAIER Oussama**.
- Slogan **Discover the patterns. Understand the proofs.**
- Matte charcoal **#191919**, warm coral **#F28B79**, ivory **#F5F1E9**.
- A fine double rectangular coral border, without decorative corners.
- Minimal sans-serif cover type: left-aligned series heading, slogan, volume label,
  prominent bold book title, italic explanatory subtitle and author. Book titles
  wrap at word boundaries without hyphenation, fitting the shared title region.
- Exactly **one substantial lower-right illustration** per book. No small top
  construction, collage or decorative formula above the heading.
- Production cover text, borders, background and illustrations are vectors. The
  approved concept image is a design reference, never embedded as a print master.
  Matte charcoal replaces the old textured raster background.
- Covers and paperback wraps use embedded **TeX Gyre Heros** sans-serif lettering.
  Palatino remains the readable mathematical body face. PDF front matter uses
  matching sans-serif series/title typography while keeping black-ink output.

## Mathematical illustrations

`tools/cover_plates.py` generates nineteen distinct `cover-motif.tex` files and
[the content manifest](cover-art-manifest.json). Geometry algorithms are shared with
`tools/cover_motifs.py`; the mathematical subjects and evidence are listed in
[COVER-MOTIFS.md](COVER-MOTIFS.md). Retired `cover-motif-mark.tex` files are removed.

Volume 0 remains the exact sampled graph **z = exp(-(x²+y²))**. Its taller projection
and lower-right framing place the peak toward the right without distorting
the geometry or shearing the surface. Only the outer ground mesh is cropped. Other books retain their existing content-specific constructions.
All illustrations are fitted uniformly into the lower region, without stretching,
and clipped at the inside of the frame. Mathematical labels remain vector text.

## Palette and reading themes

`common/design-colors.tex` defines the TeX palette. Older color names remain aliases
for compatibility with authored figures. Coral linework has a quieter comparison
tone; ivory is reserved for cover lettering. Light reading surfaces use neutral
paper **#FBF9F6**, charcoal text **#252323**, and accessible deep coral **#A34232**.
Dark reading surfaces use charcoal **#191919**, ivory and warm coral **#F28B79**.

Exercises, reminders, beauty notes and thinking prompts use related muted coral,
stone, sage-gray and mauve-gray tones so their meanings stay distinguishable.
Scientific diagrams retain colors needed to distinguish curves or objects. The
sole standard PDF also serves as the paperback manuscript: its existing grayscale
semantic-box and black-link overrides remain in effect for black-ink printing.

`tools/epub.css`, `tools/reader.css` and `tools/site-template.html` mirror this palette.
EPUB leaves page and body colors under the reading device's control. Online headings
use restrained sans-serif typography; mathematical paragraphs retain a readable
serif face. Both website and reader support light/dark preferences; the library's
new theme switch persists the same `theme` preference used by the reader. Search,
collection filters, downloads, chapter navigation, mobile contents and collapsible
hints/solutions remain functional. The website hero repeats the cover's charcoal,
ivory and fine double coral frame.

## Metadata and production formats

Explanatory subtitles remain canonical in `common/volume-subtitles.json`, synchronized
by `tools/series_metadata.py`. Covers, PDF title pages, EPUB subtitle metadata, KDP
listings, reader pages and library cards must agree. Volume 0 keeps **A Foundations
Prelude**. All titles, ISBNs, volume identifiers, mathematical content, references,
author spelling and edition metadata are preserved.

Each volume has one canonical **7 × 10 inch PDF**, also its paperback manuscript,
and one reflowable EPUB. A4, Kindle PDF, phone PDF and duplicate `-print.pdf` editions
remain retired. `common/print-layout.json` governs trim and margins. Paperback wraps
have **0.125 inch outside bleed** and use the actual rebuilt interior page count:
white-paper spine width = even-rounded interior pages × 0.002252 inches. Barcode
handling and the reserve for KDP-assigned barcodes are preserved. No hypothetical
page count is used to make a production wrap.

## Shared implementation and rebuild

Shared front `tools/cover-front.tex` is used by EPUB fronts and paperback wraps;
`tools/cover-colors.tex` sets fonts/palette/background, `tools/cover.tex` supplies
front canvases and `tools/cover-wrap.tex` supplies back/spine/bleed. All shared inputs
participate in `tools/build_plan.py` fingerprints, so the palette and typography
change invalidates every book, EPUB and reader in CI. Cached libraries must still
be complete before they can be published.

```
source /workspace/order-chance-system/activate.sh
python3 tools/cover_plates.py
python3 tools/preview_covers.py --out build/coral-covers
./build.sh
python3 tools/site.py dist build/site
python3 -m unittest discover -s tools -p 'test_*.py'
```

Previews validate both standard-book and EPUB proportions, embedded vector fonts,
physical dimensions, and full title/subtitle/slogan text. Inspect the full-series
contact sheet, long titles, real paperback wraps and representative interior pages.
The release pipeline verifies every standard PDF page, paperback metadata and complete
library before publishing. GitHub release/Pages deployment does not upload to Amazon
KDP; the author uploads the generated assets through their Amazon account.

## Validation and rollout

The implementation began after `git pull --ff-only origin main` advanced the clean
workspace to **18cab2c**, incorporating the latest mathematical corrections and
single-standard-PDF migration before any edits. Verification and publication results
are recorded below as they complete. Earlier trim and content reviews remain linked
in [STANDARD-FORMATS.md](STANDARD-FORMATS.md), [the production trim audit](../review/7X10-PRODUCTION.md)
and [the Volume 0 factual review](../review/TOME0-FACT-REVIEW.md).

### Completed local checks

- All **19 × 2 = 38** final fronts passed physical-size, complete title/subtitle/
  slogan/author extraction, text-boundary and embedded-vector-font checks. The
  entire series contact sheet and long titles were inspected. All nineteen artwork
  hashes match the manifest. Preview catalogue: `build/coral-covers-final/`.
- Full pipelines passed for Volume 0 and Volume 9: standard PDF, EPUB, actual-page-
  derived wrap, eBook cover, listing, metadata and HTML reader. Volume 0 has 233
  pages (234 KDP pages, **0.527 inch** spine); Volume 9 has 148 pages (**0.3333 inch**
  spine). Both full wraps, barcode handling and representative interior pages were
  inspected. The final Volume 0 cover was refreshed in its EPUB and all cover assets.
- All **26 publishing tests** passed, plus Python compilation, shell syntax and
  `git diff --check`.
- Real Chromium checks passed for website and reader light/dark modes, persisted
  preference across both, search, collection filters, KaTeX mathematics, collapsible
  hints, mobile contents and no page overflow at **320 and 390 px**. No JavaScript
  page errors. Primary controls have **5.91:1 light** and **7.32:1 dark** contrast.
- Existing one-PDF/EPUB production formats, dimensions, ISBN, metadata and authored
  mathematical content are preserved. The source change invalidates all nineteen
  book fingerprints; complete-library CI/release publication is checked separately.
