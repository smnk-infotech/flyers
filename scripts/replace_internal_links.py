#!/usr/bin/env python3
"""Replace WordPress exports with local-relative assets and links."""
from pathlib import Path
import re

BASE_DOMAINS = [
    "https://www.flyerstrust.org",
    "https://flyerstrust.org",
    "https://www.flyerscharitabletrust.org",
    "https://flyerscharitabletrust.org",
]
MAPPINGS = {
    "": "index.html",
    "/": "index.html",
    "/about": "About Us – Flyers Charitable Trust.html",
    "/services": "Services – Flyers Charitable Trust.html",
    "/donation": "Donation – Flyers Charitable Trust .html",
    "/gallery": "Gallery – Flyers Charitable Trust.html",
    "/contact": "Contact US – Flyers Charitable Trust.html",
}

HTML_EXTENSIONS = {".html", ".htm"}

ASSET_EXTENSION_MAP = {
    ".css": "css",
    ".js": "js",
    ".png": "images",
    ".jpg": "images",
    ".jpeg": "images",
    ".gif": "images",
    ".svg": "images",
    ".webp": "images",
    ".ico": "images",
}

ASSET_PATTERN = re.compile(
    r"index\.html/?(?:[^\s\"'<>?]+/)*(?P<filename>[^/\"'<>?]+\.(?:css|js|png|jpg|jpeg|gif|svg|webp|ico))",
    re.IGNORECASE,
)

def replace_urls_in_text(text: str) -> tuple[str, bool]:
    """Replace occurrences of BASE_DOMAIN URLs in the provided text."""
    replaced = False

    for base in BASE_DOMAINS:
        for path, target in MAPPINGS.items():
            for suffix in ("", "/"):
                url = f"{base}{path}{suffix}"
                if url in text:
                    text = text.replace(url, target)
                    replaced = True

        # Handle bare domain cases without trailing path
        if base in text:
            text = text.replace(base, "index.html")
            replaced = True

    return text, replaced


def replace_index_routes(text: str) -> tuple[str, bool]:
    """Convert index.html/<slug> WordPress routes into exported HTML filenames."""
    replaced = False

    for path, target in MAPPINGS.items():
        slug = path.strip("/")
        if not slug:
            continue

        candidates = {
            f"index.html/{slug}/",
            f"index.html/{slug}",
            f"index.html{path}/",
            f"index.html{path}",
        }

        for candidate in candidates:
            if candidate in text:
                text = text.replace(candidate, target)
                replaced = True

    # Collapse redundant homepage pointers like index.html/ into index.html (without touching assets)
    text, collapses = re.subn(r"index\.html/(?=[\"'])", "index.html", text)
    if collapses:
        replaced = True

    return text, replaced


def replace_asset_paths(text: str) -> tuple[str, bool]:
    """Rewrite index.html/wp-content asset URLs to local folders."""
    replaced = False

    def _asset_replacer(match: re.Match[str]) -> str:
        nonlocal replaced
        filename = match.group("filename")
        suffix = Path(filename).suffix.lower()
        target_dir = ASSET_EXTENSION_MAP.get(suffix)
        if not target_dir:
            return match.group(0)

        replaced = True
        return f"{target_dir}/{filename}"

    text, substitutions = ASSET_PATTERN.subn(_asset_replacer, text)
    replaced = replaced or substitutions > 0
    return text, replaced


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = original
    replaced_any = False

    for replacer in (replace_urls_in_text, replace_asset_paths, replace_index_routes):
        updated, replaced = replacer(updated)
        replaced_any = replaced_any or replaced

    if replaced_any:
        path.write_text(updated, encoding="utf-8")
    return replaced_any


def main():
    root = Path(__file__).resolve().parents[1]
    changed_files = []
    for html_file in root.iterdir():
        if html_file.suffix in HTML_EXTENSIONS and html_file.is_file():
            if process_file(html_file):
                changed_files.append(html_file.name)

    if changed_files:
        print("Updated links in:")
        for filename in sorted(changed_files):
            print(f" - {filename}")
    else:
        print("No files required updates.")


if __name__ == "__main__":
    main()
