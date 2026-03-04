#!/usr/bin/env bash
set -euo pipefail

# GitHub Copilot adapter — generates a single copilot-instructions.md
# Output: adapters/github-copilot/output/copilot-instructions.md

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUTPUT_DIR="${REPO_ROOT}/adapters/github-copilot/output"

command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 required"; exit 1; }
python3 -c "import yaml" 2>/dev/null || { echo "ERROR: PyYAML required (pip install pyyaml)"; exit 1; }

mkdir -p "${OUTPUT_DIR}"

python3 "${REPO_ROOT}/adapters/github-copilot/render.py" \
  --skills-dir "${REPO_ROOT}/skills" \
  --output "${OUTPUT_DIR}/copilot-instructions.md"

echo "GitHub Copilot adapter: output written to ${OUTPUT_DIR}/copilot-instructions.md"
