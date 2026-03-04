# GitHub Copilot Adapter

Generates a single `copilot-instructions.md` aggregating all skill bodies.

## Output

`output/copilot-instructions.md` — all skills concatenated with `## <skill-title>` headings,
ordered by domain (contribution → governance → security → lifecycle), then alphabetically
within each domain.

## Generate

```bash
bash adapters/github-copilot/generate.sh
```

## Installation

Copy the output file to your repository:

```bash
# New file
cp adapters/github-copilot/output/copilot-instructions.md .github/copilot-instructions.md

# Append to existing file
cat adapters/github-copilot/output/copilot-instructions.md >> .github/copilot-instructions.md
```

The `.github/copilot-instructions.md` file is automatically loaded by GitHub Copilot
for context in your repository.
