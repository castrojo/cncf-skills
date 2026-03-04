# SKILL_FORMAT_V2.md — Authoritative v2 Skill Format Specification

> All skill rewrites must conform to this document exactly.
> Read this before writing or editing any skill in the v2 format.

---

## File location

Each skill lives at `skills/<skill-id>/SKILL.md`.
Heavy content lives at `skills/<skill-id>/references/<filename>.md`.

## Size constraints

- `SKILL.md` body: **50-80 lines** (excluding front-matter)
- `references/*.md`: unlimited — loaded only on demand

## Front-matter (YAML, required)

```yaml
---
id: kebab-case-id
title: "Human-readable title"
version: "2.0.0"
domain: contribution | governance | security | lifecycle
cncf_requirement: required | encouraged | optional
applies_to: [sandbox, incubating, graduated]   # one or more
template_source: "https://..."

# Optional
how_to_guide: "https://..."
tags: [tag1, tag2]

# Optional — list MCP servers this skill can use
mcp_servers:
  - id: github
    description: "Check file existence, create files, open PRs"
    url: "https://github.com/github/mcp-server-github"
  - id: cncf-landscape
    description: "Verify project maturity level and landscape metadata"
    url: "https://github.com/cncf/landscape-mcp"
---
```

## Body structure (REQUIRED sections in this order)

1. **Opening sentence (no heading).** 1-2 sentences. What artifact this skill creates or manages. Imperative voice.

2. **`## When to use`** — Positive triggers as a bullet list. Followed immediately by `Do NOT use when:` (inline, no separate heading) for negative conditions.

3. **`## Steps`** — Numbered. Each step: bold title + action description. MCP tool call first, CLI fallback second. Inline `⚠️` warning within the step where relevant (not in a separate section).

4. **`## Reference files`** — Bullet list of `references/` files with one-line description each. Omit this section if there are no reference files.

5. **`## Checklist`** — Checkboxes. Verifiable items only. Mark graduation-required items with `(graduation)` at the end of the line.

## MCP step pattern (required for any step that touches the repo)

```
If GitHub MCP available: `github_get_contents` path=CONTRIBUTING.md
Otherwise: `gh api repos/{owner}/{repo}/contents/CONTRIBUTING.md`
```

## What to REMOVE from v1 skills

| v1 section | v2 replacement |
|---|---|
| `## What this skill does` | Opening 1-2 sentence description (no heading) |
| `## Common mistakes` | Inline `⚠️` warnings within the relevant step |
| `## Graduation readiness` | `(graduation)` markers on checklist items only |
| Inline template content | `references/template.md` (loaded on demand) |
| Repeated graduation criteria text | Cross-reference: "See graduation-checklist skill" |

## What to move to references/

- Any template file > 20 lines (CONTRIBUTING.md, SECURITY.md, etc.)
- GitHub Actions workflow YAML
- Policy text templates
- Full embargo notice templates

## MCP server assignments by domain

| Domain | MCP servers |
|---|---|
| All skills | `github` |
| lifecycle skills | `github` + `cncf-landscape` |

## Graduation markers

Add `(graduation)` to the END of any checklist item that is required for CNCF graduation.
Example:
```markdown
- [ ] Multi-org maintainer representation (graduation)
```
Do NOT add a `## Graduation readiness` section. Use markers only.

## Version

Set `version: "2.0.0"` for all rewritten skills.
