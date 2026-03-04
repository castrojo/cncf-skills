---
id: incident-response
title: "Create or Update an Incident Response Plan"
version: "1.0.0"
domain: security
cncf_requirement: encouraged
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/tag-security/blob/main/project-resources/templates/INCIDENT-RESPONSE.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/security/"
tags:
  - security
  - incident-response
  - vulnerability
---

# Create or Update an Incident Response Plan

## When to use this skill

Use when:
- A project has never formally documented how it responds to a confirmed vulnerability
- The project is expanding its security team and needs a shared runbook
- A post-incident review revealed gaps in the response process

Do NOT use when:
- The project does not yet have a `SECURITY.md` — the reporting channel must exist before defining how to respond; create the security policy first

## What this skill does

Creates or updates the incident response document with the step-by-step process
for triaging, remediating, and disclosing a confirmed security vulnerability.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/tag-security/blob/main/project-resources/templates/INCIDENT-RESPONSE.md`

2. Fill in the **Triage** section: who is notified first, how severity is rated
   (CVSS score or project-defined levels), and the decision to patch vs. mitigate.

3. Fill in the **Remediation** section: branching strategy for patches, who has
   access to private security forks, how patches are tested without public disclosure.

4. Fill in the **Coordinated Disclosure** section: how the project notifies downstream
   distributors before public disclosure, the embargo period, and the GitHub Security
   Advisory publishing process.

5. Fill in the **Communication** section: what the public announcement includes,
   which channels are used (GitHub Security Advisory, project mailing list, CNCF blog),
   and who approves the message.

6. Fill in the **Post-Incident Review** section: blameless retrospective process
   and how learnings feed back into the security policy.

## Validation checklist

- [ ] Triage process documented with severity definitions
- [ ] Private patch development process documented
- [ ] Coordinated disclosure timeline defined
- [ ] Public communication plan documented
- [ ] Post-incident review process defined

## Common mistakes

- **"Who has access to private security forks" left undefined** — during an active incident, unclear access control delays patch development; define this in the doc, not in someone's head
- **No named incident commander role** — "the security contacts will handle it" is not a runbook; one named person must own each active incident
- **Post-incident review section skipped** — this is where security posture actually improves; treating every incident as a one-off guarantees the same failures recur
