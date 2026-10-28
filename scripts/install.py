"""Install an explicit-only MAGI skill for one host without overwriting files."""

import argparse
from pathlib import Path
import shutil


SOURCE = Path(__file__).resolve().parents[1] / "skills" / "magi-review"


def install(host: str, destination: Path) -> Path:
    if host not in {"codex", "claude"}:
        raise ValueError(f"Unsupported host: {host}")
    target = destination.expanduser().absolute()
    # lexists semantics: also refuse dangling symlinks.
    if target.exists() or target.is_symlink():
        raise FileExistsError(f"Destination already exists; left unchanged: {target}")
    skill = (SOURCE / "SKILL.md").read_text(encoding="utf-8")
    license_text = (SOURCE.parents[1] / "LICENSE").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        raise ValueError("Invalid source frontmatter")
    if host == "claude":
        skill = skill.replace("---\n", "---\ndisable-model-invocation: true\n", 1)
    target.mkdir(parents=True, exist_ok=False)
    owned_target = target.resolve()
    try:
        (target / "LICENSE").write_text(license_text, encoding="utf-8")
        shutil.copytree(SOURCE / "references", target / "references")
        if host == "codex":
            shutil.copytree(SOURCE / "agents", target / "agents")
        # Publish the discoverable manifest only after all required assets exist.
        manifest = target / ".SKILL.md.tmp"
        manifest.write_text(skill, encoding="utf-8")
        manifest.replace(target / "SKILL.md")
    except Exception as error:
        try:
            # Only remove this invocation's new directory at its original location.
            if target.is_symlink() or target.resolve() != owned_target:
                raise OSError("Installation path changed; refusing cleanup")
            shutil.rmtree(owned_target)
        except OSError as cleanup_error:
            raise OSError(
                f"Installation failed ({error}); cleanup failed at {target}: {cleanup_error}. "
                "Inspect this incomplete installation before retrying."
            ) from error
        raise
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", required=True, choices=["codex", "claude"])
    parser.add_argument("--destination", required=True, type=Path,
                        help="New skill directory, including magi-review")
    args = parser.parse_args()
    try:
        target = install(args.host, args.destination)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Installation failed: {error}\n")
    print(f"Installed for {args.host}: {target}")


if __name__ == "__main__":
    main()
