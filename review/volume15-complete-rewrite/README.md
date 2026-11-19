# Volume 15 complete rewrite

Started from immutable `60ce094742a84e3da028ad2c9d31d535db656344`, including the prior Volume 15 rewrite (PR #244) and the Volume 13 teaching-extension model (PR #250). The master plan is PR #157. The goal is a further teaching extension: every numbered chapter receives four newly graded exercises with full hints and solutions, and two teaching TikZ figures. Numerical tests never certify proofs.

`ra-*.tex` and `moments-zeta.tex` are sections pulled in by the fourteen numbered chapters. They are not separate chapters or appendices in `main.tex`. The additions sit in those section files when that is where the chapter's exercises or the teaching moment lives.

Reproduce: `python3 review/volume15-complete-rewrite/check_preservation.py --final`; `python3 review/volume15-complete-rewrite/check_new_examples.py`; `python3 review/volume15-complete-rewrite/check_figures.py`; from `review/volume15-rewrite`, `python3 check_ch*.py`; `python3 -m unittest discover -s tools -p 'test_*.py'`; `python3 tools/listing.py volume15-order-and-chance /tmp/v15.md`; `./build.sh volume15-order-and-chance`. Publishing runs in the normal Build books workflow on the same PR head; evaluate actual PDF/print/EPUB/website artifacts separately.
