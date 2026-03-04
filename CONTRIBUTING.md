# Contributing to CNCF Skills

## Adding a New Skill

1. Choose the correct domain directory: `skills/contribution/`, `skills/governance/`,
   `skills/security/`, or `skills/lifecycle/`
2. Copy the template below into a new `kebab-case-name.md` file
3. Fill in all front-matter fields — see `schema/skill.schema.json` for the contract
4. Write the Markdown body following the required sections
5. Run `bash adapters/opencode/generate.sh` locally to verify your skill parses cleanly
6. Open a PR — CI will validate schema, links, and adapter smoke tests

## Skill Template

See `skills/contribution/contributing-guide.md` as a reference implementation.

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
- **Removed or renamed field / changed step contract**: bump major version, update adapter mapping

## Adding a New Tool Adapter

See `adapters/README.md` for the full adapter contract.
