---
name: magi-review
description: Run an explicitly requested MAGI review with three same-model evaluators, then produce a Plan and execution Goal.
license: MIT
---

# MAGI review

Use only when the user explicitly invokes MAGI review. Questions about this skill, skill edits, or task difficulty alone do not trigger a review. Follow the user's language. This is a review and planning workflow; implementation and native Goal registration follow the user's actual authorization.

## 1. Select the review model

Before launching evaluators, offer `Default — current session model` and the models the host actually exposes for subagent selection. Here Default means session inheritance for this review, not the provider's moving default alias. Model access is usually remote, not a list of locally installed weights. Do not infer availability from marketing pages, old configuration, or credentials. If discovery is unavailable, ask the user to choose Default or an exact host-supported model and report what remains unverified.

The user's choice is the review-local default for all three evaluators and their cross-check; do not change persistent app/account settings. Reuse a choice already supplied for this review. Keep the user's effort setting (otherwise the session setting) consistent across evaluators where supported. Record the model ID or supported alias, the evidence for resolution, and effective effort settings where exposed. Do not claim identical backend versions when only alias equality is observable. Never silently substitute models or use specialist agents that force a different model. If selection/inheritance cannot be honored, explain and ask before proceeding. Keep the coordinator's current model unless the user separately requests a change. Do not install models or change providers to make a choice available.

## 2. Frame the problem and recommend criteria first

Ask for the problem situation or purpose if it is not already clear. Extract the desired outcome, scope/non-goals, hard constraints, relevant artifacts/version, and observable success evidence. Ask only decision-changing questions that existing context cannot answer.

Before any evaluator launch, list 3–6 recommended, task-specific criteria with: criterion, why it matters, priority (must-have or preference), and observable evidence. Suggest priorities; do not invent user preferences. Organize them under these lenses, adapting emphasis to the problem:

| Evaluator | Lens |
| --- | --- |
| A | Purpose and value: does the approach solve the actual problem and cover the requirements? |
| B | Correctness and safety: contracts, compatibility, failure paths, integrity, and verification. |
| C | Simplicity and operability: simpler alternatives, maintenance/cost, operation, and reversibility. |

Present the recommended list and request the user's acceptance or changes. An explicit instruction to use your recommended criteria is advance acceptance: still show the list, then proceed. Otherwise wait for the reply; silence is not acceptance. Resolve material scope or priority gaps before evaluation. Accept short requests and help formulate them rather than requiring a completed specification.

## 3. Three independent evaluations

Launch exactly three read-only subagents using the chosen model; no child delegation. Use isolated contexts where supported. Give each the same neutral problem brief, accepted criteria, artifacts/version, permissions, and bounded stopping condition, plus its assigned lens. Do not share the coordinator's preferred solution or peer conclusions in the first pass. Existing required host/project instructions still apply; disclose unavoidable shared-history limitations.

Each returns: recommended approach/alternative; evidence locations; material findings and impact; unknowns; evidence that would change the recommendation. Distinguish observed facts from inference. Do not require dissent, personality acting, scores, or a quota of findings. No file edits, services, broad tests, or separately billed external experiments are authorized by a review alone. Subagent reasoning itself is part of the requested review.

If fewer than three agents can run concurrently, use three separate contexts sequentially and report scheduling. If three agents, isolation, or same-model execution cannot be provided, explain the limitation and ask about an alternative; never label single-agent role-play as three-agent review.

## 4. Check material disputes

After all first-pass reports arrive, send only decision-changing disputes and their evidence to the original evaluators for at most one cross-check. Skip this round if none exist. The coordinator resolves factual claims using source artifacts and already-permitted focused checks. Stop when no new evidence appears. Leave value tradeoffs for user choice and unresolved facts as verification prerequisites.

No majority vote, forced unanimity, or numerical averaging overrides a substantiated must-have violation. Unsupported worries have no veto. Same-model agreement is not independent proof or an executed test. Note which disagreements were resolved and why, and preserve meaningful remaining dissent.

## 5. Plan and execution Goal

Produce a concise Plan: selected approach and tradeoffs, scope/non-goals, ordered milestones, acceptance evidence, prerequisites, unresolved decisions, and replanning triggers. Drafting a Plan does not switch the host's Plan mode.

Produce a portable execution Goal: outcome, completion evidence, constraints, execution permissions, stop/escalation conditions. Keep changeable implementation steps in the Plan. Only register a native Goal when explicitly requested and the host provides that capability; inspect existing state first and never replace or complete an unfinished goal to make room. Otherwise provide the Goal as text and state that it is not registered. Do not start implementation from a review-only request. Add token budgets only when explicitly requested.

Conclude with model/configuration evidence, accepted criteria, key findings and disputes, Plan, and Goal status. Do not invent compatibility/performance evidence. Read [host notes](references/hosts.md) only for host-specific setup or limitations; read the repository's research notes only when research rationale is requested.
