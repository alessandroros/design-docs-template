# Design docs template

A generic, English starting point for technical design documentation of a software project. It does not invent a format. It vendors the templates teams already use, and explains when to use each one.

| Question | Document | Where |
|----------|----------|--------|
| What is the system, and how is it shaped? | [arc42](https://arc42.org/) architecture documentation | [`docs/architecture/`](docs/architecture/) |
| Why did we choose this, for good? | [MADR](https://adr.github.io/madr/) architecture decision record | [`docs/adr/`](docs/adr/) |
| How should we build this change? | RFC / design doc | [`docs/rfc/`](docs/rfc/) |
| How do the pieces fit, visually? | [C4](https://c4model.com/) diagrams in Mermaid | [`docs/architecture/diagrams/`](docs/architecture/diagrams/) |

Upstream files are copied in, not rewritten. See [NOTICES.md](NOTICES.md).

## Use this repository as a template

On GitHub, open this repository and choose **Use this template**.

Or from the CLI:

```bash
gh repo create my-project --template alessandroros/design-docs-template --private
```

Then, in the new project:

1. Fill [`docs/architecture/01_introduction_and_goals.md`](docs/architecture/01_introduction_and_goals.md): business goals, the top quality goals as measurable scenarios, stakeholders.
2. Fill context, solution strategy, and the building block view (sections 3, 4, and 5). Leave the other arc42 sections empty until you have something real to write.
3. Replace the placeholder names in the [C4 diagrams](docs/architecture/diagrams/).
4. Keep [`docs/adr/0000-use-markdown-architectural-decision-records.md`](docs/adr/0000-use-markdown-architectural-decision-records.md). It records that this project uses MADR. Add further decisions as `0001-…`, `0002-…`.
5. Write an RFC only when a change is ambiguous enough to need a design review.

## How the three documents work together

An **RFC** is a proposal. You write it before implementing, while the design can still change. Reviewers comment, the text moves, and when the work ships the RFC is history.

An **ADR** is a closed decision. One question, one file, kept next to the code. You do not edit an accepted ADR to change the decision. You add a new ADR and mark the old one `superseded by ADR-NNNN`.

**arc42** is the map of the system as it is. Section 9 points at the ADRs. An accepted RFC that changes the structure should update the relevant arc42 section and the C4 diagrams. The RFC does not replace the architecture document.

```text
RFC  (proposal, mutable while in review)
  └─ may produce one or more ADRs  (immutable decisions)
        └─ are indexed from arc42 section 9
              └─ arc42 sections 3 and 5 stay in sync with the C4 diagrams
```

Skip the RFC when the solution is obvious and the risk is low. A ticket with acceptance criteria is enough.

## What to fill first

For a new system, stop after this. Do not fill all twelve arc42 sections on day one.

1. Section 1 — goals and quality scenarios
2. Section 3 — context and scope, plus the context diagram
3. Section 4 — solution strategy, half a page
4. Section 5 — building blocks, plus the container diagram
5. The first real ADRs (stack, persistence, boundaries, deploy), after `0000`

Add runtime, deployment, cross-cutting concepts, quality scenarios in depth, risks, and the glossary when those topics become real.

## Further reading

- [arc42 overview](https://arc42.org/overview/) and [section docs](https://docs.arc42.org/)
- [MADR](https://adr.github.io/madr/)
- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), Michael Nygard
- [The C4 model](https://c4model.com/)
- [Design docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/), the practice this RFC shape follows
