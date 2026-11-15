# Chapter 6 writer record

Complete rewrite of the chapter, including all fourteen original formal numbered statements and six original exercises, every proof, calculation and example, all hints and idea/writeup solutions, short formula introductions, historical prose and ending. The original bibliography is retained verbatim. The entire original cubic figure block, caption and label are retained verbatim. Original section headings, their order, and all original labels are preserved.

## Mathematical and prerequisite repairs

- **V10-C06-01 — forward dependency in `ex:sixtwice`.** The original proves Z[sqrt(−5)] Dedekind by citing the later `thm:intclosure` and later `lem:trace`. The rewrite gives a direct proof at the example: a finite Z-module gives Noetherianity; integral-extension dimension gives dimension one; conjugation and normality of Z make trace and norm integral; the reduced-denominator and mod-4 argument puts the integral element in Z[sqrt(−5)]. No theorem conclusion is weakened. All four prime-ideal identities and nonprincipality of all three primes are also proved there rather than used from a later exercise.
- **V10-C06-02 — primitive-element prerequisite in `thm:intclosure`.** Volume 3 Theorem 8.20 is for subfields of C. The theorem here allows arbitrary characteristic finite separable extensions. The rewrite supplies the finite-bad-coefficient proof locally in an infinite K, using a common splitting field and a linear gcd, and then iterates. Scaling the resulting generator is justified by an explicit monic-equation denominator argument. The separability and all original conclusions remain.
- **V10-C06-03 — cubic normality before ideal factorisation.** The original Numbers and curves argument invokes Dedekind factorisation without proving normality for a general squarefree cubic, referring elsewhere to the later specialised exercise. The rewrite proves normality by trace/norm and squarefree denominators before factorisation. It separately handles a vertical line over a root of g, where the repeated point has ideal exponent two. The chord-and-tangent group law and stronger class-group bijection remain explicitly unproved previews, not premises.
- Define v(0)=+∞ so the valuation inequality covers cancellation x+y=0. Handle zero in integral-closure arguments and the zero ideal separately from nonzero fractional ideal factorisation.
- Expand the full Dedekind equivalence proof, especially its three-part (d)⇒(c) cancellation argument; no new condition is inserted into the theorem.
- Explain finite-generation in the local inverse-colon identity, why inverse-colon is fractional, and where the dimension hypothesis enters the DVR proof.
- Cover the unit/empty-prime-list case of the two-generator proposition with b=0.
- In the fundamental identity, prove pS proper using lying over, finite residue degrees from module finiteness, each consecutive prime-power layer one-dimensional, and why localisation does not change S/pS.
- Mark Claborn and Krull–Akizuki as quoted advanced results; neither is used as a premise. Class-number finiteness and Galois prime transitivity are later-volume previews. The supplied problem on the real circle explicitly retains its given Dedekind-domain assumption, as the original permits.

Fixing commits for these repairs will be identified by the parent integration ledger. No false original numbered theorem in Chapter 6 was found; the repairs concern proof completeness, prerequisite order and boundary explanations.

## Prerequisites actually checked

Actual Volume 3 statements checked with the current statement walker: Theorem 6.9 (ring CRT), Theorem 6.14 (PID⇒UFD), Theorem 7.6 (finitely generated PID modules), Theorem 8.2 (tower law), Theorem 8.20 (restricted primitive element theorem). Also inspected the actual proof and restriction in `ch08-extensions.tex`, the zero-ring/domain convention in `ch06-rings.tex`, and Chapter 4's `prop:noethmodules`. The Vandermonde reference follows the actual earlier Volume 1 Proposition 7.4. No later volume supplies a proof premise.

## Additions

- Two mathematical illustrations, after the last original figure: valuation-coordinate sums/intersections; three Gaussian prime-splitting patterns separating residue degree and ramification. Each has unique label, explanatory prose and caption.
- Four appended exercises, each with fresh label, rating, hint and full idea/writeup solution: arithmetic of two ideal valuations; invertible ideals as projective modules; Gaussian primes 2/3/5; noninvertibility in the cusp ring K[t²,t³].

## Source checks actually run

- All twenty original formal/exercise kind-label pairs remain in the same order, with four exercises added at the end.
- All original labels retained; whole original figure block byte-identical.
- Original section heading sequence identical.
- Counts: 3 figures, 10 exercises, 10 hints, 10 solutions (original: 1,6,6,6).
- No build, numerical script or rendered artifact inspection was run by this writing agent. Parent owns production and visual checks. Separate mathematical/editorial review is still required; this is a writer record.
