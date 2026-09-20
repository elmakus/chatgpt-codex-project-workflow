#!/usr/bin/env python3
"""Bounded Project Workflow SessionStart bootstrap."""

from __future__ import annotations

import json
import os
from pathlib import Path


MAX_CONTEXT_CHARS = 900


def plugin_root() -> Path:
    configured = os.environ.get("PLUGIN_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    return Path(__file__).resolve().parents[1]


def build_context(root: Path) -> str:
    router = root / "workflow" / "CONTEXT_ROUTING.md"
    if router.is_file():
        context = (
            "Project Workflow is enabled for this workspace. "
            "Read the workspace repository's PROJECT.md first, then read the canonical "
            f"Project Workflow router at {router}. "
            "Follow only the execution policy selected there and load route modules, durable "
            "state, authority, and evidence progressively as required. "
            "Durable repository state outranks chat recollection. "
            "The bundled $pw:project-workflow Skill is an explicit entry/recovery path; "
            "this SessionStart reminder is not workflow policy."
        )
    else:
        context = (
            "Project Workflow is enabled, but its canonical router is missing at "
            f"{router}. Treat this as a blocking plugin-package error and do not invent "
            "or reconstruct Project Workflow policy from this bootstrap."
        )
    return context[:MAX_CONTEXT_CHARS]


def main() -> None:
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": build_context(plugin_root()),
        }
    }
    print(json.dumps(output, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
