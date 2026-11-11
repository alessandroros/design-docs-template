# Design docs template — Cursor skills

Agent commands for the **RFC → ADR → arc42 + Starlight** docs stack. They live in this folder so anyone who clones the template (or a project born from it) gets the same workflow in Cursor.

## How to use

In Cursor Agent chat, invoke the router or name a command:

- `/design-docs-template` — lists commands and dispatches
- Or say what you want in plain language, e.g. “bootstrap a new docs repo”, “new RFC for payments”, “hygiene on RFC-0007”, “close the loop on RFC-0004”

| Command | Use it when |
| --- | --- |
| **bootstrap** | You need a **new** docs repository from this template (folders, Starlight site, day-zero pointers). |
| **new-rfc** | A change has real trade-offs and needs a **proposal** before code. |
| **new-adr** | A choice is **settled** and must be recorded (MADR); accepted ADRs are never rewritten. |
| **rfc-hygiene** | A draft RFC got **noisy** after iterations (stale names, diagrams out of sync, dead options). |
| **close-loop** | An RFC is **approved**: draft ADR(s), freeze/link the RFC, checklist of arc42 + C4 updates in the same change. |

Typical path: `bootstrap` → write → `new-rfc` while deciding → `rfc-hygiene` before review → `close-loop` → `new-adr` is often created for you inside close-loop.

## Where the files are

```text
.cursor/skills/design-docs-template/
  README.md          ← this guide (humans)
  SKILL.md           ← router (agents)
  bootstrap/
  new-rfc/
  new-adr/
  rfc-hygiene/
  close-loop/
```

Cursor loads project skills from `.cursor/skills/`. Keep this tree in the template repo so new projects inherit it.

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
