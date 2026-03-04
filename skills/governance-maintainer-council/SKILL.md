---
id: governance-maintainer-council
title: "Set Up Maintainer Council Governance (GOVERNANCE-maintainer.md)"
version: "2.0.0"
domain: governance
cncf_requirement: encouraged
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/GOVERNANCE-maintainer.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/governance/"
tags:
  - governance
  - maintainers
  - decision-making
mcp_servers:
  - id: github
    description: "Check file existence, fetch template, create or update GOVERNANCE-maintainer.md"
    url: "https://github.com/github/mcp-server-github"
---

Create or update `GOVERNANCE-maintainer.md` with the maintainer council structure,
decision-making process, add/remove procedures, and conflict resolution.

## When to use

Use when:
- A project uses a flat maintainer council (no elections, no steering committee)
- New maintainers are added by existing maintainer consensus
- The project needs to document its decision-making process

Do NOT use when:
- The project's contributor base has grown to the point where maintainer appointments are contested — use governance-elections instead

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/project-template/GOVERNANCE-maintainer.md`
   Otherwise: `gh api repos/cncf/project-template/contents/GOVERNANCE-maintainer.md`

2. **Fill in Maintainer Responsibilities**: review cadence, release duties, community management.

3. **Fill in Decision Making:**
   - Lazy consensus: silence = approval after N days (standard: 5-7 business days).
   ⚠️ "Silence = approval" is meaningless without a number — state it explicitly.
   - Formal vote: when required and what is quorum.
   - Tie-breaking: who resolves ties.
   ⚠️ Ties happen in live conflicts; the policy must exist before it is needed.

4. **Fill in Adding Maintainers**: nomination process, approval threshold, onboarding
   checklist (repo access, add to MAINTAINERS.md).
   ⚠️ Require at least one other maintainer's approval even for maintainer self-merges.

5. **Fill in Removing Maintainers**: inactivity definition, emeritus process,
   involuntary removal process (conduct violation).

6. **Add a Vendor Neutrality section** asserting vendor-neutral project direction
   and cross-linking `https://contribute.cncf.io/maintainers/community/vendor-neutrality/`.

7. **Document meeting cadence** and link to calendar or meeting notes archive.

8. **Remove all TODO markers and instruction links.**

## Checklist

- [ ] Maintainer responsibilities defined
- [ ] Lazy consensus waiting period stated explicitly (graduation)
- [ ] Formal vote threshold and quorum defined (graduation)
- [ ] Tie-breaking mechanism stated
- [ ] Maintainer addition process documented
- [ ] Emeritus and removal processes documented (graduation)
- [ ] Vendor Neutrality section with cross-link present (graduation)
- [ ] Meeting cadence documented and calendar linked (graduation)
- [ ] Governance reflects actual current practice, not original intent (graduation)
- [ ] No `TODO` markers remain
