# CNCF Graduation Application Template

> Annotated guidance for completing the CNCF graduation due diligence document.
> The canonical template is at:
> https://github.com/cncf/toc/blob/main/process/graduation_due_diligence.md
>
> For each section below: what reviewers look for, which project document answers it,
> and common gaps that cause applications to be sent back.

---

## 1. Project Summary

**What reviewers look for:** One paragraph confirming the project's current maturity
level, time at incubating, and a brief statement of why the project is ready to graduate.

**Source:** Write fresh for the application. Do not copy from README.md.

**Common gaps:** Applications that skip the time-in-incubation context. Reviewers want
to see the trajectory, not just the current state.

---

## 2. Governance

**Reviewer checks:**
- GOVERNANCE.md exists and is current
- Maintainer list is complete with affiliation column
- Decision-making process is documented and company-agnostic
- Vendor-neutral governance statement present under a clear heading

**Project document:** GOVERNANCE.md, MAINTAINERS.md

**Skills:** `governance-maintainer-council`, `maintainers-list`, `vendor-neutrality`

**Common gaps:** Governance document that describes process but has no vendor-neutrality
statement. Reviewers use this as a line-item check — it must exist under its own heading.

---

## 3. Contributors and Adopters

**Reviewer checks:**
- MAINTAINERS.md lists active maintainers from 2+ organizations
- ADOPTERS.md has 3+ production adopters with use-case descriptions
- Commit distribution shows no single company > ~80% of recent activity

**Project documents:** MAINTAINERS.md, ADOPTERS.md

**Skills:** `maintainers-list`, `adopters`, `vendor-neutrality`

**Common gaps:** Adopters list with only company names and no use-case context. Reviewers
want to understand how the project is being used in production.

---

## 4. Security

**Reviewer checks:**
- SECURITY.md with private disclosure instructions
- SECURITY_CONTACTS.md with current, reachable contacts
- TAG Security self-assessment issue/PR is closed (not just filed)
- OpenSSF Scorecards score ≥ 5.0 on CLOMonitor
- OpenSSF Best Practices badge at Passing level

**Project documents:** SECURITY.md, SECURITY_CONTACTS.md, TAG Security assessment

**Skills:** `security-policy`, `security-contacts`, `security-self-assessment`,
`openssf-scorecards`, `openssf-badge`

**Common gaps:** Self-assessment filed but not yet reviewed by TAG Security. Applications
submitted before the review is complete are put on hold. File at least 3 months early.

---

## 5. Release Process

**Reviewer checks:**
- RELEASES.md exists with versioning scheme and release steps
- GitHub Releases page has published releases with release notes
- Artifact signing is implemented (cosign or SLSA level 1+)
- Supported versions table consistent with SECURITY.md

**Project document:** RELEASES.md, GitHub Releases page

**Skill:** `releases`

**Common gaps:** RELEASES.md describes process but does not include artifact signing.
Unsigned artifacts are a graduation blocker.

---

## 6. Roadmap

**Reviewer checks:**
- ROADMAP.md updated within the last 6 months
- Active work items linked to GitHub issues or milestones
- Deprecations and breaking changes documented
- Process for proposing roadmap items is described and consistent with GOVERNANCE.md

**Project document:** ROADMAP.md

**Skill:** `roadmap`

**Common gaps:** Roadmap with no last-reviewed date, or a date older than 6 months.
Reviewers treat a stale roadmap the same as a missing roadmap.

---

## 7. Due Diligence Questionnaire

The TOC due diligence template includes a questionnaire covering:
- Community health metrics (contributors, commits, releases)
- Infrastructure and CI/CD
- End-user adoption evidence
- Compatibility and API stability

For each question, link directly to the project document or public URL that answers it.
Do not write prose — link to evidence.

**Tip:** Prepare answers before filing the application. Each unanswered question
becomes a reviewer comment that extends the timeline by at least one review cycle.
