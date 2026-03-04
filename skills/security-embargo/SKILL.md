---
id: security-embargo
title: "Set Up Embargo Policy and Draft Embargo Notices"
description: "Sets up an embargo policy document and draft notice templates for coordinated vulnerability disclosure. Use when a CNCF project needs pre-disclosure coordination agreements and embargo notification templates."
version: "2.0.0"
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
mcp_servers:
  - id: github
    description: "Check file existence, create or update embargo policy, open PRs"
    url: "https://github.com/github/mcp-server-github"
---

Create and maintain the security embargo policy for downstream distributors, and draft
embargo notices for coordinated security releases.

## When to use

- Project distributes software that downstream vendors bundle and ship
- A formal pre-disclosure policy for distribution partners is needed
- A security release is scheduled and distributors need advance notice before public disclosure

Do NOT use when:
- Project has no downstream distributors (library consumed only via package managers)
- The vulnerability is already public — skip embargo, go directly to `incident-response`
- No embargo policy exists yet — create the policy (Steps 1-5) before sending a notice (Steps 6-10)

## Steps

**1. Check for existing policy.**
If GitHub MCP available: `github_get_contents` path=SECURITY_EMBARGO.md
Otherwise: `gh api repos/{owner}/{repo}/contents/SECURITY_EMBARGO.md`
⚠️ If a policy exists, review it for consistency with SECURITY.md before modifying.

**2. Fetch the canonical policy template.**
See `references/policy-template.md`. ⚠️ Do not publish the policy before the private
distributor channel (mailing list or GitHub team) is created.

**3. Define the embargo period.**
Set default embargo length (45 days non-critical, 7 days critical) and criteria for
extending or shortening. Align with the coordinated disclosure timeline in SECURITY.md.

**4. Set up the distributors list.**
Document how vendors join, vetting criteria, and the private channel used.
Add at least one known downstream distributor (Linux distro, cloud vendor, etc.) before
the graduation review.

**5. Document distributor obligations and consequences.**
Require: no disclosure before embargo lifts, status updates, coordinated patch timing.
Specify the consequence for early disclosure (removal from the list).
Remove all `TODO` markers. Commit the policy file.

**6. Draft a specific embargo notice (when a release is imminent).**
Use `references/notice-template.md`. Fill in CVE ID (or "pending"), affected component,
CVSS severity. ⚠️ Write the summary as if it could leak — no PoC details or reproduction steps.

**7. Fill in patch availability.**
Specify affected versions, patch release date, and private patch branch access
(GitHub private fork or security advisory draft).

**8. Set the public disclosure date.**
Use UTC. ⚠️ Local timezone disclosures cause distributor confusion — UTC always.

**9. Send via the distributor channel and track acknowledgements.**
Note which distributors have acknowledged. Follow up with non-respondents 24h before
the disclosure date. Silence is not consent.

**10. Publish the GitHub Security Advisory when embargo lifts.**
Ensures CVE databases and security scanners index the advisory automatically.

## Reference files

- `references/policy-template.md` — embargo policy document template
- `references/notice-template.md` — per-release embargo notice template

## Checklist

- [ ] Embargo period defined with clear exception criteria
- [ ] Distributor onboarding process documented
- [ ] Distributor obligations and enforcement clause included
- [ ] Private distribution channel created before policy is published
- [ ] Policy consistent with SECURITY.md coordinated disclosure timeline
- [ ] CVE ID included in notice (or noted as pending)
- [ ] Affected versions and private patch access listed in notice
- [ ] Public disclosure date/time in UTC
- [ ] All distributors acknowledged before embargo lifts
- [ ] GitHub Security Advisory published when embargo lifts
