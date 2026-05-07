---
name: plan-disaster-recovery
description: "灾备恢复场景，规划和实施灾难恢复策略，确保业务连续性"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Disaster Recovery Planning Scenario

## Overview

灾备恢复规划是确保业务连续性的关键，涵盖对灾难场景的预防、准备、响应和恢复能力建设。本场景定义 RPO/RTO 目标、恢复策略和演练机制。

## Key Metrics

### Recovery Point Objective (RPO)
- 定义：最大可接受的数据丢失时间窗口
- 计算：备份频率决定 RPO
- 示例：每 4 小时备份 → RPO = 4 小时

### Recovery Time Objective (RTO)
- 定义：最大可接受的系统恢复时间
- 计算：恢复步骤决定 RTO
- 示例：多可用区部署 → RTO = 15 分钟

## Disaster Categories

### Tier 1: Data Center Failure
| Aspect | Description |
|--------|-------------|
| 影响 | 单个数据中心不可用 |
| RTO | 15-60 分钟 |
| 策略 | 多可用区部署，自动 failover |

### Tier 2: Region Failure
| Aspect | Description |
|--------|-------------|
| 影响 | 整个区域不可用 |
| RTO | 1-4 小时 |
| 策略 | 跨区域备份，手动切换 |

### Tier 3: Cyber Attack
| Aspect | Description |
|--------|-------------|
| 影响 | 数据泄露或勒索软件 |
| RTO | 4-24 小时 |
| 策略 | 隔离，恢复备份 |

## Chain of Thought

```
1. 业务影响分析
   ↓
2. 确定 RPO/RTO
   ↓
3. 设计恢复策略
   ↓
4. 规划备份方案
   ↓
5. 设计故障转移
   ↓
6. 准备恢复流程
   ↓
7. 制定演练计划
   ↓
8. 执行演练验证
   ↓
9. 持续优化改进
```

## Decision Checkpoints

### Checkpoint 1: 需求分析
- 业务关键程度？
- 可接受的停机时间？
- 可接受的数据丢失？
- 合规要求？

### Checkpoint 2: 策略选择
- 采用什么备份策略？
- 使用什么恢复架构？
- 如何验证恢复能力？

### Checkpoint 3: 资源规划
- 需要多少备用资源？
- 成本预算？
- 人员配置？

### Checkpoint 4: 演练验证
- 多久演练一次？
- 如何衡量成功？
- 如何改进？




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
| `RTO-COMPLY` | 100% | RTO达成：恢复时间≤目标 |
| `RPO-COMPLY` | 100% | RPO达成：数据丢失≤目标 |
| `DR-TEST-FREQ` | ≥1/year | DR演练频率：每年至少一次全量演练 |

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

- [ ] DR 计划文档完整
- [ ] RPO/RTO 已定义
- [ ] 备份方案已实施
- [ ] 故障转移已配置
- [ ] 恢复流程已测试
- [ ] 演练已执行

## Related Scenarios

- [respond-incident](./respond-incident/SCENARIO.md) - 事件响应
- [plan-rollback](./plan-rollback/SCENARIO.md) - 回滚计划
- [backup-data](./backup-data/SCENARIO.md) - 数据备份
- [monitor-operate](./monitor-operate/SCENARIO.md) - 监控运维


## Purpose

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




> Define the objectives and scope of the plan-disaster-recovery scenario.
>
> This scenario ensures systematic execution of plan-disaster-recovery activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: Business impact analysis (BIA) is completed with RTO/RPO
- [ ] Prerequisite 2: Infrastructure inventory and dependencies are documented
- [ ] Prerequisite 3: Threat scenarios and risk appetite are defined


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/plan-disaster-recovery/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/plan-disaster-recovery.prompt.md` | Execution prompt |
| Instructions | `instructions/plan-disaster-recovery.instructions.md` | Technical instructions |
| Agent | `agents/plan-disaster-recovery.agent.md` | Responsible agent |
| Skill | `skills/plan-disaster-recovery/SKILL.md` | Domain skill |


## Error Handling

### Error Scenario 1
**Error**: DR plan does not meet recovery time objective (RTO) targets
**Handling**: [Resolution steps]

### Error Scenario 2
**Error**: DR procedures have not been tested or are outdated
**Handling**: [Resolution steps]


### Handover Context Template

```yaml
handover:
  header:
    from_stage: "plan-disaster-recovery"
    to_stage: "unknown"
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

