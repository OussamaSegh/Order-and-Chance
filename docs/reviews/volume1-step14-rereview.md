# Re-review: Volume 1 after step 14

Independent reading of the repairs squash-merged as #74 at `3f264ba` (`3f264bab27ae57146e73e635c86685526eff1e48`), which landed before the re-review `docs/plan/PROGRESS.md` required. The comparison text is `docs/reviews/volume1-final-grok-review.md` (the PDF at `7fae5a8`). This reading also covers the two items that review left open: the PDF text layer, and the launch photograph. It does not mark the book first-edition ready.

## Verdict on the #74 repairs

**The repairs hold.** The two must-fix lines are no longer false, and the should-fix gaps are filled. Two local sentences in that repair were still loose, and two further local gaps showed up in the same reading: the real Cauchy–Schwarz theorem was being applied to a complex sum, and the Lucas nearest-integer sentence had lost the hypothesis \(n\ge 2\). They are corrected in this pull request. Nothing in the repair asks for a chapter to be rewritten.

### Must-fix

**Exercise `pb:bilinear`, part (a) and (b).** The square root is taken. Part (a) ends at \(\bigl|\sum\sigma(a)\bigr|\le\sqrt{p\,|A|\,|B|}\), and the sentence calls that the claim. Part (b) ends at \(|E|\le\sqrt{p\,|U|\,|V|}\), after \(|E|^2\le|V|(p-1)|U|\le p|U||V|\). Part (c) may then subtract the square root. Part (d) uses that cosine is strictly decreasing on \([0,\pi/2]\), that \(2\pi/9<\pi/3\), and that \(\cos(\pi/3)=1/2\), so \(\cos(2\pi/9)>1/2\).

