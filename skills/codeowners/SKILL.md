---
id: codeowners
title: "Create or Update a CODEOWNERS File"
description: "Creates or updates CODEOWNERS to assign code review ownership by directory or file pattern. Use when a CNCF project needs to define who must approve changes to specific parts of the codebase."
version: "2.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners"
tags:
  - governance
  - ownership
  - code-review
  - maintainers
mcp_servers:
  - id: github
    description: "Check file existence, list repo structure, create .github/CODEOWNERS, verify branch protection"
    url: "https://github.com/github/mcp-server-github"
---

Create or update `.github/CODEOWNERS` mapping file path patterns to GitHub users or
teams responsible for reviewing changes, and enforce it via branch protection.

## When to use

Use when:
- The project does not yet have a CODEOWNERS file and wants automatic review requests on PRs
- MAINTAINERS.md has been updated and ownership mappings need to stay in sync
- A maintainer has stepped down and their paths must be reassigned
- Preparing a CNCF graduation application that requires evidence of distributed ownership

Do NOT use when:
- The project uses Kubernetes-style OWNERS files managed by prow/tide — those use a different format; adapt the concept but do not create a GitHub CODEOWNERS file on top of them
- The repo is a single-file or documentation-only project with no meaningful directory structure

## Steps

1. **Check for an existing CODEOWNERS file.**
   If GitHub MCP available: `github_get_contents` path=`.github/CODEOWNERS`
   Otherwise: check `.github/CODEOWNERS`, `CODEOWNERS` (root), `docs/CODEOWNERS` — GitHub reads in that order.

2. **Inventory maintainer responsibilities** from MAINTAINERS.md.

3. **Use `@org/team` references** instead of individual handles where GitHub teams exist.
   ⚠️ Individual handles require manual updates on every maintainer rotation; teams do not.

4. **Define the catch-all last:**
   ```
   *  @my-org/maintainers
   ```
   ⚠️ GitHub uses the last matching rule — placing `*` first overrides all path-specific rules.

5. **Add path-specific rules** for core, CLI, docs, CI paths:
   ```
   /pkg/core/  @my-org/core-maintainers
   /cmd/       @alice @bob
   /docs/      @my-org/docs-maintainers
   /.github/   @my-org/maintainers
   ```

6. **Verify no single person is sole owner of all critical paths.**
   ⚠️ Sole ownership of critical paths is a bus-factor flag at graduation review.

7. **Cross-check every handle and team against MAINTAINERS.md.** Remove emeritus/former maintainers.
   ⚠️ Stale handles not in MAINTAINERS.md signals governance drift to reviewers.

8. **Enable "Require review from Code Owners"** in branch protection on the default branch.
   ⚠️ Without this, CODEOWNERS is advisory only — PRs can merge without owner approval.

9. **Validate** by opening a test PR and confirming GitHub auto-requests the correct reviewers.

## Checklist

- [ ] CODEOWNERS file exists at `.github/CODEOWNERS`
- [ ] Catch-all `*` rule maps to full maintainer team (placed last)
- [ ] Every critical directory (core, API, CI, docs) has an explicit rule (graduation)
- [ ] No single handle is sole owner of all critical paths (graduation)
- [ ] All handles and teams match active entries in MAINTAINERS.md (graduation)
- [ ] `@org/team` references used instead of individuals where teams exist
- [ ] Branch protection "Require review from Code Owners" enabled on default branch (graduation)
- [ ] Test PR confirmed GitHub auto-requested correct reviewers
