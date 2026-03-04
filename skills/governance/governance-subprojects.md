---
id: governance-subprojects
title: "Document Subprojects in Governance (GOVERNANCE-subprojects.md)"
version: "1.0.0"
domain: governance
cncf_requirement: encouraged
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/GOVERNANCE-subprojects.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/governance/"
tags:
  - governance
  - subprojects
  - scope
---

# Document Subprojects in Governance (GOVERNANCE-subprojects.md)

## When to use this skill

Use when:
- A project has grown to include multiple distinct components or repos
- Different teams own different parts of the codebase
- CNCF reviewers request a subproject inventory during due diligence

Do NOT use when:
- The project is a single repository with no distinct ownership areas — subproject governance adds structure without benefit at that scale

## What this skill does

Creates or updates `GOVERNANCE-subprojects.md` with the list of official subprojects,
their scope, ownership, and relationship to the top-level project governance.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/project-template/blob/main/GOVERNANCE-subprojects.md`

2. List all official subprojects. For each one, document:
   - Name and GitHub repository URL
   - Brief description of scope
   - Maintainer list (or reference to the subproject's own MAINTAINERS.md)
   - Relationship to the top-level project (same governance, delegated governance, etc.)

3. Define the process for **creating a new subproject**: proposal, approval threshold,
   and required files (OWNERS, MAINTAINERS, README).

4. Define the process for **archiving a subproject**: inactivity criteria, deprecation
   notice, transition plan.

5. Ensure CODEOWNERS in each subproject repo is consistent with the governance doc.

6. Remove all `TODO` markers and instruction links.

## Validation checklist

- [ ] All active subprojects listed with repo URLs
- [ ] Each subproject has a named maintainer or ownership reference
- [ ] New subproject creation process documented
- [ ] Subproject archiving process documented
- [ ] Consistent with CODEOWNERS in each subproject repo
- [ ] No `TODO` markers remain

## Common mistakes

- **Listing effectively-archived repos as active subprojects** — each listed subproject implies active maintenance and CNCF due-diligence coverage; remove or explicitly mark archived repos
- **Not specifying whether subprojects inherit or delegate governance** — this is the most common gap in subproject docs and the first question a TOC reviewer will ask
- **CODEOWNERS not updated in each listed subproject repo** — the governance doc and CODEOWNERS must be consistent; publish the doc and update CODEOWNERS in the same PR batch
