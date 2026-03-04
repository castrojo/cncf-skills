#!/usr/bin/env bash
set -euo pipefail

# Goose adapter — generates a single toolkit.yaml from all skill files
# Output: adapters/goose/output/toolkit.yaml

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUTPUT_DIR="${REPO_ROOT}/adapters/goose/output"

command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 required"; exit 1; }
python3 -c "import yaml" 2>/dev/null || { echo "ERROR: PyYAML required (pip install pyyaml)"; exit 1; }

mkdir -p "${OUTPUT_DIR}"

python3 "${REPO_ROOT}/adapters/goose/render.py" \
  --skills-dir "${REPO_ROOT}/skills" \
  --output "${OUTPUT_DIR}/toolkit.yaml"

echo "Goose adapter: output written to ${OUTPUT_DIR}/toolkit.yaml"
