#!/usr/bin/env python3
"""Render all skill files into Claude Code artifacts."""

import argparse
import glob
import json
import os
import re
import shutil
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

    out = os.path.join(output_dir, skill_id)
    os.makedirs(out, exist_ok=True)

    # SKILL.md — body with front-matter stripped
    with open(os.path.join(out, "SKILL.md"), "w") as f:
        f.write(body + "\n")

    # claude.json — Claude Code skill manifest
    manifest = {
        "name": skill_id,
        "description": meta["title"],
        "version": meta["version"],
    }
    with open(os.path.join(out, "claude.json"), "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    # Copy references/ directory if present
    skill_dir = os.path.dirname(skill_path)
    refs_src = os.path.join(skill_dir, "references")
    if os.path.isdir(refs_src):
        refs_dst = os.path.join(out, "references")
        if os.path.exists(refs_dst):
            shutil.rmtree(refs_dst)
        shutil.copytree(refs_src, refs_dst)

    print(f"  rendered: {skill_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-dir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    skill_files = sorted(glob.glob(os.path.join(args.skills_dir, "*/SKILL.md")))
    for sf in skill_files:
        render(sf, args.output)
