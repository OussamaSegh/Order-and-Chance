# Chapter 11 writer record

Complete rewrite of the introduction, explanations, all ten numbered statements,
proofs, calculations, six original exercises, six hints and six idea/writeup
solutions, ending and reading guidance. Literal Weyl quotation, bibliography and
complete original weight-diagram block remain unchanged. No statement/section
counter changes. Added two figures after the original figure and four exercises
with difficulty, hints and full solutions after the respective original lists.

New figures: two-row Young-diagram growth and exact power-trace variances for U(4).
New exercises: Laurent linear-statistic variance; central-weight obstruction and
positive balanced determinant/trace moments; descent to PU(n); first missing
Gaussian radial moment and finite-size tail bounds. All use earlier printed tools.

## Explicit mathematical corrections

- The original finite-size prose said a trace at size 1000 is exactly Gaussian
  'whatever the size'. The exact variance is 1; Gaussian behavior is a limit.
  Finite support |trU|≤n contradicts an exact Gaussian law. The limit theorem
  itself is preserved unchanged.
- Schur orthogonality now chooses one representative per isomorphism class,
  making the displayed cases exhaustive. Equivalent realizations require matching
  bases; the coefficient formula is not basis-free across arbitrary realizations.
- Trace-moment parameter a is explicitly a nonnegative integer, as the permutation
  and tableau statement requires. The empty permutation handles a=0.
- Original dimension exercise retains symmetric/exterior calculations at n=1;
  its adjoint-weight request explicitly requires n≥2. Exterior powers use 0≤k≤n.
- SU(2) exercise specifies integer m≥0 and continuous values at 0,π. The domino
  solution explicitly handles first-row/second-row boundary cases and determinant
  shifts for negative weights.
- General compact-group Peter–Weyl extension is honestly quoted, not attributed
  to the matrix-group Stone–Weierstrass proof. The theorem's existing global
  matrix-group scope is preserved. Sphere followup is explained via stabilizers.
- Supplied local alternant proofs for exterior/symmetric-power characters before
  using their irreducibility. Distinguished quoted hook-content and Schur–Weyl
  formulas from proved character consequences. Zeta-moment predictions remain
  conjectural and require the arithmetic factor.

Actually inspected Volume 7 Stone–Weierstrass 4.19; Volume 8 circle-character 13.11;
Volume 6 Gaussian-moment lemma 9.6 and its smoothing proof; Volume 9's integration
and group material (also separately checked by reviewer). No later-volume theorem
is a premise. The independent reviewer read the entire new chapter and found two
stray exponent commas, an ambiguous moment caption and an unnecessarily restricted
n=1 task; all corrected before commit. Source math checked; no rendered inspection
or successful final build is claimed in this writer record.

Fixing commit: supplied in final correction ledger after integration.

## Integrated fixing commits

c9f0258a. These commits fix the original problems and prerequisite gaps
listed above; separate review records distinguish any additional draft-only fixes.
