# KDP print export: required production process

The author approved the prepared Volume-0 print interior and cover and required
that every pipeline output use the same working settings. The latest artwork and
manuscripts are retained. These rules supersede historical raw-PDF instructions.

## The three reader-facing formats

| File | Purpose | Required preparation |
| --- | --- | --- |
| `dist/<book>.pdf` | Reading/download PDF, with front cover | Original typeset vectors, Unicode mathematics, links, bookmarks and labels retained. |
| `dist/kdp/<book>-print.pdf` | KDP paperback manuscript | Opaque, noninteractive PDF 1.3; no front cover or document metadata. |
| `dist/<book>.epub` | Reflowable ebook | Original licensed font faces and canonical cover. |

The separate `dist/kdp/<book>-cover-wrap.pdf` is the paperback **cover upload**,
not another reading edition. It uses opaque PDF 1.5, matching the working cover.
Do not add A4, fixed Kindle, phone or extra public PDF editions.

## Interior export

1. Typeset `build/<book>/main.pdf` in 7 × 10 inches. Existing source/layout,
   whole-box, font, missing-glyph and reference checks must pass first.
2. Build the reading PDF from that original file using `tools/book_pdf.py`.
   The exact original streams, labels, links and destinations are checked here.
3. Run `tools/kdp_pdf.py` to produce the canonical `*-print.pdf`.
   - Repair missing ASCIIHex end markers in PGF mesh streams.
   - Remove annotations, links, outlines, named destinations, startup actions,
     layers, attachments and document metadata from the print export.
   - Prune unused opacity and XObject resources. Unused global PGF alpha can
     otherwise rasterize almost an entire book, even when only five pages use it.
   - Normalize through Ghostscript to PDF 1.3. Flatten actual transparent pages
     at **600 ppi**, with no image downsampling. Keep vector text elsewhere.
   - Reject unencrypted-format regressions, live alpha, malformed/unnormalized
     streams, interactions, crop/rotation changes, unembedded/bitmap fonts,
     images below 300 physical ppi, invalid page counts and oversized files.
4. Compare every page against the original body: geometry, visible colours and
   two-sided ink coverage. Unexpected rasterization is an error. Do not weaken
   the comparison to make a failing book publish; investigate the affected page.
5. Retain `build/<book>/kdp-preflight.json`: source/output hashes, original
   navigation/body digest, repaired streams, transparent/flattened pages,
   resolution and comparison measurements. The report is required by CI/cache.

Ghostscript can rewrite font Unicode maps. That is why the cleaned print PDF must
**never** replace the raw manuscript as the reading/EPUB source. Print/read stream
identity is intentionally superseded by independent reading-source provenance and
final visible-content parity. Visible pagination, mathematics and colours must agree.

## Cover export

1. Compile the latest canonical vector front/wrap. Preserve fonts, shared identity,
   art direction, poses, material, title-relative subtitles and approved source.
2. Validate the raw vector cover against its master, source manifest, embedded
   fonts, native muted paper, frame placement and back-copy requirements.
3. `tools/kdp_cover.py` composites only transparent illustration regions at
   **600 ppi**, using lossless RGB pixels from the actual cover rendering.
   It must refuse a composite overlapping title/subtitle/back/spine lettering or
   one large enough to rasterize the whole cover. Frames/barcodes stay vector.
4. Preserve the original embedded font programs and Unicode maps; do not run
   covers through Ghostscript font rewriting. Remove invisible searchable
   duplicates of traced identity lettering and stale
   opacity states after compositing. Do not make invisible text visible. Remove
   metadata and interactions, then normalize to the working cover's PDF 1.5.
5. Compare the original and final cover outside composited regions. Inside each
   region, verify the exact RGB pixels sampled from the original at 600 ppi and
   their physical placement; then compare the entire final cover against the
   composited reference. This avoids comparing dense vector meshes rendered at
   screen resolution to the same meshes sampled at print resolution. Do not
   relax the comparison threshold to hide antialiasing differences. Require vector lettering,
   no live alpha, valid source/output hashes, the current series manifest, native
   paper >=300 ppi and all generated illustration patches >=600 physical ppi.
   The generated patch hashes extend the paper-only raster whitelist **only for
   this checked print export**. Source/digital artwork remains vector.
