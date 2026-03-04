---
id: contributor-ladder
title: "Create or Update a CONTRIBUTOR_LADDER.md"
version: "1.1.0"
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

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Document a complete maintainer lifecycle process (including roles, onboarding, offboarding, and emeritus status)** (Required)
- **Document how role, function-based members, or sub-teams are assigned, onboarded, and removed** (Required)
- **Demonstrate usage of the maintainer lifecycle with outcomes** (Required — behavioral, not just documented)

What graduation reviewers specifically check:

1. **Evidence the ladder has been used** — this is the most commonly missed graduation criterion. The graduation application asks projects to "demonstrate usage of the maintainer lifecycle with outcomes, either through the addition or replacement of maintainers as project events have required." A ladder that was written but never exercised does not satisfy this. Before applying, compile a list of PRs or issues where contributors were advanced (or offboarded) through the documented process. Link these in the graduation application.

2. **Emeritus status defined and used** — graduation reviewers look for emeritus entries in MAINTAINERS.md or the contributor ladder doc. An emeritus section with at least one name signals that the process is real and has been applied when maintainers became inactive.

3. **Affiliation diversity at the top tier** — graduation requires maintainers from ≥2 organizations. The ladder should explicitly state that affiliation diversity is considered when evaluating maintainer nominations — not to discriminate, but to ensure no single organization can block project decisions. This statement protects the project in vendor-neutrality assessments.

4. **Offboarding process documented** — the "removing maintainers" section must define what happens to repo access when a maintainer is offboarded (revoke GitHub org membership, remove from CODEOWNERS, update MAINTAINERS.md). Graduation reviewers check this against the project's actual GitHub team membership.
