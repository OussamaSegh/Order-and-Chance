# Verified GitHub filename normalization — 28 October 2026

Live run 40703902773 built all nineteen books and validated the complete library,
but release verification exposed that GitHub replaces spaces with dots on both
upload and rename. The publisher now explicitly validates either the exact name
or that known transformation, requires the readable label and matching byte size,
and verifies the SHA-256 digest when GitHub supplies it. Arbitrary names and
content mismatches remain failures. Generated files and Pages downloads retain
spaces. README direct links now use Pages, where those names are preserved.
This supersedes the earlier expectation that PATCH could restore spaced names.

The preceding subtitle-only run 40701152017 also passed all builds and library
validation, but its release creation was refused after the newer workflow commit
changed main. The final combined publication must be verified at its exact SHA.

---

# Readable public filenames — 28 October 2026

The author requested “Volume” and readable filenames with spaces. Public main-book
assets now use basenames such as `Volume 0 - Mathematical Maturity`; the problem
books use `Problem Book 1 - Crossroads`, `Problem Book 2 - Machinery` and
`Problem Book 3 - Frontiers`. `tools/public_names.py` derives these from current
book title metadata. This supersedes earlier instructions to retain machine-style
public filenames; internal source directories, TeX identifiers and reader routes
remain stable. No manuscript, typography, cover, export setting or pagination changes.

Reading PDFs and EPUBs use their ordinary extensions. Public publishing assets add
` - Print.pdf`, ` - Paperback Cover.pdf`, ` - eBook Cover.jpg`,
` - Publishing Listing.md` and ` - Print Metadata.json`. Site thumbnails add
` - Cover.png`; browser listings use `.txt`. Both build paths and validation use
one naming helper, with quoted shell arguments and encoded URLs. Cache schema 8
invalidates prior outputs; assembly removes obsolete names and rejects unexpected
assets, including a third PDF or a superseded-title download. README release links,
site downloads, reader links and runnable editorial packaging helpers follow suit.

GitHub documents upload-time filename normalization. The release helper labels
each uploaded file, restores any changed name using the update API, and requires
the resulting exact filename and byte count. Pagination handles all nineteen books.
Tests simulate normalization and rejection; live release writes were not performed.
See https://docs.github.com/en/rest/releases/assets#upload-a-release-asset.

Verification: 83 publishing tests completed, 65 passing and 18 skipped for missing
TeX/PDF build-tool dependencies. Naming tests cover all nineteen unique basenames
and all public suffixes; cache/site tests exercise filenames with spaces, stable
ordering, URL decoding, copied bytes and stale-output rejection. Shell syntax and
`git diff --check` pass. The prescribed `/workspace/order-chance-system/activate.sh`
and XeLaTeX are absent on this Mac; dependencies were installed in a temporary
isolated Python environment. A full typeset rebuild, real release upload and CI
publication remain unverified. The existing subtitle publication run 40701152017
was not changed or cancelled. This naming change is local only, pending the author's
instruction to push/publish.

---

# Volume 0 subtitle — 28 October 2026

The author approved **Proof, Problem Solving and Mathematical Thinking** for
Mathematical Maturity, explicitly including the covers. Canonical JSON and its
generated TeX now supply this wording to the title page, EPUB metadata, KDP
listing, web reader and library. The shared front used by reading/eBook covers
and paperback wraps uses a cover-only break after “Solving”, keeping the exact
words, existing Inter italic size/tracking and title-relative first baseline.
The established 5.4-inch subtitle area is now explicit in the common template.
Other subtitles remain on one line; illustrations and their hashes are unchanged.

Verification: 28 cover, site and build-planner tests pass; metadata and generated
cover configuration are synchronized. Volume 0 and Crossroads fronts pass the
7×10 geometry, embedded-font, overflow, shared identity and subtitle-position
checks. The revised Volume 0 front was rendered and visually inspected with two
balanced subtitle lines and clearance above the Gaussian. Local review files are
in `build/subtitle-final-review/` and the print-source front proof is in
`build/subtitle-final-print-review/`. These are local cover proofs; the full book,
EPUB, KDP export and live release/Pages have not been rebuilt or published here.

---

# Approved KDP exports for every book

The author confirmed the prepared Volume-0 interior and print wrap, then required
that both pipeline outputs follow those working files for all nineteen books.
Current main was pulled through `a65d685`, including the ten-chapter Volume-0
reconstruction and newer cover art. The author explicitly retained the latest
artwork and requested the working PDF export settings. No manuscript, illustration,
font, shared cover template or mathematical content is changed by this task.

