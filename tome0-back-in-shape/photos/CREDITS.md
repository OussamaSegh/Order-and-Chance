# Image provenance and reproduction

New photographs are authentic images, not generated illustrations. Retrieved from
scikit-image v0.22.0 on 2026-10-27. The data documentation identifies these assets
as public domain:
https://github.com/scikit-image/scikit-image/blob/v0.22.0/skimage/data/_fetchers.py
(functions `astronaut`, `hubble_deep_field`, `rocket`). Captions credit the original providers.

| Local file | Original credit and source | SHA256 of downloaded original |
|---|---|---|
| astronaut.jpg | NASA, Eileen Collins; https://flic.kr/p/r9qvLn | PNG: 88431cd9653ccd539741b555fb0a46b61558b301d4110412b5bc28b5e3ea6cb5 |
| hubble-deep-field.jpg | NASA, Hubble eXtreme Deep Field; http://hubblesite.org/newscenter/archive/releases/2012/37/image/a/ | 3a19c5dd8a927a9334bb1229a6d63711b1c0c767fb27e2286e7c84a3e2c2f5f4 |
| rocket.jpg | SpaceX Photos, DSCOVR launch; https://www.flickr.com/photos/spacexphotos/16511594820/ | c2dd0de7c538df8d111e479619b129464d0269d0ae5fd18ca91d33a7fdfea95c |

Download URLs are `https://raw.githubusercontent.com/scikit-image/scikit-image/v0.22.0/skimage/data/`
followed by `astronaut.png`, `hubble_deep_field.jpg`, `rocket.jpg`. All three hashes
match scikit-image's versioned `_registry.py`. Astronaut was converted from PNG to
JPEG at quality 95; no scene edits or AI generation. The other two are unmodified.
No endorsement is implied.

Existing historical images retain their original chapter captions. Most captions
identify public-domain reproductions. Two require separate attribution:

- d'Alembert: Maurice Quentin de La Tour portrait, photograph by Didier Descouens,
  CC BY-SA 4.0, via Wikimedia Commons; https://creativecommons.org/licenses/by-sa/4.0/.
- Paul Erdős, Budapest 1992: Topsy Kretts, CC BY 3.0, via Wikimedia Commons;
  https://creativecommons.org/licenses/by/3.0/.

These existing images have not been independently re-sourced in this revision;
the final publisher should retain their original provenance records. Their licences
apply to the images, not automatically to the surrounding book. The image captions
and back-matter credits identify exceptions to the book's copyright notice.

Print height is capped per source at pixel height / 300 inches (and at 1.65 inches),
with aspect ratio retained. Actual effective resolutions must be checked in the
final PDF with `pdfimages -list`. All mathematical figures added in this revision
are original vector drawings, with line styles, markers and text suitable for grayscale.
