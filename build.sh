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
  # The cover (tools/cover.tex with the tome's picture from tools/cover_motifs.py): a PDF page
  # for the book and a 1600x2560 PNG for the EPUB, which e-readers and Kindle show as the cover.
  title=$(sed -n 's/^% epub-title: //p' "$root/$tome/main.tex")
  num=$(sed -n 's/^.*Tome \([0-9]*\):.*/\1/p' <<<"$title")
  (cd "$root" &&
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname=cover \
      "\\def\\TOMENUM{$num}\\def\\TOMETITLE{${title#*: }}\\def\\MOTIF{$tome/cover-motif}\\input{tools/cover.tex}" \
      >"$out/cover.out" || { tail -30 "$out/cover.out"; exit 1; })
  pdftoppm -png -singlefile -scale-to-x 1600 -scale-to-y 2560 "$out/cover.pdf" "$out/cover"

  # Three PDFs: A4 (dist/<tome>.pdf), phone (-phone.pdf) and 7-inch e-reader (-kindle.pdf).
  for format in a4 phone kindle; do
    job=main; [ "$format" = a4 ] || job="main-$format"
    (cd "$root/$tome" &&
      for _ in 1 2 3; do
        pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname="$job" \
          "\\def\\FORMAT{$format}\\def\\COVER{$out/cover.pdf}\\input{main.tex}" >"$out/$job.stdout" ||
          { tail -40 "$out/$job.stdout"; exit 1; }
      done)
    suffix=""; [ "$format" = a4 ] || suffix="-$format"
    cp "$out/$job.pdf" "$root/dist/$tome$suffix.pdf"
  done

  # Each figure also becomes an SVG for the EPUB (needs pdftocairo, from poppler-utils).
  mkdir -p "$out/figures"
  for fig in "$root/$tome"/figures/*.tex; do
    [ -e "$fig" ] || continue
    name=$(basename "$fig" .tex)
    (cd "$root" &&
      pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out/figures" -jobname="$name" \
        "\\def\\FIG{$tome/figures/$name}\\input{tools/figure.tex}" >"$out/figures/$name.log" ||
        { tail -30 "$out/figures/$name.log"; exit 1; })
    pdftocairo -svg "$out/figures/$name.pdf" "$out/figures/$name.svg"
  done

  python3 "$root/tools/epub_prep.py" "$root/$tome/main.tex" "$out/epub.tex" "$out/figures"
  (cd "$root/$tome" &&
    pandoc "$out/epub.tex" -f latex -t epub3 --mathml --toc --toc-depth=2 \
      --split-level=1 --number-sections --epub-cover-image="$out/cover.png" \
      --lua-filter="$root/tools/epub.lua" --css="$root/tools/epub.css" \
      --metadata title="${title:-$tome}" --metadata lang=en \
      -o "$root/dist/$tome.epub")
  python3 "$root/tools/epub_fix.py" "$root/dist/$tome.epub"
  echo "   dist/$tome.pdf  dist/$tome-phone.pdf  dist/$tome-kindle.pdf  dist/$tome.epub"
done
