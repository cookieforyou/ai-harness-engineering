---
name: plan-rollback
description: "回滚计划场景，为部署发布制定详细的回滚策略和执行方案"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Rollback Planning Scenario

## Overview

回滚计划是部署发布流程的关键组成部分，确保在部署出现问题时能够快速、安全地恢复到稳定状态。本场景涵盖回滚策略制定、脚本准备和验证流程。

## Trigger Conditions

- 任何生产环境部署前
- 重大版本升级
- 架构变更部署
- 配置变更部署
- 紧急热修复部署

## Chain of Thought

```
1. 评估变更风险
   ↓
2. 确定回滚策略
   ↓
3. 设计回滚路径
   ↓
4. 准备回滚脚本
   ↓
5. 定义触发条件
   ↓
6. 制定验证清单
   ↓
7. 安排回滚演练
   ↓
8. 沟通协调准备
```

## Rollback Strategies

### Strategy 1: Blue-Green Deployment

| Aspect | Description |
|--------|-------------|
| 原理 | 维护两套环境，一套备用 |
| 回滚方式 | 切换流量到原环境 |
| 回滚时间 | 分钟级 |
| 成本 | 高（双倍资源） |

### Strategy 2: Canary Deployment

| Aspect | Description |
|--------|-------------|
| 原理 | 逐步放量，发现问题立即停止 |
| 回滚方式 | 停止放量，部分流量回滚 |
| 回滚时间 | 分钟级 |
| 成本 | 中等 |

### Strategy 3: Feature Toggle

| Aspect | Description |
|--------|-------------|
| 原理 | 通过开关控制功能 |
| 回滚方式 | 关闭功能开关 |
| 回滚时间 | 秒级 |
| 成本 | 低 |

### Strategy 4: Database Migration Rollback

| Aspect | Description |
|--------|-------------|
| 原理 | 使用可逆的数据库变更 |
| 回滚方式 | 执行逆向迁移 |
| 回滚时间 | 分钟级到小时级 |
| 成本 | 中等 |

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 范围确认 | 执行启动前 | 继续 / 缩小范围 / 升级 | 与上游 Handover 一致 | 执行记录 |
| DC-002 | 质量门禁 | 产出验证前 | 修复后继续 / 记录 open_issues | Scenario KPI ≥70 | 验证报告 |
| DC-003 | 交接准出 | 阶段完成前 | 完成交接 / 部分交接 / 阻塞 | Handover 必填字段齐全 | Handover YAML |


## Error Handling

| Error Scenario | Handling Strategy |
|----------------|-------------------|
| 回滚失败 | 立即升级到 P0 事故，启动应急响应 |
| 部分回滚 | 评估状态，决定是否完全回滚 |
| 数据损坏 | 启动数据恢复流程 |
| 回滚超时 | 强制停止，分析原因 |




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
| `ROLLBACK-TESTED` | 100% | 回滚方案测试率：所有场景已演练 |
| `RECOVERY-RTO` | ≤15min | 恢复时间目标：回滚到稳定状态 |
| `DATA-CONSISTENCY` | 100% | 数据一致性：回滚后数据完整性 |

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

- [ ] 回滚策略已评审
- [ ] 回滚脚本已测试
- [ ] 触发条件已定义
- [ ] 验证清单已准备
- [ ] 回滚权限已配置
- [ ] 沟通计划已制定

## Expected Artifacts

| Artifact | Description |
|----------|-------------|
| rollback-plan.md | 完整回滚计划 |
| rollback-scripts.md | 回滚脚本和命令 |
| verification-checklist.md | 回滚后验证清单 |
| communication-plan.md | 回滚沟通计划 |

## Related Scenarios

- [deploy-release](./deploy-release/SCENARIO.md) - 部署发布
- [prepare-release](./prepare-release/SCENARIO.md) - 发布准备
- [review-incident](./review-incident/SCENARIO.md) - 事件复盘
- [plan-disaster-recovery](./plan-disaster-recovery/SCENARIO.md) - 灾备恢复


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




> Define the objectives and scope of the plan-rollback scenario.
>
> This scenario ensures systematic execution of plan-rollback activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/plan-rollback/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/plan-rollback.prompt.md` | Execution prompt |
| Instructions | `instructions/plan-rollback.instructions.md` | Technical instructions |
| Agent | `agents/plan-rollback.agent.md` | Responsible agent |
| Skill | `skills/plan-rollback/SKILL.md` | Domain skill |


### Handover Context Template

```yaml
handover:
  header:
    from_stage: "plan-rollback"
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

