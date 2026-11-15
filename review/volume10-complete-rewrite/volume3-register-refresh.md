# Required Volume 3 register refresh

The register failed after the authorized Volume 10 About the Cover copy edit,
because its whole-volume conceptual snapshot includes common/cover-notes.json.
Compared every old/new snapshot entry: only that JSON file changed. Only its
Volume 10 about field changed; Volume 3 cover copy/art/mathematics did not.
Refreshed the snapshot and matching snapshot hashes without changing any review
classification, anchor, prerequisite evidence or acceptance status.

Old snapshot: `0b4d77a6f6abdfbdbea57e0acca23c0ce79e17fde63c128ed2724341da4b56e2`.
New snapshot: `2cf413ff25d0b68a6856bbe43941a10104b2cb55df713b26afdd5e1152ac16de`.
This required validation record is the only Volume 3 file change.

The CI copy guard requires the provenance phrase “TikZ cover generator”. Restored
that precise phrase in the Volume10 note (no artwork change); final snapshot
is `5cf23ada895083439e3c85a30e07351f285f7bf5cf0503932ac7cfe39f8572ef`. Only the same shared JSON hash changes.

Final cover note retains the generator phrase and required80–150word length.
Snapshot `09dce5a7fd978cf3beceb3588108e71404b8fa4a201205340d8a2037b7b9313a` again changes only the same Volume10 about-field hash.
