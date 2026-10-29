# Book 10 — Abstraction

*Categories, Algebra and Homology.*

**Element.** The hidden frame. The rooms are standing. This floor is the framework one cannot see from inside a single room: an object known by the maps into it, a module known by its presentations, a hole known by a homology group.

**On disk.** Volume 9, `tome9-higher-structures`. The catalog title is still Higher Structures. This plan uses Abstraction. Eleven chapters, about 152 pages. The October review scored it 8. The cubic class-group sentence in `ch05-dedekind.tex` no longer claims an isomorphism. The shuffle chapter's Fourier comparison now states both the factor \(|G|\) and the conjugation.

## Promise

Book 3 met groups, rings, and fields one at a time. Abstraction looks at the maps between them. Yoneda's lemma is the thesis: an object is known by the way other objects map to it. The floor then builds the frame the upper storeys hang on. Commutative Algebra carries the rings and the homology of modules. Representations carries the character theory and the homology of groups, and it is where the shuffle proof now leaves for Book 11.

## Prerequisites

Book 3 entire, including characters. Book 8's Hilbert spaces and compact operators, for the shuffle and for compact groups. Book 9's homology of \(\mathbb{RP}^2\), cited by the universal-coefficient discussion. No scheme theory. The one sentence on schemes in the Noetherian chapter stays one sentence.

## How the subtitle is delivered

The parts keep their catalog names. *Categories, Algebra and Homology* is what they do, and homology is not given a part of its own.

Categories delivers the first word: an object known by the maps into it, and the tensor product as a universal map. Commutative Algebra delivers the algebra, from Noetherian rings through Dedekind domains, and the homology of modules: Tor, Ext, and the long exact sequence sit in this part, which the catalog already runs through homological algebra. Representations delivers the algebra of symmetry, Wedderburn through Weyl's character formula, and the homology of groups: group cohomology opens the part. \(H^n(G,M)\) is not Book 9's \(H_n\). Tensors from Book 3's Appendix J arrive in Categories. No part is renamed.

**Move.** Chapter 10, Shuffling cards (`ch10-shuffling.tex`), is a cutoff, a limit theorem about a deck. It does not deliver categories, algebra, or homology. MOVE it to Book 11, into Martingales and Ergodic Theory, beside the other mixing theorems. The upper-bound lemma may be cited from the symmetric-group chapter, where the Fourier analysis of \(S_n\) remains algebra. Representations stays the part name. Shuffling no longer closes it.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Categories | 1–2, and the tensor appendix from Book 3 |
| II | Commutative Algebra | 3–6 |
| III | Representations | 7–9 and 11. Chapter 10 moves. |

---

The chapter notes follow the manuscript's file order. The part names are the table above. The shuffle chapter is under Book 11.

### Part I. Categories

#### Chapter 1. Categories

**Status.** KEEP — `tome9-higher-structures/chapters/ch01-categories.tex` (483 lines).

**Hook.** A free group, an abelianisation, a double dual, and the currying of a function of two variables. What do they have in common?

**Synopsis.** Categories, functors, natural transformations, universal properties, Yoneda, and adjunctions. The hidden frame is the sentence that an object is its incoming maps. The chapter is short on examples from the lower floors and should keep the ones it has: free groups from Book 9, abelianisation from Book 3, the double dual from Book 3's linear appendix.

**Proved.** Yoneda's lemma. The uniqueness of adjoints up to unique isomorphism. The universal property of the product, the coproduct, and the free group, as the chapter states them.

**Examples.** The forgetful functor from groups to sets, and its left adjoint. One natural transformation that is not a natural isomorphism, the double dual of a finite-dimensional vector space against an infinite-dimensional one.

**Figures.** One.

#### Chapter 2. Tensors and Exactness

**Status.** KEEP — `chapters/ch02-tensors.tex` (422 lines).

**Hook.** Kernels and cokernels sit in exact sequences. One diagram chase, the snake lemma, connects them. Tensor products turn bilinear maps into linear ones.

