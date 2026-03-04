set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    just --list

# Validate all skills against JSON Schema
check:
    python3 scripts/validate_schema.py --schema schema/skill.schema.json --skills-dir skills
