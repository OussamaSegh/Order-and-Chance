# Volume 7 review loop — handoff

Fresh agents continue from this file alone. The book sources live in `volume7-spaces/`. The intent note is `docs/plan/book-07.md`. Do not edit book source on the tracker branch. A Volume 6 loop is running in parallel. Do not touch its branches, including `review/v6-loop-tracker` and `review/v6-round1`.

Round 1 reviewed `af3f9afbaee7b76237f8b9ad085420fda82d328f`. That SHA is `origin/main` at the time of the review. Volume 7 at that SHA is the text scored in round 1.

- Tracker PR: https://github.com/OussamaSegh/Order-and-Chance/pull/331 (draft), branch `review/v7-loop-tracker`. The head is the tip of that branch.
- Round-1 review PR: https://github.com/OussamaSegh/Order-and-Chance/pull/330 (draft), head `7d021f907c2d2948f0a9ec5fe80974645dc2204a`, branch `review/v7-round1`, file `docs/review/volume7-round1-review.md`.

## Goal

Bring Volume 7 to 10/10. The loop is: review, then one small fix PR per issue, then a distinct second reviewer per fix (a note and an issue log in `docs/review/volume7-rN-NNN-review.md` on the fix branch), then a SHA-guarded squash merge once CI is green on the exact reviewed head, then a fresh re-review that also checks every earlier-changed passage for regressions. At most 6 rounds. At the end, merge the review-only draft PRs and the tracker, and confirm main CI is green.

## Rules

- Never fabricate a check, a build, or a CI result. Say what was not checked.
- Never weaken a proof silently.
- Keep theorem numbering stable. If a number must move, update cross-references across the whole series in the same change.
- Do not change caption or diagram typography. Wording and numbers in captions may change.
- Keep numerical checks separate from proofs.
- No KDP uploads, and no force-push to `main`.
- Do not edit other volumes. Wrong numbers in another volume are fixed by correcting the citation in Volume 7, not by renumbering that volume.
- Do not touch the Volume 6 branches.
- Volume 1 sets the chapter counter to \(-1\), so its first chapter is Chapter 0. Theorem, proposition, lemma, corollary, definition, and example share one counter. Check a cross-volume citation against the source before flagging it.
- Jordan is a chapter of Volume 7, so the printed numbers are one chapter later than the plan's "Theorem 8.6 / 8.8". Fubini is Theorem 9.6 and change of variables is Theorem 9.8. Do not renumber them.

## Round and score

| Round | Base SHA | Score | Review | Status |
| --- | --- | --- | --- | --- |
| 1 | `af3f9afbaee7b76237f8b9ad085420fda82d328f` | 8/10 | https://github.com/OussamaSegh/Order-and-Chance/pull/330 head `7d021f907c2d2948f0a9ec5fe80974645dc2204a` | open, not merged |

Score reason, short. One numbered statement is false as written: part (d) of the mean value theorem omits continuity on the interval. Eighteen further issues are local false sentences or quantifiers that do not close. No flagship theorem (Banach, Baire, Carathéodory, Fubini, change of variables, Radon–Nikodym, Jordan, the Khinchin cover) was found false. The round-1 reviewer did not run `./build.sh`.

## Fix PRs

Each branch was cut from current `main` at `ddf23cd89103582fc5879cd3351dfb5b22053df0`. Between the review SHA and that commit, `volume7-spaces/` did not change. None of these pull requests is merged. The fixer did not run `./build.sh` and did not open an Actions log.

| Issue | PR | Head | Status |
| --- | --- | --- | --- |
| V7-R1-001 | https://github.com/OussamaSegh/Order-and-Chance/pull/333 | `0e59353677fd1e13297ec7bf9f8cebd59fa59468` | awaiting second review |
| V7-R1-002 | https://github.com/OussamaSegh/Order-and-Chance/pull/334 | `dd95fb34a09aa797f158621c37f7bbdcf2e1cb9e` | awaiting second review |
| V7-R1-003 | https://github.com/OussamaSegh/Order-and-Chance/pull/335 | `7ef6228b02e45ff1ad86001aad7a06b610f50238` | awaiting second review |
| V7-R1-004 | https://github.com/OussamaSegh/Order-and-Chance/pull/336 | `590a12562b12d24ceeac4951daf9e0febe66d5e4` | awaiting second review |
| V7-R1-005 | https://github.com/OussamaSegh/Order-and-Chance/pull/337 | `faa907594ed4ad48e1a0debe8023f2cb639971ef` | awaiting second review |
| V7-R1-006 | https://github.com/OussamaSegh/Order-and-Chance/pull/338 | `ee5f9171d08a71eca4acb8840be180bfdb1ae34c` | awaiting second review |
| V7-R1-007 | https://github.com/OussamaSegh/Order-and-Chance/pull/339 | `6277012d107bca4844d58bcffa854286e1a9b8c5` | awaiting second review |
| V7-R1-008 | https://github.com/OussamaSegh/Order-and-Chance/pull/340 | `5c51d0995ea165da267f5a0484edbf44ec074a3a` | awaiting second review |
| V7-R1-009 | https://github.com/OussamaSegh/Order-and-Chance/pull/341 | `bdd7723bb6df60d0181dd986510ac2b966791fee` | awaiting second review |
| V7-R1-010 | https://github.com/OussamaSegh/Order-and-Chance/pull/343 | `d5a77e1593a5f34c699e1c23873f3a6186081f0a` | awaiting second review |
| V7-R1-011 | https://github.com/OussamaSegh/Order-and-Chance/pull/344 | `44851861cc89e3e81ca65b214181072cb4f924dc` | awaiting second review |
| V7-R1-012 | https://github.com/OussamaSegh/Order-and-Chance/pull/345 | `bb9036c432c9743476321889b3e84f36804b705c` | awaiting second review |
| V7-R1-013 | https://github.com/OussamaSegh/Order-and-Chance/pull/346 | `7c58ea3eca897d8f032d655709c3db3526faa433` | awaiting second review |
| V7-R1-014 | https://github.com/OussamaSegh/Order-and-Chance/pull/347 | `368ac06253ce45d58255e02131e6934228f65111` | awaiting second review |
| V7-R1-015 | https://github.com/OussamaSegh/Order-and-Chance/pull/348 | `4fb7f248e59eb69309331f62538e7b4a37ab96b6` | awaiting second review |
| V7-R1-016 | https://github.com/OussamaSegh/Order-and-Chance/pull/349 | `f8c2c660c917e41b96e843502002045ba9eb7973` | awaiting second review |
| V7-R1-017 | https://github.com/OussamaSegh/Order-and-Chance/pull/350 | `5c37d4a16156a5f2dd2362dd6596654705527764` | awaiting second review |
| V7-R1-018 | https://github.com/OussamaSegh/Order-and-Chance/pull/351 | `b7de0f1adfad1d95ef59de9db9bb020f0821e0bb` | awaiting second review |
| V7-R1-019 | https://github.com/OussamaSegh/Order-and-Chance/pull/352 | `64636e7dea072c84fe5e87248647fb34c5457860` | awaiting second review |

