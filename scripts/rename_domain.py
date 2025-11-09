import os
import sys
from pathlib import Path

OLD = "www.flyerstrust.org"
NEW = "www.flyerscharitabletrust.org"

# File extensions to scan
EXTS = {
    ".html", ".htm", ".css", ".js", ".json", ".xml", ".txt"
}


def should_scan(path: Path) -> bool:
    # Skip common binary/asset folders
    parts = {p.lower() for p in path.parts}
    if any(skip in parts for skip in {"fonts", "images", ".git", ".venv", "node_modules"}):
        return False
    return path.suffix.lower() in EXTS


def replace_in_file(fp: Path) -> int:
    try:
        text = fp.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return 0
    if OLD not in text:
        return 0
    new_text = text.replace(OLD, NEW)
    if new_text != text:
        fp.write_text(new_text, encoding="utf-8")
        return new_text.count(NEW)  # crude count of occurrences (post-change)
    return 0


def main(root: Path) -> int:
    changed = 0
    files_changed = 0
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            fp = Path(dirpath) / name
            if should_scan(fp):
                count = replace_in_file(fp)
                if count:
                    files_changed += 1
                    changed += count
                    print(f"Updated: {fp}")
    print(f"Done. Files changed: {files_changed}, occurrences now set to '{NEW}': {changed}")
    return 0


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    sys.exit(main(project_root))
