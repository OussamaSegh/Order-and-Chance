# Book 8 — Analysis

*Operators, Spectra and Transforms.* The on-disk subtitle is "Limits, Measures and Transformations".

**Element.** The beams. A function is a point. A beam of infinite dimension has a spectrum, and the spectrum is not always a list of eigenvalues.

**Source.** `tome8-analysis`. Ten chapters plus `chapters/ch11-harder.tex`, the former Machinery chapter on Hilbert space, input from `main.tex`. About 178 pages before that chapter. The October review scored the ten chapters 7. Wiener's local inverse now uses \(e^{+2\pi i\xi_0 x}\) in `ch10-tauberian.tex`. The blurb still has to be checked against the compact spectral theorem: the review found it claiming the unbounded case.

## Promise

Book 7 built the rooms. This floor asks what lives in them. Hahn–Banach and the three consequences of Baire, Hilbert space, compact operators, the Fourier transform, distributions, finite abelian Fourier analysis, Haar measure and the adèles, a second complex-analysis course, and tauberian theorems. Ikehara's theorem is a second proof of the prime number theorem, carried by a different beam from Book 6's. The zeros are not yet a spectrum. The book says so.

## Prerequisites

Book 7 entire. Book 5's Fourier series and complex analysis. Book 3's groups, for finite Fourier analysis and Haar measure. Book 6's zero-free line, quoted and not reproved.

## How the subtitle is delivered

The parts keep their catalog names. *Operators, Spectra and Transforms* is what they do.

Banach and Hilbert Spaces delivers the operators: Hahn–Banach, the duals, and the geometry of a Hilbert space. Spectral Theory delivers the spectra. It holds the compact spectral theorem, and it receives the matrix spectral theorem, the singular-value decomposition, the graph spectra, the semicircle, and the sine kernel. Those are spectra. They are not the geometry of a path. Fourier and Tauberian Methods delivers the transforms: Fourier analysis on the line and on finite abelian groups, Haar measure and Pontryagin duality as the measure that makes a group Fourier transform, Mellin inversion, and Ikehara's theorem. The problem chapter on zeta off the line stays here. It does not prove Bohr–Jessen. No part is renamed.

**Moves out.**

| Material | File | Where it goes |
| --- | --- | --- |
| Construction of \(\mathbb Q_p\) and the adèles, beyond Haar measure and the dual | `ch08-haar.tex` | Book 13, Chapters 6 and 9. Haar measure and Pontryagin duality stay in Fourier and Tauberian Methods. |
| Jordan's curve theorem | `ch09-complex.tex` | Book 7, Metric and Topological Spaces. |
| The Riemann mapping theorem | `ch09-complex.tex` | Book 9, Groups and Geometry. A conformal map is a connection of shapes. |
| Phragmén–Lindelöf, Hadamard factorisation, Dixon | the same file | KEEP in Fourier and Tauberian Methods. They are the engine of Dirichlet series and Mellin inversion. |

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Banach and Hilbert Spaces | 1–2 |
| II | Spectral Theory | 3–4, the spectral appendices from Book 3, and the random-matrix and graph spectra from Book 12 |
| III | Fourier and Tauberian Methods | 5–7, Haar and Pontryagin from Chapter 8, Mellin and the tauberian theorems from Chapters 9–10, and the zeta problems |

---

The chapter notes follow the manuscript's file order. The part names are the table above. Material marked MOVE leaves Fourier and Tauberian Methods.

### Part I. Banach and Hilbert Spaces

#### Chapter 1. Banach Spaces

**Status.** REVISE — `tome8-analysis/chapters/ch01-banach.tex` (476 lines). Write the complex \(L^p\) dual with the real-part reconstruction already used for Hahn–Banach. The real proof is complete. The sentence "apply the real case to the real and imaginary parts" is not that reconstruction.

**Hook.** In infinite dimension the unit ball is not compact, a linear map can be discontinuous, and a sequence of unit vectors can converge weakly to zero.

**Synopsis.** Normed spaces, bounded operators, analytic and geometric Hahn–Banach, the three consequences of Baire, the duals of the classical spaces, and weak topologies. Infinite dimension is not more of the same. That sentence is the floor's thesis, and the chapter proves the three ways it fails.

**Proved.** Hahn–Banach. Uniform boundedness, the open mapping theorem, and the closed graph theorem. \(L^p\) duality for \(1\le p<\infty\), real and, after the revision, complex. Riesz–Markov for real \(C(K)\), or the citation to Book 7 if that is where the positive theorem lives.

