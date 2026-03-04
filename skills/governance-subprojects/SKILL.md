---
id: governance-subprojects
title: "Document Subprojects in Governance (GOVERNANCE-subprojects.md)"
version: "2.0.0"
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
mcp_servers:
  - id: github
    description: "Check file existence, fetch template, list repos in org, create or update GOVERNANCE-subprojects.md"
    url: "https://github.com/github/mcp-server-github"
---

Create or update `GOVERNANCE-subprojects.md` with the list of official subprojects,
their scope, ownership, maturity status, and relationship to top-level project governance.

## When to use

Use when:
- A project has grown to include multiple distinct components or repos
- Different teams own different parts of the codebase
- CNCF reviewers request a subproject inventory during due diligence

Do NOT use when:
- The project is a single repository with no distinct ownership areas — subproject governance adds structure without benefit at that scale

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/project-template/GOVERNANCE-subprojects.md`
   Otherwise: `gh api repos/cncf/project-template/contents/GOVERNANCE-subprojects.md`

2. **List all official subprojects.** For each one, document:
   - Name and GitHub repository URL
   - Brief scope description
   - Maintainer list or reference to the subproject's own MAINTAINERS.md
   - Maturity status: `active`, `maintained`, `deprecated`, or `archived`
   - Relationship to top-level project governance
   ⚠️ Do NOT list effectively-archived repos as active — each listed subproject implies active maintenance.

3. **Specify governance relationship**: does the subproject inherit top-level governance,
   or is governance delegated?
   ⚠️ This is the first question a TOC reviewer asks — answer it explicitly.

4. **Define the new subproject creation process**: proposal, approval threshold,
   required files (OWNERS, MAINTAINERS, README).

5. **Define the subproject archiving process**: inactivity criteria, deprecation notice, transition plan.

6. **Verify CODEOWNERS** in each subproject repo is consistent with the governance doc.
   ⚠️ Publish the governance doc and update CODEOWNERS in the same PR batch.

7. **Remove all TODO markers and instruction links.**

## Checklist

- [ ] All active subprojects listed with repo URLs (graduation)
- [ ] Each subproject has maturity status: active / maintained / deprecated / archived (graduation)
- [ ] Each subproject has a named maintainer or ownership reference (graduation)
- [ ] Governance relationship (inherited vs. delegated) specified per subproject (graduation)
- [ ] New subproject creation process documented
- [ ] Subproject archiving process documented
- [ ] CODEOWNERS consistent with governance doc in each listed repo
- [ ] No `TODO` markers remain
