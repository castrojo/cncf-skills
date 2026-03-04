---
id: openssf-badge
title: "Earn the OpenSSF Best Practices Badge"
version: "1.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://bestpractices.coreinfrastructure.org/en"
how_to_guide: "https://bestpractices.coreinfrastructure.org/en/criteria/0"
tags:
  - security
  - openssf
  - badge
  - graduation
  - cncf-required
---

# Earn the OpenSSF Best Practices Badge

## When to use this skill

Use when:
- The project is preparing a CNCF graduation application
- The project has not yet earned a Passing-level OpenSSF Best Practices badge
- The project's existing badge has lapsed or its percentage has dropped below 100%
- A TOC reviewer has flagged the badge as missing or incomplete

Do NOT use when:
- The project already holds a current Passing badge at 100% — just verify it is still active and linked in README.md
- The repo is a documentation-only sub-repo or fork — link to the parent project's badge instead of creating a new entry

## What this skill does

This skill walks a maintainer through creating a badge entry at bestpractices.coreinfrastructure.org, answering all ~60 Passing-level criteria, resolving the highest-friction items that most CNCF projects struggle with, and embedding the badge in README.md. The Passing badge is a hard gate for CNCF graduation — a project cannot graduate without it, regardless of technical maturity or community size.

## Steps

1. **Create an account and start the badge entry.**
   Go to https://bestpractices.coreinfrastructure.org, sign in with GitHub, and click "Get Your Badge Now". Enter the project's repository URL. The questionnaire opens immediately; your progress is saved automatically after each answer.

2. **Work through all criteria sections in order.**
   The questionnaire is organized into sections: Basics, Change Control, Reporting, Quality, Security, Analysis. Answer every criterion — do not skip. For each item, choose Met, Unmet, N/A, or ? (unknown). Unknown counts against your percentage; N/A does not. Provide URLs as evidence wherever the form accepts them.

3. **Resolve the SECURITY.md criterion first (Reporting section).**
   Criterion `report_process` requires a documented vulnerability disclosure process. Create `SECURITY.md` in the repo root with: how to report a vulnerability privately, expected response time, and a note that public GitHub issues must not be used for security reports. The `security-policy` skill covers the full template if needed.

4. **Resolve the automated test suite criterion (Quality section).**
   Criterion `test` requires an automated test suite. Criterion `test_invocation` requires it to run via a standard command. Criterion `test_continuous_integration` requires it to run on every proposed code change (i.e., in CI). Verify all three are met; link to your CI workflow file as evidence.

5. **Resolve the test coverage criterion (Quality section).**
   Criterion `test_most` asks whether at least 80% of code paths are covered by automated tests. If coverage tooling is not yet in place, add it to CI (e.g., `go test -coverprofile`, `pytest --cov`, `jest --coverage`) and publish the report as a CI artifact or to a service like Codecov. If the project has a documented exception explaining why 80% is not feasible, provide that explanation in the "justification" field — this is accepted by the badge program.

6. **Resolve the static analysis criterion (Analysis section).**
   Criterion `static_analysis` requires at least one static analysis tool to be run on every proposed code change. Use a language-appropriate tool (e.g., `golangci-lint`, `flake8`/`ruff`, `eslint`, `clippy`) integrated into CI. Criterion `static_analysis_fixed` requires that new warnings introduced by a change are addressed before merge. Document the tool and threshold in your contributing guide.

7. **Resolve the signed releases criterion (Security section).**
   Criterion `signed_releases` requires that release artifacts carry cryptographic signatures or that the project uses a reproducible build process. Use `cosign` for container images, `gpg` for tarballs, or GitHub's artifact attestations (`actions/attest-build-provenance`). The `openssf-scorecards` skill covers the Scorecards `Signed-Releases` probe if you want automated tracking.

8. **Resolve the code review criterion (Change Control section).**
   Criterion `two_person_review` requires that all new code changes are reviewed by a person other than the author before being merged. Enforce this with a branch protection rule: require at least one approving review on pull requests targeting the default branch. Screenshot or link the branch protection settings as evidence.

