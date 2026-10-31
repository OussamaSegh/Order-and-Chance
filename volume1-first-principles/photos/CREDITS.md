# Image provenance and reproduction

New photographs are authentic images, not generated illustrations. The Collins
portrait and the Hubble image were retrieved from scikit-image v0.22.0 on
2026-10-27. That version's data documentation records them as public-domain NASA
images:
https://github.com/scikit-image/scikit-image/blob/v0.22.0/skimage/data/_fetchers.py
(functions `astronaut`, `hubble_deep_field`). Captions credit NASA.

The file that used to be `rocket.jpg` was scikit-image's copy of SpaceX Flickr
image 16511594820 (DSCOVR on Falcon 9). Checked on 31 October 2026, the Flickr
page https://www.flickr.com/photos/spacexphotos/16511594820/ marks that
photograph **CC BY-NC 2.0** (`https://creativecommons.org/licenses/by-nc/2.0/`).
scikit-image's docstring still says the image was released into the public
domain. The Flickr page is the licence of record, and a non-commercial licence
does not cover a book for sale. The file has been removed. It is replaced by a
NASA photograph, below. No endorsement is implied.

| Local file | Original credit and source | SHA256 of downloaded original |
|---|---|---|
| astronaut.jpg | NASA, Eileen Collins; https://flic.kr/p/r9qvLn | PNG: 88431cd9653ccd539741b555fb0a46b61558b301d4110412b5bc28b5e3ea6cb5 |
| hubble-deep-field.jpg | NASA, Hubble eXtreme Deep Field; http://hubblesite.org/newscenter/archive/releases/2012/37/image/a/ | 3a19c5dd8a927a9334bb1229a6d63711b1c0c767fb27e2286e7c84a3e2c2f5f4 |
| apollo11.jpg | NASA photograph 6900556, Apollo 11 Saturn V launch, 16 July 1969. https://images.nasa.gov/details-6900556 and the file `https://images-assets.nasa.gov/image/6900556/6900556~orig.jpg`. NASA's media guidelines (https://www.nasa.gov/nasa-brand-center/images-and-media/, read 31 October 2026) say NASA images are generally not subject to copyright in the United States, and that textbook authors may use them without separate permission when NASA is acknowledged and the use does not imply endorsement. The same page says NASA insignia and identifiers are not in the public domain; this credit therefore does not call the photograph public domain. The image metadata names Marshall Space Flight Center and gives no separate copyright holder. | 9046233c2c5b0dc88a8f69e016df4c03171d241d95e42de0b8238b58df0b8754 |

Download URLs for the first two are `https://raw.githubusercontent.com/scikit-image/scikit-image/v0.22.0/skimage/data/`
followed by `astronaut.png` and `hubble_deep_field.jpg`. Those hashes
match scikit-image's versioned `_registry.py`. Astronaut was converted from PNG to
JPEG at quality 95; no scene edits or AI generation. The Hubble file is unmodified.
`apollo11.jpg` is the NASA original JPEG, unmodified, 3000×2380. At the 1.65-inch
print cap the short side is about 1440 pixels per inch.
No endorsement is implied.

Two further public-domain portraits were added for the counting chapter on 30 October 2026, from Wikimedia Commons, with no scene edits:

- `montmort.jpg`, 499×579. Alexis-Simon Belle, portrait of Pierre Rémond de Montmort, about 1715. File:Remond de Montmort.jpg. The Commons page marks the painting public domain (the painter died in 1734). https://commons.wikimedia.org/wiki/File:Remond_de_Montmort.jpg
- `dirichlet.jpg`, 493×545. Anonymous portrait of Peter Gustav Lejeune Dirichlet, before 1859. File:Peter Gustav Lejeune Dirichlet.jpg. The Commons page marks it public domain. https://commons.wikimedia.org/wiki/File:Peter_Gustav_Lejeune_Dirichlet.jpg

At the 1.65-inch cap the effective resolutions are about 351 and 330 pixels per inch. Captions in the chapter carry the credit.

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

## Portraits added with the language chapter

Both are public domain and are credited again in the chapter caption.
Print height is capped at 1.65 in. Neither file is a generated illustration.

| Local file | Source | Pixels | Notes |
|---|---|---|---|
| `boole.jpg` | Engraving of George Boole, *The Illustrated London News*, 21 January 1865. Wikimedia Commons file `Portrait of George Boole.png`. | 960 × 1288 | Scaled from the Commons original and saved as JPEG quality 90. At 1.65 in the short side is above 300 ppi. |
| `cantor.jpg` | Photograph of Georg Cantor, early twentieth century, author unknown. Wikimedia Commons file `Georg Cantor2.jpg`, public-domain mark. | 534 × 700 | Unmodified scene. At the 1.65 in cap the height is about 424 ppi. |
