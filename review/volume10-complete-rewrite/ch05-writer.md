# Chapter 5 writer record

Complete chapter rewrite, including each definition and numbered statement, every proof, examples, original exercises, all six original hints and idea/writeup solutions, opening and ending, and formula introductions. Literal bibliographic records and the entire original Figure 5.1 block are preserved. The original chapter section headings remain in their order (their printed numbers are checked by the parent build).

## Mathematical correction

- **V10-C05-01 — Noether normalisation, `thm:noethernorm`.** The original states the theorem for every finitely generated K-algebra, while zero rings are permitted by the series. The zero K-algebra cannot contain even the polynomial ring on an empty list, K: its structure map has kernel K. The corrected statement explicitly assumes A≠0. This also repairs the proof's claim that a nonzero constant cannot vanish in A. Every conclusion for a nonzero algebra is retained. Fixing commit: parent integration commit, to be filled in its correction ledger.

## Proof and prerequisite repairs

- Give the zero-divisor example Z/6 localised at powers of 2 and an actual check of the equivalence relation, rather than calling construction checks routine.
- Expand the tensor/localisation proof, including the common-denominator reduction, exactness at ends and naturality.
- Explain minimal generator lists with Nakayama, including the zero module and the necessity of finite generation.
- Handle the zero ring explicitly in the local-zero criterion, empty spectrum, local-ring exercise and nilradical exercise. Krull dimension on an empty spectrum is declared −∞, making the integral-extension dimension statement precise.
- Supply the short upper-bound argument for dim Z[x]=2, not just one chain giving a lower bound.
- Explain that normalisation is surjective with finite fibres on prime spectra; an ordinary K-point interpretation requires algebraically closed K. R⊂C warns against surjectivity on real points. No numbered conclusion is weakened.
- Correct the containment typo in the irreducible-implies-primary proof: the other ideal would be strictly *larger* than I.
- Expand the colon-ideal proof of associated-prime invariance and minimal-prime statements, accounting for the empty indexing set.
- The hyperbola solution proves x+y transcendental and gives both exceptional double fibres s=±2. The real-spectrum exercise explicitly distinguishes a set bijection from Euclidean topology.

Actual earlier prerequisites consulted: Volume 3 ring/zero-ring convention, UFD/Gauss results, PID structure, ring Chinese remainder theorem; Volume 7's Zorn statement; Chapter 4 Noetherian module/basis theorem and weak Nullstellensatz; the tensor construction from Chapter 3. No result from Volumes 11–15 is used as a premise. References to later arithmetic are labelled as prospective applications.

## Additions

- Figures `v10-new-ch05-local` (surviving primes of Z_(3)) and `v10-new-ch05-primary` (monomial obstruction in (x²,xy)). Both are after the last original figure and have mathematical captions and prose references.
- Four appended exercises: primary torsion components of Z/60; nilpotents and an unchanged spectrum; normalisation of K[u²,u³]; nonuniqueness of an embedded primary component. Each has unique label, difficulty, hint and complete idea/writeup solution.

## Checks actually run

- Source comparison: every original label remains; the complete original figure block is byte-identical.
- Numbered-environment comparison: original kind/label sequence preserved, followed by four exercises.
- Counts: 3 figures, 10 exercises, 10 hints, 10 solutions (original counts: 1,6,6,6).
- No build or rendered-page review was run by this writing agent. Parent owns builds, printed-number checks and visual review. These source checks do not replace separate review.

## Integrated fixing commits

291af767. These commits fix the original problems and prerequisite gaps
listed above; separate review records distinguish any additional draft-only fixes.
