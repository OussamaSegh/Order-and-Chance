# Chapter 3: separate mathematical and editorial source review

Reviewer: `/root/rewrite_ch09_ch10`, a different agent from this chapter's writer.
This was a separate read of the complete rewritten chapter, not a review of a
summary. Baseline: `59014a9aad3454ad60786c6549c81fcac88df9df`, using the full
original blocks in `starting-statement-content.json`. Reviewed source SHA256:
`145294f4a23ea20e2d187c6f319d9392b1b8289792c11d1f9434a23c7794861e`.

**Source review passed.** No unresolved mathematical/editorial finding was found
in this read. This is not a build, rendered-page, print-export or EPUB certificate;
parent owns those separate checks. I did not write the reviewed chapter.

## Every original numbered statement

Numbers below are the immutable baseline printed numbers. Each statement's full
mathematical content was compared, including its hypotheses and conclusion;
matching environment order/labels was also checked mechanically. No original
valid conclusion is weakened.

| Number and label | Concrete comparison and proof check |
| --- | --- |
| Definition 3.1 `def:exact` | Image equals kernel at every inner term; short sequence requires injection, surjection and middle equality. Zero end terms interpreted correctly. |
| Example 3.2 `ex:ses` | Both nonsplit sequences retained. First map into Z/4 is explicitly a residue-class multiplication map; torsion/order obstructions valid. |
| Proposition 3.3 `prop:split` | All three compatible splitting conditions retained, not just abstract middle-module isomorphism. Retraction-coordinate map injective/surjective by exactness; section inverse and both recovered maps checked. |
| Theorem 3.4 `thm:snake` | Top right-surjectivity, bottom left-injectivity, commuting squares, six-term conclusion and both conditional end conclusions all retained. Lift/push/pull/quotient independence and R-linearity checked. Exactness at all four inner terms and optional endpoints proved. No sign or orientation reversal. |
| Corollary 3.5 `cor:fivelemma` | Both exact rows short and both outside isomorphisms required. Zero kernels/cokernels force the middle isomorphism by the proven snake sequence. |
| Proposition 3.6 `prop:homleft` | Both variances retained. Covariant kernel factorisation uses injective f; contravariant quotient factorisation uses surjective g. The theorem does not promise a final surjection. |
| Lemma 3.7 `lem:testexact` | Universal quantifier over every target retained. Targets C/im(g), C and B/im(f) separately prove surjectivity, gf=0 and reverse kernel inclusion. No circular appeal to tensor exactness. |
| Definition 3.8 `def:tensor` | Every target and every bilinear map have a unique linear factorisation. Commutative-unital standing ring convention retained. |
| Theorem 3.9 `thm:tensorexists` | Existence, pure-tensor generation and unique compatible isomorphism all retained. Free module is on the actual set M×N; relations enforce both additive/scalar laws; uniqueness proves the two composites are identities. |
| Proposition 3.10 `prop:tensorrules` | Unit, symmetry, arbitrary direct sums and quotient-by-I formulas retained with maps and inverses. Finite support prevents accidental infinite sums. Quotient inverse kills all finite sums generating IM. Empty sum allowed. Naturality checked on generators. |
| Example 3.11 `ex:zmzn` | Cyclic gcd formula, all four families in the finitely generated abelian-group formula, and tensor-basis/dimension product retained. Positive cyclic parameters explicit; zero/infinite vector dimensions covered via I×J basis. |
| Theorem 3.12 `thm:tensorhom` | Full R-linear natural isomorphism in M and P retained. Currying/uncurrying inverse checks correct; explicit pre/postcomposition verifies variance. |
| Corollary 3.13 `cor:rightexact` | All modules N and arbitrary right-exact input retained. Uses earlier Hom-left-exactness, natural adjunction arrows, then the universal-target exactness test; no later flatness theorem used. |
| Definition 3.14 `def:projective` | Three distinct preservation properties retained. Lifting, extension and tensor-injection equivalences earned from the preceding exactness results. |
| Proposition 3.15 `prop:projective` | Free/projective-summand equivalence, free flatness, summands of flat modules and domain torsion-free implication all retained. Infinite basis choices acknowledged; free presentation lift splits; arbitrary direct-sum tensor maps handled by finite support. Domain assumption used exactly at multiplication injection. |
| Theorem 3.16 `thm:baer` | Every ideal map criterion, both directions, retained. Maximal extension uses actual earlier Zorn; extension on A1+Rb is well-defined by the ideal I={r:rb∈A1}. Difference/sign calculation checked. Empty-chain upper bound stated. |
| Corollary 3.17 `cor:divisible` | PID hypothesis, every nonzero r/e division request and Q/QZ/Z examples retained. Principal-ideal map determined by u(r) uses domain; zero ideal handled; quotient divisibility valid. |
| Theorem 3.18 `thm:pidflat` | Finite-generation and PID assumptions retained for all four equivalent properties. Structure theorem eliminates every nonzero cyclic torsion summand; R^0 case included. Q counterexample and new local proof of its flatness avoid a forward prerequisite. |

## Every original and added exercise, hint and solution

All ten exercise labels have one matching semantic hint and one complete
idea/writeup solution. Hints were checked as hints rather than as unavailable
prerequisites; every solution was read in full.

