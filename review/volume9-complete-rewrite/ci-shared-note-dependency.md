# CI shared-note dependency reconciliation

Run 43619208600 on 66ca56fd5574659147614271c2ea2d2d7d8bd7ae failed the
Volume 3 inventory freshness check. The shared canonical cover-notes file is
tracked by that inventory and its conceptual ledger. The Volume 9 note was
rewritten in 331fa2c3 and its required cover-generator credit restored in c724c7f4.

Before regeneration, the complete generated inventory was compared as data with
the checked-in inventory. Only the supporting-source hash for
common/cover-notes.json differed. All Volume 3 source files, review items,
figures, historical images and reference edges were identical.

The full conceptual snapshot was separately compared path by path. Again, only
common/cover-notes.json differed. The recorded snapshot is refreshed following
the existing Volume 6, 7 and 8 hash-only reconciliation practice. Each of the
120 existing entries retains its anchors, classifications, substantive review
text and statuses; the refresh history explicitly says this is not a new
mathematical approval. No archived source-freeze evidence is rewritten.

Actual checks after reconciliation:

- inventory.py --check: exit 0, 1,681 items across 23 source files.
- registers.py: exit 0, 1,177 accepted-internal, 19 pending (unchanged).
- check_global_ledgers.py: exit 0, 120 conceptual entries and 89 earlier-source
  occurrences retain their previous internal statuses.

This fixes a build dependency; it is not a claim that the failing CI run passed.
