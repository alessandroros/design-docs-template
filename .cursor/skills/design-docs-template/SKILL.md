---
name: design-docs-template
description: >-
  Router for the design-docs stack (RFC → ADR → arc42 + Starlight). Commands:
  bootstrap, new-rfc, new-adr, rfc-hygiene, close-loop. Use when the user says
  design-docs-template, docs-template, design-docs bootstrap, new RFC/ADR,
  RFC hygiene, close an RFC into ADRs and arc42, or nested docs-template
  commands.
---

# Design docs template

Five commands under one roof. Read the matching child `SKILL.md` and follow it; do not invent a sixth path.

| Command | What it does | Child |
| --- | --- | --- |
| **bootstrap** | Starts a new docs repo from `design-docs-template`: arc42, ADR, RFC folders and a Starlight site ready to publish. Use on day zero so you never rebuild the scaffolding by hand. | [bootstrap/SKILL.md](bootstrap/SKILL.md) |
| **new-rfc** | Adds the next numbered RFC from the project template, wires the index, and leaves a draft ready to fill. Use when a change has real trade-offs and a ticket is not enough. | [new-rfc/SKILL.md](new-rfc/SKILL.md) |
| **new-adr** | Adds the next numbered ADR from the MADR template (minimal by default), status `proposed`, and updates the ADR index. Use when a choice is settled and must not be rewritten later. | [new-adr/SKILL.md](new-adr/SKILL.md) |
| **rfc-hygiene** | Consistency pass on a draft RFC: one canon for names, diagrams, prose, and examples; strips stale noise after many iterations. Use when the RFC still “works” but readers trip on old terms or dead options. | [rfc-hygiene/SKILL.md](rfc-hygiene/SKILL.md) |
| **close-loop** | Closes an approved RFC into the permanent record: draft ADR(s) for the decisions it produced, freeze/point the RFC, and a concrete arc42 + C4 update checklist in the same change. Use when review is done and implementation (or the map) must catch up. | [close-loop/SKILL.md](close-loop/SKILL.md) |

## Dispatch

1. If the user named a command (or a clear synonym: `hygiene`, `clean RFC`, `from template`, `accept RFC`, `scaffold RFC`…), open that child and run it.
2. Otherwise ask once which command. Defaults: **bootstrap** on empty/new docs root; **rfc-hygiene** if an RFC path is in chat; **close-loop** if they say the RFC was approved; **new-rfc** / **new-adr** if they ask to “add” one.
3. After the child finishes, stop. Chain another command only if they ask (typical chain: `rfc-hygiene` → `close-loop`).

## Method (shared)

| Still deciding | **RFC** | Changes until accepted, then history |
| Already decided | **ADR** | Never edit accepted; supersede with a new one |
| What exists today | **arc42 + C4** | Keep current; update in the same change that closes an RFC |

## Template sources

| Flavour | GitHub template |
| --- | --- |
| Personal / generic | `alessandroros/design-docs-template` |
| OpenMove | `openmove/engineering-design-playbook` |

**bootstrap** uses the flavour of *this* repo when already inside one of them; otherwise ask which template to clone from.