| Exercise | Mathematical check |
| --- | --- |
| 3.1 `ex:zmzncomp` | Positive m,n repair explicit; generator image must solve mx=0 modulo n and gives gcd order. Divisible/torsion tensor vanishes by moving its killing integer; Q tensor Q/Z follows. |
| 3.2 `ex:whichsplit` | Outcomes split, nonsplit, nonsplit, split verified. Section 1→4 modulo 6 works; orders distinguish Z/9; torsion excludes Z²⊕Z/5; any onto Z²→Z splits by a lift of 1. Kernel generator (-b,a) correct for primitive (a,b). |
| 3.3 `ex:composite` | Every kernel/cokernel map explicitly given. Direct exactness checks at all positions valid. Original erroneous placement of the snake connecting label corrected: it belongs from coker f to coker(gf), not from ker g. No theorem claim changed. |
| 3.4 `ex:qnotproj` | Hom(Q,Z)=0 uses divisibility by arbitrarily large integers; coordinate projection of a nonzero vector in a free direct sum excludes projectivity. Finite sum extension proof includes empty sum. Prime-denominator decomposition onto and injective via coprime annihilators; Prüfer summands divisible. |
| 3.5 `ex:tensoralgebra` | Polynomial base change derived from direct sums/right exactness, then checked multiplicatively. C factors distinct via 2i; Q(√2) does not contain a root of X²−3 by rational prime exponents. Fields and characteristic-zero assumptions are present. |
| 3.6 `ex:fivelemma` | Full five-term conditions retained. Injectivity uses h4,h2 injective and h1 onto; surjectivity uses h4,h2 onto and h5 injective. Each correction lift lies in the required kernel. |
| 3.7 `ex:v10new-ch03-quotients` | Multiplication gives quotient tensor R/(I+J), inverse 1⊗r kills I and J separately. Z/12 tensor Z/18=Z/6; dual-number quotient tensor=K. Nonzero nilpotent cannot be recovered. |
| 3.8 `ex:v10new-ch03-snake` | Commutative multiplication diagram valid. Snake sends k modulo m to nk/m modulo n on its kernel; changing lift adds n times an integer. Generator m/d maps to n/d, both order d; image is ker(m on Z/n). Example 6,4 gives 3→2. Coprime case gives zero groups. |
| 3.9 `ex:v10new-ch03-idempotent` | eR and (1−e)R have zero intersection, sum R. Tensor inverse e⊗x correct on eM, including e=0,1. In Z/6, e=3 gives groups Z/2 and Z/3. Domain torsion-free claim is not misapplied. |
| 3.10 `ex:v10new-ch03-finiterank` | Arbitrary-space tensor/Hom map injective by independent finite output vectors; image exactly finite-rank maps via coordinates on image. Infinite-dimensional identity excluded; either finite-dimensional factor makes it onto. Zero-space cases explicit. |

## Additional prose and prerequisite review

Read all introductions, transitions, short formula introducers, examples outside
formal boxes, historical copy, beauty/think boxes, ending and sources. The voice
is concrete and mathematical. The opening parity example demonstrates why exact
need not split. Bilinear versus jointly linear is explained by actual sums and
does not incorrectly exclude the zero map. Fractions for Q-flatness are defined
locally, their equality condition is checked in the tensor inverse, and injection
survival is proved before any use of localisation theory. Finite-dimensional
Hom/tensor/rank observations do not assume the later arbitrary-space exercise.
Winograd optimality is correctly quoted, not claimed proved.

Actually inspected prerequisite sources: Volume 3 `ch07-modules.tex` statement
and proof of PID structure (Theorem 7.6); `ch06-rings.tex` CRT 6.9 and polynomial
UFD 6.18; Volume 7 `ch01-sets.tex` Zorn 1.19 and vector-space basis discussion;
current Chapter 1 `prop:initialunique`, `ex:functors`, `ex:adjunctions`. Their
printed locations precede Chapter 3. No proof requires a later exercise, appendix
or Volume 11–15. Cross-volume citation resolver command below finds the expected
targets; that automated result supports these actual source reads.

## Figures and source preservation

Both added sources were read in full. `v10-new-ch03-collapse` has the correct
multiplication-2 upper arrow, zero lower arrow, identity quotient and no claim of
exactness at the first lower Z/2. `v10-new-ch03-lifts` has the correct domains,
onto/inclusion labels and missing dashed lift/extension orientations. Its caption
states the commuting condition accurately. No scale represents numerical data.
Both use the approved palette. Both blocks appear after the original snake figure.

Source comparisons confirm the original snake figure block is an exact substring,
all original figure source hashes in this volume remain unchanged, every original
chapter label remains, and the numbered section list/order is unchanged. The chapter
has exactly 6+4 exercises and 1+2 mathematical figures. No photograph occurs here.
Built label numbers and rendered text require the parent's final production check.

Commands actually run by reviewer: Python source comparison (exit 0) checked
original blocks, labels and original figure hashes against starting-source.json;
`python3 review/volume10-rewrite/resolve_citations.py volume10-abstraction/chapters/ch02-tensors.tex volume10-abstraction/chapters/ch03-noetherian.tex`
exited 0 and resolved expected prior source targets. No builds or numerical
experiments were used as proof substitutes.
