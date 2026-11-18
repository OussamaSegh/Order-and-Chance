# Frozen source before Volume 13 complete rewrite

Immutable commit: `480cbe195022977a04bdcb78255ab6a1eb12720b` (main after PR #249 merged). Volume 13's earlier PR #229 is included. Read the authoritative revised blueprint from PR #157 at `claude/project-thread-khh5pi:docs/plan/book-13.md`. Original printed units: 1. `ch11-algebraic.tex`, 2. `ch12-ideals-quadratic.tex`, 3. `ch01-number-fields.tex`, 4. `ch02-ideals.tex`, 5. `ch03-geometry.tex`, 6. `ch04-units.tex`, 7. `ch05-cyclotomic.tex`, 8. `ch12-padic.tex`, 9. `ch06-local.tex`, 10. `ch07-hasse.tex`, 11. `ch08-zeta.tex`, 12. `ch09-tate.tex`, 13. `ch10-cft.tex`, 14. `ch11-curves.tex`, 15. `ch12-elliptic.tex`, 16. `ch13-finite.tex`, 17. `ch14-modular.tex`.

Git history, not a mutable copied table, defines the exact original formal statements, numbering, labels, exercises, hint/solution bodies, figures, and chapter architecture. Recover any original file with `git show 480cbe195022977a04bdcb78255ab6a1eb12720b:volume13-arithmetic/chapters/FILE.tex`. Check with `python3 review/volume13-complete-rewrite/check_preservation.py --final`.

Structural preservation is not proof verification. Accepted Volumes 1–12 and existing cover artwork are frozen.