**Examples.** A discontinuous linear functional using a Hamel basis, with the axiom of choice named. The dual of \(c_0\).

**Figures.** Two.

#### Chapter 2. Hilbert Spaces

**Status.** KEEP — `chapters/ch02-hilbert.tex` (412 lines).

**Hook.** Pythagoras holds for functions. Fourier coefficients are coordinates.

**Synopsis.** Inner products, the projection theorem, Riesz representation, orthonormal bases, Fourier series as Hilbert expansions, orthogonal polynomials, averages along orbits, von Neumann's proof of Radon–Nikodym, and reproducing-kernel Hilbert spaces. The reproducing kernel is the member the Machinery cover once pointed at, and this chapter is its home. Book 12's Gaussian processes use the same geometry.

**Proved.** Orthogonal projection. Riesz representation. The existence of an orthonormal basis. Parseval for a Hilbert basis. Von Neumann's proof of Radon–Nikodym, as a second proof beside Book 7's, and the text should say it is a second proof.

**Examples.** The Fourier basis of \(L^2(\mathbb T)\). One projection onto a subspace of polynomials.

**Figures.** Three.

### Part II. Spectral Theory

#### Chapter 3. Operators, Spectra and Banach Algebras

**Status.** KEEP — `chapters/ch03-operators.tex` (372 lines).

**Hook.** A matrix is understood through its eigenvalues. An operator on an infinite-dimensional space may have none, and it still has a spectrum.

**Synopsis.** Adjoints, compact operators, the Fredholm alternative, the spectrum, Gelfand's theory of commutative Banach algebras, and Wiener's lemma in its first form. The spectrum is a beam's stiffness, not a list. Emptiness of the point spectrum is the surprise.

**Proved.** The Fredholm alternative for compact operators. Non-emptiness of the spectrum of an element of a Banach algebra. Gelfand–Mazur. Wiener's lemma for absolutely convergent Fourier series, or the form the chapter proves before Chapter 10's tauberian Wiener theorem.

**Examples.** The shift, with no eigenvalues and a spectrum the unit disc or the circle, as the chapter computes it. A compact integral operator.

**Figures.** Two.

#### Chapter 4. The Spectral Theorem

**Status.** REVISE — `chapters/ch04-spectral.tex` (559 lines). The compact self-adjoint theorem and the continuous functional calculus are proved. The projection-valued measure and the unbounded theorem are sent to Reed–Simon. The public blurb must say that, and it must not say "every theorem is proved in full" if the blurb still claims the unbounded case. Courant–Fischer's "word for word" sentence should match the min-max orientation the proof uses. Exercise 5.3 on Bochner, if it lives in the next chapter, states that the converse is not proved; keep that honesty next to whatever this chapter says about functional calculus.

**Hook.** A symmetric matrix is a list of stretches in the right axes. The same is true of a compact self-adjoint operator, and one can hear a string.

**Synopsis.** Self-adjoint operators, the compact spectral theorem, min-max, Sturm–Liouville, Hilbert–Schmidt operators, Mercer, and the continuous functional calculus. The vibrating string is the picture. The unbounded spectral theorem is not this floor's load. Book 12's Itô integral is an \(L^2\) limit and does not need it.

**Proved.** The spectral theorem for compact self-adjoint operators. Courant–Fischer. The continuous functional calculus for bounded self-adjoint operators. Mercer's theorem for the kernels the chapter treats.

**Examples.** The Dirichlet Laplacian on an interval, eigenvalues \((n\pi)^2\). One Hilbert–Schmidt kernel and its singular values.

**Figures.** Two.

### Part III. Fourier Analysis

#### Chapter 5. The Fourier Transform

**Status.** REVISE — `chapters/ch05-fourier.tex` (503 lines). Exercise 5.3 proves that Fourier transforms of finite positive measures are positive definite, then names the converse of Bochner's theorem. The solution's last sentence must keep saying the converse is not proved. Lévy's continuity theorem is Book 11 and does not depend on that converse.

**Hook.** Every signal is a chord. In the right space the listing of its notes loses nothing.

**Synopsis.** The transform on \(L^1\), the Schwartz space, Plancherel, the Hermite basis, Riesz–Thorin and Hausdorff–Young, measures and characteristic functions, band-limited functions, and Poisson summation on lattices. The convention \(\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}\,\mathrm dx\) is the series convention. Book 5's transform matches it, or this chapter says where it differs.

