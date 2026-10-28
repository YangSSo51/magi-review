# Example: decide how to migrate a database

Illustrative conversation and output shape only. This is not an executed review or benchmark result.

## Starting request

```text
Use MAGI review. We need to migrate our production database with minimal
interruption. Help define the criteria before choosing an approach.
```

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
