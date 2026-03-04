# Agent Instructions — cncf-skills

## This repo is intentionally minimal

Skills are markdown files. That is the entire design.

**Before adding any file, script, or tooling, ask:** "Can the agent just read the markdown directly?" If yes, do not add the file.

## What you must not do

- Add scripts to transform, render, or pre-process skills for specific tools
- Add per-tool output directories or generated artifacts
- Create boilerplate (generate scripts, render scripts, adapter classes, registries)
- Generate files, tasks, or commits without the user explicitly asking for them
- Write multi-task plans with multiple commits for work that fits in one commit

## The scope test

A new skill is one file. `just check` validates it. Done.

If adding a skill requires more than that, something has gone wrong.

## Adding a new skill

```
1. Create skills/<id>/SKILL.md with valid YAML front-matter + body
2. Run: just check
Done.
```

## Adding support for a new agent tool

Add one section to `adapters/README.md`. Nothing else.

## Repo structure

```
skills/*/SKILL.md          — one file per CNCF community health template
adapters/README.md         — pointer guide for common agent tools; no scripts
schema/skill.schema.json   — JSON Schema for skill front-matter validation
scripts/validate_schema.py — sole tooling artifact; runs locally and in CI
```

## Validation

```bash
just check   # validates all skill front-matter against the schema
```

---

## Skill authoring requirements

Every `SKILL.md` must have a YAML front-matter block and a body. Both are validated
by `just check`. A skill that fails validation will not be merged.

### Front-matter fields

Per the Claude skill spec (https://docs.anthropic.com/en/docs/claude-code/skills):
- `name` — optional; if omitted, the directory name is used as the slash command
- `description` — recommended; used by Claude to decide when to auto-invoke the skill

This repo's schema requires only `id` (the canonical cross-tool identifier, equal to the
directory name) and `description`. No other fields are required.

**Before adding a front-matter field, ask:** "Does an agent need this to use the skill?"
If no, do not add the field. Metadata that helps humans browse the repo belongs in the
skill body, not the front-matter.

```yaml
---
id: kebab-case-id     # required — stable identifier (leading underscore allowed for meta-skills)
description: "..."    # required — third-person, 20–1024 chars, what + when
---
```

Optional fields (only include if the skill actively uses them):
- `template_source` — URI of the canonical CNCF template
- `how_to_guide` — URI of the CNCF how-to guide
- `mcp_servers` — list of MCP servers the skill uses (see schema for structure)

### `description` field rules (enforced by validator)

The `description` field is used by agents to decide whether to invoke this skill.
Write it as if explaining the skill to another agent in one or two sentences.

| Rule | Detail |
|---|---|
| Third-person only | Do not start with "I" or "You". Write "Creates…", "Guides…", "Audits…", etc. |
| What + when | State what the skill does AND when an agent should use it. |
| Length | 20–1024 characters. |
| No time-sensitive content | Do not reference dates, version numbers, or deadlines. |

**Good example:**
```
Creates or updates SECURITY.md defining the vulnerability reporting process,
disclosure timeline, and supported versions. Use when a CNCF project is
missing a security policy or needs to update reporting instructions.
```

**Bad examples:**
```
# Too vague — no "when":
"Handles security policies."

# First-person — rejected by validator:
"I help you create a SECURITY.md file."

# Time-sensitive — will rot:
"Use this in 2024 when applying for graduation."
```

### Body rules

| Rule | Detail |
|---|---|
| Max 500 lines | Keeps skills context-efficient for agents with limited windows. |

### Checklist for new skills

Before running `just check`, confirm:

- [ ] `id` is kebab-case, unique across all skills in `skills/`
- [ ] `description` is third-person, 20–1024 chars, includes what + when
- [ ] Body is ≤500 lines
- [ ] `just check` passes: 0 errors

