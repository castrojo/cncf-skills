---
description: Creates or updates CONTRIBUTING.md using the CNCF template, replacing
  all TODO markers with project-specific content. Use when a CNCF project is missing
  a contributing guide or has unfilled placeholder text.
how_to_guide: https://contribute.cncf.io/projects/best-practices/templates/contributing
id: contributing-guide
mcp_servers:
- description: Check file existence, fetch template, create or update CONTRIBUTING.md
  id: github
  url: https://github.com/github/mcp-server-github
template_source: https://github.com/cncf/project-template/blob/main/CONTRIBUTING.md
---

Create or update `CONTRIBUTING.md` using the CNCF template, replacing all TODO
markers with project-specific content so the guide is free of placeholder text.

## When to use

Use when:
- A CNCF sandbox project does not yet have a `CONTRIBUTING.md` (required for sandbox+)
- An existing `CONTRIBUTING.md` still contains unfilled TODO markers or instruction links
- A maintainer wants to audit the contributing guide for completeness

Do NOT use when:
- The project uses a non-GitHub contribution platform (Gerrit, Phabricator) — the CNCF template assumes GitHub PRs; adapt manually
- The existing `CONTRIBUTING.md` is already complete and project-specific — run the checklist only

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/project-template/CONTRIBUTING.md`
   Otherwise: `gh api repos/cncf/project-template/contents/CONTRIBUTING.md`

2. **Check if the file exists.**
   If GitHub MCP available: `github_get_contents` path=`CONTRIBUTING.md`
   Otherwise: `gh api repos/{owner}/{repo}/contents/CONTRIBUTING.md`
   - Exists: diff against template to identify missing sections.
   - Missing: use template as starting point.

3. **Fill in every TODO marker.** Common markers:
   - `[meetings](TODO)` → project meeting notes URL or CNCF calendar link
   - `[contact us](TODO)` → Slack channel or mailing list URL
   - `[good first issue](TODO)` → `https://github.com/<org>/<repo>/labels/good%20first%20issue`
   - `[help wanted](TODO)` → `https://github.com/<org>/<repo>/labels/help%20wanted`
   ⚠️ Verify the org/repo slug in label URLs exactly matches the repository.

4. **Fill in the PR Lifecycle section** with the project's actual process: review turnaround,
   WIP vs ready-for-review signaling, and merge policy (squash / merge commit / rebase).
   ⚠️ This section is the most commonly skipped and the most visible gap to CNCF reviewers.

5. **Fill in Development Environment Setup:** clone, install dependencies, build, test,
   and optionally preview docs locally.

6. **Keep DCO or CLA — delete the other.**
   ⚠️ Both sections left in is the most frequent template mistake; you must delete one.

7. **Add a PR checklist** with the project's automated checks (e.g., `make test`, `make lint`).

8. **Remove all instruction links** (lines starting with `[Instructions](`).

9. **Verify no TODO markers remain.**
   `grep -c 'TODO' CONTRIBUTING.md` must return 0.

## Checklist

- [ ] No `TODO` markers remain (`grep -c 'TODO' CONTRIBUTING.md` returns 0)
- [ ] No `[Instructions](` links remain
- [ ] Either DCO or CLA section present — not both
- [ ] PR Lifecycle section is filled in (not placeholder) (graduation)
- [ ] Development Environment Setup is filled in (not placeholder) (graduation)
- [ ] PR checklist is project-specific
- [ ] Communications channel is a real link, not generic text (graduation)
- [ ] Meeting link points to CNCF calendar or project calendar entry (graduation)
- [ ] All URLs resolve (meetings, contact, label links)
