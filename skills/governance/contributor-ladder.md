---
id: contributor-ladder
title: "Create or Update a CONTRIBUTOR_LADDER.md"
version: "1.0.0"
domain: governance
cncf_requirement: encouraged
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/CONTRIBUTOR_LADDER.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/governance/"
tags:
  - governance
  - contributor-growth
  - roles
---

# Create or Update a CONTRIBUTOR_LADDER.md

## When to use this skill

Use when:
- A project wants to define clear paths for contributor advancement
- New contributors ask "how do I become a maintainer?"
- The project is preparing for CNCF incubation or graduation review

Do NOT use when:
- The project has fewer than 6 months of history and 1-2 contributors — a ladder creates governance overhead before there is anyone to advance; add it when a second contributor is ready to become a reviewer

## What this skill does

Creates or updates `CONTRIBUTOR_LADDER.md` with the project's defined contributor
roles, responsibilities, and advancement criteria from Community Participant through
Maintainer and above.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/project-template/blob/main/CONTRIBUTOR_LADDER.md`

2. Review the template's default roles: Community Participant, Contributor,
   Organization Member, Reviewer, Maintainer. Add or remove roles to match
   the project's actual governance structure.

3. For each role, define:
   - Responsibilities (what they do)
   - Requirements (what qualifies someone)
   - Privileges (what access they have)

4. Fill in the nomination and voting process for each advancement.

5. Remove all `TODO` markers and instruction links.

## Validation checklist

- [ ] All roles reflect the project's actual governance structure
- [ ] Each role has defined responsibilities, requirements, and privileges
- [ ] Advancement process is documented for each role transition
- [ ] No `TODO` markers remain

## Common mistakes

- **Copying template roles without removing unused tiers** — if the project has no Reviewers distinct from Maintainers, delete that tier rather than leaving it empty
- **Leaving the nomination and voting process vague** (e.g., "maintainer consensus") — define the exact vote threshold and quorum; ambiguity leads to disputes at the moment when they are hardest to resolve
- **Granting GitHub org membership at the wrong ladder tier** — org membership grants read access to all org repos; only grant it at the tier where that access is appropriate and intentional
