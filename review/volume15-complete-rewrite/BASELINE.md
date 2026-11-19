# Frozen source before Volume 15 complete rewrite

Immutable commit: `60ce094742a84e3da028ad2c9d31d535db656344` (main after PR #250 merged). Volume 15's earlier rewrite is PR #244. Read the authoritative plan from PR #157. Original printed units, in book order:

1. `ch01-integers.tex`, which inputs the section `ra-anatomy.tex`
2. `ch02-cramer.tex`, which inputs the sections `ra-largemoduli.tex` and `ra-gaps.tex`
3. `ch03-divisors.tex`, which inputs the sections `ra-additive.tex`, `ra-selbergdelange.tex` and `ra-erdoskac.tex`
4. `ch04-multiplicative.tex`, which inputs the sections `ra-randommult.tex` and `ra-polynomials.tex`
5. `ch05-short.tex`
6. `ch06-sieves.tex`
7. `ch07-classgroups.tex`, which inputs the sections `ra-cohenlenstra.tex` and `ra-symmoments.tex`
8. `ch08-ranks.tex`
9. `ch09-gue.tex`, which inputs the section `moments-zeta.tex`
10. `ch10-moments.tex`, which inputs the section `ra-moments.tex`
11. `ch11-values.tex`, which inputs the sections `ra-bohrjessen.tex` and `ra-selberg.tex`
12. `ch12-pseudorandom.tex`
13. `ch13-bias.tex`, which inputs the section `ra-bias.tex`
14. `ch14-meeting.tex`

`main.tex` does not input `ra-*.tex` or `moments-zeta.tex` as chapters or appendices. Those files are sections of the fourteen chapters above. The preface is front matter, not a numbered chapter.

Git history, not a mutable copied table, defines the exact original formal statements, numbering, labels, exercises, hint/solution bodies, figures, and chapter architecture. Recover any original file with `git show 60ce094742a84e3da028ad2c9d31d535db656344:volume15-order-and-chance/chapters/FILE.tex`. Check with `python3 review/volume15-complete-rewrite/check_preservation.py --final`.

Structural preservation is not proof verification. Accepted Volumes 1–14 and existing cover artwork are frozen. No original sentence was altered.
