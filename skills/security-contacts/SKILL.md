---
id: security-contacts
title: "Create or Update SECURITY_CONTACTS"
version: "2.0.0"
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
mcp_servers:
  - id: github
    description: "Check file existence, fetch template, create or update SECURITY_CONTACTS"
    url: "https://github.com/github/mcp-server-github"
---

Create or update the `SECURITY_CONTACTS` file in the repository root with the
current list of individuals responsible for handling security disclosures.

## When to use

Use when:
- A CNCF incubating or graduating project does not have a `SECURITY_CONTACTS` file
- Security contacts have changed (people left, new security leads assigned)
- CNCF staff requests an updated contact list

Do NOT use when:
- The project has a dedicated security team with a formal contact process already published — reference that process and link to it from SECURITY.md rather than duplicating it here

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/tag-security/main/project-resources/templates/SECURITY_CONTACTS`
   Otherwise: `gh api repos/cncf/tag-security/contents/project-resources/templates/SECURITY_CONTACTS`

2. **List each security contact** with:
   - Full name, GitHub handle
   - Role: `Triage`, `Patch Owner`, `Communications Lead`, or `Incident Commander`
   - Email — prefer a role address like security@\<project\>.io
   ⚠️ Personal email addresses become dead ends when a person leaves; use role addresses.

3. **Ensure at least 2 contacts are listed.**
   ⚠️ A single contact on vacation during an active incident means the disclosure goes unacknowledged.

4. **Verify each GitHub handle is current** and the person is still active on the project.

5. **Cross-reference with SECURITY.md** — contacts listed here must be recipients of
   the reporting channel documented there.
   ⚠️ If SECURITY.md says "email security@project.io" but no one monitors that address, disclosures are lost silently.

6. **Test the reporting channel.**
   Send a test message to the contact address and confirm at least one contact receives
   and acknowledges it within 24 hours. Document the test date.
   Repeat this test at least annually — reporting channels silently break when email
   aliases go unchecked after personnel changes.

7. **Set a calendar reminder to review contacts annually.**
   Security contact lists go stale faster than maintainer lists because security roles
   are often informal. Add a recurring review to the project's release calendar or
   governance meeting agenda.

## Checklist

- [ ] At least 2 security contacts listed
- [ ] Each contact has a defined role (Triage, Patch Owner, etc.) (graduation)
- [ ] All GitHub handles verified as current
- [ ] Role email addresses used, not personal addresses
- [ ] Contacts span ≥2 organizations where possible (graduation)
- [ ] Consistent with the reporting channel in SECURITY.md
- [ ] Each contact has GitHub permissions to access draft security advisories (graduation)
