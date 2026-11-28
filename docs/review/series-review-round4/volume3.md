# Volume 3 — Symmetry

**Score: 8/10.**

The round-3 repairs hold. The Smith form still identifies the determinantal ideals, and the diagonal is still unique up to a unit. The cube count, the five groups of order \(8\), the simplicity of \(A_n\) for \(n\ge 5\), the Sylow census below \(60\), the cyclotomic minimal polynomial, the \(A_5\) table, the finite subgroups of \(SO(3)\), Wielandt’s bound, the Paley Gauss sum, both Paley block products, and the Lucas–Lehmer argument were read as proofs and hold. Seven sentences still skip a sign, a comparison, or one step of an isomorphism.

**Counts.** 0 critical, 0 major, 7 minor. `V3-R4-001` through `V3-R4-003` and `V3-R4-101` through `V3-R4-104`.

**Round-3 follow-up.** 9 resolved, 0 partial, 0 open, 0 regressed.

**How this was read.** Book order in `volume3-symmetry/main.tex`, on main at `e5a2a929`, including the four appendices and the afterword. Every chapter file was read, including exercises, hints, solutions, and captions. Each new row was opened at the cited line. No full LaTeX build was run.

## Issues

Paths are relative to `volume3-symmetry/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V3-R4-001 | `chapters/ch08-extensions.tex:1004` | minor | “Writing \(t=\zeta+\zeta^{-1}=2\cos 72^\circ\), we obtain \(t=(\sqrt5-1)/2\).” | The quadratic is \(t^2+t-1=0\), with roots \((-1\pm\sqrt5)/2\). The positive root is \((\sqrt5-1)/2\), because \(2\cos 72^\circ>0\). That choice is not written. |
| V3-R4-002 | `chapters/ch06-rings.tex:501` | minor | “Thus \(r=1\), both sides of the cancelled equation are empty products, and \(u=1\).” | When \(s=1\), the right side is the unit \(u\), not an empty product. The left side is empty, hence \(1\), so \(u=1\). |
| V3-R4-003 | `chapters/ch07-modules.tex:125` | minor | “Because the row and column operations are invertible over \(\Z\), they do not change the isomorphism type of the quotient.” | A matrix in \(\mathrm{GL}_2(\Z)\) is an automorphism of \(\Z^2\). The proof does not say that it carries the column lattice of \(T\) onto the column lattice of \(UT\). The isomorphism is true. Corollary 7.8 writes the same fact later. |
| V3-R4-101 | `chapters/ch12-quaternions.tex:358` | minor | “Summing over the three basis vectors gives \(3a^2-\lvert x\rvert^2\), because \(\sum(x\cdot e)^2=\lvert x\rvert^2\).” | Each diagonal entry is \(a^2-\lvert x\rvert^2+2(x\cdot e)^2\). The sum is \(3(a^2-\lvert x\rvert^2)+2\lvert x\rvert^2=3a^2-\lvert x\rvert^2\). The “because” clause names only the sum of squares. |
| V3-R4-102 | `chapters/ch10-galois.tex:881` | minor | “Provided no denominator in that expression vanishes for these coefficients, the substitutions would build a radical tower.” | Insolubility of \(X^5-4X+2\) is proved. A formula that works for every quintic is defined at these coefficients, so the proviso can be dropped. |
| V3-R4-103 | `chapters/combinatorial.tex:179` | minor | “\(d_i=\lvert A_i\rvert-\lambda\ge 0\).” | \(\lambda=\lvert A_i\cap A_j\rvert\le\lvert A_i\rvert\). That comparison is not written. |
| V3-R4-104 | `chapters/combinatorial.tex:1088` | minor | “\(\dfrac{(19381/10000)^3}{(59/100)^2}<\bigl(1722/625\bigr)^3\).” | The inequality is true and is not reduced to a comparison of integers. The constant \(2.7552\) rests on that step. |

## Round-3 follow-up

The quaternion expansion applies the proved triple-product identity and then antisymmetry. The trace is \(4a^2-1\). A determinant-\(1\) plane rotation has second column \((-\sin\theta,\cos\theta)\). The pentagon eigenvalues are \(2\), \(1/\varphi\) and \(-\varphi\). \(J\) is the all-ones matrix, and \(B=cJ\) is checked on \(\mathbf 1\) and on the sum-zero complement. Hoffman moves \(\tau s\) before dividing. The closed-walk gcd takes a simple cycle as its base. A shortest path has no repeated vertex. Hadamard uses \(n/2\) only after \(2p=n\). Smith minors are \(R\)-multiples of old minors, and the diagonal remains unique up to a unit.

## Not checked

- A LaTeX build, so printed `\ref` numbers were not seen.
- Figures were not re-rendered.
- Journal pages.
