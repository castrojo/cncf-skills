# Using cncf-skills With Your Agent Tool

> **Design principle:** This repo is optimized for context size and agent consumption.
> Skills are plain markdown files in `skills/*/SKILL.md`. There are no build steps,
> no generated outputs, and no pre-processing. Agents read skills directly.
> Any tool-specific configuration (YAML toolkits, instruction files, config blocks)
> is out of scope — agents generate those on demand from the source files.

## How skills are structured

Each skill lives at `skills/<id>/SKILL.md` with YAML front-matter followed by a
markdown body. Required front-matter: `id` (stable identifier) and `description`
(used by agents to decide when to invoke the skill). The body is the agent instruction.

Some skills include reference templates under `skills/<id>/references/`.

## OpenCode

Point your `opencode.json` at the `skills/` directory. Each `SKILL.md` is loaded
as a named skill. Use the `Skill` tool by name (e.g., `contributing-guide`) to invoke one.

## Claude Code / claude-code

Add the `skills/` directory to your `CLAUDE.md` context, or reference individual
`skills/<id>/SKILL.md` files directly using the Read tool. The `_index` skill
(`skills/_index/SKILL.md`) lists all available skills and their domains.

## Goose

Reference this repo's `skills/` directory in your toolkit configuration.
Each `SKILL.md` is self-contained and can be loaded as an instruction block.
The front-matter `id` field is the canonical skill name.

## GitHub Copilot

Paste the body of relevant `skills/<id>/SKILL.md` files into your
`copilot-instructions.md`, or reference them via `#file:skills/<id>/SKILL.md`
in your prompt.

## Other agents

Read `skills/*/SKILL.md` directly. Strip the `---` delimiters to extract YAML
front-matter; everything after the second `---` is the instruction body.
