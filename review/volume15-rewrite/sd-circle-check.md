# Written confirmation: the proof of `thm:sd` does not rest on Volume 11

Blueprint risk 2 and acceptance requirement: "A written confirmation that the proof of `thm:sd` does not use Volume 11, Chapter 11's corollary."

Volume 11, Chapter 11 (`ch11-modphi.tex`, equation `eq:selbergdelange`) admits the Selberg–Delange formula and says it is proved in Volume 15. Its Corollary `cor:unifomega` is derived from that admitted formula.

In Volume 15, `ra-selbergdelange.tex`:

- The premises of Lemmas `lem:hankel`, `lem:logzeta`, `lem:logderivK`, `lem:taupower`, Theorem `thm:sd`, Lemma `lem:eulerprod` and Corollaries `cor:omegasd`, `cor:bigomegasd`, `cor:landau` are: Volume 5, Theorem 9.36 (Gamma); Volume 6, Proposition 6.11, Theorem 6.12, Lemma 7.1, Theorem 1.5, Example 3.11; Volume 14, Lemma 2.2 and Theorem 2.3; Volume 2, Theorem 7.3; and the lemmas of the same file. These are listed in the file's reminder box.
- Between `\section{Hankel's loop}` and `\section{Prime factors: the promise of Volume~11}` the source contains no citation of any volume (checked with `grep "Volume~"` on that range: no match). The internal references in that range are `lem:hankel`, `lem:logzeta`, `lem:logderivK`, and figures.
- Volume 11 is named in four places, all outside the proofs: the introduction (Volume 11 admitted the formula), the section title, the sentence "This is equation (11.1) of Volume 11" after `cor:omegasd`, and the probabilistic reading after it. Each is a comparison. The introduction now says so in words: "The proof below uses nothing from Volume 11; that volume is only a consumer of Corollary `cor:omegasd`."
- `ra-erdoskac.tex` names Volume 11 once, as a consumer.

So the edge Volume 11 → Volume 15 is "admitted, discharged by `thm:sd`", and there is no edge Volume 15 → Volume 11 Chapter 11 in the proof. No circle.
