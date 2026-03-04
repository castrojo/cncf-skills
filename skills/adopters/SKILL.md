---
id: adopters
title: "Create or Update an ADOPTERS.md"
version: "1.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/project-template/blob/main/ADOPTERS.md"
how_to_guide: "https://contribute.cncf.io/maintainers/community/users/"
tags:
  - community
  - adopters
  - production-use
  - graduation
---

# Create or Update an ADOPTERS.md

## When to use this skill

Use when:
- A CNCF incubating project does not yet have an `ADOPTERS.md` and is preparing for due diligence
- A project is building the graduation application and needs to demonstrate production use
- Existing `ADOPTERS.md` has fewer than 3 independent end users and the project is approaching graduation
- A maintainer wants to establish a self-reporting process so adopters can add themselves via PR

Do NOT use when:
- The project is an infrastructure component that is a dependency of other CNCF projects but is not directly adopted by end users — use the parent project's `ADOPTERS.md` instead
- The project has not yet reached a level of stability where production adoption is expected (early sandbox stage)

## What this skill does

Creates or updates the project's `ADOPTERS.md` to provide a public, curated list of organizations running the project in production. It also establishes a self-reporting process (GitHub issue template + PR workflow) so adopters can add themselves without requiring maintainer research. The result satisfies the CNCF graduation requirement of demonstrating at least three independent production end users.

## Steps

1. Fetch the canonical template:
   `https://github.com/cncf/project-template/blob/main/ADOPTERS.md`

2. Check if `ADOPTERS.md` already exists in the repository root.
   - If yes: audit existing entries for completeness and confirm each entry still reflects current production use.
   - If no: create the file using the table format below as the starting point.

3. Set up the adopters table with these columns:

   ```markdown
   | Organization | URL | Description of Use |
   |---|---|---|
   | Acme Corp | https://acme.example.com | Runs <project> in production for X workload |
   ```

   Guidelines for each column:
   - **Organization**: legal or commonly known name; avoid abbreviations
   - **URL**: the organization's public homepage (not the repo or product page)
   - **Description of Use**: one sentence describing how they use the project in production — the workload, scale hint, or use case. This column is optional but strongly encouraged; entries without it carry less weight with graduation reviewers.

4. Identify the "end user" vs "vendor" distinction and sort entries accordingly:
   - **End user**: an organization that runs the project as part of its own infrastructure or product, and does not resell or redistribute it as a core offering. Examples: a bank running the project to manage internal workloads; a retailer using it for platform engineering.
   - **Vendor**: an organization that ships the project inside a product or managed service that customers pay for. Examples: a cloud provider offering a hosted version; a company that bundles the project in a commercial platform.
   - Both categories count toward the graduation requirement, but CNCF reviewers weight independent end users more heavily. If a project's adopter list is entirely vendors, it raises questions about breadth of real-world use.
   - Consider splitting the table into two sections: `## End Users` and `## Vendors`, with a short explanatory note at the top.

5. Seed the file with known adopters before opening it to self-reporting:
   - Search GitHub issues and discussions for mentions of production deployments.
   - Search conference talk abstracts (KubeCon, maintainer track) where speakers describe using the project.
   - Check community Slack for `#<project>-users` or similar channels.
   - Ask in the maintainer meeting: "Who have we heard is running this in production?"
   - For each candidate, send a brief direct message or issue comment asking them to confirm and open a PR to add themselves.

6. Create a self-reporting process so the list grows without maintainer effort:
   a. Add a GitHub issue template at `.github/ISSUE_TEMPLATE/add-adopter.yml` (or `.md`) with these fields:
      - Organization name
      - Public URL
      - Brief description of use (optional)
      - Confirmation that use is in production (checkbox)
      - Confirmation that the submitter is authorized to represent the organization (checkbox)
   b. Add instructions at the top of `ADOPTERS.md`:
      ```markdown
      ## Add your organization
      If your organization uses <project> in production, we'd love to include you.
      Open a PR adding a row to the table below, or file an issue using the
      [Add Adopter](../../issues/new?template=add-adopter.yml) template and a maintainer
      will open the PR on your behalf.
      ```
   c. Consider adding a `ADOPTERS wanted` pinned issue with a brief call to action that can be shared at conferences and in release announcements.

