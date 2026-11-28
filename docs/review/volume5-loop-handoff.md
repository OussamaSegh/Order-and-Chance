# Volume 5 review loop — handoff

This file is the state of the Volume 5 fix-and-review loop. A later agent can continue from this file and from the tracking pull request alone.

## Rules

- Keep Volume 4 as it stands. Do not edit `volume4-chance/`.
- Do not start a new Volume 5 review beyond this loop. Stop at **10/10** or after **round 6**, whichever comes first.
- Independent full review, with a regression check of every passage changed by #302, #303, and #304, and of every later fix.
- Small fix pull requests. Each one carries a distinct second-reviewer note under `docs/review/`.
- Squash-merge only when every non-skipped check is green on the exact reviewed head: `gh pr merge --squash --match-head-commit <SHA>`.
- Do not weaken a proof silently. Do not change numbered-statement numbers. Do not change caption or diagram typography. No releases. No force-push of `main`.
- Score out of 10. Critical = false statement or broken proof. Major = genuine gap or a wrong citation of a needed result. Minor = local slip or a missing one-line reason. 10/10 means nothing open.

## Repository

- Repo: `OussamaSegh/Order-and-Chance`
- Loop base when this handoff was opened: `337b1230584fea95ffb538cdbeb373c0fe2d2113`
- Volume 5 source order: `volume5-calculation/main.tex`. `bbp-borwein.tex` is included from the integrals chapter.

## Already on main before this resumed loop

| Item | PR | Merge SHA |
| --- | --- | --- |
| Round-1 review, 7/10 (0 critical, 2 major, 8 minor) | #298 | `2b3a8dfe8c0a28f5025d55ec01562f20570ce17f` |
| Eight one-line gaps | #304 | `39d89e64f7af507193108a94bce3b84ba179874d` |
| FFT length and wrapped index | #302 | `41356cffdca1bab001548c45b91ef6fae74eed7c` |
| Binary-digit blocks by exponent | #303 | `1b17516df6edd3edfefa813dbc6a24cd2c856c07` |

Those three fixes were re-read in round 2. All ten repaired passages hold. Regression count: 0.

## Round 2

**Score: 8/10.** 0 critical, 0 major, 4 minor. Review pull request to be recorded in the tracker comments.

| ID | Location | What is wrong | Fix |
| --- | --- | --- | --- |
| V5-R2-001 | `volume5-calculation/chapters/ch06-fourier.tex:270` | The inner sum with the factor \(\pi/N\) is the Riemann sum, and it tends to \(\operatorname{Si}(\pi)\). The factor \(2/\pi\) stands outside it. The sentence gives the partial-sum limit to the Riemann sum. | Name the inner sum as the Riemann sum, send it to \(\operatorname{Si}(\pi)\), and then multiply by \(2/\pi\). |
| V5-R2-002 | `volume5-calculation/chapters/ch10-zeta.tex:546` | “The integral is (b).” The integral in the error display is \(\int_0^1(-\log t)\,\mathrm dt=1\). Part (b) is \(\int_0^1(-\log t)/(1+t)\,\mathrm dt=\pi^2/12\). The main term divides that value by \(\log 2\). | Say which integral is which. |
| V5-R2-003 | `volume5-calculation/chapters/ch02-generating.tex:1519` | “Then \(u_{2n}\to 2/\mu\) instead.” The limit is right for span 2. The factor 2 is not derived. | Both simple roots \(\pm 1\) contribute \(1/\mu\), and they add on even indices. |
| V5-R2-004 | `volume5-calculation/chapters/ch02-generating.tex:988` | The third identity of `prop:explog` is \(\exp(\log(1+F))=1+F\). Recovering \(\hat C\) from \(\exp(\hat C)\) uses the second identity, \(\log(\exp(\hat C))=\hat C\). | Cite the second identity. |

## Next step

Open one fix pull request for V5-R2-001 through V5-R2-004. Second-read it. Squash-merge only on green CI for that exact head. Then run round 3 on the new main. Stop at 10/10 or after round 6.

## Do not

- Edit Volume 4.
- Close or reopen Volume 5 review logs that are already on main.
- Upload to KDP or make a release.
