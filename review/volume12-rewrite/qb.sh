#!/usr/bin/env bash
# Quick interior build of Volume 12 (two xelatex passes), then list undefined references and multiply-defined labels.
set -uo pipefail
root="$(cd "$(dirname "$0")/../.." && pwd)"; out="$root/build/qb12"; mkdir -p "$out"
export extra_mem_top=12000000
meta='\def\VOLUMENUM{12}\def\VOLUMETITLE{Random Motion}'
cd "$root/volume12-random-motion"
for i in 1 2; do
  xelatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname=main "$meta\\def\\PRINTINNER{0.9in}\\input{main.tex}" > "$out/main.stdout" || { tail -40 "$out/main.stdout"; exit 1; }
done
grep -E "undefined|multiply defined|Overfull \\\\hbox \(([2-9][0-9]|[0-9]{3})" "$out/main.log" | sort | uniq -c | head -30
pdfinfo "$out/main.pdf" | grep Pages
