"""Fetch latest homepage markup and update local index.html."""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "index.html"
SOURCE_URL = "https://www.flyerstrust.org/wp-json/wp/v2/pages/172"

ASSET_PREFIXES = (
    "https://www.flyerstrust.org/wp-content/uploads/2025/08/",
    "https://flyerstrust.org/wp-content/uploads/2025/08/",
    "https://www.flyerstrust.org/wp-content/uploads/",
    "https://flyerstrust.org/wp-content/uploads/",
)
INTERNAL_LINK_MAP = {
    "https://www.flyerstrust.org/donation/": "Donation.html",
    "https://flyerstrust.org/donation/": "Donation.html",
    "https://www.flyerstrust.org/donation": "Donation.html",
    "https://flyerstrust.org/donation": "Donation.html",
    "https://www.flyerstrust.org/about/": "About-Us.html",
    "https://flyerstrust.org/about/": "About-Us.html",
    "https://www.flyerstrust.org/about": "About-Us.html",
    "https://flyerstrust.org/about": "About-Us.html",
}


def fetch_content() -> str:
    with urllib.request.urlopen(SOURCE_URL) as response:
        payload = json.load(response)
    content = payload["content"]["rendered"]

    for prefix in ASSET_PREFIXES:
        if prefix in content:
            content = content.replace(prefix, "images/")

    for source, target in INTERNAL_LINK_MAP.items():
        if source in content:
            content = content.replace(source, target)

    return content


def replace_block(html: str, replacement: str) -> str:
    marker = '<div data-elementor-type="wp-page" data-elementor-id="172"'
    start = html.find(marker)
    if start == -1:
        raise RuntimeError("Unable to locate Elementor page container.")

    pattern = re.compile(r"<div\b|</div>")
    depth = 0
    end = None
    for match in pattern.finditer(html, start):
        token = match.group(0)
        if token.startswith("<div"):
            depth += 1
        else:
            depth -= 1
        if depth == 0:
            end = match.end()
            break

    if end is None:
        raise RuntimeError("Failed to locate closing </div> for Elementor container.")

    return html[:start] + replacement + html[end:]


def main() -> None:
    content = fetch_content()
    original_html = INDEX_PATH.read_text(encoding="utf-8")
    updated_html = replace_block(original_html, content)
    INDEX_PATH.write_text(updated_html, encoding="utf-8")


if __name__ == "__main__":
    main()
