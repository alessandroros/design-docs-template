# Design docs template — agent skills

Commands for the **RFC → ADR → arc42 + Starlight** workflow.

## The idea

You only install **this skill**. Then you ask the agent to **bootstrap**: it creates the docs project from the GitHub template (folders, Starlight, and these skills already inside). You do not clone templates by hand to get started.

```text
install skill (once)  →  /design-docs-template → bootstrap  →  repo ready
```

After that, in the new repo: `new-rfc`, `preview`, `rfc-hygiene`, `close-loop`, `update-skills`, …

## Install the skill (once per agent)

Pick your tool. One command. Restart the agent (or open the project) afterward.

Replace the destination if you want the skill **only in the current repo** (see [Project vs personal](#project-vs-personal)).

### Cursor

**Personal** (all projects): put the folder in your Cursor user/Agent Store `skills/design-docs-template/`, or ask Agent: “install the design-docs-template skill for me from `alessandroros/design-docs-template`”.

**This repo only:**

```bash
npx --yes degit alessandroros/design-docs-template/.cursor/skills/design-docs-template .cursor/skills/design-docs-template
```

Then: Agent chat → `/design-docs-template` → **bootstrap**.

### Claude Code

**Personal:**

```bash
npx --yes degit alessandroros/design-docs-template/.claude/skills/design-docs-template ~/.claude/skills/design-docs-template
```

**This repo only:**

```bash
npx --yes degit alessandroros/design-docs-template/.claude/skills/design-docs-template .claude/skills/design-docs-template
```

Then: `/design-docs-template` → **bootstrap**.

Docs: [Claude skills](https://code.claude.com/docs/en/skills).

### ChatGPT / Codex

**Personal:**

```bash
npx --yes degit alessandroros/design-docs-template/.agents/skills/design-docs-template ~/.agents/skills/design-docs-template
```

**This repo only:**

```bash
npx --yes degit alessandroros/design-docs-template/.agents/skills/design-docs-template .agents/skills/design-docs-template
```

Then invoke `design-docs-template` from the skills list → **bootstrap**.

Docs: [Codex / ChatGPT skills](https://learn.chatgpt.com/docs/build-skills).

### Pi

Same path as Codex (recommended):

```bash
npx --yes degit alessandroros/design-docs-template/.agents/skills/design-docs-template ~/.agents/skills/design-docs-template
```

Or project-local: same command into `.agents/skills/design-docs-template`.

Then: `/skill:design-docs-template` → **bootstrap**. Use `/reload` after changing the skill.

Docs: [Pi skills](https://pi.dev/docs/latest/skills).

### OpenMove flavour

If you work on OpenMove docs, swap the GitHub path:

`alessandroros/design-docs-template` → `openmove/engineering-design-playbook`  
(same `.cursor|claude|agents/skills/design-docs-template` suffix).

## Project vs personal

| Scope | Where | When |
| --- | --- | --- |
| **Personal** | `~/.cursor` / Agent Store, `~/.claude/skills`, `~/.agents/skills` | You want **bootstrap** available before any docs repo exists |
| **Project** | `.cursor/skills`, `.claude/skills`, `.agents/skills` in the repo | Team shares the workflow; also what **bootstrap** leaves in a new repo |

**bootstrap** creates the project via GitHub `--template`, so the new repo already contains all three skill paths. You should not need a second install there.

Later, refresh local skill copies with **update-skills** (or `/design-docs-template` → update-skills) instead of re-running `degit` by hand.

## Commands

| Command | What it does |
| --- | --- |
| **bootstrap** | Creates a new docs repo from the GitHub template and rebrands site config. |
| **new-rfc** | Next numbered RFC + index. |
| **new-adr** | Next numbered ADR (MADR) + index. |
| **rfc-hygiene** | Cleans a noisy draft RFC (names, diagrams, examples, stale prose). |
| **close-loop** | Approved RFC → ADR(s) + arc42/C4 checklist. |
| **preview** | Sync + local Starlight; prints URL with `base`. |
| **update-skills** | Pulls the latest skill tree from GitHub into `.cursor` / `.claude` / `.agents`. |

## Method (one screen)

| You are… | Write | Can it change? |
| --- | --- | --- |
| Still deciding | **RFC** | Yes until accepted, then history |
| Recording a choice | **ADR** | Never edit accepted; supersede |
| Describing the system today | **arc42 + C4** | Yes — update when the RFC closes |

## Template repos

| Flavour | GitHub |
| --- | --- |
| Generic | [alessandroros/design-docs-template](https://github.com/alessandroros/design-docs-template) |
| OpenMove | [openmove/engineering-design-playbook](https://github.com/openmove/engineering-design-playbook) |
