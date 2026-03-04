---
id: openssf-scorecards
title: "Set Up the OpenSSF Scorecard GitHub Action"
version: "1.0.0"
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
---

# Set Up the OpenSSF Scorecard GitHub Action

## When to use this skill

Use when:
- The project is hosted on GitHub and does not yet have the `ossf/scorecard-action` workflow
- Preparing a CNCF incubation or graduation application — graduation reviewers check the CLOMonitor dashboard, which pulls Scorecard data automatically
- The project's CLOMonitor score is low or shows "OpenSSF Scorecard" as a failing check
- The project wants automated, continuous monitoring of ~20 security best practices without manual audits
- The project is adding or auditing its GitHub Actions security posture (token permissions, pinned dependencies, branch protection)

Do NOT use when:
- The project is not hosted on GitHub — Scorecards is GitHub-specific; use an alternative like `trivy` or `snyk` for non-GitHub hosting platforms (GitLab, Gitea, Bitbucket, etc.)
- The repository is private — the public Scorecard API and OSSF badge require a public repository; the action can still run in private repos but results will not appear on CLOMonitor or the public badge endpoint

## What this skill does

Guides a maintainer through adding the `ossf/scorecard-action` GitHub Actions workflow that automatically evaluates ~20 security practices on every push and weekly schedule. The workflow uploads results to the GitHub Security tab as SARIF findings and publishes the project's score to the OpenSSF public API, which CLOMonitor reads to populate the CNCF project dashboard. CNCF graduation reviewers consult CLOMonitor; a Scorecards score below 5.0 generates questions during review.

## Steps

1. **Ensure the required repository settings are enabled.** Before adding the workflow, confirm:
   - **GitHub token permissions:** In the repository settings under *Actions → General → Workflow permissions*, set the default token to **"Read repository contents and metadata"** (read-only). The workflow grants the specific `security-events: write` permission it needs via the workflow file itself.
   - **Secret scanning:** Enable under *Settings → Security → Secret scanning*. This improves the `Token-Permissions` and `Secrets` Scorecard checks.
   - **Branch protection on the default branch:** Add at minimum one rule requiring pull request reviews before merging. The `Branch-Protection` check (weight 5.0) is the check most projects fail and has the highest single-check impact on score.

2. **Create the workflow file.** Create `.github/workflows/scorecard.yml` with the following content. Replace `main` with your default branch name if different:

   ```yaml
   # .github/workflows/scorecard.yml
   # Runs OpenSSF Scorecard analysis on push and weekly schedule.
   # Results appear in the GitHub Security tab (SARIF) and are published
   # to the OSSF public API for CLOMonitor to consume.
   name: Scorecard supply-chain security

   on:
     branch_protection_rule:
     schedule:
       - cron: '20 9 * * 1'   # Weekly on Monday at 09:20 UTC
     push:
       branches: ["main"]

   permissions: read-all

   jobs:
     analysis:
       name: Scorecard analysis
       runs-on: ubuntu-latest
       permissions:
         security-events: write        # Upload SARIF results to Security tab
         id-token: write               # Publish results to OSSF public API (OIDC)
         contents: read
         actions: read

       steps:
         - name: Checkout code
           uses: actions/checkout@v4
           with:
             persist-credentials: false

         - name: Run analysis
           uses: ossf/scorecard-action@main
           with:
             results_file: results.sarif
             results_format: sarif
             # Publish results to the OSSF REST API for CLOMonitor and the
             # public badge endpoint. Set to 'false' for private repositories.
             publish_results: true

         - name: Upload artifact
           uses: actions/upload-artifact@v4
           with:
             name: SARIF file
             path: results.sarif
             retention-days: 5

         - name: Upload to code-scanning
           uses: github/codeql-action/upload-sarif@v3
           with:
             sarif_file: results.sarif
   ```

   > **SHA pinning note:** The template above uses `@main` for `ossf/scorecard-action` for readability. In production, pin to a full commit SHA (e.g., `ossf/scorecard-action@dc0ab093b8`) and let Renovate or Dependabot manage updates. Similarly pin `actions/checkout`, `actions/upload-artifact`, and `github/codeql-action/upload-sarif`. Unpinned actions fail the `Pinned-Dependencies` Scorecard check.

3. **Commit and push the workflow file.** Push directly to the default branch (or merge a PR). The workflow runs immediately on push and then on the weekly schedule. The first run takes 2–5 minutes.

4. **Verify the workflow ran successfully.** In the *Actions* tab, confirm the `Scorecard supply-chain security` workflow completed without errors. A failed OIDC authentication step usually means the repository is private or `publish_results: true` is set on a fork — set it to `false` in those cases.

5. **Check the GitHub Security tab for SARIF findings.** Navigate to *Security → Code scanning*. Scorecard uploads one finding per failing check. Each finding names the check, its weight, and a remediation link. Use this view to prioritize which checks to fix first.

6. **Read the CLOMonitor report for the project.** Visit `https://clomonitor.io/projects/cncf/<project-name>`. The *Security* section shows the Scorecard score and per-check status. CLOMonitor polls the OSSF API; allow up to 24 hours for the score to appear after the first successful workflow run.

