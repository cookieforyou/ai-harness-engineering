---
name: document-project
description: "项目文档场景"
version: "1.2.0"
type: scenario
category: development
stage: implement-feature
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-02
status: active
language: "zh-CN"
tags: [development, workflow]
---
# 项目文档 Scenario

## Purpose

补齐 README、架构说明与 API 文档，输出可交接的标准化交付物。

### Business Value

- **一致性**: 遵循 Harness 六层模型与统一 Handover
- **可审计**: DC-* 决策与 KPI 可量化追溯
- **可复用**: 与 Prompt / Agent / Skill 基名 `document-project` 对齐

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
| DC-001 | 范围确认 | 执行启动前 | 继续 / 缩小范围 / 升级 | 与上游 Handover 一致 | 执行记录 |
| DC-002 | 质量门禁 | 产出验证前 | 修复后继续 / 记录 open_issues | Scenario KPI ≥70 | 验证报告 |
| DC-003 | 交接准出 | 阶段完成前 | 完成交接 / 部分交接 / 阻塞 | Handover 必填字段齐全 | Handover YAML |

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
| KPI-001 | DOC-COVERAGE | ≥95% | (已文档化的模块数/总模块数) × 100% | 文档清单审查 | 30% |
| KPI-002 | DOC-QUALITY | ≥85/100 | 文档完整性×0.4 + 清晰度×0.3 + 准确性×0.3 | 文档评审 | 30% |
| KPI-003 | SEARCH-SUCCESS | ≥80% | (一次搜索找到文档的次数/总搜索次数) × 100% | 用户反馈统计 | 20% |
| KPI-004 | FRESHNESS | ≥90% | (最近30天更新的文档数/总文档数) × 100% | 文档时间戳检查 | 20% |

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
    from_stage: "implement-feature"
    to_stage: "governance"
    handover_id: "HO-{timestamp}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "document-project"
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
| Agent | `../../agents/document-project.agent.md` |
| Prompt | `../../prompts/document-project.prompt.md` |
| Skill | `../../skills/document-project/SKILL.md` |
| Instruction | `../../instructions/document-project.instructions.md` |

## Related Resources

- [harness-engineering.md](../../standards/harness-engineering.md)
- [output-validation-checklist.md](../../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../../evaluations/regression-checklist.md)
