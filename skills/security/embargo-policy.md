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

Do NOT use when:
- The project has no downstream distributors who bundle and ship the software — a library consumed only via package managers does not need a distributors embargo policy

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

## Common mistakes

- **Default embargo period longer than 90 days** — this conflicts with coordinated disclosure norms and will draw criticism from security researchers; 45 days non-critical, 7 days critical is the standard
- **No enforcement clause for embargo violations** — the policy needs teeth; specify the consequence for a distributor who discloses early (removal from the list)
- **Publishing the policy before creating the private channel** — the policy references the channel; set up the private mailing list or GitHub team first, then publish the policy
