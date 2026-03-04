---
description: Lists all available CNCF community health skills by domain and requirement
  level. Use when discovering which skills exist, routing to the correct skill for
  a specific CNCF template, or getting an overview of what community health documents
  a project needs.
id: _index
template_source: https://github.com/cncf/project-template
---

Load this skill first when you need to choose which CNCF skill to invoke.
Pick the skill that matches the artifact you need to create or fix.

## When to use

- You are auditing or setting up CNCF compliance for a project
- You need to create a specific governance artifact but don't know which skill applies

## Skills catalog

### Contribution

| Skill id | Artifact | Requirement | Levels |
|---|---|---|---|
| `contributing-guide` | CONTRIBUTING.md | required | sandbox+ |
| `issue-labels` | Issue label taxonomy | encouraged | sandbox+ |
| `reviewing-guide` | Review process doc | encouraged | sandbox+ |

### Governance

| Skill id | Artifact | Requirement | Levels |
|---|---|---|---|
| `contributor-ladder` | CONTRIBUTOR_LADDER.md | required | sandbox+ |
| `governance-elections` | Election process | encouraged | incubating+ |
| `governance-maintainer-council` | Maintainer council charter | encouraged | incubating+ |
| `governance-subprojects` | Subproject list | encouraged | incubating+ |
| `maintainers-list` | MAINTAINERS.md | required | sandbox+ |

### Security

| Skill id | Artifact | Requirement | Levels |
|---|---|---|---|
| `security-policy` | SECURITY.md | required | sandbox+ |
| `security-contacts` | SECURITY_CONTACTS.md | required | sandbox+ |
| `incident-response` | Incident response process | encouraged | incubating+ |
| `security-embargo` | Embargo policy + notice | optional | incubating+ |

### Lifecycle

| Skill id | Artifact | Requirement | Levels |
|---|---|---|---|
| `adopters` | ADOPTERS.md | required | graduation |
| `architecture` | ARCHITECTURE.md | required | graduation |
| `code-of-conduct` | CODE_OF_CONDUCT.md | required | sandbox+ |
| `codeowners` | CODEOWNERS | required | graduation |
| `openssf-badge` | OpenSSF Passing badge | required | graduation |
| `openssf-scorecards` | Scorecards GitHub Action | required | graduation |
| `releases` | RELEASES.md | required | graduation |
| `roadmap` | ROADMAP.md | required | graduation |
| `security-self-assessment` | TAG Security assessment | required | graduation |
| `vendor-neutrality` | Vendor-neutrality statement | required | graduation |

## Workflows

**Sandbox onboarding (minimum viable):**
`contributing-guide` → `maintainers-list` → `security-policy` → `security-contacts` → `contributor-ladder` → `code-of-conduct`

**Graduation readiness (all required criteria):**
See `graduation-checklist` skill for the full ordered list.

## Checklist

- [ ] Loaded the right skill for the artifact you need
