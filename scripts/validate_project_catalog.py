#!/usr/bin/env python3
"""Validate the machine-readable PowerFM project catalog using only stdlib."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit

REQUIRED_PROJECT_FIELDS = {
    "id", "name", "category", "description", "homepage",
    "tasks", "modalities", "resources",
}
REQUIRED_RESOURCE_FIELDS = {"type", "label", "url"}


def _is_https_url(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlsplit(value)
    return (
        parsed.scheme == "https"
        and bool(parsed.hostname)
        and parsed.username is None
        and parsed.password is None
    )


def validate_catalog(catalog: object) -> list[str]:
    """Return all catalog validation errors, or an empty list when valid."""
    errors: list[str] = []
    if not isinstance(catalog, dict):
        return ["catalog root must be a JSON object"]
    if catalog.get("catalog_version") != 1:
        errors.append("catalog_version must equal 1")
    if not isinstance(catalog.get("title"), str) or not catalog["title"].strip():
        errors.append("title must be a non-empty string")
    if not isinstance(catalog.get("source"), str) or not catalog["source"].strip():
        errors.append("source must be a non-empty string")
    projects = catalog.get("projects")
    if not isinstance(projects, list) or not projects:
        errors.append("projects must be a non-empty list")
        return errors

    seen_ids: set[str] = set()
    for index, project in enumerate(projects):
        prefix = f"projects[{index}]"
        if not isinstance(project, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = sorted(REQUIRED_PROJECT_FIELDS - project.keys())
        if missing:
            errors.append(f"{prefix} missing required fields: {', '.join(missing)}")
        project_id = project.get("id")
        if not isinstance(project_id, str) or not project_id.strip():
            errors.append(f"{prefix}.id must be a non-empty string")
        elif project_id in seen_ids:
            errors.append(f"{prefix}.id duplicates {project_id!r}")
        else:
            seen_ids.add(project_id)

        for field in ("name", "category", "description"):
            value = project.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}.{field} must be a non-empty string")
        if not _is_https_url(project.get("homepage")):
            errors.append(f"{prefix}.homepage must be an absolute HTTPS URL")

        for field in ("tasks", "modalities"):
            values = project.get(field)
            if (not isinstance(values, list) or not values
                    or any(not isinstance(item, str) or not item.strip() for item in values)):
                errors.append(f"{prefix}.{field} must be a non-empty list of strings")
            elif len(set(values)) != len(values):
                errors.append(f"{prefix}.{field} must not contain duplicates")

        resources = project.get("resources")
        if not isinstance(resources, list) or not resources:
            errors.append(f"{prefix}.resources must be a non-empty list")
            continue
        for resource_index, resource in enumerate(resources):
            rprefix = f"{prefix}.resources[{resource_index}]"
            if not isinstance(resource, dict):
                errors.append(f"{rprefix} must be an object")
                continue
            missing_resource = sorted(REQUIRED_RESOURCE_FIELDS - resource.keys())
            if missing_resource:
                errors.append(
                    f"{rprefix} missing required fields: {', '.join(missing_resource)}"
                )
            for field in ("type", "label"):
                value = resource.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{rprefix}.{field} must be a non-empty string")
            if not _is_https_url(resource.get("url")):
                errors.append(f"{rprefix}.url must be an absolute HTTPS URL")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "catalog",
        nargs="?",
        type=Path,
        default=Path("catalog/projects.json"),
        help="catalog JSON path (default: catalog/projects.json)",
    )
    args = parser.parse_args()
    try:
        catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"error: cannot read {args.catalog}: {exc}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"error: invalid JSON in {args.catalog}: {exc}", file=sys.stderr)
        return 2

    errors = validate_catalog(catalog)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Catalog valid: {args.catalog} ({len(catalog['projects'])} projects)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
