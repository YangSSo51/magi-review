# Release checklist

Prepared 2026-10-28 for initial public publication at [YangSSo51/magi-review](https://github.com/YangSSo51/magi-review).

Before publishing:

- Verify the intended publishing account before each publication; do not use or modify the PC's existing Git account settings as a shortcut. Commit identity is repository-local.
- Confirm public visibility and repository name. MIT has been selected following the user's reference-project direction; the root LICENSE uses the project contributor attribution, not the PC's Git identity.
- Re-run local checks. Inspect the exact file list and diff before committing. This package has no vendored code, third-party runtime dependencies, credentials, private account settings, or machine-specific absolute paths. The public repository URL and owner are intentional.
- Perform an explicitly authorized small live trial in each supported host when available: model choice, criteria acceptance, three actual same-model agents, disagreement handling, and textual Goal fallback. Record actual host versions/model evidence. Do not label static checks as end-to-end validation.
- Publish from this directory only after account identity is established. Keep credentials in the host/CLI credential manager, outside this package. Do not copy local Git config or chat logs into the repository.

## Local verification

```sh
python -m unittest discover -s tests -v
```

The installer needs no third-party dependencies. Tests run in temporary directories and make no model or network calls. They include partial-copy failure, cleanup/retry, and delayed publication of the discoverable manifest.

## Codex workflow trial

See [the scoped run report](CODEX-VALIDATION.md) for the three evaluator launches, findings, Plan, and native Goal registration. Codex selector discovery, backend identity attestation, and comparative performance remain unverified.

## Claude Code workflow trial

See [the Claude run report](CLAUDE-VALIDATION.md) for native slash-command loading, `opus/high` selection, three distinct evaluator contexts, source-based dispute checking, Plan, and an unregistered textual Goal. One explicit-model path on 2.1.311 was observed; it does not establish other versions/models, Default inheritance, resumed peer follow-up, or comparative quality.
