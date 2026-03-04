#!/usr/bin/env python3
"""Validate all skill front-matter against the JSON Schema."""

import argparse
import glob
import json
import re
import sys

try:
    import yaml
    import jsonschema
except ImportError:
    print("ERROR: pip install pyyaml jsonschema", file=sys.stderr)
    sys.exit(1)

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", required=True)
    parser.add_argument("--skills-dir", required=True)
    args = parser.parse_args()

    with open(args.schema) as f:
        schema = json.load(f)

    skill_files = sorted(glob.glob(f"{args.skills_dir}/*/SKILL.md"))
    errors = []

    for sf in skill_files:
        with open(sf) as f:
            content = f.read()
        m = FRONT_MATTER_RE.match(content)
        if not m:
            errors.append(f"  FAIL {sf}: no YAML front-matter found")
            continue
        try:
            meta = yaml.safe_load(m.group(1))
            jsonschema.validate(instance=meta, schema=schema)
            print(f"  OK   {sf}")
        except jsonschema.ValidationError as e:
            errors.append(f"  FAIL {sf}: {e.message}")

    if errors:
        print("\nValidation errors:")
        for e in errors:
            print(e)
        sys.exit(1)
    print(f"\n{len(skill_files)} skills validated successfully.")


if __name__ == "__main__":
    main()
