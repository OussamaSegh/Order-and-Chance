"""Old published reader URLs.

The spellings in this table are the redirect keys. They are not directory names.
"""
import html
import json

# Published GitHub Pages reader routes before the directory rename.
OLD_STEMS = {
    "tome1-first-principles": "volume1-first-principles",
    "tome2-integers": "volume2-integers",
    "tome3-symmetry": "volume3-symmetry",
    "tome4-chance": "volume4-chance",
    "tome5-calculation": "volume5-calculation",
    "tome6-crossroads": "volume6-crossroads",
    "tome7-spaces": "volume7-spaces",
    "tome8-analysis": "volume8-analysis",
    "tome9-shapes": "volume9-shapes",
    "tome10-abstraction": "volume10-abstraction",
    "tome11-randomness": "volume11-randomness",
    "tome12-random-motion": "volume12-random-motion",
    "tome13-arithmetic": "volume13-arithmetic",
    "tome14-primes": "volume14-primes",
    "tome15-order-and-chance": "volume15-order-and-chance",
}

# Machine filenames and cache keys that used the same prefix.
OLD_PREFIX = "tome"


def redirect_html(target: str) -> str:
    safe = html.escape(target, quote=True)
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        f"<link rel=\"canonical\" href=\"{safe}\">\n"
        f"<meta http-equiv=\"refresh\" content=\"0; url={safe}\">\n"
        "<title>Moved</title>\n"
        f"<script>location.replace({json.dumps(target)});</script>\n"
        "</head>\n<body>\n"
        f"<p><a href=\"{safe}\">This page has moved.</a></p>\n"
        "</body>\n</html>\n"
    )
