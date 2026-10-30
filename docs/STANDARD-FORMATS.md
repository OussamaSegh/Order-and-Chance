# Current KDP-compatible output contract

The author's confirmed working print files are now the required pipeline format.
The reading PDF is built from the original typeset manuscript and retains original
vectors, Unicode maps and navigation. The print interior is independently exported
to opaque, noninteractive PDF 1.3; print covers use opaque PDF 1.5 with vector
lettering and verified 600 ppi illustration composites only where transparency
requires them. Both PDFs preserve the same visible body and pagination, rather
than identical PDF byte streams. Existing filenames, one EPUB and 7×10 remain.

Both export reports, source/output hashes, complete visual comparisons and original
reading navigation are checked before publication. Ghostscript and pinned PyMuPDF
are build dependencies. Cache schema 8 / `library-v8-` supersede older schemas.
Source fonts, semantic boxes, mathematical content and approved latest artwork
remain unchanged. Wrap geometry follows the actual new exported print page count.

See [KDP-EXPORT.md](KDP-EXPORT.md) for mandatory steps and future-agent rules.
The earlier migration/verification records below are historical; their identical
print/read stream requirements do not override this current contract.

---

# Standard book formats

Latest decision: 27 October 2026. Applies to all sixteen main volumes and three problem books.
The author requires **two distinct PDFs: a reading download with cover, and a print interior**.
Both use the final 7 × 10 inch layout. This supersedes the earlier single-PDF decision.

## Published files

| File | Purpose |
|---|---|
| `dist/<Book>.pdf` | Reading download: approved front cover followed by the complete interior, 7 × 10 inches |
| `dist/kdp/<Book> - Print.pdf` | Print interior without the front cover, starting with the half-title; paperback manuscript |
| `dist/<Book>.epub` | Reflowable eBook with cover, MathML and diagrams |
| `dist/html/<volume>/` | Online chapter reader |
| `dist/kdp/<Book> - Paperback Cover.pdf` | Separate paperback cover with bleed and actual-print-page-derived spine |
| `dist/kdp/<Book> - eBook Cover.jpg` | Separate eBook front cover |
| `dist/kdp/<Book> - Print Metadata.json` | Print interior pages, even-rounded KDP pages, gutter, spine and wrap size |
| `dist/kdp/<Book> - Publishing Listing.md` | Title fields, description and keywords |

Both PDFs share identical typeset body pages: 11.5 pt EB Garamond/Garamond-Math with Cormorant headings, mirrored margins,
full charcoal part pages and banded chapter openers, full-colour styling and whole framed boxes. The reading PDF
has exactly one additional front-cover page; its interior labels and references
are preserved. The print file excludes that page. Never calculate a paperback
spine from the reading PDF's total count. Upload the print file as the paperback
manuscript and the wrap separately as its cover.

The reading front is uniformly scaled from the approved front PDF, preserving its
composition, embedded images and vector elements. Volume 0 retains the exact
approved image pixels, verified by `tools/check_cover_reference.py`. ISBNs,
editions, titles, subtitles, author spelling and mathematical content are preserved.

A4, fixed-page Kindle and phone PDF editions remain retired. The library's
**PDF with cover** and **Print PDF** buttons link to different files. README tables
offer both; the online reader's PDF link opens the reading download. Release assets
use the same filenames. Pages flattens the publishing files into its download root.

## Build and cache migration

- Install Python publishing helpers with `python3 -m pip install -r tools/requirements-build.txt`.
- `./build.sh [volume...]` builds both PDFs, EPUB, reader and publishing assets.
- `./build.sh --pdf-only [volume...]` refreshes both PDFs and publishing assets
  without rebuilding EPUB or HTML.
- Three TeX passes resolve references. If the print interior exceeds 700 pages,
  the larger-gutter rule is applied and the same interior is rebuilt.
- `tools/book_pdf.py` clones the entire print PDF and inserts the approved front.
  It preserves body streams, annotations, named destinations, bookmarks and metadata.
  The added front is labeled “Cover”; original interior page labels are retained.
