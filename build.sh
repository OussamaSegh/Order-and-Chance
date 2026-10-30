#!/usr/bin/env bash
# Build the 7 x 10 download PDF with cover, print interior and EPUB of each volume
# into dist/, and the files for an Amazon KDP edition into dist/kdp/.
# Requires xelatex, Ghostscript, pandoc >= 3, poppler-utils and tools/requirements-build.txt.
set -euo pipefail
export LC_ALL=C.UTF-8  # pandoc reads the copyright sign of the metadata as UTF-8
# Unicode math plus dense PGFPlots surfaces needs more token memory than XeTeX's default.
export extra_mem_top=12000000
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
  python3 "$root/tools/check_cover_pdf.py" --log "$output/$job.log"
}
python3 "$root/tools/series_metadata.py" --check
python3 "$root/tools/series_cover.py" --check
python3 "$root/tools/print_layout.py" --check
pdf_only=false
case "${1:-}" in
  --pdf-only) pdf_only=true; shift ;;
  --help) echo "Usage: ./build.sh [--pdf-only] [volume...]"; exit 0 ;;
  --*) echo "Unknown option: $1" >&2; exit 2 ;;
esac
python3 "$root/tools/book_outputs.py" clean "$root/dist"
volumes=("$@")
[ ${#volumes[@]} -eq 0 ] && volumes=($(cd "$root" && ls -d volume*/ | tr -d /))

for volume in "${volumes[@]}"; do
  public=$(python3 "$root/tools/public_names.py" "$volume" stem)
  echo "== $public"
  python3 "$root/tools/check_edition_copy.py" "$volume"
  out="$root/build/$volume"
  mkdir -p "$out"
  # Every volume uses the shared Cormorant front; the generator checks the plates above.
  title=$(sed -n 's/^% epub-title: //p' "$root/$volume/main.tex")
  num=$(sed -n 's/^.*Volume \([0-9A-Z]*\):.*/\1/p' <<<"$title")
  meta="\\def\\VOLUMENUM{$num}\\def\\VOLUMETITLE{${title#*: }}"
  plate="\\def\\MOTIF{$volume/cover-motif}\\def\\COVERLETTER{$volume/cover-lettering}"
  # The same plate supplies the reading PDF, EPUB and separate print wrap.
  compile_cover "$out" cover "$meta$plate\\input{tools/cover.tex}"
  python3 "$root/tools/check_cover_template.py" "$out/cover.pdf" --number "$num"
  if ! $pdf_only; then
    pdftoppm -png -singlefile -scale-to-x 1792 -scale-to-y 2560 "$out/cover.pdf" "$out/cover"
  fi

  # Typeset the print interior once: 7 x 10 in, no bleed. The full
  # cover (back, spine, front) with 0.125in bleed and the spine width of KDP's formula for white
  # paper, 0.002347in per page for premium colour. The interior design (docs/design/interior.md)
  # uses a 0.9in gutter at every page count, which meets KDP's inside-margin minimum up to 828 pages.
  inner=0.9in
  # Discard generated state from earlier font engines (e.g. Palatino's PazoBB
  # tokens in an old TOC). Three clean passes rebuild all reference state.
  rm -f "$out/main.aux" "$out/main.toc" "$out/main.out" "$out/main.lof" "$out/main.lot"
  (cd "$root/$volume" &&
    for _ in 1 2 3; do
      xelatex -interaction=nonstopmode -halt-on-error -output-directory="$out" -jobname=main \
        "$meta\\def\\PRINTINNER{$inner}\\input{main.tex}" >"$out/main.stdout" ||
        { tail -40 "$out/main.stdout"; exit 1; }
    done)
  python3 "$root/tools/check_book_layout.py" "$out/main.log" "$out/main.oclayout"
  python3 "$root/tools/check_cover_pdf.py" "$out/main.pdf" --interior
  python3 "$root/tools/check_interior_style.py" "$out/main.pdf"
  # Reading keeps the original vectors, font mappings and navigation. The KDP
  # upload is a separately validated, noninteractive PDF 1.3 press export.
  python3 "$root/tools/book_pdf.py" "$out/cover.pdf" "$out/main.pdf" "$root/dist/$public.pdf"
  python3 "$root/tools/kdp_pdf.py" "$out/main.pdf" "$root/dist/kdp/$public - Print.pdf" \
    --report "$out/kdp-preflight.json"
  python3 "$root/tools/check_cover_pdf.py" "$root/dist/kdp/$public - Print.pdf" --interior
  python3 "$root/tools/check_interior_style.py" "$root/dist/kdp/$public - Print.pdf"
  pages=$(pdfinfo "$root/dist/kdp/$public - Print.pdf" | sed -n 's/^Pages: *//p')
  python3 "$root/tools/check_cover_pdf.py" "$root/dist/$public.pdf" --interior
  python3 "$root/tools/check_cover_template.py" "$root/dist/$public.pdf" --number "$num"
  python3 "$root/tools/print_layout.py" --pages "$pages" --inner "$inner" > "$root/dist/kdp/$public - Print Metadata.json"
  spine=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["spine_in"])' "$root/dist/kdp/$public - Print Metadata.json")
  spinetext=""; [ "$pages" -ge 80 ] && spinetext="\\def\\SPINETEXT{}"
  blurb="$volume/blurb"; [ -e "$root/$blurb.tex" ] || blurb=tools/blurb-default
  # The ISBN barcode on the back cover, once the volume has its paperback ISBN (\bookisbnprint in main.tex).
  barcode=""
  isbn=$(sed -n 's/^\\renewcommand{\\bookisbnprint}{\([0-9-]*\)}.*/\1/p' "$root/$volume/main.tex")
  if [ -n "$isbn" ]; then
    python3 "$root/tools/ean13.py" "$isbn" "$out/barcode.tex"
    barcode="\\def\\BARCODE{$out/barcode.tex}"
  fi
  compile_cover "$out" cover-wrap "$meta$plate\\def\\SPINE{$spine}$spinetext\\def\\BLURB{$blurb}$barcode\\input{tools/cover-wrap.tex}"
  python3 "$root/tools/check_cover_pdf.py" "$out/cover-wrap.pdf" --spine "$spine" --title "${title#*: }" --number "$num"
  python3 "$root/tools/kdp_cover.py" "$out/cover-wrap.pdf" "$root/dist/kdp/$public - Paperback Cover.pdf" \
    --number "$num" --report "$out/cover-preflight.json"
  python3 "$root/tools/check_cover_pdf.py" "$root/dist/kdp/$public - Paperback Cover.pdf" \
    --spine "$spine" --title "${title#*: }" --number "$num" --print-export
  # The KDP listing (title fields, description, keywords) from <volume>/kdp.md, see tools/listing.py.
  python3 "$root/tools/listing.py" "$root/$volume" "$root/dist/kdp/$public - Publishing Listing.md"
  # Separate eBook cover: 1792 x 2560 pixels, preserving the approved 7:10 design, also used for publishing.
  pdftoppm -jpeg -jpegopt quality=95 -singlefile -scale-to-x 1792 -scale-to-y 2560 "$out/cover.pdf" \
    "$root/dist/kdp/$public - eBook Cover"
  if $pdf_only; then
    echo "   dist/$public.pdf (cover + $pages pages); dist/kdp/$public - Print.pdf ($pages print pages, 7 x 10 in)"
    continue
  fi

  # Each figure also becomes an SVG for the EPUB (needs pdftocairo, from poppler-utils).
  mkdir -p "$out/figures"
  for fig in "$root/$volume"/figures/*.tex; do
    [ -e "$fig" ] || continue
    name=$(basename "$fig" .tex)
    (cd "$root" &&
      xelatex -interaction=nonstopmode -halt-on-error -output-directory="$out/figures" -jobname="$name" \
        "\\def\\FIG{$volume/figures/$name}\\input{tools/figure.tex}" >"$out/figures/$name.log" ||
        { tail -30 "$out/figures/$name.log"; exit 1; })
    pdftocairo -svg "$out/figures/$name.pdf" "$out/figures/$name.svg"
  done

  # Chapter openers of the EPUB and online reader show the volume's cover illustration (design 5e).
  python3 "$root/tools/opener_motif.py" "$volume" "$out/figures"
  python3 "$root/tools/epub_prep.py" "$root/$volume/main.tex" "$out/epub.tex" "$out/figures"
  (cd "$root/$volume" &&
    pandoc "$out/epub.tex" -f latex -t epub3 --mathml --toc --toc-depth=2 \
      --split-level=1 --number-sections --epub-cover-image="$out/cover.png" \
      --lua-filter="$root/tools/epub.lua" --css="$root/tools/epub.css" \
      --epub-embed-font="$root/common/fonts/*.otf" --epub-embed-font="$root/common/fonts/*.ttf" \
      --metadata title="${title:-$volume}" --metadata subtitle="$(python3 -c 'import json,sys; from pathlib import Path; print(json.loads(Path(sys.argv[1]).read_text()).get(sys.argv[2], ""))' "$root/common/volume-subtitles.json" "$num")" --metadata author="SEGHAIER Oussama" --metadata lang=en \
      --metadata date=2026 --metadata rights="$(python3 "$root/tools/epub_prep.py" --rights "$root/$volume/main.tex")" \
      --metadata subject=Mathematics \
      -o "$root/dist/$public.epub")
  python3 "$root/tools/epub_fix.py" "$root/dist/$public.epub"
  # The online reader for the website: one HTML page per chapter, from the same LaTeX as the EPUB.
  python3 "$root/tools/reader.py" "$volume" "$out" "$root/dist/html/$volume"
  python3 "$root/tools/check_cover_template.py" "$out/cover.pdf" --number "$num" --cover-png "$out/cover.png" --epub "$root/dist/$public.epub" --reader "$root/dist/html/$volume"
  echo "   dist/$public.pdf (7 x 10 in)  dist/$public.epub  dist/html/$volume/"
  echo "   KDP: dist/kdp/$public - Print.pdf ($pages interior pages); dist/kdp/$public - Paperback Cover.pdf (spine ${spine}in)"
done