Print interiors now use the approved PDF 1.3 process: terminate malformed ASCIIHex
mesh streams, remove interaction/metadata, prune unused global PGF opacity and
XObject resources, then normalize with Ghostscript. Only genuine transparent pages
are flattened at 600 ppi; images are not downsampled. Reading PDFs are made first
from the original typeset body so Unicode mathematics, vectors and navigation are
retained. The two files share pagination/visible content rather than byte-identical
PDF streams. Exact reading-source checks and final visual/provenance checks replace
the obsolete print/read stream-equality contract.

Print wraps follow the working cover's opaque PDF 1.5 settings. Their original
vector source passes all master/font/art/paper gates. Only transparent illustration
regions are composited losslessly at 600 ppi; title, subtitle, back copy, spine,
barcode and frames retain vectors. Whole-cover rasterization is rejected. A print
cover's generated art pixels are allowed only with matching source/provenance and
full-page visual comparison. Source art remains vector, and digital fronts remain
unchanged. This is the specific exception to the earlier paper-only print-raster
policy; grain itself must still be native >=300 ppi.

Both export reports are retained by CI and required by cache assembly. Ghostscript
is an explicit build dependency, PyMuPDF is pinned for comparison, and cache schema
7 forces regeneration of every book. Spines use each fresh print count; the old
241-page specimen does not override Volume 0's revised manuscript. See
[KDP-EXPORT.md](KDP-EXPORT.md) for the authoritative workflow and verification.

---

# Volumes 0 and 1 harmonised to the established series style

The author rejected further attempts to match every book to the stronger glow in
Volume 0 and instead explicitly asked to make Volume 0 look like the others, also
harmonising Volume 1. Volume 0's Gaussian is now a native parametric height mesh
using the common renderer, coral material, wire weights and five restrained halo
layers. The special reference-art draw/import branch is removed from production.
The traced Gaussian and original approval PNG remain untouched archival references.

Volume 1 retains its exact Ulam prime locations while reducing the needle-like
height, broadening bases and subdividing each face into a fine triangular mesh.
It uses the same renderer and material as the rest. Generation verifies that only
motifs 0 and 1 change; the remaining seventeen artwork hashes are identical.
Common typography, identity, title-relative subtitles, all book content and the
concurrent interior styles are preserved. The manifest/composition/material guards
now apply to Volume 0 without an exemption. Print settings, vector-only artwork,
native paper and actual-page-derived spines remain unchanged.

The latest main was fetched at f4d797f before editing. Review evidence is under
build/harmonization-review. Local verification: both new vector fronts pass the shared typography, subtitle,
identity, material and composition checks; all 65 tests pass. A real previous
Volume-0 PDF is rejected by the new archived-art guard, while the new native front
passes. Publication rebuilds print and digital versions and refreshes the full
high-resolution series image.

---

# Individual mathematical illustration review

The author explicitly requested a separate aesthetic/content review of every
illustration, permitting replacements and individual pose/scale/placement. The
nineteen decisions and their chapter connections are in COVER-ART-DIRECTION.md;
compositions live in tools/assets/cover-art-direction.json. This supersedes the
older assumption that a fixed camera implies identical geometry orientation.
Type, subtitle spacing, colours, frame, author identity and five-layer vector
radiance remain shared. Volume 0 and the approved Volume-2 composition are retained.

Substantial replacements include smooth Fourier interference, a logarithm helicoid,
an actual Plancherel Ferrers wall, a Bernoulli large-deviation bowl, upright Dyson
eigenvalue ribbons, the inverse Collatz tree, a seventh-roots-of-unity star prism,
the book's exact Sobolev reproducing kernel, and finite Bernoulli-convolution laws.
Spaces retains its explicitly referenced Sierpiński carpet with shallow solid
walls. Existing zeta, prime-error, multiplicative-field, hyperbolic and elliptic
subjects receive individual composition rather than arbitrary new symbols.

The shared renderer rotates only world geometry and fits its complete silhouette
and halo within a title-safe viewport. PDF/manifest checks enforce the reviewed
composition and prevent title/footer overlap. The broader art window permits
single-line titles to use more space, while two-line titles retain full clearance.
All halos/geometry remain vector; only native paper is raster. The proof tool now
uses production's extra token-memory allowance for dense vector sculptures.

Four mathematical regressions independently verify the Collatz inverse graph,
Plancherel box count, actual H1 kernel values and symmetric normalised finite
probability laws. All 65 integrated publishing tests pass. Obsolete cover
claims in the Structures/Chance appendices are corrected without changing mathematical
statements or figures. The carpet and Young-diagram cover references remain true.

