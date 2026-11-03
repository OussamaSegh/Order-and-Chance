# Volume 2 — Step 7 printed-route and publishing-copy audit

**3 November 2026 · PR #97 (draft) · source-level editorial review**

**Result:** the first-reading route, chapter introductions and exits, field guide, back cover, and KDP listing now describe the same **four-part, eleven-chapter** book with only **Volume 1** assumed. This is an *editorial/source acceptance gate*, not a claim that the latest PDF/EPUB/KDP production has passed.

## Approved print route, with actual mathematical links

The chapter files have historical filenames; the left-hand numbers below are their **printed** numbers from \`volume2-integers/main.tex\`. Every chapter has a new *The next question* paragraph immediately before Exercises, and Chapters 2–11 have a *What carries forward* paragraph at the end of their introduction (before the first numbered section). These are concrete mathematical connections, not generic “next we will” text.

| Printed position | Chapter and source | Carried in from the preceding chapter | Sent forward to the next chapter |
| --- | --- | --- | --- |
| Part I, 1 | Divisibility — \`ch01-divisibility.tex\` | Opening computation from Euclid, Bézout and Volume 1 proof habits | Shared divisors and prime factorisation → infinitude of primes |
| Part I, 2 | Primes — \`ch02-primes.tex\` | Unique prime factorisation justifies a genuinely new factor in Euclid's argument | Recognising divisibility of huge powers → finite congruences |
| Part I, 3 | Congruences — \`ch03-congruences.tex\` | Prime moduli, modular inverses and product reconstruction | Counting invertible classes φ(n) → multiplicative arithmetic functions |
| Part I, 4 | Arithmetic Functions — \`ch04-arithmetic-functions.tex\` | φ(n) as the count of units; factorisation prime power by prime power | Counting units → orders and generators in their group |
| Part II, 5 | Primitive Roots — \`ch05-primitive-roots.tex\` | The φ(n) unit count and modular invertibility | Powers and square classes → quadratic residues and reciprocity |
| Part II, 6 | Quadratic Reciprocity — \`ch06-quadratic-reciprocity.tex\` | Prime-field cyclicity makes the square/nonsquare sign explicit | The root of −1 modulo p → integer representations p=x²+y² |
| Part III, 7 | Sums of Squares — \`ch07-sums-of-squares.tex\` | Reciprocity gives the local condition; an extra construction proves global representation | Local obstructions and complete classification → general Diophantine methods |
| Part III, 8 | Diophantine Equations — \`ch09-diophantine.tex\` | Obstructions, two/four squares, descent and parametrisation | Infinitely many exact integer solutions → Pell and continued fractions |
| Part III, 9 | Continued Fractions and Pell — \`ch08-continued-fractions.tex\` | Infinite-solution Pell problems and exact approximation | Real quadratic norm x²−Dy² → Gaussian/Eisenstein positive norms |
| Part III, 10 | Gaussian and Eisenstein Integers — \`ch10-gaussian-eisenstein.tex\` | Ring-specific norm and factorisation, from the preceding norm equation | Rings and their unit groups → multiplicative characters of residue units |
| Part IV, 11 | Characters, Euler Products and the Sieve — \`ch14-characters.tex\` | Multiplicative structure becomes character homomorphisms and finite filters | **Volume 3 — Symmetry: Groups, Rings and Fields**, with specific residue-group, Gaussian-ring and character examples |

The sequence **Sums of Squares → Diophantine Equations → Continued Fractions → Gaussian and Eisenstein Integers** is now explicit in *both* incoming and outgoing bridges. The reader does not have to infer the legacy \`ch09\`/\`ch08\` filenames or study advanced extensions as prerequisites.

## Reader’s entry and destination

- **Preface:** confirms the four-part route, only Volume 1 prerequisites, optional advanced workshops, and Volume 3 as the immediate next book; Volume 6 is where analytic distribution of primes deepens, Volume 13 where ideals and general \(p\)-adic fields are developed.
- **Last printed chapter:** closes with three explicit examples for Volume 3: the group of units modulo 7, the ring \(\mathbb Z[i]\) in which \(5=(2+i)(2-i)\), and the homomorphism \(\chi_4(3^2)=\chi_4(3)^2=1\). The algebraic language is a destination, **not a prerequisite assumed by Volume 2**.
- **Arithmetic Field Guide:** notation and actionable problem-solving tests now appear before a clearly titled **Optional later-volume preview: ideals and p-adic notation**. The first-use valuation is for nonzero integers and rationals; the extended convention \(v_p(0)=+\infty\) is in the advanced preview with \(\mathcal O_K\), ideals, \(N(I)\), \(|x|_p\), \(\mathbb Z_p\), and \(\mathbb Q_p\). The final field-guide section returns to the **immediate Volume 3 handoff** via a small check of \(\chi_4\) preserving multiplication.
- **Bertrand epigraph:** updated to the same careful historical attribution used in the Step 5 theorem heading, avoiding an unnecessary disputed year.

## Publishing contract verified in source

| Surface | Corrected/preserved contract |
| --- | --- |
| \`main.tex\` and canonical \`common/series-catalog.json\` | Four ordered parts, eleven actual chapter inputs; Volume 2 subtitle *Primes, Patterns and Proofs* |
| \`kdp.md\` | Removed obsolete **fourteen chapters**, false claim that ideals and \(p\)-adics are developed here, and wrong post-characters chapter sequencing; replaced with four parts / eleven chapters, a complete Volume 1 first route, and an accurate closing chapter and immediate Volume 3 sequel |
| KDP description and search keywords | Description **1,922 characters** (maximum 4,000); **seven** keyword phrases, each no longer than 50 characters |
| \`blurb.tex\` | **153 words**; retains the accurate mathematical arc and now mentions all 144 graded exercises and Volume 3 as the immediate continuation |
| Paperback identity | \`main.tex\` retains author-supplied print ISBN **9798167208650**; \`PUBLISHING.md\` already documents KDP-generated page-count-derived wrap and matching printed EAN-13 |
| Volume 3 opening | Its existing preface explicitly recalls Volume 2 residues, primitive roots, characters and multiplicative homomorphisms: the handoff is consistent in both directions |

No content chapter, exercise, hint, full solution, part, figure or printed ISBN was deleted. No format, trim, print colour, EAN-13 algorithm or packaging procedure was changed. Because the prose can change pagination, **rebuild and match the new print wrap**; never reuse a previous volume-2 cover PDF or the old page-count estimate.

## Source regression and the remaining independent production gates

Added \`tools/test_volume2_reader_route.py\` to test:
1. Eleven input chapters in the approved print sequence and exactly four parts, with a chapter-specific *incoming* bridge in Chapters 2–11 and an *outgoing* bridge in each chapter's pre-exercise text.
2. KDP description promises, no false fourteen-chapter or ideals/\(p\)-adic coverage statements, all seven keyword length limits, and the correct Volume 1 → Volume 2 → Volume 3 contract.
3. Main field-guide toolbox before the optional later-volume definitions, with \(v_p(0)\) and ideal/\(p\)-adic notation only in the preview.
4. The ISBN, canonical subtitle, preface, 153-word blurb, preserved exercises and explicit Volume 3 exit.

A separate independent source scan after the final bridge edits confirmed **11 chapters, 144 original exercise blocks**, exactly one pre-exercise forward bridge per chapter, the ten correct incoming bridges, and the last chapter's immediate Volume 3 route. The suite is part of the global CI Python test discovery; **source scan is not an actual CI result**.

**Still to complete:** (i) a fully green run on the latest commit; (ii) Step 8 regenerated PDF, print interior, EPUB, HTML, cover and rendered visual/technical QA; (iii) final Step 9 KDP Previewer/Kindle Previewer account/device review, ISBN association, and physical print proof. Step 7 does not waive any of them. **Keep PR #97 draft and unmerged.**
