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

### Required front-matter fields

```yaml
---
id: kebab-case-id          # stable identifier; leading underscore allowed for meta-skills
title: "Human-readable title"
description: "Third-person summary of what the skill does and when an agent should invoke it. No first-person pronouns (I, You). Between 20 and 1024 characters."
version: "1.0.0"           # semantic version
domain: contribution       # one of: contribution | governance | security | lifecycle
cncf_requirement: required # one of: required | encouraged | optional
applies_to:                # one or more of: sandbox | incubating | graduated
  - sandbox
template_source: "https://..." # canonical CNCF template URL
---
```

Optional fields: `how_to_guide` (URI), `tags` (string array), `mcp_servers` (see schema).

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
| Required sections (in order) | See below. |

### Required body sections (in order)

```markdown
## When to use this skill
<positive conditions — when the agent SHOULD invoke this>

Do NOT use when:
<negative conditions — when the agent should NOT invoke this>

## What this skill does
<concise description of the outputs and actions>

## Steps
1. Step one
2. Step two
...

## Validation checklist
- [ ] Item one
- [ ] Item two

## Common mistakes
**Mistake title** — explanation of the mistake and how to avoid it.
```

All six sections must be present and in the order shown above.
The "Do NOT use when:" block is inline under the `## When to use this skill` heading,
not a separate heading.

### Checklist for new skills

Before running `just check`, confirm:

- [ ] `id` is kebab-case, unique across all skills in `skills/`
- [ ] `description` is third-person, 20–1024 chars, includes what + when
- [ ] `domain` and `cncf_requirement` use the allowed enum values
- [ ] `applies_to` lists at least one maturity level
- [ ] `template_source` is a valid HTTPS URI
- [ ] Body has all six required sections in the correct order
- [ ] Body is ≤500 lines
- [ ] `just check` passes: 0 errors

