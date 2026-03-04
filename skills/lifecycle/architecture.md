---
id: architecture
title: "Create or Update an ARCHITECTURE.md"
version: "1.0.0"
domain: lifecycle
cncf_requirement: required
applies_to:
  - incubating
  - graduated
template_source: "https://contribute.cncf.io/maintainers/templates/"
tags:
  - architecture
  - documentation
  - design
  - onboarding
---

# Create or Update an ARCHITECTURE.md

## When to use this skill

Use when:
- The project is preparing for incubating or graduation review and lacks a written architecture overview
- A new contributor asks "how does this project actually work?" and there is no single document to point them to
- The project has grown beyond a single binary or package and its structure is no longer self-evident from the code
- A significant architectural change (new subsystem, new data flow, replaced dependency) has been merged and the existing document is now stale
- TAG Security or a TOC reviewer has flagged the absence of an architecture document during due diligence

Do NOT use when:
- The project is a specification, not code — write a "How it works" section in `README.md` instead; a separate architecture file for a spec project creates confusion about what is normative
- The project is extremely small (single binary, under ~1000 LOC) — a detailed `README.md` is sufficient; an `ARCHITECTURE.md` at this scale adds maintenance overhead without orientation value

## What this skill does

This skill walks a maintainer through creating or updating `ARCHITECTURE.md` — a document that explains the project's major components, how they interact, the data flow, and the key design decisions that shaped the current implementation. The document is calibrated for two audiences: new contributors who need orientation before reading code, and CNCF graduation reviewers (TOC and TAG Security) who need to assess the project's design before evaluating its security posture and scalability. The output is a document that answers "what are the moving parts and why are they built this way?" without duplicating what code comments already cover.

## Steps

1. **Identify the major subsystems.** Start by reading the top-level directory structure and the project's own README. List every top-level package, binary, or module that has a distinct responsibility. A subsystem is anything that could be described in a sentence starting with "this component is responsible for…". Aim for 3–10 subsystems; if you have more, group related ones.

2. **Draw a component diagram.** Create a simple diagram showing how the subsystems connect. ASCII art is acceptable and preferred over an external image file — it renders in every viewer, requires no tooling, and can be kept in sync with a text editor. Use the following style as a starting point:
   ```
   ┌─────────────┐     gRPC      ┌──────────────┐
   │   CLI/SDK   │ ──────────── │  API Server  │
   └─────────────┘               └──────┬───────┘
                                         │ watches
                                  ┌──────▼───────┐
                                  │  Controller  │
                                  └──────┬───────┘
                                         │ writes
                                  ┌──────▼───────┐
                                  │  Data Store  │
                                  └──────────────┘
   ```
   Label each arrow with the protocol or mechanism (HTTP, gRPC, event queue, shared memory, file system, etc.).

3. **Describe each component in 2–5 sentences.** For each subsystem in the diagram, write a short paragraph covering: what it does, what it owns (data, state, resources), and what it does NOT do (boundary clarity). Do not describe implementation details that are already visible in the code — describe the role and responsibilities.

4. **Document the primary data flow.** Walk through the most important end-to-end user journey (e.g., "a request comes in, is validated, queued, processed, and a result returned") as a numbered sequence. This is distinct from the component diagram: the diagram shows structure, the flow shows behavior. One flow is usually enough; add a second only if the project has a genuinely different operational mode (e.g., a batch path versus a streaming path).

5. **List external dependencies and integration points.** Enumerate every external system the project talks to: databases, message queues, cloud provider APIs, container runtimes, Kubernetes API server, etc. For each, note: the protocol used, whether it is required or optional, and what happens when it is unavailable. This section is read directly by TAG Security reviewers.

6. **Document the deployment model.** Describe the supported deployment topologies in 3–5 sentences: single-binary, operator-deployed, Helm chart, sidecar, standalone daemon, etc. If the project runs in Kubernetes, note what namespace permissions it requires and why. If it runs as a standalone binary, note OS/arch support.

7. **Record extension points.** If the project is designed to be extended (plugins, webhooks, provider interfaces, admission hooks, custom resource definitions), list them. One sentence per extension point noting the interface type and where to find the API definition is sufficient.

8. **Capture key design decisions inline.** For each major architectural choice (why gRPC over REST, why a single-process design instead of microservices, why the reconciliation loop runs every N seconds), add one or two sentences explaining the rationale. Do NOT write full ADRs here — this is not an Architecture Decision Record repository. The goal is enough context that a reviewer understands the intent without needing to excavate commit history.

9. **State what is intentionally out of scope.** Add a short paragraph noting what the project deliberately does NOT do and why. This prevents reviewers from flagging an absent feature as a gap rather than a design choice.

