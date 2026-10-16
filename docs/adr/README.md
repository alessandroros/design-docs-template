# Architecture decision records

Format: [MADR 4.0.0](https://adr.github.io/madr/). The files `adr-template.md`, `adr-template-minimal.md`, and `0000-use-markdown-architectural-decision-records.md` are the upstream templates. Do not edit those three except to record a real decision in `0000` if this project ever stops using MADR.

## Which template

| File | Use it when |
|------|-------------|
| [adr-template-minimal.md](adr-template-minimal.md) | Most decisions. Context, options, outcome, consequences. |
| [adr-template.md](adr-template.md) | The trade-off needs drivers, a per-option pros/cons list, and links. |

## Add a decision

1. Copy the template to `NNNN-short-title.md`. `NNNN` is the next number, starting at `0001`.
2. Status starts as `proposed`.
3. Open a pull request. Review the decision there.
4. On acceptance, set status to `accepted` and link the ADR from [section 9](../architecture/09_architecture_decisions.md).
5. If the decision changes the structure, update the building block view and the C4 diagrams in the same change.

## Change a decision

Do not rewrite an accepted ADR. Add a new one and set the old status to `superseded by ADR-NNNN`.

An ADR is one decision. If you are still comparing designs, describing APIs, and planning a rollout, that is an [RFC](../rfc/README.md). The RFC can produce one or more ADRs once the choice is made.

## Index

| ID | Title | Status |
|----|-------|--------|
| [0000](0000-use-markdown-architectural-decision-records.md) | Use Markdown Architectural Decision Records | accepted |
