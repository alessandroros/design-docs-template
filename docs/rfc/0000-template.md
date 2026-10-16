# RFC: {title}

- Author(s): {names}
- Status: Draft | In review | Approved | Rejected | Implemented
- Created: {YYYY-MM-DD}
- Updated: {YYYY-MM-DD}
- Tracking: {ticket or link}
- Related ADRs: {links, once decisions are accepted}

## Summary

{One paragraph. A reader should understand the proposal from this section alone.}

## Motivation

{The problem, the users who have it, and why it is worth solving now. Include the concrete cases this design has to handle.}

## Goals and non-goals

**Goals**

- {what success looks like}

**Non-goals**

- {a plausible goal you are explicitly not taking on}

Non-goals are reasonable things you choose not to do, not negated qualities such as "the system should not crash".

## Proposed design

{Overview first, then the parts that carry the trade-offs: boundaries, main flows, APIs, data. Explain how it works. Link a diagram when a picture is clearer than a paragraph. Do not paste a full schema that will be stale next week.}

## Alternatives considered

| Alternative | Why it was not chosen |
|-------------|------------------------|
| {option} | {trade-off against the goals} |
| Do nothing | {cost of not doing this} |

## Drawbacks and risks

- Security and privacy: {impact and mitigation}
- Performance and scale: {expected load and behavior}
- Operability: {failure modes, rollout, rollback}
- Compatibility: {migration or deprecation}

## Rollout

{How this reaches production, how you know it worked, and how you undo it.}

## Unresolved questions

- {what review or implementation still has to settle}

---

For a small change, keep Summary, Motivation, Proposed design, and Unresolved questions. Delete the rest.
