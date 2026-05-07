---
name: manage-change
description: "manage change execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 变更管理场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行变更管理流程，包括变更申请评估、风险分析、审批流程和实施跟踪。

## Execution Variables

| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `change_title` | string | 是 | 变更标题 | "数据库迁移至新集群" |
| `change_type` | enum | 是 | 变更类型 | HOTFIX/PROCEDURE_STANDARD/EMERGENCY |
| `change_description` | string | 是 | 变更详细描述 | 包含变更范围、影响分析... |
| `change_requester` | string | 是 | 申请人 | "zhangsan" |
| `change_implementer` | string | 是 | 实施人 | "lisi" |
| `change_reviewers` | string[] | 是 | 审批人列表 | ["wangwu", "zhaoliu"] |
| `risk_level` | enum | 是 | 风险等级 | LOW/MEDIUM/HIGH/CRITICAL |
| `rollback_plan` | string | 是 | 回滚方案 | "执行 rollback.sql 脚本" |
| `test_plan` | string | 否 | 测试计划 | "灰度验证方案..." |
| `change_schedule` | datetime | 是 | 计划时间窗口 | "2024-01-15 02:00-04:00" |
| `impact_scope` | object | 是 | 影响范围 | 见 ImpactScope 结构 |

### ImpactScope 结构

```typescript
interface ImpactScope {
  services: string[];      // 受影响服务列表
  users: number;           // 受影响用户数
  downtime_required: boolean; // 是否需要停机
  downtime_duration?: number; // 停机时长(分钟)
  data_migration: boolean; // 是否涉及数据迁移
}
```

## Chain of Thought

### Step 1: 变更类型判定

```
输入: change_type
判断:
  - HOTFIX → 走紧急变更通道
  - PROCEDURE_STANDARD → 走标准变更流程
  - EMERGENCY → 启动应急变更流程
```

### Step 2: 风险评估

```
评估维度:
1. 技术风险
   - 变更是否涉及核心系统
   - 是否需要数据库 schema 变更
   - 是否涉及第三方依赖

2. 业务风险
   - 影响用户数量
   - 是否影响核心功能
   - 是否有业务回滚窗口

3. 运营风险
   - 变更时间段是否高峰期
   - 团队响应能力是否充足
```

### Step 3: 审批链确认

```
基于 risk_level 确定审批链:
- LOW: 技术负责人
- MEDIUM: 技术负责人 + 运维负责人
- HIGH: 技术负责人 + 运维负责人 + 业务负责人
- CRITICAL: CTO + 所有相关方
```

### Step 4: 回滚策略制定

```
回滚决策树:
1. 变更前状态是否可以快速恢复
2. 回滚操作对业务的影响
3. 回滚窗口时间是否充足
4. 是否需要人工介入还是自动回滚
```

## Error Handling

### 识别信号

| 信号类型 | 检测条件 | 优先级 |
|----------|----------|--------|
| 风险信息不完整 | 缺少关键风险项描述 | HIGH |
| 回滚方案不可行 | 回滚成功率 < 80% | CRITICAL |
| 审批人无法联系 | 24h 内无响应 | HIGH |
| 变更时间冲突 | 与其他变更窗口重叠 | MEDIUM |
| 资源不足 | 变更所需资源不可用 | HIGH |

### 处理方式

1. **风险信息不完整**
   - 自动补充通用风险项
   - 标记需要人工确认的风险点
   - 通知申请人补充

2. **回滚方案不可行**
   - 建议简化变更方案
   - 提供标准回滚模板
   - 要求增加预验证步骤

3. **审批超时**
   - 发送提醒通知
   - 升级至备用审批人
   - 记录超时原因

### 升级条件

```
CRITICAL 升级条件:
- 风险等级被判定为 CRITICAL
- 回滚方案缺失或不可行
- 涉及核心系统且无备用方案

HIGH 升级条件:
- 审批流程超过 48 小时
- 变更涉及多个部门协调
- 需要特殊权限操作
```

## Output Validation

### 必须包含的字段

- [ ] `change_id`: 变更唯一标识符 (格式: CHG-YYYYMMDD-NNN)
- [ ] `risk_assessment`: 风险评估报告
- [ ] `approval_chain`: 审批链列表
- [ ] `rollback_plan`: 可执行的回滚方案
- [ ] `implementation_plan`: 分步骤实施计划
- [ ] `verification_steps`: 变更后验证步骤
- [ ] `communication_plan`: 通知计划

### Quality Standards

| 检查项 | 标准 |
|--------|------|
| 风险识别覆盖率 | ≥ 90% |
| 回滚方案完整性 | 100% |
| 审批链合理性 | 符合分级授权 |
| 实施计划可执行性 | 每个步骤可验证 |
| 变更窗口合理性 | 有足够缓冲时间 |



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



## Handover Preparation

```markdown
## Change Handover Context

### 变更基础信息
- 变更ID: {change_id}
- 变更类型: {change_type}
- 风险等级: {risk_level}

### 审批状态
- 当前审批阶段: {current_approval_stage}
- 已完成审批: {completed_approvals}
- 待审批: {pending_approvals}

### 实施准备
- 实施计划: {implementation_plan}
- 验证步骤: {verification_steps}
- 预期完成时间: {expected_completion_time}

### 紧急联系人
- 技术负责人: {technical_lead}
- 运维负责人: {ops_lead}
- 业务负责人: {business_lead}
```

## Execution Constraints

1. **信息保密**: 敏感配置信息脱敏处理
2. **合规审计**: 所有变更操作必须可追溯
3. **最小影响**: 优先选择对业务影响最小的变更方案
4. **及时通知**: 变更状态变更必须及时通知相关方

## Task Description

> Describe the specific task for the manage-change scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for manage-change

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core manage-change activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality



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



## Output Format

```markdown
## Change Management Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Change Record**: Documented change with status and timeline
2. **Impact Analysis**: System, team, and user impact assessment
3. **Approval Status**: Approval chain documentation
4. **Execution Schedule**: Change implementation window and steps
5. **Validation Results**: Post-change verification results

### Validation Checklist
- [ ] Change success rate target is met
- [ ] Approval SLA is within 24 hours
- [ ] Change-correlated incident rate is below 2%
- [ ] Rollback plan is tested and ready

### Next Steps
- [ ] Execute change in approved window
- [ ] Monitor for incidents post-change
```

