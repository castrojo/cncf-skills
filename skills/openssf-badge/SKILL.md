---
id: openssf-badge
title: "Earn the OpenSSF Best Practices Badge"
version: "2.0.0"
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
mcp_servers:
  - id: github
    description: "Add badge to README, verify branch protection, check CI workflow files"
    url: "https://github.com/github/mcp-server-github"
---

Complete the OpenSSF Best Practices questionnaire at bestpractices.coreinfrastructure.org
to earn the Passing badge — a hard gate for CNCF graduation — and embed it in README.md.

## When to use

Use when:
- The project is preparing a CNCF graduation application
- The project has not yet earned a Passing-level OpenSSF Best Practices badge
- The project's existing badge has lapsed or dropped below 100%

Do NOT use when:
- The project already holds a current Passing badge at 100% — just verify it is still active and linked in README.md
- The repo is a documentation-only sub-repo — link to the parent project's badge instead

## Steps

1. **Create an account and start the badge entry.**
   Go to https://bestpractices.coreinfrastructure.org, sign in with GitHub, click "Get Your Badge Now", enter the repository URL.
   ⚠️ Budget 2–4 weeks — do not start on the day of the graduation application.

2. **Work through all criteria sections in order.** Answer every item (Met / Unmet / N/A / ?).
   ⚠️ Unknown (`?`) counts against your percentage; N/A with a clear justification does not.
   ⚠️ Mark N/A only when the criterion genuinely does not apply — reviewers read every justification.

3. **Resolve SECURITY.md first** (`report_process`): private disclosure channel, response time,
   no public issues for security reports. See the `security-policy` skill.

4. **Resolve automated tests** (`test`, `test_invocation`, `test_continuous_integration`):
   test suite, standard invocation command, runs in CI on every proposed change.

5. **Resolve test coverage** (`test_most`): ≥80% code path coverage or a documented justification.
   Add coverage tooling to CI (e.g., `go test -coverprofile`, `pytest --cov`, `jest --coverage`).

6. **Resolve static analysis** (`static_analysis`): at least one tool (e.g., `golangci-lint`,
   `ruff`, `eslint`) runs in CI on every proposed change; new warnings are addressed before merge.

7. **Resolve signed releases** (`signed_releases`): use `cosign` for containers, `gpg` for
   tarballs, or GitHub artifact attestations. See the `openssf-scorecards` skill for automated tracking.

8. **Resolve code review** (`two_person_review`): branch protection requires ≥1 approving review
   on every PR to the default branch.

9. **Reach 100% Passing.** The badge is awarded only at exactly 100%.

10. **Add the badge to README.md:**
    ```markdown
    [![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/<ID>/badge)](https://bestpractices.coreinfrastructure.org/projects/<ID>)
    ```
    If GitHub MCP available: `github_update_file` path=`README.md` with badge in header.

## Checklist

- [ ] Badge entry created with the correct repository URL
- [ ] All ~60 Passing criteria answered (no `?` items remain)
- [ ] Badge entry shows 100% Passing (graduation — hard gate)
- [ ] SECURITY.md exists with private disclosure process
- [ ] Automated test suite runs in CI on every pull request
- [ ] Test coverage measured or documented exception provided
- [ ] Static analysis tool runs in CI on every pull request
- [ ] Release artifacts signed or build is reproducible
- [ ] Branch protection requires ≥1 approving review before merge
- [ ] Badge Markdown snippet in README.md header with correct project ID
- [ ] Badge URL resolves and displays green Passing badge
