#!/usr/bin/env python3
"""
Validate startup entries for consistency and completeness.
"""

import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
STARTUPS_DIR = DATA_DIR / "startups"


def validate_metrics(slug: str) -> list:
    """Validate metrics.json for a startup."""
    errors = []
    metrics_path = STARTUPS_DIR / slug / "metrics.json"

    if not metrics_path.exists():
        errors.append(f"Missing metrics.json")
        return errors

    with open(metrics_path) as f:
        data = json.load(f)

    required_fields = ["startup", "slug", "source", "metrics"]
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    if "metrics" in data:
        if "mrr" not in data["metrics"]:
            errors.append("Missing mrr in metrics")

    return errors


def validate_index() -> list:
    """Validate index.json structure."""
    errors = []
    index_path = DATA_DIR / "index.json"

    if not index_path.exists():
        errors.append("Missing index.json")
        return errors

    with open(index_path) as f:
        data = json.load(f)

    if "startups" not in data:
        errors.append("Missing startups array")
        return errors

    for startup in data["startups"]:
        if "slug" not in startup:
            errors.append(f"Startup missing slug: {startup}")

    return errors


def main():
    """Run all validations."""
    errors = []

    # Validate index
    errors.extend(validate_index())

    # Validate each startup
    if STARTUPS_DIR.exists():
        for slug_dir in STARTUPS_DIR.iterdir():
            if slug_dir.is_dir():
                errors.extend(validate_metrics(slug_dir.name))

    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("All validations passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
