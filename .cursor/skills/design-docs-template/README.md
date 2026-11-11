# Design docs template — agent skills

Agent commands for the **RFC → ADR → arc42 + Starlight** docs stack. Same skill tree is published for **Cursor**, **Claude Code**, **ChatGPT/Codex**, and **Pi** so every agent in the repo gets the same workflow.

## How to use

Invoke the router or name a command:

- `/design-docs-template` — lists commands and dispatches (Cursor / Claude)
- Codex / ChatGPT: pick the skill from the skills list, or ask in plain language
- Pi: `/skill:design-docs-template` (or `/skill:design-docs-template preview`, etc.)
- Or plain language anywhere: “bootstrap a new docs repo”, “new RFC for payments”, “hygiene on RFC-0007”, “close the loop on RFC-0004”, “preview the docs”

| Command | Use it when |
| --- | --- |
| **bootstrap** | You need a **new** docs repository from this template (folders, Starlight site, day-zero pointers). |
| **new-rfc** | A change has real trade-offs and needs a **proposal** before code. |
| **new-adr** | A choice is **settled** and must be recorded (MADR); accepted ADRs are never rewritten. |
| **rfc-hygiene** | A draft RFC got **noisy** after iterations (stale names, diagrams out of sync, dead options). |
| **close-loop** | An RFC is **approved**: draft ADR(s), freeze/link the RFC, checklist of arc42 + C4 updates in the same change. |
| **preview** | You want the Starlight site on **localhost** (sync + `npm run dev`, URL includes `base`). |

Typical path: `bootstrap` → write → `preview` while drafting → `new-rfc` while deciding → `rfc-hygiene` before review → `close-loop` → `new-adr` is often created inside close-loop.

## How to add the skills (per system)

