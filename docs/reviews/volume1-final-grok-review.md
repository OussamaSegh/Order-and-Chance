# Final review: Volume 1, *First Principles*

Independent review of the reading PDF (502 pages) built from `7fae5a8c6724c29dca4132fa7284525a3334f6dd`, which includes the approved preface and the opener-page swap. Page numbers below are the printed folios. This review does not rewrite the book.

## Verdict

**Publish after fixes.**

The book is already a first edition in the ways that matter. A reader with school algebra can follow a real argument from a sentence’s quantifiers through induction, counting, limits, and a finite probability, and the voice is mostly a person at the board. Two printed lines are false, and both are local. One is the last sentence of a solution that names the wrong bound as the claim. The other is a reminder that says the product of the greatest and least stretches is the determinant. Neither is a reason to rebuild a chapter. Both would teach a careful reader something untrue, so they block a first printing. The rest of the list is repair work of the same kind: a missing definition, a dependency a chapter promised to name, one loose word in the field guide, and a text layer that drops spaces on about a hundred lines while the ink stays readable.

## Strengths

The preface earns its place. The cubes \(1^3+\cdots+10^3=3025=55^2\), checked again at \(n=4\), and the four-hat count \(9/24\), are the two kinds of sentence the series is built on, and both are proved later where the preface says they will be. The assumptions list is the right one for this volume: well-ordering of \(\mathbb N=\{0,1,2,\ldots\}\), completeness of \(\mathbb R\), the integral of a continuous function with four named properties, and \(\exp\), \(\ln\), \(\sin\), \(\cos\) taken as given with their derivatives. Later chapters use that contract. Chapter 1 derives induction from well-ordering. Chapter 3 proves the intermediate-value, extreme-value, and uniform-continuity theorems on a closed bounded segment, and Rolle and the mean value theorem with the usual one-sided hypotheses. Chapter 8 proves the derivative rules and the fundamental theorem, and it says plainly that Lagrange’s pointwise remainder is not what the proof locates.

The set pieces that a hostile reading tries to break held up.

- The four proofs that \(\sum_{k=1}^n k^3=\bigl(\sum_{k=1}^n k\bigr)^2\) agree, including the induction step and the odd-block decomposition.
- \(D_4=9\), the recurrence, and the passage to \(1/e\) in Chapter 10, where Chapter 2 said it would be proved. The expected number of fixed points is \(1\) for \(n\ge 1\), kept separate from that limit.
- Abel summation matches the discrete product rule. Absolute convergence is required before a rearrangement is allowed to keep its sum.
- Erdős–Ko–Rado is stated with the hypothesis \(n<2k\) in the direction that makes the theorem true. \(\Phi_{105}\) is the first cyclotomic polynomial with a coefficient outside \(\{-1,0,1\}\), and the book says so.
- The fundamental theorem of algebra is proved from the minimum of \(|P|\), not assumed. The spectral theorem is the real symmetric case. Stirling is \(\sqrt{2\pi n}\,(n/e)^n\bigl(1+1/(12n)+O(1/n^2)\bigr)\). Carleman’s constant is \(e\), claimed sharp as a constant and not as an equality case.
- Birthday arithmetic for \(23\) people, the stake division \(11/16\), Monty Hall at \(2/3\) for the informed host, and the weak law with pairwise independence and a common variance, all match the calculations. The orbit of \(27\) in About the Cover takes \(111\) steps and reaches \(9232\).
- The field guide hands the reader to Volume 2, *The Integers: Primes, Patterns and Proofs*, with a real teaser: \(2\cdot 3\cdot 5\cdot 7\cdot 11\cdot 13=30030\) and \(30031=59\cdot 509\).
- Reader-facing copy does not describe this book as a revision, and it does not mention companion notebooks. Cross-references use the printed chapter numbers, including Chapter 0, and they match.

The interior matches the approved opener swap. Part pages are solid charcoal, with the coral numeral and the ivory title, and no illustration. Chapter openers put a charcoal band over the top \(3.4\) inches, then about \(0.15\) inch of air, then the coral chapter number, the title, a short coral rule, and the epigraph. Long titles wrap cleanly (Chapter 1, Chapter 9). Running heads sit on the outside, folios on the outside, and the gutter is the wide margin on the binding edge of the printed recto and verso. The contents leaders line up. About the Cover is one clean paragraph, \(149\) words, and it says what the picture is, one checked fact, and why that picture faces the language chapter. The back-cover blurb is not part of this reading PDF.

## MUST-FIX

Two items.

**1. Solution of Exercise 1.20(a)–(b), p. 90.** The exercise (pp. 76–77) asks for
\[
\Bigl|\sum_{a\in A}\sum_{b\in B}e(rab/p)\Bigr|\le\sqrt{p\,|A|\,|B|}
\]
and, in (b), for the same square root on \(|N(x)-|U||V|/p|\). The write-up of (a) proves the square of that bound and stops with “The right side is therefore \(p|A||B|\), which is the claim.” Part (b) ends at \(|E|^2<p|U||V|\). Part (c) then subtracts \(\sqrt{p\,|A||B||C||D|}\), as if (b) had already taken the root. The estimate is one honest sentence short of the exercise, and the sentence that is there names the wrong bound. In (d), “cosine is decreasing on that interval, and \(\cos(2\pi/9)>1/2\)” does not say why the number is larger than \(1/2\).

