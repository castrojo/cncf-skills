---
id: maintainers-list
title: "Create or Update a MAINTAINERS.md"
version: "2.0.0"
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
mcp_servers:
  - id: github
    description: "Check file existence, fetch template, create or update MAINTAINERS.md, verify org membership"
    url: "https://github.com/github/mcp-server-github"
---

Create or update `MAINTAINERS.md` with the current list of project maintainers,
their GitHub handles, employer affiliations, and areas of ownership.

## When to use

Use when:
- A new CNCF sandbox project needs to establish its MAINTAINERS.md (required)
- Maintainer affiliations or areas have changed
- CNCF staff requests an updated maintainer list

Do NOT use when:
- The project uses an automated OWNERS file as the sole authoritative source — OWNERS files are machine-read by Prow/Tide; MAINTAINERS.md is the human-readable companion, not a replacement

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/project-template/MAINTAINERS.md`
   Otherwise: `gh api repos/cncf/project-template/contents/MAINTAINERS.md`

2. **Replace `<Project Name>`** with the actual project name throughout.

3. **For each current maintainer, add a table row:**
   - Full name, GitHub handle, employer/affiliation, area of ownership (optional)
   ⚠️ Verify affiliations against current employment — outdated entries are flagged at graduation due diligence.
   ⚠️ "Independent" is not a second organization for multi-org diversity purposes.

4. **Check multi-org diversity.** Count distinct employer affiliations.
   ⚠️ Graduation requires maintainers from at least 2 organizations — this is a hard gate.

5. **Ensure consistency** with root-level approvers in OWNERS / CODEOWNERS.

6. **Notify CNCF staff** if this is the initial creation by updating:
   `https://github.com/cncf/foundation/blob/master/project-maintainers.csv`
   ⚠️ CNCF cannot include the project in official maintainer counts until this CSV is updated.

7. **Remove all TODO markers and instruction links.**

## Checklist

- [ ] Project name replaced throughout
- [ ] All current maintainers listed with correct affiliations
- [ ] Affiliations verified against current employment (graduation)
- [ ] Maintainers from at least 2 organizations (graduation — hard gate)
- [ ] Domain of responsibility column present (graduation)
- [ ] Consistent with OWNERS / CODEOWNERS root approvers (graduation)
- [ ] CNCF foundation CSV updated if initial creation
- [ ] No `TODO` markers remain
