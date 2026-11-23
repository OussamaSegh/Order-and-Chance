# Volume 1 publication handoff

From the repository root, activate the environment and build:

```sh
source /workspace/order-chance-system/activate.sh
./build.sh volume1-first-principles
```

The build also regenerates the wrap using the current even-rounded paperback page
count. Never combine a new interior with an older wrap. The source ISBN
**9798165526770** is preserved from the existing manuscript; its checksum is valid.
That is not independent confirmation of its registration or title association.
Verify the existing KDP account record before upload. Preserve the existing edition
and series association when revising an already published title.

| Output | Upload/use |
|---|---|
| `dist/Volume 1 - First Principles.pdf` | 7 × 10 inch reading PDF, approved front cover followed by unchanged print body |
| `dist/kdp/Volume 1 - First Principles - Print.pdf` | Paperback manuscript, premium colour ink, white paper, 7 × 10 inch trim, Bleed (PDF only). The submitted pages are 7.125 × 10.25 inches. |
| `dist/kdp/Volume 1 - First Principles - Paperback Cover.pdf` | Matching full paperback cover, 0.125-inch bleed, white-paper spine |
| `dist/Volume 1 - First Principles.epub` | Reflowable Kindle manuscript |
| `dist/kdp/Volume 1 - First Principles - eBook Cover.jpg` | 1792 × 2560 Kindle cover |
| `dist/kdp/Volume 1 - First Principles - Publishing Listing.md` | Generated details: description and seven keywords |
| `dist/html/volume1-first-principles/` | Chapter-by-chapter web reader |

Author: **SEGHAIER Oussama**. Use the title/subtitle and series fields in the generated
listing; do not invent a new title association for the existing ISBN. Photographs
have per-image print height caps to retain at least 300 effective pixels per inch.
Inspect actual output resolution, font embedding, colour diagrams, page margins,
recto title/chapter starts, copyright and barcode in the final PDF. Photo sources,
hashes and licence exceptions are in `photos/CREDITS.md` and in the book credits.

The local build and EPUBCheck do not replace Kindle Previewer, KDP Print Previewer,
account metadata checks or a physical proof. Review the interior and matching cover
together, inspect maths and image legibility on intended Kindle devices, and make
the accurate AI-content disclosures required by KDP (see `../tools/PUBLISHING.md`).
No KDP upload, release publication or Pages deployment is performed by local validation.
The [Volume 1 editorial review](../review/series-close-reading-2026-11-22.md)
records the current proof corrections and edition checks. Use the new build's
print metadata for the wrap dimensions. Earlier reconstruction and digital
validation records are in `../review/volume0-reconstruction/`.
