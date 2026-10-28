# Plan + challenge workflow trial — 2026-10-28

This coordinator-authored note records one live, explicitly authorized cross-host review. The reviewed project and all task-specific artifacts are private. Its source, paths, identifiers, input hashes, criteria wording, findings, draft, critique, final plan, and raw logs are intentionally excluded from this distribution. This is a procedural trial, not a quality benchmark or backend attestation.

## Setup and evidence

- Skill baseline: public commit `671960b80dd566f4295bcd4bbd240e9c27e958d1`.
- The user selected **Codex `gpt-6.1-sol / high`** as primary planner and **Claude `opus / high`** as challenger. Existing selections were reused. The user amended the recommended criteria before either role started; the accepted criteria were then sealed.
- The planner used a fresh generic subagent context with explicit model/effort launch parameters and no inherited conversation. This is launcher configuration evidence, not independent verification of the serving backend.
- The challenger used a fresh **Claude Code 2.1.312** print session with `--model opus --effort high`, project-only settings, an empty explicit MCP configuration, and a separate project installation. No persistent account/model settings were changed.
- Claude's init event and assistant messages reported **`claude-opus-5-5`**. The CLI accepted the effort setting; effective compute effort was not independently attested. The command completed successfully with no reported permission denials.
- The installed `magi-review` command appeared in discovery, and the challenger read the bundled mode reference. This note does not independently attest the complete native command-expansion payload; the earlier [Claude trial](CLAUDE-VALIDATION.md) separately covered native loading.

## Frozen inputs and sequence

The coordinator copied the selected source into a private snapshot, including relevant dirty/untracked content, and recorded a per-file hash manifest. A missing source dependency was added before the primary draft was sealed; the planner received the revised scope and completed the draft against that snapshot. The original files were unchanged during that scope revision. Both roles ultimately reviewed the same final snapshot and accepted criteria.

The planner returned one draft. The coordinator preserved and hashed it before launching the challenger. The challenger received the same neutral brief, source, criteria, and permissions, plus that exact draft. It did not receive the planner's private reasoning, other chat history, or a preferred verdict.

The coordinator verified the sealed source/criteria before the planner, the revised inputs before the challenger, and all final source/criteria/draft identities before consolidation. The challenger had no program-execution tool and explicitly disclosed that it had compared recorded identities rather than recomputing the hashes itself. The coordinator performed the hash verification.

The challenge returned a substantive report identifying its snapshot, criteria, and draft target. The coordinator checked material findings against the frozen source, recorded dispositions and resulting changes locally, then produced **one consolidated Plan and one portable execution Goal**. No additional peer clarification, replacement reviewer, or repeated whole review was run. The Goal is text only; no native Goal was registered and no application implementation began.

## Permissions and limits

The Codex planner was instructed to keep source read-only and not delegate; its only authorized write was its private draft artifact. Those boundaries were instructions, not a claim of an OS sandbox. Claude's offered tools were `Read`, `Glob`, `Grep`, and `Skill`; observed calls were only reading and searching. No application tests, database access, services, package installations, web searches, or application inference runs were performed by the roles. Model reasoning for this review was explicitly authorized.

Real incident reproduction and application correctness remain unverified. Source-based agreement and a completed review sequence do not establish a reliability, accuracy, cost, or performance improvement. Other models, Default inheritance, manual transport, resumed clarification, and other host versions remain untested in this mode.

## Changes after the trial

The baseline reference described manual cross-host transport. This run used the user's explicit authorization for a local second-host CLI and a challenger-only role scope. The published guidance now makes that supported procedural option explicit, preserves execution/source-access authorization, and prevents the receiving role from restarting the entire workflow.

It also explicitly keeps private review artifacts outside public distribution checkouts and separates permission to publish skill improvements from permission to disclose the reviewed project. A separate read-only publication reviewer checked the public documentation delta, found two wording issues, and confirmed their corrections. The subsequent generic trial note was reviewed separately before publication.

These are post-trial documentation corrections; no second full model run was performed on the amended wording. Local installer checks and skill validation are package checks, not a rerun of the application review.
