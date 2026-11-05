# Actual earlier printed order and reopened reference evidence

Internal AI review,5November2026. Reopened the actual V1 main.tex30–56 and
V2 main.tex mainmatter inputs. A source basename is not a printed chapter number.

| Actual source basename | V1 printed chapter |
| --- | --- |
| ch00-language | 0 |
| ch01-sums | 1 |
| ch02-counting | 2 |
| ch05-sequences-series | 3 |
| orders | 4 |
| ch02-complex-roots | 5 |
| ch03-polynomials | 6 |
| ch07-linear-algebra | 7 |
| ch06-integrals-taylor | 8 |
| ch04-inequalities | 9 |
| ch09-probability | 10 |

V2 source ch09-diophantine prints8, ch08-continued-fractions prints9, and
ch14-characters prints11. Its other ch01–07 and ch10 numbers agree with their
basenames. The source-order regression reads the actual mainmatter sequence
and chapter commands, not titles inferred from filenames. Both actual main.tex
files now have hashes in prerequisite-sources.json so structural drift is caught.

At V3-014 I introduced three reader-facing Chapter5 references for V1 sequence
criteria by following the basename. This was a review error. Their actual
source proofs were read and correctly reconstructed, but the printed locator
was wrong. All three become Chapter3. The C Ramsey discussion now points to
printed V1 Chapter10 and reconstructs its expected-count argument locally.
Actual V1 ex:ramsey solution812–824 was reopened before doing so.

The two affected accepted A rows (linear:thm:perron and
linear:ex:pagerankrate) were explicitly reopened by the hash checker, then
rechecked. Reread actual Perron proof63–190 and PageRank solution1304–1350.
Programmatically verify that the entire old1b948 A source changes only by
the three literal Chapter5->3 substitutions. Reconstruct the same finite
Delta/K maximization/strict defect/Jordan argument and independent phase/
left-weight check; reconstruct the PageRank zero-sum contraction and Cauchy
tail/limit/uniqueness argument again. The actual V1 prop:seqcrit bounded-
subsequence and Cauchy proofs246–265 and their source bytes are unchanged.
New statement/related-proof/answer hashes are retained; only the explicitly
reviewed mathematical evidence fields are re-entered. No blind status or
visual evidence transfer occurs.

The whole-volume scan /tmp/volume3-earlier-reference-scan.txt has80 explicit
earlier-volume occurrences. It reveals additional stale V1 reader chapter
numbers in the previously read main route. These are still open for the global
context/prerequisite pass: roots/complex5, polynomials6, linear7, sequences3,
probability10 and sums1 must be checked against every actual cited argument.
Do not report that global reconciliation complete or infer concept availability
from this numbering table. All unreferenced uses still require manual review.