**Synopsis.** Exact sequences, the snake lemma, Hom and exactness, the tensor product, and projective, injective, and flat modules. This is the algebra the subtitle names, begun one chapter early so that exactness is in place before the Noetherian theory. Book 3's PID structure theorem is the case where every finitely generated module is a sum of cyclics. The chapter cites it.

**Proved.** The snake lemma. Right-exactness of the tensor product. The characterisation of projective modules by lifting, or by being a direct summand of a free module.

**Examples.** \(\mathbb Z/2\otimes\mathbb Z/2\). One Tor computation that can wait for Chapter 6, or a failed exactness on the left of a tensor, exhibited here.

**Figures.** One.

### Part II. Algebra

#### Chapter 3. Noetherian Rings and Hilbert's Theorems

**Status.** KEEP — `chapters/ch03-noetherian.tex` (432 lines). Gordan's "theology", attributed to Constance Reid, can stay if the citation is Reid's. The sentence on schemes stays one honest sentence.

**Hook.** Can every system of polynomial equations, even an infinite one, be replaced by a finite one? When does a system have no solution at all?

**Synopsis.** Noetherian rings and modules, Hilbert's basis theorem, varieties and the Zariski topology, the Nullstellensatz, and Gröbner bases. The weak and strong Nullstellensatz and Zariski's lemma are the theorems. \(\mathrm{Spec}\) is defined and is not a locally ringed space.

**Proved.** Hilbert's basis theorem. The Nullstellensatz. Noether normalisation is Chapter 4's if that is where dimension is proved; this chapter owns the basis theorem and the Nullstellensatz.

**Examples.** The Gröbner basis of \((X^2-Y,X^3-X)\), zero set \(\{(0,0),(1,1),(-1,1)\}\). The real Nullstellensatz's failure for \((X^2+Y^2)\).

**Figures.** One.

#### Chapter 4. Localisation and Dimension

**Status.** KEEP — `chapters/ch04-localisation.tex` (396 lines).

**Hook.** To study a ring near one prime, invert everything outside it.

**Synopsis.** Rings of fractions, local rings, Nakayama, the spectrum, integral extensions, going up, Krull dimension, and Noether normalisation. Dimension of \(K[x_1,\ldots,x_n]\) equals \(n\). Going down is not proved. The chapter may say so.

**Proved.** Nakayama's lemma. The lying-over and going-up theorems. Noether normalisation. \(\dim K[x_1,\ldots,x_n]=n\).

**Examples.** Localisation of \(\mathbb Z\) at \((p)\). One integral extension and the primes above a named prime.

**Figures.** One.

#### Chapter 5. Dedekind Domains

**Status.** EXPAND — `chapters/ch05-dedekind.tex` (475 lines). Primary decomposition and associated primes are absent, and the review asked for them before this chapter. Add them as a section of Chapter 4 or as the opening of this chapter. They are not a prerequisite of Book 13, which proves unique ideal factorisation for \(\mathcal O_K\) on its own. They are the frame's honesty: Dedekind domains are the rings where the associated primes of a nonzero ideal are the primes in its factorisation, and every nonzero prime is maximal.

The map from a cubic's points to the class group of its coordinate ring is not claimed to be an isomorphism. Keep that refusal.

**Hook.** In the integers of a number field, numbers may factor in several ways. Ideals factor in one way. Which rings are like that?

**Synopsis.** Fractional ideals, discrete valuation rings, the four equivalent definitions of a Dedekind domain, the class group, integral closure in a finite extension, and the splitting \(\sum e_if_i=n\). Book 2 saw this for one quadratic ring. Book 13 proves it for every \(\mathcal O_K\). This chapter owns the axiom set. A sentence at the start says those two returns.

**Proved.** The equivalence of the Dedekind axioms the file lists, including unique factorisation of nonzero ideals. \(\sum e_if_i=n\). The class group is a group.

**Examples.** \(\mathbb Z[\sqrt{-5}]\), again, now as a Dedekind domain whose class group has order 2. A prime that splits, with \(e\) and \(f\).

**Figures.** One.

### Part III. Homology

#### Chapter 6. Homological Algebra

**Status.** KEEP — `chapters/ch06-homological.tex` (397 lines). Universal coefficients for finitely generated free complexes over a PID. The theorem is not stated for singular chains, which are not finitely generated. That restriction is correct and should stay visible. Book 9's singular homology is not rewritten here.

