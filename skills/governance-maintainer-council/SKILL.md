---
id: governance-maintainer-council
title: "Set Up Maintainer Council Governance (GOVERNANCE-maintainer.md)"
version: "1.1.0"
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
---

# Set Up Maintainer Council Governance (GOVERNANCE-maintainer.md)

## When to use this skill

Use when:
- A project uses a flat maintainer council (no elections, no steering committee)
- New maintainers are added by existing maintainer consensus
- The project needs to document its decision-making process

Do NOT use when:
- The project has a large enough contributor base that contested leadership decisions are expected — governance-elections is more appropriate when maintainer appointments are not universally accepted by the community

## What this skill does

Creates or updates `GOVERNANCE-maintainer.md` with the maintainer council structure,
decision-making process, adding/removing maintainers, and conflict resolution.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/project-template/blob/main/GOVERNANCE-maintainer.md`

2. Fill in the **Maintainer Responsibilities** section: what maintainers are expected
   to do (review cadence, release duties, community management).

3. Fill in the **Decision Making** section:
   - Lazy consensus: silence = approval after N days
   - Voting: when is a formal vote required? What is quorum?
   - Tie-breaking: who breaks ties?

4. Fill in the **Adding Maintainers** section: nomination process, approval threshold,
   onboarding checklist (granting repo access, adding to MAINTAINERS.md, etc.).

5. Fill in the **Removing Maintainers** section: inactivity definition, emeritus
   process, involuntary removal process (conduct violation, etc.).

6. Remove all `TODO` markers and instruction links.

## Validation checklist

- [ ] Maintainer responsibilities defined
- [ ] Decision-making process documented (lazy consensus + formal vote threshold)
- [ ] Maintainer addition process documented
- [ ] Maintainer removal / emeritus process documented
- [ ] No `TODO` markers remain

## Common mistakes

- **Lazy consensus defined without a waiting period** — "silence = approval" is meaningless without a number; the standard is 5-7 business days; state it explicitly
- **Tie-breaking mechanism omitted** — ties happen; the policy must say who resolves them before it is needed in a live conflict (e.g., longest-tenured maintainer, random selection)
- **Self-merge after self-approval allowed** — at minimum require one other maintainer's approval even for maintainers; unchecked self-merge is a common code-of-conduct and security issue source

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Governance clearly documents vendor-neutrality of project direction** (Required)
- **Document how the project makes decisions on leadership roles, contribution acceptance, requests to the CNCF, and changes to governance or project goals** (Required)
- **Governance is up to date with actual project activities, including any meetings, elections, leadership, or approval processes** (Required)

What graduation reviewers specifically check:

1. **Explicit vendor-neutrality statement** — the graduation application has a dedicated checkbox: "All project metadata and resources are vendor-neutral." The governance document must contain an explicit statement that no single company controls project direction. The CNCF vendor-neutrality guide (`https://contribute.cncf.io/maintainers/community/vendor-neutrality/`) defines what this means. Add a "Vendor Neutrality" section to the governance document that cross-links this guide and asserts the project's compliance.

2. **Decision-making process covers CNCF-facing decisions** — graduation reviewers ask how the project decides things like: applying to graduate, accepting CNCF funding for an event, changing the project charter. The governance document must address not just code decisions but project-level decisions that affect the project's relationship with CNCF.

3. **Governance reflects actual current practice** — a common graduation finding is that the governance document was written at sandbox, adopted maintainer council governance, and then the project grew to 15+ contributors but the governance was never updated. Before applying, read every section and verify it describes how decisions actually happen today, not how they were intended to happen originally.

4. **Meeting cadence documented** — graduation asks for "up-to-date public meeting schedulers." If the maintainer council meets regularly, document the cadence and link to the calendar entry or meeting notes archive. This is often missing from governance docs that were written before regular meetings were established.
