from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    name: (ROOT / "workflow/codex_only" / name).read_text(encoding="utf-8")
    for name in (
        "ROUTER.md",
        "EXECUTION_PREP.md",
        "EXECUTION.md",
        "STATE.md",
        "RECOVERY.md",
        "CLOSE.md",
        "MICRO_FIX.md",
        "TASK_CARDS.md",
        "TASK_CARD_TEMPLATE.md",
        "REPOSITORY.md",
        "REVIEW.md",
        "RESEARCH.md",
        "WORKSTREAMS.md",
        "TASK_BOARD_TEMPLATE.yaml",
        "WORKSTREAM_TASK_BOARD_TEMPLATE.yaml",
    )
}


class CodexOnlyBranchFirstExecutionStateTests(unittest.TestCase):
    def test_execution_prep_never_scaffolds_root_default_board(self):
        prep = FILES["EXECUTION_PREP.md"]
        self.assertIn(
            "Root `implementation/TASK_BOARD.yaml` and "
            "`workflow/codex_only/TASK_BOARD_TEMPLATE.yaml` are historical "
            "recovery/migration surfaces only and MUST NOT be scaffolded, selected or mutated",
            prep,
        )
        self.assertIn("WORKSTREAM_TASK_BOARD_TEMPLATE.yaml", prep)
        self.assertIn("manifest-selected workstream Task Board", prep)

    def test_state_contract_requires_manifest_bound_workstream_board(self):
        state = FILES["STATE.md"]
        self.assertIn(
            "Historical root/default `implementation/TASK_BOARD.yaml` is "
            "recovery/migration input only; it MUST NOT be selected or mutated",
            state,
        )
        self.assertIn(
            "root/default `implementation/TASK_BOARD.yaml` selected or mutated "
            "as active state",
            state,
        )
        self.assertIn("manifest-selected branch-isolated Task Board", state)

    def test_historical_default_routes_through_migration_before_mutation(self):
        recovery = FILES["RECOVERY.md"]
        self.assertIn("## Historical root/default migration before mutation", recovery)
        self.assertIn(
            "migration itself outranks review, Research, Execution Prep, batch recovery and Execution",
            recovery,
        )
        self.assertIn(
            "This discovery is read-only with respect to root/default execution state",
            recovery,
        )
        self.assertIn(
            "Only after that readback is GREEN may the namespaced Task Board become "
            "the selected mutable execution state",
            recovery,
        )
        self.assertIn(
            "retry/recover the same deterministic migration identity **and topology** without mutating "
            "the source root board",
            recovery,
        )

    def test_historical_migration_proves_topology_before_branch_creation(self):
        recovery = FILES["RECOVERY.md"]
        router = FILES["ROUTER.md"]
        self.assertIn(
            "Recover one exact migration topology **before branch creation or adoption**",
            recovery,
        )
        self.assertIn("INTAKE.md#Base and dependency classification", recovery)
        self.assertIn("integration_target", recovery)
        self.assertIn("base_ref", recovery)
        self.assertIn("parent_dependency", recovery)
        self.assertIn("fail closed before creating/adopting a branch", recovery)
        self.assertIn(
            "INTAKE.md` only when historical root/default migration",
            router,
        )

    def test_migration_preserves_codex_review_and_batch_lineage(self):
        recovery = FILES["RECOVERY.md"]
        self.assertIn("semantic `implementation_owner_role`", recovery)
        self.assertIn("append-only attempt history", recovery)
        self.assertIn("complete `parallel.current_batch`", recovery)
        self.assertIn("frozen base, membership/order, returned/integrated refs", recovery)
        self.assertIn("post-batch review-drain lineage", recovery)
        self.assertIn("Never reinterpret a historical lane as a new batch", recovery)

    def test_binding_mismatch_and_historical_selection_fail_closed(self):
        router = FILES["ROUTER.md"]
        workstreams = FILES["WORKSTREAMS.md"]
        self.assertIn(
            "route to Recovery before further managed-change mutation",
            router,
        )
        self.assertIn("Branch-isolated binding mismatch is Recovery", router)
        self.assertIn(
            "mismatched/null `execution_ref.branch` is inconsistent branch-isolated state",
            workstreams,
        )
        self.assertIn(
            "route to Recovery rather than falling back to the legacy/default board",
            workstreams,
        )

    def test_codex_main_tester_and_research_ownership_are_preserved(self):
        self.assertIn(
            "Codex Main remains the sole writer of shared Task Board/integration state",
            FILES["EXECUTION_PREP.md"],
        )
        self.assertIn(
            "Codex Main is the sole writer of shared Project Workflow Task Board and integration state",
            FILES["STATE.md"],
        )
        self.assertIn("independent Tester", FILES["REVIEW.md"])
        self.assertIn(
            "selected canonical Task Board → `research_obligation`",
            FILES["RESEARCH.md"],
        )
        self.assertIn(
            "The manifest `review` block is reserved for a **workstream-level final integration review**",
            FILES["WORKSTREAMS.md"],
        )

    def test_bounded_batch_and_post_batch_drain_remain_intact(self):
        prep = FILES["EXECUTION_PREP.md"]
        state = FILES["STATE.md"]
        execution = FILES["EXECUTION.md"]
        self.assertIn("Serial execution is always the safe/default shape", prep)
        self.assertIn("## Freeze batch state", prep)
        self.assertIn("current parallel batch", state)
        self.assertIn("post-batch review drain", state)
        self.assertIn("Bounded same-member retry", execution)
        self.assertIn("post-batch review drain", execution)

    def test_micro_fix_refresh_and_terminal_recovery_remain_intact(self):
        micro = FILES["MICRO_FIX.md"]
        close = FILES["CLOSE.md"]
        recovery = FILES["RECOVERY.md"]
        self.assertIn(
            "normal selected-workstream `EXECUTION.md`, `STATE.md`, "
            "`REVIEW.md`, `RESEARCH.md` and `RECOVERY.md` semantics apply",
            micro,
        )
        self.assertIn("## Branch-isolated integration refresh gate", close)
        self.assertIn("## Integrated terminal workstream recovery", recovery)
        self.assertIn(
            "never a reason to fall back to root `implementation/TASK_BOARD.yaml`",
            recovery,
        )

    def test_historical_artifacts_are_preserved_but_not_active(self):
        repository = FILES["REPOSITORY.md"]
        template = FILES["TASK_BOARD_TEMPLATE.yaml"]
        close = FILES["CLOSE.md"]
        self.assertIn(
            "Historical root/default state remains readable for recovery and provenance",
            repository,
        )
        self.assertIn(
            "Do not rewrite historical evidence/handoffs solely because the state model changed",
            repository,
        )
        self.assertIn(
            "Recovery/migration compatibility only: do NOT scaffold this template",
            template,
        )
        self.assertIn(
            "Historical root/default handoffs under `project-handoffs/` remain readable",
            close,
        )

    def test_task_contract_surfaces_do_not_offer_root_default_active_state(self):
        self.assertIn(
            "Historical root/default `implementation/TASK_BOARD.yaml` is "
            "recovery/migration input only",
            FILES["TASK_CARDS.md"],
        )
        self.assertIn(
            "Historical root/default `implementation/TASK_BOARD.yaml` is "
            "recovery/migration input only",
            FILES["TASK_CARD_TEMPLATE.md"],
        )
        self.assertIn(
            "Active Codex-only managed execution uses the exact manifest-bound "
            "WORKSTREAM_TASK_BOARD_TEMPLATE.yaml",
            FILES["TASK_BOARD_TEMPLATE.yaml"],
        )
        self.assertIn(
            "Codex-only branch-isolated Task Board",
            FILES["WORKSTREAM_TASK_BOARD_TEMPLATE.yaml"],
        )
        self.assertNotIn(
            "same M02 provenance/review shape as the default board",
            FILES["WORKSTREAM_TASK_BOARD_TEMPLATE.yaml"],
        )

    def test_runtime_identity_stays_outside_durable_state(self):
        recovery = FILES["RECOVERY.md"]
        state = FILES["STATE.md"]
        self.assertIn(
            "Concrete worker/session/model-instance/invocation/worktree identity is never migrated",
            recovery,
        )
        self.assertIn(
            "opaque manifest policy/profile selection is established through the runtime owner",
            recovery,
        )
        self.assertIn(
            "Runtime worker identity and lifecycle are not Project Workflow state",
            state,
        )

    def test_repository_recovery_uses_manifest_and_workstream_state(self):
        repository = FILES["REPOSITORY.md"]
        self.assertIn("selected manifest `routing.exploratory_scope`", repository)
        self.assertIn("selected manifest `routing.research_obligation`", repository)
        self.assertIn(
            "historical root/default Task Board and PROJECT routing pointers are read only as Recovery migration input",
            repository,
        )

    def test_codex_only_lifecycle_does_not_import_chatgpt_only_modules(self):
        for name, text in FILES.items():
            self.assertNotIn(
                "workflow/chatgpt_only/",
                text,
                msg=f"{name} imports ChatGPT-only lifecycle semantics",
            )


if __name__ == "__main__":
    unittest.main()
