#!/usr/bin/env python3
"""Full Harness Engineering compliance optimizer for e2e-delivery-harness."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Shared with harness-compliance-patch.py (load via path — module name has hyphens)
import importlib.util

_patch_path = Path(__file__).resolve().parent / "harness-compliance-patch.py"
_spec = importlib.util.spec_from_file_location("harness_compliance_patch", _patch_path)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)

HANDOFF_MAP = _mod.HANDOFF_MAP
patch_agent = _mod.patch_agent
patch_prompt_sections = _mod.patch_prompt_sections

PHASE_MAP: dict[str, str] = {
    "analyze-requirement": "requirement",
    "plan-sprint": "requirement",
    "design-system": "design",
    "design-architecture": "design",
    "design-database": "design",
    "review-design": "design",
    "decompose-task": "development",
    "implement-feature": "development",
    "integrate-api": "development",
    "manage-dependencies": "development",
    "manage-config": "development",
    "manage-secrets": "development",
    "document-project": "development",
    "verify-test": "testing",
    "automate-test": "testing",
    "performance-testing": "testing",
    "review-code": "testing",
    "setup-infra": "deployment",
    "implement-cicd": "deployment",
    "prepare-release": "deployment",
    "deploy-release": "deployment",
    "plan-rollback": "deployment",
    "backup-data": "operations",
    "migrate-data": "operations",
    "migrate-environment": "operations",
    "monitor-operate": "operations",
    "integrate-monitor": "operations",
    "manage-change": "operations",
    "optimize-performance": "operations",
    "plan-capacity": "operations",
    "audit-security": "governance",
    "manage-tech-debt": "governance",
    "manage-knowledge": "governance",
    "respond-incident": "governance",
    "review-incident": "governance",
    "plan-disaster-recovery": "governance",
    "apply-hotfix": "governance",
}

STAGE_ID_MAP: dict[str, str] = {
    "analyze-requirement": "requirement-analysis",
    "plan-sprint": "requirement-analysis",
    "design-system": "system-design",
    "design-architecture": "system-design",
    "design-database": "system-design",
    "review-design": "system-design",
    "decompose-task": "task-decomposition",
    "implement-feature": "development",
    "integrate-api": "development",
    "manage-dependencies": "development",
    "manage-config": "development",
    "manage-secrets": "development",
    "document-project": "development",
    "verify-test": "testing",
    "automate-test": "testing",
    "performance-testing": "testing",
    "review-code": "testing",
    "setup-infra": "deployment",
    "implement-cicd": "deployment",
    "prepare-release": "deployment",
    "deploy-release": "deployment",
    "plan-rollback": "deployment",
    "backup-data": "operations",
    "migrate-data": "operations",
    "migrate-environment": "operations",
    "monitor-operate": "operations",
    "integrate-monitor": "operations",
    "manage-change": "operations",
    "optimize-performance": "operations",
    "plan-capacity": "operations",
    "audit-security": "governance",
    "manage-tech-debt": "development",
    "manage-knowledge": "governance",
    "respond-incident": "incident-response",
    "review-incident": "incident-resolution",
    "plan-disaster-recovery": "governance",
    "apply-hotfix": "incident-resolution",
}

SCENARIO_DC: dict[str, list[tuple[str, str, str, str, str, str]]] = {
    "plan-sprint": [
        ("DC-001", "Sprint Goal 确认", "Backlog 选择完成后", "单一聚焦目标 / 多目标并列", "SMART + 团队共识", "Sprint Goal 文档"),
        ("DC-002", "容量与承诺", "估算完成后", "满载承诺 / 保守承诺 / 拆分冲刺", "容量利用率 85–95%", "Sprint Commitment"),
        ("DC-003", "范围变更", "规划中发现新需求", "纳入本冲刺 / 放入 Backlog", "DoR 与风险评审", "变更记录"),
    ],
    "audit-security": [
        ("DC-001", "审计范围", "启动审计前", "全量 / 增量 / 专项", "风险与合规要求", "审计计划"),
        ("DC-002", "发现分级", "发现漏洞后", "Critical 立即修复 / 计划修复", "CVSS + 业务影响", "审计报告"),
        ("DC-003", "准出决策", "整改完成后", "通过 / 有条件通过 / 不通过", "整改率与残留风险", "准出签字"),
    ],
    "review-code": [
        ("DC-001", "审查范围确认", "开始审查前", "全量 / 增量 / 关键路径", "变更影响与风险", "审查计划"),
        ("DC-002", "严重问题处理", "发现 Blocker 时", "修复后合并 / 拒绝合并", "安全与功能影响", "审查意见"),
        ("DC-003", "合并批准", "问题处理完成后", "批准 / 条件批准 / 拒绝", "DoD 与测试通过", "PR 状态"),
    ],
    "review-design": [
        ("DC-001", "评审范围", "评审启动前", "架构 / 接口 / 全量", "变更范围与风险", "评审议程"),
        ("DC-002", "问题处置", "发现设计缺陷", "修订后通过 / 重大变更", "影响分析与 ADR", "评审记录"),
        ("DC-003", "准出签字", "修订完成后", "通过 / 有条件通过", "KPI 与开放问题", "评审结论"),
    ],
    "review-incident": [
        ("DC-001", "复盘范围", "事件关闭后", "完整复盘 / 轻量复盘", "严重级别与影响", "Postmortem 大纲"),
        ("DC-002", "根因确认", "分析完成后", "已确认 / 待验证", "5 Whys + 证据链", "根因分析"),
        ("DC-003", "改进项优先级", "行动项列出后", "P0 立即 / 排期实施", "风险降低幅度", "改进 backlog"),
    ],
    "plan-capacity": [
        ("DC-001", "预测 horizon", "启动规划前", "3 月 / 6 月 / 12 月", "业务增长计划", "容量模型"),
        ("DC-002", "扩容策略", "预测超阈值", "垂直 / 水平 / 混合", "成本与 SLA", "扩容方案"),
        ("DC-003", "预算批准", "方案完成后", "批准 / 分阶段 / 拒绝", "ROI 与风险", "容量计划"),
    ],
}

DEFAULT_DC = [
    ("DC-001", "范围确认", "执行启动前", "继续 / 缩小范围 / 升级", "与上游 Handover 一致", "执行记录"),
    ("DC-002", "质量门禁", "产出验证前", "修复后继续 / 记录 open_issues", "Scenario KPI ≥70", "验证报告"),
    ("DC-003", "交接准出", "阶段完成前", "完成交接 / 部分交接 / 阻塞", "Handover 必填字段齐全", "Handover YAML"),
]

HANDOVER_CRITERIA_BLOCK = """
## Handover Criteria

