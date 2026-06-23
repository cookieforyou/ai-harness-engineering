---
name: traceability-mapping
description: "跨资产可追溯性标准，定义 CoT↔DC-*↔KPI↔Handoff 的映射关系，确保 AI Agent 执行时能正确关联决策点、质量指标和交接要求"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
status: active
tags: ['standard', 'traceability', 'mapping', 'cross-asset']
---

# 跨资产可追溯性映射标准

## 概述

本文件定义了 E2E Delivery Harness 中五类执行资产之间的**结构化可追溯性关系**。每条映射确保 AI Agent 在执行时能正确关联：思维链步骤→决策检查点→质量 KPI→交接要求。

## 核心映射维度

```
CoT Step ─────────→ Decision Checkpoint (DC-*) ─────────→ Quality KPI
    │                        │                                  │
    │ 触发                   │ 决策结果影响                     │ 准出条件
    ↓                        ↓                                  ↓
Prompt Variable ────→ Scenario Input ──────────────→ Handoff Artifact
```

## 标准映射表格式

每个场景必须在其 SCENARIO.md 末尾提供以下映射表：

```markdown
## Traceability Matrix (可追溯性矩阵)

| CoT Step | 触发 DC | DC 决策影响 | 关联 KPI | Handoff 字段 |
|----------|---------|------------|---------|-------------|
| Step 1: [THINK] 理解需求 | DC-001 (范围确认) | 决定需求基线范围 | REQ-COVER | `handover.summary.total_requirements` |
| Step 2: [ANALYZE] 分析约束 | DC-002 (优先级) | 决定需求优先级排序 | STAKEHOLDER-ALIGN | `handover.decisions[DC-001]` |
| Step 3: [SPECIFY] 编写规格 | DC-003 (验收标准) | 决定验收标准格式 | REQ-QUALITY | `handover.artifacts[requirements_spec]` |
| Step 4: [VERIFY] 评审确认 | DC-004 (质量门禁) | 决定是否通过评审 | QUALITY-SCORE | `handover.quality_metrics.kpi_results` |
```

## 核心 7 场景标准映射

### analyze-requirement

| CoT Step | 触发 DC | 关联 KPI | Handoff 字段 |
|----------|---------|---------|-------------|
| [THINK] 理解业务背景 | DC-001 干系人覆盖 | REQ-COVER | `summary.total_requirements` |
| [ANALYZE] 分析需求 | DC-002 需求优先级 | STAKEHOLDER-ALIGN | `decisions[DC-001]` |
| [GATHER] 收集约束 | DC-003 非功能需求 | NFR-COMPLETENESS | `open_issues[non_blocking]` |
| [SPECIFY] 编写规格 | DC-004 验收标准 | REQ-QUALITY | `artifacts[requirements_spec]` |
| [VERIFY] 评审签认 | DC-005 质量门禁 | QUALITY-SCORE | `quality_metrics.kpi_results` |

### design-system

| CoT Step | 触发 DC | 关联 KPI | Handoff 字段 |
|----------|---------|---------|-------------|
| [THINK] 理解系统边界 | DC-001 架构风格 | DESIGN-COVER | `artifacts[architecture_design]` |
| [ANALYZE] 分析 NFR | DC-002 技术栈 | ARCH-REVIEW-PASS | `risks[]` |
| [DESIGN] 模块划分 | DC-003 模块策略 | ADR-COMPLETENESS | `decisions[]` |
| [EVALUATE] 数据+接口 | DC-004 数据方案 | RISK-IDENTIFICATION | `open_issues[]` |
| [VALIDATE] 评审确认 | DC-005 通信协议 | DOC-QUALITY | `quality_metrics.kpi_results` |

### decompose-task

