#!/usr/bin/env python3
"""Render all skill files into a Goose toolkit.yaml."""

import argparse
import glob
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


def render(skills_dir: str, output_path: str) -> None:
    skill_files = sorted(glob.glob(os.path.join(skills_dir, "*/SKILL.md")))
    instructions = []
    for sf in skill_files:
        meta, body = parse_skill(sf)
        instructions.append(
            {
                "name": meta["id"],
                "description": meta["title"],
                "instructions": body,
            }
        )
        print(f"  included: {meta['id']}")

    toolkit = {
        "toolkit": {
            "name": "cncf-skills",
            "description": "AI agent skills for CNCF project maintainers",
            "instructions": instructions,
        }
    }
    with open(output_path, "w") as f:
        yaml.dump(toolkit, f, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-dir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    render(args.skills_dir, args.output)
