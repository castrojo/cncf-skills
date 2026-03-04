---
id: vendor-neutrality
title: "Add a Vendor-Neutral Governance Statement"
version: "1.0.0"
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
---

# Add a Vendor-Neutral Governance Statement

## When to use this skill

Use when:
- The project is preparing a CNCF graduation application and the governance documentation does not yet contain an explicit vendor-neutrality statement
- Maintainer affiliation analysis shows that one company holds a majority of maintainer seats and the project wants to document the path toward broader representation
- A recent governance review (by the CNCF TOC, TAG Contributor Strategy, or a community member) has flagged that decision-making appears vendor-controlled
- The project is updating its `GOVERNANCE.md` or `GOVERNANCE-maintainer.md` and wants to add a neutrality section as part of that revision
- The project is being evaluated for incubation and wants to establish vendor-neutrality expectations early

Do NOT use when:
- The project is in early sandbox stage and is legitimately dominated by the founding company — making an explicit vendor-neutrality statement before the conditions are true is misleading; instead, document the intent and the concrete path toward neutrality (timeline, recruitment goals, mentoring plan) without claiming a state that does not yet exist
- The project has already completed a vendor-neutrality audit within the last six months and no major maintainer or governance changes have occurred since

## What this skill does

Guides a project through auditing its current vendor diversity, writing an explicit vendor-neutral governance statement, and embedding that statement in the appropriate governance document. It also covers how to identify and correct neutrality problems before they become graduation blockers. The result is a governance record that demonstrates CNCF's core principle — that the project belongs to its community, not to any single company — in clear, verifiable language.

## Steps

1. **Audit maintainer affiliation diversity.**
   Open `MAINTAINERS.md` (or the equivalent file for your project). For each listed maintainer, record their current employer affiliation. Count the number of unique organizations represented.
   - Graduation requires maintainers from at least two different companies. The TOC looks for meaningful diversity — two maintainers from Company A and one from Company B, where Company B's maintainer is inactive, is not meaningful diversity.
   - If all maintainers are from one company, stop here and move to step 6 (improving neutrality) before writing the statement.

2. **Audit commit and review distribution.**
   Run a commit graph analysis for the past 12 months:
   ```bash
   git log --since="12 months ago" --format="%ae" | sort | uniq -c | sort -rn
   ```
   Map each email domain to a company. Calculate the percentage of commits attributable to the top single company. Also check PR review history in GitHub: filter closed PRs and note which accounts approved or requested changes most frequently.
   - A project where one company accounts for more than 80% of commits over the past year will raise questions regardless of what the governance document says. The statement must reflect reality.
   - Document this analysis — graduation reviewers will ask for it.

3. **Audit tooling and contribution requirements.**
   Review the contributing guide and CI/CD setup for any requirements that would exclude contributors who do not have access to a specific vendor's resources:
   - Does testing require a proprietary cloud account?
   - Does the build pipeline require access to a private registry?
   - Are any required tools available only under a non-open-source license?
   Any such requirement must be resolved or documented with a documented alternative before the vendor-neutrality statement can honestly cover contribution openness.

4. **Choose where the statement lives.**
   The statement can live in one of three places, in order of preference:
   - **`GOVERNANCE.md` or `GOVERNANCE-maintainer.md`** — most common and most credible; reviewers expect to find it here
   - **A standalone `VENDOR-NEUTRALITY.md`** — appropriate if the governance document is already very long, or if the project wants the statement to be highly visible and easily linkable
   - **A dedicated section in `README.md`** — acceptable for small projects without a separate governance document, but provides less detail than a governance-level statement
   Whatever location is chosen, the other documents should cross-link to it.

