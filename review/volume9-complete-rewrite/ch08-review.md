# Chapter 8 — rewrite and checking record

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: full draft rewrite; intermediate PDF-only build completed, final small
clarifications await the next complete build. Separate final review is outstanding.
This is a later checking pass by the writer, not an independent certificate.

## Coverage and preservation

Rewrote all opening prose, explanations, constructions, transitions, sixteen
formal statements and proofs, the SU2 example, remarks, beauty discussion,
ending, six original exercises, hints and complete idea/writeup solutions.
The CUE figure block and all bibliographic records remain literal.
The six theorems, six lemmas, three corollaries and one example remain in their
original counter order, including Weyl as 8.8 and the SU2 example as 8.5.
The four mathematical sections and all later section numbers are unchanged.

## Explicit mathematical corrections

- The first-column density requires n>=2. For n=1, the squared entry is the
  point mass at one. The original density expression did not describe that atom.
  The full valid n>=2 result and the exponential scaling limit are retained.
- Dyson's limiting integrand is dominated in ABSOLUTE VALUE by |h|. The original
  proof put it in [0,||h||], which failed for signed test functions. The proof
  now covers negative and complex values, including the continuous u=0 value.
- The Weyl measure proof uses |C|. Merely changing the orientation of the domain
  does not change the scalar C relating two already fixed differential forms;
  the original instruction to make C positive that way was insufficient.
- The trace-moment solution treats n=1 directly. It no longer invokes correlation
  order two at n=1, outside the stated range 1<=k<=n of that theorem.
- Repulsion suppresses close pairs and gives zero probability to exact repeated
  eigenvalues; it does not say distinct eigenvalues can never be close. The
  two-point exercise now covers all real epsilon and both angular endpoints.
- Arbitrary QR phase conventions need not ALL be biased. The text identifies
  exactly what the positive-diagonal proof guarantees, and gives a concrete
  biased convention as a new exercise rather than making a universal claim
  about numerical libraries.
- Real-symmetric, Hermitian and quaternionic Hermitian ensembles are the stated
  1/2/4 analogy. Haar orthogonal matrices are not identified with the first of
  those ensembles.
- The zeta discussion counts distinct zero INDICES with multiplicity, including
  distinct copies at an equal ordinate, instead of discarding equal ordinates.
  Full pair correlation remains conjectural. A restricted weighted Montgomery
  theorem under RH is quoted for smooth rapidly decreasing test functions with
  Fourier support inside (-1,1); no arbitrary interval-counting theorem is claimed.
  Self-adjointness alone does not force the sine-kernel spacing law.

## Prerequisites and formal checks

- Degree-zero forms, the empty wedge and empty determinant are explained. Haar
  measure on a zero-dimensional matrix group is scaled counting measure.
  Smooth positive chart densities give positivity, local finiteness and regularity.
- The modular convention was checked against Volume 8's Haar chapter: it is
  mu(Eh)=delta(h)mu(E), with affine delta=1/a. No reciprocal was substituted.
- Compactness gives absolute determinant one; connectedness is needed for the
  SIGNED form's right invariance. Both conclusions remain distinct.
- Uniqueness uses Fubini on f(yx); equality of finite Borel measures is justified
  by compact-set distance approximants and regularity. Empty sets cause no issue.
  Compact-group pushforward uses surjectivity and uniqueness explicitly.
- Gram–Schmidt is continuous on the invertible set; the triangular-unitary
  uniqueness proof has positive diagonal. Conditional Gaussian columns avoid
  every proper complex span almost surely.
- Added a local Borel eigenangle-ordering argument valid also at repeated roots:
  closed-arc root counts have closed superlevel sets by compactness of roots and
  continuity of characteristic coefficients. This makes all bounded Borel
  eigenvalue expressions used later measurable without an unstated selection
  theorem.
- Orbit construction uses Newton identities, the Hermitian spectral theorem and
  the earlier regular-value theorem. The normal gradient frame produces a
  nonvanishing invariant form, including the point orbit at n=1.
- Jacobian coordinates, denominator k-j and complex determinant |z|^2 checked.
  The constant may have either sign; all measure formulas use its absolute value.
