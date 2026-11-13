# Volume 6 rewrite — findings and fixes

Date: 13 November 2026. Branch `cursor/volume6-complete-rewrite-5aa1`. The rewrite is the twelve chapter commits `81d3356a` through `eb37cbf2`, plus the preface `5f837b99`.

## What was checked

- Every old `\label` is still present, in the same order. The numbered environments before the new exercises match the pre-rewrite sequence, so theorem and exercise numbers cited by later volumes did not move. The only added environments are four exercises at the end of each chapter.
- No duplicate labels in `volume6-crossroads`.
- Every exercise environment has a hint and a solution.
- Every `\fig` name has a file.
- The defects in `docs/review/volume6-independent-scored-read-2026-11-13-reread.md` that were already repaired on `main` are still repaired: the \(\tau\) warning, the quoted Piltz error, the cotangent comparison, the \(\lambda>2\) restriction, the Gaussian-moment clause in Lemma 9.6, Rankin's quotient \(19.5\), and the conditional \(99.59\%\) on the jacket.
- Recomputed: \(\prod_{p\le 1000}(1-1/p)=0.080965\) (printed \(0.0810\)); \(2e^{-\gamma}-1=0.1229\) (about \(12.3\%\)); \(\tau(n)\) for \(n\le 12\); the three Cramér-window means at \(x=e^{10}\) (\(3.200\), \(9.998\), \(99.78\)); the class sums of \((\log p)/p\) up to \(30\); \(\mathfrak S(\{0,d\})\) for \(d\le 6\) with \(C_2=0.66016\); the ratio \(\log T/\log(T+2)\) at \(\log x=100\).
- The identity in Exercise `ex:m6d`, relating \(\psi(x)\) to the remainder in Mertens's first theorem, was re-derived from Abel summation.
- \(\bigl(\frac{2}{p}\bigr)=1\) for odd primes \(\equiv 1\) or \(7\pmod 8\), as the solution of `ex:mod8share` uses.
- Local build `./build.sh volume6-crossroads`: layout check (335 boxes, max height \(391.1\) pt), interior style, reading PDF, KDP print PDF (377 pages), paperback cover, EPUB media check. EPUB is 28 MB, 48 plates at 1800 px, formulas on the em baseline.

## Fixes

| Where | What was wrong | Fix |
| --- | --- | --- |
| `ch12-modular.tex`, the product for \(\tau(n)\) through \(q^3\) | The aligned display was \(13.5\) pt wider than the measure. The algebra was right. | Broke the line after the \(q^2\) term. The layout check then passed. |
| Chapter 7, proof of `thm:pnterror` | The previous review found a display that used \(\log T\) where the sentence had proved \(\log(T+2)\). | The rewrite states the exponential with \(\log(T+2)\), then uses \(\log T/\log(T+2)\to 1\) to take the factor \(\frac12\). |
| Chapter 10 | An earlier draft of the book claimed the short-interval law for every \(\lambda>1\). | The rewrite keeps the law for \(\lambda>2\) only, and says the gap theorem forces liminf \(0\) for \(1<\lambda\le 2\), in the text, the figure caption, `ex:shortmodel`, and `ex:lambdaless`. |

No wrong constant, sign, or index was found in the statements that were recomputed. The new exercises that were read line by line (`ex:m6a`–`ex:m6d`, `ex:avg6a`, `ex:avg6b`, `ex:count80`, `ex:weight30`, `ex:mod8share`, `ex:schi4`, `ex:balanceT`, `ex:coinprobs`, `ex:threeS`, `ex:windowe10`, `ex:lowtau`) match the theorems they cite.

## Voice

The openings were rewritten as a concrete picture or a small count, then the theorem. The preface was rewritten in the same voice and still names the two admitted facts (the functional equation of \(L(s,\chi)\) in one remark of Chapter 7, Tonelli in one solution of Chapter 12). The word “Journey” on some exercises is the existing tag for a long exercise, not a filler noun. No notebooks, and the book is not described as a revision.

## Not edited elsewhere

Volume 5 citations stay hand-typed. After the parallel Volume 5 rewrite, re-check Theorem 10.8 (\(\xi\)), Theorem 12.4 (\(\eta\)), Proposition 10.6, Corollary 10.9, Theorems 9.15, 9.18, 9.26 and 9.36, and Exercises 5.7 and 6.5.

Volume 8, `ch09-expanders.tex`, still cites Chapter 5 for an error term that Chapter 5 does not prove. The right pointer is Theorem 7.10. That file was not edited.

No photograph was added. The new plates are TikZ, generated in the repository.
