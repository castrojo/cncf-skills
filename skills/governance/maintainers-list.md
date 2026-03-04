---
id: maintainers-list
title: "Create or Update a MAINTAINERS.md"
version: "1.0.0"
domain: governance
cncf_requirement: required
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/MAINTAINERS.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/templates/maintainers"
tags:
  - maintainers
  - governance
  - cncf-required
---

# Create or Update a MAINTAINERS.md

## When to use this skill

Use when:
- A new CNCF sandbox project needs to establish its MAINTAINERS.md (required)
- Maintainer affiliations or areas have changed
- CNCF staff requests an updated maintainer list

Do NOT use when:
- The project uses an automated OWNERS file as the sole authoritative source — OWNERS files are machine-read by Prow/Tide; MAINTAINERS.md is the human-readable companion, not a replacement for it

## What this skill does

Creates or updates `MAINTAINERS.md` with the current list of project maintainers,
their GitHub handles, employer affiliations, and (optionally) their specific
areas of ownership.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/project-template/blob/main/MAINTAINERS.md`

2. Replace `<Project Name>` with the actual project name throughout.

3. For each current maintainer, add a table row with:
   - Full name
   - GitHub handle
   - Employer / affiliation
   - Area of ownership (optional — omit column if all maintainers are general)

4. If the project uses an OWNERS file or GitHub CODEOWNERS, ensure this list is
   consistent with the root-level approvers in those files.

5. If the project has a Steering Committee or elected leadership, list those
   members instead of (or in addition to) code approvers.

6. Remove all `TODO` markers and instruction links.

7. After merging, notify CNCF staff if this is the initial creation:
   reference the CNCF foundation maintainer CSV at
   `https://github.com/cncf/foundation/blob/master/project-maintainers.csv`

## Validation checklist

- [ ] Project name replaced throughout
- [ ] All current maintainers listed with correct affiliations
- [ ] No `TODO` markers remain
- [ ] Consistent with OWNERS / CODEOWNERS root approvers
- [ ] CNCF staff notified if initial creation

## Common mistakes

- **Employer listed as "Independent" without verification** — ask the maintainer directly; "independent" vs. employed affects CNCF's vendor-neutrality assessment for incubation and graduation
- **Forgetting the CNCF foundation CSV after initial creation** — CNCF staff cannot include the project in official maintainer counts until `project-maintainers.csv` is updated; this is the step most often skipped
- **MAINTAINERS.md drifting from OWNERS root approvers** — the two must stay in sync; a mismatch is embarrassing during due diligence and easy to prevent with a reminder in the PR template
