#!/usr/bin/env python3
"""Render a single skill file into OpenCode-native artifacts."""

import argparse
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)", re.DOTALL)


def parse_skill(path: str) -> tuple[dict, str]:
    with open(path) as f:
        content = f.read()
    m = FRONT_MATTER_RE.match(content)
    if not m:
        raise ValueError(f"No valid front-matter in {path}")
    meta = yaml.safe_load(m.group(1))
    body = m.group(2).strip()
    return meta, body


def render(skill_path: str, output_dir: str) -> None:
    meta, body = parse_skill(skill_path)
    skill_id = meta["id"]
    domain = meta["domain"]

    out = os.path.join(output_dir, domain, skill_id)
    os.makedirs(out, exist_ok=True)

    # SKILL.md — the Markdown body verbatim
    with open(os.path.join(out, "SKILL.md"), "w") as f:
        f.write(body + "\n")

    # opencode.json — OpenCode skill manifest
    manifest = {
        "name": skill_id,
        "description": meta["title"],
        "version": meta["version"],
        "tags": meta.get("tags", []),
    }
    with open(os.path.join(out, "opencode.json"), "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    print(f"  rendered: {domain}/{skill_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    render(args.skill, args.output)
