# Claude Code workflow trial — 2026-10-28

This coordinator-authored summary describes one scoped trial on Claude Code **2.1.311** using the first-party subscription login. It is not a benchmark, a raw transcript, or an attestation of the model provider's backend. Raw logs, account details, and machine-specific paths are not published.

## Setup and intake

- Source snapshot: `78b42e850786b3e77dba616f777078f8fa727d0b`; the working tree stayed unchanged during evaluation.
- Installed the Claude variant with the repository's Python installer into a separate test project's `.claude/skills/magi-review`. Its frontmatter contained `disable-model-invocation: true`.
- The first intake used `--restricted`: the project command was missing and Claude read source instructions as a fallback. That attempt did **not** validate native loading.
- A fresh normal-project session using project-only settings, an empty MCP configuration, denied permission prompts, and an explicit read/tool allowlist exposed `magi-review` in the command list. Claude received the native slash-command expansion and the installed skill's base directory. It did not use source reading as the discovery fallback in that check.
- The human selected **`opus / high`** and accepted the six recommended criteria before the evaluation phase. The normal-project session was resumed for evaluation with those choices. No persistent account/model settings were changed.

This comparison identifies a test-mode discovery difference on this client. It does not prove a general installation bug or authorize automatically relaxing security settings on another machine.

## Accepted criteria and observations

| Criterion | Observed evidence |
| --- | --- |
| Explicit invocation | Native `/magi-review` expansion and installed explicit-only frontmatter were observed; model-driven invocation remained disabled. |
| Complete review flow | Three actual evaluator calls and reports, coordinator source checks, Plan, and execution Goal text were returned. |
| Host guidance matches runtime | Evaluators identified missing caveats about model/effort defaults, fork contexts, follow-up availability, and read-only boundaries. These were addressed in the post-trial changes. |
| Installer safety | Static evaluator review found no current blocking installer defect. The outer runner reran focused installer tests after changes; Claude evaluators did not execute them. |
| Boundaries are explicit | Child traces contained only Read, Glob, and Grep. General-purpose agent definitions may still expose broader capabilities; instructions are not a universal sandbox guarantee. |
| Small, consistent package | Retained one skill source, corrected explicit-command examples, research-note routing, and backup guidance. No permanent agent definitions or orchestration service were added. |

## Three real evaluators

The outer runner inspected the JSON stream, rather than relying solely on the coordinator's claims:

| Lens | Accepted Agent parameters | Child message model | Report |
| --- | --- | --- | --- |
| A: purpose/value | `general-purpose`, `model=opus`, `effort=high` | `claude-opus-5-5` | Distinct report received |
| B: correctness/safety | `general-purpose`, `model=opus`, `effort=high` | `claude-opus-5-5` | Distinct report received |
| C: simplicity/operability | `general-purpose`, `model=opus`, `effort=high` | `claude-opus-5-5` | Distinct report received |

The trace had three unique launch IDs, three task-start events, and three completion notifications. All were top-level launches; no child Agent calls were observed. Each received the same neutral purpose, criteria, source snapshot, and read-only boundaries plus its assigned lens. All launches preceded the first returned report; no peer conclusions were supplied in the first-pass prompts. The Agent calls used fresh general-purpose contexts, not the conversation-fork agent type.

Across children, the trace showed **38 Read, 2 Glob, and 2 Grep calls**, counting forwarded messages with a `parent_tool_use_id` and excluding coordinator tool calls. No child shell, edit, write, network, or delegation calls were observed. Response model identifiers and accepted effort arguments are host evidence, not independent backend or effective-compute attestation. A common brief and shared model can still produce correlated conclusions.

## Findings and source-based resolution

- A and B found that requiring follow-up with the original evaluator context is not portable when the offered dispatch API cannot resume it. C treated the workflow as structurally complete. The coordinator inspected the source instruction and its offered tool description, then recorded the limitation. No additional evaluator contexts were spawned.
- B emphasized untested installer branches; A and C found the present installer statically sound. The coordinator distinguished a test-coverage suggestion from a reproduced defect. No new installer defect was demonstrated in this trial.
- The installed frontmatter order was checked against the installer, resolving a concern caused by a prose enumeration of its keys. The outer runner also retained the actual installer invocation as local evidence.
- All three highlighted host caveats and small documentation issues. The outer runner adopted the concrete portability/documentation changes and did not expand the package with speculative model routing, permanent agents, or every suggested test.

The coordinator resolved these assessment differences using read-only sources. **A resumed peer cross-check was not run.** The amended skill explicitly permits coordinator evidence checking when original contexts cannot be resumed, discloses that limit, and asks before adding replacement evaluator contexts if they are needed for an unresolved material dispute. This fallback preserves the three-evaluator contract; the amended fallback itself was not rerun as a new live review.

## Plan and execution Goal

Claude returned a Plan covering host guidance, minimal skill changes, documentation consistency, focused validation, and replan triggers. It proposed preserving the shared-source design and keeping permanent agent definitions outside the default scope.

Claude also returned an execution Goal with an outcome, acceptance conditions, constraints, execution permissions, and stop/escalation conditions. It explicitly labelled the Goal **text only, not registered**. No native `/goal` command or Goal-registration tool was exercised, and no app Plan-mode change was claimed. The outer runner applied the human's existing authorization to make and publish fixes rather than treating the generated Plan as new permission.

## Post-trial changes and checks

- Clarify fresh-context selection, model-default/effort caveats, and instruction-only boundaries.
- Make original-context follow-up conditional on host support; keep coordinator evidence checking as a disclosed fallback without silently adding evaluators.
- Link the installed skill to published research notes rather than assuming repository docs were installed.
- Correct explicit-command examples and keep update backups outside discovered skill roots.
- Rerun the five existing installer tests, host-adapter installation smoke checks, skill format validation, local Markdown target checks, and diff review before publishing.

The live trial ran against the baseline above. The amended instructions were checked locally after it; another full model review was not repeated. No comparative accuracy, cost, or latency gain is claimed. The completed evaluation command reported approximately **$2.05 list-price-equivalent usage**; this is not a claim of an actual charge to the subscription account or an independently isolated cost for the three children, and duplicate result events were not summed.

## Remaining limits

Default inheritance, alternate models, arbitrary account configurations, sequential scheduling, unsupported-capability escalation, actual denied writes, native Goal registration, and resumed peer debate remain untested. This documents one successful explicit-model workflow with a portable Goal on one client version, not a guarantee for every Claude environment.