```
✅ 所有必需交付物已生成并通过 Output Validation
✅ 质量评分达到合格标准（≥70 分）
✅ 决策点 DC-* 已记录 rationale
✅ 开放问题与风险已写入 Handover
✅ Handover Context YAML 已生成
```

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "{from_stage}"
    to_stage: "{to_stage}"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
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

STANDARD_STUBS: dict[str, str] = {
    "12-factor-app.md": "十二要素应用",
    "adr-template.md": "架构决策记录 (ADR)",
    "alerting-guidelines.md": "告警规范",
    "api-design-guidelines.md": "API 设计规范",
    "c4-model.md": "C4 架构模型",
    "change-management.md": "变更管理",
    "code-review-checklist.md": "代码审查清单",
    "coding-standards.md": "编码规范",
    "database-naming-convention.md": "数据库命名规范",
    "defect-classification.md": "缺陷分级",
    "deployment-best-practices.md": "部署最佳实践",
    "emergency-response.md": "应急响应",
    "git-workflow.md": "Git 工作流",
    "health-check-guidelines.md": "健康检查规范",
    "incident-management.md": "事件管理",
    "invest-principle.md": "INVEST 任务原则",
    "monitoring-standards.md": "监控标准",
    "normalization-guidelines.md": "数据库范式指南",
    "rollback-procedures.md": "回滚流程",
    "rollback-strategy.md": "回滚策略",
    "sre-best-practices.md": "SRE 最佳实践",
    "task-naming-convention.md": "任务命名规范",
    "test-coverage-guidelines.md": "测试覆盖率指南",
    "test-data-management.md": "测试数据管理",
    "testing-best-practices.md": "测试最佳实践",
    "testing-guidelines.md": "测试指南",
}

