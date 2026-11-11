# RFC hygiene checklist

Use with [SKILL.md](SKILL.md). Every row: OK or a finding with location.

## Names

- [ ] One current name per concept in prose, headings, Mermaid, field boxes, and examples
- [ ] Old names appear only in an explicit rename / From / mapping table
- [ ] Status enums and extension labels match the constraints section (no orphan statuses)

## Structure vs diagrams

- [ ] Full ER (or main graph) edges match the relationship list claimed in prose
- [ ] Simplified / split diagrams cover the same relationship set they advertise (no silent drops)
- [ ] Entities shown only in one place are intentional; “unchanged → other RFC” is stated where fields are omitted

## Examples

- [ ] Example tables use current entity names and real FK targets from the ER
- [ ] Graph nodes in family / walkthrough examples exist as tables (or are explicitly out of scope)
- [ ] Counts and “after usage” deltas still match the narrative (no leftover pre-rename rows)

## Noise

- [ ] Closed “Must discuss” / open questions are not still framed as open at the top
- [ ] Discarded options are gone or collapsed to one line in an Alternatives / rejected table
- [ ] “For now”, “later”, “temporary”, “TODO” that the later text already resolved are removed
- [ ] Duplicate explanations of the same rule are merged (keep the sharpest)

## Cross-doc (when a family is in scope)

- [ ] This RFC’s renames are not contradicted by sibling RFCs it claims to supersede or extend
- [ ] Pointers to other RFCs resolve to the right section names
- [ ] Shared examples (same people / accounts / packages) stay consistent across files or are marked as variants

## Reader path

- [ ] A new reader can learn the model from constraints → ER → entities → examples without hitting a stale name first
- [ ] Index / README links still match titles and paths
