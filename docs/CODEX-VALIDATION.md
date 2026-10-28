# Codex workflow trial — 2026-10-28

This is a coordinator-authored record of one observed run, not a raw execution trace or a benchmark. It tests workflow continuity in a Codex desktop chat. It does not establish general reliability, accuracy gains, or Claude Code compatibility at runtime.

## Inputs and scope

- Baseline: commit `62427a979a098bf410e9321649ca4fad63783ac3`, plus the user's requested removal of ACKNOWLEDGMENTS and its README links.
- Subject: MAGI Review's readiness for public use and its actual Codex workflow.
- The coordinator read the installed explicit-only skill manually; native skill selector discovery was not exercised.
- Model choices and Default were presented first. An unrelated answer to the model question was not treated as a selection; the coordinator asked again.
- User explicitly selected `gpt-6.1-sol / high` and accepted the five proposed criteria before evaluator launch.

## Accepted criteria

| Criterion | Evidence observed |
| --- | --- |
| Model choice reaches all evaluators | Three accepted spawn calls with `agent_type=default`, `model=gpt-6.1-sol`, `reasoning_effort=high`, `fork_turns=none`. |
| Criteria are accepted before evaluation | User selection and acceptance preceded all three calls. |
| Independent first-pass evaluation | Each received the same neutral brief and one lens; no parent conversation or peer results were supplied. All three returned separate reports. |
| Findings lead to evidence checks, Plan, and Goal | Partial installation failure was reproduced, a repair Plan was stated, `get_goal` returned null, and `create_goal` returned an active native Goal. |
| Checks and publication claims stay scoped | Local test commands/results and the remaining runtime limits are documented below; publication is checked against the remote commit after pushing. |

## Three evaluator reports

| Evaluator | Lens | Independent result |
| --- | --- | --- |
| `magi_purpose` | Purpose/value | Retain the shared criteria and three-lens design; add session-refresh/discovery guidance for Python installs as well as manual installs. |
| `magi_correctness` | Correctness/safety | P2: a mid-copy error can leave SKILL.md present without explicit-only metadata, and the remaining folder blocks retry. Add failure-path verification. |
| `magi_simplicity` | Simplicity/operability | Independently identified the same partial-install/retry defect; keep the small instruction package and fix failure recovery rather than adding an orchestrator. |

All three disclosed that they could not independently attest their backend model ID or effective effort. Launch arguments are the observable configuration evidence, not proof of a pinned backend deployment. The reports were read-only; no child delegation was requested or observed.

There was no material conflict between recommendations, so peer debate was skipped under the skill's conditional cross-check rule. The coordinator checked the shared finding against the installer and reproduced it with an injected copy error: target and SKILL.md remained while the Codex policy file was absent. The new regression checks failed before the fix. This validates the no-dispute path, not a live disagreement-resolution round.

## Plan and execution Goal

Plan stated before repair:

1. Reproduce the partial-install failure with a focused check.
2. Fix incomplete-install cleanup and installation-discovery guidance.
3. Run focused checks and record only observed runtime evidence.
4. Review and publish the authorized changes, preserving existing global Git account settings.

Native Goal registration succeeded after `get_goal` returned no existing Goal. The registered objective required three isolated configured evaluator calls, evidence-backed corrections and passing regressions, accurate runtime documentation, removal of ACKNOWLEDGMENTS, and verified publication. It excluded Claude live testing, model/account changes without authorization, and claims of selector discovery. No token budget was requested or set. The coordinator's app mode was not changed by writing the Plan.

The Goal remains active until required checks and remote publication are verified; final completion is reported by the coordinator after publication. This report does not claim a pre-publication completion event.

## Repair and local checks

- Write supporting assets before publishing SKILL.md through a temporary file rename.
- On failure, clean up the newly created installation at its original resolved location. Existing destinations are still refused. A cleanup failure reports the incomplete path rather than claiming success.
- Add tests for copy failure with safe retry and for a manifest remaining undiscoverable until supporting files are ready.
- Add common session-refresh/selector guidance for both installation methods.
- Command: `python -m unittest discover -s tests -v` — all 5 tests passed after the fix; the two new regressions failed on both host variants before it.
- CLI smoke checks installed both host variants in temporary folders and verified that a repeated install refused the destination without changing its files. These are installer checks, not Claude model execution.
- A post-fix read-only review by the original correctness evaluator found no additional material blocker. It reviewed the source, tests, and evidence claims; it did not independently rerun tests or attest model/publication results.

## Limits

Only the explicit `gpt-6.1-sol/high` path was exercised. Default inheritance, alternate models, sequential scheduling, unavailable-capability handling, and actual peer disputes were not tested. Native selector discovery and Claude Code model execution remain untested. No comparative quality, cost, or latency study was performed. Run evidence is summarized here without private conversation transcripts, credentials, or machine-specific paths.
