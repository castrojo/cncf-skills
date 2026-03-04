---
id: embargo
title: "Draft an Embargo Notice for a Security Release"
version: "1.0.0"
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
