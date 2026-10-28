# Example: decide how to migrate a database

Illustrative conversation and output shape only. This is not an executed review or benchmark result.

## Starting request

```text
/magi-review We need to migrate our production database with minimal
interruption. Help define the criteria before choosing an approach.
```

Use `$magi-review` instead of `/magi-review` in Codex. The explicit command matters; a plain request mentioning MAGI is not a substitute for native skill invocation.

The assistant first offers the host-supported model choices and Default (current session inheritance), then clarifies the interruption budget, compatibility needs, migration size, and rollback constraints only where unknown.

## Recommended criteria, before evaluation

| Criterion | Suggested priority | Evidence to seek |
| --- | --- | --- |
| Interruption stays within the user-confirmed budget | Must-have | Measured migration/lock duration on a representative environment |
| Existing clients remain compatible during rollout | Must-have | API/schema contract checks and deployment order |
| Data is preserved and recovery is possible | Must-have | Reconciliation results and a tested recovery procedure |
| Approach adds minimal ongoing maintenance | Preference | Components, operational steps, and ownership compared across alternatives |

The user accepts or edits these suggestions. The assistant then launches the three independent evaluations using the selected model.

## Expected deliverable shape

Before review, the request leaves interruption, compatibility, and recovery requirements unspecified. After review, the deliverable should contain:

- A chosen approach justified against accepted criteria and alternatives.
- Specific evidence-backed findings from each lens; remaining uncertainty stays visible.
- One dispute check if material disagreements exist.
- A Plan with validation prerequisites and rollout milestones.
- An execution Goal describing outcomes, acceptance evidence, permissions, and stop/replan conditions.

The example does not preselect a migration technique or invent successful test results. If the user requested review only, the deliverable ends with the Plan and Goal draft.

## Plan + challenge variant

```text
/magi-review Use plan + challenge for the same migration decision.
Let me choose the primary and challenger models. Recommend criteria first.
```

After acceptance, label the criteria C1–C4 and freeze the reviewed commit plus relevant local changes. The primary model drafts P1… steps using those inputs. A different model receives the same inputs and the exact frozen draft, then returns F1… findings tied to P/C IDs. The coordinator checks each finding against the source and records its disposition and plan change. A proposed test is not evidence that a failure occurred.

Return one corrected Plan, one execution Goal, and the short findings ledger. If the challenger used another commit or changed the interruption budget, reconcile that mismatch before consolidation. If the models require separate hosts, provide a manual handoff packet; do not claim the challenger ran just because its prompt was prepared. This variant is illustrative and has not been live-tested.
