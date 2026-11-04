#!/usr/bin/env python3
"""Audit generated Volume 2 navigation without assigning editorial approval.

Run against an immutable, completed book build. Uses only the standard library.
The library index belongs to the assembled site, so a book-only build records it
as pending instead of declaring it checked. External URLs are not fetched.
"""

import argparse
from collections import Counter
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import posixpath
import subprocess
from urllib.parse import unquote, urlsplit
import zipfile


class Page(HTMLParser):
    def __init__(self, data):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.roles = []
        self.stack = []
        self.feed(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        roles = [name for name in attrs.get("class", "").split()
                 if name in ("exercise", "hint", "solution")]
        record = None
        if roles:
            record = {"role": roles[0], "id": attrs.get("id"),
                      "number": attrs.get("data-number"), "targets": []}
            self.roles.append(record)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        for key in ("href", "src", "poster"):
            if attrs.get(key):
                self.links.append((tag, key, attrs[key]))
        if tag == "a" and attrs.get("href"):
            for _, parent in self.stack:
                if parent is not None:
                    parent["targets"].append(attrs["href"])
        void_tags = ("area", "base", "br", "col", "embed", "hr", "img",
                     "input", "link", "meta", "param", "source", "track", "wbr")
        if tag not in void_tags:
            self.stack.append((tag, record))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break


def destination(source, url):
    return (posixpath.normpath(posixpath.join(posixpath.dirname(source),
                                            unquote(url.path)))
            if url.path else source)


def audit(files, read, scope, documents=None):
    pages = {name: Page(read(name).decode("utf-8"))
             for name in sorted(files if documents is None else documents)
             if name.endswith((".html", ".xhtml", ".opf", ".ncx"))}
    errors, external, pending = [], [], []
    counts, exercises = Counter(), {}
    local_links = 0
    for name, page in pages.items():
        duplicates = [key for key, count in Counter(page.ids).items() if count > 1]
        if duplicates:
            errors.append({"file": name, "duplicate_ids": duplicates})
        for _, _, target in page.links:
            url = urlsplit(target)
            if url.scheme or url.netloc:
                external.append(target)
                continue
            local_links += 1
            dest = destination(name, url)
            if dest not in files and f"{dest}/index.html" in files:
                dest = f"{dest}/index.html"
            if dest not in files:
                if scope == "reader" and dest == "index.html":
                    pending.append({"source": name, "target": target,
                                    "reason": "Library index requires assembled site."})
                else:
                    errors.append({"source": name, "target": target,
                                   "error": "missing_file"})
            elif (url.fragment and dest in pages
                  and unquote(url.fragment) not in pages[dest].ids):
                errors.append({"source": name, "target": target,
                               "error": "missing_fragment"})
        for role in page.roles:
            counts[role["role"]] += 1
            if role["role"] == "exercise":
                key = role["id"]
                if not key or key in exercises:
                    errors.append({"file": name, "missing_or_duplicate_exercise": key})
                exercises[key] = {"file": name, "number": role["number"],
                                  "hint": 0, "solution": 0}
    for name, page in pages.items():
        for role in page.roles:
            if role["role"] not in ("hint", "solution"):
                continue
            # The first anchor is the heading's prompt backlink. Exercise IDs
            # have both ex: and pb: prefixes; do not infer keys from one prefix.
            if not role["targets"]:
                errors.append({"file": name, "role": role["role"],
                               "error": "missing_prompt_backlink"})
                continue
            url = urlsplit(role["targets"][0])
            key = unquote(url.fragment)
            if key not in exercises:
                errors.append({"file": name, "role": role["role"],
                               "unknown_exercise": key})
                continue
            exercises[key][role["role"]] += 1
            if destination(name, url) != exercises[key]["file"]:
                errors.append({"file": name, "role": role["role"],
                               "incorrect_prompt_file": role["targets"][0]})
    for key, record in exercises.items():
        if (record["hint"], record["solution"]) != (1, 1):
            errors.append({"exercise": key, "destinations": record})
    expected = {"exercise": 144, "hint": 144, "solution": 144}
    if dict(counts) != expected:
        errors.append({"expected_roles": expected, "actual_roles": dict(counts)})
    return {"scope": scope, "document_count": len(pages),
            "local_references_checked": local_links,
            "external_references_not_fetched": len(external),
            "role_counts": dict(counts), "exercise_destinations": exercises,
            "site_references_pending": pending, "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-commit", help="Verified provenance for an extracted CI artifact without Git metadata")
    args = parser.parse_args()
    root = args.dist.resolve()
    revision = args.source_commit or subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    reader_root = root / "html" / "volume2-integers"
    files = {path.relative_to(root).as_posix(): path
             for path in root.rglob("*") if path.is_file()}
    # Include sibling download/library targets but parse only this volume.
    documents = [name for name, path in files.items()
                 if path.is_relative_to(reader_root)]
    reader = audit(files, lambda name: files[name].read_bytes(), "reader", documents)
    epub = root / "Volume 2 - The Integers.epub"
    with zipfile.ZipFile(epub) as archive:
        ebook = audit(set(archive.namelist()), archive.read, "epub")
    hashes = {path.relative_to(root).as_posix():
              hashlib.sha256(path.read_bytes()).hexdigest()
              for path in sorted(reader_root.rglob("*"))
              if path.is_file() and path.suffix in (".html", ".css", ".js")}
    report = {
        "source_commit": revision,
        "method": "All generated href/src/poster local files and fragments, duplicate IDs, "
                  "and exactly one hint and solution backlink per exercise. "
                  "No visual, external-URL, Kindle or editorial approval is inferred.",
        "reader_file_sha256": hashes,
        "epub_sha256": hashlib.sha256(epub.read_bytes()).hexdigest(),
        "reader": reader, "epub": ebook,
    }
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    for result in (reader, ebook):
        print(f"{result['scope']}: {result['local_references_checked']} local references, "
              f"{len(result['exercise_destinations'])} exercise triples, "
              f"{len(result['errors'])} errors, "
              f"{len(result['site_references_pending'])} site references pending")
    return int(bool(reader["errors"] or ebook["errors"]))


if __name__ == "__main__":
    raise SystemExit(main())
