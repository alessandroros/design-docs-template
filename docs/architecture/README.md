# Architecture

This folder is the [arc42](https://arc42.org/overview/) template, version 9.0, English, plain. Each file is one section. Help for what belongs in a section is at [docs.arc42.org](https://docs.arc42.org/), not inlined here.

| File | Section | Fill when |
|------|---------|-----------|
| [01_introduction_and_goals.md](01_introduction_and_goals.md) | Goals, quality, stakeholders | First |
| [02_architecture_constraints.md](02_architecture_constraints.md) | Constraints you cannot choose | When you know them |
| [03_context_and_scope.md](03_context_and_scope.md) | Actors and external systems | First, with the [context diagram](diagrams/c4-context.md) |
| [04_solution_strategy.md](04_solution_strategy.md) | How the design meets the quality goals | First, half a page |
| [05_building_block_view.md](05_building_block_view.md) | Static structure | First, with the [container diagram](diagrams/c4-containers.md) |
| [06_runtime_view.md](06_runtime_view.md) | Important runtime scenarios | When a flow is non-obvious |
| [07_deployment_view.md](07_deployment_view.md) | Where it runs | When deploy is decided |
| [08_concepts.md](08_concepts.md) | Cross-cutting concepts | As they appear |
| [09_architecture_decisions.md](09_architecture_decisions.md) | Index of decisions | Link to accepted ADRs in [`../adr/README.md`](../adr/README.md) |
| [10_quality_requirements.md](10_quality_requirements.md) | Quality tree and scenarios | When section 1 is not enough |
| [11_technical_risks.md](11_technical_risks.md) | Risks and technical debt | When you know them |
| [12_glossary.md](12_glossary.md) | Domain language | As terms stabilize |

Prefer relevance over completeness. Describe the building blocks that are important, surprising, risky, or volatile. Leave out the boring ones.

## Diagrams

[C4](https://c4model.com/) in Mermaid, so the diagrams render on GitHub:

- Context diagram → section 3
- Container diagram → section 5, level 1
- Add a dynamic diagram next to section 6 when a runtime scenario needs one

## Decisions

Do not rewrite a decision into section 9. Record it as an ADR and link it. Section 4 may summarize the few decisions that define the strategy, and point at the same ADRs.