Take the nonnegative square root at the end of (a) and of (b), and call that the claim. In (d), use that cosine decreases on \([0,\pi/2]\), that \(2\pi/9<\pi/3\), and that \(\cos(\pi/3)=1/2\).

**2. Reminder “small determinant, different question,” p. 322.** “Conditioning compares the greatest stretch with the least. Their product is the determinant, up to sign.” The product of the greatest and least stretches equals \(|\det|\) in dimension \(2\). The same box has just said that \(\varepsilon I\) has determinant \(\varepsilon^n\) and stretches every direction by \(\varepsilon\). Those two stretches multiply to \(\varepsilon^2\). The condition number is the ratio of the greatest stretch to the least. The determinant, up to sign, is the product of one stretch from each dimension.

Replace the sentence with those two facts. The examples already in the box, \(\varepsilon I\) and \(\operatorname{diag}(M,1/M)\), then agree with it.

## SHOULD-FIX

**p. 8, §0.2.** After a correct check that \(x>1\) is sufficient for \(x^2>1\) and that it is not necessary, the text says “A necessary and sufficient condition is \(x>1\) or \(x<-1\).” The paragraph above has just said that a necessary and sufficient condition is an equivalence, so both directions have to be justified. Write the two directions for \(x<-1\), in the same style as the check for \(x>1\). The statement itself is true, and Exercise 0.1 already writes both directions for \(x^2>4\).

**Exercise 0.2, p. 28, and the odd blocks on p. 67.** Even is defined on p. 4: \(n=2k\) for some integer \(k\). Odd is not defined. Exercise 0.2 asks about integers that are both even and odd, and the solution on p. 32 silently takes odd to mean \(n=2m+1\). On p. 67, “Each is odd, because \(k^2-k=k(k-1)\) is even” shows that \(k(k-1)\) is even and does not yet say why \(k^2-k+1\) is odd. Define odd next to even, and use that definition in both places.

**Exercise 2.1, p. 114.** The question asks for the number of solutions in \((\mathbb N^*)^k\). The book fixes \(\mathbb N=\{0,1,2,\ldots\}\) and never defines the star. The same symbol returns in Niven’s argument in Chapter 8. Write \(\{1,2,\ldots\}^k\), or define \(\mathbb N^*=\{1,2,\ldots\}\) where \(\mathbb N\) is introduced.

**Chapter 1’s promise, p. 72, against three exercises.** The chapter says the exercises use only this chapter, except where a later chapter is named.

- Exercise 1.17(b), p. 75, asks the reader to deduce \(\sum_{n\ge 0}1/F_{2^n}=(7-\sqrt5)/2\). The finite identity is proved here. The solution on p. 88 says the language of the limit is in Chapter 3. Say that in the exercise. The closed form is right: the partial sums tend to \(3-1/\varphi\).
- Exercise 1.18, p. 76, is the Erdős–Heilbronn conjecture at three stars. The solution uses the nullstellensatz problem in Chapter 3. Name that problem in the exercise.
- Exercise 1.20 names the complex exponential and Chapter 5, then uses Cauchy–Schwarz, Theorem 9.4. Name Chapter 9 in the exercise. (The missing square root is the must-fix above.)

**Field guide, p. 475.** “This is why a prime value at one point of an arithmetic progression forces composite values further along the same progression.” The theorem underneath is the right statement: a non-constant polynomial with integer coefficients takes non-prime values for infinitely many \(n\ge 0\). “Composite” is a stronger word, and it fails. For \(f(n)=41-n\), one has \(f(0)=41\) prime, then \(f(41)=0\) and \(f(82)=-41\), neither of which is composite. The \(41k\) family for \(n^2+n+41\) really is composite, and the proof already says “not prime” when that is all it has earned. Use “not prime” in the sentence before the theorem.

**Copyright page, against About the Cover, p. 489.** The copyright line says the tree was “computed from the first \(8{,}000\) integers.” The colophon starts at \(2\) and stops at \(8{,}000\), and it draws a value past \(8{,}000\) only when an orbit climbs there. Make the copyright line say “from \(2\) up to \(8{,}000\).” The rest of the note is accurate, including the orbit of \(27\).

**Text layer, about a hundred lines, worst on p. v.** On those lines the PDF’s text has no space characters, so copy, search, and a screen reader run the words together. Three lines of the preface’s thesis paragraph do this (“and no pile of examples settles that” is stored as one long token), and so does the opening line of the image credits on p. 487. The ink still separates the words: the rendered preface and the pause box on p. 277 read normally. Rebuild the reading PDF so the text layer matches the ink. Font expansion is the likely cause. This does not change the prose.

