---
id: adopters
title: "Create or Update an ADOPTERS.md"
version: "2.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/ADOPTERS.md"
how_to_guide: "https://contribute.cncf.io/maintainers/community/users/"
tags:
  - community
  - adopters
  - production-use
  - graduation
mcp_servers:
  - id: github
    description: "Check file existence, fetch template, create ADOPTERS.md, create issue template"
    url: "https://github.com/github/mcp-server-github"
  - id: cncf-landscape
    description: "Verify project maturity level and production adoption metadata"
    url: "https://github.com/cncf/landscape-mcp"
---

Create or update `ADOPTERS.md` with a curated list of organizations running the project
in production and a self-reporting process so adopters can add themselves via PR.

## When to use

Use when:
- A CNCF incubating project does not yet have an `ADOPTERS.md` and is preparing for due diligence
- The graduation application needs to demonstrate at least 3 independent production end users
- Existing entries are stale or the list has fewer than 3 independent end users

Do NOT use when:
- The project is an infrastructure dependency of other CNCF projects but not directly adopted by end users — use the parent project's `ADOPTERS.md`
- The project has not yet reached a level of stability where production adoption is expected (early sandbox stage)

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/project-template/ADOPTERS.md`
   Otherwise: `gh api repos/cncf/project-template/contents/ADOPTERS.md`

2. **Check if ADOPTERS.md exists.**
   If GitHub MCP available: `github_get_contents` path=`ADOPTERS.md`
   If yes: audit entries — confirm each still reflects current production use.

3. **Set up the adopters table:**
   ```
   | Organization | URL | Description of Use |
   ```
   Distinguish End Users from Vendors (separate sections recommended).
   ⚠️ CNCF graduation requires ≥3 independent end users; a list of vendors only does not pass.
   ⚠️ "Independent" means separate legal entities — subsidiaries of the same parent count as one.

4. **Seed with known adopters.** Search GitHub issues, Slack, conference talks (KubeCon),
   community meetings. Contact candidates to confirm production use and open a PR.

5. **Create a self-reporting process:**
   - Add `.github/ISSUE_TEMPLATE/add-adopter.yml` with: org name, URL, description, production-use checkbox, authorization checkbox.
   - Add "Add your organization" instructions at the top of `ADOPTERS.md`.
   ⚠️ Without a self-reporting process the list requires maintainer legwork before every graduation review.

6. **Link from README.md** in a Community or Adopters section.

7. **Verify each entry** before the graduation application: URL resolves, entry reflects
   active production use, submitter had standing to represent the org.

## Checklist

- [ ] `ADOPTERS.md` exists in the repo root
- [ ] Table has Organization, URL, and Description of Use columns
- [ ] No placeholder rows remain
- [ ] All URLs resolve to the correct organization homepage
- [ ] At least 3 independent production end users (graduation — hard gate)
- [ ] Each entry can be verified as current production use (graduation)
- [ ] End Users and Vendors are distinguished (graduation)
- [ ] Self-reporting issue template exists at `.github/ISSUE_TEMPLATE/add-adopter.yml`
- [ ] README.md links to ADOPTERS.md
