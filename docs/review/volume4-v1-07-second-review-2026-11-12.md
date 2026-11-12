# Second review of V1-07

**Verdict: APPROVE**

**Issue.** V1-07, from the Volume 1 scored read. The Volume 4 bibliography credited “Volume 1, Chapter 8, for the Riemann integral, the fundamental theorem, and \(\int_0^\infty e^{-u^2}\,du=\sqrt\pi/2\).” Volume 1’s preface defines the integral as signed area and says a later volume builds that area from rectangles. Chapter 8 does contain a first fundamental theorem and the Gaussian value. Calling the whole of that the Riemann integral overstates the construction.

This note is a second reading of the repair, after the sentences were changed. It is not the writing pass.

## What was checked

- Volume 1, preface: the integral of a continuous function is the signed area under its graph. An integral over an unbounded interval is a limit of ordinary integrals. The preface says Volume 7 builds the area from the rectangles.
- Volume 1, the integrals chapter: the four rules are stated, a Riemann sum is named there as the rectangular sum, and the text says Volume 7 builds the integral from Heine’s theorem. The Gaussian evaluation \(\int_0^\infty e^{-u^2}\,du=\sqrt\pi/2\) is still in that chapter, and so is a fundamental theorem. The bibliography’s “Chapter 8” is still the right chapter for those two facts.
- The four credit sentences in Volume 4 now say “the integral as Volume 1 axiomatized it” or “signed area,” and they keep the Gaussian value. They are the collected bibliography, the Chapter 5 source list, the Chapter 5 opening, and the density definition.
- A search of Volume 4 for “Riemann integral” now hits one sentence only: changing a density at finitely many points does not alter its Riemann integrals. That sentence does not say Volume 1 constructed them. The Riemann sums in the Fubini argument, the polar-cell argument, and the later chapters are this book’s own sums. They were left as written.
- No theorem, proposition, or exercise label in `ch05-continuous.tex` moved. The source-identity test was given the new blob hash for that reason alone. It is not a new sign-off of the chapter’s proofs.

## Result

V1-07 is fixed. Nothing else in the Volume 4 scored-read logs was still open: V4R2-01 through V4R2-20 are marked fixed in the final-status table of the second scored read.
