# Content migration plan

All 205 original labels and all 97 original exercises/hints/solutions must survive. `baseline-inventory.json` enumerates every section, result, definition, worked example, proof, exercise, hint, solution, teaching box and figure. `migration-units.json` records exact unchanged units or current semantic-label/target destinations; revised unlabelled prose requires the file diff and the mapping below.

| Original source | Destination / disposition |
|---|---|
| ch01-divisibility | Retained, including subgroup/ideal viewpoint and all 11 exercises. Exercise n2n gets a self-contained proof of its Fermat input. |
| ch02-primes | Retained, including sieve, Chebyshev and Bertrand and all 10 exercises. |
| ch03-congruences | Retained as chapter 3; receives counting proof of totient divisor sum. |
| ch04-arithmetic-functions | Same filename, now chapter 6. Label prop:phisum and its counting proof move to chapter 3; Möbius inversion consequence stays here. |
| ch05-primitive-roots | Same filename, chapter 4; its totient prerequisite now established in 3. |
| ch06-quadratic-reciprocity | Same filename, chapter 5; both proofs and seven exercises retained. |
| ch07-sums-of-squares | Chapter 7, all proofs/exercises/figures retained. |
| ch08-continued-fractions | Chapter 8, all retained; uniqueness demonstration becomes available before periodicity as well as in its exercise. |
| ch09-diophantine | Chapter 9, all retained and grouped by methods. |
| ch10-gaussian-eisenstein | Chapter 10, three original rings and cubic Fermat descent retained. |
| ch11-algebraic, through units | Chapter 11 in original filename, plus original ringint/goldenunit exercises and their complete triples. |
| ch11-algebraic, from Kummer ideals onward | New ch12-ideals.tex, including all six other original exercises (sqrt10 remains here because its conclusion uses the class number) and complete triples, all ideal theorems and figures. |
| ch12-padic | Original filename, chapter 13; construction and foundational explanations strengthened. |
| preface, field-guide | Updated in place; historical credits and valid references retained. |
| all figures/photos | Retain paths and bytes unless a documented mathematical correction requires a specific change. |

No mathematical result, exercise, hint, solution, challenge or bibliography entry is proposed for removal. Replaced inaccurate/stale prose is documented in the correction log. Other volumes are untouched; final numbering concordance records the consequences of restructuring.