7. Promote the self-reporting process in community channels:
   - Post in Slack and mailing list when the file is created.
   - Include a line in release notes: "Using `<project>` in production? Add your org to ADOPTERS.md."
   - At conferences, ask in the maintainer track session: raise hands / survey, then follow up with those who raise their hand.
   - Consider a community survey (using the CNCF survey infrastructure or a simple Google Form) that asks production users to opt in to being listed.

8. Verify each entry before the graduation application is submitted:
   - Confirm the organization URL resolves.
   - Confirm the entry still reflects current production use (not just evaluation or POC).
   - Confirm the entry was made by someone with standing to represent the organization (not just a random community member).

## Validation checklist

- [ ] `ADOPTERS.md` exists in the repository root
- [ ] File contains a table with Organization, URL, and Description of Use columns
- [ ] At least one row exists with a real organization and a working URL
- [ ] Instructions for adding new entries are present in the file
- [ ] GitHub issue template for self-reporting exists (`.github/ISSUE_TEMPLATE/add-adopter.yml` or equivalent)
- [ ] No placeholder rows or template example rows remain in the table
- [ ] All URLs in the table resolve to the correct organization homepage
- [ ] For graduation: at least 3 rows representing independent production end users (not just vendors)
- [ ] For graduation: each entry can be verified — URL works, description names a real workload, person who submitted it has standing

## Common mistakes

**Counting vendors as end users without distinction** — a vendor shipping the project inside a commercial product is not the same as an independent end user running it for their own needs. Both count, but CNCF reviewers want to see at least 3 independent end users. A list of 10 vendors and 0 end users will not satisfy the graduation requirement.

**Accepting entries from individuals, not organizations** — ADOPTERS.md tracks organizational production use. An entry that says "Jane Doe at Acme Corp" without confirmation from Acme Corp's side is not credible to reviewers. Require at minimum that the PR comes from an account with the organization's domain in their public profile, or that the person states they are authorized to represent the organization.

**Listing POC or evaluation deployments as production** — "we evaluated it last year" does not satisfy "production use." The description column should describe an active workload. If an adopter isn't sure, ask: "Is it running in a production environment serving real traffic or data?"

**No self-reporting process in place** — without a documented process, the file stays empty or requires maintainer legwork before every graduation application. The issue template + PR instructions are low effort and compound: once the process exists, the list grows organically.

**Waiting until the graduation application to build the list** — ADOPTERS.md is one of the hardest graduation requirements to satisfy quickly because it depends on external organizations taking action. Start collecting adopters at incubation. Three months before a planned graduation application is too late if you have zero entries.

**Not linking `ADOPTERS.md` from the project README** — many potential adopters will only think to add themselves if they see that the file exists. Add a one-line mention and link in the README's Community or Adopters section.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):
- **Production use by at least 3 independent end users** (Required)

What graduation reviewers specifically check:

1. **Count of independent end users, not total entries** — reviewers distinguish between end users (organizations running the project for their own needs) and vendors (organizations shipping it as part of a product). The graduation requirement is "3 independent end users." Three vendors with zero end users does not pass. If your list is mixed, make the distinction explicit in the file with separate sections.

2. **"Independent" means unaffiliated** — three subsidiaries of the same parent company count as one. Three projects in the same umbrella org where the same engineering team runs all three count as one. "Independent" means separate legal entities with no common ownership or control making the adoption decision.

3. **Verification of production status** — reviewers may reach out directly to listed adopters to confirm production use. Entries with a description naming a real workload ("processing 10M events/day for our data pipeline") are far more credible than entries with no description. The more specific the description, the less likely a reviewer will question it.

4. **Recency** — an adopter added three years ago who has since moved to a different tool does not count. Review the list before submission and remove or flag stale entries. A note like "(confirmed 2025-Q4)" in the description column signals that the list is maintained.

5. **CNCF due diligence document references** — the graduation due diligence document explicitly asks for the `ADOPTERS.md` link and asks the project to call out the end-user entries. Have a short paragraph ready that identifies which entries are end users, which are vendors, and confirms all are in production.
