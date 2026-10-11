#!/usr/bin/env python3
"""Validate Markdown links in the PowerFM catalogue without network access."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

# Covers inline Markdown links and images. Deliberately avoids a network probe:
# external availability is transient, while URL shape and local assets are stable.
MARKDOWN_LINK = re.compile(
    r"!?(?:\[[^\]]*\])\(\s*(?:<([^>]+)>|([^\s)]+))"
)

def check_catalog(readme: Path, root: Path | None = None) -> list[str]:
    """Return actionable diagnostics for invalid URLs and missing local targets."""
    readme = readme.resolve()
    root = (root or readme.parent).resolve()
    if not readme.is_file():
        return [f"{readme}: catalogue file does not exist"]

    errors: list[str] = []
    for line_number, line in enumerate(readme.read_text(encoding="utf-8").splitlines(), 1):
        for match in MARKDOWN_LINK.finditer(line):
            target = (match.group(1) or match.group(2) or "").strip()
            if not target or target.startswith("#"):
                continue

            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                    errors.append(
                        f"{readme}:{line_number}: unsupported or malformed URL: {target}"
                    )
                continue

            local_path = unquote(parsed.path)
            if not local_path:
                continue
            resolved = (readme.parent / local_path).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                errors.append(
                    f"{readme}:{line_number}: local link escapes repository root: {target}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"{readme}:{line_number}: local link target does not exist: {target}"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    errors = check_catalog(args.readme, args.root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Catalogue links valid: {args.readme}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
