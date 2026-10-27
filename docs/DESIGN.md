# Exact approved-image cover policy — correction

The author rejected the published recreation and then explicitly asked **“i want
exactly the same please”**. The earlier vector approximation, font substitutions,
flattened background and reconstructed Volume 0 illustration below are superseded.

The definitive visible front is the original file
[`tools/assets/approved-volume-0.png`](../tools/assets/approved-volume-0.png), copied
byte-for-byte from the approved reference. Its SHA-256 is recorded in
[`approved-cover.json`](../tools/assets/approved-cover.json). Volume 0's front embeds
this image unchanged: no retyping, recoloring, redrawing, stretching or cropping.
Transparent text provides search/accessibility without changing visible pixels.

The other eighteen covers directly reuse the original image's frame, series heading,
slogan and author. Their variable content uses licensed Inter weights and their own
mathematical vector illustration on a matching blank charcoal texture. No top mark
is added. Covers/wraps use XeLaTeX with bundled fonts; body PDFs retain pdfLaTeX,
Palatino, whole-box pagination, black-ink settings and existing mathematical content.
The approved image is cached as a reusable PDF XObject rather than re-encoded for
each clipped identity region.

EPUB images, readers and library thumbnails preserve the approved proportions.
The previous forced 1600 × 2560 output and 100 × 160 thumbnail crop altered the
composition; these are replaced by the standard 7:10 front. Volume 0's EPUB,
reader and library PNGs are the **original PNG bytes**, not a PDF rasterization.
Other EPUB/Kindle images use 1792 × 2560. The original master is 1049 × 1500 pixels,
about **150 ppi at 7 × 10 inches**; embedding/upscaling it does not create more detail.
This is an explicit exception to the old vector-only production rule.

`tools/check_cover_reference.py` verifies the master file hash and actual decoded
image pixels extracted from the production PDF. When supplied, it also checks EPUB,
reader and library images byte-for-byte. This replaces the discarded approximate
text-landmark comparison. New print wraps still use actual rebuilt interior page
counts and the existing barcode/bleed rules. `docs/COVER-MOTIFS.md` records the
master/vector distinction. The source was pulled to **dc98d05** before this correction,
preserving the author's intervening pagination fixes.

The remainder of this file records the previous implementation and its historical
checks; its approximation claims do not override the exact-image policy above.

---

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

### Verified complete publication

Implementation commit **5936eed** passed the [complete nineteen-book clean run](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/40564431866).
All nineteen build jobs, complete-library snapshot validation, release publication
and the actual **Deploy the download page** step succeeded. The rolling [books
release](https://github.com/OussamaSegh/Order-and-Chance/releases/tag/books) targets
that exact commit and contains **114 assets**. The [live library](https://oussamasegh.github.io/Order-and-Chance/)
was checked for all nineteen books, the exact design commit, the new theme and
updated Volume 0 reader CSS.

All nineteen **published** paperback wraps were downloaded from that run and checked
again for physical dimensions, embedded fonts, full front copy and actual-page spine
metadata, then visually reviewed as a complete wrap contact sheet. Production wrap
review artifacts and page/spine records are in `build/ci-coral-wraps/`.

## Source pagination for the final 7 × 10 pages

Framed exercises/problems, reminders, beauty notes, pause-and-think prompts and
challenges are now unbreakable. The preamble measures every frame and rejects a
frame taller than the text area or a locally reenabled split frame. Larger future
material must be reorganised into logically complete units in the source. Box
labels and reference anchors travel with their exercises, preserving numbering.

Long inline formulas that protruded beyond the final measure have been reflowed
as unnumbered displays, and two prose/citation lines were adjusted for line fit.
Hint/solution starts reserve space; paragraph widows and orphans are blocked.
Ragged page bottoms preserve natural paragraph spacing when a whole box moves.
Body type, trim, margins and approved cover identity are preserved. EPUB styles
request matching keeps within the reading system's pagination capabilities.

`tools/check_book_layout.py` runs after the final TeX pass and rejects horizontal
or vertical overflow, oversized figures, unresolved/duplicate references and
missing/invalid box measurements. Eight new tests cover diagnostics, actual moved
box reference placement, solution and section openings, oversized boxes and forbidden
split frames. CI executes the typesetting tests after installing TeX. All 34 publishing
tests pass locally.
Full-library PDF checks, page counts and review evidence are in
[7X10-PAGINATION.md](../review/7X10-PAGINATION.md). All production wraps are rebuilt
from their revised interior page counts.
