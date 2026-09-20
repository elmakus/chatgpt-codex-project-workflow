from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

README = (ROOT / "README.md").read_text(encoding="utf-8")
PROJECT = (ROOT / "PROJECT.md").read_text(encoding="utf-8")
CHANGELOG = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
PROJECT_TEMPLATE = (ROOT / "templates" / "PROJECT.md").read_text(encoding="utf-8")
CHATGPT_PROJECT_INSTRUCTIONS = (
    ROOT / "prompts" / "CHATGPT_PROJECT_INSTRUCTIONS.md"
).read_text(encoding="utf-8")
CHATGPT_START = (ROOT / "prompts" / "CHATGPT_START.md").read_text(encoding="utf-8")
CODEX_START = (ROOT / "prompts" / "CODEX_START.md").read_text(encoding="utf-8")
CONTEXT_ROUTING = (ROOT / "workflow" / "CONTEXT_ROUTING.md").read_text(
    encoding="utf-8"
)
AUTHORITY = (ROOT / "workflow" / "common" / "AUTHORITY.md").read_text(
    encoding="utf-8"
)

CHATGPT_EXECUTION_PREP = (
    ROOT / "workflow" / "chatgpt_only" / "EXECUTION_PREP.md"
).read_text(encoding="utf-8")
CHATGPT_RECOVERY = (
    ROOT / "workflow" / "chatgpt_only" / "RECOVERY.md"
).read_text(encoding="utf-8")
CODEX_EXECUTION_PREP = (
    ROOT / "workflow" / "codex_only" / "EXECUTION_PREP.md"
).read_text(encoding="utf-8")
CODEX_RECOVERY = (
    ROOT / "workflow" / "codex_only" / "RECOVERY.md"
).read_text(encoding="utf-8")


class BranchFirstIntegratedClosureTests(unittest.TestCase):
    def test_readme_no_longer_presents_root_default_as_fixed_policy_active_state(self):
        forbidden = (
            "legacy/default `chatgpt_only` mutable execution-state authority",
            "Existing projects may continue in legacy/default single-workstream mode",
            "The legacy/default fallback remains `implementation/TASK_BOARD.yaml`",
            "`PROJECT.md → Active research obligation`",
            "pre-execution routing is located from `PROJECT.md`",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, README)

        self.assertIn(
            "Historical root/default state is Recovery input only, never the active "
            "fallback for new or continued managed work",
            README,
        )

    def test_readme_documents_generic_entry_shortcuts_and_proportional_trivial_path(self):
        self.assertIn("Natural-language authorization is enough", README)
        self.assertIn(
            "use Project Workflow to introduce these changes",
            README,
        )
        self.assertIn("`#issue` and `#feature` remain optional explicit shortcuts", README)
        self.assertIn(
            "A trivial bounded change still uses branch → pull request → merge",
            README,
        )

    def test_root_project_is_integrated_index_not_live_workstream_state(self):
        self.assertNotIn("Active exploratory scope:", PROJECT)
        self.assertNotIn("Active research obligation:", PROJECT)
        self.assertNotIn("- Task Board: `implementation/TASK_BOARD.yaml`", PROJECT)
        self.assertNotIn("current project uses the legacy/default Task Board", PROJECT)

        self.assertIn("Workstream root: `implementation/workstreams/`", PROJECT)
        self.assertIn(
            "Historical/default Task Board: `implementation/TASK_BOARD.yaml`",
            PROJECT,
        )
        self.assertIn("recovery/migration navigation only", PROJECT)
        self.assertIn(
            "Active exploratory, pre-execution Research and plan-review locators "
            "must not be mirrored here",
            PROJECT,
        )

    def test_project_template_matches_integrated_index_contract(self):
        self.assertNotIn("Active exploratory scope:", PROJECT_TEMPLATE)
        self.assertNotIn("Active research obligation:", PROJECT_TEMPLATE)
        self.assertIn(
            "Historical/default Task Board: `implementation/TASK_BOARD.yaml | none`",
            PROJECT_TEMPLATE,
        )
        self.assertIn(
            "Active workstream-local exploratory, pre-execution Research and "
            "plan-review locators belong to the exact selected workstream manifest",
            PROJECT_TEMPLATE,
        )

    def test_bootstraps_require_branch_before_first_managed_write(self):
        self.assertIn(
            "a newly authorized managed change must create or recover its exact "
            "branch-isolated workstream before the first durable change-specific write",
            CHATGPT_PROJECT_INSTRUCTIONS,
        )
        self.assertIn(
            "create or recover the exact branch-isolated workstream **before** "
            "writing `PROJECT.md`",
            CHATGPT_START,
        )
        codex_only = CODEX_START.split("## Mixed-policy bounded start", 1)[0]
        self.assertIn(
            "create or recover the exact branch-isolated workstream before the "
            "first durable change-specific write",
            codex_only,
        )
        self.assertIn("branch → pull request → merge", codex_only)

    def test_fixed_policy_router_and_common_authority_encode_branch_first_boundary(self):
        self.assertIn(
            "for new `chatgpt_only` managed work, resolve the exact "
            "branch-isolated workstream first",
            CONTEXT_ROUTING,
        )
        self.assertIn(
            "historical root/default state is recovery/migration input only and "
            "must migrate before further managed-change mutation",
            CONTEXT_ROUTING,
        )
        self.assertIn("## Branch-first managed-change invariant", AUTHORITY)
        self.assertIn(
            "an exact branch-isolated workstream must exist before the first durable "
            "change-specific Project Workflow or project-source write",
            AUTHORITY,
        )
        self.assertIn(
            "managed changes reach the integration target through branch → pull "
            "request → merge",
            AUTHORITY,
        )

    def test_fixed_policy_execution_never_resumes_root_default_as_active_state(self):
        self.assertIn(
            "MUST NOT be scaffolded or selected for new/continued managed work",
            CHATGPT_EXECUTION_PREP,
        )
        self.assertIn(
            "## Historical root/default migration before mutation",
            CHATGPT_RECOVERY,
        )
        self.assertIn(
            "MUST NOT be scaffolded, selected or mutated for new or continued managed work",
            CODEX_EXECUTION_PREP,
        )
        self.assertIn(
            "## Historical root/default migration before mutation",
            CODEX_RECOVERY,
        )

    def test_changelog_records_fixed_policy_branch_first_migration(self):
        self.assertIn("## Unreleased — branch-first managed changes", CHANGELOG)
        self.assertIn(
            "Migrated both fixed policies (`chatgpt_only` and `codex_only`) "
            "to a branch-first managed-change model",
            CHANGELOG,
        )
        self.assertIn(
            "Historical root/default Task Boards and cumulative handoffs",
            CHANGELOG,
        )


if __name__ == "__main__":
    unittest.main()
