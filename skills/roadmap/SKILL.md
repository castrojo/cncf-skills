---
id: roadmap
title: "Create or Update a Public ROADMAP.md"
description: "Creates or updates ROADMAP.md publishing the project's planned direction, milestones, and timeline. Use when a CNCF project needs a public roadmap required for sandbox and above, or when the existing roadmap is stale."
version: "2.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://contribute.cncf.io/maintainers/community/roadmap/"
tags:
  - roadmap
  - planning
  - transparency
  - governance
mcp_servers:
  - id: github
    description: "Check file existence, create files, open PRs"
    url: "https://github.com/github/mcp-server-github"
  - id: cncf-landscape
    description: "Verify project maturity level and landscape metadata"
    url: "https://github.com/cncf/landscape-mcp"
---

Create or update `ROADMAP.md` to give the community a clear picture of where the project
is headed — active work, near-term plans, backlog, and deprecations — along with the
governance process for proposing and accepting roadmap items.

## When to use

- Project has no public roadmap document and is preparing for incubation or graduation due diligence
- Existing `ROADMAP.md` has not been updated in more than six months
- Community has asked where the project is headed and there is no canonical answer
- A major or breaking-change release is being planned
- Migrating roadmap from an informal location (Google Doc, single issue) to the repository

Do NOT use when:
- Project is at 0.x with an unstable API — a roadmap creates false commitment expectations;
  link to the current GitHub milestone from `README.md` and revisit when the API stabilizes
- Roadmap is already actively maintained in a GitHub Project board — create a minimal
  `ROADMAP.md` that links to the board and describes the process; do not duplicate content

## Steps

1. **Check for an existing file.**
   If GitHub MCP available: `github_get_contents` path=ROADMAP.md
   Otherwise: `gh api repos/{owner}/{repo}/contents/ROADMAP.md`
   If it exists, read it and note gaps before editing.

2. **Add a scope and disclaimer at the top.**
   A roadmap is a direction, not a contract. State that items represent current intent,
   not binding commitments, and that priorities can shift. Direct readers to linked
   GitHub milestones or issues for authoritative status.

3. **Structure the body into four sections.**
   - **Active development** — items currently being worked on; each must link to a GitHub issue or PR and state a target version.
   - **Planned (next 1–2 releases)** — accepted, not-yet-started items with a linked issue or milestone. ⚠️ Do not list items without a tracking issue — untracked items are aspirations, not plans.
   - **Backlog / Under consideration** — unscheduled items; mark clearly as such to avoid confusion.
   - **Deprecations and breaking changes** — any feature deprecated or scheduled for removal, with timeline, migration path, and issue links.

4. **Document the change process.**
   Add a "Proposing roadmap items" section explaining how items are added and reprioritized.
   State how many maintainer approvals are required. This process must be consistent with
   `GOVERNANCE.md` — graduation reviewers cross-check the two documents.

5. **Verify every active and planned item has a GitHub milestone or issue.**
   If no milestone exists for the next release, create one at
   `https://github.com/{org}/{repo}/milestones`.

6. **Add a last-reviewed date.**
   Add a line at the top: `*Last reviewed: YYYY-MM-DD by the maintainers.*`
   Update this date with every significant change.
   ⚠️ A file not updated in over six months fails graduation review even if the content was once accurate.

7. **Cross-link from `README.md` and `CONTRIBUTING.md`.**
   Add a roadmap link in the Contributing or Community section of `README.md`.
   In `CONTRIBUTING.md`, note that large feature PRs should check `ROADMAP.md` first.

## Checklist

- [ ] `ROADMAP.md` exists in the repository root
- [ ] Opens with a scope/disclaimer clarifying it is direction, not a commitment
- [ ] Active development items listed with GitHub issue/PR links and target versions (graduation)
- [ ] Planned items listed with GitHub milestone or issue links (graduation)
- [ ] Backlog section clearly marked as unscheduled
- [ ] Deprecations and breaking changes documented with timelines and migration paths (graduation)
- [ ] "Proposing roadmap items" section exists and is consistent with `GOVERNANCE.md` (graduation)
- [ ] Last-reviewed date present and within the last six months (graduation)
- [ ] `README.md` links to `ROADMAP.md` (graduation)
- [ ] `CONTRIBUTING.md` references the roadmap process for large contributions
