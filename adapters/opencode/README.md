# OpenCode Adapter

Generates a `SKILL.md` + `opencode.json` per skill, organized by domain,
under `adapters/opencode/output/`.

## Usage

```bash
bash adapters/opencode/generate.sh
```

## Output Structure

```
adapters/opencode/output/
  contribution/
    contributing-guide/
      SKILL.md
      opencode.json
  governance/
    ...
  security/
    ...
```

## Installing into an OpenCode project

Copy the output directories into your project's OpenCode skills directory:

```bash
cp -r adapters/opencode/output/* ~/.config/opencode/skills/cncf/
```
