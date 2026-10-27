# Tome 0 publication handoff

From the repository root, activate the environment and build:

```sh
source /workspace/order-chance-activate.sh
./build.sh tome0-mathematical-maturity
```

The build also regenerates the wrap using the current even-rounded paperback page
count. Never combine a new interior with an older wrap. The source ISBN
**9798165526770** is preserved from the existing manuscript; its checksum is valid.
That is not independent confirmation of its registration or title association.
Verify the existing KDP account record before upload. Preserve the existing edition
and series association when revising an already published title.

| Output | Upload/use |
|---|---|
| `dist/kdp/tome0-mathematical-maturity-print.pdf` | 6 × 9 inch paperback interior, black ink, white paper, no bleed |
| `dist/kdp/tome0-mathematical-maturity-cover-wrap.pdf` | Matching full paperback cover, 0.125-inch bleed, white-paper spine |
| `dist/tome0-mathematical-maturity.epub` | Reflowable Kindle manuscript |
| `dist/kdp/tome0-mathematical-maturity-ebook-cover.jpg` | 1600 × 2560 Kindle cover |
| `dist/kdp/tome0-mathematical-maturity-listing.md` | Generated details: description and seven keywords |
| `dist/tome0-mathematical-maturity.pdf` | A4 reading/printing edition |
| `dist/tome0-mathematical-maturity-kindle.pdf` | Fixed-page reading edition; use EPUB for reflowable Kindle upload |
| `dist/html/tome0-mathematical-maturity/` | Chapter-by-chapter web reader |

Author: **SEGHAIER Oussama**. Use the title/subtitle and series fields in the generated
listing; do not invent a new title association for the existing ISBN. Photographs
have per-image print height caps to retain at least 300 effective pixels per inch.
Inspect actual output resolution, font embedding, grayscale diagrams, page margins,
recto title/chapter starts, copyright and barcode in the final PDF. New photo
provenance, source hashes and licence exceptions are in `photos/CREDITS.md` and in
book captions/back matter. Existing historical image provenance has been retained,
not independently rediscovered for this revision.

The local build and EPUBCheck do not replace Kindle Previewer, KDP Print Previewer,
account metadata checks or a physical proof. Review the interior and matching cover
together, inspect maths and image legibility on intended Kindle devices, and make
the accurate AI-content disclosures required by KDP (see `../tools/PUBLISHING.md`).
No KDP upload, release publication or Pages deployment is performed by local validation.
The review log is `../review/TOME0-ENHANCEMENT.md`.
