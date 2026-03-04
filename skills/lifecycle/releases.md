---
id: releases
title: "Document the Release Process (RELEASES.md)"
version: "1.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://contribute.cncf.io/maintainers/github/releases/"
tags:
  - releases
  - versioning
  - lifecycle
  - changelog
---

# Document the Release Process (RELEASES.md)

## When to use this skill

Use when:
- The project does not yet have a `RELEASES.md` or equivalent release process document
- The release process exists only as tribal knowledge and has never been written down
- Preparing a CNCF incubation or graduation application that requires a documented release process
- The current `RELEASES.md` lacks versioning policy, artifact signing, or supported-versions guidance
- Onboarding a new release manager who needs a step-by-step rundown of how releases work

Do NOT use when:
- The project is a specification or documentation-only project with no compiled artifacts to release — adapt the template to document the specification publication process instead (e.g., how drafts become ratified specs)

## What this skill does

Guides a maintainer through writing a `RELEASES.md` that documents the project's versioning scheme, release cadence, branch support policy, end-to-end release steps, artifact signing, and publication locations. The result gives contributors, operators, and CNCF reviewers a single authoritative reference for how new versions of the project are created and verified. It also ties the release process to the project's `SECURITY.md` (supported versions) and `MAINTAINERS.md` (release authority).

## Steps

