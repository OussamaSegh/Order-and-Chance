# Mathematical review ledger — Volume 13

**Not a proof certificate.** Independently reviewed theorem-by-theorem derivations are still required. Automated preservation, arithmetic and typesetting tests cannot establish their mathematical truth. The preceding PR #229 did not confer independent proof certification.

High-risk dependencies and classification to check: integral closure/Dedekind factorisation (Volume 10); Minkowski, Hermite and Dirichlet units; Kummer's first case versus the quoted second case; Hensel, Ostrowski, Hilbert reciprocity, Hasse–Minkowski; analytic class number formula; Chebotarev in **Dirichlet density** versus unproved natural density; Tate's adelic Poisson argument; Artin reciprocity, existence, Hilbert class field (**admitted**); general Weil bound, Mazur, Sato–Tate, Eichler–Shimura and modularity (**quoted**); all-century Fermat claims (quote without proof). Original proof and solution status is **NOT FULLY REVIEWED** until explicitly checked.

For each important result record exact quantified statement, proof dependencies, independently checked derivation, boundary cases and counterexamples, primary textbook/paper sources, correction and human reviewer status. No external mathematical certification was obtained.


## Independently checked correction: Tate's theorem, pole statement

**Statement:** \`volume13-arithmetic/chapters/ch09-tate.tex\`, Theorem \`thm:tate\` (its number and label are preserved), for arbitrary Schwartz test function \(f\) on the adeles and a Dirichlet character \(\chi\).

**Original error:** The printed claim that a trivial character *has* simple poles at both \(s=1\) and \(s=0\) is false without \(f(0)\ne0\) and \(\widehat f(0)\ne0\). The nonzero test function \(f=f_\infty\otimes\mathbf1_{\widehat{\mathbb Z}}\), \(f_\infty(x)=xe^{-\pi x^2}\), is odd under \(q\mapsto-q\). In the trivial-character sum \(q\in\mathbb Q^\times\), opposite terms cancel, so the zeta integral is identically zero and has no poles. The zero test function is an even simpler boundary case.

**Derivation:** The existing proof obtains equation \`eq:tatesplit\`, expressing the meromorphic continuation as two entire terms plus
\[
\delta_\chi\left(\frac{\widehat f(0)}{s-1}-\frac{f(0)}s\right).
\]
It follows rigorously that the **only possible** poles are at \(s=1,0\), each **at most** simple, with the stated residues. One cannot conclude that a pole is present if its residue vanishes.

**Change made:** Replace only this false existential-pole sentence. No numbering, label, hypothesis, contour computation, functional equation, or other formal result changes. The frozen-source preservation checker encodes this single exact textual exception and continues enforcing byte-for-byte preservation of all other formal blocks. The Riemann-zeta corollary remains a statement of actual simple poles because its specific Gaussian test function has \(f(0)=\widehat f(0)=1\).

**Proof dependencies:** \`lem:Fbounds\` and \`cor:scaledpoisson\` \(\to\) equation \`eq:tatesplit\` \(\to\) \(thm:tate\) \(\to\) \`cor:riemannFE\`. This correction is an independently rederived author-side boundary-case check, **not** certification of the entire Tate argument or the other original theorems.
