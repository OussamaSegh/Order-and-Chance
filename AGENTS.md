# Order and Chance: session handoff

Read `docs/DESIGN.md` before changing covers, colours, typography or publishing templates.
It records the author's approved series identity and how it is applied and checked.

## Author-approved decisions (2026-10-27)

- Series: **Order and Chance**. Author: **SEGHAIER Oussama**.
- Slogan: **Beautiful mathematics through problems and proofs.** Replaces the old
  "Number theory, algebra and probability, all proved" slogan everywhere.
- Cover reference: **docs/reference/approved-cover.jpg**, supplied by the author
  after initially choosing D. This later attachment supersedes the first D concept:
  textured burnt-orange/rust paper, large cream serif masthead, fine cream double
  border and corner ornaments, cream slogan/author, large dark book title. Apply to
  all 28 volumes, paperback wraps and ebook covers.
- Every illustration must depict mathematics from its own volume. Read
  `docs/COVER-MOTIFS.md`; keep the illustrated constructions mathematically correct.
- Coordinate interior and online colours with the cover. Keep paperback interior
  accents grayscale for black-ink printing and preserve mathematical distinctions in figures.
- Record substantial decisions, implementation details, validation and outstanding
  work in the repository so future sessions can continue from evidence.

## Working conventions

- Read the current git status and fetch the latest `main` before editing; other
  writing sessions can update the repository. Preserve their work.
- Phone PDFs were retired by a concurrent author session (2026-10-27); production
  now includes A4 and Kindle PDFs plus EPUB. Notebook execution is manual. Preserve this.
- Shared cover templates and `common/design-colors.tex` are the source of the design;
  avoid per-volume copies or rasterising the mathematical diagrams.
- CI caches complete book outputs using `tools/build_plan.py`; shared cover assets
  in `tools/assets/` must participate in book fingerprints.
- `build.sh` produces reading PDFs, EPUB, ebook covers, paperback interiors/wraps,
  KDP listings and online readers. Pushing `main` triggers all-volume builds and
  publication through `.github/workflows/build.yml`.
- Review representative rendered output and all cover title lengths after layout changes.
  A source change or queued workflow is not evidence that live downloads are updated.
- Preserve author spelling, volume identifiers, ISBNs, edition metadata, mathematical
  contents, figure meanings and cross-volume references during design-only work.
