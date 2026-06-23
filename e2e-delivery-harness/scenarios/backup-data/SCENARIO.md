---
name: backup-data
description: "Backup Data scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['workflow', 'process']
---
# Scenario: 数据备份 (Backup Data)

## Overview

本场景用于设计、实现和管理数据备份策略，包括数据库备份、文件备份、灾备方案等。

## Chain of Thought

```
[THINK] 分析备份需求
├─ 识别需要备份的数据
├─ 评估 RTO/RPO 要求
├─ 确定备份频率和保留期

[ANALYZE] 设计备份策略
├─ 选择备份类型（全量/增量/差异）
├─ 设计备份存储方案
├─ 规划备份验证机制

[DESIGN] 实现备份系统
├─ 搭建备份服务
├─ 配置备份任务
├─ 设置监控告警

[IMPLEMENT] 部署备份方案
├─ 配置备份脚本/工具
├─ 测试备份恢复
├─ 验证备份完整性

[VERIFY] 验证备份就绪
├─ 备份恢复测试
├─ 备份时间验证
├─ 备份监控验证
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 备份策略选型 | 哪种备份方案？ |
| DC-002 | 存储位置 | 本地还是云端？ |
| DC-003 | 恢复验证 | 是否需要定期演练？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 备份失败 | 重试并告警 |
| 存储空间不足 | 清理旧备份 |
| 备份损坏 | 使用上一版本 |
| 恢复失败 | 触发灾备恢复 |

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
| `BACKUP-SUCCESS` | ≥99.5% | 备份成功率 |
| `RPO-COMPLY` | 100% | RPO达成：数据丢失量≤RPO目标 |
| `RESTORE-TEST` | ≥1/quarter | 恢复测试频率：每季度至少一次 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 备份策略已定义
- [x] 备份任务已配置
- [x] 监控告警已设置
- [x] 恢复演练已通过
- [x] 运维文档已编写

## Associated Assets

- **Prompt**: `prompts/backup-data.prompt.md`
- **Instruction**: `instructions/backup-data.instructions.md`
- **Agent**: `agents/backup-data.agent.md`
- **Skill**: `skills/backup-data/SKILL.md`

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "backup-data"
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