This repo already ships the skill in three project folders (see [Where it lives](#where-it-lives-multi-agent)). Use the sections below when you **install into another repo**, install **only for yourself**, or verify a tool can see them.

Canonical source to copy (any one of these trees — they are identical):

```bash
# from a clone of this template
SRC=.cursor/skills/design-docs-template   # or .claude/... or .agents/...
```

Or from GitHub without cloning the whole template:

```bash
# personal template
gh api repos/alessandroros/design-docs-template/contents/.cursor/skills/design-docs-template \
  --jq '.[]'   # or: git clone --depth 1 and copy the folder

# OpenMove playbook
# openmove/engineering-design-playbook — same path under .cursor/skills/...
```

Simplest: clone the template (or playbook), then copy the folder:

```bash
git clone --depth 1 https://github.com/alessandroros/design-docs-template.git /tmp/ddt
# or: https://github.com/openmove/engineering-design-playbook.git
```

### Cursor

**Project (shared with the team)** — commit into the repo:

```bash
mkdir -p .cursor/skills
cp -R /tmp/ddt/.cursor/skills/design-docs-template .cursor/skills/
git add .cursor/skills/design-docs-template && git commit -m "feat(skills): add design-docs-template"
```

**Personal (all your Cursor projects on this machine)** — Cursor Agent Store / user skills (UI: Cursor Settings → rules/skills, or copy into your user skills location). If you already use a personal Agent Store `skills/` tree, place `design-docs-template/` there.

**Check:** open the project in Cursor → Agent chat → `/design-docs-template` or ask “preview the docs”.

Docs: [Cursor agent skills](https://cursor.com/docs) (project skills under `.cursor/skills/`).

### Claude Code

**Project (shared):**

```bash
mkdir -p .claude/skills
cp -R /tmp/ddt/.claude/skills/design-docs-template .claude/skills/
git add .claude/skills/design-docs-template && git commit -m "feat(skills): add design-docs-template"
```

**Personal (all repos on this machine):**

```bash
mkdir -p ~/.claude/skills
cp -R /tmp/ddt/.claude/skills/design-docs-template ~/.claude/skills/
```

**Check:** from the repo, run Claude Code → `/design-docs-template`. After edits to the skill, start a new session or reload skills if your build requires it.

Docs: [Extend Claude with skills](https://code.claude.com/docs/en/skills) — project path `.claude/skills/<name>/SKILL.md`, personal `~/.claude/skills/`.

### ChatGPT / Codex

Codex discovers **Agent Skills** under `.agents/skills/` (and user `~/.agents/skills/`).

**Project (shared):**

```bash
mkdir -p .agents/skills
cp -R /tmp/ddt/.agents/skills/design-docs-template .agents/skills/
git add .agents/skills/design-docs-template && git commit -m "feat(skills): add design-docs-template"
```

**Personal:**

```bash
mkdir -p ~/.agents/skills
cp -R /tmp/ddt/.agents/skills/design-docs-template ~/.agents/skills/
```

**Check:** start Codex in the repo; confirm `design-docs-template` appears in the skills list, then invoke it or ask in natural language.

Docs: [Build skills (ChatGPT / Codex)](https://learn.chatgpt.com/docs/build-skills) — repo skills in `.agents/skills/`.

### Pi

Pi implements the same Agent Skills layout. Prefer `.agents/skills/` so Codex and Pi share one copy; `.pi/skills/` also works if you only use Pi.

**Project (shared) — recommended (same as Codex):**

```bash
mkdir -p .agents/skills
cp -R /tmp/ddt/.agents/skills/design-docs-template .agents/skills/
git add .agents/skills/design-docs-template && git commit -m "feat(skills): add design-docs-template"
```

**Project (Pi-only path, optional):**

```bash
mkdir -p .pi/skills
cp -R /tmp/ddt/.agents/skills/design-docs-template .pi/skills/
```

**Personal:**

```bash
mkdir -p ~/.agents/skills    # also scanned by Pi
cp -R /tmp/ddt/.agents/skills/design-docs-template ~/.agents/skills/
```

**Check:** run Pi in the repo → `/skill:design-docs-template`. After editing a skill in an active session, `/reload`.

Docs: [Pi skills](https://pi.dev/docs/latest/skills).

### Install everything at once (recommended for templates)

From the repo root, after you have `/tmp/ddt` (or use this repo as source):

```bash
for dest in .cursor/skills .claude/skills .agents/skills; do
  mkdir -p "$dest"
  rsync -a --delete /tmp/ddt/.cursor/skills/design-docs-template/ "$dest/design-docs-template/"
done
```

Keep the three copies identical when you change the skill.

## Where it lives (multi-agent)

| Agent | Project path |
| --- | --- |
| **Cursor** | `.cursor/skills/design-docs-template/` |
| **Claude Code** | `.claude/skills/design-docs-template/` |
| **ChatGPT / Codex** | `.agents/skills/design-docs-template/` |
| **Pi** | `.agents/skills/design-docs-template/` (optional: `.pi/skills/`) |

```text
.cursor/skills/design-docs-template/   ← Cursor
.claude/skills/design-docs-template/   ← Claude Code
.agents/skills/design-docs-template/   ← Codex, Pi, and other Agent Skills clients
  README.md
  SKILL.md           ← router
  bootstrap/
  new-rfc/
  new-adr/
  rfc-hygiene/
  close-loop/
  preview/
```

## Method (one screen)

| You are… | Write | Can it change? |
| --- | --- | --- |
| Still deciding | **RFC** | Yes until accepted, then history |
| Recording a choice | **ADR** | Never edit accepted; supersede with a new ADR |
| Describing the system today | **arc42 + C4** | Yes — update when the RFC closes |

## Template flavours

| Repo | GitHub |
| --- | --- |
| Generic English template | [alessandroros/design-docs-template](https://github.com/alessandroros/design-docs-template) |
| OpenMove playbook | [openmove/engineering-design-playbook](https://github.com/openmove/engineering-design-playbook) |

**bootstrap** clones from the flavour you are standing in (or asks which one).
