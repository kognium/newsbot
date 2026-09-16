#!/usr/bin/env python3
"""Validate Newsbot's media profile catalog."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


CATALOG = Path(__file__).resolve().parents[1] / "references" / "media-profiles.yaml"
CONFIDENCE = {"low", "medium", "high"}
REVIEW_STATUS = {"seed", "reviewed", "needs_review"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    errors: list[str] = []

    if data.get("schema_version") != 1:
        fail(errors, "schema_version must be 1")

    sources = data.get("sources", {})
    outlets = data.get("outlets", [])
    seen_ids: set[str] = set()

    if not sources:
        fail(errors, "catalog must contain sources")
    if not outlets:
        fail(errors, "catalog must contain outlets")

    for outlet in outlets:
        outlet_id = outlet.get("id", "<missing-id>")
        if outlet_id in seen_ids:
            fail(errors, f"duplicate outlet id: {outlet_id}")
        seen_ids.add(outlet_id)

        required = {
            "name",
            "edition",
            "base_country",
            "languages",
            "outlet_type",
            "ownership",
            "alignment_priors",
            "domestic_orientation",
            "evidence",
            "review",
        }
        for key in sorted(required - outlet.keys()):
            fail(errors, f"{outlet_id}: missing {key}")

        ownership_confidence = outlet.get("ownership", {}).get("confidence")
        if ownership_confidence not in CONFIDENCE:
            fail(errors, f"{outlet_id}: invalid ownership confidence")

        for index, prior in enumerate(outlet.get("alignment_priors", [])):
            weight = prior.get("weight")
            if not isinstance(weight, (int, float)) or not 0 <= weight <= 1:
                fail(errors, f"{outlet_id}: prior {index} weight must be between 0 and 1")
            if prior.get("confidence") not in CONFIDENCE:
                fail(errors, f"{outlet_id}: prior {index} has invalid confidence")
            for key in ("target", "dimension", "rationale"):
                if not prior.get(key):
                    fail(errors, f"{outlet_id}: prior {index} missing {key}")
            for source_id in prior.get("evidence", []):
                if source_id not in sources:
                    fail(errors, f"{outlet_id}: prior {index} references unknown source {source_id}")

        orientation = outlet.get("domestic_orientation", {})
        strength = orientation.get("strength")
        if not isinstance(strength, (int, float)) or not 0 <= strength <= 1:
            fail(errors, f"{outlet_id}: domestic orientation strength must be between 0 and 1")
        if orientation.get("confidence") not in CONFIDENCE:
            fail(errors, f"{outlet_id}: invalid domestic orientation confidence")
        for source_id in orientation.get("evidence", []):
            if source_id not in sources:
                fail(errors, f"{outlet_id}: domestic orientation references unknown source {source_id}")

        for source_id in outlet.get("evidence", []):
            if source_id not in sources:
                fail(errors, f"{outlet_id}: references unknown source {source_id}")

        if outlet.get("review", {}).get("status") not in REVIEW_STATUS:
            fail(errors, f"{outlet_id}: invalid review status")

    for source_id, source in sources.items():
        if not source.get("url", "").startswith("https://"):
            fail(errors, f"source {source_id}: URL must use https")
        for key in ("title", "publisher", "source_type"):
            if not source.get(key):
                fail(errors, f"source {source_id}: missing {key}")

    if errors:
        print("Profile validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(outlets)} outlet profiles and {len(sources)} sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