**Proved.** Inversion when \(\hat f\in L^1\). Plancherel. The Hermite functions as a basis of \(L^2(\mathbb R)\). Riesz–Thorin. Poisson summation on lattices.

**Examples.** The Gaussian, again, as its own transform. Shannon sampling for a band-limited function.

**Figures.** Two.

#### Chapter 6. Distributions and Sobolev Spaces

**Status.** KEEP — `chapters/ch06-distributions.tex` (441 lines). Sobolev space in dimension \(d>1\) stops at the remark that the embedding threshold is \(s>d/2\). That remark stays a remark.

**Hook.** How do you differentiate a corner, a jump, or a continuous nowhere differentiable function? You ask how it acts, not what it equals.

**Synopsis.** Test functions, distributional derivatives, smoothing, tempered distributions, fundamental solutions, \(H^1\) on an interval, and Lax–Milgram. A fundamental solution of \(\Delta\) in \(\mathbb R^3\) is the theorem a reader can compute. The Laplacian's fundamental solution is the beam's response to a point load.

**Proved.** The distributional derivative. The fundamental solution of the Laplacian in \(\mathbb R^3\). Lax–Milgram. Rellich's theorem on an interval, if the file contains it.

**Examples.** The derivative of a jump is a Dirac mass. The Newtonian potential of a point mass.

**Figures.** Two.

#### Chapter 7. Fourier Analysis on Finite Abelian Groups

**Status.** KEEP — `chapters/ch07-finite.tex` (627 lines). This is the return of Book 3's abelian characters, now as a change of basis with no convergence questions.

**Hook.** On a finite group there are no null sets and no distributions. The Fourier transform is a change of basis.

**Synopsis.** Characters and duality, a fast transform, uncertainty, quadratic reciprocity from the Fourier analysis of \((\mathbb Z/n\mathbb Z)^\times\) or from Gauss sums, the cap-set bound, and linearity testing. Quadratic reciprocity proved again is a return, and the chapter should name Book 2's proof. The cap-set argument is the home of the Crossroads Journey if that Journey uses this Fourier analysis. One home only.

**Proved.** Pontryagin duality for finite abelian groups. Inversion. Quadratic reciprocity by the method the chapter actually finishes. The cap-set bound of the strength the file proves. Meshulam's bound is the one Book 14 cites as a numbered theorem; keep that number stable.

**Examples.** The dual of \(\mathbb Z/n\mathbb Z\). A cap set in \(\mathbb F_3^n\) for small \(n\), and the bound.

**Figures.** Two.

### Part IV. Haar Measure, the Complex Plane and Tauberian Theorems

#### Chapter 8. Haar Measure, Duality and the \(p\)-adic Numbers

**Status.** KEEP — `chapters/ch08-haar.tex` (575 lines). Book 2 built \(\mathbb Q_p\) by hand. This chapter gives it a Haar measure and sets it beside \(\mathbb R\) in the adèles. Book 13's Tate thesis starts from here.

**Hook.** Lebesgue measure does not care where you stand. Every reasonable group has such a measure, and its characters form a second group.

**Synopsis.** Topological groups, Haar measure on a compact or locally compact group of the class the chapter constructs, invariant means, Pontryagin duality in the cases proved, \(\mathbb Q_p\), and the adèles of \(\mathbb Q\). General Haar existence on a compact metrizable abelian group is proved. The abstract existence theorem is marked unused if that is what the file says. The adèles are the joint into the concealed storeys.

**Proved.** Existence and uniqueness of Haar measure in the cases the chapter claims. The dual of \(\mathbb Q_p\) and of the adèles, at the level Book 13 quotes. Ostrowski may be cited back to Book 2 rather than reproved.

**Examples.** Haar measure on the circle, and on \(\mathbb Z_p\). One additive character of \(\mathbb Q_p\).

**Figures.** Two.

#### Chapter 9. Curves, Growth and Conformal Maps

**Status.** KEEP — `chapters/ch09-complex.tex` (753 lines). Delete "Perron's formula" from the preface if the name never appears again. What is proved is Mellin inversion and one rectangular shift. Book 5 owns the computational residue theorem. This chapter owns the topological one.

**Hook.** A closed curve that does not cross itself has an inside and an outside. The proof took a century.

