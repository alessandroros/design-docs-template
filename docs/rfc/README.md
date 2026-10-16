# RFCs

An RFC is a design proposal for one change. Write it before implementation, while changing the design is still cheap. Share it early. A draft that gets comments beats a polished document that arrives late.

There is no single upstream file for a software-project RFC the way MADR is the upstream ADR template. [0000-template.md](0000-template.md) follows the shape used by [Rust RFCs](https://github.com/rust-lang/rfcs) and by [design docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/): summary, motivation, the design, alternatives, drawbacks, unresolved questions. The wording here is for a product or service change, not for a language change.

## When to write one

| Situation | What to write |
|-----------|----------------|
| The solution is obvious and the risk is low | Nothing here. Use the ticket. |
| Small change, some ambiguity | Mini RFC: Summary, Motivation, Proposed design, Unresolved questions. Delete the other sections. |
| A feature or architectural change with real trade-offs | The full template. |

A useful RFC shows the alternatives and why they lost. A document that only says "this is how we will implement it" can be skipped in favor of writing the code.

## Lifecycle

1. `Draft` — circulate it.
2. `In review` — comments on the pull request.
3. `Approved` — write any ADRs the decision produced.
4. `Implemented` — update arc42 and the C4 diagrams if the structure changed.
5. `Rejected` — leave the file. Rejected proposals are part of the history.

## Add an RFC

Copy [0000-template.md](0000-template.md) to `NNNN-short-title.md`, starting at `0001`. Link related ADRs from the header once they exist.

## Index

| ID | Title | Status |
|----|-------|--------|
| — | _none yet_ | — |
