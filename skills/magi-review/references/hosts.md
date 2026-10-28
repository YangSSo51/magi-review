# Host notes

Documentation checked 2026-10-28. Capabilities and model access vary by client/version/account; runtime evidence takes precedence. This package is an instruction workflow, not a model router or an orchestrator executable.

## Codex

- Invoke `$magi-review`. `agents/openai.yaml` disables implicit invocation.
- Use the host's available subagent tool and model choices. Prefer a generic agent that honors the selected model; specialist roles can pin models. Use isolated context plus a neutral brief when supported.
- Session inheritance is Default only where the launcher actually guarantees it. Do not infer the running model from a saved default. Host limits may require sequential scheduling.
- Native Goal tools are optional; a textual execution Goal is always a valid deliverable. Never claim that writing a Plan changed the app's mode.
- Current documented project skill path: `.agents/skills/magi-review`; user path: `~/.agents/skills/magi-review`. Some clients support legacy paths such as `~/.codex/skills`; use the active client's known path rather than installing duplicate copies.

## Claude Code

- Invoke `/magi-review`. The installer adds `disable-model-invocation: true` to the skill frontmatter. Merely copying the unadapted common source does not enforce the native explicit-only setting.
- Use the host's general-purpose Agent/subagent mechanism. Do not use built-in Explore/Plan agents when they force a different model. Honor effective model precedence, organization restrictions, and fallback behavior; identical alias strings alone do not prove identical backend model IDs.
- Some versions accept `inherit` in an agent definition but not as a per-call model value. Use only the actual tool schema; if an exact selected model cannot be requested, ask the user to select that session model in the host UI and then use supported inheritance. Do not create persistent agents or alter settings without a request.
- Personal skill path: `~/.claude/skills/magi-review`; project path: `.claude/skills/magi-review`. A normal chat surface without subagent tooling cannot perform this three-agent workflow.
- A portable execution Goal is Markdown text. Do not assume Codex Goal tools exist in Claude Code.

## Official references

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills and invocation control](https://code.claude.com/docs/en/skills)
- [Claude Code subagents and model selection](https://code.claude.com/docs/en/sub-agents)
- [Claude Code model configuration](https://code.claude.com/docs/en/model-config)
