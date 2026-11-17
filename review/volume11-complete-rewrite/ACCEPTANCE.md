# Volume 11 complete rewrite — acceptance record

**Manuscript source head examined:** `4f9e15e6e3ce70a5900da9450ad5db3aaceb908c` (PR #247).
**Basis:** immutable baseline `b005c4a0a33409f443594f3bb1efe3e955e95468`.
**Review:** author-side mathematical/editorial review and exact-source production-output inspection. This is **not** a claim of independent third-party proof certification.

## Source preservation and mathematical review

- The original 14 printed chapters, 182 formal statements, 110 exercises/problems and 30 figure environments remain, in printed order. The revised manuscript contains **166 exercises/problems and 58 figure environments**, including 56 additional solved exercises with hints and 28 new mathematical figures. Existing artwork is untouched.
- The branch-specific immutable-baseline regression, the original chapter numerical checks, the new 14-group arithmetic/enumeration checks and the inbound/outbound Volume 11 cross-volume citation check passed on the final manuscript source: [audit run 43825324375](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43825324375).
- A second author-side reading covered the newly added exercise solutions and selected high-risk original arguments. Confirmed fixes included the gamma Lévy-measure shape factor and drift convention, the Poisson factorial-moment recursion, the Brownian embedding hypotheses, convex-distance support subtleties, Ville's maximal inequality, Kakutani's equivalent-marginals case, integer shuffle times, the coarse transposition spectral bound and the actual likelihood-ratio argument for the shuffled Gaussian limit. Original structural preservation and a passing numerical suite are not, by themselves, proofs of correctness.
- Published Volumes 1–3 and accepted Volume 10 have not been edited by this PR. The Volume 10 downstream citation fixes in PR #246 were incorporated through PR #248.

## Production build and rendered-output QA

[Production run 43825324374](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43825324374) **succeeded** on the same manuscript source. Publishing preflight, the Volume 11 build and the site/build output validation passed. The `publish` job is appropriately skipped on a pull request (publishing only happens on `main`).

The following release-candidate artifacts were downloaded and checked directly, rather than inferred from green CI.

| Output | Result |
| --- | --- |
| Reading PDF | 314 pages, including the approved front cover; 7 × 10 in; extractable text and valid PDF metadata |
| Paperback interior PDF | 313 pages; 7.125 × 10.25 in with bleed; PDF 1.3; page count and KDP preflight correct |
| EPUB | ZIP CRC passes; valid `application/epub+zip` mimetype and manifest; 22 spine documents; all 26 XML-like documents parse |
| EPUB resources | 13,385 local resources links checked, **0 missing**; 1,080 XHTML anchor links, **0 unresolved**; 12,305 image elements, **0 without alt attributes** |
| Layout and figures | Reading-PDF text blocks remain inside the page edges; reviewed cover, preface, part page, regular proof and exercises, and 17 figure-heavy pages distributed across chapters; figures and captions visibly legible |
| Print parity | 227/313 pages have byte-equivalent whitespace-normalized extracted text; another 83 have >99% text similarity (minor export glyph shifts). The three 600-ppi-flattened pages are print pages 124, 179 and 202: images were visually compared against the corresponding reading pages and preserve their content. |

Reading PDF SHA-256: `476bb5bebaff875f448d30386f8df7cf1d769c6cc0082eaedb2ce18bddd7e81f`.

Print PDF SHA-256: `7ce003e7f37e8dc36a4e6a82a3c7c29544c666b46952b3bd3bc43f92a9dc8b2b`.

EPUB SHA-256: `6ab85b2e1029dfefa2e1aeb109396730ffa763907648f518241a1b0c409eb70d`.

## Acceptance and limitations

**Decision: accept and merge PR #247, subject to successful integration and publishing workflow on `main`.** This decision is an author-side signoff supported by preserved numbering, mathematical corrections, reproducible regressions, successful full production outputs and directly inspected artifacts.

A genuinely independent external mathematical or editorial reviewer has **not** certified all 182 formal statements. The final record does not imply that automated checks or this author-side review constitute such certification. If that higher standard is required for formal publication approval, it must be obtained separately. This user-directed merge proceeds with the limitation disclosed.

After the merge, check the `main` Build books run, release assets and publication results; record any platform-only failure separately.
