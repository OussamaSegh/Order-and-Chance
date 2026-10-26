#!/usr/bin/env bash
# Build the PDF and EPUB of every tome (or of the tomes given as arguments)
# into dist/, and the files for an Amazon KDP edition into dist/kdp/.
# Requires pdflatex, pandoc >= 3, python3 and poppler-utils.
set -euo pipefail
export LC_ALL=C.UTF-8  # pandoc reads the copyright sign of the metadata as UTF-8
root="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$root/dist/kdp" "$root/build"
tomes=("$@")
[ ${#tomes[@]} -eq 0 ] && tomes=($(cd "$root" && ls -d tome*/ | tr -d /))

for tome in "${tomes[@]}"; do
  echo "== $tome"
  out="$root/build/$tome"
  mkdir -p "$out"
  # The cover (tools/cover.tex with the tome's picture from tools/cover_motifs.py): a PDF page
  # for the book and a 1600x2560 PNG for the EPUB, which e-readers and Kindle show as the cover.
  title=$(sed -n 's/^% epub-title: //p' "$root/$tome/main.tex")
  num=$(sed -n 's/^.*Tome \([0-9A-Z]*\):.*/\1/p' <<<"$title")
  meta="\\def\\TOMENUM{$num}\\def\\TOMETITLE{${title#*: }}"
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
          "$meta\\def\\FORMAT{$format}\\def\\COVER{$out/cover.pdf}\\input{main.tex}" >"$out/$job.stdout" ||
          { tail -40 "$out/$job.stdout"; exit 1; }
      done)
    suffix=""; [ "$format" = a4 ] || suffix="-$format"
    cp "$out/$job.pdf" "$root/dist/$tome$suffix.pdf"
  done

  # Amazon KDP paperback (dist/kdp/): the interior, 6in x 9in trim without bleed, and the full
  # cover (back, spine, front) with 0.125in bleed and the spine width of KDP's formula for white
  # paper, 0.002252in per page. The inside margin is the one KDP asks for at that page count.
  inner=0.75in
  for pass in 1 2; do
    (cd "$root/$tome" &&
      for _ in 1 2 3; do
        pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname=main-print \
          "$meta\\def\\FORMAT{print}\\def\\PRINTINNER{$inner}\\input{main.tex}" >"$out/main-print.stdout" ||
          { tail -40 "$out/main-print.stdout"; exit 1; }
      done)
    pages=$(pdfinfo "$out/main-print.pdf" | sed -n 's/^Pages: *//p')
    [ "$pages" -le 700 ] || [ "$inner" = 0.875in ] && break
    inner=0.875in
  done
  [ "$pages" -le 828 ] || echo "   WARNING: $pages pages, more than KDP's 828 for a 6x9 paperback"
  [ "$pages" -ge 24 ] || echo "   WARNING: $pages pages, fewer than KDP's minimum of 24"
  cp "$out/main-print.pdf" "$root/dist/kdp/$tome-print.pdf"
  pages=$(( (pages + 1) / 2 * 2 ))
  spine=$(python3 -c "print(f'{$pages * 0.002252:.4f}')")
  spinetext=""; [ "$pages" -ge 80 ] && spinetext="\\def\\SPINETEXT{}"
  blurb="$tome/blurb"; [ -e "$root/$blurb.tex" ] || blurb=tools/blurb-default
  (cd "$root" &&
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname=cover-wrap \
      "$meta\\def\\MOTIF{$tome/cover-motif}\\def\\SPINE{$spine}$spinetext\\def\\BLURB{$blurb}\\input{tools/cover-wrap.tex}" \
      >"$out/cover-wrap.out" || { tail -30 "$out/cover-wrap.out"; exit 1; })
  cp "$out/cover-wrap.pdf" "$root/dist/kdp/$tome-cover-wrap.pdf"
  # Kindle eBook cover: KDP asks for a JPEG of 1600 x 2560 pixels.
  pdftoppm -jpeg -jpegopt quality=95 -singlefile -scale-to-x 1600 -scale-to-y 2560 "$out/cover.pdf" \
    "$root/dist/kdp/$tome-ebook-cover"

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
      --metadata title="${title:-$tome}" --metadata author="SEGHAIER Oussama & Claude Opus 5.5" --metadata lang=en \
      --metadata date=2026 --metadata rights="$(python3 "$root/tools/epub_prep.py" --rights "$root/$tome/main.tex")" \
      --metadata subject=Mathematics \
      -o "$root/dist/$tome.epub")
  python3 "$root/tools/epub_fix.py" "$root/dist/$tome.epub"
  # The online reader for the website: one HTML page per chapter, from the same LaTeX as the EPUB.
  python3 "$root/tools/reader.py" "$tome" "$out" "$root/dist/html/$tome"
  echo "   dist/$tome.pdf  dist/$tome-phone.pdf  dist/$tome-kindle.pdf  dist/$tome.epub  dist/html/$tome/"
  echo "   KDP: dist/kdp/$tome-print.pdf ($pages pages)  dist/kdp/$tome-cover-wrap.pdf (spine ${spine}in)  dist/kdp/$tome-ebook-cover.jpg"
done
