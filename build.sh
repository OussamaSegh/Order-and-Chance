#!/usr/bin/env bash
# Build the PDF and EPUB of every tome (or of the tomes given as arguments)
# into dist/. Requires pdflatex, pandoc >= 3 and python3.
set -euo pipefail
root="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$root/dist" "$root/build"
tomes=("$@")
[ ${#tomes[@]} -eq 0 ] && tomes=($(cd "$root" && ls -d tome*/ | tr -d /))

for tome in "${tomes[@]}"; do
  echo "== $tome"
  out="$root/build/$tome"
  mkdir -p "$out"
  (cd "$root/$tome" &&
    for _ in 1 2; do
      pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" main.tex >"$out/pdflatex.log" ||
        { tail -40 "$out/pdflatex.log"; exit 1; }
    done)
  cp "$out/main.pdf" "$root/dist/$tome.pdf"

  python3 "$root/tools/epub_prep.py" "$root/$tome/main.tex" "$out/epub.tex"
  title=$(sed -n 's/^% epub-title: //p' "$root/$tome/main.tex")
  (cd "$root/$tome" &&
    pandoc "$out/epub.tex" -f latex -t epub3 --mathml --toc --toc-depth=2 \
      --split-level=1 --number-sections \
      --lua-filter="$root/tools/epub.lua" --css="$root/tools/epub.css" \
      --metadata title="${title:-$tome}" --metadata author="SEGHAIER & Claude" --metadata lang=en \
      -o "$root/dist/$tome.epub")
  echo "   dist/$tome.pdf  dist/$tome.epub"
done