10. **Add a "Keeping this document current" note.** At the end of the document, add one paragraph stating the update policy: the document is updated as part of any PR that changes the architecture — not as a separate maintenance task. This signals to contributors that it is a living document, not a snapshot.

11. **Cross-link from `README.md` and `CONTRIBUTING.md`.** In `README.md`, add a line in the "Getting Started" or "Architecture" section linking to `ARCHITECTURE.md`. In `CONTRIBUTING.md`, add a line recommending new contributors read it before submitting their first PR.

## Validation checklist

- [ ] `ARCHITECTURE.md` exists in the repo root
- [ ] A component diagram (ASCII art or image) shows all major subsystems and their connections
- [ ] Each connection in the diagram is labeled with its protocol or mechanism
- [ ] Each subsystem has a 2–5 sentence description covering role, ownership, and boundaries
- [ ] At least one end-to-end data flow is described as a numbered sequence
- [ ] All external dependencies are listed with protocol, required/optional status, and failure behavior
- [ ] The deployment model is described (topology, Kubernetes permissions if applicable, OS/arch)
- [ ] Extension points are listed (or explicitly stated as "none" if there are none)
- [ ] Key design decisions include at least one sentence of rationale each
- [ ] Out-of-scope items are stated explicitly
- [ ] An update policy paragraph is present at the end of the document
- [ ] `README.md` links to `ARCHITECTURE.md`
- [ ] `CONTRIBUTING.md` recommends reading `ARCHITECTURE.md` before contributing

## Common mistakes

**Writing for experts instead of newcomers** — The primary reader of `ARCHITECTURE.md` is a developer who has never seen the codebase. Avoid jargon that is only understood after reading the code. If a term is project-specific, define it on first use.

**Describing implementation details instead of design** — Statements like "the reconciler uses a `sync.Mutex` to protect the state map" belong in code comments, not in `ARCHITECTURE.md`. The document should describe what the reconciler is responsible for and why it exists — not how it is implemented internally.

**Omitting external dependencies** — TAG Security reviewers specifically look for the list of external systems and the trust model for each. A document that describes internal components in detail but mentions "a database" without naming it, the protocol, or the auth mechanism will be flagged as incomplete.

**Creating a diagram that immediately goes stale** — Diagrams maintained as binary image files (PNG, SVG exported from a tool) are routinely abandoned because updating them requires opening an external tool. Use ASCII art or Mermaid syntax in the Markdown source. Both render in GitHub and can be updated with a text editor.

**Treating it as a one-time deliverable** — Projects that write `ARCHITECTURE.md` once for graduation review and never update it create a document that misleads new contributors within months. The update policy (step 10) and the cross-link from `CONTRIBUTING.md` are the mechanisms that keep it alive; omitting them produces a document that decays.

**Over-documenting to the point of replacement** — `ARCHITECTURE.md` should be readable in 10–15 minutes. If it exceeds ~1500 words of prose (diagrams excluded), it is probably covering implementation details that belong elsewhere. Trim to orientation-level content.

**Missing the "why" for major decisions** — A diagram without rationale tells reviewers what the project does but not whether the design choices are sound. One sentence of rationale per major decision — "we chose a single-process design to simplify deployment for the target user base of small teams" — is far more informative than a detailed description of the implementation.

## Graduation readiness

Graduation criteria satisfied (from the CNCF graduation application):

- **Architecture documentation sufficient for security and scalability review** (Required)

What graduation reviewers specifically check:

1. `ARCHITECTURE.md` exists at the root of the primary repository and is linked from `README.md` — reviewers look for both the file and the cross-reference; a file that exists but is not discoverable is treated as absent
2. The document includes a **component diagram** that shows major subsystems and their communication protocols — TOC reviewers use this to assess whether the project has a coherent design; TAG Security reviewers use it to identify trust boundaries and attack surface
3. **External dependencies are enumerated** with protocol and auth model — TAG Security specifically checks whether the project talks to a database, message queue, cloud API, or Kubernetes API server, what credentials are used, and what happens on unavailability; missing this section is a common TAG Security finding
4. **Design decisions include rationale** — reviewers distinguish between projects that made deliberate, documented trade-offs and projects that accumulated complexity without intent; at least the three most significant design choices should have a sentence of justification
5. The **deployment model** describes namespace permissions and resource requirements if the project runs in Kubernetes — TOC reviewers assess whether the project follows least-privilege; an undocumented requirement for cluster-admin is a red flag
6. The document is **demonstrably current** — reviewers check whether the architecture described matches the current codebase by spot-checking one or two subsystem descriptions against the repo structure; a document that describes a two-year-old architecture while the code has moved on signals poor maintenance hygiene
