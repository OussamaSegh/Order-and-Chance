# Approved black-and-gold series design

The author approved the balanced black-and-gold Volumes 0/1 proofs and requested
application to **all 28 volumes**, their KDP covers, interiors and online themes.
This supersedes every prior two-volume-only restriction and earlier rust, navy,
dense-edge and tiny-motif design. See [DESIGN-HISTORY.md](DESIGN-HISTORY.md) for the
archived sequence of proposals; it does not override this document.

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
- All 28 fresh main/secondary illustrations are generated from mathematical data
  and deterministic algorithms by `tools/cover_plates.py`. Underlying constructions
  are in `tools/cover_motifs.py`; the old command delegates to the new generator.
  Parameters, seeds and sampling density are fixed for reproducible output.
- Volume 0: exact sampled graph z=exp(-(x²+y²)); a Fibonacci construction above.
  Volume 1: exact integer circle a²+b²=25 and 3–4–5 triangle; Fibonacci mark above.
  Other plates follow their own manuscripts; see [COVER-MOTIFS.md](COVER-MOTIFS.md)
  and [the machine-readable manifest](cover-art-manifest.json).

## Explanatory subtitles

After approving the style the author requested an explanatory subtitle for every
volume, following **A Foundations Prelude**. All 28 unique subtitles are stored in
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

`build.sh` creates A4 and Kindle reading PDFs, EPUB, ebook covers, KDP interiors and
wraps, listings and HTML readers. Wraps use 6x9 trim, 0.125-inch outside bleed and
white-paper spine width = even-rounded interior pages × 0.002252 inches. ISBN
barcodes remain intact; books without an ISBN reserve the lower-right back area
for KDP. No hypothetical page counts are valid production inputs.

The all-volume front preview checks five formats (print/reference, ebook, A4,
Kindle and print-front); PDF text extraction verifies every title and the slogan,
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
