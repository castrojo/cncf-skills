---
id: roadmap
title: "Create or Update a Public ROADMAP.md"
version: "1.0.0"
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
---

# Create or Update a Public ROADMAP.md

## When to use this skill

Use when:
- The project is preparing for a CNCF incubating or graduation due diligence and has no public roadmap document
- An existing `ROADMAP.md` has not been updated in more than six months or does not reflect the current development direction
- The community has asked where the project is headed and there is no canonical place to point them
- A major version or breaking-change release is being planned and the direction needs to be communicated publicly
- The project is migrating its roadmap from an informal location (e.g., a Google Doc or a single GitHub issue) to a discoverable, versioned file in the repository

Do NOT use when:
- The project version is 0.x and the public API is still unstable — a roadmap at this stage creates false expectations about commitments; link to the current GitHub milestone in `README.md` instead and revisit when the API stabilizes
- The roadmap is already actively maintained in a GitHub Project board with triage and status columns — do not duplicate content; instead, create a minimal `ROADMAP.md` that links to the board and describes the process for proposing and accepting items

## What this skill does

This skill walks a maintainer through creating or updating a `ROADMAP.md` that gives the community a clear, honest picture of where the project is headed without creating contractual obligations. It covers the content structure (themes, active work, backlog, deprecations), the governance process for accepting and revising roadmap items, and how the roadmap connects to GitHub milestones and issues. The output is a file that satisfies the CNCF graduation requirement for demonstrating a clear, publicly communicated project direction.

## Steps

1. **Confirm the roadmap entry point.** A `ROADMAP.md` in the repository root is the canonical discovery mechanism regardless of where the actual planning lives. If your project uses a GitHub Project board or an external planning tool, `ROADMAP.md` still needs to exist — it describes the process and links outward. Start by checking: `ls ROADMAP.md`. If it exists, read it and identify gaps before editing.

2. **Add a scope and disclaimer section at the top.** Open with one short paragraph that sets expectations. A roadmap is a direction, not a contract. Example:
   ```markdown
   # Roadmap

   This document describes the current project direction and planned work. Items listed here
   represent the maintainers' current intent, not a binding commitment. Priorities can shift
   based on community needs, contributor availability, and upstream changes.

   For the authoritative status of any item, see the linked GitHub milestone or issue.
   ```

3. **Organize roadmap content into four sections:**

   - **Active development** — Features and changes currently being worked on. Each item should link to the tracking GitHub issue or PR. Example format:
     ```markdown
     ## Active development

     - **[Feature name](https://github.com/org/repo/issues/NNN)** — one-sentence description of what it does and why. Target: v1.4
     ```

   - **Planned (next 1–2 releases)** — Accepted items that have not yet started but are committed for the next one or two releases. These must have a linked issue or milestone. Do not list items without a tracking issue — untracked items are aspirations, not plans.

   - **Backlog / Under consideration** — Items the project wants to do eventually but has not scheduled. Mark these clearly as unscheduled to avoid confusion:
     ```markdown
     ## Backlog / Under consideration

     These items are not scheduled. They may be picked up if a contributor volunteers or
     if community demand increases. Open a GitHub Discussion to signal interest.
     ```

   - **Deprecations and breaking changes** — Any feature currently deprecated or scheduled for removal. Include the deprecation timeline, migration path, and links to the relevant issues or documentation.

4. **State the change process.** Add a section that explains how items get added to the roadmap and how priorities change. This is the governance hook that graduation reviewers look for. Example:
   ```markdown
   ## Proposing roadmap items

   To propose a new roadmap item:
   1. Open a GitHub issue using the [roadmap proposal template](.github/ISSUE_TEMPLATE/roadmap.md).
   2. The issue will be discussed at the next maintainer meeting or async in the issue thread.
   3. Acceptance requires approval from [N] maintainers (see GOVERNANCE.md).
   4. Accepted items are added to the relevant GitHub milestone and listed here.

   The roadmap is reviewed at the start of each release cycle. Maintainers may remove,
   defer, or reprioritize items at any time; changes are noted in the commit history.
   ```
   Adjust the approval threshold and process to match your `GOVERNANCE.md` — the two documents must be consistent.

5. **Link the roadmap to GitHub milestones.** Every item in "Active development" and "Planned" must have a corresponding GitHub milestone or issue. If no milestone exists for the next release, create one now: `https://github.com/org/repo/milestones`. The roadmap is the narrative; the milestone is the operational tracker. Both must exist.

6. **Cross-link from `README.md`.** In the project's main `README.md`, add a roadmap link in the "Contributing" or "Community" section:
   ```markdown
   ## Roadmap

   See [ROADMAP.md](ROADMAP.md) for the current project direction and how to propose new features.
   ```

