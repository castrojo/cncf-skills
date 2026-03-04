---
id: code-of-conduct
title: "Adopt the CNCF Code of Conduct"
version: "2.0.0"
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
mcp_servers:
  - id: github
    description: "Check file existence, create CODE_OF_CONDUCT.md, update README and CONTRIBUTING"
    url: "https://github.com/github/mcp-server-github"
---

Place a CNCF-compliant `CODE_OF_CONDUCT.md` in the repository root, link it from
`README.md` and `CONTRIBUTING.md`, and designate an enforcement contact.

## When to use

Use when:
- The project is being submitted to CNCF as a sandbox proposal and has no Code of Conduct
- Incubating or graduation review has flagged CoC compliance as incomplete
- A new repository has been added to the project and needs its own CoC file or cross-reference
- The enforcement contact is undocumented, outdated, or points to a non-CNCF address

Do NOT use when:
- The repo is a fork with an upstream CoC — link to the upstream CoC instead
- The project already has Contributor Covenant v2.x — add a CNCF cross-reference rather than overwriting

## Steps

1. **Check if CODE_OF_CONDUCT.md exists.**
   If GitHub MCP available: `github_get_contents` path=`CODE_OF_CONDUCT.md`
   Otherwise: `gh api repos/{owner}/{repo}/contents/CODE_OF_CONDUCT.md`
   If it references `https://github.com/cncf/foundation/blob/main/code-of-conduct.md`
   and names an enforcement contact, skip to step 5.

2. **Create CODE_OF_CONDUCT.md** (preferred link approach for most projects):
   ```markdown
   # Code of Conduct
   This project follows the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/main/code-of-conduct.md).
   ## Reporting
   To report a violation, contact the CNCF at conduct@cncf.io.
   For project-level concerns, contact [maintainer alias or email].
   ```

3. **Add a scope statement** covering all project spaces:
   > "This Code of Conduct applies to the GitHub repository, issue tracker, mailing lists,
   > Slack channels, community meetings, and any other project forums."
   ⚠️ Scoping only to "code contributions" is a graduation finding — broaden it.

4. **Cross-link from README.md and CONTRIBUTING.md.** Both files must reference the CoC.
   ⚠️ Reviewers check these files directly, not just CODE_OF_CONDUCT.md in isolation.

5. **Audit multi-repo coverage.** Every repo in the GitHub org must have a CoC file
   or a visible pointer to the primary one.
   ⚠️ Secondary repos (docs, website) commonly fail this check at graduation.

6. **Verify all links resolve** (no 404s, no stale CNCF URLs).

## Checklist

- [ ] CODE_OF_CONDUCT.md exists in the repo root
- [ ] References the CNCF CoC at `https://github.com/cncf/foundation/blob/main/code-of-conduct.md`
- [ ] Enforcement contact explicitly named (`conduct@cncf.io` or documented project alias) (graduation)
- [ ] Scope statement covers all project spaces (graduation)
- [ ] README.md contains a link or badge to CODE_OF_CONDUCT.md (graduation)
- [ ] CONTRIBUTING.md references the CoC and names the reporting contact (graduation)
- [ ] All secondary repositories have their own CoC file or canonical cross-reference (graduation)
- [ ] All CoC links resolve
