# Volume 3 — Symmetry

**Score: 7/10.**

The book does the job the preface announces. A reader who has Volumes 1 and 2 can follow Lagrange, the isomorphism theorems, Burnside, the Sylow theorems, Gauss’s lemma, the structure theorem for modules over a PID, the tower law, the cyclotomic degree, the Galois correspondence, and the character table of \(\mathfrak S_4\). Round 1’s four unfinished arguments are now in the main text: rank–nullity over an arbitrary field, the splitting sentence in the primitive-element proof, the cyclotomic degree before Gauss–Wantzel, and the stabiliser comparison for the Platonic groups. The score stays at 7 because the proof that a cube rotation fixes the origin is circular, and that count is what later identifies the rotation group with \(\mathfrak S_4\). The other new slips are one sentence each. No displayed formula re-opened here was false.

**Counts.** 0 critical, 1 major, 8 minor. Nine issues, `V3-R2-001` through `V3-R2-009`.

**Round-1 follow-up.** 34 resolved, 2 partial (`V3-003`, `V3-032`), 0 open, 0 regressed.

**How this was read.** Book order in `volume3-symmetry/main.tex`: preface and jacket; Chapters 1–5 (groups); 6–8 (rings and polynomials); 9–12 (fields, Galois, characters, quaternions); Appendices A–D were not read line by line, and that limit is under Not checked; afterword, index, About the Cover. Every chapter file in the main matter was read, including exercises, hints, and solutions, except that the longest solution blocks of Chapters 11 and 12 were read when they carried a number, a citation, or a round-1 repair, and the rest of those solutions were sampled rather than re-derived. Every former major and every new issue below was re-opened in the source. `propositionx` was checked in `common/interior-boxes.tex`: it is an unnumbered theorem environment.

**Style, once.** The banned intensifiers do not recur in the passages read. No notebook is mentioned. Reader-facing copy does not call the book a revision.

## Issues

