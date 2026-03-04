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
| `id` | yes | Stable kebab-case identifier — never change after v1.0 |
| `title` | yes | Human-readable skill name |
| `version` | yes | semver — bump minor for new instructions, major for breaking changes |
| `domain` | yes | `contribution`, `governance`, `security`, or `lifecycle` |
| `cncf_requirement` | yes | `required`, `encouraged`, or `optional` |
| `applies_to` | yes | List of: `sandbox`, `incubating`, `graduated` |
| `template_source` | yes | Canonical GitHub URL of the upstream template file |
| `how_to_guide` | no | URL to the contribute.cncf.io how-to page |
| `tags` | no | Free-form list of searchable tags |

## Modifying an Existing Skill

- **Non-breaking** (better wording, additional guidance): bump patch version
- **New required step**: bump minor version
- **Removed or renamed field / changed step contract**: bump major version

## Adding Support for a New Agent Tool

Add one section to `adapters/README.md`. Nothing else.
