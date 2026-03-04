---
id: governance-elections
title: "Set Up Elections-Based Governance (GOVERNANCE-elections.md)"
version: "1.1.0"
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
---

# Set Up Elections-Based Governance (GOVERNANCE-elections.md)

## When to use this skill

Use when:
- A project wants to move from appointment-based to election-based leadership
- A project is preparing for CNCF graduation and needs formal governance docs
- The community is large enough that maintainer seats are contested

Do NOT use when:
- The project has fewer than 5 active contributors — elections require a viable electorate; use the maintainer-council model and revisit when the community grows
- The project is at sandbox stage — elections governance is for incubating+ projects with demonstrated community scale

## What this skill does

Creates or updates `GOVERNANCE-elections.md` with the project's election process for
maintainer seats, including eligibility, nomination, voting method, and term lengths.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/project-template/blob/main/GOVERNANCE-elections.md`

2. Fill in the **Eligibility** section: who can vote and who can run for a seat.
   Typical CNCF pattern: contributors with N+ merged PRs in the past 12 months.

3. Fill in the **Nomination** section: how candidates are nominated (self-nomination,
   seconding requirement, nomination period length).

4. Fill in the **Election** section: voting method (Condorcet, approval voting, or
   simple majority), voting period, and quorum requirement.

5. Fill in the **Terms** section: term length, whether seats are staggered, and
   what happens when a seat is vacated mid-term.

6. Fill in the **Administration** section: who runs the election (election officers),
   what platform is used (CIVS, Helios, GitHub discussion vote, etc.).

7. Remove all `TODO` markers and instruction links.

## Validation checklist

- [ ] Eligibility criteria defined (voting and candidacy)
- [ ] Nomination process documented with timeline
- [ ] Voting method specified
- [ ] Term lengths and staggering documented
- [ ] Election administration responsibilities assigned
- [ ] No `TODO` markers remain

## Common mistakes

- **No quorum defined** — an election where 1 person votes is not legitimate; set a minimum participation threshold before the election starts
- **Eligibility set too broadly or too narrowly** — all GitHub users who starred the repo is too broad; existing maintainers only is too narrow; the CNCF pattern is contributors with merged PRs in the past 12 months
- **Mid-term vacancy left unaddressed** — maintainers change jobs and lose interest; the policy for filling a vacated seat mid-term must exist before it is needed

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Governance clearly documents vendor-neutrality of project direction** (Required)
- **Document how the project makes decisions on leadership roles, contribution acceptance, requests to the CNCF, and changes to governance or project goals** (Required)
- **Governance has continuously been iterated upon by the project as a result of their experience** (Suggested — strong positive signal)

What graduation reviewers specifically check:

1. **Vendor-neutrality in election eligibility** — if eligibility criteria (voting rights, candidacy) can be structured to favor contributors from a dominant employer (e.g., requiring N merged PRs in a component where only one company contributes), reviewers will flag it. Eligibility must be based on project-neutral criteria: total contribution activity, time in project, mentorship provided — not component-specific activity.

2. **Evidence of governance evolution** — the graduation application specifically asks whether "governance has continuously been iterated upon." Link the git history of the governance document and highlight changes made after incubation. A GOVERNANCE-elections.md that has not been touched since sandbox acceptance signals stagnation to reviewers.

3. **Election actually conducted** — an elections governance document that has never been exercised is weaker evidence than one that has. If the project has held at least one election cycle, note the date and outcome in the graduation application. If no election has occurred because no seats were contested, document that explicitly — it is acceptable but must be stated.

4. **Cross-link vendor-neutrality policy** — the CNCF vendor-neutrality guide is at `https://contribute.cncf.io/maintainers/community/vendor-neutrality/`. Reference it explicitly in the governance document; reviewers verify this cross-link exists.
