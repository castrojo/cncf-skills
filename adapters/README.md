# Adapter Contract

An adapter transforms the tool-agnostic skill files in `skills/` into
artifacts native to a specific AI agent tool.

## Contract

An adapter MUST:

1. Read all `skills/**/*.md` files from the repository root
2. Parse the YAML front-matter block (delimited by `---`)
3. Use the Markdown body (everything after the closing `---`) as the instruction content
4. Write output artifacts to `adapters/<tool>/output/` (gitignored)
5. Exit 0 on success, non-zero on any parse or generation error
6. Be idempotent — running twice produces the same output

An adapter MUST NOT:
- Modify any file in `skills/`
- Commit generated output to version control
- Require network access

## Input: Skill File Structure

```
---
id: contributing-guide
title: "Create or Update a CONTRIBUTING.md"
version: "1.0.0"
domain: contribution
cncf_requirement: required
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/CONTRIBUTING.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/templates/contributing"
tags:
  - onboarding
---

# Markdown body starts here
...
```

## Available Adapters

| Tool | Directory | Output format |
|---|---|---|
| OpenCode | `adapters/opencode/` | `SKILL.md` + `opencode.json` per skill |
| Goose | `adapters/goose/` | `toolkit.yaml` (all skills) |

## Adding a New Adapter

1. Create `adapters/<toolname>/`
2. Write `adapters/<toolname>/generate.sh` — must follow the contract above
3. Write `adapters/<toolname>/README.md` — document the output format and install steps
4. Add a smoke test step to `.github/workflows/validate.yml`
