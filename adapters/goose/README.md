# Goose Adapter

Generates a single `toolkit.yaml` from all skill files under
`adapters/goose/output/`.

## Usage

```bash
bash adapters/goose/generate.sh
```

## Output

`adapters/goose/output/toolkit.yaml` — a Goose toolkit manifest with all
skills as named instructions.

## Installing into a Goose project

Reference the generated toolkit in your Goose config:

```yaml
toolkits:
  - path: /path/to/cncf-skills/adapters/goose/output/toolkit.yaml
```