**Hook.** Tensor and Hom forget the ends of exact sequences. Homological algebra measures exactly what they forget.

**Synopsis.** Projective and injective resolutions, the horseshoe lemma, the long exact sequence, Tor and Ext, the classification of extensions by \(\mathrm{Ext}^1\), and universal coefficients. No spectral sequences and no derived categories. The frame is computed one degree at a time, which is the right depth for this floor.

**Proved.** The horseshoe lemma. The long exact sequence for Ext. \(\mathrm{Ext}^1(A,B)\) classifies extensions. Universal coefficients for the complexes the chapter allows.

**Examples.** \(\mathrm{Ext}(\mathbb Z/n,\mathbb Z/m)\). One extension of abelian groups classified by a class.

**Figures.** One.

#### Chapter 7. Group Cohomology

**Status.** EXPAND — `chapters/ch07-groupcoh.tex` (350 lines). State the inflation-restriction sequence in degrees 1 and 2, even if the spectral sequence stays a remark. The notation \(H^n(G,M)\) is the series convention and must not collide with Book 9's \(H_n\).

**Hook.** A group acting on an abelian group. Three small cohomology groups answer three old questions: fixed points, twisted homomorphisms, and extensions.

**Synopsis.** Inhomogeneous cochains, \(H^1\) and \(H^2\), Hilbert 90, group extensions, cyclic groups and the carry in schoolroom addition, and Schur–Zassenhaus. The carry is the surprise: a cohomology class is what a child does when a column overflows. There is no Lyndon–Hochschild–Serre spectral sequence.

**Proved.** Hilbert 90. The classification of extensions with abelian kernel by \(H^2\). Schur–Zassenhaus under the coprime-order hypothesis the file uses. Inflation-restriction in degrees 1 and 2, once it is added.

**Examples.** \(H^1(\mathrm{Gal}(\mathbb C/\mathbb R),\mathbb C^\times)\), or the Hilbert 90 case the chapter computes. The carry sequence for base \(10\).

**Figures.** One.

### Part IV. Representations

#### Chapter 8. Semisimple Algebras and Induction

**Status.** KEEP — `chapters/ch08-semisimple.tex` (398 lines). Maschke is cited to Book 3, Theorem 11.3, the averaging proof. The citation was checked and lands. Do not reprove Maschke.

**Hook.** The group algebra \(\mathbb C[G]\) is a product of matrix algebras, one for each irreducible representation.

**Synopsis.** Semisimple modules, Wedderburn, induced representations, Mackey, Burnside's \(p^aq^b\) theorem, and Frobenius groups. Induction is how a representation of a subgroup becomes a representation of the group. The character table of Book 3 is the case of a finite group over \(\mathbb C\), and the chapter says so.

**Proved.** Wedderburn's theorem for finite-dimensional semisimple algebras over an algebraically closed field. Frobenius reciprocity. Mackey's formula in the form used. Burnside's \(p^aq^b\) theorem.

**Examples.** A representation of \(S_3\) induced from a subgroup. One group of order \(pq\) whose irreducible degrees the theorem constrains.

**Figures.** One.

#### Chapter 9. The Symmetric Group

**Status.** KEEP — `chapters/ch09-symmetric.tex` (472 lines).

**Hook.** The irreducible representations of \(S_n\) are indexed by the partitions of \(n\). Each can be built from a Young diagram. Its dimension is a hook-length count.

**Synopsis.** Specht modules, standard tableaux, the hook-length formula, and the character of a transposition. The hook walk is the proof, and the identity \((h_{a\beta}-1)+(h_{\alpha b}-1)=h_{ab}-1\) is the step the review found doing the work. Young diagrams return from Book 3's nilpotent operators, now as representations. Book 12's longest increasing subsequence is a different use of a permutation; a sentence is optional.

**Proved.** The Specht modules are the irreducibles, over \(\mathbb C\), in the characteristic-zero form the chapter proves. The hook-length formula. The trace of a transposition on the Specht module.

