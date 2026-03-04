---
id: reviewing-guide
title: "Create or Update a REVIEWING.md"
version: "1.0.0"
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
