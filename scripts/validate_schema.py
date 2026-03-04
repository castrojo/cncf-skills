#!/usr/bin/env python3
"""Validate all skill front-matter against the JSON Schema.

Extra checks beyond JSON Schema (see schema/skill.schema.json for field rules):

  - Body length: the content after the closing '---' must be ≤500 lines.
    Keeps skills context-efficient for agents with limited windows.

  - Description third-person: the 'description' front-matter field must not
    start with a first-person pronoun ("I " or "You "). It should read as a
    third-person summary of what the skill does and when to use it.
"""

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

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)", re.DOTALL)
BODY_LINE_LIMIT = 500
FIRST_PERSON_RE = re.compile(r"^(I |You )", re.IGNORECASE)


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

        front_matter_text = m.group(1)
        body_text = m.group(2)

        # --- Schema validation ---
        try:
            meta = yaml.safe_load(front_matter_text)
            jsonschema.validate(instance=meta, schema=schema)
        except jsonschema.ValidationError as e:
            errors.append(f"  FAIL {sf}: {e.message}")
            continue

        # --- Body line limit ---
        body_lines = body_text.splitlines()
        if len(body_lines) > BODY_LINE_LIMIT:
            errors.append(
                f"  FAIL {sf}: body is {len(body_lines)} lines "
                f"(limit {BODY_LINE_LIMIT})"
            )
            continue

        # --- Description must be third-person ---
        desc = meta.get("description", "")
        if FIRST_PERSON_RE.match(desc):
            errors.append(
                f"  FAIL {sf}: description starts with first-person pronoun "
                f'("{desc[:40]}...") — use third-person'
            )
            continue

        print(f"  OK   {sf}")

    if errors:
        print("\nValidation errors:")
        for e in errors:
            print(e)
        sys.exit(1)
    print(f"\n{len(skill_files)} skills validated successfully.")


if __name__ == "__main__":
    main()
