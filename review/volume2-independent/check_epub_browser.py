#!/usr/bin/env python3
"""Measure actual EPUB assets in Chromium; this does not certify Kindle.

Requires Playwright and Chromium, outside the standard-library source checks.
Example: python3 review/volume2-independent/check_epub_browser.py BOOK.epub \
    --source-commit SHA --output report.json --screenshots /tmp/epub-screens
Saved screenshots require separate actual visual review.
"""
import argparse
from functools import partial
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import tempfile
import threading
import zipfile

from playwright.sync_api import sync_playwright


MEASURE = r"""() => ({
    viewport: innerWidth, body_width: document.documentElement.scrollWidth,
    images: [...document.images].map(x => {
        const r = x.getBoundingClientRect();
        return {src: x.getAttribute('src'), kind: x.className,
            loaded: x.complete && x.naturalWidth > 0,
            width: r.width, height: r.height,
            natural_width: x.naturalWidth, natural_height: x.naturalHeight,
            outside_viewport: r.left < -1 || r.right > innerWidth + 1,
            aspect_error: Math.abs((r.width / r.height) /
                (x.naturalWidth / x.naturalHeight) - 1)};
    }), fonts: document.fonts.status
})"""


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("epub", type=Path)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--screenshots", type=Path)
    parser.add_argument("--chromium", default="/usr/bin/chromium")
    args = parser.parse_args()
    if args.screenshots:
        args.screenshots.mkdir(parents=True, exist_ok=True)
    rows, captures, problems = [], [], []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        with zipfile.ZipFile(args.epub) as archive:
            archive.extractall(root)
        server = ThreadingHTTPServer(("127.0.0.1", 0),
            partial(QuietHandler, directory=str(root)))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(
                    executable_path=args.chromium, args=["--no-sandbox"])
                for width in (390, 1280):
                    page = browser.new_page(viewport={"width": width, "height": 844})
                    for file in sorted(root.rglob("*.xhtml")):
                        errors, failed = [], []
                        on_error = lambda error: errors.append(str(error))
                        def on_response(response):
                            if response.status >= 400:
                                failed.append({"url": response.url, "status": response.status})
                        page.on("pageerror", on_error)
                        page.on("response", on_response)
                        relative = file.relative_to(root).as_posix()
                        page.goto(f"http://127.0.0.1:{server.server_port}/{relative}",
                                  wait_until="load", timeout=45000)
                        page.evaluate("document.fonts.ready")
                        row = page.evaluate(MEASURE)
                        row.update(file=relative, width=width,
                                   page_errors=errors, http_failures=failed)
                        rows.append(row)
                        if row["body_width"] > width or errors or failed:
                            problems.append({"file": relative, "width": width,
                                             "error": "page overflow or runtime/HTTP error"})
                        for item in row["images"]:
                            if not item["loaded"] or item["outside_viewport"]:
                                problems.append({"file": relative, "width": width,
                                                 "error": "image loading/bounds", "image": item})
                            if ("oc-math-display" in item["kind"]
                                    and item["aspect_error"] > .05):
                                problems.append({"file": relative, "width": width,
                                                 "error": "display aspect distortion >5%", "image": item})
                        images = row.pop("images")
                        displays = [x for x in images if "oc-math-display" in x["kind"]]
                        row.update(
                            image_count=len(images),
                            math_images=sum("oc-math-" in x["kind"] for x in images),
                            display_images=len(displays),
                            max_display_aspect_error=max(
                                (x["aspect_error"] for x in displays), default=0),
                            unloaded_images=[x for x in images if not x["loaded"]],
                            outside_viewport=[x for x in images if x["outside_viewport"]],
                            plates=[x for x in images if "oc-plate" in x["kind"]])
                        if args.screenshots:
                            for kind, selector in (("inline", "img.oc-math-inline"),
                                                   ("display", "img.oc-math-display")):
                                image = page.locator(selector).first
                                if image.count():
                                    dest = args.screenshots / f"{file.stem}-{kind}-{width}.png"
                                    image.locator("xpath=..").screenshot(path=str(dest))
                                    captures.append({"path": str(dest), "actually_opened": False})
                        page.remove_listener("pageerror", on_error)
                        page.remove_listener("response", on_response)
                    page.close()
                browser.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
    result = {"source_commit": args.source_commit,
        "epub_sha256": hashlib.sha256(args.epub.read_bytes()).hexdigest(),
        "method": "Actual unmodified EPUB XHTML/CSS/fonts/PNG assets rendered in Chromium at390/1280px; all image loading/bounds and all display-image intrinsic versus displayed aspect ratios. A5% threshold allows raster/measurement rounding. Screenshots are not approved merely by being saved. No native Kindle or independent human approval.",
        "pages": rows, "problems": problems, "captures": captures}
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(f"{len(rows)} page/viewport checks; {len(problems)} problems")
    return bool(problems)


if __name__ == "__main__":
    raise SystemExit(main())
