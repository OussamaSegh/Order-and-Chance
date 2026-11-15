# Chapters 1–4 teaching expansion: writer record

Starting main: `b005c4a0a33409f443594f3bb1efe3e955e95468`.
Branch: `codex/volume10-teaching-expansion`. Immutable comparison is the new
`review/volume10-expansion/starting-source.json`, not the earlier rewrite baseline.
Read current main.tex (printed chapter order), instructions/style, relevant
chapter sections and all current exercise/hint/solution lists before inserting.
Only the four assigned manuscript files and this record were edited. No figures,
numbered sections, formal statements, equations, front matter or shared files
were added or modified. This is the writing pass; separate review is still needed.

Every chapter now has two substantial unnumbered worked examples, marked exactly
`% V10-EXPANSION WORKED EXAMPLE 1` and `2`. They are placed before Exercises in
existing teaching sections, using `subsection*` headings. Every chapter also has
four appended exercises: one ★ calculation, two ★★ tasks (conceptual and
hypothesis/counterexample), and one ★★★ application. Each has one new unique
label, a hint, and a complete `idea`/`writeup` solution. New hints and solutions
follow the complete existing lists. No existing protected block was rewritten.

## Chapter 1 — maps, universal properties and naturality

Worked examples:

1. Compute the abelianisation of S3 explicitly by sign and one commutator.
   Parametrise maps to arbitrary abelian targets, including concrete C×, Z/3
   and Z/4 targets. Placed in Universal properties, before Yoneda.
2. Compare natural squaring with the impossibility of a conjugation-compatible
   choice of square root. Give the square over Z→Z/6→Z/2 and the automorphism
   obstruction at −1 in C. Placed after Yoneda and before Adjunctions.

Appended exercises (now14 total):

- `ex:v10exp-ch01-homproduct`, ★: all six maps Z/6→Z/4×Z/9, image orders,
  two injections and no surjection;
- `ex:v10exp-ch01-equalisers`, ★★: transpose equaliser problems across an
  adjunction, with the full existence/uniqueness proof and set model;
- `ex:v10exp-ch01-bijections`, ★★: objectwise bijections commuting with all
  isomorphisms but failing naturality on the singleton injection;
- `ex:v10exp-ch01-presentation`, ★★★: abelianise <a,b|a²=b³=1>, give its
  nonabelian S3 quotient, and classify its six homomorphisms to C×.

Prerequisites: earlier universal properties, naturality and adjunctions from
this chapter; cyclic-group arithmetic and commutators from Volume3; free
products/group presentations from actual Volume9 Chapter5. No later theorem is
used. The last example does not assume the entire group is finite or abelian.

Editorial repair requested by parent: close the unmatched TeX quotation in the
opening nickname sentence, now `The nickname ``general abstract nonsense'' ...`.
This is outside every protected formal/exercise/figure block. No mathematical
correction to preserved material was necessary.

## Chapter 2 — vectorisation, rank and matrix multiplication

Worked examples:

1. Solve AX−XB=I with a non-diagonalisable Jordan A and diagonal B. Show both
   column solves, the exact solution, direct product check and the4×4 vec system.
   Placed after Sylvester and before Tensors and their rank.
2. Compute every one of Strassen's seven products and all four outputs for
   matrices with entries1–8. Compare total scalar-operation counts25 versus12,
   then check the same identity modulo2. Placed after Strassen's theorem proof,
   before its exponent argument. This illustrates a proved identity, not an
   experimental substitute for its proof.

Appended exercises (now20 total):

- `ex:v10exp-ch02-vecsystem`, ★: exact4×4 system for AX+XB and its solution;
- `ex:v10exp-ch02-bases`, ★★: invertible factor changes preserve tensor rank;
  diagonal tensor rank r proved by flattening, including zero;
- `ex:v10exp-ch02-transpose`, ★★: omitting transpose works for all X exactly
  when B is symmetric, with nonsymmetric and adjoint counterexamples and m=0;
- `ex:v10exp-ch02-leastsquares`, ★★★: all Frobenius least-squares solutions
  for normal A,B, the compatibility condition at common eigenvalues, minimum
  residual and complete uniqueness condition.

Prerequisites: Sylvester, vec and flattening already proved in this chapter;
unitary diagonalisation and Frobenius norm from actual earlier Volume8 spectral
and SVD chapters. The least-squares proof separates a finite sum of scalar
squares; no later functional analysis or optimisation theorem is assumed.

## Chapter 3 — exactness, presentations and lifting

Worked examples:

1. Compute a nonzero snake connecting map with two identical Z--2→Z→Z/2 rows
   and vertical maps2,2,0. Track lift1, pullback1, choice independence and every
   map in the resulting exact sequence. Placed before Hom and exactness.
2. Present Z²/<(2,0),(1,3)>, prove it is Z/6 using explicit inverse maps,
   tensor its relation matrix with Z/4 and prove its cokernel is Z/2. Placed
   after right exactness and before Projective, injective and flat modules.

