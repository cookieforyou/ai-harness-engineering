---
name: plan-sprint
description: "冲刺规划场景"
version: "1.2.0"
type: scenario
category: requirement
stage: analyze-requirement
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-02
status: active
tags: [requirement, workflow]
---
# 冲刺规划 Scenario

## Purpose

定义 Sprint Goal、Backlog 承诺与任务分配，输出可交接的标准化交付物。

### Business Value

- **一致性**: 遵循 Harness 六层模型与统一 Handover
- **可审计**: DC-* 决策与 KPI 可量化追溯
- **可复用**: 与 Prompt / Agent / Skill 基名 `plan-sprint` 对齐

## Chain of Thought

```
[THINK] Step 1: 读取 Handover 与 Global Context，确认准入条件
[ANALYZE] Step 2: 识别约束、依赖与风险
[DESIGN] Step 3: 制定执行方案与验收标准
[IMPLEMENT] Step 4: 按 Prompt 逐步执行，每步 [VALIDATE]
[VERIFY] Step 5: Output Validation（V-001～V-004）
[HANDOVER] Step 6: 生成 Handover Context，更新 Global Context
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | Sprint Goal 确认 | Backlog 选择完成后 | 单一聚焦目标 / 多目标并列 | SMART + 团队共识 | Sprint Goal 文档 |
| DC-002 | 容量与承诺 | 估算完成后 | 满载承诺 / 保守承诺 / 拆分冲刺 | 容量利用率 85–95% | Sprint Commitment |
| DC-003 | 范围变更 | 规划中发现新需求 | 纳入本冲刺 / 放入 Backlog | DoR 与风险评审 | 变更记录 |

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

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | SPRINT-GOAL-CLARITY | 100% | Sprint目标明确且有量化验收标准 | Product Owner确认 | 30% |
| KPI-002 | CAPACITY-UTILIZATION | 70-85% | (承诺故事点数/团队可用容量) × 100% | 容量规划表 | 30% |
| KPI-003 | BACKLOG-HEALTH | ≥80% | (有明确验收标准的Backlog项/总Backlog项) × 100% | Backlog审查 | 20% |
| KPI-004 | STAKEHOLDER-ALIGN | ≥90% | 关键干系人对Sprint计划达成一致的比例 | 干系人反馈 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```


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
    from_stage: "analyze-requirement"
    to_stage: "decompose-task"
    handover_id: "HO-{timestamp}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "plan-sprint"
  summary:
    status: completed|partial|blocked
    quality_score: {0-100}
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

## Related Assets

| Asset Type | Path |
|------------|------|
| Agent | `../../agents/plan-sprint.agent.md` |
| Prompt | `../../prompts/plan-sprint.prompt.md` |
| Skill | `../../skills/plan-sprint/SKILL.md` |
| Instruction | `../../instructions/plan-sprint.instructions.md` |

## Related Resources

- [harness-engineering.md](../../standards/harness-engineering.md)
- [output-validation-checklist.md](../../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../../evaluations/regression-checklist.md)
