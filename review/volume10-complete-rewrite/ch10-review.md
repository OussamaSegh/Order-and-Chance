# Chapter 10 separate mathematical and editorial source review

Reviewer: `rewrite_ch05_ch06`, separate from the Chapter 10 writer. This reviewer wrote Chapters5–6. Starting main: `59014a9aad3454ad60786c6549c81fcac88df9df`. The review reads the entire source and every mathematical argument; it does not claim human certification, a build, rendered-artifact inspection or CI success.

Final reviewed chapter SHA-256: `87b864a110a09767b7ebaa366c08c714d1e354c46c2df7d9f5523de03ca551a0`. Both new figure hashes are recorded in `ch10-statement-review.json`.

## Coverage and preservation

Read all prose, including short clauses and formula introductions, historical text, definitions and statements, complete proofs, examples and calculations, every original and added exercise/hint/idea-writeup solution, reading guidance and ending. Compared every one of the sixteen original formal statements and six original exercises against full baseline content. `ch10-statement-review.json` records a concrete individual judgement for each and for all four added exercises.

The original kind/label order is unchanged. All original labels remain, including the three numbered equations `eq:frecur`, `eq:hooksum`, `eq:hooktarget` in order. The entire original hook figure block and its caption are exact; the original figure source matches its baseline hash. Total counts are three figures and ten exercises/hints/solutions, adding exactly two explanatory diagrams and four complete exercises. Compiled numbering and visual placement are owned by the parent.

## Mathematics and prerequisites

- Specht construction is complete over the chapter's complex field. The dominance cell count, antisymmetrizer cancellation, row-by-row column matching and self-adjoint inner-product argument prove the stated submodule alternatives. Nonzero polytabloids, pairwise inequivalent shapes and exhaustion are earned before the dimension argument; the earlier character class-count theorem is the only counting premise.
- Standard-polytabloid independence uses a legitimate tabloid order on the rows of descending labels. The largest moved label can move only upwards in its original column. Distinct standard tableaux give distinct leading tabloids. No unproved straightening theorem is assumed.
- Forward insertion preserves rows, columns and Young shape, and weakly decreases bumping columns. Reverse insertion chooses the rightmost smaller entry; the same-column entry above guarantees existence and the reverse path moves weakly rightward. Entries below a changed cell exceed the replacement or are absent. Both inverse directions are checked, so arbitrary pairs of tableaux, not just pairs already produced by insertion, are covered. The sum-of-squares then proves dimensions without circularity.
- Schensted's minimal-ending-value invariant handles length1 and empty input. Its first row need not itself be a subsequence, as the 31452 example correctly explains. The decreasing companion theorem is quoted, and the patience solution proves Erdős–Szekeres without using it.
- Hook walk: finite right/down moves terminate at corners. For a fixed target corner the whole upper-left rectangle exists. The prescribed visited-set probability is explicitly conditional on its start; its first-step recurrence has the correct numerator identity and zero numerators for missing boundary moves. The factor1/n occurs once at the final average. Empty/one-cell shapes and all positive denominators are handled, proving the hook recursion exactly.
- Transposition-character coefficient calculation handles same-row, same-column and distinct-row/column swaps exhaustively. A column permutation contributing to the last case would fix every other label, leaving only1 or that invalid swap. The content and row/column formulas agree. n≥2 states the valid transposition domain explicitly; conjugate tableau counts retain their full n≥1 scope.
- Every old and new exercise, hint and solution was checked. Catalan bracket inversion, all S4/S5 degrees and characters, two-row boundary cases, the local standard decomposition and multiplicity proof, the missing-hook difference partition, Gram/action computations, four-cell conditional probabilities, exact n=4 LIS distribution and all eleven S6 degree/content entries are correct. The complete eigenvalue1/5 multiplicity is125, and conjugation gives the same at−1/5.

Actual earlier sources inspected: Volume3's Maschke, Schur, row/column orthogonality, degree sum and class-count results; the current Chapter9 induction/Wedderburn constructions and its permutation-module norm argument. All are available before use. No later exercise, compact-group formula or later-volume limit theorem is a proof premise. Young's rule, modular classification, sign twist and asymptotic laws are explicitly quoted.

The writer's substantive corrections are warranted: the modular simple quotients are not an open classification problem; distinct shapes may have coincident central scalars; and the cover is the snake lemma, not a Plancherel diagram. The original complex numbered conclusions are retained. The explicit empty-partition convention and n≥2 ratio domain clarify actual boundary meaning without discarding a valid case.

## Review finding and recheck

The quoted limit-shape formula Ω uses Russian coordinates, not a bare orthonormal45° rotation of a diagram scaled by1/√n. Parent repaired the prose in `ee5c8ac6` to give u=(x−y)/√n and v=(x+y)/√n and the additional √2 factor. Exact final source rechecked: the Ω formula and its stated |u|≤2 range now agree with those coordinates.

Both new figure sources were checked mathematically. For31452, P=125/34 and Q=134/25; the final corner carries4 in P and time5 in Q, and reverse bump ejects2, leaving145/3. In the(3,1) hook walk, the three first moves each have probability1/3, conditional corner probabilities are2/3 and1/3, and averaging the four starts leaves the same values. Caption orientation and labels match the text.

No remaining source-level blocker was found at the recorded hashes. Rendered pages/figure label overlap, EPUB content and final production are separate parent checks.
