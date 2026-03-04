# Embargo Policy Template

> Source: https://github.com/cncf/tag-security/blob/main/project-resources/templates/embargo-policy.md
> Fetch the latest version from the source before using — this is a local reference copy.

---

# [PROJECT NAME] Security Embargo Policy

## Embargo Period

Vulnerabilities reported to the [PROJECT NAME] security team are subject to a coordinated
disclosure embargo period before public disclosure.

- **Default embargo period:** 45 days from private notification to downstream distributors
- **Critical vulnerabilities (CVSS ≥ 9.0):** 7 days
- **Extensions:** The security team may extend the embargo period by up to 14 days with
  written agreement of affected distributors if patch complexity requires it.
- **Early disclosure:** If the vulnerability is publicly known before the embargo lifts,
  the team will accelerate disclosure with as much notice as possible.

## Distributors List

The private distributors list (`[PRIVATE-CHANNEL-URL]`) notifies downstream vendors of
upcoming security releases before public disclosure.

### Joining the List

Vendors who bundle and ship [PROJECT NAME] may request to join by emailing
`security@[project-domain]` with:

1. Organization name and description
2. How [PROJECT NAME] is distributed (OS package, container image, etc.)
3. Primary contact email for security notifications
4. Agreement to the obligations below

The security team will review and respond within 14 days.

### Distributor Obligations

By joining the list, distributors agree to:

1. **Not disclose** vulnerability details before the embargo lifts
2. **Prepare patches** in private and coordinate release timing with the [PROJECT NAME] team
3. **Acknowledge notifications** within 48 hours
4. **Notify the security team** if early disclosure becomes necessary

### Enforcement

Distributors who violate the embargo without prior agreement will be removed from the
list immediately. Re-admission requires written review by the security team.

## Coordination with CNCF

[PROJECT NAME] coordinates with CNCF TAG Security for high-severity vulnerabilities
that may affect the broader CNCF ecosystem. The CNCF security team may be notified
on a need-to-know basis.

## Policy Updates

This policy is reviewed annually. Distributors on the list are notified of material changes.
