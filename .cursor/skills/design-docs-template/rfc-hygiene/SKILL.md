---
name: docs-template-rfc-hygiene
description: >-
  Hygiene pass on a draft RFC: aligns names, Mermaid diagrams, prose, and
  examples to one canon; removes stale noise after iteration so readers are not
  misled. Use before review or close-loop when the RFC grew messy. Invoked via
  design-docs-template.
---

# rfc-hygiene — clean a noisy draft

**What:** Cleanup pass (not a rewrite): one vocabulary, diagrams↔prose↔examples, delete dead options and obsolete “for now”.  
**When:** Long-edited draft; renames landed in one section but not others; before merge or **close-loop**.  
**Not:** Accepting the RFC (**close-loop**) or starting a blank proposal (**new-rfc**).

## Process

### 1. Pin the canon

Read the RFC end-to-end once. Extract the **canon** — current entity names, renames, closed questions, and “source of truth” tables (constraints, From-table, ER, field boxes).

Completion: a short internal list of canonical names and what they replaced. If two sections disagree on the canon, stop and ask (at most two questions).

### 2. Audit against the checklist

Apply every item in [CHECKLIST.md](CHECKLIST.md). Record findings as concrete locations (heading / diagram / table / example id), not vibes.

Completion: every checklist row is either OK or a finding.

### 3. Report, then edit

Present findings first, grouped:

| Severity | Meaning |
| --- | --- |
| **Blocker** | Reader would trust the wrong model (stale name, diagram≠prose, example broken FK) |
| **Noise** | Closed options, dead “Must discuss”, obsolete “for now / later”, duplicate explanations |
| **Nit** | Wording only; meaning already clear |

Then:

- User said only “check / rivedi / hygiene” → stop after the report; wait for apply.
- User said “sistema / fix / clean it / togli il rumore” → apply **Blocker** + **Noise** in the same turn. Leave **Nit** unless they asked for a full polish.

Edits stay proportional: rename, delete stale paragraphs, fix Mermaid edges, repair example tables. No new sections unless a checklist gap forces a one-line pointer (“see RFC-NNNN”).

### 4. Verify

Re-scan the touched headings and diagrams. Confirm:

- no old name left where the canon forbids it (search the file)
- every Mermaid entity in the overview still has a home in prose or an explicit “unchanged → other RFC” line
- examples still compile against the ER

If the repo syncs docs into a site (`website/scripts/sync-docs.mjs` or equivalent), run sync after edits when a local preview is in use.

Completion: report what changed (bullet list) and what was left as Nit or open question.

## Hard rules

- Prefer **delete** over “comment that this is outdated”.
- Prefer **one term** everywhere; put the old name only in an explicit rename/From table.
- Accepted / frozen RFCs: hygiene is read-only unless the user explicitly reopens them — say so and offer **close-loop** / new ADR + arc42 instead.
- Do not expand scope into new entities or reopening closed Qs unless the inconsistency proves the close was never reflected in the text.