7. **Cross-link from `CONTRIBUTING.md`.** Contributors planning a significant feature need to know the roadmap process before they start coding. Add a note in `CONTRIBUTING.md`:
   ```markdown
   Before opening a large pull request for a new feature, check [ROADMAP.md](ROADMAP.md)
   to see if it aligns with current project direction, and open a roadmap proposal issue first.
   ```

8. **Set a review cadence.** Add a one-liner at the top of `ROADMAP.md` stating how often it is reviewed and who is responsible:
   ```markdown
   *This roadmap is reviewed and updated at the start of each release cycle by the maintainers.
   Last reviewed: YYYY-MM-DD.*
   ```
   Update this date with every significant change. Graduation reviewers check whether the roadmap is current — a file last updated two years ago fails the review even if the content was once accurate.

## Validation checklist

- [ ] `ROADMAP.md` exists in the repository root
- [ ] The file opens with a scope/disclaimer statement clarifying that the roadmap is a direction, not a commitment
- [ ] Active development items are listed with links to GitHub issues or PRs
- [ ] Planned items for the next 1–2 releases are listed with GitHub milestones or issue links
- [ ] A backlog or "under consideration" section is clearly marked as unscheduled
- [ ] Deprecations and breaking changes are called out with timelines and migration paths
- [ ] A "proposing roadmap items" section exists and is consistent with `GOVERNANCE.md`
- [ ] All listed items have corresponding GitHub issues or milestone entries
- [ ] `README.md` links to `ROADMAP.md`
- [ ] `CONTRIBUTING.md` references the roadmap process for large feature contributions
- [ ] A last-reviewed date is present and is within the last six months
- [ ] If an external planning tool (GitHub Project board, etc.) is used, `ROADMAP.md` links to it and describes the process

## Common mistakes

**Listing items with no tracking issues** — A roadmap item with no linked issue is an aspiration, not a plan. Graduation reviewers sample roadmap items to verify they have corresponding GitHub issues or milestones. Any item without a link is evidence that the roadmap is aspirational rather than operational.

**Conflating roadmap with a release checklist** — A roadmap describes direction over one to two releases; a release checklist describes tasks for a single release. If every item has a checkmark and is tied to one version, it's a release plan, not a roadmap. Include a backlog section with unscheduled longer-horizon items to demonstrate strategic thinking.

**Presenting the roadmap as a commitment** — Roadmaps that say "we will ship X in v2.0" create community expectations that become public relations problems when priorities shift. Use language like "planned for," "target," or "intended for" rather than "will be released in."

**Not updating the last-reviewed date** — A stale date is an immediate red flag for graduation reviewers. Establish a recurring calendar event or a release checklist item to update the roadmap at the start of every cycle. A `ROADMAP.md` that has not changed in over six months signals that it is not actually driving project planning.

**Roadmap inconsistent with GOVERNANCE.md** — If the governance document says "two maintainer approvals required for new features" but the roadmap proposal process says "one maintainer can accept," reviewers will flag the contradiction. These two documents must describe the same process.

**Duplicating content from a GitHub Project board** — If you maintain a GitHub Project board, putting the same item list in `ROADMAP.md` creates a synchronization burden and the two sources will inevitably diverge. Use `ROADMAP.md` as the narrative and process document; point readers to the board for current item status.

**No mention of breaking changes or deprecations** — Graduation reviewers look for evidence that the project manages breaking changes responsibly. If there are active deprecations or upcoming breaking changes and they are not in the roadmap, that is a governance gap. Always include a deprecations section, even if it says "No active deprecations as of YYYY-MM-DD."

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):

- **Clear project roadmap and community understands where the project is going** (Required)

What graduation reviewers specifically check:

1. `ROADMAP.md` exists in the primary repository root and is linked from `README.md` — reviewers look for both the file and the cross-link; a roadmap buried in a wiki or docs site without a root-level pointer does not satisfy the requirement
2. The roadmap contains items for the **current or next release cycle** with linked GitHub issues or milestones — an empty roadmap or one with only completed items does not demonstrate active planning
3. A **last-reviewed or last-updated date** is present and is recent (within the last six months) — a stale roadmap is treated as absent for graduation purposes
4. The roadmap includes a **process for proposing and accepting items** and that process is consistent with the project's `GOVERNANCE.md` — reviewers cross-check the two documents
5. **Deprecations and breaking changes** are documented with timelines — this demonstrates that the project communicates change responsibly to its adopters
6. The roadmap **distinguishes between committed work and aspirational items** — reviewers look for explicit language (e.g., "under consideration," "backlog," "not yet scheduled") to confirm the project is not overpromising to the community
