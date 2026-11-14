# Appendix E — rewrite and checking record

Status: full draft rewrite; PDF-only build passed; rendered additions inspected. Final-volume independent
review and EPUB validation remain outstanding. This is a later checking pass
by the writer, not an independent verification certificate.

## Coverage and preservation

Rewrote all introduction, exposition, transitions, eleven formal statements and
proofs, twelve original exercises, hints and idea/writeup solutions, the beauty
passage, the quoted-results discussion and the closing bridge. The epigraph,
three original figure blocks and bibliography records are retained literally.
The original six mathematical sections and the Exercises/Hints/Solutions sections
retain their order, numbers and labels. No original formal environment is added
or removed; no numbered equation is introduced.

## Mathematical checking pass

- Polarisation uses characteristic !=2 throughout. Congruence is distinguished
  from an arbitrary matrix operation. The nondegenerate-subspace complement
  proof remains valid even if the ambient form is degenerate.
- Orthogonal-basis induction explicitly includes dimension zero and the zero
  form. Sylvester's maximal-dimension argument includes zero coefficients and
  p=0 or m=0. Equivalence by signature specifies a fixed ambient dimension.
- Projective forms are nonzero and scalar multiplication preserves their zero
  sets. The projective no-line argument uses a two-dimensional zero subspace.
- The affine normal-form proof checks the invertible case's Schur determinant,
  excludes c'=0 by nondegeneracy, and proves rank(M)>=2 in the singular case.
  The new height variable is specified directly. The two hyperboloids are
  distinguished by explicit connected parametrisations, not a drawing.
- The Segre parametrisation is well-defined in projective coordinates and unique
  by row/column spaces. The no-other-lines proof tests the rank of the sum using
  vectors dual to two independent rows. Both ruling intersection clauses remain.
- Hyperbolic-plane splitting normalises beta(e,f')=1 and computes q(f)=0 exactly.
  Reflections have nonzero denominators and square to the identity. The two-
  reflection lemma handles u=v. Witt cancellation allows degenerate residual
  forms and separately handles a zero-dimensional cancelled form.
- Witt decomposition terminates by dimension and uses anisotropy for uniqueness.
  The zero-dimensional anisotropic remainder is allowed.
- Finite-field isotropy counts both sets including zero and has a nonzero final
  coordinate. The point counts remove the zero vector before dividing by q-1.
  Both split and anisotropic binary residual cases are checked.

## Explicit corrections and completed solutions

- The Gram determinant solution previously chose a k-dimensional subspace of R^n
  even for k>n. It now treats dependent families first, including k>n, and gives
  the empty-family convention as well.
- The binary-discriminant solution previously identified degenerate zero
  directions with finite double roots without handling a=0. The new solution
  gives finite and infinite projective roots, including linear/constant
  polynomials and the identically zero form.
- 'All conics' is made consistent with the earlier definition by specifying
  nonzero defining forms. The zero polynomial defines the whole plane and is
  explicitly discussed rather than silently forgotten.
- The skew-lines solution now proves the rank-three cone assertion using the
  nondegenerate quotient and dim(U)<=dim(U-perp); rank-one and rank-two cases
  split over the algebraic closure. It explains that skewness survives extension.
  The final substitution is a polynomial identity because K is infinite.
- Hasse--Minkowski is explicitly quoted and unused, rather than an implicit
  prerequisite. The finite-field opening now correctly says anisotropic forms
  cannot have three or more variables, rather than 'small' anisotropic forms.

## Additions

Two new illustrations follow all three original figures:

- `v9-app-e-polarisation`: exact u=(2,0), v=(1,1), with squared norms 4,2,10
  and mixed difference 4; arrows and dashed sum construction checked.
- `v9-app-e-projective-grid`: the sixteen incidence points of the F3 split
  quadric, two families of four lines, each of four points. The caption states
  that it is an incidence array, not a Euclidean model.

Four exercises follow the original twelve and have unique labels, two-star
ratings, hints and complete idea/writeup solutions:

- `geometry:ex:v9-schur-complement`: exact block congruence, positive-definite
  criterion and c>5/6 threshold with the boundary signature.
- `geometry:ex:v9-maximal-isotropic`: upper bound by two injective projections
  and a matching constructed subspace, including radical dimensions.
- `geometry:ex:v9-finite-tangent-plane`: counts 2q+1 versus one using the induced
  binary form; proves the tangent-plane equation locally.
- `geometry:ex:v9-rulings-under-map`: separate actions on column/row coordinates,
  transposition swaps families, and the full pointwise-fixing criterion for the
  stated maps. The scalar test uses three distinct projective points available
  over every field under the appendix's characteristic assumption.

No new proof uses a result from a later printed unit. Numerical checks are not
used to establish any theorem. Build, preservation and rendered checks will be
recorded after they finish.

## Actual intermediate validation

The three-unit PDF-only build exited 0 at **397 print pages**. It checked 577
whole boxes with maximum height 318.2 pt; no overflow or unresolved references
were reported. Fonts, reading-PDF equivalence, print interior, bleed and covers
passed their checks. All 544 original printed labels and captions and all 57
original figure files passed preservation. The two new Appendix E figures were
inspected on rendered manuscript PDF pages 300 and 301; labels, values, ruling
colours and captions were legible, with no visible collision. Original source
figure blocks also compare literally equal. `git diff --check` passed.
This is not a full EPUB build, exact-final-head CI or final review certificate.