- Output fingerprint/cache schema **5** and Actions namespace `library-v6-` force
  all books to regenerate. Each cached volume must contain both PDFs and EPUB,
  reader, front, wrap and publishing metadata. Removed books are cleared.
- Every page of both PDFs is checked at **504 × 720 pt**, with embedded fonts.
  The pair must have identical body streams, crop boxes, rotations, annotation
  counts and interior labels. Every named destination must shift by one physical
  page in the reading file. Missing covers or changed body pages fail validation.
- The print page count must agree with metadata and the calculated cover dimensions.
  The complete library passes these checks before release upload or Pages publication.

## Source adapted to the final pages

Exercises, problems, reminders, beauty notes, thinking prompts and challenges
stay whole in both PDFs. Hint and solution openings reserve space; section and
solution headings stay with the following content. Paragraph widows and orphans
are blocked, with natural bottom whitespace when needed. Long formulas are
reflowed in the source. Oversized/split frames, overflowing text or figures and
unresolved references stop the build. EPUB carries corresponding pagination
preferences, subject to the reading system's reflow.

See [the pagination review](../review/7X10-PAGINATION.md) for the print page counts
and source verification record. These print counts remain authoritative after
adding the separate reading covers.

## Verification

- **52 publishing tests pass**, including PDF cover attachment, unchanged original
  print bytes/body streams, preserved labels/metadata/bookmarks/internal and
  external links, rejection of missing covers or modified body pages, distinct
  library links, complete-library validation and cache migration.
- Existing whole-box/reference-placement typesetting tests and source layout gates
  remain in the build. Shell syntax, metadata synchronization and diff checks pass.
- Local PDF pairs and the clean all-volume publication run are checked before
  completion. The final delivery message identifies the exact published commit.
- All nineteen local pairs pass: **4,206 print pages** and **4,225 reading pages**.
  Volume 0 is 239 print pages and 240 with its cover; its spine remains 0.5405 in.
  Its approved front pixels are unchanged. The generated library has nineteen
  separate reading/print link pairs; browser checks verify their downloads and
  desktop/320-pixel layout. Evidence: `build/pdf-pair-review/`.

## Colour print and typefaces

The latest author instruction requires colour printing. Both PDFs preserve the
same full-colour interior, using 11.5/14.75 pt EB Garamond and Garamond-Math with
Cormorant Garamond headings, Fira Sans labels and DejaVu Sans Mono for Unicode code.
The licensed font files are bundled in `common/fonts/`. EPUB embeds OTF/TTF faces;
the online reader serves the same files. Reading systems may override EPUB
fonts, colours or MathML rendering.

Headings and box labels use charcoal; rules, numbers and links use coral.
Formal boxes (theorems, propositions, lemmas, corollaries, definitions, examples)
have an 8% charcoal fill under a 1.2 pt coral rule and never split; teaching boxes
(exercises/problems, reminders, prompts, beauty notes, challenges, remarks) have one
2 pt charcoal left bar, no fill, and may break. Hide the full frame; saturated
underpainting can expose stray horizontal PDF seams. Figures keep their sources; the
palette in `common/figure-palette.tex` redefines their colour names, and captions
name the new colours. See `docs/design/interior.md`. Approved cover art and
cover fonts are preserved; each print wrap uses its actual new page count.

The paperback is **Premium color ink on white paper**, 7 × 10 inches, no bleed.
This supports books down to 24 pages, including the short problem books; standard
colour starts at 72 pages. Premium-colour spines use **0.002347 inch per page**,
after even rounding. Metadata, listings, wrappers and cache validation share the
canonical settings in `common/print-layout.json`.

`check_interior_style.py` verifies actual embedded font families and charcoal/coral
PDF drawing commands, while the TeX log gate rejects missing glyphs. Tests typeset
mathematical alphabets, legacy domain notation and Unicode code, and reject an
accidental grayscale override. The extra XeTeX token memory in `build.sh` supports
the dense 3D plots with Unicode mathematics. These checks precede publication.

Public `<Book>` basenames are derived by `tools/public_names.py`, for example
`Volume 0 - Mathematical Maturity` or `Problem Book 1 - Crossroads`. Spaces
are literal on disk; shell paths are quoted and web links percent-encoded.
