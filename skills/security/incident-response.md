---
id: incident-response
title: "Create or Update an Incident Response Plan"
version: "1.1.0"
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

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Document assignment of security response roles and how reports are handled** (Required)
- **Third Party Security Review — moderate and low findings planned/tracked for resolution** (Required)
- **Document Security Self-Assessment** (Required) — the incident response plan is a prerequisite document referenced in the self-assessment

What graduation reviewers specifically check:

1. **Link to the security self-assessment** — graduation requires a completed security self-assessment in the TAG Security format (`https://tag-security.cncf.io/community/assessments/guide/self-assessment/`). The incident response plan should cross-link to it under the Remediation or Post-Incident Review section; the self-assessment in turn describes the incident response process. Reviewers verify this cross-linking exists.

2. **Third Party Security Review integration** — if the project has undergone a TPR, the incident response plan must reference how TPR findings feed into the remediation process. Add a section: "Incorporating Security Review Findings" that describes how issues identified in a TPR are triaged, assigned, and tracked to resolution.

3. **Private patch development access** — the graduation security review checks that the private fork/advisory mechanism actually works before it is needed. Verify that the GitHub Security Advisory draft workflow is enabled for the repository and that all security contacts can access draft advisories. Document this verification step in the plan.

4. **Disclosure timeline matches SECURITY.md** — reviewers check that the timeline in the incident response plan (triage window, patch window, disclosure window) is consistent with what SECURITY.md promises reporters. Inconsistencies are a finding. Run a diff between the two documents before submitting the graduation application.
