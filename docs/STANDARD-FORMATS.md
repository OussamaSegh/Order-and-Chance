# Standard book formats

Decision: 27 October 2026. Applies to all sixteen main volumes and three problem books.

## Published files

| File | Purpose |
|---|---|
| `dist/<tome>.pdf` | Sole standard book PDF, 7 × 10 inches; also the paperback manuscript |
| `dist/<tome>.epub` | Reflowable eBook with cover, MathML and vector diagrams |
| `dist/html/<tome>/` | Online chapter reader |
| `dist/kdp/<tome>-cover-wrap.pdf` | Separate paperback cover with bleed and actual-page-derived spine |
| `dist/kdp/<tome>-ebook-cover.jpg` | Separate eBook front cover |
| `dist/kdp/<tome>-print-metadata.json` | Actual PDF pages, even-rounded KDP pages, gutter, spine and wrap size |
| `dist/kdp/<tome>-listing.md` | Title fields, description and keywords |

The PDF starts with the half-title and uses the existing 11 pt Palatino book
layout, mirrored margins and recto chapter openings. Its black-ink styling and
scientific figure distinctions are preserved. Covers remain separate so this
same PDF can be uploaded as the paperback interior. ISBNs, editions, titles,
subtitles, author spelling and mathematical content are unchanged.

There is no A4, fixed-page Kindle, phone or duplicate `-print.pdf` edition. The
old `dist/<tome>.pdf` A4 filename now contains the canonical 7×10 PDF. All download
buttons, README links and reader PDF links use this file. The publishing panel's
paperback-interior link points to the same file.

## Build and cache migration

- `./build.sh [tome...]` builds the standard PDF, EPUB, reader and publishing assets.
- `./build.sh --pdf-only [tome...]` refreshes that same PDF and publishing assets
  without rebuilding EPUB or HTML. The former `--print-only` option is retired.
- The TeX preamble defaults directly to 7×10; it contains no A4, phone or Kindle
  layout branch. The existing layout hooks remain for volume-specific typography.
- Three TeX passes resolve references. If the actual PDF exceeds 700 pages, the
  existing larger-gutter rule is applied and the same layout is rebuilt.
- Front previews now check the two supported cover proportions: standard book
  front and EPUB front. Removed reading formats have no front-preview jobs.
- Output fingerprint/cache schema 3 and Actions namespace `library-v3-` force a
  complete rebuild. The TeX package cache remains reusable.
- Cache assembly removes retired PDF variants from both flat downloads and KDP
  directories. It also removes deleted books across a cache schema migration.
- Before a snapshot or release, every canonical PDF is checked page by page at
  **504 × 720 pt**, with embedded vector fonts. Its actual page count must agree
  with the print metadata and calculated wrap dimensions. Retired PDF files or
  incomplete book outputs prevent publication.
- The complete library is validated before uploading the combined books artifact.
  Release notes now describe one PDF and one EPUB per volume.

## Verification

- **26 publishing tests pass**, including stale-output cleanup, old-cache migration,
  rejection of an A4 PDF under the canonical filename, metadata disagreement,
  library completeness, download links, EPUB anchors and MathML.
- `bash -n build.sh`, metadata synchronization and `git diff --check` pass.
- Volume 0 and Higher Structures fronts pass title/subtitle/slogan extraction,
  exact size and embedded-font checks in both supported proportions.
- Volume 0 completed the full PDF/EPUB/reader pipeline. Its 233-page standard PDF
  has identical extracted text to the reviewed paperback; the EPUB ZIP and MathML
  checks pass. Other volumes are rebuilt and checked during the rollout.
- Local builds and the clean all-volume publication run are checked as part of
  the rollout. The final completion message identifies the published commit and
  confirms the exact Actions run; local output alone is not publication evidence.

Earlier trim comparisons and review records describe their formats at the time.
This document and the current author instructions supersede their format policy.
