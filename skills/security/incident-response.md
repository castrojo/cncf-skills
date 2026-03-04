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
