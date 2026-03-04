---
id: embargo
title: "Draft an Embargo Notice for a Security Release"
version: "1.1.0"
domain: security
cncf_requirement: optional
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/tag-security/blob/main/project-resources/templates/embargo.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/security/"
tags:
  - security
  - embargo
  - communication
---

# Draft an Embargo Notice for a Security Release

## When to use this skill

Use when:
- A security release is scheduled and distributors need advance notice
- An embargo notice needs to be sent to the distributors list

Do NOT use when:
- No embargo policy exists yet — the policy must be in place before sending an embargo notice; use the embargo-policy skill first
- The vulnerability is already public — there is nothing to embargo; move directly to the incident response plan

## What this skill does

Drafts a specific embargo notice for a security release, to be sent to the
distributors list before the public disclosure date.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/tag-security/blob/main/project-resources/templates/embargo.md`

2. Fill in the **Vulnerability Summary**: CVE ID (if assigned), affected component,
   severity (CVSS score), and a non-identifying description that avoids exposing
   exploitable details.

3. Fill in the **Patch Availability**: when the patch will be available, which
   versions are affected, and where distributors can access the private patch branch
   (GitHub private fork or security advisory draft).

4. Fill in the **Public Disclosure Date**: the exact date and time (with timezone)
   when the embargo lifts and the public advisory is published.

5. Send via the distributors list channel defined in the embargo policy.

6. Track responses: note which distributors have acknowledged and are ready.

## Validation checklist

- [ ] CVE ID included (or noted as pending)
- [ ] Affected versions listed
- [ ] Private patch access instructions included
- [ ] Public disclosure date and time (with timezone) specified
- [ ] Sent to the distributors list before public disclosure

## Common mistakes

- **Vulnerability summary contains exploitable detail** — write the summary as if it could be leaked; severity + component + CVE ID is sufficient; no proof-of-concept details or reproduction steps
- **No receipt confirmation from distributors before the embargo lifts** — silence is not consent; follow up with non-respondents at 24h before the disclosure date
- **Disclosure date/time in local timezone** — every distributor operates in a different timezone; use UTC for the public disclosure date and time, always

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **History of regular, quality releases** (Required) — security releases handled through a documented embargo process are direct evidence of release quality and process maturity

What graduation reviewers specifically check:

1. **Evidence of process execution** — graduation reviewers look for whether the security response process has been used in practice, not just documented. If the project has issued one or more security releases, note them in the graduation application. The existence of a sent embargo notice (even if the CVE details are redacted) is evidence that the process works end-to-end.

2. **GitHub Security Advisory published** — when the embargo lifts, the public disclosure should appear as a GitHub Security Advisory in the repository. This feeds CVE databases automatically and is indexed by security scanners. Graduation reviewers may check whether past security releases have published advisories; missing advisories for known CVEs are a finding.
