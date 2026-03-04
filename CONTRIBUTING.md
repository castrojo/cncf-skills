# Contributing to CNCF Skills

## Adding a New Skill

1. Create `skills/<id>/SKILL.md` with valid YAML front-matter + body
2. Fill in all front-matter fields — see `schema/skill.schema.json` for the contract
3. Write the Markdown body following the required sections
4. Run `just check` to verify the skill parses cleanly
5. Open a PR — CI will validate schema and links

## Skill Template

See `skills/contributing-guide/SKILL.md` as a reference implementation.

## Front-matter Fields

| Field | Required | Description |
|---|---|---|
| `id` | yes | Stable kebab-case identifier — never change after publishing |
| `description` | yes | Third-person, 20–1024 chars, what the skill does and when to use it |
| `template_source` | no | Canonical GitHub URL of the upstream CNCF template file |
| `how_to_guide` | no | URL to the contribute.cncf.io how-to page |
| `mcp_servers` | no | MCP servers this skill uses (see schema for structure) |

See `schema/skill.schema.json` for the authoritative contract and
`https://docs.anthropic.com/en/docs/claude-code/skills` for Claude's skill spec.

## Modifying an Existing Skill

- **Better wording, additional guidance**: update the body, re-run `just check`
- **New required step or changed instructions**: update the body, re-run `just check`

## Adding Support for a New Agent Tool

Add one section to `adapters/README.md`. Nothing else.
