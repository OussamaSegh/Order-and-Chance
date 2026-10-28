# Outstanding issues and limits of verification

No known unresolved mathematical defect remains from the recorded source audits
and independent review after the final fixes. This states the review outcome,
not a claim that the manuscript is error-free or formally verified.

1. **Other-volume numeric citations.** The ten-chapter reorganisation changes
   printed numbers. All original semantic labels survive, and a complete compiled
   concordance is supplied. The read-only inventory contains 314 source lines
   mentioning Volume 0 across other volumes; some are generic and some need numeric
   updates. Those manuscripts were not edited. A coordinated series publication
   must reconcile their hardcoded citations.
2. **Historical verification.** Existing sources, quotations and image credits
   were preserved. The full historical bibliography and original documents behind
   every quotation were not retrieved. Targeted Hadamard/Ramsey source checks are
   recorded in `historical-verification.json`; inherited exact anecdotes and
   quotations should receive a specialist historical proofread before a definitive
   edition. Existing photo/licence records were not independently recertified.
3. **Visual scope.** Whole-book layout/geometry/font/navigation checks are
   automated; rendered contact sheets and representative enlarged pages were
   inspected. This is not a word-for-word visual proofread at print size of every
   page, nor a physical printer's proof.
4. **Retained warnings.** Standard unicode-math compatibility warnings and
   underfull paragraph warnings remain in logs. They are not silently described
   as a zero-warning build. Overflow, missing-glyph, undefined-reference and
   automatic display-shrink checks must be clean in the final build.
5. **Formats and release.** This revision's final deliverables are PDF, source
   and QA/editorial artifacts. The revised EPUB/HTML reader was not regenerated
   or validated. No remote push, release/Pages publication or KDP upload occurred.
6. **Length.** The volume is kept below the suggested page range when the added
   mathematics is complete; no filler was added to meet a quota. Final page counts
   are measured in the compilation report, including the distinction between
   physical PDF pages and printed main-matter page labels.

All remaining items are documented follow-up or verification limits; none is
concealed behind a blanket assurance of correctness.