| CoT Step | 触发 DC | 关联 KPI | Handoff 字段 |
|----------|---------|---------|-------------|
| [THINK] 理解设计 | DC-001 拆分粒度 | TASK-COVER | `artifacts[task_list]` |
| [ANALYZE] 分析依赖 | DC-002 依赖策略 | DEPENDENCY-CLARITY | `risks[]` |
| [DESIGN] 估算排序 | DC-003 容量分配 | CAPACITY-UTILIZATION | `decisions[]` |
| [VERIFY] 计划评审 | DC-004 迭代计划 | ESTIMATION-ACCURACY | `quality_metrics.kpi_results` |

### implement-feature

| CoT Step | 触发 DC | 关联 KPI | Handoff 字段 |
|----------|---------|---------|-------------|
| [THINK] 理解任务 | DC-001 实现范围 | CODE-COVERAGE | `artifacts[source_code]` |
| [DESIGN] 详细设计 | DC-002 设计模式 | CYCLOMATIC | `decisions[]` |
| [IMPLEMENT] 编码 | DC-003 代码规范 | BUG-DENSITY | `artifacts[unit_tests]` |
| [VERIFY] 自测+审查 | DC-004 审查门禁 | REVIEW-PASS | `quality_metrics.kpi_results` |

### verify-test

| CoT Step | 触发 DC | 关联 KPI | Handoff 字段 |
|----------|---------|---------|-------------|
| [THINK] 理解测试范围 | DC-001 测试范围 | TEST-PASS | `summary.total_test_cases` |
| [ANALYZE] 测试策略 | DC-002 测试方法 | AUTO-COVERAGE | `artifacts[test_cases]` |
| [DESIGN] 用例设计 | DC-003 缺陷分级 | DEFECT-DETECTION | `artifacts[defect_reports]` |
| [VERIFY] 测试充分性 | DC-004 质量评估 | QUALITY-SCORE | `quality_metrics.kpi_results` |

### deploy-release

| CoT Step | 触发 DC | 关联 KPI | Handoff 字段 |
|----------|---------|---------|-------------|
| [THINK] 确认发布范围 | DC-001 发布授权 | DEPLOY-SUCCESS | `summary.deployment_version` |
| [ANALYZE] 环境检查 | DC-002 部署策略 | ROLLBACK-READY | `artifacts[deployment_plan]` |
| [DESIGN] 部署流程 | DC-003 回滚触发 | DEPLOY-SUCCESS-RATE | `risks[]` |
| [VERIFY] 部署验证 | DC-004 验证充分性 | VERIFICATION-PASS | `quality_metrics.kpi_results` |

### monitor-operate

| CoT Step | 触发 DC | 关联 KPI | Handoff 字段 |
|----------|---------|---------|-------------|
| [SETUP] 监控就绪 | DC-001 监控覆盖 | MON-SLO | `artifacts[monitoring_config]` |
| [WATCH] 持续观察 | DC-002 告警阈值 | ALERT-PRECISION | `summary.monitoring_status` |
| [RESPOND] 响应事件 | DC-003 升级决策 | MTTR | `artifacts[incident_timeline]` |
| [IMPROVE] 优化改进 | DC-004 改进优先级 | SLO-ACHIEVE | `recommendations[]` |

## Prompt 变量 → Scenario 输入映射

每场景的 Prompt 文件变量应与 Scenario 的 Input Handoff 对齐：

```yaml
variable_to_input_mapping:
  prompt_variable: "project_name"
  scenario_input: "project_metadata.name"
  required: true
  validation: "non_empty_string"
  
  prompt_variable: "requirements_spec"
  scenario_input: "from_analyze_requirement.requirements_spec"
  required: true
  validation: "valid_markdown_file"
```

## 验证方法

使用 `scripts/validate-variables.py` 自动验证：
- Prompt 变量是否与 Scenario 输入要求一致
- Required=true 的变量是否有对应的 Handoff 传递路径
- CoT 步骤是否关联了正确的 DC-*

## 相关资产

- [cot-framework.md](cot-framework.md) - CoT 执行框架
- [variable-schema-standard.md](variable-schema-standard.md) - 变量 Schema 规范
- [id-generation-quantification.md](id-generation-quantification.md) - KPI 和 DC 编号体系
- [AGENTS.md](../AGENTS.md) - 资产类型职责说明