The current interior colour/frame correction from 8135b0b was pulled before this
pass and is preserved. No interior fonts, teaching-box roles, semantic palette,
scientific figure colours or print settings are changed. Any copy reflow is
handled by rebuilding the current manuscripts and deriving new spines from their
actual pages. Review outputs are under build/art-direction-review. All nineteen final 7 by 10 vector fronts pass the shared type, title-relative subtitle, identity, composition and clipping checks. Every illustration was inspected separately and again in the complete contact sheet. The final integrated suite passes all 65 tests; all-volume CI will recheck the finished print wraps and packaged EPUB/reader images before publication.

---

# Teaching-box colour and frame correction

The author identified that all teaching boxes used one colour and that some
appeared to have extra top or bottom rules. The earlier version-C implementation
had made every semantic accent coral. Its zero-width tcolorbox frame still
painted a full saturated rectangle underneath the body/title backgrounds. PDF
antialiasing could expose that underpainting at particular zoom levels.

All box types now share one frame definition: the full frame is hidden, and only
an explicit 1 pt left rule is drawn. Exercises and problems use blue `#235E82`,
reminders and challenges coral `#A34232`, beauty notes teal `#22675B`, and thinking
prompts plum `#704B80`. Pale fills, dark labels, the STIX/Inter version-C fonts,
charcoal headings and coral chapter/link accents are retained. EPUB and reader
styles use the same roles, including brighter distinct accents in dark mode.
Challenges and all three problem-book overrides use the common frame definition.

A real-PDF regression checks every box type, including all problem-book overrides:
exactly one vertical 1 pt rule per box, the expected distinct colours, and no
saturated frame underpainting. Existing whole-box/overflow/reference guards stay
in place. Shared-input fingerprints rebuild all nineteen volumes automatically;
cover source/artwork, trim and premium-colour settings are unchanged. Current
cover work from `3259d46` was integrated before these edits; the subsequent
`dabf093` glow/subtitle update is also preserved during integration. Review
evidence is under `build/box-review/`. All 61 integrated publishing tests pass
locally. Rebuilt
Volume 0 (241 print pages, 200 whole boxes) and P3 (45 pages, 23 whole boxes)
pass layout, PDF-pair, font/colour and vector-cover preflight. The exact reported
Volume-0 pages 42 and 56 are visually checked; browser checks verify four colour
roles and left-only rules in light/dark themes at desktop and 320 px widths.

---

# Approved glow and subtitles below the title

The author approved the glowing Volume-2 proof and its subtitle directly below
Structures, then asked for both refinements across all nineteen books. This
supersedes the earlier fixed-subtitle-position rule below. The approved generated
proof is a visual reference; production covers retain their real vector typography
and geometry rather than substituting a newly generated full-cover bitmap.

Subtitles now follow the last title line with the reference gap. Two-line titles
keep Volume 0's original baseline (source y=632.36); one-line titles move up by one
49.5 pt title leading. Font, size, tracking and alignment remain identical. The
single master generates these baselines, and the PDF checker validates each one.

All eighteen native illustrations use five layers of soft coral vector radiance,
with bright warm cores on upper wires and restrained fading toward the lower
mesh. Deduplicated edges are depth-tested before lighting, so hidden rear wires
cannot reappear in the halo pass. The depth buffer is a geometry calculation only;
no bitmap is included in the exported illustration. Volume 0's traced Gaussian
stays unchanged. Complete silhouettes and halos fit inside the common art window.

Chance replaces its Gaussian-like surface with a Galton branching lattice feeding
exact binomial probability columns. Machinery replaces the repeated torus with a
saddle patch in orthogonal principal coordinates of an indefinite quadratic form,
inspired by the Hilbert-space chapter. Mathematical data and source evidence are
recorded in the art manifest. The two new silhouettes distinguish them from
Mathematical Maturity and Arithmetic respectively. The Research Workshop tree now shows seven generations in space-time, keeping its branching structure legible instead of projecting a tangled spatial bundle.

Both cover formats, EPUB/eBook images, HTML readers and the public library render
the same updated source. Back-copy layout, all body content and approved Version C
interior typography remain unchanged. Premium-colour 7 by 10 inch trim, outside
bleed, actual-manuscript spines and the native >=300 ppi paper preflight are retained.
Review proofs are under build/glow-review; baseline pulled before editing: 3259d46. Local verification: all 60 publishing tests pass, all nineteen vector front proofs pass the shared font/subtitle/identity checks, and the Volume 2 and Machinery wraps pass 360 ppi paper, embedded-font, visible-frame, copy and actual-manuscript geometry checks (379 and 76 print pages). The contact sheet and full vector fronts were visually inspected; the final library build will repeat the complete checks before publication.

