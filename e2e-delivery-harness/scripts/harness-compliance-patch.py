#!/usr/bin/env python3
"""Batch apply Harness Engineering compliance patches to e2e-delivery-harness assets."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TOOL_MAP: dict[str, list[str]] = {
    # Requirement
    "analyze-requirement": ["search", "read", "edit", "analyze"],
    "plan-sprint": ["search", "read", "edit", "analyze"],
    # Design
    "design-system": ["search", "read", "edit", "analyze"],
    "design-architecture": ["search", "read", "edit", "analyze"],
    "design-database": ["search", "read", "edit", "analyze"],
    "review-design": ["search", "read", "analyze"],
    # Development
    "decompose-task": ["search", "read", "edit", "analyze"],
    "implement-feature": ["search", "read", "edit", "run_terminal", "test"],
    "integrate-api": ["search", "read", "edit", "run_terminal", "test"],
    "manage-dependencies": ["search", "read", "edit", "run_terminal"],
    "manage-config": ["search", "read", "edit"],
    "manage-secrets": ["search", "read", "edit"],
    "document-project": ["search", "read", "edit"],
    # Testing
    "verify-test": ["search", "read", "run_terminal", "test"],
    "automate-test": ["search", "read", "edit", "run_terminal", "test"],
    "performance-testing": ["search", "read", "run_terminal", "test"],
    "review-code": ["search", "read", "analyze"],
    # Deployment
    "setup-infra": ["search", "read", "edit", "run_terminal", "deploy"],
    "implement-cicd": ["search", "read", "edit", "run_terminal", "deploy"],
    "prepare-release": ["search", "read", "edit", "deploy"],
    "deploy-release": ["search", "read", "edit", "run_terminal", "deploy"],
    "plan-rollback": ["search", "read", "edit", "deploy"],
    # Operations
    "backup-data": ["search", "read", "run_terminal", "deploy"],
    "migrate-data": ["search", "read", "run_terminal", "deploy"],
    "migrate-environment": ["search", "read", "edit", "run_terminal", "deploy"],
    "monitor-operate": ["search", "read", "run_terminal", "monitor"],
    "integrate-monitor": ["search", "read", "edit", "monitor"],
    "manage-change": ["search", "read", "edit"],
    "optimize-performance": ["search", "read", "run_terminal", "test", "monitor"],
    "plan-capacity": ["search", "read", "analyze", "monitor"],
    # Governance
    "audit-security": ["search", "read", "analyze", "audit"],
    "manage-tech-debt": ["search", "read", "edit", "analyze"],
    "manage-knowledge": ["search", "read", "edit"],
    "respond-incident": ["search", "read", "run_terminal", "monitor", "deploy"],
    "review-incident": ["search", "read", "analyze"],
    "plan-disaster-recovery": ["search", "read", "edit", "analyze"],
    "apply-hotfix": ["search", "read", "edit", "run_terminal", "test", "deploy"],
}

HANDOFF_MAP: dict[str, tuple[str, str]] = {
    "analyze-requirement": ("requirement-analysis", "system-design"),
    "plan-sprint": ("requirement-analysis", "decompose-task"),
    "design-system": ("system-design", "decompose-task"),
    "design-architecture": ("system-design", "decompose-task"),
    "design-database": ("system-design", "implement-feature"),
    "review-design": ("system-design", "decompose-task"),
    "decompose-task": ("task-decomposition", "development"),
    "implement-feature": ("development", "testing"),
    "integrate-api": ("development", "testing"),
    "manage-dependencies": ("development", "development"),
    "manage-config": ("development", "deployment"),
    "manage-secrets": ("development", "deployment"),
    "document-project": ("development", "governance"),
    "verify-test": ("testing", "deployment"),
    "automate-test": ("testing", "testing"),
    "performance-testing": ("testing", "deployment"),
    "review-code": ("testing", "development"),
    "setup-infra": ("deployment", "deployment"),
    "implement-cicd": ("deployment", "deployment"),
    "prepare-release": ("deployment", "deployment"),
    "deploy-release": ("deployment", "operations"),
    "plan-rollback": ("deployment", "deployment"),
    "backup-data": ("operations", "operations"),
    "migrate-data": ("operations", "operations"),
    "migrate-environment": ("operations", "operations"),
    "monitor-operate": ("operations", "operations"),
    "integrate-monitor": ("operations", "operations"),
    "manage-change": ("operations", "operations"),
    "optimize-performance": ("operations", "operations"),
    "plan-capacity": ("operations", "operations"),
    "audit-security": ("governance", "governance"),
    "manage-tech-debt": ("development", "development"),
    "manage-knowledge": ("governance", "governance"),
    "respond-incident": ("incident-response", "incident-resolution"),
    "review-incident": ("incident-resolution", "governance"),
    "plan-disaster-recovery": ("governance", "operations"),
    "apply-hotfix": ("incident-resolution", "incident-review"),
}

HARNESS_LAYERS = [
    "goal",
    "strategy",
    "tooling",
    "constraint",
    "feedback",
    "observability",
]

OUTPUT_VALIDATION_SECTION = """
## Output Validation (输出验证)

