from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
ROUTER = (ROOT / "workflow/codex_only/ROUTER.md").read_text(encoding="utf-8")
PLANNING = (ROOT / "workflow/codex_only/PLANNING.md").read_text(encoding="utf-8")
CLOSE = (ROOT / "workflow/codex_only/CLOSE.md").read_text(encoding="utf-8")
RECOVERY = (ROOT / "workflow/codex_only/RECOVERY.md").read_text(encoding="utf-8")
REVIEW = (ROOT / "workflow/codex_only/REVIEW.md").read_text(encoding="utf-8")
ORCHESTRATION = (ROOT / "workflow/codex/CODEX_ORCHESTRATION.md").read_text(encoding="utf-8")


class CodexOnlyContinuousOrchestrationContractTests(unittest.TestCase):
    def test_codex_only_context_health_gate_is_absent(self):
        self.assertFalse((ROOT / "workflow/codex_only/CONTEXT_HEALTH.md").exists())
        self.assertNotIn("workflow/codex_only/CONTEXT_HEALTH.md", ROUTER)
        self.assertNotIn("## Context-health trigger check", ROUTER)
        self.assertNotIn("CONTEXT_HEALTH:", ROUTER)
        self.assertNotIn("context-hygiene boundary", ROUTER)

    def test_router_continues_without_coordinator_hygiene_stop(self):
        self.assertIn(
            "Coordinator/session context hygiene is not a Project Workflow stop under `codex_only`",
            ROUTER,
        )
        self.assertIn(
            "continue deterministic Project Workflow orchestration without a user-facing "
            "coordinator-hygiene stop",
            ROUTER,
        )
        self.assertNotIn("perform the context-health trigger check below", ROUTER)

    def test_planning_cannot_schedule_coordinator_refresh_boundary(self):
        self.assertNotIn(
            "coordinating-context refresh boundaries only when materially useful",
            PLANNING,
        )
        self.assertIn(
            "do not schedule coordinator/session context refresh, Context Health, FRESH or "
            "hygiene boundaries as Master Plan checkpoints",
            PLANNING,
        )

    def test_review_and_next_milestone_remain_internal_continuation(self):
        self.assertIn(
            "A required/recommended independent review is not, by itself, a reason to return "
            "control to the user or normal ChatGPT under `codex_only`.",
            ORCHESTRATION,
        )
        self.assertIn(
            "deterministic authorized continuation proceeds without a user/normal-ChatGPT stop",
            REVIEW,
        )
        self.assertIn("## Automatic next milestone", CLOSE)
        self.assertIn('continue without requiring user “continue”', CLOSE)

    def test_recovery_replaces_coordinator_hygiene_handoffs(self):
        self.assertIn(
            "it is not a Project Workflow Context Health/FRESH/hygiene stop",
            RECOVERY,
        )
        self.assertIn(
            "Once durable state is coherent, deterministic continuation resumes without asking "
            "the user solely for a fresh coordinator context.",
            RECOVERY,
        )

    def test_runtime_boundary_remains_codex_workflow_owned(self):
        self.assertIn(
            "Project Workflow must not duplicate/fork those mechanics",
            ORCHESTRATION,
        )
        self.assertIn(
            "`codex_workflow` remains the owner of the concrete resume/replacement/session mechanics",
            ORCHESTRATION,
        )

    def test_chatgpt_only_context_health_contract_remains_present(self):
        self.assertTrue((ROOT / "workflow/chatgpt_only/CONTEXT_HEALTH.md").is_file())
        self.assertTrue((ROOT / "tests/test_chatgpt_only_context_health_contract.py").is_file())


if __name__ == "__main__":
    unittest.main()
