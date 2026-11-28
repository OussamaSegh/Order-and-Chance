# Volume 3 — Symmetry

**Score: 8/10.**

The book does the job the preface announces. A reader who has Volumes 1 and 2 can follow Lagrange, the isomorphism theorems, Burnside, the Sylow theorems, the structure theorem for modules over a PID, the tower law, the cyclotomic degree, the Galois correspondence, and the character table of \(\mathfrak S_4\). The circular cube proof is now an argument about midpoints and averages. The cyclotomic degree and the Platonic rotation groups are numbered propositions, and the later counters in Chapter 10 moved with them. The appendix proofs, which round 2 did not read line by line, hold. What remains is a one-line reason in a quaternion formula, a Smith-form clause, and six sentences in the appendices. No main theorem re-opened here was false.

**Counts.** 0 critical, 0 major, 9 minor. Nine issues, `V3-R3-001` through `V3-R3-009`.

**Round-2 follow-up.** 9 resolved, 0 partial, 0 open, 0 regressed.

**How this was read.** Book order in `volume3-symmetry/main.tex`: preface and jacket; Chapters 1–5; 6–8; 9–12; then the Perron appendix, the symmetry appendix, the combinatorial appendix, the Paley appendix, the afterword, and the index. Every one of those files was read, including exercises, hints, and solutions. The appendix proofs were read in full; round 2 had left them unread. Every round-2 issue and every new row below was re-opened at the cited line on main at `68261d60`. Chapter 10’s printed numbers were taken from the shared counter in `common/interior-boxes.tex`, not from a PDF. A search of `*.tex` for `Volume~3` followed by a Chapter 10 number, and for `Lemma~10.15`, was run on the whole series. No full LaTeX build of Volume 3 was run for this note.

**Style, once.** The blurb’s identity \(24=1^2+1^2+2^2+3^2+3^2\) is \(24\). It names necklaces, a finite field repairing a message, the quintic \(X^5-4X+2\), and the cube’s character table. The afterword names Volume 4, *Chance: The Logic of Uncertainty*. No notebook is mentioned. Reader-facing copy does not call the book a revision.

## Chapter 10 numbers

Numbering `prop:cyclodegree` and `prop:solids` shifts only the statements that follow them. On this main the shared counter gives:

| Number | Label |
| --- | --- |
| Proposition 10.9 | `prop:cyclo` |
| Proposition 10.10 | `prop:cyclodegree` |
| Theorem 10.11 | `thm:gw` |
| Theorem 10.14 | `thm:radsolv` |
| Theorem 10.15 | `thm:abelruffini` |
| Lemma 10.16 | `lem:dedekind` |
| Proposition 10.17 | `prop:kummer` |
| Theorem 10.18 | `thm:galoiscrit` |
| Proposition 12.6 | `prop:solids` |

Theorem 10.6 is still the fundamental theorem. Proposition 10.9 is still the cyclotomic injection; its proof already contains \([\Q(\zeta_p):\Q]=p-1\) for prime \(p\). Proposition 12.6 is the last numbered statement in Chapter 12, so 12.1–12.5 did not move. Lemma 12.3 is still Euler’s lemma.

The index lines for Abel–Ruffini, Artin, the cyclotomic degree, Dedekind, the fundamental theorem, Galois, Galois’s criterion, Gauss–Wantzel, and Kummer match this list. A search of the series’ `.tex` files found no remaining `Lemma~10.15`. The external citations that name a Chapter 10 number are:

- Volume 8, `ch07-finite.tex:188`, and Volume 10, `ch08-semisimple.tex:351`: Proposition 10.9.
- Volume 10, `ch08-semisimple.tex:356`, and Volume 13, `ch02-ideals.tex:41` and `ch06-local.tex:332`: Theorem 10.6.
- Volume 10, `ch07-groupcoh.tex:110`, and Volume 13, `ch10-cft.tex:33`: Lemma 10.16, Dedekind’s independence of automorphisms.

Those numbers are the current ones.

## Issues

