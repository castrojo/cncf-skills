# Embargo Notice Template

> Use this template when sending a pre-disclosure notice to the distributors list.
> Source: https://github.com/cncf/tag-security/blob/main/project-resources/templates/embargo.md

---

Subject: [EMBARGO] [PROJECT NAME] Security Release — Public Disclosure [DATE] UTC

---

This message is sent to the [PROJECT NAME] security distributors list. It is under embargo
until the public disclosure date below. Do not forward or discuss publicly.

## Vulnerability Summary

- **CVE ID:** [CVE-XXXX-XXXXX or "pending assignment"]
- **Affected component:** [component name]
- **Severity:** [Critical / High / Medium] (CVSS [score])
- **Summary:** [One paragraph. Describe impact and component only. No PoC, no reproduction
  steps, no exploitable detail. Write as if this message could be leaked.]

## Affected Versions

| Version | Affected? |
|---------|-----------|
| [X.Y.Z] | Yes       |
| [X.Y.Z] | No (patched) |

## Patch Availability

- **Patched version release date:** [DATE TIME UTC]
- **Private patch access:** [GitHub private fork URL or security advisory draft URL]
  (access requires prior arrangement with the security team)
- **Patch notes:** [Brief description of the fix — no exploitable detail]

## Public Disclosure Date

**[DATE TIME UTC]**

At this date and time, the GitHub Security Advisory will be published and the CVE
will be updated. Distributors should coordinate their release timing accordingly.

## Actions Required

1. Acknowledge receipt by replying to this message within 48 hours
2. Prepare your patched distribution in private
3. Do not release before the public disclosure date above
4. Coordinate with `security@[project-domain]` if you need early access to the patch

## Contact

Security team: `security@[project-domain]`
PGP key: [URL to public key if applicable]
