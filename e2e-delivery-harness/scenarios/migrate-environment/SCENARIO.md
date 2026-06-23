---
name: migrate-environment
description: "Migrate Environment scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Scenario: 环境迁移 (Migrate Environment)

## Overview

本场景用于将应用程序从一个环境迁移到另一个环境，包括开发、测试、预发布、生产环境之间的迁移。

## Chain of Thought

```
[ANALYZE] 分析迁移需求
├─ 确定源环境和目标环境
├─ 分析差异和依赖
└─ 评估迁移风险

[PLAN] 制定迁移计划
├─ 数据迁移策略
├─ 配置迁移策略
├─ 回滚方案

[PREPARE] 准备迁移
├─ 备份数据
├─ 准备配置文件
├─ 验证目标环境

[MIGRATE] 执行迁移
├─ 数据迁移
├─ 配置迁移
├─ 服务部署

[VERIFY] 验证迁移
├─ 功能验证
├─ 数据验证
├─ 监控验证
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 迁移方案 | 全量迁移还是增量迁移？ |
| DC-002 | 数据同步 | 在线迁移还是停机迁移？ |
| DC-003 | 回滚方案 | 是否需要保留回滚能力？ |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```

## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `MIGRATION-SUCCESS` | ≥98% | 迁移成功率：应用功能无损迁移 |
| `PERF-PARITY` | ≥95% | 性能对等：新环境性能≥原环境95% |
| `COST-EFFICIENCY` | ≤110% | 成本效率：新环境成本≤原环境110% |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 迁移计划已评审
- [x] 数据已备份
- [x] 迁移已执行
- [x] 验证已通过

## Associated Assets

- **Prompt**: `prompts/migrate-environment.prompt.md`
- **Instruction**: `instructions/migrate-environment.instructions.md`
- **Agent**: `agents/migrate-environment.agent.md`
- **Skill**: `skills/migrate-environment/SKILL.md`

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "migrate-environment"
    to_stage: "monitor-operate"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "{{artifact_name}}"
        path: "{{file_path}}"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-XXX"
      description: "{{决策描述}}"
      rationale: "{{决策理由}}"
      alternatives_considered: ["选项1", "选项2"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{{问题描述}}"
        
  risks:
    - id: "RISK-XXX"
      description: "{{风险描述}}"
      probability: "low/medium/high"
      impact: "low/medium/high"
      mitigation: "{{缓解措施}}"
      
  recommendations:
    - "{{建议1}}"
    - "{{建议2}}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{actual_value}}
        target: {{target_value}}
        status: "pass/fail"
```
