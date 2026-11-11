# Design docs template

Three documents, one rule: **separate what changes from what must not change.**

Reading view: [alessandroros.github.io/design-docs-template](https://alessandroros.github.io/design-docs-template/).

## The method in 30 seconds

Before you write anything, ask one question: *is this still being decided, already decided, or describing what exists?*

| You are… | Write | When | Can it change? |
|----------|-------|------|----------------|
| Still convincing people | **RFC** — a proposal | Before building | Yes, while in review. Then it is history. |
| Recording a choice | **ADR** — one decision | The moment you decide | Never. A new ADR supersedes it. |
| Describing the system today | **arc42** — the map | Continuously | Yes, always kept current. |

They form a chain. Skipping the last step is how documentation rots.

```mermaid
flowchart LR
  work["New work"] --> q{"Is the solution<br/>obvious?"}
  q -->|yes| ticket["Ticket"]
  q -->|no| rfc["RFC<br/>propose and review"]
  rfc --> adr["ADR<br/>record each decision"]
  adr --> arc["arc42 + C4<br/>update the map"]
  ticket --> arc
```

## Why

Without this split, every project hits the same three problems:

- **Nobody remembers why.** Six months in, the reason for a choice left with the person who made it. ADRs keep the reason next to the code.
- **The architecture doc is stale.** One big document is too expensive to keep current, so nobody does. arc42 splits it into sections, so you update only the one that changed.
- **The same debate happens twice.** Discussions buried in chat get repeated. An RFC keeps the proposal, the alternatives, and why they lost in one place.

## Three rules

1. **Never edit an accepted ADR.** It is a record of what was true when you decided, like a commit. If the decision changes, write a new ADR and mark the old one `superseded by ADR-NNNN`.
2. **Close the loop.** An implemented RFC is not documentation of the system. Update the arc42 section and the C4 diagram it touched, in the same change.
3. **Skip the RFC when the answer is obvious.** If there are no trade-offs, a ticket is enough. An RFC that only says "here is how we will build it" is overhead.

## See it on a real-looking project

**[design-docs-example](https://github.com/alessandroros/design-docs-example)** — CityCycle, a fictional bike-sharing service. It walks the whole chain: initial architecture, two founding ADRs, an RFC that adds electric bikes, and the ADR that RFC produced. Read it once before starting your own.

## Start a project

```bash
gh repo create my-project --template alessandroros/design-docs-template --private
```

Or choose **Use this template** on GitHub.

In [Cursor](https://cursor.com/), you can also run the **bootstrap** agent skill (see [Agent skills](#agent-skills) below).

On day one, fill only this. Leave the other arc42 sections empty until there is something real to write.

1. [Section 1](docs/architecture/01_introduction_and_goals.md) — goals, and the top three quality goals as measurable scenarios
2. [Section 3](docs/architecture/03_context_and_scope.md) and the [context diagram](docs/architecture/diagrams/c4-context.md) — who and what the system talks to
3. [Section 4](docs/architecture/04_solution_strategy.md) — half a page on how the design meets those goals
4. [Section 5](docs/architecture/05_building_block_view.md) and the [container diagram](docs/architecture/diagrams/c4-containers.md) — the deployable pieces
5. The first ADRs — stack, persistence, boundaries, deploy

## What is inside

```text
docs/
  architecture/   arc42 9.0, one file per section, plus C4 diagrams in Mermaid
  adr/            MADR 4.0 templates and ADR 0000 (we use MADR)
  rfc/            RFC template, full and mini
website/          Starlight site that renders docs/ for GitHub Pages
.cursor/skills/   Cursor agent skills for this docs workflow
.claude/skills/   Claude Code skills (same tree)
.agents/skills/   ChatGPT/Codex and Pi skills (same tree)
```

`docs/` is the source. Edit and review the Markdown there. `website/` only turns it into the reading view; to preview it locally, run `npm install` and `npm run dev` inside `website/`.

The arc42 and MADR files are the official upstream templates, copied in unchanged. Nothing here is a new format. See [NOTICES.md](NOTICES.md) for sources and licenses.

How each folder works: [architecture](docs/architecture/README.md) · [ADRs](docs/adr/README.md) · [RFCs](docs/rfc/README.md)

## Agent skills

This template ships the same skill tree for **Cursor**, **Claude Code**, **ChatGPT/Codex**, and **Pi**:

| Agent | Path |
| --- | --- |
| Cursor | [`.cursor/skills/design-docs-template/`](.cursor/skills/design-docs-template/) |
| Claude Code | [`.claude/skills/design-docs-template/`](.claude/skills/design-docs-template/) |
| ChatGPT / Codex / Pi | [`.agents/skills/design-docs-template/`](.agents/skills/design-docs-template/) |

Full usage notes (commands **and how to install per tool**): [skills README](.cursor/skills/design-docs-template/README.md) (identical in the other two trees).

In agent chat, run `/design-docs-template` or ask in plain language. To add the skills to another repo or only for yourself, follow the **How to add the skills (per system)** section in that README (Cursor, Claude Code, ChatGPT/Codex, Pi).

| Command | What it does |
| --- | --- |
| **bootstrap** | Create a new docs repo from this template (arc42, ADR, RFC, Starlight) and rebrand the site config. Day zero — do not rebuild the scaffolding by hand. |
| **new-rfc** | Add the next numbered RFC from the project template and update the index. Use when a change has real trade-offs and a ticket is not enough. |
| **new-adr** | Add the next numbered ADR (MADR, minimal by default), status `proposed`, and update the index. Use when a choice is settled and must not be rewritten later. |
| **rfc-hygiene** | Consistency pass on a draft RFC: one canon for names, diagrams, prose, and examples; strip stale noise after many iterations. |
| **close-loop** | Close an approved RFC: draft ADR(s), freeze/link the RFC, and a concrete arc42 + C4 update checklist in the same change. |
| **preview** | Sync `docs/` into Starlight and start the local server; report the Local URL with the configured `base` path. |

Typical path: **bootstrap** → write → **preview** while drafting → **new-rfc** while deciding → **rfc-hygiene** before review → **close-loop** when approved.

## Further reading

- [arc42](https://arc42.org/overview/) and its [section docs](https://docs.arc42.org/)
- [MADR](https://adr.github.io/madr/)
- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), Michael Nygard
- [The C4 model](https://c4model.com/)
- [Design docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)
