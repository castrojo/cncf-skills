# CNCF Skills

A collection of tool-agnostic AI agent skills for CNCF project maintainers.

Each skill guides an AI agent (OpenCode, Goose, or any compatible tool) through
creating, updating, or auditing a required CNCF community health file.

## Structure

- `skills/` — one Markdown file per skill, organized by domain
- `schema/` — JSON Schema for skill front-matter validation

## Domains

| Domain | Skills | CNCF Requirement |
|---|---|---|
| `contribution` | contributing-guide, reviewing-guide, issue-labels | required / encouraged |
| `governance` | maintainers-list, contributor-ladder, governance docs | required / encouraged |
| `security` | security-policy, security-contacts, incident-response, embargo docs | required / encouraged |
| `lifecycle` | _(reserved for future growth)_ | — |

## Using a Skill

Skills are plain markdown files. Point your agent tool at `skills/*/SKILL.md` and
read them directly — no build step, no generation, no pre-processing required.

See [adapters/README.md](adapters/README.md) for tool-specific instructions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache 2.0
