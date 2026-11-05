# V3-012a — complex representation prerequisites, partial chapter checkpoint

This is a coherent foundation repair, not completion of Chapter11. Its ten named
results and eleven exercises remain pending full supplied-solution/adversarial
closure. Main source and every prompt were read; first solutions were recorded
before hints/answers. All hints and the first four complete answers have since
been read (pairs, one-dimensional, A4, central/Q8); the remaining answers and
entire figure source still need comparison. No Chapter11 register approval yet.

Actual V1 ch07 `thm:gramschmidt` and `thm:spectral` full proofs were read. They
concern real inner-product spaces and real symmetric matrices. The old C11
reference to that spectral theorem did not earn a complex unitary eigenbasis.
The correction defines Hermitian products with the linear-first convention,
proves complex Gram–Schmidt by checking each coefficient and positive denominator,
and constructs W-perpendicular by extending its basis to V. Zero spaces and empty
bases are included. A second reconstruction checks the coordinate projector's
image/kernel/idempotence and direct sum, with no spectral theorem needed.

The finite-order unitary result is earned locally: C7's squarefree-annihilator
criterion gives an eigenbasis; invariance makes distinct unit-modulus eigenspaces
orthogonal; local Gram–Schmidt within each produces an orthonormal eigenbasis.
An adversarial check expands λ conjugate(μ) and verifies it differs from1 exactly
when λ≠μ, with no division by an unproved positive norm or zero eigenvalue.

The chapter now explicitly fixes finite G and finite complex dimension. Dimension0
is allowed for subrepresentations/empty finite sets; irreducibles must be nonzero.
The decomposition proof discards zero summands and terminates by positive integer
dimensions. A two-by-two unipotent action in characteristic p shows why a
stable complement may fail when p divides group order; all possible complement
generators(a,1) are tested directly in the general proof.

The multiplicity proof now bounds the number of irreducibles by orthogonality
in a finite-dimensional class-function space before choosing a full list. It
does not silently treat the theorem's initial partial list as complete. The
Fourier paragraph earns radix-two complexity through its finite recurrence.
Dirichlet's filter is first an exact finite prime-sum identity; analytic series
and Euler products are clearly later outlook. A stale quotient reference and
hard-coded exercise number were corrected.

`check_chapter11.py` currently checks foundations only: exact complex C4 powers,
the invariant averaged Hermitian form and its conjugate-linearity/orthogonal
eigenvectors, plus the modular counterexample. Its source/prerequisite contract
gate fails on the old source and passes on the repair. This is a regression,
not mathematical certification from matching source strings. The internal unit
suite has15 focused tests including C1–10 evidence guards; full-suite result is
recorded in PROGRESS.md. Source changes reopen relevant evidence.

Next: continue actual supplied solutions from ex:circulant in printed order,
then independent second checks, all character/table data, history and the complete
Frobenius–Schur problem. CH11-PROMPT-FIRST.md contains a proposed finite signed
involution model to earn the quoted symmetric-group reality theorem and degree
sum without an unproved premise; it still needs adversarial proof/computation
and source attribution. Do not insert or approve it from this checkpoint alone.
