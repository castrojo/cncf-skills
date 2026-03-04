---
id: security-policy
title: "Create or Update a SECURITY.md (Security Policy)"
version: "1.0.0"
domain: security
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/tag-security/blob/main/project-resources/templates/SECURITY.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/security/"
tags:
  - security
  - vulnerability-disclosure
  - cncf-required
  - openssf
---

# Create or Update a SECURITY.md (Security Policy)

## When to use this skill

Use when:
- A CNCF incubating or graduating project does not yet have a `SECURITY.md`
- The existing `SECURITY.md` is missing the reporting channel, response SLA, or supported versions
- A project is working toward an OpenSSF Best Practices badge (requires a security disclosure policy)

Do NOT use when:
- The repository is documentation-only or contains no executable code — link to the parent project's SECURITY.md instead of creating a redundant one

## What this skill does

Creates or updates `SECURITY.md` with the project's vulnerability reporting process,
supported versions matrix, disclosure timeline, and security contact information.
Also guides setup of GitHub private vulnerability reporting and OpenSSF security tooling.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/tag-security/blob/main/project-resources/templates/SECURITY.md`

2. Fill in the **Reporting a Vulnerability** section:
   - Primary channel: use GitHub's private vulnerability reporting
     (`Settings → Code security → Private vulnerability reporting → Enable`)
   - Fallback: security@<project>.io or security@lists.cncf.io if GitHub PVR is not available
   - Do NOT use a public issue tracker for initial disclosure

3. Fill in the **Supported Versions** table: list which release branches currently
   receive security patches. Mark end-of-life versions clearly.

4. Fill in the **Response Timeline** section (CNCF recommended):
   - Acknowledge report: within 2 business days
   - Triage and assign severity: within 5 business days
   - Patch + coordinated disclosure: within 90 days for non-critical; 7 days for critical

5. Enable **GitHub Private Vulnerability Reporting** if not already enabled:
   `https://github.com/<org>/<repo>/settings/security_analysis`

6. Set up **OpenSSF Scorecards** GitHub Action to continuously assess security posture:
   - Add `.github/workflows/scorecard.yml` following the instructions at
     `https://github.com/ossf/scorecard-action`
   - This feeds into the CNCF CLOMonitor dashboard automatically

7. Apply for the **OpenSSF Best Practices badge** at
   `https://bestpractices.coreinfrastructure.org`
   - The passing badge is required for CNCF graduation
   - Add the badge link to README.md after receiving it

8. Remove all `TODO` markers and instruction links.

## Validation checklist

- [ ] Reporting channel documented (GitHub PVR or email)
- [ ] Supported versions table filled in
- [ ] Response timeline defined
- [ ] GitHub Private Vulnerability Reporting enabled in repo settings
- [ ] OpenSSF Scorecards action added (or tracked as a follow-up issue)
- [ ] OpenSSF Best Practices badge application submitted (or link added to README if already earned)
- [ ] No `TODO` markers remain

## Common mistakes

- **Directing reporters to a public GitHub issue** — this exposes the vulnerability before a patch exists; always use GitHub Private Vulnerability Reporting or a private email channel
- **No timezone specified in response timeline** — all dates in coordinated disclosure must use UTC; a timezone-ambiguous disclosure date causes confusion with downstream distributors
- **Supported versions table with no EOL criteria** — reviewers will ask "how does a version reach EOL?"; define the criteria or link to a RELEASES.md that does
- **GitHub Private Vulnerability Reporting not configured** — reporters will try it even if not documented; configure it in repo settings before publishing SECURITY.md
