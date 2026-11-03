# Volume 2 continuity: initial source and prerequisite audit

Date: 2026-11-03. Branch: editorial/volume2-continuity-foundations-20261103.
Status: partial source audit, **not** a theorem-by-theorem mathematical sign-off.

## CI failure and repair

The initial PR #97 run, https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41551781706, passed the earlier source and export unit tests but failed before typesetting at the series metadata check. The new four-part main.tex disagreed with the old Volume 2 part names in common/series-catalog.json.

Repaired the canonical catalog and its cover-source SHA-256 in tools/assets/series/manifest.json. The original catalog checksum matched the existing manifest before the update. The common metadata file is a shared build input, so this change may cause CI to rebuild all fifteen volumes.

## Source-level baseline

Reviewed the eleven chapters in the approved printed order plus the preface and field guide. The inspection counted:

| Check | Result |
| --- | --- |
| Chapter sources and parts | Eleven chapters, four approved parts |
| Exercise identifiers | 144 |
| Hint identifiers | 144, in matching order |
| Solution identifiers | 144, in matching order |
| Distinct manuscript-local labels | 266 |
| Duplicate local labels | Zero |
| Missing local reference targets | Zero |
| Main-body forward reference occurrences | 15 |
| Exercise, hint, solution and other forward reference occurrences | 18 |

The 15 main-body forward references were examined in their surrounding text. They concern previews of modular inverses, continued fractions, Gaussian integers, characters and sieves; none was an explicit invocation of a later theorem as an earlier displayed proof premise. This is a **reference-context scan**, not a certification that every implicit theorem prerequisite has been found.

The 18 exercise-area forward references warrant a separate challenge audit, notably links to character-problem machinery introduced only in the final chapter.

## Repairs made during this audit

1. **Canonical book parts.** Synchronized the new part names with the series metadata and cover-manifest checksum.
2. **CRT versus sieve.** Replaced a statement incorrectly identifying the Chinese remainder theorem with the exact sieve identity. The manuscript now distinguishes CRT's reconstruction of compatible residue information from the Möbius/inclusion-exclusion formula for finite sieving.
3. **Unproved ring claim.** The Diophantine chapter referred to the Gaussian/Eisenstein chapter as though it developed arithmetic in the ring Z[sqrt(-2)]. It does not. The revised prose treats the example as beyond the local toolkit, verifies only the displayed examples, and directs broader theory to Volume 13.
4. **Stale printed numbers.** Replaced the advanced reciprocity solution's old Volume 2 Chapter 4/5 numbers with stable references to the actual orders, reciprocity and characters chapters.
5. **Wrong destination for CRT.** A challenge in divisibility incorrectly sent the reader to Volume 3 Chapter 2 for Chinese remainders; it now points to Volume 2's congruences chapter.
6. **Gauss-sum cross-reference.** An arithmetic-functions challenge now points directly to the Gauss-sum exercise instead of an obsolete numerical chapter.
7. **Regression tests.** Added source checks that require book parts and the canonical catalog to match and that find duplicate/missing manuscript-local reference targets.

## Reordering prerequisite spot-check

Arithmetic functions follows prime factorisation and congruences, and its references to characters are previews. Primitive roots uses earlier congruences and does not invoke quadratic reciprocity as a premise. The quadratic-residue chapter precedes sums-of-squares applications. The moved Diophantine chapter does not explicitly invoke results from the now-later continued-fractions chapter.

Searches through subsequent main chapter bodies did not find Hensel lifting or Chebyshev/Bertrand material being invoked as a stated prerequisite. This is only a spot-check: every implicit dependency still needs review.

## Remaining gates

- Independently audit every theorem, lemma, corollary and full proof for hypotheses, definitions and edge cases.
- Check arithmetic examples and non-elementary analytic constants, especially the Basel evaluation in coprime density, prime estimates, quadratic reciprocity signs, Pell solutions, sum-of-squares descents, norm division and Euler products.
- Review all 144 exercises, hints and solutions, including explicit signposts on challenges needing later chapters.
- Confirm every chapter-opening and transition reflects the reordered neighbours and first-reading route.
- Run complete tests and regenerate the reading PDF, EPUB and new-page-count paperback cover. Verify the ISBN 9798167208650 and matching barcode in final artifacts, not only source.
- Conduct author-side KDP title association, Print Previewer and physical proof reviews separately.

Keep PR #97 in draft. This source scan does not certify mathematical correctness, KDP acceptance or readiness to merge.

## Additional advanced-exercise dependency repair

Five Chapter 4 prompts have been signposted without deleting exercises or changing their identifiers: the coprime-density exercise points to Volume 1's Basel proof; Eisenstein's trigonometric reciprocity proof and the Euler--Jacobi liar problem explicitly require the later reciprocity chapter; the largest-prime-factor problem names the quantitative prime-distribution tool from Volume 6; and the finite-field sum-of-squares exercise defines its quadratic-symbol notation and marks the later quadratic Gauss sum and Volume 4 total-variation tool. These repairs preserve the corpus but do not yet constitute a full solution audit.
