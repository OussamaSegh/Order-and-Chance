# Volume 2 — Final repository acceptance and KDP handoff

> **Historical PR #97 evidence, superseded for current PR #103.** The old page counts, spine, artifact and repository acceptance below do not approve the rewritten manuscript. Current evidence and open gates: [strict ledger](volume2-independent-verification-ledger-2026-11-03.md). PR #103 remains draft, unmerged and unpublished.

**Date:** 3 November 2026  
**Editorial PR:** [#97](https://github.com/OussamaSegh/Order-and-Chance/pull/97)  
**Release state:** Manuscript/source and generated publishing files **accepted for the repository**. Amazon KDP / Kindle Previewer acceptance and a physical paperback proof are **not completed**. Do not claim the edition is on sale or approved by KDP.

## Final repository acceptance

The approved four-part, eleven-chapter reading sequence and all 144 original exercise/hint/solution triples have been preserved. The internal prerequisite, proof, mathematical example, exercise, continuity, listing and cross-format production review records are in the preceding Step 1–8 audit documents. These are internal editorial reviews, **not** independent academic mathematical refereeing.

**Exact production validation:** [Build books #1435](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41643856976) **completed successfully** with **18 successful jobs and one intentionally skipped publish job**, on commit `631c33a9723f657b2d37f715a11423bd44737781` (the Step 8 manuscript, production automation and QA documentation checkpoint). Crucially, the new **“QA the rendered Volume 2 PDF, EPUB, online reader and KDP wrap”** step succeeded. The job log reported:

> Volume 2 cross-format QA PASS: 314 reading pages, 313 print pages, 314 KDP-counted pages, spine 0.737 in; 11 chapters and 144 exercise/hint/solution triplets in EPUB and HTML

GitHub Actions artifact: [books-volume2-integers (artifact 13234583338)](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41643856976/artifacts/13234583338). Use the output of this successful workflow rather than an earlier edition's wrap when submitting to KDP.

| Publication item | Verified value or source |
| --- | --- |
| Series, volume | Order and Chance, Volume 2 |
| Title and subtitle | The Integers — Primes, Patterns and Proofs |
| Edition / author | First edition, 2026 / SEGHAIER Oussama |
| Paperback ISBN | **9798167208650** (EAN-13 check digit 0) |
| Trim / paper / colour | 7 × 10 inches; no-bleed interior; white paper, premium colour ink |
| Reading PDF | `dist/Volume 2 - The Integers.pdf`, **314 pages** (front cover included) |
| Print interior | `dist/kdp/Volume 2 - The Integers - Print.pdf`, **313 pages** |
| KDP spine count | **314** pages after even-page rounding |
| Paperback cover | `dist/kdp/Volume 2 - The Integers - Paperback Cover.pdf`; **14.987 × 10.25-inch** full wrap with bleed |
| Spine width | **0.737 inches**, matched to 314 KDP-counted pages for the selected stock |
| Kindle book | `dist/Volume 2 - The Integers.epub` |
| Kindle cover | `dist/kdp/Volume 2 - The Integers - eBook Cover.jpg` |
| Listing | `dist/kdp/Volume 2 - The Integers - Publishing Listing.md`; canonical description/keywords in `volume2-integers/kdp.md` |
| Online reader | `dist/html/volume2-integers/` |
| Machine-readable QA | `build/volume2-integers/production-output-qa.json` inside the build artifact |

The KDP interior and paperback cover **must always be submitted as a pair from the same successful run**. The ISBN is embedded on the copyright page and printed with a decoded, matching EAN-13 barcode on the paperback wrap. The cover already has a barcode: prevent KDP from superimposing another one.

## Publisher-side acceptance — author action required

- [ ] Open the existing Amazon KDP title/series record (or the correct new draft). Confirm **ISBN 9798167208650 is assigned to this exact paperback title, format and edition**. A syntactically valid ISBN or a PDF barcode does **not** establish KDP account ownership or assignment.
- [ ] Confirm that the KDP book-details fields, exact title/subtitle, contributor credit, series association, edition number, rights and AI-generated-content disclosures match the publication listing and actual content.
- [ ] Upload **the 313-page current print interior** together with its **0.737-inch spine full cover**, selecting the correct 7 × 10 trim, premium colour ink, white paper, no bleed for interior, and **“barcode already on cover.”**
- [ ] Run **KDP Print Previewer**: review trimming, safe areas, gutter, spine centering, artwork, barcode field, colour and contrast, mathematical symbols, figures, exercises, all eleven chapter openings, the final field-guide pages and any platform-specific errors or warnings.
- [ ] Upload the EPUB and corresponding eBook cover in the correct Kindle title record. Run **Kindle Previewer** on the intended screen sizes; inspect navigation, image alt/placement, displays of formulas, inline mathematics, exercise/hint/solution headings and chapter/part breaks.
- [ ] Order and inspect a **physical paperback proof**. Confirm cover/spine registration, barcode scan, colour, binding, paper, mathematics legibility, facing pages, and no cut-off text. Revise any defect, rebuild *both* interior and cover, and repeat all quality gates.
- [ ] Only after all publisher-side items pass: approve publication in KDP and record the date, edition/artifact identity and any post-publication changes. **Publishing and Amazon account actions are not part of PR #97.**

## Repository handoff decision

The repository editorial changes and automated production validation are accepted. The KDP and physical-proof tasks above are **external publishing dependencies**, not known defects in the approved source, and are deliberately left unchecked. Merging the editorial PR, if approved, is a **repository integration** and **does not** mean an Amazon upload, ISBN-assignment verification, physical-proof sign-off or public release.

If any new content or layout edit occurs after this sign-off, the manuscript and paperback cover must be regenerated together, and the exact-head CI and publishing checks repeated. This protects the page-count-dependent spine and barcode placement.

**Related records:** [implementation plan](../plan/volume2-continuity-implementation-2026-11-03.md); [prerequisite audit](volume2-prerequisite-order-audit-2026-11-03.md); [mathematics audit](volume2-mathematics-examples-audit-2026-11-03.md); [144-solution audit](volume2-exercise-solution-audit-2026-11-03.md); [reader and listing audit](volume2-reader-continuity-metadata-audit-2026-11-03.md); [production proof](volume2-production-proof-audit-2026-11-03.md).
