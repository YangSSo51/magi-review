# Host notes

Documentation checked 2026-10-28. Capabilities and model access vary by client/version/account; runtime evidence takes precedence. This package is an instruction workflow, not a model router or an orchestrator executable. Exactly three same-model evaluators applies to three-lens mode; plan + challenge has two different-model roles. A host's model list does not imply access to another provider's models. Use the selected mode's handoff rules when two hosts are required.

## Codex

- Invoke `$magi-review`. `agents/openai.yaml` disables implicit invocation.
- Use the host's available subagent tool and model choices. Prefer a generic agent that honors the selected model; specialist roles can pin models. Use isolated context plus a neutral brief when supported.
- Session inheritance is Default only where the launcher actually guarantees it. Do not infer the running model from a saved default. Host limits may require sequential scheduling.
- Native Goal tools are optional; a textual execution Goal is always a valid deliverable. Never claim that writing a Plan changed the app's mode.
- Current documented project skill path: `.agents/skills/magi-review`; user path: `~/.agents/skills/magi-review`. Some clients support legacy paths such as `~/.codex/skills`; use the active client's known path rather than installing duplicate copies.

## Claude Code

- Invoke `/magi-review`. The installer adds `disable-model-invocation: true` to the skill frontmatter. Merely copying the unadapted common source does not enforce the native explicit-only setting.
- Use the host's general-purpose Agent/subagent mechanism. Do not use built-in Explore/Plan agents when they force a different model. Honor effective model precedence, organization restrictions, and fallback behavior; identical alias strings alone do not prove identical backend model IDs.
- Prefer a fresh general-purpose context. A host's `fork` option may inherit the whole conversation or ignore model overrides; do not use it when either would violate this review's independence/model choice. Filesystem/worktree isolation alone does not establish conversation isolation.
- Some versions accept `inherit` in an agent definition but not as a per-call model value. Use only the actual tool schema; if an exact selected model cannot be requested, ask the user to select that session model in the host UI and then use supported inheritance. Do not create persistent agents or alter settings without a request.
- Omitting `model` is not proof of session inheritance: agent definitions, subagent defaults, organization rules, or fallback may take precedence. Verify the effective selection or disclose the uncertainty. If the Agent schema exposes `effort` and the user has selected it, pass that same supported value to all three; omission may use an agent default rather than the session's setting.
- Agent follow-up/resume capabilities vary by runtime. If original role contexts cannot be resumed, follow the chosen mode's coordinator evidence-check fallback and disclose the lack of peer follow-up. Do not silently expand the selected mode's role count with replacement contexts.
- General-purpose agent definitions may expose write, shell, or delegation tools. Restrict tools through supported session/agent controls where possible; otherwise disclose prompt-only boundaries. Never treat a read-only brief as a sandbox guarantee. The 2026-10-28 trial observed only Read/Glob/Grep calls, not universal enforcement in other clients.
- Personal skill path: `~/.claude/skills/magi-review`; project path: `.claude/skills/magi-review`. A normal chat surface without subagent tooling cannot perform this three-agent workflow.
- A portable execution Goal is Markdown text. Do not assume Codex Goal tools exist in Claude Code.
- In the 2.1.311 trial, `--restricted` omitted the project skill from discovery; a fresh normal-project session with project-only settings and explicit tool allowlists loaded it. This is a scoped observation, not a claim that all versions behave identically. Check customization/setting-source restrictions before blaming installation, and do not automatically relax user security settings.

## Official references

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills and invocation control](https://code.claude.com/docs/en/skills)
- [Claude Code subagents and model selection](https://code.claude.com/docs/en/sub-agents)
- [Claude Code model configuration](https://code.claude.com/docs/en/model-config)
