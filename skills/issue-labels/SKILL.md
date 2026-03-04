---
id: issue-labels
title: "Set Up Issue Labels for New Contributors"
version: "2.0.0"
domain: contribution
cncf_requirement: encouraged
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/templates/issue-labels"
tags:
  - issues
  - triage
  - contributors
  - onboarding
mcp_servers:
  - id: github
    description: "List labels, create missing labels, list issues"
    url: "https://github.com/github/mcp-server-github"
---

Create the standard CNCF `good first issue` and `help wanted` labels in the GitHub
repository and tag at least a few existing issues to activate the contributor funnel.

## When to use

Use when:
- A project does not have `good first issue` or `help wanted` labels
- Existing labels use inconsistent naming or colors
- A project wants to attract more new contributors

Do NOT use when:
- The repo manages labels via a config file and automation (e.g., a labeler GitHub Action) — update the config file instead of running `gh label create` directly
- The project tracks issues in a non-GitHub system (Jira, GitLab) — apply the equivalent label concept in that tool

## Steps

1. **List current labels.**
   If GitHub MCP available: `github_list_labels` repo=`<org>/<repo>`
   Otherwise: `gh label list --repo <org>/<repo>`

2. **Check for the two required labels:**
   - `good first issue` (color: `#7057ff`)
   - `help wanted` (color: `#008672`)

3. **Create any missing labels.**
   ⚠️ The `--color` flag takes the hex value without `#` (e.g., `7057ff` not `#7057ff`).
   ```
   gh label create "good first issue" --color "7057ff" \
     --description "Good for newcomers" --repo <org>/<repo>
   gh label create "help wanted" --color "008672" \
     --description "Extra attention is needed" --repo <org>/<repo>
   ```

4. **Tag at least 2-3 existing issues** with the new labels.
   ⚠️ Labels with zero tagged issues send no signal to new contributors; tag immediately.
   Choose issues that are self-contained, have clear acceptance criteria, and do not
   require deep knowledge of the codebase.

5. **Add a triage label set** (optional but recommended) for tracking issue status:
   - `triage/accepted` — confirmed valid issue, ready to work on
   - `triage/needs-information` — waiting on reporter response
   - `triage/wontfix` — acknowledged but out of scope
   These complement `good first issue` by keeping the issue queue actionable.

6. **Verify labels appear in the GitHub UI** and match the URLs used in CONTRIBUTING.md.

## Checklist

- [ ] `good first issue` label exists with color `#7057ff`
- [ ] `help wanted` label exists with color `#008672`
- [ ] At least 2 issues tagged with each label (graduation)
- [ ] CONTRIBUTING.md links point to the correct label URLs
- [ ] Open `good first issue` issues have activity in the past 6 months (graduation)