7. **Prioritize fixes by check weight.** The checks with the largest impact on overall score are:

   | Check | Weight | Most common failure reason |
   |---|---|---|
   | `Dependency-Update-Tool` | 10 | No Renovate or Dependabot config |
   | `Branch-Protection` | 5 | Default branch has no protection rules |
   | `Vulnerabilities` | 5 | Known CVEs in pinned dependencies |
   | `Token-Permissions` | 3 | Workflows use `permissions: write-all` or omit `permissions` entirely |
   | `Pinned-Dependencies` | 2 | GitHub Actions pinned to tags, not SHAs |

   Fix `Dependency-Update-Tool` first (add `.github/dependabot.yml` or a `renovate.json`) — it has the highest weight and is the quickest win. Then add branch protection rules for `Branch-Protection`.

8. **Add the Scorecard badge to `README.md`.** After the first successful run, retrieve the badge URL from the OSSF API and add it to the project README:

   ```markdown
   [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/<org>/<repo>/badge)](https://securityscorecards.dev/viewer/?uri=github.com/<org>/<repo>)
   ```

   Replace `<org>` and `<repo>` with the actual GitHub organization and repository names.

## Validation checklist

- [ ] `.github/workflows/scorecard.yml` exists and matches the template above (or equivalent)
- [ ] Workflow triggered successfully on push — no errors in the Actions tab
- [ ] SARIF findings appear in *Security → Code scanning* tab
- [ ] `publish_results: true` is set (repository is public) — score is visible on OSSF API
- [ ] CLOMonitor shows a Scorecard score for the project (allow up to 24 hours)
- [ ] Scorecard score is 5.0 or higher — scores below 5.0 require a remediation plan before graduation
- [ ] `Dependency-Update-Tool` check passes (Dependabot or Renovate configured)
- [ ] `Branch-Protection` check passes (default branch has protection rules)
- [ ] `Token-Permissions` check passes (workflows declare minimal permissions)
- [ ] `Pinned-Dependencies` check passes (Actions pinned to full commit SHAs)
- [ ] Scorecard badge added to `README.md` and links to the project's OSSF score page

## Common mistakes

**Using `permissions: write-all` or no `permissions` key in other workflows** — Scorecard's `Token-Permissions` check (weight 3.0) scans all workflow files in `.github/workflows/`, not just `scorecard.yml`. A single workflow that omits the `permissions` key causes this check to fail. Add `permissions: read-all` at the top level of every workflow file and grant only the specific write permissions each job needs.

**Pinning actions to tags instead of full commit SHAs** — Tags are mutable; a maintainer or attacker can move a tag to a different commit. Scorecard's `Pinned-Dependencies` check (weight 2.0) fails if any `uses:` line references a tag. Pin all actions to the full 40-character commit SHA: `actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af68` and let Renovate or Dependabot update the SHA automatically. Do not update SHAs manually.

**Setting `publish_results: true` on a fork** — Forks cannot authenticate to the OSSF public API via OIDC because the repository identity does not match. The workflow will fail with an OIDC error. Set `publish_results: false` in forked repositories and in any repository that is private.

**Expecting CLOMonitor to update immediately** — CLOMonitor polls the OSSF REST API on its own schedule, typically every 24 hours. The Scorecard workflow completing successfully does not mean CLOMonitor reflects the new score immediately. Wait at least 24 hours, then check the CLOMonitor dashboard. If the score is still absent after 48 hours, verify `publish_results: true` is set and the first workflow run succeeded with no OIDC errors.

**Not adding branch protection before running Scorecards** — The `Branch-Protection` check (weight 5.0) is evaluated by querying the GitHub API for the default branch's protection rules. The Scorecard workflow itself does not add branch protection — a human must configure it in repository settings. Failing `Branch-Protection` alone can drop the overall score by 0.5–1.0 points.

**Treating the Scorecard score as a one-time task** — Scores degrade over time as new checks are added, dependencies accumulate CVEs, or protection rules are removed. The weekly schedule trigger ensures the score is re-evaluated continuously. Monitor the CLOMonitor dashboard or subscribe to OSSF score alerts to catch regressions before a graduation review.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):

- **OpenSSF Best Practices / Scorecard** (Required) — Graduation reviewers explicitly check the CLOMonitor dashboard for a passing Scorecard score. A score of 5.0 or higher with no critical check failures is the expected baseline at graduation.

What graduation reviewers specifically check:

1. **CLOMonitor shows a Scorecard score of 5.0 or higher.** Reviewers navigate to `clomonitor.io/projects/cncf/<project>` and look at the Security section. A missing score (workflow not configured or `publish_results: false`) is treated the same as a failing score.

2. **`Dependency-Update-Tool` check passes.** This is the highest-weight check (10.0). Reviewers expect Dependabot (`.github/dependabot.yml`) or Renovate (`renovate.json` or `.renovaterc`) to be present and configured for at least the primary language ecosystem and GitHub Actions.

3. **`Branch-Protection` check passes.** Reviewers look for branch protection rules on the default branch (required reviews, status checks, no force-push). Projects that allow direct pushes to `main` without review fail this check and raise governance concerns beyond the Scorecard score.

4. **No known high or critical CVEs in pinned dependencies (`Vulnerabilities` check).** The `Vulnerabilities` check (weight 5.0) queries the OSV database. Projects with unresolved high-severity CVEs in dependencies will be asked to remediate before graduation is approved.

5. **SARIF findings visible in the GitHub Security tab.** Reviewers verify the workflow is actually running by checking for code-scanning alerts. An empty Security tab with no findings may indicate `publish_results` or SARIF upload is misconfigured rather than that all checks pass.

6. **Scorecard badge present in `README.md` and links to a live score.** The badge serves as a public commitment to maintaining the score. Reviewers click through to confirm the linked score is current and matches the CLOMonitor data.