9. **Reach 100% on all Passing criteria.**
   The badge is awarded only at exactly 100% for the Passing level. Review any remaining amber or red items. Use the "justification" field for N/A items where the criterion genuinely does not apply (e.g., `crypto_weaknesses` for a project with no cryptographic code). Do not mark items N/A to avoid work — reviewers read justifications.

10. **Add the badge to README.md.**
    Once the entry shows 100% Passing, copy the Markdown badge snippet from the badge entry page. It looks like:
    ```markdown
    [![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/<ID>/badge)](https://bestpractices.coreinfrastructure.org/projects/<ID>)
    ```
    Place it in the README.md header section alongside other status badges. The numeric project ID is in the URL of your badge entry.

11. **Keep the badge current.**
    The badge does not expire on a fixed schedule, but it can lapse if the project becomes inactive or if criteria are no longer met (e.g., a CI job is removed, the repo is archived). Schedule a review at least once per year and before every graduation application update. The badge entry page shows the last-updated date.

12. **Plan for 2–4 weeks of elapsed time.**
    A mature project completing the questionnaire for the first time typically spends 1–2 weeks answering questions and gathering evidence, then 1–2 weeks implementing missing criteria (coverage tooling, static analysis CI step, branch protection). Start well before the graduation application — do not attempt to complete this on the same day as the application.

## Validation checklist

- [ ] Badge entry created at bestpractices.coreinfrastructure.org with the correct repository URL
- [ ] All ~60 Passing criteria answered (no items left at "?")
- [ ] Badge entry shows 100% Passing level
- [ ] `SECURITY.md` exists in the repo root with a private disclosure process
- [ ] Automated test suite runs in CI on every pull request
- [ ] Test coverage is measured and meets or documents an exception to the 80% target
- [ ] At least one static analysis tool runs in CI on every pull request
- [ ] Release artifacts are signed or the build is reproducible
- [ ] Branch protection requires at least one approving review before merge
- [ ] Badge Markdown snippet is present in README.md header
- [ ] Badge URL resolves and displays the green Passing badge
- [ ] Badge project ID in README.md matches the entry URL

## Common mistakes

**Marking criteria N/A to reach 100% faster** — Reviewers read every N/A justification. Unjustified N/A items are a red flag during graduation review and can result in the application being held. Only use N/A when the criterion genuinely does not apply, and write a clear one-sentence explanation.

**Starting the badge entry on the same day as the graduation application** — The badge requires real implementation work (coverage tooling, CI changes, branch protection). Budget 2–4 weeks minimum and start well before the application deadline.

**Forgetting to add the badge to README.md** — Earning the badge is not enough; CNCF graduation reviewers check that it is linked in the README. The badge must be visible and the link must resolve to a 100% Passing entry.

**Letting the badge entry go stale** — If CI jobs are reorganized or the repo is transferred, badge criteria can silently become unmet. Check the badge entry percentage after any major infrastructure change and before filing a graduation application.

**Conflating badge levels** — The Passing badge is the graduation requirement. Silver and Gold badges are encouraged but not required for graduation. Do not spend time on Silver/Gold criteria until the Passing badge is secured.

**Using the wrong repository URL** — If the project spans multiple repos, the badge entry must be for the primary source repository — the one listed in the CNCF project entry. Documentation repos, website repos, and forks do not need their own badge entries.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):

- **OpenSSF Best Practices badge at Passing level** (Required)

What graduation reviewers specifically check:

1. The badge entry URL is present in the graduation application and links to a valid, current entry at bestpractices.coreinfrastructure.org.
2. The entry shows 100% Passing — not 95%, not "almost there". The badge is a binary gate.
3. The badge Markdown link appears in the project's main README.md and renders as the green "Passing" image.
4. The last-updated date on the badge entry is recent enough to be credible (not years old with a stale CI pipeline).
5. The `two_person_review` and `signed_releases` criteria are met — these are the most commonly challenged items during TOC due diligence.
6. N/A justifications are present and reasonable for any criteria marked not applicable.
