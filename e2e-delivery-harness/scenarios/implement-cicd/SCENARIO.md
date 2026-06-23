---
name: implement-cicd
description: "Implement Cicd scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Scenario: CI/CD 实施 (Implement CI/CD)

## Overview

本场景用于设计并实施持续集成/持续部署流水线，包括构建、测试、部署全流程自动化。

## Chain of Thought

```
[THINK] 分析 CI/CD 需求
├─ 了解项目技术栈
├─ 确定部署环境
└─ 评估发布频率

[ANALYZE] 设计流水线架构
├─ 设计构建流程
├─ 设计测试阶段
├─ 设计部署策略

[DESIGN] 设计流水线
├─ 设计触发机制
├─ 设计审批流程
├─ 设计回滚机制

[IMPLEMENT] 实现流水线
├─ 配置构建任务
├─ 配置测试任务
├─ 配置部署任务

[VERIFY] 验证流水线
├─ 端到端测试
├─ 性能验证
└─ 安全扫描
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | CI/CD 工具选型 | GitHub Actions/GitLab CI/Jenkins？ |
| DC-002 | 部署策略 | 蓝绿/金丝雀/滚动更新？ |
| DC-003 | 环境配置 | 如何管理环境变量？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 构建失败 | 发送通知、阻止部署 |
| 测试失败 | 阻止合并、发送通知 |
| 部署失败 | 自动回滚、发送通知 |
| 超时 | 重试或人工介入 |

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
| `LEAD-TIME` | ≤1d | 交付前置时间：代码提交到生产部署 |
| `DEPLOY-FREQ` | ≥1/day | 部署频率：每日部署次数 |
| `MTTR` | ≤1h | 恢复时间：故障到恢复平均时间 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 流水线配置完成
- [x] 所有环境可用
- [x] 回滚机制已验证
- [x] 监控告警已配置
- [x] 文档已编写

## Associated Assets

- **Prompt**: `prompts/implement-cicd.prompt.md`
- **Instruction**: `instructions/implement-cicd.instructions.md`
- **Agent**: `agents/implement-cicd.agent.md`
- **Skill**: `skills/implement-cicd/SKILL.md`

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "implement-cicd"
    to_stage: "prepare-release"
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