**Examples.** The partitions of 4, matched with the character table of \(S_4\) from Book 3. One hook-length computation, \(n=5\) or the standard \(4!/(\mathrm{hooks})\).

**Figures.** One.

#### Chapter 10. Shuffling Cards

**Status.** MOVE — `chapters/ch10-shuffling.tex` (356 lines), to Book 11, Limits. A cutoff is a limit theorem. It does not deliver categories, algebra, or homology. The Fourier sentence is repaired and travels with the proof. The multiplicity of an irreducible in the regular representation is Corollary 11.9 of Book 3, and the chapter's citation should say that corollary if it still says Theorem 11.8. The cutoff proved is a weaker explicit bound than \(\tfrac12 n\log n\), and line 202 already says so. Keep the honesty in the chapter's first page, not only at the end.

**Hook.** How many random transpositions mix a deck of \(n\) cards?

**Synopsis.** Fourier analysis on a finite group, the upper-bound lemma, and random transpositions. The eigenvalue \(1-2/n\) on the standard representation is the right one. For \(n\ge 10^4\) the chapter proves an explicit cutoff of the right shape. Book 4 announced the phenomenon. Book 15's workshop proves the Bayer–Diaconis limit profile for riffle shuffles, which is a different shuffle and a different theorem. The two must not be cited as one result.

**Proved.** The upper-bound lemma. The transposition cutoff in the form the chapter states, with the range of \(n\) on the page.

**Examples.** The total-variation bound at \(\tfrac12 n\log n+cn\). A small deck, \(n=3\) or \(n=4\), diagonalised by hand.

**Figures.** One.

#### Chapter 11. Compact Groups

**Status.** REVISE — `chapters/ch11-compact.tex` (382 lines). Schur–Weyl duality is stated and not proved. Move the isomorphism into a remark, next to the sentence that already says it is not proved. Weyl's character formula does not need it.

**Hook.** Averaging over a compact group with Haar measure makes representations unitary and characters orthonormal, as for finite groups.

**Synopsis.** Representations of compact groups, Peter–Weyl, the irreducibles of \(U(n)\), and traces of random unitary matrices. Dimensions 8 and 10 for the two sample weights are the numerical check. Book 9 computed the eigenvalue law. This chapter computes the representation ring. Book 12 will pass from the finite-\(n\) law to the sine kernel. The three citations should form a chain, each naming the previous.

**Proved.** Peter–Weyl, at the strength the file reaches. Weyl's character formula for \(U(n)\). The dimension formula on the sample weights.

**Examples.** The standard representation of \(U(n)\) and its exterior powers. One character value.

**Figures.** One.

## Owns, defers, hands forward

**Owns.** Yoneda and adjunctions. The snake lemma and the tensor product. Hilbert basis and the Nullstellensatz. Noether normalisation and dimension. Dedekind domains as an axiom set, after primary decomposition is added. Ext, Hilbert 90, Schur–Zassenhaus. Wedderburn, induction, Burnside's \(p^aq^b\) theorem. Specht modules and the hook-length formula. The transposition cutoff. Peter–Weyl and Weyl's character formula for \(U(n)\).

**Defers.** Schemes. Spectral sequences and derived categories. The number-field case of unique ideal factorisation (Book 13). The Bayer–Diaconis profile (Book 15). The sine-kernel limit (Book 12). Going down, Artinian rings, completions, and Hilbert–Samuel polynomials, unless a later sentence needs one of them; none of Books 11–15 does.

**Hands forward.** The frame. Book 13 cites the Dedekind axioms and proves the number-field case itself. Book 12 cites Peter–Weyl only as a pointer if it needs it, and cites Book 9 for the eigenvalue law. Book 15's Cohen–Lenstra chapter uses the classification of finite abelian groups from Book 3 and the class group from Book 13, and it may mention this book's Ext only if a cocycle is written down. The preferred path in Book 15 is the explicit cokernel, not a cocycle.

## Pages and effort

Baseline 152 pages. Target 170–200 after primary decomposition and the inflation-restriction sequence. Effort: moderate. The theorems that carry the book are proved. The work is the missing commutative-algebra section, two citation sentences, the Schur–Weyl remark, and the part names that match the subtitle.
