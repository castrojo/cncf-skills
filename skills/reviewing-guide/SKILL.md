---
id: reviewing-guide
title: "Create or Update a REVIEWING.md"
version: "2.0.0"
domain: contribution
cncf_requirement: encouraged
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/REVIEWING.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/templates/reviewing"
tags:
  - reviewers
  - code-review
  - process
mcp_servers:
  - id: github
    description: "Check file existence, fetch template, create or update REVIEWING.md"
    url: "https://github.com/github/mcp-server-github"
---

Create or update `REVIEWING.md` with project-specific reviewer roles, values,
process, and a review checklist so review behavior is consistent and documented.

## When to use

Use when:
- A project wants to define a consistent, written review process
- Reviewer behavior is inconsistent across contributors
- New maintainers need guidance on the project's review norms

Do NOT use when:
- The project enforces review rules entirely via tooling (OWNERS files, required status checks) — document the tool config, not a separate narrative guide
- The project has 1-2 maintainers — a formal guide adds friction without benefit at that scale; revisit when a third reviewer joins

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/project-template/REVIEWING.md`
   Otherwise: `gh api repos/cncf/project-template/contents/REVIEWING.md`

2. **Check if REVIEWING.md exists.**
   If GitHub MCP available: `github_get_contents` path=`REVIEWING.md`
   Otherwise: `gh api repos/{owner}/{repo}/contents/REVIEWING.md`

3. **Fill in the Reviewer Role section:**
   - Who may review? (anyone, or only those with write access?)
   - Are maintainers and reviewers distinct roles?
   - Does the project use OWNERS or CODEOWNERS?

4. **Fill in the Values section.** Suggested defaults: kindness, patience, educational over gatekeeping.

5. **Fill in the Process section.** Answer each question explicitly:
   - Do reviewers assign PRs or apply labels on first look?
   - How many approvals required to merge?
   ⚠️ Setting approval count higher than active maintainer count stalls every PR.
   - Can a maintainer merge their own PR after approval?
   ⚠️ Leave this unanswered and it becomes a source of recurring conflict.
   - Emergency merge policy for critical CVEs or broken builds?
   ⚠️ The emergency policy is most needed on a Friday and least likely to have been written.

6. **Fill in the review checklist.** Required items:
   - [ ] Code matches the stated intent of the PR
   - [ ] Tests cover the new behavior
   - [ ] Documentation updated if user-facing behavior changed
   - [ ] No new dependencies added without maintainer discussion
   - [ ] CI checks pass
   Add at least one security-focused item (graduation).

7. **Remove all prompts and instruction links.**

## Checklist

- [ ] Reviewer Role section defines who may review
- [ ] Values section present
- [ ] Process section filled in (not placeholder) (graduation)
- [ ] Approval count ≤ number of active maintainers
- [ ] Emergency merge policy is explicit
- [ ] Review checklist contains at least one security-focused item (graduation)
- [ ] No instruction links remain
