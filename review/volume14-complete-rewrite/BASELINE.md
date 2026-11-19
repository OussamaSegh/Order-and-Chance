# Frozen source before Volume 14 complete rewrite

Immutable commit: `60ce094742a84e3da028ad2c9d31d535db656344` (main after PR #250 merged). Volume 14's earlier PR #232 is included. Read the authoritative revised blueprint from PR #157 at `claude/project-thread-khh5pi:docs/plan/book-14.md`. Original printed units, in book order:

1. `ch01-zeros.tex` — Zeros and primes in short intervals
2. `ch02-siegel.tex` — Siegel's theorem
3. `ch03-sieves.tex` — Sieves and the parity problem
4. `ch04-largesieve.tex` — The large sieve and Bombieri–Vinogradov
5. `ch05-expsums.tex` — Exponential sums over primes
6. `waring.tex` — Waring's problem
7. `three-primes.tex` — Three primes
8. `ch08-gpy.tex` — Small gaps between primes
9. `ch09-maynard.tex` — Bounded gaps between primes
10. `ch10-halasz.tex` — Multiplicative functions
11. `ch11-additive.tex` — Additive combinatorics
12. `ch12-roth.tex` — Roth's theorem
13. `ch13-gowers.tex` — Gowers norms and the Green–Tao theorem
14. `ch14-critical.tex` — The critical line

Git history, not a mutable copied table, defines the exact original formal statements, numbering, labels, exercises, hint and solution bodies, figures, and chapter architecture. Recover any original file with `git show 60ce094742a84e3da028ad2c9d31d535db656344:volume14-primes/chapters/FILE.tex`. Check with `python3 review/volume14-complete-rewrite/check_preservation.py --final`.

Structural preservation is not proof verification. Accepted Volumes 1–13, Volume 15, and existing cover artwork are frozen.