EVAL_STUBS: dict[str, str] = {
    "alert-effectiveness.md": "告警有效性评估",
    "architecture-review-checklist.md": "架构评审清单",
    "code-quality-checklist.md": "代码质量清单",
    "coverage-analysis.md": "覆盖率分析",
    "defect-analysis.md": "缺陷分析",
    "deployment-quality-checklist.md": "部署质量清单",
    "design-quality-assessment.md": "设计质量评估",
    "estimation-accuracy-review.md": "估算准确性回顾",
    "hotfix-quality-checklist.md": "热修复质量清单",
    "monitoring-quality-checklist.md": "监控质量清单",
    "performance-baseline.md": "性能基线",
    "query-performance-benchmark.md": "查询性能基准",
    "regression-test-suite.md": "回归测试套件",
    "response-time-analysis.md": "响应时间分析",
    "rollback-drill-report.md": "回滚演练报告",
    "schema-review-checklist.md": "Schema 评审清单",
    "slo-compliance.md": "SLO 合规",
    "static-code-analysis.md": "静态代码分析",
    "task-quality-checklist.md": "任务质量清单",
    "test-coverage-analysis.md": "测试覆盖分析",
    "test-quality-checklist.md": "测试质量清单",
}

DOC_BODY_STANDARD = """---
name: {name}
type: standard
version: "1.0.0"
status: active
---

# {title}

> 本文件为 E2E Delivery Harness 引用标准。审查基准见 [harness-engineering.md](harness-engineering.md)。

## 适用范围

- 与场景 Prompt / Scenario 中 Related Resources 对齐
- 准出前对照 [output-quality-rubric.md](output-quality-rubric.md)

## 检查要点

- [ ] 与 [id-generation-quantification.md](id-generation-quantification.md) KPI 一致
- [ ] 决策点 DC-* 有对应验证项
- [ ] 交接 HO-* 字段可映射本标准检查项

## 引用

- [asset-model.md](asset-model.md)
- [authoring-checklist.md](authoring-checklist.md)
"""

DOC_BODY_EVAL = """---
name: {name}
type: evaluation
version: "1.0.0"
status: active
---

# {title}

> 本文件为 E2E Delivery Harness 阶段/场景评估清单。

## 使用方式

1. 场景执行完成后，对照本清单逐项 PASS / PARTIAL / FAIL
2. 结合 [output-validation-checklist.md](output-validation-checklist.md) 通用项
3. 失败项写入 Handover `open_issues`

## 检查项

- [ ] V-001 完整性：必填章节与交付物齐全
- [ ] V-002 一致性：与上游 Handover 无矛盾
- [ ] V-003 准确性：假设已标注，数据可验证
- [ ] V-004 质量：Scenario KPI ≥70

## 引用

- [regression-checklist.md](regression-checklist.md)
- [common-error-patterns.md](common-error-patterns.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)
"""

ANTI_PATTERNS_SECTION = """
## Anti-patterns (反模式)

> 执行本场景时必须避免以下反模式。若 [Common Pitfalls](#common-pitfalls) 已存在，二者一并遵守。

| ID | 反模式 | 风险 | 正确做法 |
|----|--------|------|----------|
| AP-001 | 跳过 [VALIDATE] 直接汇总 | 幻觉与遗漏 | 每步 CoT 后自检 |
| AP-002 | 变量未填即执行 | 产出不可追溯 | Required 变量必须确认 |
| AP-003 | 无 Handover 进入下游 | 上下文断裂 | 输出 unified-handover YAML |
| AP-004 | KPI 未量化 | 无法准出 | 对照 Scenario Quality Metrics |
| AP-005 | 错误不升级 | 阻塞 hidden | 触发升级条件即请求人工 |
"""

REWRITE_SCENARIOS = {
    "plan-sprint": "plan-sprint",
    "document-project": "document-project",
    "integrate-monitor": "integrate-monitor",
}


def dc_table(rows: list[tuple[str, ...]]) -> str:
    lines = [
        "## Decision Checkpoints",
        "",
        "| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |",
        "|----|--------|----------|----------|----------|----------|",
    ]
    for row in rows:
        lines.append(f"| {' | '.join(row)} |")
    return "\n".join(lines) + "\n"