Appended exercises (now14 total):

- `ex:v10exp-ch03-presentation`, ★: explicit integer operations give
  Z²/<(4,0),(2,6)>≅Z/2⊕Z/12; tensor and Hom to Z/6 both computed;
- `ex:v10exp-ch03-projective-splitting`, ★★: every sequence ending in P
  splits iff P projective, with explicit fibre-product lift construction;
- `ex:v10exp-ch03-pid-hypothesis`, ★★: I=(X,Y) over K[X,Y] is finitely
  generated/torsion-free but not free, using a rank-one fraction-field argument;
- `ex:v10exp-ch03-extensions`, ★★★: full splitting criterion and section
  count for the presented middle group na=0,kb=ta, namely gcd(k,n)|t and
  exactly gcd(k,n) sections when solvable, with the two order-four examples.

Prerequisites: snake, tensor right exactness, splitting and projective criteria
already proved here; integer Smith operations/PID module structure from Volume3
Chapter7 and polynomial UFD from Volume3 Chapter6. The fraction/tensor
identification is already explained before this chapter's exercise list.
The nonfree-ideal solution deliberately needs no local-ring theorem from later
Chapter5. Extension classes or Ext from Chapter7 are not premises.

## Chapter 4 — polynomial equations, reduction and geometry

Worked examples:

1. The union Y(Y−X²)=0: prove two prime components and product/intersection
   equality despite failure of comaximality; identify functions as pairs of
   polynomials agreeing modulo X². Explicit compatible and incompatible pairs
   explain the extra restriction caused by tangency. Placed before Nullstellensatz.
2. For Y=X²,Y²=1, compute the elimination identity, sole S-pair, unique
   remainder basis and all four complex points. Check an ideal member and a
   nonmember, then repeat over R to exhibit a genuinely radical ideal whose
   real vanishing ideal is larger. Placed after Gröbner theory before ending.

Appended exercises (now14 total):

- `ex:v10exp-ch04-reduction`, ★: Gröbner basis for (Y−X²,X³−8), normal
  form7X+8, three zeros, quotient basis and radicality;
- `ex:v10exp-ch04-radicalproduct`, ★★: sqrt(IJ)=sqrt(I)∩sqrt(J)=sqrt(I∩J)
  over any commutative ring, zero-set union and strict product/intersection example;
- `ex:v10exp-ch04-infinitevariables`, ★★: infinitely many coordinate
  equations cannot be replaced by any finite polynomial list, even a new one;
- `ex:v10exp-ch04-fourvalues`, ★★★: four-point evaluation isomorphism,
  interpolation idempotents, exact invertibility criterion and inverse polynomial
  1−X/2−2Y/3+5XY/12 for1+X+2Y modulo(X²−X,Y²−Y).

Prerequisites: earlier ideal quotient/UFD/ring CRT facts from Volume3; each
insertion uses only the variety/irreducible or Gröbner results already preceding
it in Chapter4. Interpolation is proved locally from four explicit polynomials.
No dimension, localisation, primary decomposition or later geometry is assumed.

## Checks actually executed

Source-preservation and exact symbolic checks were executed with Python after
`source /workspace/order-chance-system/activate.sh`. The first run exited1 in
the check harness: SymPy inferred an integer coefficient domain for the final
four-point calculation and rejected rational1/2. Source-preservation and earlier
calculations had already passed. The harness was rerun with explicit `domain=QQ`
for the Gröbner computations; it exited0. This was not a manuscript/build failure.
The successful run checked:

- all56,66,51,53 protected literal blocks in Chapters1–4 respectively, including
  every original formal statement, exercise, hint, solution and figure block;
- retention of all original labels, no duplicate labels, exactly2 marked worked
  examples and4 new exercise/hint/solution sets per chapter;
- unchanged per-chapter figure counts3,4,3,3; no figure file was edited;
- exact matrix identities for both new vec examples, relation determinant24,
  Gröbner remainder7X+8 and the four-point polynomial inverse.

`git diff --check --` followed by the four assigned chapter paths exited0.
No local book build, rendered-page inspection, EPUB check, commit or push was
performed by this writer. Parent owns those checks and integration. Print-page
increase is a target, not measured by this source work.

Final writer source SHA-256 receipts:

- Chapter1: `876b9849d162e6683229f21bb717ce8d8dd2b93f61614151612815a4d4cdfc43`;
- Chapter2: `7bcc425afa7e4f16f49388cc0b97e780ac5225bb8051e540a48faa07967d1712`;
- Chapter3: `e1d2d6b770f90a57c8cd9ccb19e2c7143c4895705e740f0b3c2a7e2b31241385`;
- Chapter4: `e568589ea862953fe411d8f8e4b69fc16289f3010fca11f4140c2d43bca98326`.
