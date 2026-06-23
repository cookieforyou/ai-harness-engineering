---
name: setup-infra
description: "Setup Infra scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['workflow', 'process']
---
# Scenario: 基础设施搭建 (Setup Infrastructure)

## Overview

本场景用于搭建项目基础设施，包括云资源、网络、安全组、存储等。

## Chain of Thought

```
[THINK] 理解基础设施需求
├─ 分析业务负载类型
├─ 确定性能和安全要求
└─ 评估成本约束

[ANALYZE] 设计基础设施架构
├─ 选择云服务商和区域
├─ 设计网络拓扑
├─ 规划资源规格

[DESIGN] 规划资源清单
├─ 计算实例规格
├─ 设计存储方案
├─ 配置安全策略

[IMPLEMENT] 实施基础设施
├─ 创建网络资源
├─ 部署计算资源
├─ 配置存储资源

[VERIFY] 验证部署
├─ 资源连通性测试
├─ 性能基准测试
└─ 安全合规检查
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 云服务商选型 | 选择哪个云平台？ |
| DC-002 | 网络架构设计 | VPC CIDR 如何划分？ |
| DC-003 | 资源规格确认 | 实例类型是否合适？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 配额不足 | 申请配额或优化资源 |
| 网络冲突 | 调整 CIDR 范围 |
| 权限不足 | 申请 IAM 权限 |
| 资源创建失败 | 检查参数或重试 |

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
| `IAC-COVERAGE` | ≥95% | IaC覆盖率：基础设施即代码管理比例 |
| `DEPLOY-TIME` | ≤30min | 部署时间：新环境就绪时间 |
| `SEC-BASELINE` | 100% | 安全基线达标率 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 所有资源创建成功
- [x] 网络连通性验证通过
- [x] 安全组规则配置正确
- [x] 监控告警已配置
- [x] 运维文档已编写

## Associated Assets

- **Prompt**: `prompts/setup-infra.prompt.md`
- **Instruction**: `instructions/setup-infra.instructions.md`
- **Agent**: `agents/setup-infra.agent.md`
- **Skill**: `skills/setup-infra/SKILL.md`

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "setup-infra"
    to_stage: "implement-cicd"
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
