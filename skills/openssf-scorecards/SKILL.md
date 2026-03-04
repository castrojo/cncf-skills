---
id: openssf-scorecards
title: "Set Up the OpenSSF Scorecard GitHub Action"
description: "Sets up the OpenSSF Scorecard GitHub Action for automated supply-chain security scoring. Use when a CNCF project needs to configure continuous security posture measurement."
version: "2.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/ossf/scorecard-action"
how_to_guide: "https://securityscorecards.dev"
tags:
  - security
  - openssf
  - scorecards
  - ci
  - clomonitor
mcp_servers:
  - id: github
    description: "Check file existence, create files, open PRs"
    url: "https://github.com/github/mcp-server-github"
  - id: cncf-landscape
    description: "Verify project maturity level and landscape metadata"
    url: "https://github.com/cncf/landscape-mcp"
---

Add the `ossf/scorecard-action` GitHub Actions workflow to your repository so that
~20 supply-chain security checks run automatically on every push and weekly schedule.
Results publish to the GitHub Security tab and the OSSF public API, which CLOMonitor
reads to populate the CNCF project dashboard.

## When to use

- Project is on GitHub and does not yet have `ossf/scorecard-action` in `.github/workflows/`
- Preparing a CNCF incubation or graduation application — reviewers check CLOMonitor
- CLOMonitor shows "OpenSSF Scorecard" as a failing check
- Project wants continuous, automated monitoring of security best practices

Do NOT use when:
- Project is not hosted on GitHub — Scorecards is GitHub-specific; use `trivy` or `snyk` for GitLab/Gitea/Bitbucket
- Repository is private — results will not appear on CLOMonitor or the public badge endpoint

## Steps

1. **Enable required repository settings before adding the workflow.**
   In repository Settings: set *Actions → General → Workflow permissions* to read-only.
   Enable *Secret scanning* under *Settings → Security*. Add branch protection on the
   default branch requiring PR reviews before merging — `Branch-Protection` (weight 5.0)
   is the check most projects fail.

2. **Follow the official quickstart to generate the workflow file.**
   Go to `https://securityscorecards.dev` and use the guided setup, or copy the starter
   workflow directly from `https://github.com/ossf/scorecard-action#installation`.
   ⚠️ Pin all `uses:` lines to full 40-character commit SHAs — tags are mutable and
   will fail the `Pinned-Dependencies` check. Let Renovate or Dependabot manage SHA
   updates; never update them manually.

3. **Commit the workflow and verify it runs.**
   Push to the default branch. Check the *Actions* tab — the first run takes 2–5 minutes.
   If the OIDC step fails, confirm the repo is public and `publish_results: true` is set.
   ⚠️ Set `publish_results: false` on forks and private repos.

4. **Check SARIF findings in the Security tab.**
   Navigate to *Security → Code scanning*. Each failing check appears as a finding with
   its weight and a remediation link. Prioritize by weight:
   `Dependency-Update-Tool` (10) → `Branch-Protection` (5) → `Vulnerabilities` (5) →
   `Token-Permissions` (3) → `Pinned-Dependencies` (2).
   Fix `Dependency-Update-Tool` first: add `.github/dependabot.yml` or `renovate.json`.

5. **Verify the score appears on CLOMonitor.**
   Visit `https://clomonitor.io/projects/cncf/<project-name>` and check the Security
   section. Allow up to 24 hours after the first successful run. A score of 5.0 or
   higher is the expected baseline for graduation.

6. **Add the Scorecard badge to `README.md`.**
   After the first successful run, add:
   ```
   [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/<org>/<repo>/badge)](https://securityscorecards.dev/viewer/?uri=github.com/<org>/<repo>)
   ```

## Checklist

- [ ] `.github/workflows/scorecard.yml` exists and all `uses:` lines are pinned to full commit SHAs
- [ ] Workflow ran successfully — no errors in the Actions tab
- [ ] SARIF findings visible in *Security → Code scanning*
- [ ] `publish_results: true` set and score visible on the OSSF public API
- [ ] CLOMonitor shows a Scorecard score for the project (graduation)
- [ ] Score is 5.0 or higher (graduation)
- [ ] `Dependency-Update-Tool` check passes — Dependabot or Renovate configured (graduation)
- [ ] `Branch-Protection` check passes — default branch has protection rules (graduation)
- [ ] `Token-Permissions` check passes — all workflows declare minimal permissions (graduation)
- [ ] `Pinned-Dependencies` check passes — all Actions pinned to SHAs (graduation)
- [ ] Scorecard badge added to `README.md` and links to the live score page (graduation)