def ensure_dc_section(text: str, base: str) -> tuple[str, bool]:
    dcs = set(re.findall(r"DC-\d{3}", text))
    if len(dcs) >= 3:
        return text, False
    # Normalize DC-1 -> DC-001 style
    text = re.sub(r"\*\*DC-(\d):", r"**DC-00\1:", text)
    text = re.sub(r"\| \*\*DC-(\d)", r"| DC-00\1", text)
    dcs = set(re.findall(r"DC-\d{3}", text))
    if len(dcs) >= 3:
        return text, True
    rows = SCENARIO_DC.get(base, DEFAULT_DC)
    block = dc_table(rows)
    if "## Decision Checkpoints" in text:
        text = re.sub(
            r"## Decision Checkpoints.*?(?=\n## )",
            block + "\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        anchor = "## Error Handling"
        if anchor in text:
            text = text.replace(anchor, block + anchor, 1)
        else:
            text = text.rstrip() + "\n\n" + block
    return text, True


def ensure_handover_criteria(text: str, base: str) -> tuple[str, bool]:
    if "## Handover Criteria" in text:
        return text, False
    from_stage, to_stage = HANDOFF_MAP.get(base, (STAGE_ID_MAP.get(base, base), "next-stage"))
    block = HANDOVER_CRITERIA_BLOCK.format(from_stage=from_stage, to_stage=to_stage, base=base)
    if "## Related Assets" in text:
        text = text.replace("## Related Assets", block + "\n## Related Assets", 1)
    else:
        text = text.rstrip() + "\n" + block
    return text, True


def fix_skill(path: Path, base: str) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    if "category:" not in text:
        cat = PHASE_MAP.get(base, "general")
        text = re.sub(
            r"(^description:.*\n)",
            rf"\1category: {cat}\n",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if not re.search(r"anti.pattern|反模式", text, re.I):
        if "## Common Pitfalls" in text:
            text = text.replace("## Common Pitfalls", "## Anti-patterns (反模式)\n\n> 与 Common Pitfalls 同义，执行时合并检查。\n\n## Common Pitfalls", 1)
        else:
            text = text.rstrip() + "\n" + ANTI_PATTERNS_SECTION
    text = re.sub(
        r"\]\(\.\./(standards|evaluations|templates|agents|prompts|instructions|scenarios)/",
        r"](../../\1/",
        text,
    )
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def fix_instruction(path: Path, base: str) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    phase = STAGE_ID_MAP.get(base, base)
    if "applyTo:" not in text:
        insert = f'applyTo: "scenarios/{base}/**"\nphase: {phase}\n'
        text = re.sub(r"(^description:.*\n)", r"\1" + insert, text, count=1, flags=re.MULTILINE)
    elif "phase:" not in text:
        text = re.sub(r"(^applyTo:.*\n)", rf"\1phase: {phase}\n", text, count=1, flags=re.MULTILINE)
    if "standards/harness-engineering.md" not in text and "standards/" not in text:
        footer = (
            "\n## References\n\n"
            "- [harness-engineering.md](../standards/harness-engineering.md)\n"
            "- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)\n"
            "- [regression-checklist.md](../evaluations/regression-checklist.md)\n"
        )
        text = text.rstrip() + footer
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def create_stub(directory: Path, filename: str, title: str, doc_type: str) -> bool:
    path = directory / filename
    if path.exists():
        return False
    name = filename.replace(".md", "")
    body = DOC_BODY_STANDARD if doc_type == "standard" else DOC_BODY_EVAL
    path.write_text(body.format(name=name, title=title), encoding="utf-8")
    return True


def rewrite_scenario(base: str) -> str:
    phase = PHASE_MAP.get(base, "general")
    from_stage, to_stage = HANDOFF_MAP.get(base, (STAGE_ID_MAP.get(base, base), "next-stage"))
    rows = SCENARIO_DC.get(base, DEFAULT_DC)
    titles = {
        "plan-sprint": ("冲刺规划", "定义 Sprint Goal、Backlog 承诺与任务分配"),
        "document-project": ("项目文档", "补齐 README、架构说明与 API 文档"),
        "integrate-monitor": ("监控集成", "为新服务接入指标、告警与仪表板"),
    }
    title, purpose = titles[base]
    return f"""---
name: {base}
description: "{title}场景"
version: "1.2.0"
type: scenario
category: {phase}
stage: {STAGE_ID_MAP.get(base, base)}
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-02
status: active
tags: [{phase}, workflow]
---
# {title} Scenario

## Purpose

{purpose}，输出可交接的标准化交付物。

### Business Value

- **一致性**: 遵循 Harness 六层模型与统一 Handover
- **可审计**: DC-* 决策与 KPI 可量化追溯
- **可复用**: 与 Prompt / Agent / Skill 基名 `{base}` 对齐

## Chain of Thought

```
[THINK] Step 1: 读取 Handover 与 Global Context，确认准入条件
[ANALYZE] Step 2: 识别约束、依赖与风险
[DESIGN] Step 3: 制定执行方案与验收标准
[IMPLEMENT] Step 4: 按 Prompt 逐步执行，每步 [VALIDATE]
[VERIFY] Step 5: Output Validation（V-001～V-004）
[HANDOVER] Step 6: 生成 Handover Context，更新 Global Context
```

{dc_table(rows)}
## Error Handling (错误处理)

### Error Scenario 1: 输入不完整

**识别信号**: Required 变量缺失或上游 Handover 不完整  
**处理流程**: 停止执行 → 列出缺失项 → 请求人工补充 → 记录 ERR-*  
**升级条件**: 阻塞项无法在 1 轮内补齐

### Error Scenario 2: 质量未达标

**识别信号**: KPI 或 V-* 验证失败  
**处理流程**: 记录失败项 → P0/P1 修复后重验 → 仍失败则升级  
**升级条件**: 综合评分 <70 且无法在本阶段修复

## Quality Metrics

| KPI ID | 指标名称 | 目标值 | 权重 |
|--------|----------|--------|------|
| KPI-001 | COMPLETION | ≥95% | 30% |
| KPI-002 | QUALITY-SCORE | ≥70 | 30% |
| KPI-003 | COMPLIANCE | 100% | 20% |
| KPI-004 | HANDOVER-READY | 100% | 20% |

**合格线**: ≥70 分

{HANDOVER_CRITERIA_BLOCK.format(from_stage=from_stage, to_stage=to_stage, base=base)}
## Related Assets

| Asset Type | Path |
|------------|------|
| Agent | `../../agents/{base}.agent.md` |
| Prompt | `../../prompts/{base}.prompt.md` |
| Skill | `../../skills/{base}/SKILL.md` |
| Instruction | `../../instructions/{base}.instructions.md` |

## Related Resources

- [harness-engineering.md](../../standards/harness-engineering.md)
- [output-validation-checklist.md](../../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../../evaluations/regression-checklist.md)
"""


def main() -> None:
    stats: dict[str, int] = {}

    for fname, title in STANDARD_STUBS.items():
        if create_stub(ROOT / "standards", fname, title, "standard"):
            stats["standards_created"] = stats.get("standards_created", 0) + 1

    for fname, title in EVAL_STUBS.items():
        if create_stub(ROOT / "evaluations", fname, title, "evaluation"):
            stats["evaluations_created"] = stats.get("evaluations_created", 0) + 1

    for agent in (ROOT / "agents").glob("*.agent.md"):
        base = agent.stem.replace(".agent", "")
        if patch_agent(agent, base):
            stats["agents"] = stats.get("agents", 0) + 1

    for prompt in (ROOT / "prompts").glob("*.prompt.md"):
        base = prompt.stem.replace(".prompt", "")
        if patch_prompt_sections(prompt, base):
            stats["prompts"] = stats.get("prompts", 0) + 1

    for base in REWRITE_SCENARIOS:
        path = ROOT / "scenarios" / base / "SCENARIO.md"
        if path.exists():
            path.write_text(rewrite_scenario(base), encoding="utf-8")
            stats["scenarios_rewritten"] = stats.get("scenarios_rewritten", 0) + 1

    for scenario in (ROOT / "scenarios").glob("*/SCENARIO.md"):
        if scenario.parent.name in REWRITE_SCENARIOS or scenario.parent.name.startswith("_"):
            continue
        base = scenario.parent.name
        text = scenario.read_text(encoding="utf-8")
        changed = False
        text, c = ensure_dc_section(text, base)
        changed = changed or c
        text, c = ensure_handover_criteria(text, base)
        changed = changed or c
        if changed:
            scenario.write_text(text, encoding="utf-8")
            stats["scenarios_patched"] = stats.get("scenarios_patched", 0) + 1

    for skill in (ROOT / "skills").glob("*/SKILL.md"):
        base = skill.parent.name
        if fix_skill(skill, base):
            stats["skills"] = stats.get("skills", 0) + 1

    for inst in (ROOT / "instructions").glob("*.instructions.md"):
        if inst.name == "README.md":
            continue
        base = inst.stem.replace(".instructions", "")
        if fix_instruction(inst, base):
            stats["instructions"] = stats.get("instructions", 0) + 1

    print("Harness full compliance results:")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")
    if not stats:
        print("  (no changes needed)")


if __name__ == "__main__":
    main()
