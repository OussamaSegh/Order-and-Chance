# Volume 4 round-1 strong-Markov repair, second reading

Mathematics confirmed at `cadb8f2ce5f3b4f28426be860f7ab6706363af7d`. This note does not change the mathematics. No LaTeX build was run for this reading.

A first draft bounded the stopped position by a union over the level-\(n\) grid. That bound grows like \(2^n\) and was not committed. The committed paragraph chooses the level \(N\) before the threshold \(A\). Theorem `thm:levy` supplies the modulus on each unit copy. On \([0,R]\) there are at most \(R2^N+1\) samples. The union bound tends to \(0\) as \(A\to\infty\) and does not depend on the later index \(n\). On \(\{\tau_n\le R\}\) the stopped time \(r\wedge\tau_n\) is at most \(R\). The two-sided tail carries the factor \(2\). Doob's inequality is not used.

No numbered statement moved. No claim was weakened.
