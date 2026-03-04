---
id: code-of-conduct
title: "Adopt the CNCF Code of Conduct"
version: "1.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - sandbox
  - incubating
  - graduated
template_source: "https://github.com/cncf/foundation/blob/main/code-of-conduct.md"
how_to_guide: "https://contribute.cncf.io/maintainers/community/code-of-conduct/"
tags:
  - community
  - code-of-conduct
  - governance
  - cncf-required
---

# Adopt the CNCF Code of Conduct

## When to use this skill

Use when:
- The project is being submitted to CNCF as a sandbox proposal and has no Code of Conduct yet
- The project is preparing for an incubating or graduation review and CoC compliance is flagged as incomplete
- The project has an existing CoC that needs to be replaced or updated to reference the CNCF CoC
- A new repository has been added to the project and needs its own CoC file or cross-reference
- The enforcement contact is undocumented, outdated, or points to a non-CNCF address

Do NOT use when:
- The repo is a fork of an upstream project that already has a CoC — link to the upstream CoC instead of creating a duplicate; duplicates create maintenance burden and version drift
- The project already has a CoC that is compatible with CNCF's (e.g., Contributor Covenant v2.x) — review for differences and add a CNCF cross-reference rather than overwriting

## What this skill does

This skill walks a maintainer through placing a CNCF-compliant `CODE_OF_CONDUCT.md` in the repository root, linking it from `README.md` and `CONTRIBUTING.md`, and designating a documented enforcement contact. The output is a repository that satisfies the CNCF CoC adoption requirement across all project spaces, with explicit coverage language that graduation reviewers can verify.

## Steps

1. **Check for an existing CoC.** Run `ls CODE_OF_CONDUCT.md` in the repo root. If one exists, read it. If it already references `https://github.com/cncf/foundation/blob/main/code-of-conduct.md` and names an enforcement contact, skip to step 6 to verify cross-links.

2. **Create `CODE_OF_CONDUCT.md` in the repo root.** Use one of two approaches:
   - **Link approach (preferred for most projects):** The file contains a one-paragraph statement pointing to the canonical CNCF CoC. Example:
     ```markdown
     # Code of Conduct

     This project follows the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/main/code-of-conduct.md).

     ## Reporting

     To report a violation, contact the CNCF at conduct@cncf.io.
     For project-level concerns, contact [maintainer alias or email].
     ```
   - **Copy approach (for large projects with a separate CoC committee):** Copy the full text from `https://github.com/cncf/foundation/blob/main/code-of-conduct.md`. Update the enforcement section with the project-specific contact. Add a note at the top: `This is the CNCF Code of Conduct, adopted by <project>.`

3. **Choose the enforcement contact.** For most sandbox and incubating projects, use `conduct@cncf.io` — CNCF staff handle enforcement. For graduated projects with a large community (e.g., Kubernetes, Prometheus), a project-level CoC committee may be appropriate. Document the contact explicitly in `CODE_OF_CONDUCT.md`; a vague "contact a maintainer" is not acceptable.

4. **Add a CoC reference to `README.md`.** In the project's main `README.md`, add a badge or inline link in the top-level section or in a "Community" or "Contributing" section:
   ```markdown
   ## Community

   This project follows the [CNCF Code of Conduct](CODE_OF_CONDUCT.md).
   ```
   If a badge is preferred, use:
   ```markdown
   [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)
   ```

5. **Add a CoC reference to `CONTRIBUTING.md`.** In the contribution guide, add a section or inline paragraph noting that all contributors are expected to follow the CoC. Include a direct link to `CODE_OF_CONDUCT.md`:
   ```markdown
   ## Code of Conduct

   All contributors are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
   Please report any violations to conduct@cncf.io.
   ```

6. **Declare scope explicitly.** Graduation reviewers specifically check that the CoC applies to all project spaces, not just code. Add one sentence to `CODE_OF_CONDUCT.md` that names the covered spaces:
   ```
   This Code of Conduct applies to all project spaces, including the GitHub repository, issue tracker, mailing lists, Slack channels, community meetings, and any other forums where the project community gathers.
   ```

