# Content migration and preservation

The complete unit ledger is `migration-units.json`. Each original section,
statement/example environment, proof, exercise, hint, solution, challenge, pause,
reminder and figure has its original file/line range, excerpt, hash and destination
record. Labelled material has an exact current label location; unchanged units
have hash matches; edited unlabelled units have documented source homes and must
be read with the source diff. This is provenance tracking, not a claim that a
changed proof is textually identical.

| Original material | Present home |
|---|---|
| Chapter 1 sums, induction, arithmetic, binomials, differences, workshop | Chapter 1, same source filename |
| Chapter 1 lattice paths, figure and complete Catalan triple | Chapter 2, `ch02-counting.tex` |
| Chapter 8 counting rules, pigeonhole, inclusion--exclusion and finite derangements | Chapter 2 |
| Chapter 8 stars, pigeonhole, totient, derangement recurrence, surjection and Erdős--Szekeres triples | Chapter 2, same labels, full hints and solutions |
| Chapter 8 finite probability, Bayesian workshop, eleven remaining triples and three challenge topics | Chapter 9, `ch09-probability.tex` |
| Derangement limits/error and two-panel probability figure | Chapter 9 analytic return; exact count remains Chapter 2 |
| Chapter 5 real analysis | Chapter 3, `ch05-sequences-series.tex` |
| Chapter 5 complex series extensions | Chapter 4 after complex arithmetic; real proofs retained in Chapter 3 |
| Chapter 2 complex algebra and geometry | Chapter 4, `ch02-complex-roots.tex` |
| Complex exponential series identification | Chapter 7, full `ex:taylorln(c)` proof; definition explained in Chapter 4 |
| Chapter 3 polynomial theory, examples and eighteen triples | Chapter 5, `ch03-polynomials.tex` |
| Chapter 7 linear algebra | Chapter 6, same source file; maps/rank-nullity and Gram--Schmidt moved before uses |
| Chapter 6 differentiation-rule proof parts (a),(b) | Chapter 3; Chapter 7 statement references preserved proof |
| Chapter 6 calculus, numerical methods, integrals and fifteen triples | Chapter 7, `ch06-integrals-taylor.tex` |
| Chapter 6 Gamma log-convexity statement/proof | Chapter 8, with explicit reference at former home |
| Chapter 4 inequalities and seventeen triples | Chapter 8, `ch04-inequalities.tex` |
| Chapter 4 real triangle proof | Chapter 3; Chapter 8 reminder references it |
| Chapter 4 Bernoulli induction proof | Chapter 1; Chapter 8 application context and exercise remain |
| Existing eight chapter workshops | Retained at their subject homes; new language/counting workshops added |
| Existing 24 challenge topics | Retained; proof/outlook scope clarified where necessary |
| Existing preface | Reconstructed as ten-chapter route and precise foundational contract |
| Existing field guide | Retained, updated and extended by a fully solved integrative investigation |
| Existing figures, portraits, photograph credits | Preserved; one function/fibre figure added |

There are no proposed removals of original numbered exercises, mathematical
results or assets. The retired combined counting/probability filename is a split;
its contents are accounted for above. Front-matter descriptions of the obsolete
eight-chapter architecture were intentionally replaced, with the reason stated.

Printed theorem/exercise numbers change. `NUMBERING-CONCORDANCE.md` maps all 250
original labels. `OTHER-VOLUME-CITATIONS.md` is read-only: those other manuscripts
were not independently revised. A series release must reconcile their hardcoded
numeric references using the concordance.
