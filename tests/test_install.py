import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("magi_install", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def test_host_adapters_preserve_body_and_enforce_explicit_invocation(self):
        source = (installer.SOURCE / "SKILL.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as folder:
            for host in ("codex", "claude"):
                target = installer.install(host, Path(folder) / host / "magi-review")
                actual = (target / "SKILL.md").read_text(encoding="utf-8")
                self.assertEqual(actual.split("\n---\n", 1)[1],
                                 source.split("\n---\n", 1)[1])
                self.assertTrue((target / "references/hosts.md").is_file())
                self.assertEqual((target / "LICENSE").read_text(encoding="utf-8"),
                                 (ROOT / "LICENSE").read_text(encoding="utf-8"))
                if host == "claude":
                    self.assertIn("disable-model-invocation: true", actual.split("\n---\n")[0])
                    self.assertFalse((target / "agents").exists())
                else:
                    self.assertEqual(source, actual)
                    metadata = (target / "agents/openai.yaml").read_text(encoding="utf-8")
                    self.assertIn("allow_implicit_invocation: false", metadata)

    def test_existing_destination_is_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "magi-review"
            target.mkdir()
            marker = target / "user-file.txt"
            marker.write_text("user content", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                installer.install("codex", target)
            self.assertEqual(marker.read_text(encoding="utf-8"), "user content")
            self.assertEqual([item.name for item in target.iterdir()], [marker.name])

    def test_invalid_host_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "magi-review"
            with self.assertRaises(ValueError):
                installer.install("unknown", target)
            self.assertFalse(target.exists())

    def test_copy_failure_removes_new_destination_and_allows_retry(self):
        for host in ("codex", "claude"):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as folder:
                target = Path(folder) / "magi-review"
                with patch.object(installer.shutil, "copytree", side_effect=OSError("copy failed")):
                    with self.assertRaisesRegex(OSError, "copy failed"):
                        installer.install(host, target)
                self.assertFalse(target.exists())
                installer.install(host, target)
                self.assertTrue((target / "SKILL.md").is_file())

    def test_skill_is_not_discoverable_until_supporting_files_are_ready(self):
        real_copytree = installer.shutil.copytree
        for host in ("codex", "claude"):
            with self.subTest(host=host), tempfile.TemporaryDirectory() as folder:
                target = Path(folder) / "magi-review"

                def copy_supporting_files(source, destination, *args, **kwargs):
                    self.assertFalse((target / "SKILL.md").exists())
                    return real_copytree(source, destination, *args, **kwargs)

                with patch.object(installer.shutil, "copytree", side_effect=copy_supporting_files):
                    installer.install(host, target)
                self.assertTrue((target / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
