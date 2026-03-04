# Agent Instructions — cncf-skills

## This repo is intentionally minimal

Skills are markdown files. That is the entire design.

**Before adding any file, script, or tooling, ask:** "Can the agent just read the markdown directly?" If yes, do not add the file.

## What you must not do

- Add scripts to transform, render, or pre-process skills for specific tools
- Add per-tool output directories or generated artifacts
- Create boilerplate (generate scripts, render scripts, adapter classes, registries)
- Generate files, tasks, or commits without the user explicitly asking for them
- Write multi-task plans with multiple commits for work that fits in one commit

## The scope test

A new skill is one file. `just check` validates it. Done.

If adding a skill requires more than that, something has gone wrong.

## Adding a new skill

```
1. Create skills/<id>/SKILL.md with valid YAML front-matter + body
2. Run: just check
Done.
```

## Adding support for a new agent tool

Add one section to `adapters/README.md`. Nothing else.

## Repo structure

```
skills/*/SKILL.md          — one file per CNCF community health template
adapters/README.md         — pointer guide for common agent tools; no scripts
schema/skill.schema.json   — JSON Schema for skill front-matter validation
scripts/validate_schema.py — sole tooling artifact; runs locally and in CI
```

## Validation

```bash
just check   # validates all skill front-matter against the schema
```
