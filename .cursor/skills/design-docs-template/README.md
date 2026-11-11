# Design docs template — agent skills

Agent commands for the **RFC → ADR → arc42 + Starlight** docs stack. Same skill tree is published for **Cursor**, **Claude Code**, **ChatGPT/Codex**, and **Pi** so every agent in the repo gets the same workflow.

## How to use

Invoke the router or name a command:

- `/design-docs-template` — lists commands and dispatches
- Or plain language: “bootstrap a new docs repo”, “new RFC for payments”, “hygiene on RFC-0007”, “close the loop on RFC-0004”, “preview the docs”

| Command | Use it when |
| --- | --- |
| **bootstrap** | You need a **new** docs repository from this template (folders, Starlight site, day-zero pointers). |
| **new-rfc** | A change has real trade-offs and needs a **proposal** before code. |
| **new-adr** | A choice is **settled** and must be recorded (MADR); accepted ADRs are never rewritten. |
| **rfc-hygiene** | A draft RFC got **noisy** after iterations (stale names, diagrams out of sync, dead options). |
| **close-loop** | An RFC is **approved**: draft ADR(s), freeze/link the RFC, checklist of arc42 + C4 updates in the same change. |
| **preview** | You want the Starlight site on **localhost** (sync + `npm run dev`, URL includes `base`). |

Typical path: `bootstrap` → write → `preview` while drafting → `new-rfc` while deciding → `rfc-hygiene` before review → `close-loop` → `new-adr` is often created inside close-loop.

## Where it lives (multi-agent)

One skill directory, copied to each tool’s project path (keep the copies identical):

| Agent | Project path |
| --- | --- |
| **Cursor** | `.cursor/skills/design-docs-template/` |
| **Claude Code** | `.claude/skills/design-docs-template/` |
| **ChatGPT / Codex** | `.agents/skills/design-docs-template/` |
| **Pi** | `.agents/skills/design-docs-template/` (also discovers `.pi/skills/` if you prefer) |

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

After editing the skill, update **all three** project copies (or re-run your sync from the canonical tree). Do not diverge the copies.

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
