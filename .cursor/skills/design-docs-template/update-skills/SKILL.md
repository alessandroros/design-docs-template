---
name: docs-template-update-skills
description: >-
  Refreshes the design-docs-template skill trees in this repo (and optionally
  personal skill dirs) from the GitHub template latest main. Use when the user
  says update-skills, self-update, refresh the docs skills, or pull the latest
  skill from the template. Invoked via design-docs-template.
---

# update-skills — refresh from GitHub

**What:** Overwrite local `design-docs-template` skill copies with the latest from the template repo.  
**When:** “Aggiorna le skill”, “self-update”, after the playbook/template published new commands.  
**Not:** Updating `docs/` or `website/` content; not a git pull of the whole project.

## Process

### 1. Pick the source flavour

Default from context:

| Clue | Source |
| --- | --- |
| Remote / this skill README says OpenMove | `openmove/engineering-design-playbook` |
| Generic template / personal | `alessandroros/design-docs-template` |
| Unclear | Ask once |

Skill path inside the source (identical on all flavours):

`.cursor/skills/design-docs-template`

(Use that tree as the canonical download; it matches `.claude` / `.agents` content.)

### 2. Confirm scope

Default **project only** (all three paths below). Ask only if they mentioned personal install:

- Project: `.cursor/skills/design-docs-template`, `.claude/skills/design-docs-template`, `.agents/skills/design-docs-template`
- Optional personal: `~/.claude/skills/design-docs-template`, `~/.agents/skills/design-docs-template`, and Cursor user/Agent Store `skills/design-docs-template` if clearly available

Do not invent other destinations.

### 3. Download and replace

From the **docs repo root** (create parent dirs if missing):

```bash
npx --yes degit <owner>/<repo>/.cursor/skills/design-docs-template /tmp/design-docs-template-skill
```

Then for each project destination:

```bash
mkdir -p .cursor/skills .claude/skills .agents/skills
rsync -a --delete /tmp/design-docs-template-skill/ .cursor/skills/design-docs-template/
rsync -a --delete /tmp/design-docs-template-skill/ .claude/skills/design-docs-template/
rsync -a --delete /tmp/design-docs-template-skill/ .agents/skills/design-docs-template/
```

If personal was requested, the same `rsync` into those home paths.

Prefer `degit` + `rsync --delete` so removed files disappear. If `degit` fails, report the error; do not half-update one tree only.

### 4. Verify

Check that each updated tree contains `SKILL.md`, `update-skills/SKILL.md`, and `README.md`. Spot-check that OpenMove vs generic flavour in `README.md` matches the source you pulled (OpenMove playbook should mention `openmove/…` in install lines).

### 5. Hand off

List paths updated and source repo. Tell them to start a **new agent chat** or `/reload` (Pi) so the runtime picks up changes. Do not commit unless they ask.

## Hard rules

- Never modify `docs/` or `website/` in this command.
- Never run this as a recursive “update then update again” loop in the same turn.
- Keep all project copies identical after the run.
- If the repo has local uncommitted edits **inside** the skill folders, warn and ask before `--delete`.
