# Second review of the Volume 7 scored-read fixes

12 November 2026. This pass reads the diffs against the issue log in the Volume 7 scored read. It is not the writer pass.

Heads reviewed:

- Volume 7 in the volume: `846e1c9e8b6a930627bf4c422fa440dfe0374bd8`
- Downstream citations: `b32714113a98333cdd7ed00b5e9b3343ffc12018`

The statement list of Volume 7 was regenerated after the edits. The 308 printed numbers, kinds and labels are the same as before the edits. No numbered environment was added.

## In the volume

| ID | Severity | What was checked | Verdict |
|---|---|---|---|
| V7-01 | major | The third column of the debts table is ragged-right. The theorem numbers were not changed. | Accept |
| V7-02 | major | The layer-cake identity is proved in the text immediately before Theorem 12.4, for a simple function and then by monotone convergence. The proof of (e)⇒(a) cites that paragraph. It is not a new numbered statement, so Chapter 8's numbers stay put. The exercise and its solution remain. | Accept |
| V7-06 | major | `chapters/index.tex` lists the 80 captioned statements, with `\ocindexpage` on their labels, and `main.tex` inputs it in the back matter. | Accept |
| V7-07 | minor | \(x=0\) is the zero of the field morphism. For \(x>0\) the step \(h\) is \(\min\bigl(1,(x-s^2)/(2s+2)\bigr)\), and a rational is chosen inside that room. The opposite inequality is the same estimate. | Accept |
| V7-08 | minor | Part (f) names the integral as the one Volume 1 admitted, and points at Theorem 8.10. Parts (a)–(e) still do not use it. | Accept |
| V7-09 | minor | The nine pairs were recomputed: every \(p\) for \(2\le q<8\), and the convergents for \(q\ge 8\). The list is \((5,2),\ (6,2),\ (8,3),\ (11,4),\ (19,7),\ (193,71),\ (2721,1001),\ (49171,18089),\ (1084483,398959)\). The checking script now searches every nearby \(p\), and it matches. \(|e-3|>1/(8)\) was checked, so Legendre does not delete \(6/2\). | Accept |
| V7-10 | minor | The parenthetical already builds a \(2\varepsilon\)-net of the value vectors. The next sentence and the display now say \(2\varepsilon\) and \(4\varepsilon\). The converse, which starts from an \(\varepsilon\)-net of functions, is still \(3\varepsilon\). | Accept |
| V7-11 | minor | \(\operatorname{Log}\) on the right half-plane is defined from Theorem 2.16(e): unique argument in \((-\pi/2,\pi/2)\), then \(\ln|w|+it\). | Accept |
| V7-12 | minor | \(3^t\) is odd by induction, and strictly increasing, so equal prime powers force equal exponents. Volume 2 is not cited. | Accept |
| V7-13 | minor | The cover proves the coordinate hyperplane is null. The rotation is named as a fact of Chapter 9 and is not used for the faces of a box. | Accept |
| V7-14 | minor | Hardy's \(ab\ge 1\) is marked quoted. The figure is \(a=1/2\), \(b=3\), so \(ab=3/2\), which meets Hardy and not Weierstrass. | Accept |
| V7-15 | minor | Each of the twelve other source lists now has the same contents line the Jordan list already had. | Accept |
| V7-16 | minor | Problems 13.4 and 13.8 are marked with three stars, which is the grade the preface already defines. | Accept |
| V7-17 | minor | \(0.9^{100}=2.656\times 10^{-5}\). The text prints \(2.7\times 10^{-5}\). The script now checks that figure within 2 percent. | Accept |
| V7-19 | minor | \(c\) is the right endpoint of the open interval that contains \(a\), so that interval contributes nothing to \([c,b]\). | Accept |
| V7-20 | minor | The sentence now uses the bijection from the compact quotient \(\mathbb R/\mathbb Z\) onto \(S^1\), and says the maps from \([0,1]\) are not bijective. | Accept |
| V7-21 | minor | The write-up uses \(R>\sum|c_j|\) as well as \(R>1\), both of which follow from \(R>1+\sum|c_j|\). | Accept |
| V7-22 | minor | The right-hand polylines were regenerated from \(\frac12\sin(x+c)+c/4\). The first step of the curve \(c=0\) has slope \(1/2\). Fonts and axes were left as they were. | Accept |
| V7-23 | minor | \(N+nx>0\), then the least natural number above that, then subtract \(N\). The resulting \(m\) satisfies \(nx<m\le nx+1\). | Accept |
| V7-24 | minor | The tolerance is \(1/(k+1)\), including at the index \(0\). | Accept |
| V7-25 | minor | A subset of a finite set is finite by induction, and \(\mathbb N\) is not finite because a finite image has a greatest element. The recursive enumeration then has a nonempty set at each step. | Accept |
| V7-26 | minor | The sentence says the first ten nodes, and that four levels would be fifteen. | Accept |
| V7-27 | minor | Each printed cap dominates the recurrence started at \(0.586\). The true error of \(x_5\) is about \(9\times 10^{-25}\), and the text says 23 matching decimals. The script checks both. | Accept |
| V7-28 | minor | On the chains off \(C\), the thick arrows now run from \(A\) down to \(B\), which is \(h=g^{-1}\). The thin arrows run back, which is \(g\). | Accept |
| V7-29 | minor | An empty factor makes the product empty, and the proof stops. The empty space meets the definition of connected used in the chapter. | Accept |
| V7-30 | minor | The polyline passes through \((\pm 1,1/2)\), and the caption says the value \(1\) is on the open interval. | Accept |
| V7-31 | minor | The nonnegative case is applied to \(|X|+X\) and to \(|X|-X\). | Accept |
| V7-32 | minor | The estimate \(\mu(A\setminus(C\cap K))<2\varepsilon\) is written. | Accept |
| V7-33 | minor | The rays \(]a,\infty[\) and \(]-\infty,b[\) are approximated by a large, or a small, continuity point. | Accept |
| V7-34 | minor | \(\psi(1)=1/\log 3\) and \(\psi(2)=1/(4\log 3)\). Then \(f(1)=f(2)=f(3)\), and \(f\) decreases after that. | Accept |
| V7-35 | minor | The measure is the consistent equal-mass assignment, extended by Carathéodory's theorem. The text says why normalised Lebesgue measure on \(E_k\) does not give equal masses, and names the factor \(2^\tau\). | Accept |
| V7-36 | minor | Generation \(k=1\) is the shared endpoint. Both values are claimed from \(k\ge 2\). | Accept |
| V7-37 | minor | Either norm zero is the case \(0\cdot\infty=0\), which the integral chapter already set. | Accept |
| V7-38 | minor | The label \(2\) was moved off the diagonal point of the \(p=1.5\) curve, into the region between that curve and the circle. | Accept |