## CI runs

None read for this loop. Round 1 did not run `./build.sh` and did not open an Actions log. The fixer did not run `./build.sh` and did not open an Actions log on any fix pull request. Do not treat an unread log as a pass.

## Open issues

Nineteen, all still open. Each has a fix pull request awaiting second review. None is merged. The text that was scored is `volume7-spaces/` at `af3f9afbaee7b76237f8b9ad085420fda82d328f`. That tree matches `volume7-spaces/` on the fix base `ddf23cd89103582fc5879cd3351dfb5b22053df0`.

| Id | Severity | Location | Problem |
| --- | --- | --- | --- |
| V7-R1-001 | major | `volume7-spaces/chapters/ch04-compact.tex:178` | Mean value theorem (d) omits continuity on \(I\). A jump at an endpoint is a counterexample. |
| V7-R1-002 | minor | `volume7-spaces/chapters/ch01-sets.tex:354` | \(\mathbb Q\) is injected into \(\mathbb Z\times\mathbb Z\), which has not been shown countable. |
| V7-R1-003 | minor | `volume7-spaces/chapters/ch01-sets.tex:641` | "Cannot be continuous" is cited to an exercise that only rules out a homeomorphism. |
| V7-R1-004 | minor | `volume7-spaces/chapters/ch01-sets.tex:648` | A \(d\)-dimensional space over \(\mathbb Q\) is called a finite union of copies of \(\mathbb Q^d\). |
| V7-R1-005 | minor | `volume7-spaces/chapters/ch02-metric.tex:169` | Banach's second bound uses \(x_{n-1}\) at \(n=0\). |
| V7-R1-006 | minor | `volume7-spaces/chapters/ch02-metric.tex:185` | Cosine Newton digit-doubling is cited to the square-root exercise. |
| V7-R1-007 | minor | `volume7-spaces/chapters/ch02-metric.tex:442` | The a priori bound is \(\frac54\cdot 5^{-n-1}\), not the claimed \(5^{-n-1}\). |
| V7-R1-008 | minor | `volume7-spaces/chapters/ch03-topology.tex:304` | Sine does not fill \([-1,1]\) on every open interval of length \(2\pi\). |
| V7-R1-009 | minor | `volume7-spaces/chapters/ch03-topology.tex:580` | A constant map is a continuous image of \(S^1\). |
| V7-R1-010 | minor | `volume7-spaces/chapters/ch05-baire.tex:182` | The complement of the meagre set is not every nowhere differentiable function. Takagi lies in \(E_n\) for \(n\ge 7\). |
| V7-R1-011 | minor | `volume7-spaces/chapters/ch07-integral.tex:171` | Sums between \(L\) and \(U\) do not by themselves give the mesh limit. |
| V7-R1-012 | minor | `volume7-spaces/chapters/ch07-integral.tex:475` | The closed intervals \([n,n+1]\) overlap at integers. |
| V7-R1-013 | minor | `volume7-spaces/chapters/ch07-integral.tex:487` | \(\mathbf 1_{]0,\infty[}\) is continuous on \([1,2]\). |
| V7-R1-014 | minor | `volume7-spaces/chapters/ch07-integral.tex:638` | `thm:riemanncont` does not identify the Riemann and Lebesgue integrals. |
| V7-R1-015 | minor | `volume7-spaces/chapters/ch09-lp.tex:113` | The \(L^\infty\) pointwise limit off \(N\) need not be a bounded function. |
| V7-R1-016 | minor | `volume7-spaces/chapters/ch10-radon.tex:476` | One \(\varepsilon\) gives \(\limsup\le\varepsilon\) almost surely, not the strong law. |
| V7-R1-017 | minor | `volume7-spaces/chapters/ch11-metricmeasures.tex:76` | An unused index makes \(W_i\) empty, and the distance is then undefined. |
| V7-R1-018 | minor | `volume7-spaces/chapters/ch11-metricmeasures.tex:774` | One pair \((M,\varepsilon)\) does not force the distribution limits \(0\) and \(1\). |
| V7-R1-019 | minor | `volume7-spaces/chapters/index.tex:76` | The index says "Tychonoff, 1930" for Theorem 4.11, which is the 1935 theorem. |

Counts: 0 critical, 1 major, 18 minor.

## Exact next step

Distinct second reviewer reviews each fix PR and adds docs/review/volume7-r1-NNN-review.md.
