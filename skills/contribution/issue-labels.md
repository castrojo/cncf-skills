---
id: issue-labels
title: "Set Up Issue Labels for New Contributors"
version: "1.0.0"
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
---

# Set Up Issue Labels for New Contributors

## When to use this skill

Use when:
- A project does not have `good first issue` or `help wanted` labels
- Existing labels use inconsistent naming or colors
- A project wants to attract more new contributors

Do NOT use when:
- The repo manages labels via a config file and automation (e.g., a labeler GitHub Action) — update the config file instead of running `gh label create` directly
- The project tracks issues in a non-GitHub system (Jira, GitLab) — apply the equivalent label concept in that tool

## What this skill does

Creates or audits the GitHub issue labels recommended by CNCF for new contributor
onboarding. Ensures the project uses the standard label names referenced in
CONTRIBUTING.md templates.

## Steps

1. List current repository labels:
   ```
   gh label list --repo <org>/<repo>
   ```

2. Check for the two required labels:
   - `good first issue` (color: `#7057ff`)
   - `help wanted` (color: `#008672`)

3. For each missing label, create it:
   ```
   gh label create "good first issue" --color "7057ff" \
     --description "Good for newcomers" --repo <org>/<repo>
   gh label create "help wanted" --color "008672" \
     --description "Extra attention is needed" --repo <org>/<repo>
   ```

4. Verify the labels appear in the GitHub UI and match the URLs used in CONTRIBUTING.md.

5. Triage at least 2-3 existing issues and apply `good first issue` or `help wanted`
   where appropriate, so new contributors immediately see labeled issues.

## Validation checklist

- [ ] `good first issue` label exists with standard color (`#7057ff`)
- [ ] `help wanted` label exists with standard color (`#008672`)
- [ ] At least 2 issues tagged with each label
- [ ] CONTRIBUTING.md links to the correct label URLs

## Common mistakes

- **Adding `#` to the color value in `gh label create`** — the `--color` flag takes the hex value without `#` (e.g., `7057ff` not `#7057ff`); the commands in this skill are correct
- **Creating labels but tagging zero existing issues** — new labels with no issues send no signal to new contributors; tag at least 2-3 issues immediately after creating the labels
- **Inconsistent capitalization** (`Good First Issue` vs `good first issue`) — GitHub label search is case-insensitive but CNCF template URLs use lowercase; match the casing exactly
