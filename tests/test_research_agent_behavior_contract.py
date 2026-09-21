from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

COMMON = (ROOT / "workflow/common/RESEARCH.md").read_text(encoding="utf-8")
CHATGPT = (ROOT / "workflow/chatgpt_only/RESEARCH.md").read_text(encoding="utf-8")
CODEX = (ROOT / "workflow/codex_only/RESEARCH.md").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "templates/RESEARCH.md").read_text(encoding="utf-8")
OPENSPEC = (
    ROOT
    / "openspec/changes/research-agent-behavior/specs/research-agent-behavior.md"
).read_text(encoding="utf-8")


class ResearchAgentBehaviorContractTests(unittest.TestCase):
    def test_research_remains_evidence_not_authority(self):
        self.assertIn(
            "Research does not directly promote itself into accepted product/system authority",
            COMMON,
        )
        for text in (CHATGPT, CODEX):
            self.assertIn(
                "Research is evidence, not accepted requirement/decision/plan authority",
                text,
            )
            self.assertIn(
                "These evidence rules do not change this module's durable continuation, "
                "Return-target/reconciliation or pointer-ownership semantics",
                text,
            )

    def test_public_prior_art_is_required_but_local_only_path_stays_proportional(self):
        self.assertIn(
            "smallest evidence path sufficient for the exact research question",
            COMMON,
        )
        self.assertIn(
            "Research MUST actively look for that prior art before defaulting to a "
            "bespoke/original solution",
            COMMON,
        )
        self.assertIn(
            "Purely repository-local or private-state questions do not require broad "
            "external discovery",
            COMMON,
        )

    def test_source_classes_and_evidentiary_weight_are_explicit(self):
        for phrase in (
            "official/upstream documentation and source",
            "changelogs and release notes",
            "upstream issues/discussions and public issue trackers",
            "comparable-project implementations",
            "practical community/forum/social reports and discussions",
        ):
            self.assertIn(phrase, COMMON)
        self.assertIn(
            "Stronger/primary/upstream evidence takes precedence when sources conflict",
            COMMON,
        )
        self.assertIn("popularity does not make it authoritative", COMMON)
        self.assertIn("Surface conflicting evidence explicitly", COMMON)

    def test_unavailable_external_path_and_bounded_stopping_are_explicit(self):
        self.assertIn(
            "If a materially required external source path is unavailable, record the "
            "concrete limitation",
            COMMON,
        )
        self.assertIn("never fabricate evidence", COMMON)
        self.assertIn(
            "Once enough source-grounded evidence exists to answer the exact question "
            "and compare meaningful alternatives, stop searching",
            COMMON,
        )

    def test_policy_local_routes_apply_same_shared_behavior(self):
        for text in (CHATGPT, CODEX):
            self.assertIn("## Shared evidence behavior", text)
            self.assertIn("Apply `workflow/common/RESEARCH.md` in full", text)
            self.assertIn("actively checks relevant external prior art", text)
            self.assertIn("surfaces conflicts explicitly", text)
            self.assertIn(
                "reports unavailable required source paths as limitations",
                text,
            )
            self.assertIn("stops once sufficient source-grounded evidence", text)

    def test_codex_investigator_realization_stays_runtime_owned(self):
        self.assertIn(
            "concrete Investigator/runtime realization remains owned by `codex_workflow`",
            CODEX,
        )
        self.assertIn("Project Workflow does not interpret `policy_ref`", CODEX)
        self.assertNotIn("Investigator model:", CODEX)
        self.assertNotIn("Investigator harness:", CODEX)

    def test_chatgpt_pointer_and_return_semantics_remain_manifest_task_board_owned(self):
        self.assertIn(
            "selected workstream manifest → `routing.research_obligation`",
            CHATGPT,
        )
        self.assertIn(
            "selected canonical Task Board → `research_obligation`",
            CHATGPT,
        )
        self.assertIn("## Final Return-target protocol", CHATGPT)

    def test_shared_template_uses_current_chatgpt_preexecution_pointer(self):
        self.assertIn(
            "selected workstream manifest `routing.research_obligation`",
            TEMPLATE,
        )
        self.assertIn(
            "selected canonical Task Board `research_obligation`",
            TEMPLATE,
        )
        self.assertNotIn("PROJECT.md → Active research obligation", TEMPLATE)
        self.assertIn("Class / evidentiary weight", TEMPLATE)

    def test_openspec_matches_behavior_boundaries(self):
        self.assertIn("## Requirement: proportional prior-art discovery", OPENSPEC)
        self.assertIn("Purely local/private questions MAY complete", OPENSPEC)
        self.assertIn("Stronger/primary evidence takes precedence", OPENSPEC)
        self.assertIn("MUST report the concrete limitation", OPENSPEC)
        self.assertIn("MUST remain owned by `codex_workflow`", OPENSPEC)
        self.assertIn(
            "selected workstream manifest `routing.research_obligation`",
            OPENSPEC,
        )


if __name__ == "__main__":
    unittest.main()
