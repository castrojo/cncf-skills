---
id: governance-elections
title: "Set Up Elections-Based Governance (GOVERNANCE-elections.md)"
description: "Creates or updates elections-based GOVERNANCE.md defining how maintainers are elected, terms, and removal process. Use when a CNCF project uses an election model for leadership and needs formal governance documentation."
version: "2.0.0"
domain: governance
cncf_requirement: encouraged
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/GOVERNANCE-elections.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/governance/"
tags:
  - governance
  - elections
  - maintainers
mcp_servers:
  - id: github
    description: "Check file existence, fetch template, create or update GOVERNANCE-elections.md"
    url: "https://github.com/github/mcp-server-github"
---

Create or update `GOVERNANCE-elections.md` with the project's election process for
maintainer seats: eligibility, nomination, voting method, terms, and administration.

## When to use

Use when:
- A project wants to move from appointment-based to election-based leadership
- A project is preparing for CNCF graduation and needs formal governance docs
- The community is large enough that maintainer seats are contested

Do NOT use when:
- The project has fewer than 5 active contributors — elections require a viable electorate; use governance-maintainer-council and revisit when the community grows
- The project is at sandbox stage — elections governance is for incubating+ projects with demonstrated community scale

## Steps

1. **Fetch the template.**
   If GitHub MCP available: `github_get_contents` path=`cncf/project-template/GOVERNANCE-elections.md`
   Otherwise: `gh api repos/cncf/project-template/contents/GOVERNANCE-elections.md`

2. **Fill in Eligibility**: who can vote and who can run. Typical CNCF pattern:
   contributors with N+ merged PRs in the past 12 months.
   ⚠️ Eligibility must be project-neutral (contribution activity), not component-specific — component-specific criteria can favor a dominant employer.

3. **Fill in Nomination**: how candidates are nominated, seconding requirement, nomination period.

4. **Fill in Election**: voting method (Condorcet, approval voting, or simple majority),
   voting period, and quorum requirement.
   ⚠️ No quorum defined means 1 voter can decide an election — set a minimum threshold.

5. **Fill in Terms**: term length, whether seats are staggered, and mid-term vacancy process.
   ⚠️ The mid-term vacancy policy must exist before it is needed.

6. **Fill in Administration**: who runs the election (election officers) and what platform
   is used (CIVS, Helios, GitHub discussion, etc.).

7. **Add a vendor-neutrality cross-link** to `https://contribute.cncf.io/maintainers/community/vendor-neutrality/`.

8. **Remove all TODO markers and instruction links.**

## Checklist

- [ ] Eligibility criteria defined for voting and candidacy
- [ ] Nomination process documented with timeline
- [ ] Voting method specified with quorum requirement
- [ ] Term lengths and staggering documented
- [ ] Mid-term vacancy process defined
- [ ] Election administration responsibilities assigned
- [ ] Vendor-neutrality guide cross-linked (graduation)
- [ ] At least one election cycle conducted and noted in graduation application (graduation)
- [ ] No `TODO` markers remain
