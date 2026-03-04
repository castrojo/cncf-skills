---
id: contributing-guide
title: "Create or Update a CONTRIBUTING.md"
version: "1.1.0"
domain: contribution
cncf_requirement: required
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/CONTRIBUTING.md"
how_to_guide: "https://contribute.cncf.io/projects/best-practices/templates/contributing"
tags:
  - onboarding
  - contributors
  - documentation
---

# Create or Update a CONTRIBUTING.md

## When to use this skill

Use when:
- A CNCF sandbox project does not yet have a `CONTRIBUTING.md` (required for sandbox+)
- An existing `CONTRIBUTING.md` still contains unfilled TODO markers or instruction links
- A maintainer wants to audit the contributing guide for completeness

Do NOT use when:
- The project uses a non-GitHub contribution platform (Gerrit, Phabricator) — the CNCF template assumes GitHub PRs; adapt manually
- The existing `CONTRIBUTING.md` is already complete and project-specific — run the validation checklist only, do not rewrite from the template

## What this skill does

Creates or updates the project's `CONTRIBUTING.md` by filling out the CNCF template
with project-specific information. The result is a contributing guide free of
placeholder text, customized for the project's communication channels, issue labels,
meeting schedule, and DCO/CLA policy.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/project-template/blob/main/CONTRIBUTING.md`

2. Check if `CONTRIBUTING.md` already exists in the repository root.
   - If yes: diff it against the template to identify missing sections.
   - If no: copy the template as the starting point.

3. Search the file for `TODO` markers. For each one, fill in the correct value:
   - `[meetings](TODO)` → replace with the project's meeting notes URL or calendar link
   - `[contact us](TODO)` → replace with the project's Slack channel or mailing list
   - `[good first issue](TODO)` → replace with the GitHub label URL:
     `https://github.com/<org>/<repo>/labels/good%20first%20issue`
   - `[help wanted](TODO)` → replace with the GitHub label URL:
     `https://github.com/<org>/<repo>/labels/help%20wanted`

4. Fill in the **Pull Request Lifecycle** section with the project's actual PR process.
   Ask the maintainer to describe: review turnaround expectations, how to signal
   WIP vs ready-for-review, and the merge policy (squash / merge commit / rebase).

5. Fill in the **Development Environment Setup** section with:
   - How to get the source code
   - How to install dependencies
   - How to build
   - How to run tests locally
   - How to preview documentation locally (if applicable)

6. Keep either the **DCO** or **CLA** section — delete the other.
   - DCO: standard CNCF pattern, keep as-is
   - CLA: replace the placeholder with the project's EasyCLA or custom CLA link

7. Create the **Pull Request Checklist** section with the project's automated checks
   (e.g., `make test`, `make lint`, required label, required reviewer).

8. Remove all instruction links (lines starting with `[Instructions](`).
   Remove all prompts and their explanatory text.

9. Verify no `TODO` markers remain: `grep -n 'TODO' CONTRIBUTING.md`

## Customization points

| Marker | What to fill in |
|---|---|
| `TODO` in meeting links | Project meeting notes URL or CNCF calendar entry |
| `TODO` in contact links | Slack `#project-name` channel or mailing list archive URL |
| `TODO` in good first issue | `https://github.com/<org>/<repo>/labels/good%20first%20issue` |
| `TODO` in help wanted | `https://github.com/<org>/<repo>/labels/help%20wanted` |
| PR Lifecycle body | Actual PR process for this project |
| Dev setup body | Actual build/test commands for this project |
| DCO or CLA choice | Keep one, delete the other |
| PR checklist | Actual CI checks and reviewer requirements |

## Validation checklist

- [ ] No `TODO` markers remain (`grep -c 'TODO' CONTRIBUTING.md` returns 0)
- [ ] No `[Instructions](` links remain
- [ ] Either DCO or CLA section present — not both
- [ ] PR Lifecycle section is filled in (not the placeholder)
- [ ] Development Environment Setup is filled in (not the placeholder)
- [ ] Pull Request Checklist is project-specific (not the placeholder)
- [ ] All URLs resolve (test a sample: meetings link, contact link, label links)

## Common mistakes

- **Both DCO and CLA sections left in** — the template includes both; you must delete one before merging
- **PR Lifecycle section left as placeholder** — this is the most commonly skipped section and the most visible gap to CNCF reviewers; it must describe the project's actual process
- **Wrong org/repo slug in label URLs** — every label URL contains the org and repo name; verify both match the actual repository
- **Not running the TODO grep before the PR** — `grep -c 'TODO' CONTRIBUTING.md` must return 0; "looked fine" is not a verification step

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Clearly defined and discoverable process to submit issues or changes** (Required)
- **Documentation of how to contribute, with increasing detail as the project matures** (Required)
- **Project must have at least one public communications channel** (Required)

What graduation reviewers specifically check beyond a filled-in template:

1. **Communications channel named explicitly** — the channel must be a real link (Slack workspace URL + channel name, or mailing list archive URL), not generic text. Reviewers paste the link to verify it is public and active.

2. **Meeting schedule linked to the CNCF calendar** — the graduation application asks for "up-to-date public meeting schedulers and/or integration with CNCF calendar." The meeting link in CONTRIBUTING.md is the natural place to satisfy this. Link to `https://www.cncf.io/calendar` or the project's specific calendar entry.

3. **Development setup section current** — reviewers clone the repo and run the setup instructions. A section that was accurate at sandbox stage but drifted since will fail this check silently. Verify the build/test commands produce the expected output immediately before submitting the graduation application.

4. **Increasing detail signal** — graduation reviewers compare the CONTRIBUTING.md against what it looked like at incubation. Projects where the file is identical signal governance stagnation. Add a changelog note or date at the top, or simply ensure new sections (PR checklist, security-aware review guidance) were added post-incubation.
