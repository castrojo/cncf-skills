---
id: embargo-policy
title: "Create or Update the Embargo Policy"
version: "1.0.0"
domain: security
cncf_requirement: optional
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/tag-security/blob/main/project-resources/templates/embargo-policy.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/security/"
tags:
  - security
  - embargo
  - disclosure
---

# Create or Update the Embargo Policy

## When to use this skill

Use when:
- A project distributes software that downstream vendors bundle and ship
- The project needs a formal policy for pre-disclosure to distribution partners
- Setting up a security response committee or distributors list

## What this skill does

Creates or updates the embargo policy governing how and when the project notifies
downstream distributors before public disclosure of a security vulnerability.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/tag-security/blob/main/project-resources/templates/embargo-policy.md`

2. Fill in the **Embargo Period** section: default embargo length (typically 45 days
   for non-critical, 7 days for critical), and the criteria for extending or shortening.

3. Fill in the **Distributors List** section: how vendors join the list, the vetting
   criteria, and the private channel used (private mailing list, GitHub team, etc.).

4. Fill in the **Obligations** section: what distributors must agree to — not disclose
   before the embargo lifts, provide status updates, coordinate patch timing.

5. Remove all `TODO` markers and instruction links.

## Validation checklist

- [ ] Embargo period defined with clear criteria for exceptions
- [ ] Distributor onboarding process documented
- [ ] Distributor obligations documented
- [ ] Private distribution channel identified
- [ ] No `TODO` markers remain