> 生成最终交付物前必须完成。详见 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)。

### Mandatory Validation (V-*)

**V-001 Completeness**: 必填章节齐全；无 `{TODO}` / `[placeholder]`  
**V-002 Consistency**: 术语、数据、与上游 Handover 无矛盾  
**V-003 Accuracy**: 假设已标注；计算与引用正确  
**V-004 Quality**: Scenario KPI 达标（合格线通常 ≥70 分）

### Validation Failure Protocol

```
IF 任一 V-* 未通过
THEN 记录失败项 → P0/P1 必须修复后重验 → P2/P3 可记录 open_issues 并升级人工
```

### Self-Assessment

- Confidence: High | Medium | Low  
- Human Review Required: {列出需人工确认项}
"""

HANDOVER_SECTION_TEMPLATE = """
## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "{from_stage}"
    to_stage: "{to_stage}"
    handover_id: "HO-{{ISO8601}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{base}"
  summary:
    status: completed|partial|blocked
    quality_score: {{0-100}}
  artifacts:
    delivered: []
  decisions: []
  open_issues:
    blocking: []
    non_blocking: []
  risks: []
  quality_metrics:
    kpi_results: []
  recommendations: []
```
"""


def patch_agent(path: Path, base: str) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False
    tools = TOOL_MAP.get(base, ["search", "read", "edit", "analyze"])
    tools_line = "tools: " + str(tools).replace("'", '"')
    layers_line = "harness_layers: " + str(HARNESS_LAYERS).replace("'", '"')

    if "tools:" not in text:
        # Insert after description line in frontmatter
        text = re.sub(
            r"(^description:.*\n)",
            r"\1" + tools_line + "\n" + layers_line + "\n",
            text,
            count=1,
            flags=re.MULTILINE,
        )
        changed = True
    if "harness_layers:" not in text and "tools:" in text:
        text = re.sub(
            r"(^tools:.*\n)",
            r"\1" + layers_line + "\n",
            text,
            count=1,
            flags=re.MULTILINE,
        )
        changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


def patch_prompt_frontmatter(text: str) -> str:
    return re.sub(r"^type:\s*execution\s*$", "type: prompt", text, flags=re.MULTILINE)


def patch_prompt_sections(path: Path, base: str) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = patch_prompt_frontmatter(text)

    if "## Output Validation" not in text:
        # Insert before ## Output Format or at end
        if "## Output Format" in text:
            text = text.replace("## Output Format", OUTPUT_VALIDATION_SECTION + "\n## Output Format", 1)
        else:
            text = text.rstrip() + "\n" + OUTPUT_VALIDATION_SECTION

    if not re.search(r"## Handover (Preparation|准备)", text):
        from_stage, to_stage = HANDOFF_MAP.get(base, (base, "next-stage"))
        block = HANDOVER_SECTION_TEMPLATE.format(
            from_stage=from_stage, to_stage=to_stage, base=base
        )
        text = text.rstrip() + "\n" + block

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def patch_apply_hotfix_scenario(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "## Error Handling" in text:
        return False
    text = text.replace(
        "## Error Scenarios (错误场景)",
        "## Error Handling (错误处理)",
        1,
    )
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    agents_changed = 0
    prompts_changed = 0
    for agent in (ROOT / "agents").glob("*.agent.md"):
        base = agent.stem.replace(".agent", "")
        if patch_agent(agent, base):
            agents_changed += 1

    for prompt in (ROOT / "prompts").glob("*.prompt.md"):
        base = prompt.stem.replace(".prompt", "")
        if patch_prompt_sections(prompt, base):
            prompts_changed += 1

    scenario = ROOT / "scenarios/apply-hotfix/SCENARIO.md"
    scenario_changed = patch_apply_hotfix_scenario(scenario) if scenario.exists() else False

    print(f"agents patched: {agents_changed}")
    print(f"prompts patched: {prompts_changed}")
    print(f"apply-hotfix scenario: {scenario_changed}")


if __name__ == "__main__":
    main()
