---
id: graduation-checklist
title: "CNCF Graduation Readiness Checklist"
version: "2.0.0"
domain: lifecycle
cncf_requirement: optional
applies_to: [incubating, graduated]
template_source: "https://github.com/cncf/toc/blob/main/process/graduation_criteria.md"
how_to_guide: "https://github.com/cncf/toc/blob/main/process/graduation_due_diligence.md"
tags:
  - graduation
  - checklist
  - due-diligence
mcp_servers:
  - id: cncf-landscape
    description: "Verify project maturity level and landscape metadata"
    url: "https://github.com/cncf/landscape-mcp"
  - id: github
    description: "Check file existence across all required artifacts"
    url: "https://github.com/github/mcp-server-github"
---

Use this skill to audit a project for CNCF graduation readiness. Each criterion maps to
the skill that creates the required artifact and a one-line verification command.

## When to use

- Project is preparing a graduation application and you need a complete readiness audit
- TOC reviewer has asked for a due diligence checklist
- Project wants to identify which graduation blockers remain before filing

Do NOT use when:
- Project is at sandbox stage — use `_index` to identify which sandbox-required skills to run first

## Steps

1. **Confirm project is incubating and in-scope for graduation.**
   If CNCF Landscape MCP available: query project status
   Otherwise: `gh api repos/cncf/landscape/contents/landscape.yml | jq '.[] | select(.name=="<project>")'`

2. **Work through the checklist below.**
   For each failing item, load the indicated skill to create or fix the artifact.
   Run each skill's own checklist before returning here.

3. **Cross-check the due diligence template.**
   The graduation application uses the template at:
   `https://github.com/cncf/toc/blob/main/process/graduation_due_diligence.md`
   Every section of that template must be answerable from the project's public documents.

## Reference files

- `references/graduation-application-template.md` — annotated graduation application template with field-by-field guidance

## Graduation criteria

### Governance

| Criterion | Skill | Verify |
|---|---|---|
| Clear governance document exists | `governance-maintainer-council` | `gh api repos/{owner}/{repo}/contents/GOVERNANCE.md` |
| Maintainer list is complete and current | `maintainers-list` | MAINTAINERS.md exists with affiliation column |
| All subprojects listed | `governance-subprojects` | GOVERNANCE.md lists subprojects with owners |
| Contributor ladder documented | `contributor-ladder` | CONTRIBUTOR_LADDER.md exists with path to maintainer |
| Vendor-neutral governance statement | `vendor-neutrality` | `## Vendor Neutrality` heading in GOVERNANCE.md |
| Maintainers from 2+ organizations | `vendor-neutrality` | Audit MAINTAINERS.md affiliation column |
| Decision-making process documented | `governance-maintainer-council` | Voting/consensus process in GOVERNANCE.md |

### Contribution

| Criterion | Skill | Verify |
|---|---|---|
| Contributing guide exists | `contributing-guide` | CONTRIBUTING.md in repo root |
| Process for submitting issues/changes | `contributing-guide` | PR and issue process in CONTRIBUTING.md |
| Code review process documented | `reviewing-guide` | Review criteria and approver list documented |

### Security

| Criterion | Skill | Verify |
|---|---|---|
| Security issue reporting process | `security-policy` | SECURITY.md with disclosure instructions |
| Security response contacts named | `security-contacts` | SECURITY_CONTACTS.md with current contacts |
| TAG Security self-assessment completed | `security-self-assessment` | Closed issue or merged PR in cncf/tag-security |
| OpenSSF Scorecards score ≥ 5.0 | `openssf-scorecards` | `https://clomonitor.io/projects/cncf/<project>` |
| OpenSSF Best Practices badge (Passing) | `openssf-badge` | Badge link in README.md resolves to Passing |

### Lifecycle

| Criterion | Skill | Verify |
|---|---|---|
| Public adopters list | `adopters` | ADOPTERS.md with 3+ production adopters |
| Architecture document | `architecture` | ARCHITECTURE.md in repo root |
| Code of Conduct (CNCF CoC) | `code-of-conduct` | CODE_OF_CONDUCT.md references CNCF CoC |
| CODEOWNERS file | `codeowners` | CODEOWNERS in repo root matches governance roles |
| Documented release process | `releases` | RELEASES.md with versioning, signing, publication |
| Artifact signing (cosign or SLSA) | `releases` | Verification commands in RELEASES.md |
| Public roadmap | `roadmap` | ROADMAP.md updated within last 6 months |
| Roadmap proposal process | `roadmap` | "Proposing roadmap items" section in ROADMAP.md |
| Vendor-neutral contribution tooling | `vendor-neutrality` | CI requires no proprietary accounts |

## Checklist

- [ ] All governance criteria satisfied (see table above) (graduation)
- [ ] All contribution criteria satisfied (graduation)
- [ ] All security criteria satisfied (graduation)
- [ ] All lifecycle criteria satisfied (graduation)
- [ ] TAG Security self-assessment closed/approved in cncf/tag-security (graduation)
- [ ] OpenSSF Scorecards score ≥ 5.0 on CLOMonitor (graduation)
- [ ] OpenSSF Best Practices badge at Passing level (graduation)
- [ ] 3+ documented production adopters in ADOPTERS.md (graduation)
- [ ] Graduation application template fully answered (graduation)
