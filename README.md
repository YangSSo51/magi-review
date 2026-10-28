# MAGI Review

**Review a hard decision. Challenge the assumptions. Leave with one executable plan.**

A skill for **Claude Code and Codex** with two selectable workflows: three independent perspectives using one model, or a primary plan challenged by a different model. Both keep the source snapshot and accepted criteria fixed, then consolidate the evidence into one Plan and execution Goal.

[Get started](#get-started) · [Example](#example) · [Research](docs/RESEARCH.md) · [한국어](README.ko.md) · [MIT](LICENSE)

## Get started

Ask your coding assistant:

```text
Install MAGI Review from https://github.com/YangSSo51/magi-review.
Ask whether I use Claude Code or Codex and whether to install for this
project or my user account. Follow INSTALL.md and preserve existing files.
```

Or clone the repository and run the installer for your host:

```sh
git clone https://github.com/YangSSo51/magi-review.git
cd magi-review

# Choose one: personal installation
python scripts/install.py --host claude --destination ~/.claude/skills/magi-review
python scripts/install.py --host codex --destination ~/.agents/skills/magi-review
```

The optional installer uses **Python 3.10+ with no third-party packages**. It refuses existing destinations. For PowerShell paths, project installations, legacy clients, or installation without Python, see [INSTALL.md](INSTALL.md).

Open a fresh host session or use its supported skill reload mechanism, and confirm MAGI Review appears in the skill selector or command list. Then invoke it:

| Host | Invocation |
| --- | --- |
| Claude Code | `/magi-review Review our migration strategy. Recommend criteria first.` |
| Codex | `$magi-review Review our migration strategy. Recommend criteria first.` |

MAGI Review runs only when explicitly invoked. It adds no global instructions and changes no account/model defaults.

## Choose your review mode

| Mode | Roles | Best fit |
| --- | --- | --- |
| **Three lenses** (default recommendation) | Three independent evaluators, one selected model | Explore an ambiguous problem from complementary perspectives. |
| **Plan + challenge** | A primary planner and a different-model challenger | Check a proposed approach for false claims, missed failure paths, and unnecessary changes. |

Select the mode and models at intake; choices already supplied are reused. In plan + challenge, select the planner and challenger separately. The challenger reviews the frozen primary draft against the same source and criteria, rather than writing a competing plan from scratch.

```text
/magi-review Use plan + challenge. Let me choose the planner and challenger
models. Recommend criteria first and pin the code version, including local
changes. Classify the findings and consolidate one final Plan and Goal.
```

Use `$magi-review` in Codex. These are instructions to the skill, not flags for a separate CLI.

**Using Claude and Codex together:** if your host cannot run both selected models, the skill offers a manual handoff with the same brief, source manifest, criteria, and draft. It does not automatically route between providers or treat a handoff packet as a completed review. See [the workflow](skills/magi-review/references/plan-challenge.md).

## Three lenses, one shared problem

| Evaluator | What it examines |
| --- | --- |
| **Purpose & value** | Does this solve the actual problem? Are the requirements and scope right? |
| **Correctness & safety** | What can fail? Which contracts, data, and compatibility guarantees must hold? |
| **Simplicity & operability** | Is there a simpler approach? What will this cost to build, operate, maintain, and reverse? |

In three-lens mode, all three use the **same user-selected model** and accepted criteria. They evaluate independently before seeing each other's conclusions. The coordinator checks material disagreements against evidence and preserves unresolved issues. Plan + challenge uses its two-role sequence instead; it does not also launch these three evaluators.

These are evaluation responsibilities, not strict/lenient personalities. A supported must-have violation cannot be voted away.

## How it works

1. **Choose the mode and models.** Use supported model choices or **Default**, meaning verified current-session inheritance for the role. Plan + challenge requires different planner/challenger models.
2. **Describe the situation.** The assistant helps clarify your purpose, constraints, and success conditions.
3. **Freeze the inputs.** Accept or edit the recommended criteria, priorities, and observable evidence. Record stable criterion IDs and the code snapshot, including relevant dirty/untracked inputs; HEAD alone is insufficient when local changes matter.
4. **Run the selected review.** Either three independent lens evaluations, or a primary draft followed by a different-model critique. Roles are read-only and use the same frozen inputs.
5. **Resolve what matters.** In challenge mode, classify findings as confirmed, conditional, rejected, or insufficient evidence, with source evidence and resulting plan changes. Produce one consolidated Plan and execution Goal, keeping unresolved prerequisites visible.

You can authorize choices upfront: `Use three lenses, Default, and your recommended criteria; produce a Plan and a Goal draft.` A material source/criteria change invalidates affected comparisons; it must be reconciled rather than silently merged.

## Example

**You:** “We need to migrate our database with minimal interruption.”

**Before evaluation**, the assistant clarifies the interruption budget and recommends criteria such as client compatibility, data preservation, recovery evidence, and ongoing maintenance.

**After evaluation**, you get:

- A recommended approach and the alternatives considered.
- Findings with evidence, assumptions, and unresolved disagreements.
- A **Plan** with milestones, prerequisites, and validation steps.
- An **execution Goal** stating the outcome, completion evidence, permissions, and stop/replan conditions.

This is an illustrative workflow, not a recorded successful migration. See the [expanded example](docs/EXAMPLE.md).

Writing a Plan does not switch the host's Plan mode. A Goal is portable text unless you explicitly request native registration and the host supports it. A review-only request ends before implementation.

## When to use it

Use it for consequential architecture choices, migrations, ambiguous diagnoses, and plans where overlooked constraints could cause expensive rework. For small, well-defined changes, a single agent with focused verification is often a cheaper starting point.

## Evidence and limits

MAGI Review is **research-informed; this exact workflow has not been benchmarked**. Related studies report both gains from structured review and failures caused by role bias, correlated errors, or extra cost. [Research notes](docs/RESEARCH.md) separate findings from design choices.

The package requires host support for subagents and model selection/inheritance. It does not install models, provide cross-provider routing, or require API keys of its own. Reviews consume your host's normal model usage. Unsupported capabilities are reported rather than simulated. See [host notes](skills/magi-review/references/hosts.md).

The [Codex trial](docs/CODEX-VALIDATION.md) exercised user model/criteria selection, three isolated evaluator launches, evidence checking, Plan, and native Goal registration. It loaded the installed skill manually, so Codex selector discovery was not verified. The [Claude Code trial](docs/CLAUDE-VALIDATION.md) verified native slash-command loading, three `opus/high` evaluator calls with distinct contexts, coordinator evidence checks, Plan, and an explicitly unregistered textual Goal. Response messages reported `claude-opus-5-5` for all three. These are host-reported identifiers, not independent backend attestation. Same-model agreement is not proof.

Local tests cover installation, explicit-only metadata, license copying, identical workflow bodies, bundled workflow references, and cleanup/retry after copy failure. The recorded live trials cover **three-lens mode only**. Plan + challenge and cross-host handoff have not yet had a live end-to-end trial. These procedural options do not establish a reliability or performance gain. Default inheritance, alternate models, and resumed peer cross-checks remain untested.

```sh
python -m unittest discover -s tests -v
```

## License and credits

[MIT](LICENSE).

MAGI is a thematic reference. This project claims no affiliation with the franchise or the supported model providers.
