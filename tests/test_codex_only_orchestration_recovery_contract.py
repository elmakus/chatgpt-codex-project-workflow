from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


KERNEL = read("workflow/codex_only/ORCHESTRATION_KERNEL.md")
WORKSTREAMS = read("workflow/codex_only/WORKSTREAMS.md")
TEMPLATE = read("workflow/codex_only/WORKSTREAM_TEMPLATE.yaml")
TASK_BOARD_TEMPLATE = read("workflow/codex_only/WORKSTREAM_TASK_BOARD_TEMPLATE.yaml")
INTAKE = read("workflow/codex_only/INTAKE.md")
RECOVERY = read("workflow/codex_only/RECOVERY.md")
ROUTER = read("workflow/codex_only/ROUTER.md")
EXECUTION = read("workflow/codex_only/EXECUTION.md")
EXECUTION_PREP = read("workflow/codex_only/EXECUTION_PREP.md")
REVIEW = read("workflow/codex_only/REVIEW.md")
PLAN_REVIEW = read("workflow/codex_only/PLAN_REVIEW.md")
RESEARCH = read("workflow/codex_only/RESEARCH.md")
CLOSE = read("workflow/codex_only/CLOSE.md")
ORCHESTRATION = read("workflow/codex/CODEX_ORCHESTRATION.md")


class CodexOnlyOrchestrationRecoveryContractTests(unittest.TestCase):
    def test_manifest_binding_schema_is_minimal_and_workstream_local(self):
        lines = TEMPLATE.splitlines()
        start = lines.index("orchestration:")
        fields = []
        for line in lines[start + 1 :]:
            if line and not line.startswith(" "):
                break
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                fields.append(stripped.split(":", 1)[0])
        self.assertEqual(
            fields,
            ["runtime_owner", "policy_ref", "contract_fingerprint"],
        )
        self.assertIn("workstream-local routing/recovery metadata", WORKSTREAMS)
        self.assertIn("must not be mirrored into root `PROJECT.md`", WORKSTREAMS)

    def test_current_context_latch_is_nondurable_even_same_version(self):
        self.assertIn("current_context_binding_valid", KERNEL)
        self.assertIn("is non-durable and is never serialized", KERNEL)
        self.assertIn("same-version context reconstruction still requires re-bind", KERNEL)
        self.assertIn(
            "is never inferred from the existence of a durable binding or from a matching",
            KERNEL,
        )
        self.assertNotIn("current_context_binding_valid:", TEMPLATE)
        self.assertNotIn("current_context_binding_valid:", TASK_BOARD_TEMPLATE)

    def test_intake_establishes_binding_and_recovery_distinguishes_schema_age(self):
        self.assertIn(
            "Immediately after the manifest exists, establish its usable orchestration binding",
            INTAKE,
        )
        self.assertIn("Before setting `intake.state: complete`", INTAKE)
        self.assertIn("has **no `orchestration` block**", RECOVERY)
        self.assertIn(
            "block already exists but required `runtime_owner` / `policy_ref` values are missing",
            RECOVERY,
        )
        self.assertIn("do not reinterpret it as legacy absence", RECOVERY)

    def test_reconstruction_requires_conditional_kernel_and_rebind(self):
        self.assertIn(
            "After known coordinator context loss/compaction/repository-only reconstruction",
            ROUTER,
        )
        self.assertIn("Load `ORCHESTRATION_KERNEL.md` conditionally", ROUTER)
        self.assertIn(
            "before the first policy-dependent realization/re-realization",
            ROUTER,
        )
        self.assertIn(
            "Do not reload this recovery material on ordinary role transitions",
            ROUTER,
        )

    def test_all_runtime_realization_routes_share_one_generic_gate(self):
        gate = "workflow/codex/CODEX_ORCHESTRATION.md#Codex-only pre-dispatch binding gate"
        for text in (EXECUTION, REVIEW, PLAN_REVIEW, RESEARCH):
            self.assertIn(gate, text)
        self.assertIn("does not realize batch workers", EXECUTION_PREP)
        self.assertIn("does not directly realize its Tester", CLOSE)
        self.assertIn("This gate is role-agnostic", ORCHESTRATION)

    def test_missing_or_unresolvable_binding_fails_closed_without_fallback(self):
        self.assertIn(
            "A missing, stale, contradictory or unresolvable binding does not authorize another harness",
            KERNEL,
        )
        self.assertIn(
            "must not silently fall back to native/internal worker realization",
            KERNEL,
        )
        self.assertIn("preserve the accepted Project Workflow `execution_policy`", KERNEL)
        self.assertIn("normal concrete runtime blocker", KERNEL)

    def test_runtime_contract_drift_requires_policy_reresolution(self):
        self.assertIn("treat the durable binding as stale", KERNEL)
        self.assertIn(
            "re-resolve the same selected opaque policy/profile through `runtime_owner`",
            KERNEL,
        )
        self.assertIn(
            "refresh the manifest binding/fingerprint only after successful resolution",
            KERNEL,
        )
        self.assertIn(
            "A matching fingerprint only means no detected contract drift",
            KERNEL,
        )

    def test_concrete_runtime_identity_and_role_map_remain_external(self):
        self.assertIn(
            "Never persist worker/session/process/model-instance/invocation/lease/resume/worktree identity",
            KERNEL,
        )
        self.assertIn(
            "Project Workflow does not enumerate or infer which concrete harness/model",
            KERNEL,
        )
        self.assertIn("interpretation of `policy_ref`", KERNEL)
        self.assertIn("concrete role→harness/model/reasoning selection", KERNEL)
        self.assertIn(
            "Project Workflow must not duplicate/fork those mechanics",
            ORCHESTRATION,
        )

    def test_canonical_invariants_and_bounded_read_set_remain_authoritative(self):
        for item in (
            "accepted `execution_policy`",
            "exact current workstream/routing owner",
            "Card/milestone execution",
            "plan review / Card review / milestone review / workstream final-integration review",
            "implementation/reviewer separation",
            "deterministic continuation versus real stop",
        ):
            self.assertIn(item, KERNEL)
        for item in (
            "root `PROJECT.md`",
            "branch-isolated `WORKSTREAM.yaml`",
            "this kernel",
            "exact canonical state record",
        ):
            self.assertIn(item, KERNEL)
        self.assertIn("Do not load the whole Master Plan", KERNEL)

    def test_chatgpt_only_context_health_remains_unchanged(self):
        self.assertTrue((ROOT / "workflow/chatgpt_only/CONTEXT_HEALTH.md").is_file())
        chatgpt_router = read("workflow/chatgpt_only/ROUTER.md")
        self.assertIn("Context-health trigger", chatgpt_router)
        self.assertFalse((ROOT / "workflow/codex_only/CONTEXT_HEALTH.md").exists())


if __name__ == "__main__":
    unittest.main()
