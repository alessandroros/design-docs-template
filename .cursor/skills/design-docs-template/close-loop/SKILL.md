---
name: docs-template-close-loop
description: >-
  Closes an approved RFC into the permanent record: drafts ADR(s) for decisions
  it produced, updates RFC status/links, and lists concrete arc42 + C4 sections
  to update in the same change. Use after review when the proposal must become
  history and the system map must catch up. Invoked via design-docs-template.
---

# close-loop — RFC → ADR → arc42

**What:** Turn an approved RFC into ADRs + an arc42/C4 update checklist (and light edits you can do safely).  
**When:** RFC review is done (`Approved` / accepted); implementation or the map must reflect the decision.  
**Not:** Opening a new proposal (**new-rfc**), or a hygiene-only pass (**rfc-hygiene** — run that first if the draft is dirty).

## Process

### 1. Pin the RFC

User names the RFC path or id. Read it fully. Confirm status is approved (or they explicitly want to mark it approved now).

If the text is inconsistent (old names, broken examples), recommend **rfc-hygiene** first and stop unless they say close anyway.

### 2. Extract decisions

List each **decision** the RFC settled (not every design detail). One decision → one ADR candidate. Ambiguous splits: ask once.

For each candidate note: title, options that lost (one line), outcome, consequences / follow-ups called out in the RFC.

### 3. Draft ADRs

For each decision, follow [new-adr/SKILL.md](../new-adr/SKILL.md) (minimal template unless they ask full): create `proposed` or `accepted` per user — default **`accepted`** when closing an already-approved RFC, still ask if unsure.

Link RFC ↔ ADR in both headers/indexes.

### 4. Freeze the RFC

- Set RFC status to `Approved` or `Implemented` per lifecycle in `docs/rfc/README.md` and what they intend next
- Add links to the new ADR ids
- Do not delete alternatives/history inside the RFC; that is the record. Trim only if they also asked for hygiene

### 5. arc42 + C4 checklist

Produce a **concrete** checklist of files/sections to touch (paths that exist in this repo), for example:

- [ ] `docs/architecture/05_building_block_view.md` — …
- [ ] `docs/architecture/diagrams/c4-containers.md` — …
- [ ] `docs/architecture/09_architecture_decisions.md` — link new ADRs
- [ ] …only sections the RFC actually affects

Apply small, obvious link/index updates yourself. Larger narrative rewrites: leave checked items for the human (or do them only if they said “update arc42 too” and the change is clear).

### 6. Hand off

Summarise: ADR paths created, RFC status, remaining arc42 boxes. Remind rule: accepted ADRs are immutable; further change = new ADR + another loop.

## Hard rules

- Same change set should carry ADR + arc42 touches when you edit the map — do not leave “update arc42 someday” with no checklist.
- Do not invent decisions the RFC did not make.
- Rejected RFCs: leave the file; no ADRs unless they ask to record “we will not do X”.