Paths are relative to `volume3-symmetry/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V3-R2-001 | `chapters/ch01-groups.tex:244` (`prop:cube`) | math | major | “The eight vertices \((\pm 1,\pm 1,\pm 1)\) are exactly the points of the cube at distance \(\sqrt 3\) from the centre, so \(f\) permutes them and sends the centre to the centre. Thus \(f(0)=0\).” | The distance from the centre picks out the vertices only after the centre is fixed, and the sentence then concludes that the centre is fixed. The later count uses \(f(0)=0\) to get an orthogonal matrix. The vertices are the points of the cube that are not midpoints of segments in the cube; their average is the centre, and an isometry of the cube preserves that average. The explicit list of \(24\) rotations was checked: \(9+8+6+1=24\). The upper bound is the step this sentence does not finish. |
| V3-R2-002 | `chapters/ch10-galois.tex:416` and `:602` (`prop:cyclodegree`) | reference | minor | “Proposition~\ref{prop:cyclodegree} gives \([\Q(\zeta_n):\Q]=\varphi(n)\).” | The degree is proved in the main text, before the converse of Gauss–Wantzel, so the old dependence on a three-star exercise is gone. The environment is `propositionx`, which is unnumbered, so the label records the previous numbered proposition, `prop:cyclo`. Line 531 says “the statement just proved”, which rescues that one sentence. Line 602, and the later citations at `:1665` and `:1704`, do not. Give the proposition a number. This is the remainder of `V3-003`. |
| V3-R2-003 | `chapters/ch12-quaternions.tex:895` (`prop:solids`); cited at `:24`, `:911`, and `:1165` | reference | minor | “Proposition~\ref{prop:solids} names the groups.” | The stabiliser comparison itself is written and was read: order \(3\) eliminates the cyclic and dihedral groups of order \(12\), and order \(5\) eliminates those of order \(60\). The environment is again unnumbered, so the reference prints the previous numbered theorem, whose statement does not mention a solid. |
| V3-R2-004 | `chapters/ch12-quaternions.tex:1569` (`ex:hurwitz`) | reference | minor | “By the finite-field sum-of-two-squares result (Volume~2, Chapter~7), choose integers \(x,y\) with \(1+x^2+y^2\equiv 0\pmod p\).” | The congruence is the pigeonhole inside the four-square proof, and it holds for primes that are \(3\pmod 4\). The two-square theorem does not give it. The tools line at `:1635` names the pigeonhole. The write-up still calls it a sum of two squares. This is the remainder of `V3-032`. |
| V3-R2-005 | `chapters/ch06-rings.tex:927` | math | minor | “Proposition~\ref{prop:gaussirr} transfers the exclusion to the fraction field.” | `prop:gaussirr` assumes a primitive polynomial. The positive-degree exclusion just above does not. An Eisenstein polynomial can have content greater than \(1\), for instance \(15X^2+10X+10\) at the prime \(2\). Divide by the content, note that the Eisenstein prime does not divide it, and apply the proposition to the primitive part. The monic applications later in the book are unaffected. |
| V3-R2-006 | `chapters/ch11-characters.tex:587` | math | minor | “These two spaces intersect only at zero, since a vector in both would be fixed and sent to zero. Hence \(\operatorname{tr} P\) is the number of orbits.” | The intersection says the sum is direct. The trace equals the number of orbits because \(P\) is the identity on the orbit-sum basis and zero on the complement, so in that basis its diagonal is that many ones. The averages \(14\) and \(130\) match Burnside and do not use the missing sentence. |
| V3-R2-007 | `chapters/ch03-actions.tex:1224` (`pb:touchard`) | math | minor | “All their intersections with \(A\) are equal, because \(\sigma\) fixes \(A\) pointwise. Those intersections must therefore be empty.” | Equality of the intersections does not make them empty. A point of \(A\) in two of the blocks would lie in two disjoint blocks. That is the missing line. |
| V3-R2-008 | `chapters/ch03-actions.tex:1181` | math | minor | “The restriction \(\pi|_W:W\to W_0\) is injective, … and both spaces have dimension \(n-k\). So it is an isomorphism.” | The reminder proves that an injective endomorphism of one finite-dimensional space is surjective. Here the codomain is a different space of the same dimension. Rank–nullity, now proved in the same reminder, gives the image the full dimension. |
| V3-R2-009 | `chapters/ch12-quaternions.tex:940` | math | minor | “in \(A_4\) a sum of linear characters kills \(V_4\).” | The geometric-uniqueness paragraph treats that vanishing as the reason a faithful three-dimensional representation is one of the listed rows. The sum is not written. The classification of the abstract groups, which ends at line 892, does not use the sentence. |

## Round-1 follow-up

| ID | Status | Evidence |
| --- | --- | --- |
| V3-001 | resolved | Rank–nullity over an arbitrary field is proved at `ch03-actions.tex:511`, before `pb:nilpotent`. The exchange step divides only by a nonzero scalar. |
| V3-002 | resolved | `ch08-extensions.tex:1198–1206` splits \(g\), writes \(D=(X-\beta)D_1\), and concludes \(D_1\) is constant because a non-constant polynomial has a complex root. |
| V3-003 | partial | The degree is a main-text proof before the converse. The printed number is `V3-R2-002`. |
| V3-004 | resolved | `ch12-quaternions.tex:898–905` matches stabiliser orders \(3\) and \(5\) against the cyclic and dihedral cases, and cites `ex:cubeS4` for the cube. |
| V3-005 | resolved | Right cosets are defined, and the index-\(2\) case uses the inversion bijection. |
| V3-006 | resolved | The class equation uses \(C_G\). |
| V3-007 | resolved | The reverse semidirect product is written out. |
| V3-008 | resolved | The corollary stops at \(\lvert Z(G)\rvert\ge p\). The classification is the exercise. |
| V3-009 | resolved | Part (b) is marked three stars. |
| V3-010 | resolved | The shuffle pointer says chapter. |
| V3-011 | resolved | The middle binomial coefficients are proved at the first use. |
| V3-012 | resolved | The order-\(4\) fact cites `ex:order4`. |
| V3-013 | resolved | Unique factorisation in \(\Z\) is pointed at Volume 2. |
| V3-014 | resolved | The least index is strictly less than the degree, and the reduction cites Gauss. |
| V3-015 | resolved | One distributivity expansion is written. |
| V3-016 | resolved | The case of a unit on the right is separated before the induction. |
| V3-017 | resolved | \([12/g]\neq[0]\) uses \(1\le 12/g<12\). |
| V3-018 | resolved | The column operation may put a nonzero entry back under the pivot, and the proof returns to the row stage. |
| V3-019 | resolved | \(v_p\) is defined from the UFD factorisation at the point of use. |
| V3-020 | resolved | Addition of constructible lengths is given by the same circle transport as the other operations. |
| V3-021 | resolved | The root bound over an arbitrary field cites the Chapter 1 solution. |
| V3-022 | resolved | \(\psi_d\) is the identity because every element satisfies \(x^{q^d}=x\), and the gcd is a repeated remainder. |
| V3-023 | resolved | In characteristic \(2\), the squared trace is the shift of the sum, so the combination is \(\beta^{2^n}+\beta\). |
| V3-024 | resolved | Irreducibility of \(\Phi_p\) is cited as the exercise, not as a numbered theorem of Volume 1. |
| V3-025 | resolved | The stray bar in the Frobenius identity is gone. |
| V3-026 | resolved | The subjects of “neither” are \(97\) and \(193\). Recomputed: \(65537=97\cdot 675+62=193\cdot 339+110\). |
| V3-027 | resolved | Generation gives \(\sigma(M)\subseteq M\), and the inverse supplies the other inclusion. |
| V3-028 | resolved | A uniform radical expression is distinguished from the specific polynomial, which is handled on its own. |
| V3-029 | resolved | The averaged projection is written, or the paragraph is no longer offered as a second proof without the sums. |
| V3-030 | resolved | The diagonalisation criterion cites Volume 1. |
| V3-031 | resolved | One matrix of each cycle type on the cube is written. |
| V3-032 | partial | The tools line names the pigeonhole. The write-up is `V3-R2-004`. |
| V3-033 | resolved | A finite subgroup of the circle cites the cyclic-multiplicative theorem. |
| V3-034 | resolved | `ch12-quaternions.tex:601` computes the face centres of the tetrahedron with vertices \((1,1,1)\), \((1,-1,-1)\), \((-1,1,-1)\), \((-1,-1,1)\). They are \(-\frac13\) times the vertices, so the dual is the same shape and the rotations agree. |
| V3-035 | resolved | The fast transform display and the sentence describe the same order of operations. |
| V3-036 | resolved | `kdp.md` no longer claims that each appendix is self-contained in a way the preface contradicts. |

The rows `V3-013` through `V3-031`, `V3-033` through `V3-036` record the repairs located in the chapter reading. The four former majors and the two partial items were re-opened in the source for this report. Where a row above compresses a repair that was not re-opened line by line, the status is the chapter reading’s, and the file was checked for the continued presence of the old faulty sentence. None of those old sentences remains.

## Recomputed here

- The cube list \(9+8+6+1=24\).
- \(|\mathrm{GL}_2(\mathbb F_p)|=(p^2-1)(p^2-p)\) agrees with a direct count of invertible matrices for \(p=2,3,5\).
- \(65537=97\cdot 675+62=193\cdot 339+110\), and \(256^2=65536<65537<257^2\).
- The squares modulo \(13\) are \(1,3,4,9,10,12\).

The chapter reading recomputed the necklace counts \(14\) and \(130\), the degree \([\Q(\sqrt 2,\sqrt 3):\Q]=4\), the splitting field of \(X^3-2\) of degree \(6\), the Smith invariants \(2\mid 6\mid 12\) with determinant \(-144\), and the irreducible degrees \(1,1,2,3,3\) of \(\mathfrak S_4\). No mismatch was reported.

## Verified correct

Rank–nullity over an arbitrary field, the primitive-element splitting, the cyclotomic-degree argument through the division in \(\Z[X]\), and the Platonic stabiliser comparison were read as proofs. The converse of Gauss–Wantzel uses that degree and Wantzel’s theorem. The quintic \(X^5-4X+2\) is Eisenstein at \(2\), and the sign changes with \(f'=5X^4-4\) give three real roots. The afterword names Volume 4, *Chance: The Logic of Uncertainty*. About the Cover matches `common/cover-notes.json` for this volume.

## Not checked

- A LaTeX build, so the printed number of `\ref{prop:cyclodegree}` was inferred from `\newtheorem*{propositionx}` and the previous numbered environment, not from a PDF.
- Appendices A–D were not read line by line. The Paley parameters, the PageRank example, and the Oddtown opening were opened. The remaining appendix proofs and the appendix solutions were not.
- Solutions in Chapters 11 and 12 that carry neither a displayed constant nor a repaired citation were sampled, not re-derived.
- EPUB rendering, portrait files, and primary memoirs.
- External enumerations: the number of groups of order \(16\), of order \(1024\), and of the sporadic simple groups.
