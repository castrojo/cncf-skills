---
id: codeowners
title: "Create or Update a CODEOWNERS File"
version: "1.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners"
tags:
  - governance
  - ownership
  - code-review
  - maintainers
---

# Create or Update a CODEOWNERS File

## When to use this skill

Use when:
- The project does not yet have a CODEOWNERS file and wants automatic review requests on PRs
- MAINTAINERS.md has been updated and the ownership mappings need to stay in sync
- A new subproject or significant directory has been added and needs designated owners
- A maintainer has stepped down and their paths must be reassigned
- Preparing a CNCF graduation application that requires evidence of distributed ownership

Do NOT use when:
- The project uses Kubernetes-style OWNERS files managed by prow/tide — those use a different format and toolchain; adapt the ownership mapping concept but do not create a GitHub CODEOWNERS file on top of them
- The repository is a tiny single-file or documentation-only project with no meaningful directory structure to partition

## What this skill does

This skill guides a maintainer through creating or updating a `.github/CODEOWNERS` file that maps file path patterns to the GitHub users or teams responsible for reviewing changes to those paths. GitHub automatically requests reviews from the listed owners when a PR touches a matched path. Keeping CODEOWNERS consistent with MAINTAINERS.md is a CNCF graduation requirement that demonstrates distributed ownership and reduces bus-factor risk.

## Steps

1. **Locate any existing ownership file.** Check three canonical locations in order: `.github/CODEOWNERS`, `CODEOWNERS` (repo root), `docs/CODEOWNERS`. If one exists, open it for editing rather than creating a new file. GitHub reads them in that priority order; prefer `.github/CODEOWNERS` for new files.

2. **Inventory maintainer responsibilities.** Open `MAINTAINERS.md` (or the project's equivalent governance doc). List each maintainer's GitHub handle and the area(s) of the codebase they own. Cross-reference any subproject or component ownership tables.

3. **Create or confirm a GitHub org team per area of ownership.** Individual usernames (`@githubuser`) work but create maintenance burden on rotation. Where a GitHub org team exists (e.g., `@my-org/docs-maintainers`), use `@org/team` references instead — membership changes in the team automatically update review routing without touching the CODEOWNERS file.

4. **Define the catch-all rule first.** The first matching pattern wins, so start with the most specific patterns and put the catch-all last. Add a `*` entry that maps all unmatched paths to the full maintainer team:
   ```
   # All paths — full maintainer team
   *  @my-org/maintainers
   ```

5. **Add path-specific rules for each area.** Map directory prefixes to the responsible owner(s) or team. Be explicit about directories that represent subprojects or components with distinct maintainers:
   ```
   # Core library
   /pkg/core/  @my-org/core-maintainers

   # CLI
   /cmd/       @alice @bob

   # Docs
   /docs/      @my-org/docs-maintainers

   # CI/CD configuration
   /.github/   @my-org/maintainers
   /Makefile   @my-org/maintainers
   ```

6. **Verify no single person is sole owner of all critical paths.** Review the completed file. Every path that is critical to the project (core library, API, CI) must have at least two distinct owners or a team with at least two members. Single-owner paths are a bus-factor violation.

7. **Cross-check against MAINTAINERS.md.** Every GitHub handle or team in CODEOWNERS must correspond to an active maintainer listed in MAINTAINERS.md. Remove handles of emeritus or former maintainers. Add handles of newly onboarded maintainers where appropriate.

8. **Enable branch protection enforcement.** In the GitHub repository settings under **Branches → Branch protection rules**, enable **"Require review from Code Owners"** for the default branch (usually `main`). Without this, CODEOWNERS generates review requests but does not block merges.

9. **Validate the file.** Open a test PR that touches each major path section and confirm that GitHub automatically requests reviews from the correct owners. Check the **Files changed** tab — a shield icon next to a reviewer indicates they are a code owner for that file.

10. **Commit the file.** Commit `.github/CODEOWNERS` with a message such as `chore: add CODEOWNERS mapping maintainers to owned paths`. If updating an existing file, use `chore: sync CODEOWNERS with current MAINTAINERS.md`.

## Validation checklist

- [ ] CODEOWNERS file exists at `.github/CODEOWNERS`
- [ ] A catch-all `*` rule maps all unmatched paths to the full maintainer team
- [ ] Every critical directory (core, API, CI, docs) has an explicit rule
- [ ] No single GitHub handle is the sole owner of every rule — at least two distinct owners or teams across the file
- [ ] All GitHub handles and teams in CODEOWNERS match active entries in MAINTAINERS.md
- [ ] Subprojects with distinct maintainers have their own rules pointing to the correct owners
- [ ] `@org/team` references are used instead of individual handles wherever GitHub org teams exist
- [ ] Branch protection rule **"Require review from Code Owners"** is enabled on the default branch
- [ ] A test PR confirmed that GitHub auto-requested the correct reviewers for at least one path

## Common mistakes

**Listing only individuals instead of teams** — When a maintainer rotates off, their individual handle stays in CODEOWNERS until someone manually updates it. Use `@org/team` references so ownership tracks team membership automatically.

**Putting the catch-all `*` first** — GitHub uses the last matching rule in the file, not the first. If `*` appears first, every subsequent path-specific rule is overridden by it. Always place `*` at the end or structure the file so more-specific patterns appear after the catch-all (and understand that the last match wins).

**Not enabling branch protection enforcement** — CODEOWNERS without "Require review from Code Owners" in branch protection is advisory only. PRs can be merged without owner approval. Graduation reviewers check that the rule is enforced, not just present.

**CODEOWNERS out of sync with MAINTAINERS.md** — Listing people in CODEOWNERS who are not in MAINTAINERS.md (or vice versa) signals governance drift. Reviewers treat this as evidence that governance documentation is not maintained. Keep them in sync at every maintainer change.

**No coverage for CI and configuration paths** — Many projects define owners for source directories but forget `.github/`, `Makefile`, and build scripts. These paths control the release pipeline and must have explicit owners.

**Sole-owner paths on critical directories** — If one person owns the entire `pkg/` tree and they leave, there is no designated reviewer. Graduation reviewers flag this as a bus-factor risk. Every critical path needs at least two owners.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):

- **Code/documentation ownership matches governance documentation** (Required)
- **Demonstrated distributed ownership and reduced bus-factor** (Required)

What graduation reviewers specifically check:

1. The CODEOWNERS file exists and is located where GitHub will read it (`.github/CODEOWNERS`, repo root, or `docs/CODEOWNERS`).
2. Every handle and team in CODEOWNERS resolves to an active maintainer listed in MAINTAINERS.md — no stale or former-maintainer entries.
3. No single person is sole owner of all critical paths; at least two distinct maintainers or teams share ownership of the core codebase.
4. Subprojects and components documented in governance have their own CODEOWNERS entries, not just a blanket catch-all.
5. Branch protection on the default branch has "Require review from Code Owners" enabled — confirmed by checking repository settings or reviewing recent merged PRs for code-owner review badges.
6. The file has been updated within a reasonable time of the last maintainer change (evidence it is actively maintained, not stale).
