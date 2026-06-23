---
name: optimize-performance
description: "Optimize Performance scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['workflow', 'process']
---
# Scenario: 性能优化 (Optimize Performance)

## Overview

本场景用于识别和解决系统性能瓶颈，包括代码优化、数据库优化、缓存优化、网络优化等。

## Chain of Thought

```
[ANALYZE] 分析性能问题
├─ 确定性能指标基线
├─ 识别性能瓶颈
└─ 分析瓶颈原因

[MEASURE] 测量性能数据
├─ 性能分析工具
├─ 性能测试
└─ 监控数据

[OPTIMIZE] 实施优化
├─ 代码级优化
├─ 数据库优化
├─ 缓存优化
├─ 并发优化

[VERIFY] 验证优化效果
├─ 性能回归测试
├─ 压力测试
└─ 稳定性测试
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 瓶颈定位 | 哪个环节最慢？ |
| DC-002 | 优化方案选择 | 缓存/索引/重构？ |
| DC-003 | 优化优先级 | 哪个收益最大？ |

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
| `IMPROVEMENT-GAIN` | ≥20% | 性能提升：优化后目标指标提升 |
| `REGRESSION-FREE` | 100% | 无回归：其他指标不劣化 |
| `COST-EFFICIENCY` | ≤100% | 成本效率：优化不增加资源成本 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 性能瓶颈已定位
- [x] 优化方案已实施
- [x] 性能指标已达标
- [x] 性能回归测试通过

## Associated Assets

- **Prompt**: `prompts/optimize-performance.prompt.md`
- **Instruction**: `instructions/optimize-performance.instructions.md`
- **Agent**: `agents/optimize-performance.agent.md`
- **Skill**: `skills/optimize-performance/SKILL.md`

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "optimize-performance"
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