---

# One locked Volume-0 master

The author requires every cover to have the same typography, positions, colours,
frame, background and illustration treatment. Only the volume number, title and
illustration vary; each book keeps its subtitle, explicitly at Volume 0's position.
A common palette applied to different layouts/renderers did not meet this request.

All nineteen production fronts now use one template and the measured configuration
in `tools/assets/series-template.json`. Volume 0's original frame, masthead and author
are reused as the same vector form everywhere. All title blocks—including Volume
0's—are typeset with one actual bundled Inter Display Bold 700 font file, rather
than the differing lettering of separate generated concepts. Point size 54.8,
leading 49.5, horizontal scale, two-line title area and left margin are fixed.
Subtitles use one Inter Light Italic face/size/tracking, without shrink-to-fit.
Their baseline is fixed at source y=632.36: capital tops remain at y=600. Using
baseline anchors avoids the sub-pixel shifts caused by differing glyph heights.
The author/footer and masthead positions are inherited directly from the reference.

Volume 0's Gaussian illustration is preserved as source-derived vector contours
in `tools/assets/series/reference-art.pdf`. Every other cover has one coherent 3D
wireframe model: prime lattices, probability landscapes, Fourier/zeta surfaces,
fractal reliefs, symmetry meshes, tori and spatial random structures, grounded in
their book subjects. `tools/cover_surfaces.py` supplies world-space geometry;
`cover_surface_renderer.py` supplies one orthographic camera and one fine coral
material with selective crown highlights. Surface cells occlude rear lines instead
of producing a flat diagram or uniform neon tubing. Geometry-specific uniform fit
is part of the illustration; fonts, text anchors and frame never depend on it.
The manifest records subjects, evidence, 3D models, shared camera/material and hashes.

The earlier approval PNGs and full-cover traces remain untouched as historical
references. They are no longer substituted into live fronts: that would bypass
the common typography. Reading PDFs, EPUB/eBook images, reader and library covers
all render from the same master, including Volumes 0–2. The original reference image
is preserved; its title block is now represented by the same real font used for all
other titles. The reference composition, common identity and Gaussian art remain.

Back blurbs retain their content and a common fixed 10.25/14.5 pt Inter layout;
they are measured before entering TikZ and never autosized. Barcode labels use the
bundled sans face rather than an unavailable legacy font. Font/glyph/overflow logs
and a separate back-text check prevent blank or substituted back copy. Print wraps
retain 7 × 10 trim, 0.125 bleed, >=300 physical ppi native muted paper and spines
calculated from actual premium-colour manuscript pages. Interior typography,
mathematical text, labels, semantic colours and paper coefficient are unchanged.

`tools/check_cover_template.py` checks exact shared identity forms, fixed title
face/size, subtitle bounding baseline, template/source hashes and 3D style provenance.
It also verifies EPUB/reader images match their freshly rendered cover. Both build
and cache assembly use it. The library always renders the common cover PDF; it no
longer copies an earlier concept image for selected volumes. Regression tests cover
fixed type, moved subtitles, mathematical probability data, 3D surface structure,
missing back text and font substitutions. Proofs are in `build/series-master/`.
The baseline pulled before editing was `c839bba`. The concurrent approved version-C
typography update `9c94065` is integrated before publication, preserving STIX and
the current interior layout; production spines must use its freshly built pages.

# Approved version C across all 19 volumes

The author selected version C after reviewing the alternatives and asked for its
implementation throughout the series. It uses the covers' exact Inter Light and
SemiBold display faces, STIX Two Text/Math, the existing 11 pt body with 1.065 line
spacing, tracked small chapter labels and 24/29 pt chapter titles. Running heads
and box labels use the same Inter display family. Pale boxes have 1 pt coral left
rules and dark labels, matching the charcoal/coral cover identity. Scientific
figure colours remain unchanged. A real Inter semibold italic face completes the
heading family so optional exercise ratings never trigger font substitution.

The implementation preserves cover update `c839bba`, both 7 × 10 PDFs, EPUB,
premium-colour paper, actual-page-derived spines, identifiers and references.
Fonts/licences/hashes are in `common/fonts/`; EPUB embeds the 17 faces, and readers
use their WOFF2 equivalents. Reader controls retain Inter Text. Web mathematical
rendering retains KaTeX's own metric-compatible fonts; EPUB MathML and both PDFs
use STIX Two Math. Cache schema 6 invalidates the superseded layout. PDF validation
requires STIX text/math, Inter headings, charcoal/coral drawing commands, embedded
fonts, correct geometry and complete navigation; missing glyphs, overflow and
split/oversized boxes still stop publication. Source formulas are reflowed where
new metrics require it. Review/build evidence is in `build/version-c/`.