**Solution of Exercise 10.21, the note “Where it leads.”** “One finds numerically \(1/u_n^2-n/3\) equal to \(2.19\) at \(n=10^3\) and \(3.57\) at \(n=10^6\).” Those two decimals are the iteration that starts at \(u_0=1\) (about \(2.193\) and \(3.573\)). Exercise 3.4 allows every start in \((0,\pi/2]\). From \(u_0=\pi/2\) the same quantities are about \(1.86\) and \(3.24\). The rise of about \(0.46\) per factor of ten is real for every such start. Name \(u_0=1\).

**Image credits, p. 487.** The three workshop photographs are described as public-domain images distributed with scikit-image 0.22.0, and the rocket is tied to Flickr image 16511594820. Confirm that item’s current licence before a book for sale repeats “public domain.” NASA’s portrait of Eileen Collins and the Hubble release are not the doubtful case.

**Voice, local.** The failures in the next section are worth rewriting. They are sentences, not chapters. The volume as a whole already sounds like a friend teaching.

## NICE-TO-HAVE

**Chapter 0.** The language chapter is numbered 0, on purpose, and the preface, the contents, and the later cross-references all use that number. A reader opening the contents can still think a chapter fell out. One sentence in the preface, that the language chapter is numbered 0 because the counting of proofs starts at the next one, would settle it. Renumbering the book to start at 1 would touch every cross-reference for a cosmetic gain.

**p. 27, the workshop.** The label “Mission” sits above a clear job. Drop the label. The staged hints already tell the reader what to try.

**p. 45, opening of Chapter 1.** “The four proofs need a way to write a sum, a difference that makes a sum collapse, induction, and the numbers that count subsets.” Each item names a job, so this is a map rather than a pure menu. It still arrives before any of those objects has been used. The cube identity two paragraphs earlier is a better door.

## Voice samples

### Passages that work

**Preface, p. v.** “Add up the first ten cubes: \(1+8+27+\cdots+1000=3025\). Now add the first ten numbers and square the answer: \(1+2+\cdots+10=55\), and \(55^2=3025\). The two numbers agree. Try \(n=4\) and they agree again: both sides are \(100\). Do they agree for every \(n\), or only for the ones you happened to try?” A number, then the same number a second way, then the question a proof has to answer. Nothing is praised.

**p. 6.** “You unpacked a word, calculated, and packed the word up again. That is a direct proof.” The definition of even has just been used twice, with the witnesses \(k\) and \(2k^2\) named. The sentence says what the reader did.

**p. 51.** “The name comes from a telescope sliding shut. You do not get a closer look at the middle terms. You get rid of them.” The joke is the mathematics. The next sentences tell the reader how to hunt for the difference \(v_{k+1}-v_k\).

A fourth, because the field guide earns it. **p. 475.** “Forty recorded primes are a long list. They are still a list.” That is the preface’s standard, applied in public to \(n^2+n+41\), after \(f(40)=41^2\) has been factored by hand.

### Passages that fail

**Preface, p. vi.** “Along the way you will meet induction and binomial coefficients, counting, limits and series, complex numbers and roots of unity, polynomials, linear algebra, calculus, inequalities and convexity, and first probability.” This is the contents, poured into one sentence. The following sentence gives every item the same job. A map belongs here only if each stop says what it is for, as the assumptions list on the previous page already does.

**p. 389, opening of Chapter 9.** “The same square, rewritten for a graph, for two lists, and for a series, produces Jensen’s inequality, the comparison of means, Cauchy–Schwarz, Hölder, the power means, and Minkowski’s triangle inequality.” The two numbers \(1\) and \(4\), in the sentence just before, are the right opening. This sentence then assigns one square the work of the whole chapter. The chord produces Jensen. Young’s areas produce Hölder. Carleman’s \(e\) comes later, from a weighted geometric mean and the tangent to \(\ln\). Let each tool arrive when it is used.

**p. 27.** “Mission and staged hints. Prove both assertions.” “Mission” is a worksheet stamp. The next lines already say what to prove, and the hints already say how to start. A friend would start with the inclusion.

## Design, pacing, and the front of the book

The design does not block publication. Part pages, chapter openers, epigraphs, margins, running heads, and the contents are the system that was approved, including the air under the band. Formal statements sit in the coral-top boxes. Workshops, pause boxes, and the split between “How to find it” and “Write-up” do the pedagogical work the house style asks for: a small case, a failed attempt, then the argument. Figure captions that were checked state a takeaway (the domain is part of the question; the telescope cancels the middle; forty primes and then a square).

Pacing is honest about its ambition and slightly dishonest about three exercises, which is the should-fix on Chapter 1’s promise. The main text builds each tool before it is used. The three-star and late two-star problems at the end of Chapter 1 reach a polynomial method, a learning-theory lemma, and an exponential sum over a finite field. Sauer–Shelah is proved from Pascal’s rule, so it can stay. Heilbronn and the bilinear sum need a sentence that names the later tool. The field guide is a method, not a syllabus: write the sentence, try a number, keep a counterexample, and know which chapter already owns an object of that shape.

The front matter is in good order. The series page lists Volumes 1 through 15 with the current subtitles. The title page carries *Proof, Problem Solving and Mathematical Thinking*. The preface tells a reader how to use the stars, the workshops, and the field guide, and it points to Volume 2 by name. About the Cover passes the jacket test. The copyright line is the one sentence that disagrees with it.
