---
id: security-contacts
title: "Create or Update SECURITY_CONTACTS"
version: "1.0.0"
domain: security
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/tag-security/blob/main/project-resources/templates/SECURITY_CONTACTS"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/security/"
tags:
  - security
  - contacts
  - cncf-required
---

# Create or Update SECURITY_CONTACTS

## When to use this skill

Use when:
- A CNCF incubating or graduating project does not have a `SECURITY_CONTACTS` file
- Security contacts have changed (people left, new security leads assigned)
- CNCF staff requests an updated contact list

Do NOT use when:
- The project has a dedicated security team with a formal contact process already published — reference that process and link to it from SECURITY.md rather than duplicating it here

## What this skill does

Creates or updates the `SECURITY_CONTACTS` file in the repository root with the
current list of individuals responsible for handling security disclosures.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/tag-security/blob/main/project-resources/templates/SECURITY_CONTACTS`

2. List each security contact with:
   - Full name
   - GitHub handle
   - (Optional) Email — use a role address like security@<project>.io if possible

3. Ensure at least 2 contacts are listed. Single-contact lists create a bus factor
   risk for security response.

4. Verify each GitHub handle is current and the person is still active on the project.

5. Cross-reference with the `SECURITY.md` reporting channel — the contacts listed
   here should be the recipients of the reporting channel.

## Validation checklist

- [ ] At least 2 security contacts listed
- [ ] All GitHub handles verified as current
- [ ] Consistent with the reporting channel in SECURITY.md
- [ ] No stale contacts (departed maintainers removed)

## Common mistakes

- **Using personal email addresses instead of role addresses** — when a person leaves, a personal address becomes a dead end; security@\<project\>.io survives maintainer turnover
- **Listing only one contact** — a single contact on vacation during an active incident means the disclosure goes unacknowledged; the minimum is two
- **SECURITY_CONTACTS not cross-checked with SECURITY.md** — if SECURITY.md says "email security@project.io" but no one in SECURITY_CONTACTS monitors that address, disclosures are lost silently
