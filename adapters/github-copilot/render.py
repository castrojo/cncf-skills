#!/usr/bin/env python3
"""Render all skill files into a single GitHub Copilot instructions file."""

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

DOMAIN_ORDER = ["contribution", "governance", "security", "lifecycle"]


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

    # Parse all skills and group by domain
    skills_by_domain: dict[str, list[tuple[dict, str]]] = {d: [] for d in DOMAIN_ORDER}
    other: list[tuple[dict, str]] = []

    for sf in skill_files:
        meta, body = parse_skill(sf)
        domain = meta.get("domain", "")
        if domain in skills_by_domain:
            skills_by_domain[domain].append((meta, body))
        else:
            other.append((meta, body))

    # Build output
    sections = []
    for domain in DOMAIN_ORDER:
        for meta, body in sorted(skills_by_domain[domain], key=lambda x: x[0]["id"]):
            sections.append(f"## {meta['title']}\n\n{body}")
            print(f"  included: {meta['id']}")

    for meta, body in sorted(other, key=lambda x: x[0]["id"]):
        sections.append(f"## {meta['title']}\n\n{body}")
        print(f"  included: {meta['id']}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n\n---\n\n".join(sections) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-dir", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    render(args.skills_dir, args.output)
