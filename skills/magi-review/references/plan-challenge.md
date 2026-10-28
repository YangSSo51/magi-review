# Plan + challenge

Load only for the user's selected plan + challenge mode. Apply the shared model selection, criteria acceptance, source-freezing, permissions, and Plan/Goal rules in SKILL.md. This mode uses two model roles, not three lens evaluators or an extra judge agent. It is a procedural option, not a measured quality improvement.

## Shared contract

Before either role starts, provide both with the same neutral problem, purpose, scope/non-goals, accepted C1… criteria, priorities, expected evidence, and source snapshot. Include relevant dirty/untracked content in the snapshot; do not discard user work to make a clean commit. State runtime assumptions and what checks are authorized. Both roles are read-only and may not delegate. A review request does not authorize implementation or expensive experiments.

For same-host and cross-host runs alike, record a reviewed-file manifest with content hashes (plus relevant dirty diff/untracked-input identities), a criteria version, and then a draft version. Check source hashes and criterion identity immediately before the planner, before the challenger, and before consolidation. Files added to the review scope must be included in the manifest before their evidence is compared. A live working directory is not an immutable snapshot: if checks differ or cannot be performed, reconcile the inputs or report a partial review rather than asserting an unchanged baseline.

The planner and challenger use different user-selected model identities. Minimum selection evidence is two distinct exact supported model IDs, or two supported aliases that the host defines as different model families, with their configured launch/selection evidence. Record requested and observed identity/effort and disclose unreported backend versions; this is not backend attestation. An unresolved Default or aliases that may resolve to the same model do not meet this minimum: resolve them or ask for supported alternatives. If runtime evidence reports the same effective model for both roles, stop rather than mark cross-model review complete. Do not claim that using two models provides independent proof.

## 1. Primary plan

Run the planner once. Return one draft with claim/step IDs (P1, P2, …), source evidence, assumptions, proposed changes, alternatives/tradeoffs, criterion mappings, milestones, and completion checks. Mark existing functionality versus proposed functionality. Do not design only around a guessed failure or treat an unexecuted check as evidence.

The selected planner may be the current coordinator only if its model matches the user's selection with runtime/inheritance evidence. Otherwise use a fresh role context with the selected model. No specialist model substitution or conversation fork that overrides the choice.

Freeze this draft as the review target. A later revision must remain distinguishable from what the challenger actually reviewed.

## 2. Different-model challenge

Give a fresh challenger context the same shared contract and source access **plus the exact frozen primary draft**. Seeing the draft is intentional here; this is critique, not three-lens blind first-pass evaluation. Do not supply the planner's private reasoning, unrelated conversation history, a preferred verdict, or the coordinator's suspected mistakes.

Ask for decision-changing problems: unsupported or false claims, concrete counterexamples, missing failure paths, violated C criteria/contracts, and unnecessary changes where a smaller solution is supported. Verify against the source rather than merely repeating or rewriting the draft. Do not demand dissent or a finding quota. An alternative is useful only when evidence shows why the challenged step needs it.

Each finding F1… identifies the P claim/step and C criterion, source/version/location, triggering condition or counterexample, impact, and the smallest correction or missing evidence. Distinguish facts, assumptions, user preferences, and proposed tests. If source access is unavailable or the snapshot differs, report that limitation and withhold a source-verified verdict.

## 3. One evidence-based consolidation

The coordinator checks each material finding against the frozen source and already-authorized focused checks. Assign a disposition:

| Disposition | Meaning and effect on the final plan |
| --- | --- |
| Confirmed | Source/check evidence supports it; amend the affected plan step. |
| Conditional | Valid under a stated condition; make the branch or prerequisite explicit. |
| Rejected | Contrary source/check evidence resolves it; retain the justified step and explain why. |
| Insufficient evidence | Not resolved; retain the uncertainty and name the evidence needed. Do not mark the criterion satisfied. |

Show a short ledger: finding → challenged claim/criterion → disposition → evidence → resulting plan change. Resolve facts by evidence, not model reputation, vote, confident wording, or forced agreement. A substantiated must-have violation blocks unconditional readiness. An unresolved fact can become an explicit verification prerequisite; an unresolved material preference requires a user decision. Do not blend incompatible alternative plans into an implementation sequence.

Use at most one focused clarification exchange with the original planner or challenger responsible for the disputed claim, if it would change the decision and that role context can be resumed. Include the same snapshot, criteria and frozen draft IDs; append the clarification without overwriting the review target. A changed draft gets a new version and its affected critique becomes stale until reconciled. Otherwise perform the source-based coordinator check and disclose no peer follow-up. Do not silently spawn more evaluators or repeat the full review when there is no new evidence.

Produce **one final Plan** identifying which draft steps changed, why, and which uncertainty remains, followed by **one execution Goal** under SKILL.md section 5. The draft and critique are review evidence, not competing execution plans. Neither critic nor planner approval is permission to implement, register a native Goal, or publish.

## Cross-host use

If one host cannot run both selected models (for example, a Claude model and a Codex model), disclose that limitation before starting the two-role workflow. Offer a manual handoff, use an available second-host tool/CLI when the user has authorized that execution, or ask the user to select two models supported by the current host. Do not pretend this skill supplies a provider router or silently fall back to two runs of the same model. A tool-assisted handoff must preserve the selected models, fresh role context, frozen inputs, and read-only boundaries; verify the returned execution evidence rather than treating a successful command launch as a completed review.

For either handoff, provide a packet with: role/model choices; neutral brief; exact source manifest including relevant dirty/untracked inputs; accepted criteria/version; authorized checks; and the frozen primary draft for the challenger. For a manual handoff the user transports it; for an authorized tool-assisted handoff the coordinator supplies the same approved inputs to the second host. The authorization must cover execution and the source/artifacts exposed to that host/provider; reuse clear authorization already given for this review rather than asking again. Permission to run a command or publish the skill alone does not establish that source-access scope. The receiving context may execute only its assigned role; do not restart intake or launch the whole workflow again. Never bundle credentials, private logs, or unrelated repository content. Save handoff files only within the requested artifact scope.

Keep private reviewed source, manifests, drafts, critiques, and consolidated plans outside any public distribution checkout. Authorization to publish skill improvements does not authorize disclosure of the reviewed project. If publishing a workflow validation note, inspect the exact staged files and diff: omit private source excerpts, project paths/identifiers, input hashes, task-specific findings, and raw logs unless the user explicitly approves their disclosure. A public note can describe the workflow and its limits without including the private review packet.

The returning critique must identify the same snapshot, criterion version, draft version and actual model evidence. Missing/mismatched inputs prevent consolidation as a completed cross-model review: reconcile them first or explicitly report partial/unverified work. Do not fetch another chat, message another session, or launch external model calls without the corresponding user authorization. A handoff packet alone is not proof the second model ran.
