---
name: docs-template-new-adr
description: >-
  Scaffolds the next numbered ADR from the MADR template (minimal by default),
  status proposed, and updates the ADR index. Use when a decision is settled and
  must be recorded immutably. Invoked via design-docs-template.
---

# new-adr — record one decision

**What:** Next `docs/adr/NNNN-slug.md` from MADR + index row, status `proposed`.  
**When:** The choice is made (often after an RFC); you need a permanent record.  
**Not:** Comparing designs still in flight (that is **new-rfc**) or closing a whole RFC (**close-loop**, which may call this).

## Process

### 1. Locate templates

- Default: `docs/adr/adr-template-minimal.md`
- Full trade-off write-up: `docs/adr/adr-template.md` if they ask
- Read `docs/adr/README.md` for numbering and “do not edit 0000 / upstream templates”

If `docs/adr/` is missing, stop and suggest **bootstrap**.

### 2. Collect inputs

Ask what is missing:

- **Decision title** (short, imperative or noun phrase per repo style) and **slug**
- **Minimal vs full** template (default minimal)
- **Context one-liner** if they already have it (optional — else leave template placeholders)
- **Supersedes ADR-NNNN?** optional

### 3. Pick NNNN

List `docs/adr/[0-9]*.md`. Keep `0000` as the MADR meta-ADR; next id = max of numeric ids + 1 (if only `0000`, next is `0001`).

### 4. Write the file

- Copy chosen template to `docs/adr/NNNN-<slug>.md`
- Status: `proposed`
- Fill title; leave options/consequences as template structure unless the user dictated the outcome in this turn
- If superseding: set old ADR status to `superseded by ADR-NNNN` only when they confirmed the old id

### 5. Index

Add a row to `docs/adr/README.md`. Do **not** mark arc42 §9 updated until **close-loop** or they ask — linking from §9 on acceptance is a separate step.

### 6. Hand off

Report path, id, status. Remind: accepted ADRs are never rewritten; a later change needs a new ADR.

## Hard rules

- Do not edit `adr-template.md`, `adr-template-minimal.md`, or rewrite accepted ADRs.
- One ADR = one decision. Split if they bundled several.
- Prefer empty honest placeholders over invented rationale.
