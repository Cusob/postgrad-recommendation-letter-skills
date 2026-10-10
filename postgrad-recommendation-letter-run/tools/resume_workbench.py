#!/usr/bin/env python3
"""Validate the exact resume path recorded in profile.json.

This tool deliberately never searches for a replacement file and never
modifies profile.json. The path in the profile is the only source of truth.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("profile.json must contain a JSON object")
    return value


def workspace_from_profile(profile_path: Path) -> Path:
    # .postgrad-recommendation-letter/profile.json lives one level below the workspace.
    return profile_path.resolve().parent.parent


def resolve_registered_path(raw_path: str, profile_path: Path) -> Path:
    candidate = Path(raw_path).expanduser()
    if not candidate.is_absolute():
        candidate = workspace_from_profile(profile_path) / candidate
    return candidate.resolve()


def validate_profile(profile_path: Path) -> Dict[str, Any]:
    profile_path = profile_path.resolve()
    profile = load_json(profile_path)
    resume = profile.get("resume")
    if not isinstance(resume, dict):
        return {
            "status": "invalid_profile",
            "reason": "missing_resume_record",
            "profile_path": str(profile_path),
        }
    raw_path = resume.get("path")
    recorded_hash = str(resume.get("sha256") or "").lower()
    if not raw_path or not recorded_hash:
        return {
            "status": "invalid_profile",
            "reason": "resume_path_or_hash_missing",
            "profile_path": str(profile_path),
        }

    registered_path = resolve_registered_path(str(raw_path), profile_path)
    result: Dict[str, Any] = {
        "status": "unknown",
        "profile_path": str(profile_path),
        "registered_path_raw": str(raw_path),
        "registered_path": str(registered_path),
        "recorded_sha256": recorded_hash,
        "replacement_search": "not_performed",
    }
    if not registered_path.exists():
        result.update({
            "status": "registered_file_missing",
            "reason": "the_exact_registered_resume_path_does_not_exist",
        })
        return result
    if not registered_path.is_file():
        result.update({
            "status": "registered_path_not_file",
            "reason": "the_exact_registered_resume_path_is_not_a_file",
        })
        return result

    actual_hash = sha256_file(registered_path).lower()
    result["actual_sha256"] = actual_hash
    if actual_hash != recorded_hash:
        result.update({
            "status": "registered_file_changed",
            "reason": "the_exact_registered_resume_file_hash_changed",
        })
        return result
    result["status"] = "valid"
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the exact profile resume path")
    parser.add_argument("profile", help="path to .postgrad-recommendation-letter/profile.json")
    args = parser.parse_args(argv)
    try:
        result = validate_profile(Path(args.profile))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "valid" else 1


if __name__ == "__main__":
    raise SystemExit(main())