5. **Write the vendor-neutral governance statement.**
   The statement must cover all four of the following elements. Each element should be a short paragraph or a clearly labeled section:

   a. **Decision-making process** — state explicitly that governance decisions (roadmap direction, feature acceptance, release approval, maintainer additions and removals) are made by the maintainer body as a whole, not by any single corporate backer. Name the decision-making mechanism (lazy consensus, supermajority vote, etc.) and where it is documented.

   Example language:
   > "Project decisions — including roadmap direction, feature acceptance, and changes to governance — are made by the maintainer body through [lazy consensus / supermajority vote / the process defined in GOVERNANCE.md]. No single organization, including the project's founding company, holds veto power or unilateral authority over project direction."

   b. **Maintainer diversity** — state the current number of unique organizational affiliations among maintainers, and state the project's commitment to maintaining diversity. Do not make up numbers; use the results from step 1.

   Example language:
   > "As of [date], the maintainer body includes contributors from [N] distinct organizations. The project is committed to recruiting and retaining maintainers from multiple organizations. Maintainer nominations are open to any contributor who meets the criteria in [link to criteria]."

   c. **Contribution openness** — state that contributions are welcome from any individual or organization, and that employment at or association with any particular company is neither required nor advantaged. Reference the contributing guide.

   Example language:
   > "Contributions to [project] are welcome from any individual or organization. No affiliation with any company is required to contribute. The contribution process is documented in [CONTRIBUTING.md](CONTRIBUTING.md) and applies equally to all contributors."

   d. **No vendor lock-in for contributors** — state that the development toolchain and CI environment do not require access to proprietary resources. If any vendor-specific tooling is used in CI, note what the open alternative is.

6. **If the audit in steps 1–3 reveals a neutrality problem, address it before publishing the statement.**
   A governance statement that does not reflect reality is worse than no statement — it will be contradicted immediately by the commit graph or maintainer list. Take these steps first:

   a. **Recruit maintainers from other organizations.** Identify active contributors who are not employed by the dominant company. Reach out directly and offer a maintainer nomination. Be specific about the time commitment and the decision-making responsibilities.

   b. **Establish a mentoring or contributor ladder program.** A documented path from contributor to maintainer signals that the project is actively working to diversify governance, not just claiming it. Even if the ladder is new, publishing it and announcing it to the community is a credible first step.

   c. **Define and publish emeritus criteria.** If the maintainer list contains inactive maintainers from the dominant company who are effectively blocking seats, emeritus criteria give you a principled, non-contentious way to rotate them out and create room for new maintainers from other organizations.

   d. **Set a concrete target and timeline.** Instead of a statement about current neutrality (which you cannot honestly make), publish a statement of intent: "By [date], we aim to have active maintainers from at least [N] organizations. Here is our current recruitment status." This is accepted by CNCF reviewers as evidence of good-faith effort when paired with a realistic timeline.

7. **Cross-link the statement from related documents.**
   - `README.md` — add a "Governance" section or expand an existing one with a link
   - `CONTRIBUTING.md` — add a sentence in the introduction: "This project is governed by a vendor-neutral maintainer body. See [GOVERNANCE.md](GOVERNANCE.md) for details."
   - If the project has a website, add a Governance page or update the existing one

8. **Record the audit results.**
   Create a short record (in a comment in the governance document, in a separate `GOVERNANCE-AUDIT.md`, or in a GitHub issue) documenting:
   - Date of audit
   - Maintainer affiliation breakdown at time of audit
   - Commit distribution summary (top company %, 12-month window)
   - Any tooling concerns found and their resolution
   This record is useful for future graduation applications and for demonstrating ongoing governance health.

## Validation checklist

- [ ] `MAINTAINERS.md` (or equivalent) lists each maintainer's current employer affiliation
- [ ] Maintainers are from at least 2 distinct organizations (graduation hard requirement)
- [ ] A vendor-neutral governance statement exists in `GOVERNANCE.md`, a standalone file, or `README.md`
- [ ] The statement explicitly says governance decisions are made by the maintainer body, not by a single company
- [ ] The statement explicitly says contributions are open to all regardless of employer
- [ ] The statement explicitly says no proprietary tooling is required to contribute
- [ ] Commit distribution has been analyzed for the past 12 months and the result is documented
- [ ] Cross-links from `README.md` and `CONTRIBUTING.md` to the governance statement are in place
- [ ] If a neutrality problem was found: a public statement of intent with a concrete timeline is published
- [ ] No CI or build steps require a proprietary account that community contributors cannot obtain

## Common mistakes

**Making the statement without running the audit** — writing "governance decisions are made by the full maintainer body" while one company holds 9 of 10 maintainer seats is immediately falsifiable. Reviewers will check `MAINTAINERS.md`. Run the audit first; fix what you find; then write what is true.

