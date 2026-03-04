#!/usr/bin/env bash
set -euo pipefail

# OpenCode adapter — generates SKILL.md + opencode.json per skill
# Output: adapters/opencode/output/<skill-id>/

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUTPUT_DIR="${REPO_ROOT}/adapters/opencode/output"

command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 required"; exit 1; }
python3 -c "import yaml" 2>/dev/null || { echo "ERROR: PyYAML required (pip install pyyaml)"; exit 1; }

rm -rf "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

python3 "${REPO_ROOT}/adapters/opencode/render.py" \
  --skills-dir "${REPO_ROOT}/skills" \
  --output "${OUTPUT_DIR}"

echo "OpenCode adapter: output written to ${OUTPUT_DIR}"
