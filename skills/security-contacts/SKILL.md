---
id: security-contacts
title: "Create or Update SECURITY_CONTACTS"
version: "1.1.0"
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

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Document assignment of security response roles and how reports are handled** (Required)
- **Enforcing Access Control Rules to secure the code base against attacks** (Required — the contacts list is evidence of who is responsible for enforcing access control)

What graduation reviewers specifically check:

1. **Role assignment, not just names** — at graduation, reviewers want to see that each contact has a defined role in the response process, not just a name in a list. Add a "Role" column to SECURITY_CONTACTS: `Triage`, `Patch Owner`, `Communications Lead`, `Incident Commander`. This connects the contacts file to the incident response plan.

2. **Multi-organization coverage** — if the security contacts are all from the same employer, the response process has a single-organization bus factor. At graduation, CNCF reviewers may flag this during the due diligence review. Aim for contacts from ≥2 organizations, or document why this is not feasible (e.g., the project is genuinely single-maintainer at a security-response level, with a named backup from the CNCF TAG Security team).

3. **Access control verification** — the graduation application asks separately about "Enforcing Access Control Rules." The security contacts are the people responsible for enforcing this. Verify that each contact has the GitHub permissions needed to act: access to draft security advisories, ability to create private forks, admin access to configure branch protection. Document this in the incident response plan, not here, but confirm it is in place before the graduation review.