7. **Verify all links resolve.** Open `CODE_OF_CONDUCT.md`, `README.md`, and `CONTRIBUTING.md` and confirm every CoC link is a valid relative or absolute URL that loads without a 404.

8. **Check for additional repositories.** If the project spans multiple repos (e.g., `org/core`, `org/docs`, `org/website`), each repo must have its own `CODE_OF_CONDUCT.md` or a clear pointer to the canonical one. A one-liner linking back to the primary repo is sufficient:
   ```markdown
   # Code of Conduct

   This project follows the Code of Conduct of [org/core](https://github.com/org/core/blob/main/CODE_OF_CONDUCT.md).
   ```

## Validation checklist

- [ ] `CODE_OF_CONDUCT.md` exists in the repo root
- [ ] The file references the CNCF CoC at `https://github.com/cncf/foundation/blob/main/code-of-conduct.md` (either by link or full copy)
- [ ] An enforcement contact is explicitly named (`conduct@cncf.io` or a project-specific address)
- [ ] The scope of the CoC is stated — it covers all project spaces, not just the repository
- [ ] `README.md` contains a link or badge pointing to `CODE_OF_CONDUCT.md`
- [ ] `CONTRIBUTING.md` references the CoC and names the reporting contact
- [ ] All CoC links resolve (no 404s, no broken relative paths)
- [ ] If the project has multiple repos, each has its own CoC file or a canonical cross-reference
- [ ] If using the copy approach, the enforcement section is updated to reflect the actual contact for this project

## Common mistakes

**Omitting the enforcement contact** — A `CODE_OF_CONDUCT.md` that says "contact a maintainer" without naming who or how is not compliant. Graduation reviewers check for a specific, reachable contact. Always name `conduct@cncf.io` or a documented project alias with a monitored inbox.

**Declaring a CoC but not linking it from CONTRIBUTING.md** — Contributors read `CONTRIBUTING.md` first. If CoC is only in the repo root file but not cross-linked, many contributors will never encounter it. The cross-link is required.

**Scoping the CoC only to "code contributions"** — The CNCF CoC applies to all community spaces: Slack, mailing lists, meetings, social media when representing the project. If the file or README language says "code contributions" or "pull requests," broaden the scope statement.

**Using the link approach without verifying CNCF's CoC has not moved** — The canonical URL is `https://github.com/cncf/foundation/blob/main/code-of-conduct.md`. Older projects sometimes point to a stale URL on `cncf.io` that redirects incorrectly. Check that the URL loads the current document.

**Overwriting a compatible pre-existing CoC without reviewing it** — If the project already uses Contributor Covenant v2.x, the content is largely equivalent to CNCF's CoC. Adding a note that the project has adopted the CNCF CoC (and updating the enforcement section) is less disruptive than a full replacement and preserves any community-specific additions.

**Forgetting secondary repositories** — Multi-repo projects frequently pass the initial CoC check on the primary repo, then fail at graduation because documentation or website repos have no CoC reference at all. Audit every repo in the GitHub org.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):

- **Explicitly adopts the CNCF Code of Conduct** (Required)

What graduation reviewers specifically check:

1. `CODE_OF_CONDUCT.md` exists at the root of the **primary** repository and links to or reproduces the CNCF CoC text — reviewers look for the canonical URL `https://github.com/cncf/foundation/blob/main/code-of-conduct.md`
2. The file names a **specific, reachable enforcement contact** — `conduct@cncf.io` is the baseline; a project CoC committee with a documented process is acceptable for large projects, but "contact the maintainers" is not
3. The CoC **scope statement** explicitly covers all project spaces (issue tracker, Slack, mailing lists, community meetings) — reviewers flag files that only mention "this repository" or "code contributions"
4. The CoC is **cross-linked from both `README.md` and `CONTRIBUTING.md`** — reviewers check these files directly, not just the CoC file in isolation
5. If the project has **multiple GitHub repositories** (docs, website, sub-projects), each must have a CoC file or a visible pointer to the primary one — reviewers sample secondary repos
6. There is **at least one public acknowledgment** that the CoC has been communicated to the community — a changelog entry, a blog post, or a community meeting announcement satisfies this; silence does not
