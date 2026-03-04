#!/usr/bin/env bash
set -euo pipefail
# Local validation script (mirrors CI)

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "==> Checking for python3 and PyYAML..."
python3 -c "import yaml" || { echo "ERROR: pip install pyyaml"; exit 1; }

echo "==> Validating skill front-matter schema..."
python3 "${REPO_ROOT}/scripts/validate_schema.py" \
  --schema "${REPO_ROOT}/schema/skill.schema.json" \
  --skills-dir "${REPO_ROOT}/skills"

echo "==> Smoke testing OpenCode adapter..."
bash "${REPO_ROOT}/adapters/opencode/generate.sh"

echo "==> Smoke testing Goose adapter..."
bash "${REPO_ROOT}/adapters/goose/generate.sh"

echo "All checks passed."
