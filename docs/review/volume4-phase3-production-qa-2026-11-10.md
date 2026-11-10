# Volume 4 Phase 3 — production and device QA

**Date:** 10 November 2026.
**Reviewer:** the designated validator (an AI reviewer).
**Book tree:** `cfe5d152a8aa2bc74b7b96f5824369a86e175b92`, which is identical to merged `main` `3cc07e8673490b9922db9d9d29fee0551e2d8a12` (`git diff` between those commits is empty).
**Artifacts inspected:** native QA run [42783238907](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42783238907), artifact `volume4-native-42783238907`. Downloaded and opened locally with PyMuPDF 1.26.6 and Pillow. This is software inspection of the built files, not a Kindle, a phone, or a printed proof.

## What the workflows actually did

Native QA job `volume4-native` on head `cfe5d152`: every executed step succeeded, including EPUB alt-text tests, `./build.sh volume4-chance`, and the digest step. The “install TeX if cache is absent” step was skipped because the cache hit.

Build books run [42783238606](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42783238606), same head:

| Job | Result |
| --- | --- |
| list | success, 42s |
| debs | success |
| build (volume4-chance) | success, 13m52s, including pagination tests, KDP export tests, the book build, and the bleed check |
| site | success, 10m49s. The snapshot step printed PASS for print preflight and the shared cover family for Volumes 1–15, including Volume 4 |
| publish | skipped, zero steps. Pull requests do not publish |

## Files that were opened

| File | SHA-256 | Bytes |
| --- | --- | --- |
| `dist/Volume 4 - Chance.pdf` | `25b31d7b8b5237840accfec664a573deadfefd9bf7cb766bd42e7e7e1b2db8a7` | 3988168 |
| `dist/Volume 4 - Chance.epub` | `dc1162354d9234f316563e5a70eeb2a45219d7d81f078482b2753dfcc87ff410` | 18968245 |
| `dist/kdp/Volume 4 - Chance - Print.pdf` | `5fa5e477e2b02f1c8770671eeb0d2749c131c8a066a4e63bc7879aea7b7bc937` | 8531492 |
| `dist/kdp/Volume 4 - Chance - Paperback Cover.pdf` | `c106eb4bce59e945a4207f5ea065077964ea8765f7a72773029d5b46d44e261f` | 2885131 |
| `dist/kdp/Volume 4 - Chance - Print Metadata.json` | `b118d9b7aca5821a9913d0249b353a832fdc77f9c43c02035a8a1847591d46f2` | 385 |

## Geometry, fonts, and preflight

- Reading PDF: 290 pages, every page 504 × 720 pt (7 × 10 in). The extra page relative to the print interior is the attached front cover.
- Print PDF: 289 pages, every page 513 × 738 pt (7.125 × 10.25 in). `kdp-preflight.json` records schema 2, PDF 1.3, `interior_bleed: true`, 289 pages, flattening at 600 ppi, and full-page charcoal backgrounds on pages 13, 69, 161 and 255.
- Cover preflight: pass. Embedded fonts, vector lettering, no live transparency, native paper at least 300 ppi (observed 360), one illustration patch at 600 ppi, exact art pixels.
- Embedded font families seen in the files include EB Garamond, Garamond Math, Cormorant Garamond, Fira Sans, and DejaVu Sans Mono, as subsets. No missing-font substitution was reported by the build.

## The three corrected plates, as rendered

Text search of both PDFs finds the new wording and does not find the old “blue” ink labels.

| Plate | Reading page | What was seen |
| --- | --- | --- |
| Poisson clock, Figure 10.1 | 205 | Caption: “original arrival points (charcoal)”. The drawing’s own words are “charcoal: an original arrival” and “rust: an arrival kept after thinning”. Kept marks are a subset of the arrival marks. The old phrase “blue: an original arrival” is absent. |
| M/M/1 rates, Figure 10.3 | 211 | Legend: “rust: customer arrival” and “charcoal: completed service”. Rust arrows point right and are labelled \(\lambda\). Charcoal arrows point left and are labelled \(\mu\). There is no service arrow out of state 0. |
| Brownian reflection, Figure 12.1 | 249 | Caption, wrapped across two lines: “The first hit is marked by a black point. The charcoal continuation and the rust continuation are exact mirror images”. The drawing labels “original tail” and “reflected tail”. The paths mirror across the barrier. “blue continuation” is absent. |

The same caption strings are in the print PDF one page earlier (204, 210, 248), which is the coverless interior.

EPUB: 18.97 MB, under 50 MB. HTML contains “original arrival points (charcoal)” and “marked by a black point” and “The charcoal continuation”, and does not contain the retired blue ink phrases. 10,642 `alt` attributes, none empty. 42 PNGs are at least 1600 pixels wide (the plates, at the pipeline’s 1800-pixel target, plus one other wide image). The thousands of narrower PNGs are formula images named `oc-math-*`, which is the EPUB math pipeline, not a shrunken plate.

## Not done

No Kindle, no physical paperback, and no KDP previewer was used. A second build on `main` after the merge, run [42786721619](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42786721619), is the integration rebuild of this same tree. Its artifact hashes are recorded in the release-candidate manifest only if that run’s files were downloaded. PDF identifiers can differ between two builds of one tree; the hashes above are the files that were opened.
