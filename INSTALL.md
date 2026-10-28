# Install MAGI Review

Download or clone this repository, then ask your coding assistant:

```text
Install MAGI Review from https://github.com/YangSSo51/magi-review for Codex or Claude Code.
Ask me which host and whether to install for this project or my user account.
Use scripts/install.py with an explicit destination; preserve existing files.
```

Repository: [YangSSo51/magi-review](https://github.com/YangSSo51/magi-review). The following commands run from a local clone or download.

## Python installer

Requires Python 3.10+ and no third-party packages. From the downloaded repository:

```sh
# Project installation into a different project's directory
python scripts/install.py --host codex --destination /path/to/project/.agents/skills/magi-review
python scripts/install.py --host claude --destination /path/to/project/.claude/skills/magi-review

# Personal installation; choose the command for your host
python scripts/install.py --host codex --destination ~/.agents/skills/magi-review
python scripts/install.py --host claude --destination ~/.claude/skills/magi-review
```

For Windows PowerShell, pass `"$HOME/.agents/skills/magi-review"` or `"$HOME/.claude/skills/magi-review"` for the personal destination. Hosts with legacy skill paths may require another explicit destination. Do not install the same skill in multiple scopes.

The script copies the skill and MIT license, applies the host's explicit-only setting, and refuses any existing destination. It publishes SKILL.md after supporting files are ready. On an installation error, it removes only the new installation directory created by that invocation; if cleanup also fails, it reports the exact path for inspection before retrying. It does not alter global agent instructions, credentials, model settings, or shell profiles.

## Without Python

1. Copy `skills/magi-review` to the appropriate skill folder and copy the root `LICENSE` into that installed folder.
2. For Claude Code, add `disable-model-invocation: true` inside SKILL.md's opening YAML frontmatter. Codex uses the supplied `agents/openai.yaml`.
3. Open a fresh host session or use its supported skill reload command, then explicitly invoke `$magi-review` in Codex or `/magi-review` in Claude Code.

## After either installation method

Open a fresh host session or use that client's supported skill reload mechanism. Confirm that MAGI Review appears in its skill selector or command list before invoking it. A successful installer exit confirms files were written; it does not confirm that an already-running session discovered them. If it is missing, check the active client's skill paths and duplicate installations before retrying.

## Update or remove

Back up your existing installation and local edits before replacing files from a new download. The installer intentionally has no overwrite or auto-update option. To remove the skill, delete only the installed `magi-review` directory you selected. Never delete a whole skills parent directory.

See [host notes](skills/magi-review/references/hosts.md) for runtime limitations. Installation success is not proof of model availability or a successful three-agent review.
