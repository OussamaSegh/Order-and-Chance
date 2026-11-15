# Required Volume 3 validation-record refresh

Volume 10's authorized About the Cover copy is stored in the shared
common/cover-notes.json. The Volume 3 conceptual snapshot and inventory both
fingerprint that file. The initial register and later CI inventory gate failed
because the retained hashes still described the old copy.

Compared every old/new snapshot and inventory entry. The only input whose bytes
changed is common/cover-notes.json, and only its Volume 10 about field changed.
Volume 3 source, mathematics, art, copy, anchors, dependencies and all review
classifications are unchanged. Required record changes are exactly:
review/volume3-internal/concepts.json and inventory.json.

Starting conceptual snapshot:
`0b4d77a6f6abdfbdbea57e0acca23c0ce79e17fde63c128ed2724341da4b56e2`.
Final conceptual snapshot:
`09dce5a7fd978cf3beceb3588108e71404b8fa4a201205340d8a2037b7b9313a`.
Final shared JSON SHA256:
`e2b0dab1f51fb19b768f2c882b83f64c1d74baafd6e1ae244716e2a49538460e`.

The cover-note generator requires 80–150 words and the provenance phrase
“TikZ cover generator”. Both guards are retained. Intermediate copy/hash
checkpoints are historical and are not final validation. The final inventory
comparison has only supporting_sources changed, and within that list only the
shared JSON hash. `inventory.py --check` and `registers.py` both exit 0;
the register retains 1,177 accepted-internal and 19 pre-existing pending items.
This refresh does not claim fresh mathematical certification of Volume 3.
