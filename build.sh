#!/usr/bin/env bash
# Build the standard 7 x 10 PDF and EPUB of each requested tome
# into dist/, and the files for an Amazon KDP edition into dist/kdp/.
# Requires pdflatex, pandoc >= 3, python3 and poppler-utils.
set -euo pipefail
export LC_ALL=C.UTF-8  # pandoc reads the copyright sign of the metadata as UTF-8
root="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$root/dist/kdp" "$root/build"
python3 "$root/tools/series_metadata.py" --check
python3 "$root/tools/print_layout.py" --check
pdf_only=false
case "${1:-}" in
  --pdf-only) pdf_only=true; shift ;;
  --help) echo "Usage: ./build.sh [--pdf-only] [tome...]"; exit 0 ;;
  --*) echo "Unknown option: $1" >&2; exit 2 ;;
esac
python3 "$root/tools/book_outputs.py" clean "$root/dist"
tomes=("$@")
[ ${#tomes[@]} -eq 0 ] && tomes=($(cd "$root" && ls -d tome*/ | tr -d /))

for tome in "${tomes[@]}"; do
  echo "== $tome"
  python3 "$root/tools/check_edition_copy.py" "$tome"
  out="$root/build/$tome"
  mkdir -p "$out"
  # The vector front cover supplies the EPUB image and library thumbnail.
  title=$(sed -n 's/^% epub-title: //p' "$root/$tome/main.tex")
  num=$(sed -n 's/^.*Tome \([0-9A-Z]*\):.*/\1/p' <<<"$title")
  meta="\\def\\TOMENUM{$num}\\def\\TOMETITLE{${title#*: }}"
  # The EPUB front is a separate asset; the standard PDF begins with book front matter.
  (cd "$root" &&
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname=cover \
      "$meta\\def\\MOTIF{$tome/cover-motif}\\input{tools/cover.tex}" \
      >"$out/cover.out" || { tail -30 "$out/cover.out"; exit 1; })
  if ! $pdf_only; then
    pdftoppm -png -singlefile -scale-to-x 1600 -scale-to-y 2560 "$out/cover.pdf" "$out/cover"
  fi

  # One canonical PDF for reading and paperback upload: 7 x 10 in, no bleed. The full
  # cover (back, spine, front) with 0.125in bleed and the spine width of KDP's formula for white
  # paper, 0.002252in per page. The inside margin is the one KDP asks for at that page count.
  inner=0.75in
  for pass in 1 2; do
    (cd "$root/$tome" &&
      for _ in 1 2 3; do
        pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname=main \
          "$meta\\def\\PRINTINNER{$inner}\\input{main.tex}" >"$out/main.stdout" ||
          { tail -40 "$out/main.stdout"; exit 1; }
      done)
    pages=$(pdfinfo "$out/main.pdf" | sed -n 's/^Pages: *//p')
    [ "$pages" -le 700 ] || [ "$inner" = 0.875in ] && break
    inner=0.875in
  done
  python3 "$root/tools/check_cover_pdf.py" "$out/main.pdf" --interior
  cp "$out/main.pdf" "$root/dist/$tome.pdf"
  python3 "$root/tools/print_layout.py" --pages "$pages" --inner "$inner" > "$root/dist/kdp/$tome-print-metadata.json"
  spine=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["spine_in"])' "$root/dist/kdp/$tome-print-metadata.json")
  spinetext=""; [ "$pages" -ge 80 ] && spinetext="\\def\\SPINETEXT{}"
  blurb="$tome/blurb"; [ -e "$root/$blurb.tex" ] || blurb=tools/blurb-default
  # The ISBN barcode on the back cover, once the tome has its paperback ISBN (\bookisbnprint in main.tex).
  barcode=""
  isbn=$(sed -n 's/^\\renewcommand{\\bookisbnprint}{\([0-9-]*\)}.*/\1/p' "$root/$tome/main.tex")
  if [ -n "$isbn" ]; then
    python3 "$root/tools/ean13.py" "$isbn" "$out/barcode.tex"
    barcode="\\def\\BARCODE{$out/barcode.tex}"
  fi
  (cd "$root" &&
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname=cover-wrap \
      "$meta\\def\\MOTIF{$tome/cover-motif}\\def\\SPINE{$spine}$spinetext\\def\\BLURB{$blurb}$barcode\\input{tools/cover-wrap.tex}" \
      >"$out/cover-wrap.out" || { tail -30 "$out/cover-wrap.out"; exit 1; })
  python3 "$root/tools/check_cover_pdf.py" "$out/cover-wrap.pdf" --spine "$spine" --title "${title#*: }" --number "$num"
  cp "$out/cover-wrap.pdf" "$root/dist/kdp/$tome-cover-wrap.pdf"
  # The KDP listing (title fields, description, keywords) from <tome>/kdp.md, see tools/listing.py.
  python3 "$root/tools/listing.py" "$root/$tome" "$root/dist/kdp/$tome-listing.md"
  # Separate eBook cover: 1600 x 2560 pixels, also used for publishing.
  pdftoppm -jpeg -jpegopt quality=95 -singlefile -scale-to-x 1600 -scale-to-y 2560 "$out/cover.pdf" \
    "$root/dist/kdp/$tome-ebook-cover"
  if $pdf_only; then
    echo "   dist/$tome.pdf ($pages pages, 7 x 10 in); publishing assets in dist/kdp/"
    continue
  fi

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
      --metadata title="${title:-$tome}" --metadata subtitle="$(python3 -c 'import json,sys; from pathlib import Path; print(json.loads(Path(sys.argv[1]).read_text()).get(sys.argv[2], ""))' "$root/common/volume-subtitles.json" "$num")" --metadata author="SEGHAIER Oussama" --metadata lang=en \
      --metadata date=2026 --metadata rights="$(python3 "$root/tools/epub_prep.py" --rights "$root/$tome/main.tex")" \
      --metadata subject=Mathematics \
      -o "$root/dist/$tome.epub")
  python3 "$root/tools/epub_fix.py" "$root/dist/$tome.epub"
  # The online reader for the website: one HTML page per chapter, from the same LaTeX as the EPUB.
  python3 "$root/tools/reader.py" "$tome" "$out" "$root/dist/html/$tome"
  echo "   dist/$tome.pdf (7 x 10 in)  dist/$tome.epub  dist/html/$tome/"
  echo "   KDP: $pages interior pages;  dist/kdp/$tome-cover-wrap.pdf (spine ${spine}in)  dist/kdp/$tome-ebook-cover.jpg"
done