One sentence in (a) still skipped a factor. The expanded sum equals \(p|B|\), and the \(|A|\) comes from Cauchy–Schwarz. The repair said “the right side is therefore \(p|A||B|\)” and then displayed the squared bound. The display was the right bound. The sentence now names both factors. Checked against the geometric sum: \(\sum_{a=0}^{p-1}\omega^a\) is \(p\) when \(\omega=1\) and \(0\) otherwise, and \(\omega=1\) exactly when \(b=b'\), since \(p\) does not divide \(r\).

The cited Cauchy–Schwarz theorem is the real form. The sums \(\sigma(a)\) are complex. The write-up now multiplies by a complex number of modulus \(1\) so the sum is real and nonnegative, applies the real theorem to those real parts and a list of ones, and uses that a real part is at most the modulus. Part (b) uses the same rotation.

**Determinant reminder, linear algebra.** The condition number is the ratio of the greatest stretch to the least. The absolute value of the determinant is the product of one stretch from each dimension. For \(\varepsilon I\) that product is \(\varepsilon^n\), and the condition number is \(1\). For \(\operatorname{diag}(M,1/M)\) the product is \(1\) and the condition number is \(M^2\). The old sentence, that the greatest and least stretches multiply to the determinant, is gone.

### Should-fix

**\(x^2>1\).** Both directions for \(x<-1\) are written. If \(x<-1\), then \(x-1<x+1<0\), so the product \(x^2-1\) is positive. If \(-1\le x\le 1\), the same product is at most \(0\), split into \(0\le x\le 1\) and \(-1\le x<0\). So \(x>1\) or \(x<-1\) is necessary and sufficient. The boundary values \(x=\pm 1\) give \(x^2=1\), not \(x^2>1\).

**Odd.** Defined next to even: \(n=2k+1\). The witness for \(19\) is \(k=9\). The odd blocks use that definition: \(k(k-1)\) is even, so \(k^2-k+1=2m+1\). The vacuous-truth solution cites the definition instead of a silent \(n=2m+1\).

**\(\mathbb N^*\).** Defined as \(\{1,2,\ldots\}\) where \(\mathbb N\) is introduced, in the preface and again in the language chapter and the sums chapter. The counting exercise can ask for solutions in \((\mathbb N^*)^k\). Niven’s argument can take \(a,b\in\mathbb N^*\).

**Chapter 1’s promise.** The Fibonacci limit names the language of the limit in the sequences chapter. The Erdős–Heilbronn exercise names Alon’s nullstellensatz in that same chapter. The bilinear sum names Cauchy–Schwarz in the inequalities chapter, and the complex exponential in the complex-numbers chapter.

**Field guide.** The theorem still says “not prime”, which is what the proof earns. The sentence in front of it no longer says that a prime value on an arithmetic progression forces composite values in general. For \(f(n)=41-n\) that stronger word fails, at \(0\) and at \(-41\). A later term on the progression of difference \(|f(a)|\) can also equal the prime itself, as with \(f(X)=X^2-6X+7\) and \(f(1)=f(5)=2\). The sentence now stays with \(f(0)=41\) and the two progressions where \(41\) divides \(f(n)\). On those progressions the later values are larger multiples of \(41\), so they are not prime, and none of them equals \(41\).

The Lucas sentence in the beauty note said \(L_n\) is the integer closest to \(\varphi^n\). The proof gives that only for \(n\ge 2\). For \(n=1\), \(L_1=1\) and the nearest integer to \(\varphi\) is \(2\). The note now keeps the hypothesis \(n\ge 2\).

**Copyright line.** The cover credit says “from \(2\) up to \(8{,}000\)”, matching About the Cover.

**Exercise on the sine iteration.** The numerical note names the start \(u_0=1\). The decimals \(2.19\) and \(3.57\) are that start, as review #73 checked. Other starts in \((0,\pi/2]\) are not claimed.

## Text layer

**Cause.** XeTeX does not put a space character in the content stream. An interword space is a position shift. Microtype’s font expansion does not run under XeTeX (the package ignores it), so expansion is not what joins the words. Character protrusion stays on. The joins happen where justification shrinks the glue: the shift becomes shorter than the gap `pdftotext -raw` and PyMuPDF treat as a space. The ink still shows the gap. Poppler 24’s default `pdftotext` reconstructs many of those gaps; `-raw`, and PyMuPDF’s text extraction, do not. On the preface, the thesis line extracted as `TheseriesiscalledOrderandChance`.

**Fix.** In `common/preamble.tex`, EB Garamond keeps its interword shrink at one fifth of its own interword space. On the same preface, one quarter of that space still extracted as separate words, and one third joined them again. Stretch and `\emergencystretch` are unchanged. Fira is left alone: a letterspaced running head inherits that font's shrink, and capping it made the head report an overfull line. The joined words were in the body face. The cap is shared, so later volumes get it when they are next built. It does not change the PDF version, the embedded fonts, or the KDP export path.

A space after inline mathematics can still be dropped (`1/x for` in the preface). That glue is not the text font’s interword shrink. It is recorded here and left alone.

## Launch photograph

The doubtful image was `photos/rocket.jpg`, scikit-image’s copy of Flickr image 16511594820 (DSCOVR on Falcon 9). On 31 October 2026 the Flickr page `https://www.flickr.com/photos/spacexphotos/16511594820/` marks it **CC BY-NC 2.0** (`https://creativecommons.org/licenses/by-nc/2.0/`). scikit-image’s docstring still says the photograph was released into the public domain. The Flickr page is the licence of record. A non-commercial licence does not cover a book for sale. The file is removed.

The replacement is NASA image 6900556, the Apollo 11 Saturn V on 16 July 1969, from `https://images.nasa.gov/details-6900556` and the file `https://images-assets.nasa.gov/image/6900556/6900556~orig.jpg` (SHA-256 `9046233c2c5b0dc88a8f69e016df4c03171d241d95e42de0b8238b58df0b8754`, unmodified, 3000×2380). NASA’s media guidelines, read the same day at `https://www.nasa.gov/nasa-brand-center/images-and-media/`, say that NASA images are generally not subject to copyright in the United States, and that textbook authors may use them without separate permission when NASA is named and the use does not imply endorsement. The same page says NASA insignia are not in the public domain, so the credit does not call this photograph public domain. The image metadata names Marshall Space Flight Center and lists no other copyright holder. No face is the subject. The caption keeps the teaching point: an estimate and a bound on the error. It says the photograph is not an endorsement.

The Collins portrait and the Hubble image were not the doubtful case. Their credits still follow the scikit-image record.

## Voice

The repaired sentences read as a person teaching: a witness for odd, both directions for \(x<-1\), the square root named as the claim. The nice-to-have notes in review #73 (the preface’s list of subjects, the label “Mission”, the opening sentence of the inequalities chapter) are still there. They are not false, and this pass does not rewrite them.

## What this reading does not settle

- A space after inline mathematics can still vanish in extraction.
- Letterspaced running heads are a separate tracking problem. Body text was the failure on page v.
- Volumes 2–15 still use the old volume numbers in places. That pass is another pull request, as is Volume 15’s solution placement.
- This file does not say the book is ready for a first printing. The pull request says what the reviewer thinks is left.
