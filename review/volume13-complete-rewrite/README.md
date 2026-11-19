# Volume 13 complete rewrite

Started from immutable `480cbe195022977a04bdcb78255ab6a1eb12720b`, including the prior seventeen-chapter blueprint rewrite (PR #229). The goal is a further rigorous editorial, teaching, visual and mathematical review, preserving original printed numbering and historical art. All 17 chapters must receive four newly graded exercises with full hints/solutions and two teaching TikZ figures. Numerical tests never certify proofs.

Reproduce: `python3 review/volume13-complete-rewrite/check_preservation.py --final`; `python3 review/volume13-complete-rewrite/check_new_examples.py`; `for s in review/volume13-rewrite/check_ch*.py; do python3 "$s"; done`; `python3 -m unittest discover -s tools -p 'test_*.py'`; `python3 tools/listing.py volume13-arithmetic /tmp/v13.md`; `./build.sh volume13-arithmetic`. Publishing runs in the normal Build books workflow on the same PR head; evaluate actual PDF/print/EPUB/website artifacts separately.
