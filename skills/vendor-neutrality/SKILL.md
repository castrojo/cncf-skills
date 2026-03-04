---
id: vendor-neutrality
title: "Add a Vendor-Neutral Governance Statement"
version: "2.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://contribute.cncf.io/projects/best-practices/governance/"
how_to_guide: "https://contribute.cncf.io/maintainers/community/vendor-neutrality/"
tags:
  - governance
  - vendor-neutrality
  - graduation
  - cncf-required
mcp_servers:
  - id: github
    description: "Check file existence, create files, open PRs"
    url: "https://github.com/github/mcp-server-github"
  - id: cncf-landscape
    description: "Verify project maturity level and landscape metadata"
    url: "https://github.com/cncf/landscape-mcp"
---

Audit the project's vendor diversity and add an explicit vendor-neutral governance
statement to `GOVERNANCE.md` (or equivalent) demonstrating that the project belongs
to its community, not to any single company.

## When to use

- Preparing a graduation application and governance docs lack an explicit vendor-neutrality statement
- Maintainer affiliation analysis shows one company holds a majority of maintainer seats
- A governance review has flagged that decision-making appears vendor-controlled
- Updating `GOVERNANCE.md` and want to add a neutrality section as part of that revision

Do NOT use when:
- Project is in early sandbox stage and is legitimately founding-company-dominated —
  document intent and a concrete path toward neutrality; do not claim a state that does not yet exist
- Project completed a vendor-neutrality audit within the last six months with no major
  maintainer or governance changes since

## Steps

1. **Audit maintainer affiliation diversity.**
   If GitHub MCP available: `github_get_contents` path=MAINTAINERS.md
   Otherwise: `gh api repos/{owner}/{repo}/contents/MAINTAINERS.md`
   For each maintainer, record their current employer. Count unique organizations.
   ⚠️ Graduation requires maintainers from at least two companies. "Active" means:
   reviewed a PR, approved a release, or participated in a governance vote in the last
   12 months. An inactive maintainer from Company B does not count as diversity.

2. **Audit commit and review distribution.**
   ```bash
   git log --since="12 months ago" --format="%ae" | sort | uniq -c | sort -rn
   ```
   Map email domains to companies. Also review PR approval history on GitHub.
   ⚠️ A project where one company accounts for more than 80% of commits over 12 months
   will face follow-up questions regardless of what the governance document says.
   Document this analysis — graduation reviewers will ask for it.

3. **Audit contribution tooling.**
   Review `CONTRIBUTING.md` and CI configuration for requirements that would exclude
   contributors without access to a specific vendor's resources (proprietary cloud
   account, private registry, non-open-source tooling).
   Any such requirement must be resolved or documented with an open alternative.

4. **If the audit reveals a neutrality problem, address it before writing the statement.**
   A statement that does not reflect reality is worse than no statement.
   Actions: recruit maintainers from other organizations; publish a contributor ladder;
   define and apply emeritus criteria; set a concrete target and timeline.
   A statement of intent with a realistic timeline is accepted by CNCF reviewers as
   good-faith effort.

5. **Write the vendor-neutral governance statement.**
   Add a `## Vendor Neutrality` section (clear heading — reviewers read dozens of
   governance docs and must be able to find it). Cover all four elements:
   - **Decision-making**: governance decisions are made by the maintainer body as a whole, not by any single corporate backer; name the mechanism and where it is documented
   - **Maintainer diversity**: current number of unique organizational affiliations; commitment to maintaining diversity; nomination criteria
   - **Contribution openness**: contributions welcome from any individual or organization; no affiliation required; reference `CONTRIBUTING.md`
   - **No tooling lock-in**: development and CI do not require proprietary resources

6. **Cross-link the statement.**
   Add a Governance section or link in `README.md`. Add a sentence in `CONTRIBUTING.md`
   introduction referencing the vendor-neutral governance.

7. **Record the audit results.**
   Document in a comment in the governance file or a GitHub issue: date of audit,
   maintainer affiliation breakdown, commit distribution summary, any tooling concerns
   and their resolution. Useful for future graduation applications.

## Checklist

- [ ] `MAINTAINERS.md` lists each maintainer's current employer affiliation
- [ ] Maintainers are from at least 2 distinct organizations (graduation)
- [ ] Vendor-neutral governance statement exists under a clear `## Vendor Neutrality` heading (graduation)
- [ ] Statement says governance decisions are made by the maintainer body, not a single company (graduation)
- [ ] Statement says contributions are open to all regardless of employer (graduation)
- [ ] Statement says no proprietary tooling is required to contribute (graduation)
- [ ] Commit distribution analyzed for past 12 months and result documented (graduation)
- [ ] No CI or build steps require a proprietary account community contributors cannot obtain (graduation)
- [ ] Cross-links from `README.md` and `CONTRIBUTING.md` to the governance statement in place
- [ ] If neutrality problem found: public statement of intent with concrete timeline published (graduation)
