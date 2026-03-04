---
id: contributor-ladder
title: "Create or Update a CONTRIBUTOR_LADDER.md"
description: "Creates or updates CONTRIBUTOR_LADDER.md defining roles, responsibilities, and advancement paths from contributor to maintainer. Use when a CNCF project wants to formalize how contributors grow and earn commit rights."
version: "2.0.0"
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
mcp_servers:
  - id: github
    description: "Check file existence, fetch template, create or update CONTRIBUTOR_LADDER.md"
    url: "https://github.com/github/mcp-server-github"
---

Create or update `CONTRIBUTOR_LADDER.md` with the project's roles, responsibilities,
and advancement criteria from Community Participant through Maintainer and above.

## When to use

Use when:
- A project wants to define clear paths for contributor advancement
- New contributors ask "how do I become a maintainer?"
- The project is preparing for CNCF incubation or graduation review

Do NOT use when:
- The project has fewer than 6 months of history and 1-2 contributors — a ladder creates governance overhead before there is anyone to advance; add it when a second contributor is ready to become a reviewer

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/project-template/CONTRIBUTOR_LADDER.md`
   Otherwise: `gh api repos/cncf/project-template/contents/CONTRIBUTOR_LADDER.md`

2. **Check if the file exists.**
   If GitHub MCP available: `github_get_contents` path=`CONTRIBUTOR_LADDER.md`
   Otherwise: `gh api repos/{owner}/{repo}/contents/CONTRIBUTOR_LADDER.md`

3. **Trim default roles** to match actual project structure. The template includes
   Community Participant, Contributor, Organization Member, Reviewer, Maintainer.
   ⚠️ Remove unused tiers rather than leaving them empty — empty tiers confuse new contributors.

4. **For each role, define:**
   - Responsibilities (what they do)
   - Requirements (what qualifies someone)
   - Privileges (what access they have)

5. **Fill in nomination and voting process** for each role transition.
   ⚠️ Define the exact vote threshold and quorum — "maintainer consensus" is too vague and leads to disputes.

6. **Add an emeritus section** defining what happens when a maintainer becomes inactive.
   ⚠️ GitHub org membership access must be explicitly revoked at offboarding — document this step.

7. **Add an affiliation diversity note** stating that maintainer diversity across organizations
   is considered in nominations. See graduation-checklist skill for the exact requirement.

8. **Remove all TODO markers and instruction links.**

## Checklist

- [ ] All roles reflect the project's actual governance structure
- [ ] Each role has defined responsibilities, requirements, and privileges
- [ ] Advancement process is documented for each role transition with vote threshold and quorum (graduation)
- [ ] Emeritus status defined and applies to at least one past maintainer (graduation)
- [ ] Offboarding explicitly revokes GitHub org membership (graduation)
- [ ] Affiliation diversity considered in maintainer nominations (graduation)
- [ ] No `TODO` markers remain
