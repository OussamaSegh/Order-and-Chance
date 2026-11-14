# Chapter 7 — rewrite and checking record

Status: full draft rewrite; PDF-only build passed; added figures inspected. The separate final independent
review and complete EPUB validation are outstanding. This is a subsequent checking
pass by the writer, not an independent certificate.

## Coverage and preservation

Rewrote the opening, all exposition and transitions, definition, eight labelled
formal statements and their proofs, beauty passage, remarks, ending, six original
exercises, hints and full idea/writeup solutions. The original ball-model figure
block and bibliography records are literal. Section order, labels and formal
counter increments are unchanged. The two new figures follow the original figure;
four new exercises follow all six original exercises.

## Explicit corrections

- The spin theorem's full-turn clause now requires a UNIT axis vector. The old
  statement omitted it while the proof assumed it; u=0 gives a constant loop and
  nonunit lengths can represent different winding counts or fail to close.
- The rotation-commutation exercise now separates the identity, which commutes
  with every rotation without an axis restriction. The proof covers nonidentity
  rotations with common axes and perpendicular half-turn exceptions.
- Zero angular velocity has every positive period and no least positive period;
  the formula 2pi/omega is used only for omega>0. L(0)'s fixed space is not
  incorrectly described as R*0.
- O(n)'s two-component claim is for n>=1; the exercise explicitly treats n=0
  as the one-element group. The closed-subgroup proof itself allows zero-
  dimensional Lie algebras, including finite groups.
- Repaired the closed-subgroup proof's neighbourhood identification: first
  exclude all small nonzero transverse exponentials, then use a product chart.
  Membership in G forces the transverse coordinate to vanish. The final ambient
  neighbourhood is explicitly the direct-sum product, avoiding a shrink that
  changed one side of a claimed equality without changing the other.
- The SL2 polar solution now gives the exact formula
  P=(A^T A+I)/sqrt(tr(A^T A)+2), with a direct Cayley–Hamilton check.
  Positive determinant-one matrices are parametrised by a>0,b real and
  bottom-right entry (1+b^2)/a. Positivity follows from an explicit completed
  square. This removes the contour-functional-calculus and global matrix-log
  continuity gaps without appealing to the later quadratic-forms appendix.
- The spin discussion distinguishes a spatial rotation from its path and a
  global state-vector sign from an observable relative phase. A neutron
  interference pattern shifts; its nonnegative intensity does not 'flip sign'.
- The Heisenberg solution supplies an exact operator calculation on complex
  polynomials and the finite-dimensional trace obstruction. The three-by-three
  matrix generators are not misidentified as finite-dimensional quantum
  position and momentum satisfying a nonzero scalar commutator.

## Formal statement and proof checks

- Logarithm: norm ranges, absolute series composition and the c=2 tail bound
  checked. Differential at zero is the identity before using inverse function.
- One-parameter subgroup: no differentiability is assumed; dyadic agreement is
  proved with the logarithm's injectivity range, then extended by continuity.
- Lie product/commutator limits: logarithmic errors become O(1/m) after powers.
  All approximants lie in G; the limits are invertible, so relative closedness
  suffices. Negative bracket parameters are supplied by exchanging X,Y.
- Closed subgroup: compact unit sphere is used only when the transverse space
  is nonzero. Large integer powers work for every fixed positive or negative t.
  The product chart, tangent slice, translated charts and restricted smooth
  operations are checked, including a zero-dimensional source slice.
- Homomorphisms: define generators by one-parameter subgroups first, prove
  homogeneity and additivity, then bracket preservation; smoothness follows
  from finite-dimensional linearity and local charts, avoiding circular use of
  a differential before smoothness. Uniqueness uses scaling and derivatives.
- Connected generation: the generated subgroup is open and its other cosets
  are open. Connectedness implies equality and gives differential uniqueness.
- Spin: Pauli products, real positive trace inner product, determinant sign,
  surjectivity, scalar kernel, compact/Hausdorff quotient, S3 simple connectivity
  and path-lifting obstruction checked. The two-turn contraction is projected
  explicitly from the covering sphere.
- Torus: normal spectral decomposition gives exponential surjectivity. A regular
  diagonal matrix has coordinate-line eigenspaces; this proves both centraliser
  and maximality. The normaliser's unique coordinate permutation gives its
  quotient, and repeated eigenvalues are included in conjugacy classification.

The general Spin(n) construction, Hilbert's fifth-problem theorem and the
non-matrix universal cover of SL2 remain explicitly quoted, unused extensions.
The Hilbert-fifth statement includes Hausdorff and second-countable assumptions.

## Additions

- `v9-ch07-spin-lift`: parameter diagram recording I,-I,I above I,I,I. Its
  caption says it is schematic, so repeated endpoint labels are not distinct
  group elements at a geometric distance.
- `v9-ch07-affine-product`: translation then dilation takes 0 to 2, while
  dilation then translation takes 0 to 1, with arrow order checked.

Four two-star exercises have unique labels, hints and complete solutions:

- `ex:v9-rodrigues`: triple-product formula, exponential, trace and recovery of
  the axis/angle, with zero and pi handled before dividing by sin(theta).
- `ex:v9-circle-homomorphisms`: periodicity forces integer differential slopes;
  brackets and connectedness make SU2-to-circle homomorphisms trivial.
- `ex:v9-affine-exponential`: relative closedness, algebra/bracket, full
  exponential and inverse, including the removable s=0 expression.
- `ex:v9-spin-traces`: exact adjoint trace relation, half-turn preimage S2,
  and all integer loop classes, including zero and negative turn counts.

No proof or solution needs a later chapter or appendix. The old group numerical
script was run successfully; its checks are illustrations rather than proofs.
Build and rendered verification will be recorded after completion.

## Actual intermediate validation

The five-unit PDF-only build exited 0 at **407 print pages**. It checked 586
whole boxes (maximum 318.2 pt), with no overflow or unresolved references, and
passed font, reading-PDF, print and cover preflights. Both new figures were
inspected on rendered manuscript PDF page 145: path endpoints, arrow order,
labels and captions were legible and mathematically consistent. The original
figure block still compares literally equal.

The preservation checker passed all 544 original labels and captions, 57
original figure files, all 213 printed part/chapter/section numbers in order,
and both approved cover artwork source files. The checker now enforces the
latter two requirements; a nested-title/unnumbered-entry parser probe passed
and a deliberately altered section number was detected. `git diff --check`
passed. The build began before the later cover-credit phrase repair; its
colophon is not claimed to validate that subsequent wording change. Full EPUB,
separate final review and exact-final-head CI remain outstanding.

A later checking pass supplied the intermediate three-factor commutator expansion
and explicitly used invariant orthogonal complements in the SO(n) block proof,
covering repeated eigenvalues without a hidden choice of real eigenbasis.
These clarifications await the subsequent complete build.
