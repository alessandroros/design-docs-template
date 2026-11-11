---
name: docs-template-new-rfc
description: >-
  Scaffolds the next numbered RFC from the repo's RFC template, updates the RFC
  index, and leaves a Draft ready to write. Use when a change has real
  trade-offs and needs a proposal before code. Invoked via design-docs-template.
---

# new-rfc — scaffold a proposal

**What:** Next `docs/rfc/NNNN-slug.md` from the project template + index row.  
**When:** Non-obvious design, alternatives matter, you want review before build.  
**Not:** Recording a settled decision (that is **new-adr**) or cleaning an existing draft (**rfc-hygiene**).

## Process

### 1. Locate templates

In the current docs repo (not the upstream template unless this *is* that repo):

- Prefer `docs/rfc/0000-template.md` (or the README’s named template)
- Read `docs/rfc/README.md` for numbering and index conventions

If no RFC folder exists, stop and suggest **bootstrap** (or confirm creating `docs/rfc/` from the upstream template).

### 2. Collect inputs

Ask what is missing:

- **Title** (human) and **slug** (kebab-case filename fragment)
- **Full vs mini** — mini = Summary, Motivation, Proposed design, Unresolved questions only (per README)
- **Related ADR/RFC ids** if known (optional)

### 3. Pick NNNN

List existing `docs/rfc/[0-9]*.md`, ignore `0000-*` templates. Next id = max+1, zero-padded to 4 digits, starting at `0001` if none.

### 4. Write the file

- Copy the template to `docs/rfc/NNNN-<slug>.md`
- Set title, id, status `Draft` (or the repo’s equivalent)
- For mini: delete sections the README says to drop
- Do **not** invent the design body; leave template headings for the author

### 5. Index

Add a row to the RFC index in `docs/rfc/README.md` (and any root docs index that lists RFCs).

### 6. Hand off

Report path, id, status, and that the body is still empty on purpose. Offer **rfc-hygiene** only after they have iterated.

## Hard rules

- Never overwrite an existing `NNNN-*` without explicit confirm.
- Do not fill Motivation/Design with guessed product content.
- One RFC = one change proposal; split if they describe two unrelated changes.