6. Retain `build/<book>/cover-preflight.json` with original master preflight,
   export hashes, patch provenance/resolution and complete-cover comparison.

Never flatten the entire cover to a bitmap, enlarge an old cover image to claim
new detail, substitute an earlier illustration, or normalize digital fronts via
this print-only path. The author explicitly chose the latest pulled artwork.

## Geometry and KDP settings

- Paperback; **7 × 10 inches**; **premium colour / white paper**.
- Interior: **no bleed**, every page exactly 504 × 720 PDF points.
- Cover: 0.125-inch outside bleed, total height 10.25 inches.
- Read actual exported print pages; round up to an even count for the spine.
- Spine = even-rounded pages × **0.002347 inches**, rounded as specified by
  `common/print-layout.json` / `tools/print_layout.py`.
- Cover width = 14.25 inches + calculated spine.
- Never reuse the initial 241-page Volume-0 specimen or its 0.568-inch spine for
  a revised manuscript. The pulled Volume 0 has ten chapters; rebuild/count it.
- Upload `*-print.pdf` under Manuscript and `*-cover-wrap.pdf` under Cover.
  The interior's “No bleed” selection does not remove the required cover bleed.

## Dependencies, CI and future-agent checks

Install XeLaTeX, Ghostscript, Poppler, Pandoc and `tools/requirements-build.txt`.
PyMuPDF is pinned for rendering comparisons. CI explicitly installs/caches
Ghostscript; its package cache is separate from older TeX-only caches.

```sh
source /workspace/order-chance-system/activate.sh
python3 -m unittest discover -s tools -p 'test_*.py'
./build.sh tome0-mathematical-maturity
python3 tools/kdp_pdf.py dist/kdp/tome0-mathematical-maturity-print.pdf \
  --report build/tome0-mathematical-maturity/kdp-preflight.json
python3 tools/check_print_cover.py dist/kdp/tome0-mathematical-maturity-cover-wrap.pdf \
  --number 0 --press-report build/tome0-mathematical-maturity/cover-preflight.json
```

Schema/fingerprint **7** and `library-v7-` force every book to regenerate. Both
export reports are required in each artifact/cache entry. Snapshot assembly checks
the final files and hashes again, verifies reading navigation/body provenance and
visual parity, and validates page-derived cover geometry before publication.
Missing reports, stale raw PDFs or altered output must block publication.

Pull before editing/pushing. Preserve concurrent manuscript/cover updates; do not
cancel another thread's build. Record the exact source/CI/release commit and verify
that the actual Pages deployment succeeds. Never treat successful local rendering
as proof that KDP accepted an upload; report actual author feedback separately.

Official preparation guidance:
https://kdp.amazon.com/en_US/help/topic/G201857950

## Implementation verification

The local publishing suite passes 76 tests, including actual Ghostscript export,
unused-opacity pruning, malformed ASCIIHex repair, reading-source provenance,
rejection of altered output, selective cover compositing, preservation of visible
lettering and removal of invisible identity duplicates. The export was exercised
on nineteen available compiled interiors with no failures. The revised Volume-0
production run passes at 295 print pages / 296 reading pages, with a 0.6947-inch
spine, original reading navigation, an opaque 600 ppi art composite and vector
cover lettering. The canonical cover sources/assets and mathematical source are
unchanged by the export implementation. Current main through `637cdb0` is retained,
including the newer thirteen-chapter Volume 1; clean CI rebuilds each latest
manuscript rather than publishing the older local conversion fixtures.

### Dense-cover comparison correction

The first clean run passed all nineteen interior exports and sixteen complete book
jobs. Three dense cover meshes exposed a comparison-resolution mismatch: the same
art rendered directly at 72 dpi differed from its exact 600 dpi composite reduced
to screen size. Spaces was reproduced locally: every pixel outside the artwork
matched exactly. The gate now checks original vector regions, exact source-sampled
art pixels and physical placement, plus the entire final-versus-composited cover.
A new regression still rejects changes outside the art region and wrong placement.
The original thresholds and artwork remain unchanged. The reproduced Spaces cover
and all six cover-export regressions pass before rerunning the full build.
