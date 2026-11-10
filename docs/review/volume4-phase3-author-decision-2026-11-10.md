# Volume 4 Phase 3 — author decision report

**Date:** 10 November 2026.
**From:** the designated validator (an AI reviewer).

## Author approval

At 11:37 Europe/Paris the author wrote: “Yes you merge and publish, then go to next phase, dont wait for me.”

The published source is `22e9d49410eb95dad6d505c1e568a21b7fd4d828`. The release is https://github.com/OussamaSegh/Order-and-Chance/releases/tag/books , tag `books`, title “Books (latest build)”, from Build books run 42806203843. The site https://oussamasegh.github.io/Order-and-Chance/ lists Volume 4: Chance. Downloaded Volume 4 asset SHA-256 values match the release digests; they are in `docs/review/volume4-phase3-release-candidate.json`.

KDP still needs the author’s account. Upload `Volume 4 - Chance - Print.pdf` (`b7ff97461a4afe2838aeccf2a84ce9bf7cd6cd82dfd2b4a5d93847485e57ae50`) and `Volume 4 - Chance - Paperback Cover.pdf` (`10ed0d4d4c3f6c05e65dac9a72828cee9156774cd6b209de2b81cac264ff07ab`).

No numbered phase follows Phase F of `docs/plan/volume4-excellence-execution-plan-2026-11-08.md`. The series content plan’s next floor is Book 5 (`docs/plan/book-05.md`). `docs/plan/PROGRESS.md` tracks Volume 1 only. None of those documents opens a phase, so none was started.

## Earlier candidate note

The text below was written before the approval, when the book was still a candidate.

Volume 4 can be treated as a **release candidate**, not as a finished publication.

The candidate tree is `main` `3cc07e8673490b9922db9d9d29fee0551e2d8a12` (squash of #140). It is the same tree as pull-request head `cfe5d152a8aa2bc74b7b96f5824369a86e175b92`. Phase 2’s mathematical signoff still covers the proofs: the only manuscript edits since that signoff are two captions and two in-figure ink words. Checksums of the files that were opened are in `docs/review/volume4-phase3-release-candidate.json`.

## What is done

- Source audit of all 41 referenced figures. Three called charcoal ink “blue”. Those words are corrected and were seen in the built reading PDF, the print PDF, and the EPUB.
- Chapter-by-chapter reading for teaching defects, recorded in `docs/review/volume4-phase3-pedagogy-2026-11-10.md`. No critical teaching defect was demonstrated, so no further chapter edit was made.
- DEP-12 through DEP-29 are still in the unpublished volumes, and Volumes 1–3 were not edited.
- Build books and native QA succeeded on the exact head that was merged. The pull-request `publish` job was skipped.

## What the author still has to decide

1. **Whether to publish.** Candidate status is not a yes. No physical Kindle or paperback was checked.
2. **Pull requests left open on purpose:**
   - [#141](https://github.com/OussamaSegh/Order-and-Chance/pull/141) Volume 6. Theorem 2.11 does not exist; the Poisson limit is Theorem 2.1. The short-interval tail \(2e^{-\delta^2\mu/3}\) is now derived in the solution. It is not a Volume 4 theorem, and Hoeffding’s exponent does not cover every \(\lambda>2\).
   - [#142](https://github.com/OussamaSegh/Order-and-Chance/pull/142) Volume 5. The odd reciprocal squares are no longer credited to a monotone-convergence theorem Volume 4 does not have.
   - [#143](https://github.com/OussamaSegh/Order-and-Chance/pull/143) Volume 11. Pólya’s uniform limit is Volume 4, Theorem 11.13, not Theorem 10.21.
3. **Tonelli, left untouched.** In Volume 5, the solution of `ex:ritelli` still equates two iterated integrals by naming Tonelli. Volume 4 does not prove Tonelli. #142 does not change that sentence. Whether to replace the name with a local argument is an author decision.
4. **The preface’s prerequisite line.** It says the reader needs high-school mathematics and Volumes 1–3. The proof citations checked in this pass point at Volume 1. Volumes 2 and 3 are described as useful, not as cited theorems. Changing the bold sentence would change the promise on the page. It was not changed.
5. **Issue #139.** The tracking issue exists, but editing it and commenting returned HTTP 403. The handoff and the pull-request descriptions are the record that could be updated.

## Rolling library build

Merging #140 pushed `3cc07e86` to `main` and started Build books [42786721619](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42786721619). That workflow, when the library snapshot changes, updates the existing rolling “books” release. That update is the repository’s ordinary library build. It was not given a final-release title, and it is not a KDP upload.