---

# Cover vibrancy: Volumes 3 onward

The author supplied the Volume 2 and Volume 3 wraps and correctly identified that
shared tokens alone did not produce the same appearance. The sixteen native-vector
covers used full-strength background grain, pastel flat fills and dim connecting
lines. The approved Volumes 0–2 had quieter charcoal and luminous coral artwork.
The previous all-cover quality check covered resolution and geometry, not this
visible material mismatch.

All sixteen remaining covers now use the same restrained 35% charcoal grain on
front, back and spine. `tools/cover_finish.py` applies warm coral linework, ember
halos and pale hot highlights using nested vector strokes. Filled histograms,
fractal cells and bands retain translucent colour with lit edges. The secondary
comparison curves retain a distinct coral tone. Coordinates, mathematical values,
paths, labels, fonts and page layout remain unchanged. All 16 original geometries
were compared against their regenerated forms. The three approved image masters
and their traced print assets remain untouched.

The shared source updates reading-PDF fronts, EPUB/eBook covers, HTML/library
images and print wraps together. It does not change interior fonts, semantic
colours, pagination or the premium-colour spine coefficient. Print preflight now
rejects the older full-strength paper tile even when its resolution is sufficient;
only the manifest-verified native muted tile is permitted. Native paper still
measures approximately 360 ppi on the panels, and every halo remains vector.

Regenerate with `python3 tools/cover_plates.py`; inspect the all-cover print proof
with `tools/preview_covers.py --print`. First proofs include sparse, dense, filled
and circular artwork (Volumes 3, 6, 8, 12 and P3). New material regression tests
preserve paths/data and secondary-curve distinctions. The integrated publishing
suite passes 51 tests. Local review evidence is in `build/vibrancy-review/`.
Latest `main` was pulled through `9ce62aa` before editing.

---

# Full-colour interiors and reading typography

The author now explicitly requires **colour printing and better fonts**. This
supersedes the earlier Palatino/black-ink interior policy below. Approved cover
art, image masters, cover text and cover fonts remain unchanged.

Interiors and figures now use bundled **Libertinus Serif + Libertinus Math**,
with **Inter Text** at optical size 14 for headings and **DejaVu Sans Mono** for
Unicode code. Body size stays 11 pt, with 1.045 leading. XeLaTeX handles the OTF
mathematics and embedded fonts; the build grants extra token memory for the 3D
PGFPlots surfaces. The source's legacy number-system commands remain valid in
unbraced scripts. No mathematical statement or reference numbering is changed.

Coral chapter/section headings and reminders, blue exercises, teal beauty notes
and plum thinking prompts provide visible colour structure. Pale fills, white
box-heading text and dark body text/math keep pages readable. Existing figure
colours preserve their scientific meaning. Long formula chains are reflowed when
the new font metrics need it; whole-box and heading pagination guards remain.

The paperback production setting is **Premium color ink, white paper**, 7 × 10
inches, no bleed. This accommodates the short problem books from 24 pages; standard
colour starts at 72. Premium-colour spines use **0.002347 inch per even-rounded
print page**, as documented in the KDP cover/print-option help pages. Canonical
JSON/TeX, listings, metadata and actual-page-derived wraps use the new setting.
Both PDFs share the colour body; only the reading PDF adds its approved cover.

EPUB embeds the licensed OTF/TTF faces; HTML readers use matching WOFF2 files.
Devices retain control over EPUB rendering. Font sources, licences and SHA-256
hashes are recorded in `common/fonts/`. Build/cache schema 5 forces a clean full
regeneration. The actual PDFs must contain the new font families and colour
accents; missing glyphs and accidental monochrome output fail validation. Tests
exercise Unicode mathematics/code, legacy scripts, font/colour output and the
existing reference-placement/pagination behaviours. Review artifacts and logs
are under `build/colour-typography/`. See [the implementation/review record](COLOUR-TYPOGRAPHY.md)
for the palette, font provenance, print settings and Volume 0 preview.

---

# Paperback print-quality upgrade

The author approved **vector paths from the approved cover**. This is a print-only
exception to the historical exact-image wrap policy below: digital PNG masters,
reading PDF fronts, EPUBs, reader and library images remain unchanged. The source
was pulled through `0838eb3` before editing, retaining the latest Volume wording.