1. **Choose a versioning scheme and document it.** State whether the project follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`) or [Calendar Versioning](https://calver.org/) (e.g., `YYYY.MM.MICRO`). Define concretely what triggers each component: breaking API change → MAJOR bump; new backwards-compatible feature → MINOR bump; bug or security fix → PATCH bump. If pre-release labels (`alpha`, `beta`, `rc`) are used, define their meaning and promotion criteria.

2. **Document the release cadence.** State whether releases follow a time-based schedule (e.g., minor release every 12 weeks) or a feature-based schedule (release when a milestone is complete). Include guidance on unscheduled patch/security releases. If there is no formal cadence, say so explicitly — "releases are made as needed" is acceptable as long as it is stated.

3. **Define the supported versions and backport policy.** List which branches or release lines receive bug fixes and security backports. This table must be consistent with the `Supported Versions` table in `SECURITY.md`. Example: "The two most recent minor releases receive security fixes; older releases are unsupported."

4. **List who has release authority.** State which role (e.g., maintainer, release manager) is authorized to create and publish releases. Link to `MAINTAINERS.md` for the current list. If a separate release team exists, name it and link to its charter or governance document.

5. **Document the end-to-end release steps.** Write a numbered checklist that a release manager can follow verbatim. At minimum, cover:
   - Branch cut (if applicable): create the release branch from `main` or the appropriate source branch
   - Changelog: generate or write release notes; call out breaking changes prominently
   - Version bump: update version strings in code, manifests, and documentation
   - Tag: create and push a signed Git tag (`git tag -s vX.Y.Z`)
   - Build: trigger the CI release pipeline or run the build locally
   - Sign artifacts: sign binaries, container images, and SBOMs using [sigstore/cosign](https://docs.sigstore.dev/) or generate [SLSA provenance](https://slsa.dev/) attestations
   - Publish: upload artifacts to GitHub Releases; push container images to the registry; publish packages to any language-specific registries (npm, PyPI, Helm chart repo, etc.)
   - Announce: post release notes to the project's mailing list, Slack channel, and any other community channels

6. **Document where releases are published.** List every artifact location: GitHub Releases page URL, container registry (e.g., `ghcr.io/org/project`), Helm chart repository, language package registry. Include the exact command or URL a user needs to pull the artifact.

7. **Document how users verify artifact integrity.** Explain how to verify checksums (`sha256sum`), verify cosign signatures (`cosign verify`), or verify SLSA provenance. Provide copy-pasteable example commands. Link to the project's public signing key or Sigstore transparency log entry if applicable.

8. **Cross-link related files.** Add links from `RELEASES.md` to `SECURITY.md` (supported versions), `MAINTAINERS.md` (release authority), `CONTRIBUTING.md` (development branch policy), and the CI release workflow file.

9. **Validate consistency.** Confirm that the supported versions in `RELEASES.md` exactly match `SECURITY.md`. Confirm that the release authority roles in `RELEASES.md` match the roles defined in governance documents.

10. **Commit and announce.** Commit `RELEASES.md` to the repository root. Add a link to it from `README.md` and `CONTRIBUTING.md` so contributors and users can discover it.

## Validation checklist

- [ ] `RELEASES.md` exists in the repository root
- [ ] Versioning scheme is explicitly named (semver, calver, or other) with definitions for each component
- [ ] Release cadence is stated (time-based, feature-based, or ad hoc)
- [ ] Supported versions and backport policy are defined and consistent with `SECURITY.md`
- [ ] Release authority is identified and links to `MAINTAINERS.md`
- [ ] End-to-end release steps are written as a numbered checklist a release manager can follow
- [ ] Artifact signing is documented (cosign, SLSA provenance, or GPG) with verification instructions
- [ ] All publication locations are listed with explicit URLs or pull commands
- [ ] Breaking changes policy is stated (how they are communicated in release notes)
- [ ] `README.md` links to `RELEASES.md`

## Common mistakes

**Listing only the Git tag workflow, not the full release pipeline** — Tagging is one step. Reviewers and operators need to know what happens after the tag: which CI pipeline runs, which registries receive artifacts, and how signing is done. Document the full pipeline.

**Inconsistent supported versions between RELEASES.md and SECURITY.md** — If `RELEASES.md` says "last two minor releases are supported" but `SECURITY.md` says "last three", operators get contradictory guidance. Keep these tables in sync; consider defining the policy in one file and referencing it from the other.

**Omitting artifact signing** — Unsigned artifacts are a graduation blocker. CNCF reviewers check for sigstore/cosign signing or SLSA provenance on binaries and container images. Documenting that signing is planned but not yet implemented is acceptable only at incubation; it must be complete at graduation.

**Release steps written as prose instead of a numbered checklist** — A paragraph describing the release process cannot be executed reliably. Write steps as a numbered list so a release manager can check off each one without missing anything.

**Not linking to the CI release workflow** — The `RELEASES.md` document describes the process; the CI workflow file is where it is automated. Link directly to the workflow file (e.g., `.github/workflows/release.yml`) so maintainers can find the automation quickly.

**Treating "release" and "deployment" as synonymous** — `RELEASES.md` covers how software versions are created and published, not how they are deployed to production environments. Keep deployment runbooks separate.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):

- **Documented release process** (Required) — A written, publicly accessible `RELEASES.md` describing versioning, cadence, steps, and artifact locations must exist before graduation reviewers will approve the application.

What graduation reviewers specifically check:

1. **Releases are published on GitHub Releases** — Source tags alone are insufficient. Reviewers look for a GitHub Releases page with release notes attached to each tag. Pre-built binary artifacts or container image references should be attached to or linked from the release.

2. **Breaking changes are called out in release notes** — The `RELEASES.md` must state that breaking changes are documented in release notes and changelog entries. Reviewers will spot-check recent releases for this.

3. **Artifact signing is implemented** — CNCF now expects either [sigstore/cosign](https://docs.sigstore.dev/) signatures on container images and binaries, or [SLSA provenance](https://slsa.dev/) attestations (level 1 minimum; level 2+ preferred). The document must include the verification commands.

4. **Supported versions are explicitly defined** — Reviewers check that end users can determine which release lines receive security fixes. The supported versions table must be present and consistent with `SECURITY.md`.

5. **Release authority is tied to governance** — Reviewers verify that only authorized maintainers can publish releases. The `RELEASES.md` must identify the role and link to `MAINTAINERS.md` or the governance document that defines it.

6. **Cadence is reasonable and observed** — There is no mandated cadence, but reviewers look for evidence that releases actually happen on the stated schedule. A cadence described in `RELEASES.md` that does not match the actual release history is a red flag.
