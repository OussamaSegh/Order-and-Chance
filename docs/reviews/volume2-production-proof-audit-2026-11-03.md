# Volume 2 — Step 8 PDF, EPUB, online reader and paperback-wrap proof

**Date:** 3 November 2026
**PR:** [#97](https://github.com/OussamaSegh/Order-and-Chance/pull/97) (draft, unmerged)
**Production source:** GitHub Actions [Build books #1429, run 41638786729](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41638786729), pull-request head commit `4d46982b5f3db88774ac3170fcbbd43926c85044`. This is the last manuscript/metadata content commit before the Step 8 *QA tooling and audit-documentation* commits.
**Downloaded artifact:** `books-volume2-integers`, GitHub artifact ID **13232292637**, approximately 33.45 MB compressed, 104 included files. This report describes the exact generated files, not a speculative layout.

## Independent inspection of the actual artifacts

The artifact was extracted and opened outside the CI worker. All three PDFs were inspected with Poppler and PyMuPDF; EPUB and HTML assets were traversed with independent ZIP/XML/HTML parsers. Twenty-five representative reading-PDF pages—including title/copyright, all eleven numbered chapter openings, contents, part opener, formula-heavy material, the field guide, Volume 3 handoff and last pages—were rendered for visual inspection, and the full paperback wrap was rendered separately. The print output was also raster-compared with the corresponding reading-PDF body pages for a 20-page sample.

| Artifact / check | Actual independent observation | Decision |
| --- | --- | --- |
| Reading PDF | **314 pages**, 7 × 10 inches, added reading-cover page; embedded text and correct front matter; all eleven chapter heading numbers in exact printed order | **Pass** |
| KDP print interior | **313 pages**, 7 × 10 inches, **PDF 1.3**, no annotations or interactive features; all nine font subsets embedded; no missing chapters or visible sample clipping | **Pass** |
| KDP counted pages | The metadata correctly rounds **313 interior pages to 314** for KDP spine sizing; it does **not** claim a 313-page spine formula | **Pass** |
| Paperback wrap | One page, **14.987 × 10.25 inches** including 0.125-inch bleed, **0.737-inch spine**; dimensions agree with the print metadata and the supplied page-count stock factor | **Pass** |
| Print barcode | Front/back/spine cover art visually reviewed; copyright and cover say ISBN **9798167208650** (cover prints 979-8167208650); an independent high-resolution pixel scan decoded all **95 EAN-13 modules** as **9798167208650**, not merely the printed text | **Pass** |
| Cover structural preflight | Fonts embedded, lettering vector, artwork placement pixel-identical; one 600-ppi flattened illustration patch, no live transparency. Cover preflight has exact artwork source/press hashes. | **Pass** |
| Pagination / reference placement | Volume 2 build reports **383 whole boxes**, maximum height 409.9 pt, **no overflow or unresolved references**; independent sample showed no clipping or stray text on chapter openings/contents/last pages | **Pass** |
| Print/reading body parity | Compared matching reading and print raster pages (20 samples); mean RGB difference per channel below **0.02** on each, and changed-ink fraction below **0.0002**. This avoids confusing minor PDF text-extraction ligatures with visual loss. | **Pass** |
| EPUB package | ZIP integrity and uncompressed `mimetype` correct; **5,754 OPF manifest items**, all present; eleven chapters in the correct EPUB navigation order | **Pass** |
| EPUB link and formula image audit | **12,929** local asset/anchor links traversed with **zero missing targets or fragments**; all **12,185 image uses** have an alt attribute. The production log records **12,143 math instances (5,724 unique)** and 39 figure plates | **Pass** |
| EPUB exercise/solution preservation | **144 exercise, 144 hint, 144 solution** sections, matched chapter by chapter in 11 XHTML chapter files | **Pass** |
| Online HTML reader | **11 chapter pages**, four part pages and the field guide; **3,167** local asset paths resolved, no missing internal resources; **144** exercise/hint/solution triplets | **Pass** |
| Online collection homepage | The 20 per-page `../../index.html` links target the wider site-root index, assembled by the *subsequent site job* rather than copied into the per-volume artifact. Those are intentionally not treated as dead book-local links. Full site CI must pass separately. | **Await site aggregation CI** |

### Page and cover visual notes

The actual rendered sample includes reading pages **1, 4, 5, 6, 10–12, 14–15, 41, 61, 92, 119, 146, 177, 195, 219, 242, 267, 301, 308, 311–314**. Numbered chapter openings match printed chapters 1–11; notably printed Chapter 8 is **Diophantine Equations** and Chapter 9 is **Continued Fractions and Pell’s Equation**. The field-guide’s optional Volume 13 notation and immediate Volume 3 homomorphism handoff appear in the printed final pages with no observed overlap or clipped formulas. The four blank reading-PDF pages (9, 13, 265, 313) occur at front-matter, part and closing recto boundaries rather than in the middle of mathematical content.

The paperback cover was visually reviewed as a full **back / spine / front** wrap. The dark cover family, accents, barcode white field, title/subtitle, spine lettering and new 153-word back-cover text fit the page with no observed cropping. The barcode was also decoded independently from the raster at high resolution, giving the exact supplied ISBN including checksum digit 0.

### Production automation strengthened in the editorial PR

Added `review/volume2-continuity/check_volume2_outputs.py` and a conditional `QA the rendered Volume 2 PDF, EPUB, online reader and KDP wrap` job step after `./build.sh` in `.github/workflows/build.yml`. Its results are placed in `build/volume2-integers/production-output-qa.json` and the JSON is included in the regular GitHub Actions artifact. This checker was first independently trialled against the extracted artifact and **passed** on the displayed 314 / 313 / 314 page counts and exact metadata, ISBN, EPUB link/asset and exercise invariants.

The permanent gate independently checks (a) reading/print/KDP-counted pages and correct spine/bleed; (b) copyright and cover ISBN; (c) print 11-chapter order; (d) press cover fonts/vector/placement preflight; (e) EPUB ZIP, manifest, navigation, anchors, alt-bearing mathematical images, and 144 exercise/hint/solution sets; (f) online local assets and the same 144 sets. A broken resource or a silently changed paperback page count now fails the **Volume 2** build automatically. The original `list` job also runs the whole Python test suite before books build.

**CI distinction:** the independently inspected production artifact was built and uploaded **successfully** on the last content-only SHA above. Newest commits that add production regression tooling and this ledger require their **own workflow result**. Do not describe the latest PR HEAD as green merely because the earlier artifact passed.

## Remaining publisher-side gate — Step 9

Automated checks and selected-page visual inspection are not full human review of every single printed page, a Kindle-device preview, an Amazon KDP Print Previewer acceptance, or a physical paperback proof. Step 9 still requires:

- verify that the author's KDP account associates **9798167208650** with this exact paperback title, format, and edition;
- upload the **current** interior together with its **matching, 0.737-inch spine** wrap; never mix with older 307-page/308-KDP-counted exports;
- inspect KDP Print Previewer trim/safe zones, actual cover barcode and bleed, color/image reproduction, all chapter starts, exercises, mathematical diagrams and final pages;
- inspect the actual EPUB in Kindle Previewer on the intended devices and check formulas, headings, navigation and page flow;
- order and inspect a physical printed proof before treating this edition as publication-ready.

**Decision:** **Step 8 artifact and independent production-QA review passed**, conditional on the new integrated CI step passing at the latest HEAD and the full site aggregation workflow finishing green. This review **does not** authorize publication, tagging an edition or merging PR #97. Keep the PR draft and unmerged until the remaining gates are evidenced.


## Final CI closure — 3 November 2026

**The provisional CI condition above is now satisfied.** GitHub Actions
[Build books #1435](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41643856976)
completed **successfully**, with **18 jobs successful, one publish job
intentionally skipped, and no failed jobs**. The Volume 2 book build
completed, the new **QA the rendered Volume 2 PDF, EPUB, online reader
and KDP wrap** step succeeded, and the site aggregation job succeeded.

The Volume 2 log reports:

> Volume 2 cross-format QA PASS: 314 reading pages, 313 print pages,
> 314 KDP-counted pages, spine 0.737 in; 11 chapters and 144
> exercise/hint/solution triplets in EPUB and HTML

The checked output is archived as [books-volume2-integers,
artifact 13234583338](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41643856976/artifacts/13234583338).
No source, print-layout or build-checker changes have been made since
this production validation; subsequent commits contain only acceptance
documentation. **Step 8 is accepted for repository integration.**

**Publishing remains distinct.** Amazon ISBN association, KDP and Kindle
Previewer approval, and physical paperback proof are unchecked
publisher-side tasks. See
[final acceptance and author handoff](volume2-final-acceptance-and-kdp-handoff-2026-11-03.md).
This later note supersedes the provisional “CI pending” decision above,
but it does **not** authorize publication or a public edition tag.