Volumes 0–2 now have reviewed source-derived print-only Bezier masters in
`tools/assets/print/`, with their original glyph contours traced separately from
the mathematical mesh. Straight fitted borders and cumulative coral contours
retain the layout and visual identity without replacing the fonts. Shared back
identity uses small matching vector masters; the other sixteen illustration plates
remain native vectors. This smooths existing boundaries, without recovering detail
that never existed in the 1049 × 1500 originals. Editable SVGZ/PDF files and a
source/output hash manifest are committed; regeneration is documented in
`tools/PUBLISHING.md` and needs Inkscape, libpotrace0 and the art requirements.

The shared print template tiles native charcoal paper, preblended for approved
fronts/backs, at approximately 360 physical ppi on panels and approximately 420 ppi on the
outside wrap. Digital background behavior is preserved. Print preflight rejects
any other bitmap, any image placement below 300 ppi, changed vector/source hashes
or unembedded fonts. Reports are retained in CI; cached assemblies are checked
again before publication. Original artwork/type never appears as a bitmap inside
the print wrap. Actual interior pages still determine every spine and sheet size;
7 × 10 trim, 0.125 outside bleed and existing barcode handling are preserved.

Visual proofing caught a XeTeX PDF-import translation despite correct page bounds.
Masters are now cached outside TikZ before placement, and tile drawing is excluded
from bounding-box calculation. Inspect the visible frame/author as well as the
searchable copy and physical dimensions when changing these templates.

Verification: all 46 publishing tests pass. Corrected front proofs for Volumes
0, 1, 2 and the long-title Volume 15 were inspected. Volume 2’s complete wrap
passes the raster whitelist, 360 ppi, visible frame, embedded fonts and geometry
checks against its 372-page print interior (0.8377-inch spine). The previously
shifted proof fails the new visible-frame guard. Digital master hashes are unchanged.

---

# English series terminology

The author chose **Volume/Volumes** for the English series and explicitly asked
to leave the covers alone. Book half-title/title/copyright pages, PDF and EPUB
metadata, chapter prose, cross-volume references, the series catalogue, publishing
listings, website labels and reader metadata now use that term. Numbering and
reference identifiers are preserved. Existing `tome…` paths, TeX macros and
technical identifiers remain stable so download URLs and build inputs keep working.

Title parsers and the approved-image validator now read the `Volume N:` metadata
prefix; cover artwork, cover templates, back-cover text and image masters are
unchanged. Listings generated from protected back-cover text normalize the word
in the listing alone. Normal production wraps still derive their spine geometry
from rebuilt print interiors. Historical review records retain their original
terminology. The source audit checks the protected cover files by hash, while
the normal layout guards check the reflow caused by the longer English word.

Verification: 41 publishing tests pass, all 19 generated listing titles and
descriptions use the new term, and label/reference identifiers are unchanged
across 270 edited book source files. Hash checks confirm that the protected
cover source/assets are untouched by this terminology change. Local proof logs, source/hash audits and title
page previews are retained in `build/volume-terminology/`; the all-volume build
checks both PDFs and EPUB/reader outputs before publication.


---

# Back-cover coherence correction

The author rejected the back’s mismatched charcoal appearance and typography.
The shared paperback back now uses `tools/cover-back.tex`, on the same logical
canvas as the front. It reuses the actual front image’s frame, masthead, slogan
and author regions, so their lettering, coral hue, border widths and margins match.
The approved-image wraps use the charcoal token `#151516` with 35% paper grain;
legacy vector fronts retain their existing background. Sampled empty strips of
Volume 2’s rendered front and back both have median RGB **21, 21, 21**.

The blurb uses a wider 6-inch printed column, bundled Inter Light at approximately
13.4 pt with 18.7 pt leading, and ragged-right text without forced hyphenation.
Long blurbs fit above the reserved barcode area. Volume/title hierarchy follows
the same left margin, with the book title in Inter SemiBold. The old untracked
masthead, dim thin borders and separate centered slogan are retired. Approved
front images, blurbs, ISBNs and actual-page-count-derived wrap geometry are preserved.
All 41 publishing tests and the vector-front regression previews pass. Corrected
Volume 2 and the longer Volume 0 blurb/barcode wrap are checked before publication.

---

# Volume 2 approved-image update

