# CNCF Skills

A collection of tool-agnostic AI agent skills for CNCF project maintainers.

Each skill guides an AI agent (OpenCode, Goose, or any compatible tool) through
creating, updating, or auditing a required CNCF community health file.

## Structure

- `skills/` — one Markdown file per skill, organized by domain
- `adapters/` — per-tool generators that produce native artifacts from skill files
- `schema/` — JSON Schema for skill front-matter validation

## Domains

| Domain | Skills | CNCF Requirement |
|---|---|---|
| `contribution` | contributing-guide, reviewing-guide, issue-labels | required / encouraged |
| `governance` | maintainers-list, contributor-ladder, governance docs | required / encouraged |
| `security` | security-policy, security-contacts, incident-response, embargo docs | required / encouraged |
| `lifecycle` | _(reserved for future growth)_ | — |

## Using a Skill

### OpenCode

Run the adapter to generate OpenCode-native artifacts:

```bash
bash adapters/opencode/generate.sh
```

Then install the output into your project's `.opencode/skills/` directory.

### Goose

```bash
bash adapters/goose/generate.sh
```

Then reference the generated `toolkit.yaml` in your Goose configuration.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache 2.0
