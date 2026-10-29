#!/usr/bin/env bash
# Complete cumulative manuscript build. Never publishes or uploads.
set -euo pipefail
batch=${1:?batch identifier required}
root=$(cd "$(dirname "$0")/../.." && pwd)
source /workspace/order-chance-system/activate.sh
export extra_mem_top=12000000
out="$root/build/volume0-mathematical-maturity"
record="/workspace/volume0-checkpoints/$batch"
mkdir -p "$out" "$record"
cd "$root"
# A full source snapshot before each batch compilation preserves the implemented state.
tar --exclude=.git --exclude=build --exclude=dist -cf "$record/source-before-build.tar" volume0-mathematical-maturity review/volume0-reconstruction common
for pass in 1 2 3; do
  (cd volume0-mathematical-maturity && xelatex -interaction=nonstopmode -halt-on-error \
    -output-directory="$out" -jobname=main \
    '\def\VOLUMENUM{0}\def\VOLUMETITLE{Mathematical Maturity}\def\PRINTINNER{0.75in}\input{main.tex}') \
    > "$record/pass-$pass.txt" 2>&1
done
python3 tools/check_book_layout.py "$out/main.log" "$out/main.oclayout"
python3 tools/check_cover_pdf.py "$out/main.pdf" --interior
python3 tools/check_interior_style.py "$out/main.pdf"
python3 tools/book_pdf.py "$out/cover.pdf" "$out/main.pdf" "$record/Volume0.pdf"
cp "$out/main.pdf" "$record/Volume0-interior.pdf"
cp "$out/main.log" "$record/compilation.log"
cp "$out/main.aux" "$record/main.aux"
cp "$out/main.toc" "$record/main.toc"
python3 review/volume0-reconstruction/inventory.py
git diff --check
pdfinfo "$record/Volume0-interior.pdf" > "$record/pdfinfo.txt"
echo "Complete cumulative PDF and logs: $record"