The author approved the revised **fine coral polyhedral symmetry wireframe** cover
with the subtitle restored to the Volume 0 reference grid, and requested its
implementation. The exact chosen image is
`docs/reference/approved-charcoal-coral-volume-2.png`; its immutable production copy
is `tools/assets/approved-volume-2.png`, recorded in `approved-cover-2.json`.
SHA-256: `7573466f2b3889ec0088efe3d0272443b7035e7f2a51fb725c76ed98bcd6c26f`.
The first, heavier Volume 2 concept was not selected. Do not redraw, retype,
recolor, stretch or crop the approved replacement. Its native resolution is
1049 × 1500 pixels, about 150 ppi at 7 × 10 inches.

The reading PDF, EPUB, HTML reader, library thumbnail and paperback front all use
this approved master. EPUB/reader/library PNGs preserve its exact file bytes.
`check_cover_reference.py --number 2` verifies actual embedded PDF pixels and
unchanged digital PNGs. The former vector plate is retired; the illustration
manifest records this approved symmetry artwork, with sixteen other vector plates.
Volumes 0 and 1 retain their approved masters. The print interior remains separate
from the covered reading PDF, and wrap geometry still derives from actual print
pages, with 0.125-inch outside bleed and existing ISBN/barcode handling.
Latest main **ce45718** was pulled before editing.

Local checks: all 41 publishing tests pass, including exact PNG copying for
Volumes 0–2. Volume 2 passes both front-size/font/copy previews (digital and 7 × 10)
and the actual embedded-pixel comparison against the approved master.

---

# Volume 1 approved-image update

The author approved the generated **Ulam-inspired coral prime lattice** cover and
requested it for Volume 1’s digital and print covers. The approved image is
`docs/reference/approved-charcoal-coral-volume-1.png`; its immutable production copy
is `tools/assets/approved-volume-1.png`, recorded in `approved-cover-1.json`.
Its SHA-256 is `0e75f9581d6a25d59d7230a7b028bf7dcd617368fbddf5ee8cc535ea8868e90a`.
Use this whole image unchanged; the previous circle/triangle plate is retired.
This is approved illustrative artwork inspired by prime patterns, not a certified
numerical plot. Its native 1049 × 1500 pixels give about 150 ppi at 7 × 10 inches.

The reading PDF, EPUB, HTML reader, library thumbnail and paperback front all use
the same master. EPUB/reader/library PNGs retain its exact file bytes. The print
wrap retains actual interior-page-derived spine sizing, bleed and ISBN/barcode.
`check_cover_reference.py --number 1` checks embedded production pixels and digital
copies; its default Volume 0 checks remain intact. Seventeen other covers retain
their existing content-specific vector art. Latest main **73f370d** was pulled first,
preserving the separate covered reading PDF and coverless print PDF policy below.

Local verification: all 41 publishing tests pass; both approved-image covers pass
the embedded-pixel check and the front-size/font/copy checks in digital and 7 × 10
formats. A regression test confirms both library PNGs bypass rasterization.
The previous main run failed because site assembly imported `pypdf` before its
installation step; the helper installation now runs immediately after checkout.

---

# Current PDF delivery decision

The author now requires **two distinct 7 × 10 inch PDFs per volume**: the public
reading PDF includes the approved front cover, while the separate print PDF starts
with the half-title. EPUB remains available. This supersedes all older one-PDF
statements below; the exact approved-image cover policy remains in force.

`dist/<tome>.pdf` is the reading download; `dist/kdp/<tome>-print.pdf` is the
paperback manuscript. The body is compiled once. `tools/book_pdf.py` clones the
complete print PDF and inserts its cover without flattening annotations or
recreating page content. Printed page labels, named destinations, bookmarks and
metadata are preserved. The reading file adds one physical page; paperback page
counts, margins and spines are calculated exclusively from the print file.

The library and README expose both files clearly. Cache schema/fingerprint 4 and
`library-v4-` force a complete regeneration. Assembly requires both PDFs and checks
geometry/fonts, matching body streams and annotation counts, page labels, shifted
named destinations and print metadata. CI installs the pinned PDF helper and runs
the publishing tests. See [STANDARD-FORMATS.md](STANDARD-FORMATS.md) for the current
file contract and verification record.

Local checks passed for all **19 PDF pairs**: 4,206 print pages and 4,225 reading
pages, with unchanged print metadata/spines. Volume 0 has **239 print pages and
240 reading pages**, spine **0.5405 in**. Its full PDF/EPUB/reader pipeline and the
exact approved-image check passed. Forty publishing tests pass. The library has
nineteen distinct reading/print link pairs; desktop and 320-pixel browser checks
verify working downloads and no horizontal overflow. Evidence is under
`build/pdf-pair-review/`. Clean CI validates the combined source for every volume
and checks the complete library before publishing the 133 release assets.

---

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

## Verified correction publication

