# Cover and UI fonts

Cormorant Garamond (static Regular, Medium, Medium Italic, SemiBold and Bold) is
taken from the upstream OFL release at https://github.com/CatharsisFonts/Cormorant
and is used for cover titles, subtitles and back-cover prose. The licence is
`OFL-CormorantGaramond.txt`.

Fira Sans Light (`FiraSans-Light.otf`) is the OFL face used for volume numbers
and the author line. Its licence is `OFL-FiraSans.txt`.

# Inter cover/UI weights

Inter is distributed under the accompanying SIL Open Font License. These static
300 upright, 600 upright and 300 italic instances use optical size 32 from the
Google Fonts Inter variable sources (https://github.com/google/fonts/tree/main/ofl/inter).
They typeset only variable cover text and the web UI. The approved common lettering
and the entire Volume 0 front are taken directly from the immutable approved image.


The locked series master also uses `Inter-Bold.ttf`, a weight-700 optical-size-32
static instance of the Google Fonts Inter variable source, internally named
Inter Display Bold. Every production title, including Volume 0, uses this one
face; see `tools/assets/series-template.json` and the series manifest for hashes.
The original common masthead/author lettering remains a shared traced vector form.
The earlier approval PNGs are archival references, rather than live title layouts.
