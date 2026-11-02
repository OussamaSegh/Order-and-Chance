# Volume 1 — KDP first-edition publication gate (2 November 2026)

**Book:** *First Principles: Proof, Problem Solving and Mathematical Thinking*, Volume 1 of *Order and Chance: The Hidden Architecture of Mathematics*.
**Review baseline:** `main` at `dcb96455d9f68d58da8b5e35e782facea5cfc794`; this PR changes the publishing listing and adds this review note, not the mathematical manuscript.

## Editorial and mathematical record

- The final full-PDF review in `docs/reviews/volume1-final-grok-review.md` identified two mathematical mistakes and a short list of local accuracy/teaching issues. The repairs in PR #74 were assessed again in `docs/reviews/volume1-step14-rereview.md`; PR #79 completed the PDF text-layer and launch-image-licence corrections.
- PR #92 (merged into this baseline) audited the first-reading dependency contract: Volume 1 needs secondary-school mathematics and its stated assumptions; Volume 2 needs only Volume 1. It explicitly introduces groups and subgroups before roots of unity and repairs the main-text Stirling and Gaussian-integral proof dependencies.
- A fresh structural pass over the **current** eleven chapter sources plus preface, field guide and image credits counted **192 exercises, 192 hints, 192 solutions**, **452 distinct labels** and **937 internal references**, with **no duplicate labels or unresolved local references** in these sources. No `TODO`, `FIXME` or placeholder markers were found in these files.
- The baseline's **push-triggered** GitHub Actions run [41417592531](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41417592531) completed successfully, including `build (volume1-first-principles)` and `publish`. The subsequent workflow-dispatch run [41435711950](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41435711950) succeeded but rebuilt only the site; its `build` and `publish` jobs were skipped and must not be cited as a fresh manuscript build.
- The source sets `First edition, 2026` in `main.tex`; `tools/listing.py` specifies KDP edition **1**, the correct series and subtitle, the English language, a 7-by-10-inch paperback, premium colour on white paper, and no interior bleed.

This evidence supports a mature publication candidate. The present check does **not** represent a new independent, line-by-line proof of every theorem and all 192 exercise solutions; the previous detailed source reviews and CI are real evidence but not a formal guarantee. Nor does a green CI job alone verify appearance on a physical Kindle or printed book.

## KDP copy changes

- Replaced the listing's example-only description with a reader-oriented narrative: the cube identity, the hats problem, intended high-school entry level, core material, the three-star exercises and complete hints/solutions.
- Introduced the **15-volume series**, its path from proofs to arithmetic, symmetry, probability, analysis, geometry, deeper randomness and number theory, and the handoff to Volume 2, *The Integers*.
- Description is **2,288 characters**, below the 4,000-character repository/KDP limit; all seven keyword phrases are below 50 characters.
- The paperback back cover (`blurb.tex`) and the mathematical manuscript are intentionally untouched.

## Publication blockers / vendor checks still required

1. **ISBN association:** `main.tex` includes `9798165526770`. `PUBLISHING.md` says its checksum is valid but expressly does not verify KDP registration or association with this edition. Confirm it belongs to the corresponding paperback entry in the actual publisher account before distributing final print files.
2. **KDP Print Previewer:** Upload the **matching** newly exported paperback interior and wrap, inspect their bleed, page count/spine, margins, font/diagram readability, image quality, copyright and barcode, and resolve any KDP upload warnings. Do not substitute the downloadable reading PDF.
3. **Kindle Previewer:** Upload the regenerated EPUB and matching eBook front; inspect formula baselines, figures, headings, navigation, and legibility on the intended Kindle viewport.
4. **Proof and rights:** A physical paperback proof and final verification of image acknowledgments are strongly recommended. The earlier noncommercial SpaceX photograph was removed in PR #79; the present photo credit file lists the remaining original source/licence qualifications.
5. **Account details:** Confirm title/subtitle, series volume 1, author, first edition, existing ISBN, paperback settings, territories/rights, and accurate AI-generated-content declarations before publication.

**Decision:** The manuscript and revised KDP copy pass the source/CI gates recorded above. **Do not treat this as confirmation of a KDP-accepted first edition.** The edition tag must remain pending until the ISBN association and final KDP vendor previews are confirmed, with any necessary corrections merged into `main`. When approved, place an immutable tag named `volume1-first-edition` on that exact final `main` commit (not this review branch); include the corresponding revision and uploaded PDF/EPUB hashes in the publication log.
