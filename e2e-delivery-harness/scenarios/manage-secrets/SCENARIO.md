---
name: manage-secrets
description: "Manage Secrets scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Scenario: 密钥管理 (Manage Secrets)

## Overview

本场景用于管理和保护应用程序密钥、凭证、证书等敏感信息，包括密钥生成、存储、轮换、审计等。

## Chain of Thought

```
[THINK] 分析密钥需求
├─ 识别需要管理的密钥类型
├─ 评估密钥安全等级
└─ 确定密钥使用场景

[ANALYZE] 设计密钥管理方案
├─ 选择密钥管理服务
├─ 设计密钥存储架构
├─ 规划密钥生命周期

[DESIGN] 设计密钥访问策略
├─ 设计访问控制策略
├─ 配置密钥权限
├─ 规划密钥轮换

[IMPLEMENT] 实现密钥管理
├─ 部署密钥管理服务
├─ 配置密钥存储
├─ 实现密钥访问接口

[VERIFY] 验证密钥安全
├─ 密钥访问审计
├─ 密钥轮换测试
└─ 密钥恢复测试
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 密钥管理服务选型 | Vault/云 KMS/自建？ |
| DC-002 | 密钥存储位置 | 本地/云服务/混合？ |
| DC-003 | 密钥轮换策略 | 自动轮换/手动轮换？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 密钥访问失败 | 检查权限、重试 |
| 密钥过期 | 自动续期或重新生成 |
| 密钥泄露 | 立即轮换、审计 |
| 密钥服务不可用 | 降级到本地缓存 |




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
| `ROTATION-COMPLY` | 100% | 轮换合规率：按计划执行轮换 |
| `ACCESS-AUDIT` | 100% | 访问审计覆盖率：所有访问有日志 |
| `LEAK-DETECTION` | ≤1h | 泄露检测时间：发现泄露到告警 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



## Handover Criteria

- [x] 密钥管理服务部署完成
- [x] 密钥访问策略已配置
- [x] 密钥轮换机制已设置
- [x] 密钥审计日志已启用
- [x] 密钥恢复方案已测试

## Associated Assets

- **Prompt**: `prompts/manage-secrets.prompt.md`
- **Instruction**: `instructions/manage-secrets.instructions.md`
- **Agent**: `agents/manage-secrets.agent.md`
- **Skill**: `skills/manage-secrets/SKILL.md`



### Handover Context Template

```yaml
handover:
  header:
    from_stage: "manage-secrets"
    to_stage: "verify-test"
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