**Confusing "vendor-neutral process" with "vendor-neutral outcomes"** — a project can have a completely open decision-making process and still have outcomes that primarily serve one company's interests, if that company dominates the maintainer body. CNCF looks at both. The statement must address the process; the commit and maintainer audit must demonstrate that the process is real.

**Listing maintainers who are no longer active** — a maintainer who has not reviewed a PR or participated in a governance vote in 18 months is not providing governance diversity. Graduation reviewers will sometimes contact listed maintainers directly. An inactive maintainer from Company B who cannot describe the project's current roadmap undermines the diversity claim. Define and apply emeritus criteria before the graduation application.

**Treating "open source license" as sufficient for vendor neutrality** — a project can be Apache 2.0 licensed and still be entirely vendor-controlled in practice. The license is necessary but not sufficient. CNCF graduation requires demonstrated, not just theoretical, neutrality. The governance document must address actual practices, not just the legal permissions granted by the license.

**Burying the statement in a long governance document without a clear header** — graduation reviewers read dozens of governance documents. If the vendor-neutrality statement is a paragraph embedded in a ten-page document with no heading, reviewers may miss it. Use a clear heading: `## Vendor Neutrality` or `## Independence from any single vendor`.

**Failing to update the statement after maintainer changes** — a project that adds a third company's maintainer should update the statement to reflect the new number. A statement that says "maintainers from 2 organizations" after a third organization joins is a minor inaccuracy that creates unnecessary reviewer questions. Treat the governance document as a living record, not a one-time filing.

**Conflating CNCF membership with vendor neutrality** — a company being a CNCF member does not make a project vendor-neutral. Vendor neutrality is about the power structure inside the project, not about the affiliations of the companies involved.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Vendor-neutral governance** (Required)
- **Maintainer diversity across organizations** (Required)
- **Open and documented contribution process** (Required)

What graduation reviewers specifically check:

1. **Maintainer affiliation breakdown in `MAINTAINERS.md`** — reviewers will read every name and check current employer affiliations (GitHub profile, LinkedIn). They are looking for at least two active maintainers from different companies. "Active" means: has reviewed a PR, approved a release, or participated in a governance decision in the last 12 months. A list of 8 maintainers from one company and 1 inactive maintainer from another does not satisfy this requirement.

2. **Whether the governance document contains an explicit vendor-neutrality statement** — this is a line-item check in the CNCF due diligence template. If the document has no such statement, the application will be sent back with a request to add one. The statement must be findable under a clear heading; it cannot be implied.

3. **Commit and review concentration** — using the project's GitHub Insights or a manual `git log` analysis, reviewers estimate what fraction of commits and PR reviews come from a single company. There is no hard threshold, but a project where one company accounts for more than 80–90% of recent activity will face follow-up questions regardless of what the governance document says. If this is the project's situation, the application should proactively address it: acknowledge the current concentration, describe the recruitment or mentoring program in place, and provide evidence of progress (e.g., a contributor ladder that is being actively used).

4. **Decision-making mechanism is documented and company-agnostic** — reviewers look for a documented process (lazy consensus, supermajority vote, etc.) where the outcome cannot be predetermined by a single corporate actor. If the process says "the founding company's CTO has final say," that is a disqualifier. If the process has a veto or blocking mechanism controlled by one company, that is a disqualifier.

5. **Contribution process does not require vendor resources** — reviewers look at the contributing guide and CI configuration. If a contributor needs a proprietary cloud account to run tests, or if the "getting started" guide assumes access to a vendor-specific tool, that is flagged. Even if the project argues that the tool is free to use, requiring it concentrates power with the vendor who controls the tool.

6. **The statement reflects the actual governance structure, not an aspirational one** — a governance document that promises future neutrality without documenting current state is less credible than one that honestly describes current limitations and a concrete plan. If the project is genuinely at 95% single-company contribution today, the reviewers already know that from the commit graph; a statement that ignores it loses credibility. A statement that says "we are at 80% and here is our 12-month plan to reach 50%" is honest and shows maturity.

7. **No single-company controlling structures embedded in the charter or governance** — some projects carry over structures from their pre-CNCF governance that give a founding company special rights: veto over maintainer nominations, reserved board seats, exclusive control of the release signing key, or a requirement that the project lead be an employee of the founding company. Any such structure must be removed or replaced before graduation. Reviewers will ask specifically whether such clauses exist.
