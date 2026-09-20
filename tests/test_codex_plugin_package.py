from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
SKILLS_ROOT = ROOT / "skills"
SKILL_PATH = SKILLS_ROOT / "project-workflow" / "SKILL.md"
HOOKS_PATH = ROOT / "hooks" / "hooks.json"
BOOTSTRAP_PATH = ROOT / "hooks" / "session-start.py"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def skill_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise AssertionError("SKILL.md frontmatter must be closed")
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, separator, value = line.partition(":")
        if separator:
            result[key.strip()] = value.strip()
    return result


class CodexPluginPackageTests(unittest.TestCase):
    def test_marketplace_points_pw_at_repository_root(self):
        marketplace = read_json(MARKETPLACE_PATH)
        self.assertEqual(marketplace["name"], "project-workflow")
        self.assertEqual(len(marketplace["plugins"]), 1)

        plugin = marketplace["plugins"][0]
        self.assertEqual(plugin["name"], "pw")
        self.assertEqual(plugin["source"], {"source": "local", "path": "."})
        self.assertEqual(plugin["policy"]["installation"], "AVAILABLE")
        self.assertEqual(plugin["policy"]["authentication"], "ON_INSTALL")

    def test_plugin_manifest_has_current_validator_shape(self):
        manifest = read_json(MANIFEST_PATH)
        self.assertEqual(manifest["name"], "pw")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertNotIn("hooks", manifest)

        self.assertTrue(manifest["description"].strip())
        self.assertTrue(manifest["author"]["name"].strip())

        interface = manifest["interface"]
        for key in (
            "displayName",
            "shortDescription",
            "longDescription",
            "developerName",
            "category",
            "defaultPrompt",
        ):
            self.assertTrue(interface[key])
        self.assertIsInstance(interface["capabilities"], list)

    def test_exactly_one_normal_bundled_skill_uses_accepted_name(self):
        skill_dirs = sorted(
            path for path in SKILLS_ROOT.iterdir()
            if path.is_dir() and not path.name.startswith(".")
        )
        self.assertEqual([path.name for path in skill_dirs], ["project-workflow"])

        skill = SKILL_PATH.read_text(encoding="utf-8")
        frontmatter = skill_frontmatter(skill)
        self.assertEqual(frontmatter["name"], "project-workflow")
        self.assertTrue(frontmatter["description"])
        self.assertNotEqual(frontmatter.get("disable-model-invocation"), "true")

    def test_skill_is_thin_and_routes_only_through_canonical_entry(self):
        skill = SKILL_PATH.read_text(encoding="utf-8")
        body = skill.split("\n---", 2)[-1]
        self.assertIn("PROJECT.md", body)
        self.assertIn("workflow/CONTEXT_ROUTING.md", body)
        self.assertNotIn("workflow/codex_only/ROUTER.md", body)
        self.assertNotIn("workflow/chatgpt_only/ROUTER.md", body)
        self.assertLess(len(re.findall(r"\S+", body)), 220)

    def test_session_start_hook_uses_installed_plugin_root(self):
        hooks = read_json(HOOKS_PATH)
        handlers = hooks["hooks"]["SessionStart"]
        self.assertEqual(len(handlers), 1)
        command_hooks = handlers[0]["hooks"]
        self.assertEqual(len(command_hooks), 1)
        self.assertEqual(command_hooks[0]["type"], "command")
        self.assertIn("$PLUGIN_ROOT/hooks/session-start.py", command_hooks[0]["command"])

    def test_session_start_bootstrap_emits_bounded_canonical_context(self):
        env = os.environ.copy()
        env["PLUGIN_ROOT"] = str(ROOT)
        result = subprocess.run(
            [sys.executable, str(BOOTSTRAP_PATH)],
            input="{}\n",
            text=True,
            capture_output=True,
            check=True,
            env=env,
        )
        payload = json.loads(result.stdout)
        output = payload["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "SessionStart")

        context = output["additionalContext"]
        self.assertLessEqual(len(context), 900)
        self.assertIn("PROJECT.md", context)
        self.assertIn(str(ROOT / "workflow" / "CONTEXT_ROUTING.md"), context)
        self.assertNotIn("codex_only", context)
        self.assertNotIn("chatgpt_only", context)

    def test_canonical_workflow_update_needs_no_skill_edit(self):
        marketplace = read_json(MARKETPLACE_PATH)
        self.assertEqual(marketplace["plugins"][0]["source"]["path"], ".")

        original_skill_hash = hashlib.sha256(SKILL_PATH.read_bytes()).hexdigest()
        canonical_router = ROOT / "workflow" / "codex_only" / "ROUTER.md"
        self.assertTrue(canonical_router.is_file())

        with tempfile.TemporaryDirectory() as temp_dir:
            staged_root = Path(temp_dir) / "pw"
            shutil.copytree(ROOT / "skills", staged_root / "skills")
            shutil.copytree(ROOT / "workflow", staged_root / "workflow")

            staged_router = staged_root / "workflow" / "codex_only" / "ROUTER.md"
            staged_router.write_text(
                staged_router.read_text(encoding="utf-8") + "\nPWCP_UPDATE_PROPAGATION_PROBE\n",
                encoding="utf-8",
            )

            self.assertIn(
                "PWCP_UPDATE_PROPAGATION_PROBE",
                staged_router.read_text(encoding="utf-8"),
            )
            staged_skill_hash = hashlib.sha256(
                (staged_root / "skills" / "project-workflow" / "SKILL.md").read_bytes()
            ).hexdigest()
            self.assertEqual(staged_skill_hash, original_skill_hash)

    def test_plugin_surfaces_contain_no_local_updater(self):
        implementation_files = [
            path.relative_to(ROOT).as_posix()
            for base in (ROOT / "hooks", ROOT / "skills", ROOT / ".codex-plugin")
            for path in base.rglob("*")
            if path.is_file()
        ]
        forbidden_name = re.compile(r"(updater?|poller|timer)", re.IGNORECASE)
        self.assertFalse(
            [path for path in implementation_files if forbidden_name.search(Path(path).name)]
        )


if __name__ == "__main__":
    unittest.main()