## Downstream

| ID | Severity | What was checked | Verdict |
|---|---|---|---|
| V7-03 | major | `volume8-analysis/chapters/ch08-haar.tex:67` already says Theorem 7.5. That is `thm:uniq6`, uniqueness on a \(\pi\)-system. The Volume 8 rewrite put this number in. No further edit. | Accept, already corrected |
| V7-04 | major | `volume8-analysis/chapters/ch05-fourier.tex:201` and `:209` already say Proposition 10.6. That is `prop:simpledense`. No further edit. | Accept, already corrected |
| V7-05 | major | `volume9-shapes/chapters/ch03-forms.tex:347` now says Definition 6.5, after Lemma 6.4. Item 6.1 remains the polygonal Jordan theorem. The same chapter's citation of Lemma 6.4 was left as it stood. | Accept |
| V7-18 | minor | `volume9-shapes/chapters/ch01-manifolds.tex:539` now cites Theorem 7.10. That theorem defines outer measure as the infimum of the total volume of covers by boxes, and a cube is a box. Theorem 7.11 remains the measure of boxes, translation and scaling. | Accept |

A pass over every `Volume~7, Theorem`, `Proposition`, `Lemma`, `Corollary` and `Exercise` in Volumes 8–15 compared the kind with the printed statement of that number. The only kind mismatch left after the Volume 8 rewrite was the winding-number phrase, which did not use the word Lemma in the citation syntax and so had to be read by hand. Volume 14 does not cite Volume 7. The same pass did not find another sentence whose claim is a different theorem from the number it prints.
