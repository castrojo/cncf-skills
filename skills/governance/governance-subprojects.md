---
id: governance-subprojects
title: "Document Subprojects in Governance (GOVERNANCE-subprojects.md)"
version: "1.1.0"
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

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **All subprojects, if any, are listed** (Required)
- **If the project has subprojects: subproject leadership, contribution, maturity status documented, including add/remove process** (Required)

What graduation reviewers specifically check:

1. **Maturity status per subproject** — the graduation application asks for subproject "maturity status." This is separate from the top-level project's maturity level. Add a status field to each subproject entry: `active` (maintained, receives features), `maintained` (bug fixes only), `deprecated` (replacement announced), or `archived` (no longer maintained). Reviewers will ask about any active subproject that has no commits in the past 6 months.

2. **Subproject leadership coverage** — each subproject must have at least one named maintainer. A subproject with no named owner signals a maintenance gap to reviewers. If a subproject genuinely has no active maintainer, mark it deprecated and link the issue tracking its future.

3. **Contribution process per subproject** — if subprojects use different contribution workflows (different review requirements, different test gates), document this. "See top-level CONTRIBUTING.md" is acceptable if the process is truly identical, but reviewers verify this claim.

4. **Add/remove process exists and has been used** — similar to the maintainer lifecycle check, reviewers look for evidence that the subproject governance has actually been exercised: was a subproject ever added post-incubation? Was one archived? If so, link the relevant issue or PR in the graduation application. If not, state this explicitly — "no subprojects have been added or removed since project inception" is an acceptable answer.
