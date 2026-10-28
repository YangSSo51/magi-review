---
name: magi-review
description: Run an explicit MAGI review with three lenses or a primary planner and a different-model challenger, then consolidate one Plan and execution Goal.
license: MIT
---

# MAGI review

Use only when the user explicitly invokes MAGI review. Questions about this skill, skill edits, or task difficulty alone do not trigger a review. Follow the user's language. This is a review and planning workflow; implementation and native Goal registration follow the user's actual authorization.

## 1. Choose the mode and models

Offer two modes at intake, together with model choices. Reuse explicit choices and do not ask again when already settled:

- **Three lenses (default):** three independent evaluators use the same chosen model. Follow sections 3–4 below.
- **Plan + challenge:** one model drafts the primary plan; a different model checks its claims and failure paths. Complete shared intake in section 2, follow [the plan-and-challenge workflow](references/plan-challenge.md), then section 5. Do not also launch the three lens evaluators.

If the mode is unspecified, ask the user to choose; present three lenses as the default recommendation, not silent acceptance. An explicit instruction to use your recommended mode/models is advance acceptance. For plan + challenge, ask for the planner and challenger selections separately and verify that they are different supported model identities; Default is allowed only where the role's effective selection can be established. Never silently substitute a same-model reviewer.

Before launching evaluators, offer `Default — current session model` and the models the host actually exposes for subagent selection. Here Default means session inheritance for this review, not the provider's moving default alias. Model access is usually remote, not a list of locally installed weights. Do not infer availability from marketing pages, old configuration, or credentials. If discovery is unavailable, ask the user to choose Default or an exact host-supported model and report what remains unverified.

Selections are review-local; do not change persistent app/account settings. In three-lens mode the same selected model/effort applies to all three; in plan + challenge preserve each role's selected model/effort. Record supported model IDs/aliases, selection evidence, and effective effort where exposed; aliases are not backend attestation. Never silently substitute models or use specialist agents that force a different model. If selection/inheritance cannot be honored, explain and ask before proceeding. Keep the coordinator's current model unless separately requested. Do not install models, change providers, or use another host/account without authorization.

## 2. Frame the problem and recommend criteria first

Ask for the problem situation or purpose if it is not already clear. Extract the desired outcome, scope/non-goals, hard constraints, relevant artifacts/version, and observable success evidence. Ask only decision-changing questions that existing context cannot answer.

Before any evaluator launch, list 3–6 recommended, task-specific criteria with: criterion, why it matters, priority (must-have or preference), and observable evidence. Suggest priorities; do not invent user preferences. In three-lens mode organize them under the lenses below; in plan + challenge give both roles the full criteria instead of splitting them by lens:

| Evaluator | Lens |
| --- | --- |
| A | Purpose and value: does the approach solve the actual problem and cover the requirements? |
| B | Correctness and safety: contracts, compatibility, failure paths, integrity, and verification. |
| C | Simplicity and operability: simpler alternatives, maintenance/cost, operation, and reversibility. |

Present the recommended list and request the user's acceptance or changes. An explicit instruction to use your recommended criteria is advance acceptance: still show the list, then proceed. Otherwise wait for the reply; silence is not acceptance. Resolve material scope or priority gaps before evaluation. Accept short requests and help formulate them rather than requiring a completed specification.

Give accepted criteria stable IDs (C1, C2, …) and freeze their wording, priorities, and acceptance evidence for this run. Freeze the reviewed source version too: repository/commit plus relevant dirty changes and untracked inputs, using a diff or content hashes rather than treating HEAD alone as the working tree. For non-Git artifacts, record exact versions or content hashes. Include relevant environment/configuration assumptions without credentials. Both modes use this same brief and snapshot. If relevant source or criteria change, stop comparison, disclose the change, and rebase affected findings; get renewed acceptance for material criteria changes. Do not silently combine reports from different snapshots.

## 3. Three independent evaluations (three-lens mode only)

Launch exactly three read-only subagents using the chosen model; no child delegation. Use isolated contexts where supported; avoid host fork options that inherit the coordinator's conclusions or ignore the selected model. Give each the same neutral problem brief, accepted criteria, artifacts/version, permissions, and bounded stopping condition, plus its assigned lens. Do not share the coordinator's preferred solution or peer conclusions in the first pass. Existing required host/project instructions still apply; disclose unavoidable shared-history limitations. Apply read-only tool restrictions where available, and state when read-only/no-delegation boundaries are instructions rather than tool-enforced limits.

Each returns: recommended approach/alternative; evidence locations; material findings and impact; unknowns; evidence that would change the recommendation. Distinguish observed facts from inference. Do not require dissent, personality acting, scores, or a quota of findings. No file edits, services, broad tests, or separately billed external experiments are authorized by a review alone. Subagent reasoning itself is part of the requested review.

If fewer than three agents can run concurrently, use three separate contexts sequentially and report scheduling. If three agents, isolation, or same-model execution cannot be provided, explain the limitation and ask about an alternative; never label single-agent role-play as three-agent review.

## 4. Check material disputes (three-lens mode only)

After all first-pass reports arrive, send only decision-changing disputes and their evidence to the original evaluators for at most one cross-check when the host supports resuming them. Skip this round if none exist. If original contexts cannot be resumed, the coordinator checks disputed claims against source artifacts, preserves dissent, and discloses that peer follow-up was unavailable. Do not silently create replacement evaluators or use a conversation fork to pretend the original context was resumed. Ask before adding evaluator contexts if an unresolved material dispute requires them. The coordinator resolves factual claims using source artifacts and already-permitted focused checks. Stop when no new evidence appears. Leave value tradeoffs for user choice and unresolved facts as verification prerequisites.

No majority vote, forced unanimity, or numerical averaging overrides a substantiated must-have violation. Unsupported worries have no veto. Same-model agreement is not independent proof or an executed test. Note which disagreements were resolved and why, and preserve meaningful remaining dissent.

## 5. Plan and execution Goal

Produce a concise Plan: selected approach and tradeoffs, scope/non-goals, ordered milestones, acceptance evidence, prerequisites, unresolved decisions, and replanning triggers. Drafting a Plan does not switch the host's Plan mode.

Produce a portable execution Goal: outcome, completion evidence, constraints, execution permissions, stop/escalation conditions. Keep changeable implementation steps in the Plan. Only register a native Goal when explicitly requested and the host provides that capability; inspect existing state first and never replace or complete an unfinished goal to make room. Otherwise provide the Goal as text and state that it is not registered. Do not start implementation from a review-only request. Add token budgets only when explicitly requested.

Conclude with chosen mode, model/configuration evidence, source snapshot, accepted criteria, key findings and dispositions, one consolidated Plan, and Goal status. Do not invent compatibility/performance evidence. Read [host notes](references/hosts.md) only for host-specific setup or limitations; consult the [published research notes](https://github.com/YangSSo51/magi-review/blob/main/docs/RESEARCH.md) only when research rationale is requested (they are not bundled into the installed skill).
