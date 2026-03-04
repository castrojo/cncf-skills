---
id: security-self-assessment
title: "Complete a TAG Security Self-Assessment"
version: "1.0.0"
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
---

# Complete a TAG Security Self-Assessment

## When to use this skill

Use when:
- The project is preparing a CNCF graduation application and has not yet submitted a TAG Security self-assessment
- The project is at incubating stage and wants to proactively document its security model ahead of graduation
- The maintainer team needs to formally describe the project's threat model, attack surfaces, and default security posture for the first time
- The project is responding to a CNCF TOC reviewer request to complete a security self-assessment

Do NOT use when:
- The project has already completed a self-assessment and received TAG Security feedback — link to the existing assessment in the graduation application rather than resubmitting
- The project has been assigned a TAG Security joint review (joint review is TAG-led and follows a different process; this skill covers the project-led self-assessment only)

## What this skill does

This skill guides the project team through writing and submitting a TAG Security self-assessment — a structured 10–20 page document that describes the project's security model, threat model, and known risks. The document is reviewed by CNCF TAG Security, who provide written feedback. Completion of this assessment (and incorporation of feedback) is a required step for CNCF graduation.

## Steps

1. **Read the official template and guide.** Start with the self-assessment template at `https://github.com/cncf/tag-security/blob/main/assessments/guide/self-assessment.md` and the reviewer guide at `https://tag-security.cncf.io/assessments/guide/`. Understand which sections are required versus optional before writing anything.

2. **Allocate time.** Budget 2–3 weeks for the first draft. Involve at least two maintainers — one who owns the security architecture and one who understands day-to-day operations. Do not assign this to a single person working alone.

3. **Fill in the Metadata section.** Provide project name, version assessed, GitHub URL, links to existing security documentation (`SECURITY.md`, security contacts file, prior CVEs), and the names of the self-assessment authors with their organizational affiliations.

4. **Write the Overview: background, goals, and non-goals.** Describe what the project does, what security properties it is designed to provide (confidentiality, integrity, availability, authentication, authorization), and explicitly what it does NOT attempt to provide. Non-goals are as important as goals — reviewers look for honest scoping.

5. **Define actors and actions.** List every type of user or system that interacts with the project (operators, end users, plugins, CI systems, external APIs). For each actor, describe what permissions they hold and what actions they can take. Distinguish between trusted and untrusted actors.

6. **Enumerate assets being protected.** List the data, secrets, APIs, and infrastructure components that the project is responsible for securing. For each asset, describe its sensitivity level and what would happen if it were compromised.

7. **Document the threat model.** For each actor-asset combination that represents a meaningful risk, describe the threat, the attack surface, and the current mitigation. Include known unmitigated risks with an honest explanation of why they are not yet addressed. Do not omit known weaknesses — reviewers expect candor here.

8. **Describe the default security posture.** Document what a default, out-of-the-box installation looks like from a security perspective: which ports are open, what authentication is enabled by default, what network access is required, and what privileges the process runs with. Flag any defaults that are insecure but exist for usability reasons.

9. **Add a security hardening guide (optional but strongly encouraged).** Provide concrete configuration recommendations for production deployments: enabling TLS, restricting RBAC, enabling audit logging, rotating credentials, and similar hardening steps. This section improves reviewer confidence and is directly useful to adopters.

10. **Internal review before submission.** Have at least one maintainer who did not write the document review it for accuracy and completeness. Check that every section in the template is addressed. Check that claims about security properties are verifiable (link to code, configuration, or documentation for each claim).

11. **Submit the self-assessment.** File a GitHub issue in the `cncf/tag-security` repository using the project assessment request template, OR open a pull request adding your document to the `assessments/projects/<your-project>/` directory. Include a brief summary of the project and a link to the draft document in the issue or PR description.

12. **Respond to reviewer feedback.** TAG Security will assign a reviewer, typically within 2 weeks of submission. The review process takes 4–8 weeks. Respond to all reviewer comments. Update the document as needed. The review is complete when the TAG Security reviewer closes the issue or approves the PR.

13. **Store and link the completed assessment.** Once accepted, commit the final document to your project repository (or link to the TAG Security `assessments/projects/` entry). Add a link to the assessment in your `SECURITY.md` and in any future graduation application. Do not let the link rot.

## Validation checklist

- [ ] Template read in full before writing began
- [ ] Metadata section complete: project name, version, links to `SECURITY.md` and security contacts, author names and affiliations
- [ ] Overview covers background, explicit security goals, and explicit non-goals
- [ ] All actor types identified with their permissions and trust levels
- [ ] All protected assets enumerated with sensitivity classification
- [ ] Threat model covers all meaningful actor-asset risk pairs, including unmitigated risks
- [ ] Default security posture documented, including any insecure-by-default settings and their rationale
- [ ] Security hardening guide included (or explicitly noted as out of scope with a reason)
- [ ] All security property claims are linked to verifiable evidence (code, docs, config)
- [ ] Internal review completed by at least one maintainer not on the writing team
- [ ] Submission filed in `cncf/tag-security` as issue or PR
- [ ] All TAG Security reviewer comments addressed
- [ ] Completed assessment linked from `SECURITY.md` and graduation application

## Common mistakes

**Omitting known weaknesses** — TAG Security reviewers expect honest disclosure of unmitigated risks. Projects that omit known issues lose reviewer trust and typically receive a request to revise. Include every known gap with a brief explanation of why it has not been addressed and whether there is a timeline to fix it.

**Conflating self-assessment with joint review** — A self-assessment is project-led: the project team writes it, TAG Security reviews it. A joint review is TAG-led: TAG Security drives the process, conducts interviews, and produces a more thorough report. Some graduation tracks require a joint review rather than (or in addition to) a self-assessment. Confirm with your TOC sponsor which is required before starting.

**Submitting too late** — The review process takes 4–8 weeks after submission, and revision cycles add more time. Submitting the self-assessment after filing the graduation application puts the graduation on hold. Submit the self-assessment at least 3 months before the planned graduation application.

**Vague threat model entries** — Writing "the API could be attacked" is not a threat model entry. Each entry needs: the specific actor, the specific asset, the attack vector, the existing mitigation, and the residual risk. Reviewers will request specificity on every vague entry.

**Claiming security properties not enforced by default** — If TLS is available but not enabled by default, do not describe the project as "using TLS." Describe the default posture accurately; describe the hardened posture separately in the hardening guide.

**Single-author document** — A document written by one person tends to reflect only that person's mental model of the system. Require at least two maintainers with different areas of ownership to co-author the document. Security blind spots are almost always in areas the primary author does not actively maintain.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):

- **TAG Security self-assessment or joint review completed** (Required)

What graduation reviewers specifically check:

1. The `cncf/tag-security` issue or PR for the project exists and is closed (or approved), confirming TAG Security reviewed and accepted the assessment — not merely that a document was written.
2. The assessment covers the current version of the project, not a stale version from incubation. If the project has changed significantly since the original assessment, an updated assessment is expected.
3. The threat model is substantive: it names specific attack surfaces, not generic categories. Reviewers read the threat model section directly and flag vague or boilerplate entries.
4. Known unmitigated risks are disclosed and tracked. If the project acknowledged a risk in the self-assessment, reviewers check whether the graduation application or release notes address it or provide a timeline.
5. The completed assessment is linked from the graduation application. A self-assessment that exists but is not linked in the application will be flagged as a missing artifact.
6. If the project is at the graduated tier and a joint review was required by the TOC (rather than a self-assessment), confirm a joint review was completed — a self-assessment alone is not sufficient in that case.