Paths are relative to `volume3-symmetry/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V3-R3-001 | `chapters/ch12-quaternions.tex:351` | math | minor | “expansion of \(qv\bar q\) gives \(\operatorname{tr} R_q=4a^2-1\)” and the skew formula \(4a(b,c,d)\). | The diagonal sum is \(3a^2-(b^2+c^2+d^2)=4a^2-1\), and \(R_{32}-R_{23}=4ab\). The expansion is not on the page. Theorem 12.4 already has the homomorphism and the kernel \(\{\pm1\}\). |
| V3-R3-002 | `chapters/ch12-quaternions.tex:250` | math | minor | “Every real \(2\times 2\) orthogonal matrix of determinant \(1\) has the form” of a plane rotation. | The fixed axis and the invariant plane are proved. The first column is a unit vector, and orthogonality together with determinant \(1\) forces the second column. That sentence is not written. |
| V3-R3-003 | `chapters/ch07-modules.tex:214` | math | minor | “the other terms are old minors up to sign.” | The sentence before this one is the right claim: a new minor is an \(R\)-linear combination of old minors. Adding \(r\) times one row to another produces an \(r\)-multiple, not merely a sign. The ideal inclusion follows from the linear combination. |
| V3-R3-004 | `chapters/linear-ch09-symmetry.tex:512` | math | minor | “eigenvalues \(2\) and \(\frac{-1\pm\sqrt5}{2}\): the golden ratio, once more.” | The golden ratio is \(\varphi=(1+\sqrt5)/2\). The two eigenvalues are \(1/\varphi=(\sqrt5-1)/2\) and \(-\varphi\). The rabbit matrix in the Perron appendix names \(\varphi\) correctly. |
| V3-R3-005 | `chapters/linear-ch09-symmetry.tex:491` | math | minor | “vanishes on \(\mathbf1^\perp\). Thus \(B=cJ\).” | \(J\) is the operator that is \(p\) on \(\mathbf1\) and \(0\) on the sum-zero vectors. \(B\) is zero on that complement, so it is a scalar multiple of \(J\) once the two operators are compared on \(\mathbf1\). The scalar is computed in the next line. The parameters \((5,2,0,1)\), \((13,6,2,3)\), and \((17,8,3,4)\) match \(k=(p-1)/2\), \(\lambda=(p-5)/4\), \(\mu=(p-1)/4\). |
| V3-R3-006 | `chapters/linear-ch09-symmetry.tex:527` | math | minor | “Dividing by \(s>0\) and \(k-\tau>0\) yields \(s\le -v\tau/(k-\tau)\).” | The displayed inequality rearranges to \(0\ge \tau s+(k-\tau)s^2/v\). Because \(\tau<0\), that collection comes before the division. The bound itself is the right one. |
| V3-R3-007 | `chapters/linear-ch07-perron.tex:367` | math | minor | “Consequently the gcd of closed-walk lengths equals the gcd of the finitely many simple cycle lengths.” | Each deletion writes the old length as a sum of two strictly shorter closed-walk lengths, so the gcd of the simple cycles divides every closed-walk length. The process is said to terminate. That sum is not written. |
| V3-R3-008 | `chapters/linear-ch07-perron.tex:1241` | math | minor | “Remove loops from that path until it is simple.” | A shortest path has no repeated vertex. Deleting only the loops \(a_{ii}>0\) leaves a longer directed cycle in place. The conclusion \(A^{n-1}>0\), once a shortest path is padded by the loop at the end, is the right one. |
| V3-R3-009 | `chapters/paley.tex:45` | math | minor | “each of these rows has \(n/2\) plus signs and \(n/2\) minus signs.” | A sum of \(n\) terms \(\pm 1\) is zero only when \(n\) is even. The count \(n/2\) is used before that sentence. The rest of the four-type count then gives \(n=4b\). |

## Round-2 follow-up

| ID | Status | Evidence |
| --- | --- | --- |
| V3-R2-001 | resolved | `ch01-groups.tex:254–256` A vertex is a point of the cube that is not the midpoint of a nontrivial segment. The eight vertices average to \(0\), and \(f\) preserves averages, so \(f(0)=0\). |
| V3-R2-002 | resolved | `ch10-galois.tex:416` The cyclotomic degree is a numbered proposition. It prints as Proposition 10.10. |
| V3-R2-003 | resolved | `ch12-quaternions.tex:895` The Platonic groups are a numbered proposition, the last one in the chapter, Proposition 12.6. The stabiliser orders \(3\) and \(5\) are still the comparison. |
| V3-R2-004 | resolved | `ch12-quaternions.tex:1569` “The pigeonhole step inside the four-square proof in Volume 2, Chapter 7.” The two-square theorem is not cited. |
| V3-R2-005 | resolved | `ch06-rings.tex:927` Divide by the content and apply `prop:gaussirr` to the primitive part. The example \(15X^2+10X+10\) has content \(5\) and is Eisenstein at \(2\). |
| V3-R2-006 | resolved | `ch11-characters.tex:586` In the orbit-sum basis, \(P\) is the identity on those sums and zero on the complement, so the trace is the number of orbits. |
| V3-R2-007 | resolved | `ch03-actions.tex:1224` A point of \(A\) in two of the blocks would lie in two disjoint blocks, so the intersections are empty. |
| V3-R2-008 | resolved | `ch03-actions.tex:1181` Rank–nullity, proved in the reminder at lines 511–515, gives the image the full dimension \(n-k\). |
| V3-R2-009 | resolved | `ch12-quaternions.tex:940` A linear character kills commutators, hence \(V_4\), so a sum of linear characters is not faithful. |

## Recomputed here

- The signed-permutation count \(3!\cdot 2^3=48\), and half of them have determinant \(1\). The geometric list \(9+8+6+1=24\).
- \(|\mathrm{GL}_2(\mathbb F_p)|\) matches a direct count for \(p=2,3,5\): \(6\), \(48\), \(480\).
- Content of \(15X^2+10X+10\) is \(5\). The primitive part \(3X^2+2X+2\) is still Eisenstein at \(2\).
- \(\varphi=(1+\sqrt5)/2\), \((-1+\sqrt5)/2=1/\varphi\), and \((-1-\sqrt5)/2=-\varphi\).
- Paley parameters from \(k=(p-1)/2\), \(\lambda=(p-5)/4\), \(\mu=(p-1)/4\): \((5,2,0,1)\), \((13,6,2,3)\), \((17,8,3,4)\).
- \(1^2+1^2+2^2+3^2+3^2=24\).

## Verified correct

The cube argument, rank–nullity over an arbitrary field, the Touchard disjoint-block sentence, the content step in Eisenstein’s criterion, the cyclotomic-degree proposition, Dedekind’s lemma as Lemma 10.16, the trace of the orbit projection, and the pigeonhole citation in the Hurwitz solution were read as the repairs round 2 asked for. The preface, Chapters 1–5, and the blurb produced no further issue. The four appendices were read through their last lines. Their parameters and the small counts above match. The handoff names Volume 4.

## Not checked

- A LaTeX build, so the printed `\ref` numbers were inferred from the shared counter and the index, not from a PDF.
- Figures were not rendered, apart from the Volume 2 sieve plate in that volume’s note.
- Portrait files, and the day on Gauss’s letter to Olbers.
- The pagination of Hanson–Petridis, and the group counts of orders \(16\) and \(1024\).
