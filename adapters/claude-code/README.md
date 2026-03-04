# Claude Code Adapter

Generates per-skill output for native Claude Code skill loading.

## Output

For each skill, produces two files in `output/<skill-id>/`:

| File | Contents |
|---|---|
| `SKILL.md` | Skill body (YAML front-matter stripped) |
| `claude.json` | Manifest: `name`, `description`, `version` |
| `references/` | Copied from `skills/<id>/references/` if present |

## Generate

```bash
bash adapters/claude-code/generate.sh
```

## Installation

Copy the output directory into your project:

```bash
# Install all skills
cp -r adapters/claude-code/output/* .claude/skills/

# Or install a single skill
cp -r adapters/claude-code/output/contributing-guide .claude/skills/
```

Or use the skills.sh toolchain:

```bash
npx skills add contributing-guide
```