- The sheet lemma explicitly requires a finite integer N (fixed in 66ca56fd).
  It gives N local branches over their common image and excludes extra points
  by the exact fibre count; N=0 is addressed. Constant infinite cardinality
  alone would not suffice: the disjoint union of the universal real-line cover
  of the circle with a proper open arc is a local homeomorphism with countably
  infinite fibres but no evenly covered neighborhood at an arc endpoint. Sard in equal
  dimensions makes the singular image null. Countable inverse charts and a
  disjoint Borel partition justify the global sheet integral. Fourier integration
  gives integral |V|^2=(2pi)^n n!, fixing the normalisation.
- The randomly ordered eigenvalue law follows by symmetrising arbitrary Borel
  tests; sorted angles are not incorrectly claimed to have uniform marginals.
- Andreief retains general bounded complex functions and a finite measure.
  Gaudin adds no Hermitian hypothesis to the general kernel lemma; the sign
  change upon cycle insertion and m=1 empty determinant are checked.
- Correlation sums use ordered distinct indices. Kernel quotients at coincident
  angles mean the continuous value n. All factorial factors, including k=n,
  are retained. The general compact-Lie-group Weyl formula is explicitly quoted;
  it needs general maximal-torus theory not proved here and is unused as a premise.
- The SU2 rotation-angle density comes from the uniform disc marginal and the two
  folding branches; its mean is computed by integration by parts. The entry's
  complex-Gaussian scaling statement is justified by independent uniform phase
  and bounded continuous phase-averaged tests, not only by a modulus assertion.

## Additions

Two explanatory figures follow the original CUE figure:

- `v9-ch08-jacobian-square`: multiplication by i-1 sends the unit square to
  (0,0),(-1,1),(-2,0),(-1,-1), preserving orientation and doubling area, exactly
  the j=1,k=2,t1=1,t2=i Jacobian block.
- `v9-ch08-count-variance`: the exact n=2 arc-count variance and the independent
  Bernoulli variance on p in [0,1], with correct zero endpoints and lower CUE curve.
  N_A and normalised circle measure are defined before the image.

Four two-star exercises have unique labels, hints and full solutions:

- `ex:v9-qr-phase-counterexample`: a valid QR choice constrained to SU(n), exact
  invariance proof of its SU(n) Haar law, and phase correction back to Haar U(n).
- `ex:v9-determinant-sampling`: surjective product homomorphism, its n-point fibres,
  uniform determinant and mixed Fourier orthogonality for scalar-invariant tests.
- `ex:v9-arc-variance`: full variance and disjoint covariance formulas, n=1
  separately, exact n=2 arc integral, comparison with independent points and
  endpoints p=0,1.
- `ex:v9-characteristic-polynomials`: triangular and tridiagonal Toeplitz
  determinants, polynomial recurrence with t=0,1 included, coefficient orthogonality
  and the mean characteristic polynomial. No representation theorem is assumed.

## Validation scope

Existing `check_ch08_haar.py` reports all checks passing. Its sampled data are
illustrations, not proofs. The initial six-unit PDF-only build reports 411 print
pages and no overflow or unresolved references; full exit and rendered checks
will be recorded after inspection. Small subsequent prose clarifications to the
angle-count variable, conjecture interval and Gaussian test argument require the
next build. Final EPUB, citations, exact-final-head CI and separate final review
are not claimed here.

## Actual intermediate rendered check

The PDF-only process exited 0 at **411 print pages**. It checked 589 whole boxes
(maximum 318.2 pt), with no overflow or unresolved references, and passed font,
reading-PDF, print-interior and cover preflights. Both new Chapter 8 figures were
inspected on manuscript PDF page 169, the tower photograph and repeated credits
on page 299, and the repaired generator-credit sentence on page 411.
No collision or incorrect curve/arrow orientation was visible. The original CUE
figure block still compares literally equal. The preservation checker passed
544 original labels/captions, 57 figure files, all 213 printed part/chapter/section
numbers in order and both approved cover-art sources. The next complete build
will include the subsequent small clarifications described above and the later
E/H/7 checking-pass repairs. This is not exact-final-head validation.
