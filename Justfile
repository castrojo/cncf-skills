set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    just --list

# Validate all skills against JSON Schema and check links
check:
    bash scripts/validate.sh

# Run all adapter generators
generate:
    bash adapters/opencode/generate.sh
    bash adapters/goose/generate.sh
