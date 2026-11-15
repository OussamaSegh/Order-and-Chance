# Chapter 11 separate source review

Reviewer: `independent_review`, separate from the chapter writer.
Starting main: `59014a9aad3454ad60786c6549c81fcac88df9df`.
First reviewed rewritten source SHA-256:
`7cc95156e783221ee4ecf7d66c8490e66b53c33939838db9a3d6e8b6f872d30f`.
This review reads the complete source, including every original and new exercise,
hint and solution, and both new figure sources. It does not claim a build,
rendered-page/EPUB inspection, final whole-volume acceptance or CI success.

## Statement comparison

All ten original numbered formal statements were compared with their full
baseline content in `starting-statement-content.json`:

| Label | Result |
| --- | --- |
| `prop:unitarytrick` | Inner product and complete reducibility retained; zero-dimensional case explicit. |
| `thm:schurorth` | Full coefficient formula and character consequences retained; representative convention fixes formerly unspecified equivalent-but-unequal case. |
| `thm:peterweyl` | Uniform density, complete coefficient basis, full Fourier/Plancherel formulas and class-character basis retained under the original compact matrix-group standing scope. |
| `def:schurpoly` | Same alternant quotient, with polynomial extension at repeated eigenvalues explicit. |
| `lem:alternants` | Integral Laurent coefficients/leading term, unique alternant expansion and full orthogonality retained. |
| `thm:weylchar` | Every dominant integer weight, uniqueness/exhaustion and exact dimension product retained. |
| `prop:powertraces` | Every original positive frequency, zero means and min(k,n) covariance retained. |
| `lem:pieri` | Every dominant integer weight and precisely the legal one-box additions retained. |
| `thm:traces` | Full character expansion, permutation count and a! range retained; integer and a=0 conventions explicit. |
| `cor:gaussiantrace` | Both original real-projection distribution limits retained. |

No valid hypothesis, quantifier, conclusion or equality case was found lost.
The six original exercises retain their mathematical requests, subject to the
boundary clarification below for `ex:dims`; all ten exercises have useful hints
and complete idea/writeup solutions. The domino rule now explains how integer
weights are shifted to draw diagrams, rather than treating negative rows as cells.

## Proof and prerequisite checks

The averaging proof handles positivity by a positive compact minimum and splits
finite-dimensional spaces by decreasing dimension. The Schur averaging indices
match the coefficient formula. Peter-Weyl uses conjugation-stable coefficient
algebras, separation by the defining matrix representation, actual complex
Stone-Weierstrass, regular-measure continuous approximation (including empty
closed/complement cases), Hilbert completeness and invariant projections.
The general compact-group extension is now explicitly quoted.

Weyl's character proof uses integral alternants and norm one to obtain precisely
one character, then class-function completeness for existence. Repeated
eigenvalues and the real-q evaluation path are justified. The exterior/symmetric
power identifications have local alternant/partial-fraction arguments, avoiding
unproved Schur-Weyl duality. Power-trace surviving indices, Pieri collisions,
standard-tableau path multiplicities, row/column transpose and the Gaussian
moment calculation all follow with the claimed ranges.

Actually read earlier prerequisites include Volume 7 Theorem 4.19(b)
(Stone-Weierstrass), Volume 8 Theorem 13.11(c) (circle characters), Volume 6
Lemma 9.6 (Gaussian moments imply convergence in distribution), Volume 9's
Weyl integration/density material, and Volume 1's Wallis integral material.
The printed target numbers were checked with the existing statement walker.
No result from Volumes 11–15 is used as a premise.

## Added exercises and illustrations

- `ex:v10new-ch11-statistic`: rotation kills distinct signed frequencies;
  diagonal terms give sum min(abs(k),n) abs(c_k)^2. The concrete variance
  1/2+2 min(2,n), including n=1, and independent variance 5n/2 are correct.
- `ex:v10new-ch11-detmoment`: the balance nr+a-b=0 is necessary by rotation
  and sufficient. For r nonnegative, character orthogonality gives the positive
  sum of f^lambda f^(lambda+(r^n)); at least one partition exists. Conjugation
  handles negative r. The one-column coefficient equals one.
- `ex:v10new-ch11-projective`: the scalar centre acts as z^(sum lambda).
  The zero-sum condition is necessary and sufficient for quotient descent;
  the quotient topology proves continuity. The twist condition and n=1 case
  are correct.
- `ex:v10new-ch11-firstfailure`: precisely the identity permutation is excluded
  at a=n+1, giving (n+1)!-1. Markov gives r!/t^(2r) in the stated range.

Both new diagrams teach their respective calculations. The growth graph has
exactly one path to (3) and two to (2,1), excluding (1,1,1); the variance plot
shows min(k,4) only at positive integer frequencies and accurately distinguishes
four independent points. Their sources use the approved palette. Rendered label
fit, scale and caption placement remain for production inspection.

The complete original weights figure block is byte-for-byte present and its
original source hash is unchanged:
`ba217df21e72e7425b08fb1e4a85b84d2ced8ba13f95d4c8d119ae33494d12bc`.
All original labels occur. Source counts are three figures (one original plus two
new) and ten exercises (six original plus four new), with additions after the
respective original lists. Printed-number verification awaits the final build.

## Findings sent to writer; repair recheck pending

1. Remove stray commas in exponents `overline{X_n}^{,l}` and
   `overline{operatorname{tr}U}^{,b}`. They alter the typeset formulas.
2. The growth caption should call E|tr U|^6 the sixth absolute moment, rather
   than the ambiguous third trace moment.
3. Preserve valid n=1 symmetric/exterior dimension tasks in `ex:dims`; impose
   n at least two only for the final adjoint-weight request. Handle exterior
   powers beyond n as zero if that range is discussed.
4. Closing bridge should use the actual full subtitle of Volume 11:
   Martingales, Limits and Ergodicity.

The parent has acknowledged these repairs. No other blocking mathematical flaw
was found in this chapter at this review checkpoint. Final status requires
reading the repairs and rechecking the exact final source after any later edits.
