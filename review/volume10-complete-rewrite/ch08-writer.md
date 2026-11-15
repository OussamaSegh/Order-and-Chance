# Chapter 8 writer record

The complete `chapters/ch07-groupcoh.tex` draft is rewritten: opener and history,
all original numbered definitions/results/examples, every proof, every original
exercise/hint/idea-writeup solution, the closing discussion and bridge. Literal
bibliographic records are retained. All original labels, section order/count and
formal environment order are preserved. The full original rational-circle figure
block and diagram source remain unchanged.

## Mathematical corrections and proof repairs

1. The opening originally said H²(C10,C10) classifies all ways to build a group
   of order 100 from two copies of C10. Corrected to fixed *trivial* action and
   fixed identifications of kernel/quotient, up to equivalence of extensions.
   Other actions produce other extensions, including nonabelian groups. This is
   a correction of the opening scope, not a weakening of `thm:h2ext`.
2. `thm:h2cyclic` is valid also for n=1, but its proof's assertion that t=(0,sigma)
   satisfies t^n=a is false in that case. The trivial-group case is now proved
   separately (N=id and normalised H²=0), then the lift argument uses n>=2.
   Theorem's full conclusion and carry representative are retained.
3. The cyclic Hilbert90 corollary also checks degree one separately; the original
   formula f(sigma)=x need not follow from the listed range of exponents in that
   case. Norm one means x=1 and trace zero means x=0, so the conclusions hold.
4. `ex:carry` now names the necessary base assumption b>=2, and proves the
   converse of the cyclic-middle-group criterion: symmetry makes the group
   abelian and its exponent divides b times the order of the carry parameter.
5. `ex:cyclich1` originally said deduce the corollary from the general theorem
   'and conversely'. Its formula only gives the converse for a *cyclic* Galois
   action. Both exercise and solution now say this explicitly; no claim that
   cyclic vanishing alone proves arbitrary finite-Galois vanishing remains.
6. The beauty box called H²(G,L×) 'the Brauer group'. Corrected to the relative
   Brauer group Br(L/K), with Brauer equivalence, for finite Galois L/K. It need
   not be the whole Br(K). Matrix Hilbert90/descent and this identification are
   clearly quoted previews, not claims proved by abelian group extensions.
7. The cochain d² calculation is expanded, group inverse verification is supplied,
   fixed-action conventions and both signs in Hilbert90 are checked, and the
   trace-one proof explicitly avoids division by |G| in positive characteristic.
8. The quaternion exercise solution now provides the full cocycle table requested
   by the exercise, instead of only selected entries. Its diagonal obstruction
   and nonsplitting proof are both complete.

Original circle artwork draws selected secants for its plotted coprime pairs;
new prose explicitly calls them selected. Protected block/caption is preserved.

## Actual prerequisites checked

- Actual Volume 3 `ch10-galois.tex`, `lem:dedekind`, supplies linear independence
  of automorphisms over every characteristic. The statement walker confirms its
  printed number is 10.15.
- The actual earlier group action, finite-field, Sylow and finite-abelian-group
  results of Volume 3 supply the algebraic background.
- Chapter 7's cyclic Ext calculation is used only for an explicit comparison,
  not as a substitute for the group-cocycle proofs.
- No result in Volumes 11–15 is used. No earlier proof relies on a later exercise.
  General nonabelian Schur–Zassenhaus and nonabelian cohomology are quoted only.

## Additions

Exactly two new numbered mathematical illustrations, both after the original:

- `v10-new-ch08-complements.tex`: integer versus half-integer reflection mirrors,
  proving the parity obstruction to conjugating graph complements by translations.
- `v10-new-ch08-carry.tex`: full base-four carry table and the two parenthesisations
  of the sum (3,2,1), illustrating the actual cocycle identity.

Exactly four appended exercises, with stars, useful hints and complete
idea/writeup solutions:

- `ex:v10new-ch08-inversion`: inversion on C4, H0/H1/H2, and D8 versus Q8 as
  fixed-action extensions, distinguished by involution counts.
- `ex:v10new-ch08-affine`: order-three action on Z², H¹=C3 computed by an explicit
  index-three congruence, and rational versus integer affine fixed points.
- `ex:v10new-ch08-quadratic90`: constructive quadratic Hilbert90 including x=±1
  and characteristic two, then a finite-field norm-one count without assuming
  cyclicity or norm surjectivity as an extra theorem.
- `ex:v10new-ch08-averaging`: primitives for cocycles when multiplication by the
  finite group order is invertible on any coefficient group, including infinite
  dimensional vector spaces.

## Checks actually run

Source inventory: 3 figure blocks, 10 exercises, 10 hints and 10 solutions; all
original labels are present, and the complete original figure block is verbatim.
No local PDF or full build was run by this writer; parent owns build integration,
rendered checks, fixing commits and final receipts. This writer pass does not
claim independent mathematical certification. Separate review remains required.

## Integrated fixing commits

c42d33c6. These commits fix the original problems and prerequisite gaps
listed above; separate review records distinguish any additional draft-only fixes.