**Synopsis.** Winding numbers, the Jordan curve theorem, Cauchy's theorem in Dixon's homology form, Phragmén–Lindelöf, Hadamard factorisation, Montel, the Riemann mapping theorem, and the Mellin transform. Carathéodory's boundary theorem is not claimed. Mellin inversion is the contour tool Book 15's Selberg–Delange argument is allowed to quote.

**Proved.** The Jordan curve theorem. Dixon's theorem and the global residue theorem. Phragmén–Lindelöf. The Riemann mapping theorem. Mellin inversion for the class stated.

**Examples.** A polygonal Jordan curve, whose elementary proof returns in Book 15's workshop as a writing exercise, a different proof. One Mellin inversion that recovers a sum.

**Figures.** Two.

#### Chapter 10. Tauberian Theorems

**Status.** KEEP — `chapters/ch10-tauberian.tex` (743 lines). The sign in the local inverse is repaired. Ikehara's Fejér-kernel proof does not use that lemma, and it was already in order. The zero-free line is imported from Book 6 and not reproved.

**Hook.** A series can have a sum without converging. Abel, Cesàro, and Borel assign one, and each way is faithful when the series does converge.

**Synopsis.** Abel and Cesàro summation, Tauber's \(o(1/n)\) theorem, Karamata, Wiener's tauberian theorem, Wiener–Ikehara, and the prime number theorem again. Counting sums of two squares by a tauberian theorem is the coda, and it points at Book 15's Selberg–Delange treatment of the same sums. Ikehara is the second beam under the prime number theorem. The chapter should say "second proof" in the heading.

**Proved.** Tauber's theorem. Karamata. Wiener–Ikehara. The deduction \(\psi(x)\sim x\) from the zero-free line. The local inverse lemma, with the repaired modulation.

**Examples.** The prime number theorem's tauberian input, one line of the Laplace transform. A series that is Abel summable and not convergent, and Tauber's extra hypothesis that restores convergence.

**Figures.** Two.

#### Chapter 11. Zeta off the Line, as Problems

**Status.** REVISE — `chapters/ch11-harder.tex` (about 1220 lines). Retitle. The file opens on Harald Bohr and the values of \(\zeta(\sigma+it)\) for \(\sigma>1\), which is Bohr's question and the problem-face of Book 15's Bohr–Jessen theorem. The chapter keeps its problems, hints, and solutions. It does not prove Bohr–Jessen. The last page points to Book 15, Chapter 11, where the limiting distribution is a theorem. "Harder problems" is not the title.

**Hook.** Bohr, in 1911: for fixed \(\sigma>1\), which values does \(\zeta(\sigma+it)\) take as \(t\) runs?

**Synopsis.** The Euler product makes the question geometric: the points \(p^{-it}\) on the circle. The problems use Hilbert space, almost periodic functions, and the mean-square theory this book and Book 5 have made legitimate. A problem may compute a mean square. It may not claim the existence of the Bohr–Jessen measure as a theorem of this floor.

**Proved.** Whatever each problem's write-up proves, and nothing beyond it.

**Examples.** One almost-periodic polynomial in the primes, and its mean. A numerical cloud of \(\zeta(2+it)\).

**Figures.** Three, already in the file.

## Owns, defers, hands forward

**Owns.** Hahn–Banach and the three Baire theorems for Banach spaces. The compact self-adjoint spectral theorem and the continuous functional calculus. Plancherel. Finite abelian Fourier analysis and a Fourier proof of quadratic reciprocity. Haar measure and the adèles of \(\mathbb Q\). Jordan, Dixon, the Riemann mapping theorem, Mellin inversion. Wiener–Ikehara and a second proof of the prime number theorem.

**Defers.** The spectral theorem for a general bounded or unbounded self-adjoint operator. The converse of Bochner. Lévy's continuity theorem (Book 11). Carleson's theorem. The value distribution of \(\log\zeta\) (Book 15).

**Hands forward.** The beams. Book 9 integrates on manifolds with the measure and the inverse-function theorem it may reprove locally. Book 12 quotes Plancherel. Book 13 quotes the adèles. Book 6's prime number theorem now has a second, independent member under it.

## Pages and effort

Baseline 178 pages plus the problem chapter. Target 200–230. Effort: moderate. The Wiener sign is repaired. The work is the blurb, the complex \(L^p\) dual, the Bochner sentence, the Perron-preface line, the part split, and the retitle.