Source commit **560804e** was published by successful Actions run
[40582430929](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/40582430929).
All nineteen clean book builds, the complete-library assembly, the 114-asset
release and the actual Pages deployment step succeeded. The 34 unit tests and
browser checks passed: light/dark controls, contrast, search/filter, shared theme
preference, reader mathematics/hints and 320/390-pixel navigation.

The downloaded production Volume 0 front and paperback wrap both contain the exact
decoded original pixels. Its production EPUB and reader contain the original PNG
bytes. The deployed library and reader PNG hashes both match the approved master;
all nineteen deployed fronts were downloaded and visually inspected together.
Representative complete wraps were inspected: Volume 0 has 239 interior pages
(240 for KDP's even-page calculation), spine 0.5405 in; Volume 9 has 152 pages,
spine 0.3423 in. All retain 0.125-inch outside bleed.

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

## Volume 0 mathematical reconstruction (28 October 2026)

The author requested a substantive ten-chapter reconstruction of Mathematical
Maturity. It was implemented on editorial/volume0-reconstruction-20261028 after
preserving original commit 3259d46 and integrating pre-existing upstream publishing
changes through 8135b0b. Mathematical edits are confined to Volume 0; the established
cover identity, version-C fonts and semantic colours remain in use. Local TOC
chapter spacing is tightened to avoid an orphaned last entry without changing
body type or page geometry. The blurb/listing now describe mathematical-question
openings and the ten-chapter content.

The local final production build has a 295-page 7 × 10 premium-colour print interior
and a covered 296-page reading PDF. Its spine/wrap derive from the actual interior.
All 130 original exercises and 250 labels remain; there are now 155 complete
exercise/hint/solution triples and ten explicit bridges. Source audits, independent
review, cumulative batch reports, migration and numbering maps, exact test logs and
verification limits are in review/volume0-reconstruction/. Full PDF preflight
passes without overflow/unresolved references/missing glyphs/display shrinking;
standard package compatibility and underfull warnings remain disclosed. Other-
volume citation compatibility, historical retrieval limits, unexecuted EPUB/reader
validation and physical-proof limits are explicit. No release/Pages or KDP upload
was performed by the mathematical reconstruction.

## Volume 0 digital validation and requested push (28 October 2026)

Following the mathematical reconstruction, the author requested EPUB/HTML
validation and a push. Current main's approved cover work through 47132c3 was
merged before the complete production build. The digital converter now preserves
the Chapter-0 counter and all corresponding chapter/section/result/exercise
references; chapter-zero figure/equation numbering follows book.cls. Plain hbox
text is normalised for native MathML, avoiding four raw-TeX fallback formulas.
Normal-book and alphabetic-appendix regression coverage is retained.

The complete EPUB passes EPUBCheck 5.3.0 with zero messages. Both formats retain
299 semantic labels, 155 exercise/hint/solution triples and all 508 explicit
PDF-matched references. The assembled reader's local links/resources pass, and
all fifteen pages render in Chromium at desktop and 320 px without formula
errors or broken images; theme/menu/reveal controls and light/dark screenshots
are checked. There are 310 reveal controls and 11,817 rendered formula occurrences.
All 67 integrated publishing tests pass. Exact evidence and remaining verification
limits are in review/volume0-reconstruction/DIGITAL-VALIDATION.md. The user
explicitly authorised pushing this revision; verify the exact main build and
publication run before reporting a successful deployment.

## Volume 1 editorial reconstruction and format verification (28 October 2026)

Volume 1 now has thirteen chapters, with a separate quadratic-integer/unit
chapter before ideals and a complete local-field construction. The current
manuscript is 189 print-interior pages, 190 reading pages, with 177 numbered
pages. The approved STIX/Inter typography, semantic boxes, original figures,
native Ulam cover and premium-colour geometry are unchanged. Its regenerated
wrap uses the actual 189-page interior, even-rounded to 190 for a 0.4459-inch spine.

The complete PDF/EPUB/reader build and all 68 publishing tests pass. EPUBCheck
5.3.0 reports no issues; 17 HTML pages pass desktop and 320-pixel mobile browser
checks, including formula rendering and reader controls. Source preservation,
mathematical review, exact verification scope and remaining historical/external
review limits are recorded in review/volume1-reconstruction/. No other volume
is edited, and no KDP upload or physical proof is claimed.

The actual GitHub artifact exposed a Pandoc-version difference in portrait alternatives. A description wrapper in the digital converter/filter now preserves those alternatives across versions, with a regression that simulates an ignored graphics alt option. It does not change visible captions, figure numbers, PDF content, cover artwork or mathematical sources in other volumes.
