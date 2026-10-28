# MAGI Review

**Review a hard decision from three perspectives. Turn the findings into an executable plan.**

A skill for **Claude Code and Codex**. Choose one model, agree on what matters, and let three independent subagents examine the same problem before you commit to an approach.

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

## Three lenses, one shared problem

| Evaluator | What it examines |
| --- | --- |
| **Purpose & value** | Does this solve the actual problem? Are the requirements and scope right? |
| **Correctness & safety** | What can fail? Which contracts, data, and compatibility guarantees must hold? |
| **Simplicity & operability** | Is there a simpler approach? What will this cost to build, operate, maintain, and reverse? |

All three use the **same user-selected model** and accepted criteria. They evaluate independently before seeing each other's conclusions. The coordinator checks material disagreements against evidence and preserves unresolved issues.

These are evaluation responsibilities, not strict/lenient personalities. A supported must-have violation cannot be voted away.

## How it works

1. **Choose the model.** Pick from the host's available subagent models or **Default**, meaning current session inheritance for this review.
2. **Describe the situation.** The assistant helps clarify your purpose, constraints, and success conditions.
3. **Agree on criteria.** The assistant recommends task-specific criteria, priorities, and observable evidence. Accept or edit the list before evaluation.
4. **Review independently.** Three read-only subagents evaluate the same brief, each through its own lens.
5. **Resolve what matters.** Check decision-changing disputes once, then produce the Plan and execution Goal.

You can authorize the recommendations upfront: `Use Default and your recommended criteria; produce a Plan and a Goal draft.`

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

Local tests cover installation, explicit-only metadata, license copying, identical workflow bodies, and cleanup/retry after copy failure. These scoped workflow trials do not establish a reliability or performance gain. Default inheritance, alternate models, and resumed peer cross-checks remain untested.

```sh
python -m unittest discover -s tests -v
```

## License and credits

[MIT](LICENSE).

MAGI is a thematic reference. This project claims no affiliation with the franchise or the supported model providers.
