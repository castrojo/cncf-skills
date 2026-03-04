---
id: security-self-assessment
title: "Complete a TAG Security Self-Assessment"
description: "Completes the CNCF TAG Security self-assessment questionnaire documenting a project's security posture, threat model, and practices. Use when preparing for a TAG Security review or graduation application."
version: "2.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://github.com/cncf/tag-security/blob/main/assessments/guide/self-assessment.md"
how_to_guide: "https://tag-security.cncf.io/assessments/guide/"
tags:
  - security
  - self-assessment
  - tag-security
  - graduation
mcp_servers:
  - id: github
    description: "Check file existence, open PRs to cncf/tag-security"
    url: "https://github.com/github/mcp-server-github"
---

Guide the project team through writing and submitting a TAG Security self-assessment —
a structured document describing the project's security model, threat model, and known
risks — required for CNCF graduation.

## When to use

- Preparing a graduation application and no TAG Security self-assessment has been submitted
- Project is at incubating stage and wants to document its security model proactively
- Maintainer team needs to formally describe threat model and attack surfaces for the first time
- Responding to a CNCF TOC reviewer request for a self-assessment

Do NOT use when:
- Project has already completed a self-assessment and received TAG Security feedback —
  link to the existing assessment in the graduation application; do not resubmit
- Project has been assigned a TAG Security *joint review* — that is TAG-led and follows
  a different process; this skill covers the project-led self-assessment only

## Steps

1. **Read the official template and reviewer guide before writing anything.**
   Template: `https://github.com/cncf/tag-security/blob/main/assessments/guide/self-assessment.md`
   Guide: `https://tag-security.cncf.io/assessments/guide/`
   Understand which sections are required vs. optional.
   ⚠️ Submit at least 3 months before the planned graduation application — the review
   takes 4–8 weeks and revision cycles add more time.

2. **Assign authors and allocate time.**
   Budget 2–3 weeks for the first draft. Involve at least two maintainers: one who owns
   security architecture, one who understands day-to-day operations.
   ⚠️ Single-author documents have consistent blind spots — require co-authorship.

3. **Fill in Metadata, Overview, and Goals/Non-goals.**
   Include project name, version assessed, GitHub URL, links to `SECURITY.md` and
   security contacts, author names and affiliations. State explicitly what security
   properties the project provides (confidentiality, integrity, availability,
   authentication, authorization) and what it does NOT attempt to provide.
   Non-goals matter as much as goals — reviewers look for honest scoping.

4. **Define actors, assets, and the threat model.**
   List every actor type (operators, end users, plugins, CI systems) with their
   permissions and trust level. List every protected asset with its sensitivity level.
   For each meaningful actor-asset risk pair: name the threat, attack surface, current
   mitigation, and residual risk.
   ⚠️ Do not omit known weaknesses — reviewers expect candor and will flag omissions.
   ⚠️ Vague entries ("the API could be attacked") will be sent back for revision.

5. **Describe the default security posture.**
   Document a default, out-of-the-box installation: open ports, default authentication,
   required network access, process privileges. Flag any insecure defaults and explain why
   they exist. Add a hardening guide with concrete production configuration recommendations.

6. **Internal review before submission.**
   Have at least one maintainer who did not write the document review it.
   Verify every security property claim is backed by a link to code, config, or documentation.

7. **Submit to cncf/tag-security.**
   File a GitHub issue using the project assessment request template, OR open a PR adding
   the document to `assessments/projects/<your-project>/` in the `cncf/tag-security` repo.
   Include a project summary and link to the draft in the issue/PR description.

8. **Respond to reviewer feedback and store the result.**
   TAG Security assigns a reviewer within ~2 weeks. Respond to all comments and update
   the document. Once accepted, commit the final document to your project repo and link
   to it from `SECURITY.md` and the graduation application.

## Checklist

- [ ] Official template read before writing began
- [ ] Metadata complete: project name, version, links to `SECURITY.md` and security contacts, author affiliations
- [ ] Overview covers background, explicit security goals, and explicit non-goals
- [ ] All actor types identified with permissions and trust levels
- [ ] All protected assets enumerated with sensitivity classification
- [ ] Threat model covers all meaningful actor-asset risk pairs including unmitigated risks (graduation)
- [ ] Default security posture documented including insecure-by-default settings
- [ ] All security property claims link to verifiable evidence
- [ ] Internal review completed by at least one non-author maintainer
- [ ] Submission filed in `cncf/tag-security` as issue or PR (graduation)
- [ ] All TAG Security reviewer comments addressed (graduation)
- [ ] Completed assessment linked from `SECURITY.md` and graduation application (graduation)
