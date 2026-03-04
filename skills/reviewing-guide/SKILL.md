---
id: reviewing-guide
title: "Create or Update a REVIEWING.md"
version: "1.1.0"
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
---

# Create or Update a REVIEWING.md

## When to use this skill

Use when:
- A project wants to define a consistent, written review process
- Reviewer behavior is inconsistent across contributors
- New maintainers need guidance on the project's review norms

Do NOT use when:
- The project enforces review rules via tooling (OWNERS files, required status checks) — document the tool config, not a separate narrative guide
- The project has 1-2 maintainers — a formal reviewing guide adds friction without benefit at that scale; revisit when a third reviewer joins

## What this skill does

Creates or updates `REVIEWING.md` by filling out the CNCF template with
project-specific reviewer roles, values, process steps, and a review checklist.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/project-template/blob/main/REVIEWING.md`

2. Check if `REVIEWING.md` exists in the repository root.

3. Fill in **The Reviewer Role** section:
   - Who is allowed to review? (anyone, or only those with write access?)
   - Are maintainers and reviewers distinct roles?
   - Does the project have an OWNERS file or GitHub CODEOWNERS?

4. Fill in the **Values** section with the project's review values.
   Suggested defaults: kindness, patience, educational over gatekeeping.

5. Fill in the **Process** section. Answer each question:
   - Do reviewers assign PRs or apply labels on first look?
   - Does automation run before human review?
   - How many approvals required to merge?
   - Can a maintainer merge their own PR after approval?
   - Emergency merge policy (critical CVE, broken build)?

6. Fill in the **Checklist** section with the project's review checklist.
   Suggested items:
   - [ ] Code matches the stated intent of the PR
   - [ ] Tests cover the new behavior
   - [ ] Documentation updated if user-facing behavior changed
   - [ ] No new dependencies added without maintainer discussion
   - [ ] CI checks pass

7. Remove all prompts and instruction links.

## Validation checklist

- [ ] Reviewer Role section clearly defines who may review
- [ ] Values section present
- [ ] Process section filled in (not placeholder)
- [ ] Checklist section contains project-specific items
- [ ] No instruction links remain

## Common mistakes

- **Emergency merge policy left blank** — this is the section most likely to be needed on a Friday and least likely to have been written; it must exist before it is needed
- **Approval count set higher than active maintainer count** — requiring 3 approvals with 2 active maintainers stalls every PR; set a count the team can actually meet
- **"Can a maintainer merge their own PR?" left unanswered** — this is a common source of conflict; the answer must be explicit in the Process section

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Documentation of how to contribute, with increasing detail as the project matures** (Required) — a REVIEWING.md that did not exist at sandbox stage is direct evidence of maturity progression
- **Governance is up to date with actual project activities** (Required) — the review process must reflect how reviews actually happen, not how they were intended to happen at project inception

What graduation reviewers specifically check:

1. **Security-aware review checklist** — the graduation application's Third Party Security Review section notes that findings often include recommendations to "improve project contribution guide [by] providing a PR review guide to look for memory leaks and other vulnerabilities the project may be susceptible to by design or language choice." Add at least one security-focused item to the review checklist (e.g., "No new unsafe memory patterns introduced", "Dependencies from trusted sources only", "No secrets or credentials in diff").

2. **Evidence the process is followed** — reviewers look at recent PRs to see if review comments match the stated values and process. A REVIEWING.md that says "kindness first" but has a history of harsh review comments is a governance red flag. If the existing PR history does not match, update the document to reflect reality or update the practice — but not both unless the change is real.

3. **Emergency merge process** — graduation reviewers verify that the project can respond to a critical CVE without its governance process becoming a bottleneck. The emergency merge policy is the signal that the project has thought about this.
