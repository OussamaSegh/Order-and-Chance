#!/usr/bin/env bash
# Build the 7 x 10 download PDF with cover, print interior and EPUB of each tome
# into dist/, and the files for an Amazon KDP edition into dist/kdp/.
# Requires pdflatex, xelatex, pandoc >= 3, poppler-utils and tools/requirements-build.txt.
set -euo pipefail
export LC_ALL=C.UTF-8  # pandoc reads the copyright sign of the metadata as UTF-8
root="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$root/dist/kdp" "$root/build"
# Cache the approved image as a PDF XObject. First pass only writes XDV/aux;
# the second pass encodes the final one-page PDF without a temporary extra page.
compile_cover() {
  local output="$1" job="$2" source="$3" pass
  for pass in 1 2; do
    local flags=()
    if [ "$pass" = 1 ]; then flags=(-no-pdf); fi
    (cd "$root" && xelatex "${flags[@]}" -interaction=nonstopmode -halt-on-error \
      -output-directory="$output" -jobname="$job" "$source" > "$output/$job.out" ||
      { tail -30 "$output/$job.out"; exit 1; })
  done
}
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
  # Approved image masters supply their volumes; other fronts reuse the series identity.
  title=$(sed -n 's/^% epub-title: //p' "$root/$tome/main.tex")
  num=$(sed -n 's/^.*Volume \([0-9A-Z]*\):.*/\1/p' <<<"$title")
  meta="\\def\\TOMENUM{$num}\\def\\TOMETITLE{${title#*: }}"
  # The approved front supplies the downloadable PDF, EPUB and separate print wrap.
  compile_cover "$out" cover "$meta\\def\\MOTIF{$tome/cover-motif}\\input{tools/cover.tex}"
  if [ -f "$root/tools/assets/approved-volume-$num.png" ]; then
    python3 "$root/tools/check_cover_reference.py" "$out/cover.pdf" --number "$num"
  fi
  if ! $pdf_only; then
    if [ -f "$root/tools/assets/approved-volume-$num.png" ]; then
      cp "$root/tools/assets/approved-volume-$num.png" "$out/cover.png"
    else
      pdftoppm -png -singlefile -scale-to-x 1792 -scale-to-y 2560 "$out/cover.pdf" "$out/cover"
    fi
  fi

  # Typeset the print interior once: 7 x 10 in, no bleed. The full
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
  python3 "$root/tools/check_book_layout.py" "$out/main.log" "$out/main.oclayout"
  python3 "$root/tools/check_cover_pdf.py" "$out/main.pdf" --interior
  cp "$out/main.pdf" "$root/dist/kdp/$tome-print.pdf"
  python3 "$root/tools/book_pdf.py" "$out/cover.pdf" "$root/dist/kdp/$tome-print.pdf" "$root/dist/$tome.pdf"
  python3 "$root/tools/check_cover_pdf.py" "$root/dist/$tome.pdf" --interior
  if [ -f "$root/tools/assets/approved-volume-$num.png" ]; then
    python3 "$root/tools/check_cover_reference.py" "$root/dist/$tome.pdf" --number "$num"
  fi
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
  compile_cover "$out" cover-wrap "$meta\\def\\MOTIF{$tome/cover-motif}\\def\\SPINE{$spine}$spinetext\\def\\BLURB{$blurb}$barcode\\input{tools/cover-wrap.tex}"
  python3 "$root/tools/check_cover_pdf.py" "$out/cover-wrap.pdf" --spine "$spine" --title "${title#*: }" --number "$num"
  python3 "$root/tools/check_print_cover.py" "$out/cover-wrap.pdf" --number "$num" \
    --report "$out/cover-preflight.json"
  cp "$out/cover-wrap.pdf" "$root/dist/kdp/$tome-cover-wrap.pdf"
  # The KDP listing (title fields, description, keywords) from <tome>/kdp.md, see tools/listing.py.
  python3 "$root/tools/listing.py" "$root/$tome" "$root/dist/kdp/$tome-listing.md"
  # Separate eBook cover: 1792 x 2560 pixels, preserving the approved 7:10 design, also used for publishing.
  pdftoppm -jpeg -jpegopt quality=95 -singlefile -scale-to-x 1792 -scale-to-y 2560 "$out/cover.pdf" \
    "$root/dist/kdp/$tome-ebook-cover"
  if $pdf_only; then
    echo "   dist/$tome.pdf (cover + $pages pages); dist/kdp/$tome-print.pdf ($pages print pages, 7 x 10 in)"
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
  if [ -f "$root/tools/assets/approved-volume-$num.png" ]; then
    python3 "$root/tools/check_cover_reference.py" "$out/cover.pdf" --number "$num" --epub "$root/dist/$tome.epub" --reader "$root/dist/html/$tome"
  fi
  echo "   dist/$tome.pdf (7 x 10 in)  dist/$tome.epub  dist/html/$tome/"
  echo "   KDP: dist/kdp/$tome-print.pdf ($pages interior pages); dist/kdp/$tome-cover-wrap.pdf (spine ${spine}in)"
done
