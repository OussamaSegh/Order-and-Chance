# Re-review: Volume 1, *First Principles*

Independent reading of the repairs in `3f264bab27ae57146e73e635c86685526eff1e48` (pull request #74), and of Volume 1 against `docs/WRITING-STYLE.md` and the accuracy rules. Review #73 is `docs/reviews/volume1-final-grok-review.md`. This file does not mark the book first-edition ready.

## Verdict

The two false lines from review #73 are repaired, and the local gaps around them are repaired. I would hand the book to the author as ready for a first printing, with the limits below. The nice-to-have voice lines from #73 are still unwritten. They are sentences, not false mathematics.

This re-review checked every change in #74, re-derived the estimates that change had to take, and checked the numerical claim it added. It is not a second proof of every theorem in the book.

## The #74 repairs

**Exercise 1.20 (a) and (b).** The write-up now ends at the square root. In (a), Cauchy--Schwarz and the complete geometric sum give \(\bigl|\sum\sigma(a)\bigr|^2\le p|A||B|\), and both sides are nonnegative, so the absolute value is at most the square root. In (b), the same completion gives \(|E|^2\le|V|(p-1)|U|\). The step \(p-1\le p\) is honest, and the square root is the claim the exercise asked for. Part (c) may then subtract that root. Part (d) uses that cosine is strictly decreasing on \([0,\pi/2]\), that \(2\pi/9<\pi/3\), and that \(\cos(\pi/3)=1/2\), so \(\cos(2\pi/9)>1/2\). Each angle \(2\pi ab/p\) lies in \((0,2\pi/9]\), so each real part is greater than \(1/2\). The comparison with the bound in (a) then gives a factor at least \(1/12\) for \(p\ge 9\).

**The determinant reminder.** The condition number is the ratio of the greatest stretch to the least. For \(\varepsilon I\) that ratio is \(1\), and \(|\det|=\varepsilon^n\). For \(\operatorname{diag}(M,1/M)\) with \(M\ge 1\) the ratio is \(M^2\), and the product of the two stretches is \(1\). The old sentence said the product of the greatest and the least was the determinant. That is the dimension-\(2\) case only. The new sentence matches the two examples in the box.

**\(x<-1\).** Sufficiency is the same factorisation as for \(x>1\), with both factors negative. Necessity is the closed interval: if \(-1\le x\le 1\), then \(x^2\le 1\). Together, \(x^2>1\) if and only if \(x>1\) or \(x<-1\).

**Odd.** An integer \(n\) is odd when \(n=2k+1\) for some integer \(k\). The witness for \(19\) is \(k=9\). In the odd-block argument, \(k(k-1)\) is even, so \(k^2-k=2m\) and \(k^2-k+1=2m+1\). That is the definition, used where the old sentence had only said that \(k(k-1)\) is even.

**\(\mathbb N^*\).** The preface and the language chapter both set \(\mathbb N=\{0,1,2,\ldots\}\) and \(\mathbb N^*=\{1,2,\ldots\}\). The sums chapter repeats the same pair.

**Chapter 1's promise.** Exercise 1.17 names Chapter 3 for the limit. The Erdős--Heilbronn exercise names the nullstellensatz problem in the sequences chapter. The bilinear-sum exercise names the complex exponential in the complex-numbers chapter and Cauchy--Schwarz in the inequalities chapter. The finite identities stay in this chapter.

**Field guide.** The sentence before the polynomial theorem now says "not prime". For \(f(n)=41-n\) one has \(f(41)=0\) and \(f(82)=-41\), neither of which is composite. The theorem, and its proof, already say "not prime". The check on \(f(n)=-n-2\) is the same distinction.

**Copyright line.** The generated credit now says the Collatz tree runs from \(2\) up to \(8{,}000\), which is what About the Cover already said. The orbit of \(27\) is still \(111\) steps to \(9{,}232\).

**The sine iteration.** Starting at \(u_0=1\), \(u_{n+1}=\sin u_n\), the quantity \(1/u_n^2-n/3\) is about \(2.193\) at \(n=10^3\) and about \(3.573\) at \(n=10^6\). The book prints \(2.19\) and \(3.57\). From \(u_0=\pi/2\) the same quantities are about \(1.859\) and \(3.240\). Naming the start is required. The rise of about \(\frac15\ln 10=0.46\) per factor of ten is the logarithmic term already proved.

## What else was checked

Reader-facing text in `volume1-first-principles` does not call this book a revision of an older edition, and it does not mention companion notebooks. "Revision" in the probability chapter is Bayes' update. "Reordering" in the sequences chapter is rearranging a series. Both are the mathematical uses the copy rule allows.

A search for the banned fillers in `docs/WRITING-STYLE.md` (`delve`, `robust`, `comprehensive`, `seamless`, `leverage`, `tapestry`, `pivotal`, `underscore`, `realm`, and the stock openers "In this section", "It is important", "In conclusion") is empty in the Volume 1 TeX.

Cross-references use Volumes 1 through 15. There is no Volume 0 in the reader-facing text. The pointers that were opened against the other books land:

- Volume 4's crossing lemma is an exercise, as the probability chapter says.
- Volume 5's Chapter 7 is the Gamma chapter, which states Bohr--Mollerup. Its own text points Stirling's series at Chapter 13, and that chapter proves it. Chapter 11 is the complex chapter.
- Volume 3's Chapters 6 and 9 are the rings chapter and the finite-fields chapter.
- The matrix-tree theorem is in Volume 12. The class number of \(\mathbb Q(\sqrt{-163})\) is in Volume 13. Finite projective planes are in Volume 9.

The series notation sheet asks later books to write \(\log\) for the natural logarithm and to keep \(D_n\) for the dihedral group of order \(2n\). Volume 1 defines \(\ln\) in the list of functions it takes as given, and it uses \(D_n\) for the number of derangements. Renaming either one would touch the whole book. The sheet says the convention does not block a local repair. Neither was renamed.

## Text layer

XeTeX, with the fonts this book embeds, draws many word spaces as horizontal shifts and does not put U+0020 in the ToUnicode map. The ink still separates the words. Poppler's default `pdftotext` often invents the spaces from those gaps. A reader who copies the line, and any extractor that trusts the character map, does not. On the preface built from the old setting, the map for EB Garamond has no U+0020, and the thesis line comes out as one token:

```
every𝑛, andnopileofexamplessettlesthat. Youcancheckamillioncasesandthenextone
```

That is `pdftotext -raw` on the preface. Default `pdftotext` on the same file still prints "and no pile of examples settles that", because it measures gaps. The review's "about a hundred lines" are the lines whose gaps fall below that guess. Font expansion is not the cause: microtype on XeTeX enables protrusion only, and the log says so.

`\XeTeXinterwordspaceshaping=2` makes XeTeX shape the word space and map the space glyph to U+0020. A comma, a colon, or a period normally raises the space factor, and XeTeX then omits that following space from the map. Those factors are set back to 1000, so every word space is the ordinary one. Sentence spaces are therefore the same width as the spaces between words. Ghostscript's PDF 1.3 rewrite, the one the print export uses, keeps the mapping.

The setting moves some line breaks. The mathematics and the wording do not change. XeTeX 0.999995 segfaults if the same shaping is left on for this book's contents list, so the contents are set with shaping turned off and the body turns it back on. A few of the fullest lines still lose their space characters under `pdftotext -raw`. Default `pdftotext` separates them. There is no overfull line in the log, and the layout check reports 456 whole boxes, none overflowing.

## The launch photograph

The doubtful credit was the workshop photograph of a Falcon 9, tied to Flickr image 16511594820 and described as a public-domain file from scikit-image 0.22.0.

On 31 October 2026 the Flickr page `https://www.flickr.com/photos/spacexphotos/16511594820` redirects to `https://www.flickr.com/photos/spacex/16511594820`. That page's licence link is `https://creativecommons.org/licenses/by-nc/2.0/`, and the visible licence is CC BY-NC 2.0, "Some rights reserved". NonCommercial does not allow a book offered for sale. scikit-image's documentation still says the file was released into the public domain. The Flickr page is the source, and it does not say that.

The photograph in the book is now NASA image NHQ202403030014, the Crew-8 launch on 3 March 2024, taken by Aubrey Gemignani. The file is NASA's original JPEG, unmodified, SHA256 `fe7da3137f0fbcc2d19972fe9879d3a1ca23932cbff47a37f3158b0fe5165e3b`. Its EXIF copyright line is `(NASA/Aubrey Gemignani)`. The NASA metadata sidecar records `UsageTerms: Released to Public`. NASA's media guidelines, read the same day at `https://www.nasa.gov/nasa-brand-center/images-and-media/`, state that NASA images are generally not subject to copyright in the United States, and that textbook authors may use them without implying endorsement. The caption says it is not an endorsement. The Collins portrait and the Hubble file were not the doubtful case, and they are unchanged.

## Still open

The voice lines review #73 marked nice-to-have are still in the book. The preface still lists the chapters in one sentence. Chapter 9 still gives one square the work of the whole chapter. The least-squares workshop still has the label "Mission". None of these is a false line.

This file does not say the book is first-edition ready. That is the author's mark.

## Built PDFs

`./build.sh volume1-first-principles` produced a 499-page print interior and a 500-page reading PDF. The layout check passed. The KDP interior check passed, including five transparent pages flattened at 600 ppi. The launch photograph is embedded at 1632 ppi.

Before, on a preface typeset with the old space handling, `pdftotext -raw` gave:

```
every𝑛, andnopileofexamplessettlesthat. Youcancheckamillioncasesandthenextone
```

After, both built PDFs give the same line with spaces. Reading PDF, page 6, `pdftotext -layout` and `pdftotext -raw`:

```
every 𝑛, and no pile of examples settles that. You can check a million cases and the next
```

Print PDF, page 5, the same two commands, the same line. Default `pdftotext` on the print PDF also keeps the next tight sentence, the one copy-and-paste still glues:

```
four properties: it is linear, it preserves order, it adds over adjacent intervals, and a constant
```

`pdftotext -raw` on that second line still returns `fourproperties:itislinear,...`. Default `pdftotext` does not. A search of the whole print PDF with default `pdftotext` finds no English words run together. The long tokens that remain are German titles such as Mannigfaltigkeitslehre.