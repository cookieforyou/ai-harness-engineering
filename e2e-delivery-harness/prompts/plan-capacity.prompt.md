---
name: plan-capacity
description: "plan capacity execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 容量规划场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行容量规划工作。

## Input Variables

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




| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `system_name` | string | 是 | 系统名称 | "订单系统" |
| `current_capacity` | object | 是 | 当前容量 | 见 Capacity 结构 |
| `growth_rate` | number | 是 | 业务增长率(%) | 20 |
| `planning_period` | number | 是 | 规划周期(月) | 12 |
| `budget_limit` | number | 否 | 预算限制(万) | 100 |

### Capacity 结构

```typescript
interface Capacity {
  current_users: number;         // 当前用户数
  current_tps: number;          // 当前 TPS
  current_storage_gb: number;   // 当前存储(GB)
  current_bandwidth_mbps: number; // 当前带宽(Mbps)
  utilization: {
    cpu: number;                // CPU 利用率 %
    memory: number;             // 内存利用率 %
    storage: number;            // 存储利用率 %
  };
}
```

## Chain of Thought

```
1. [THINK] 分析当前 → 当前容量和利用率？
2. [THINK] 预测需求 → 未来业务增长？
3. [THINK] 评估差距 → 容量缺口多大？
4. [THINK] 制定方案 → 如何扩容？
5. [VALIDATE] 验证方案 → 方案可行？
6. [OUTPUT] 输出报告 → 规划报告
```

## Error Handling

### EH-1: 数据不足

```
IF 历史数据不足
THEN
  1. 收集更多数据
  2. 使用行业基准
  3. 增加安全系数
END
```

## Output Validation

### 验证清单

```markdown
## Self-Validation Report

### V-001: 数据完整性
- [ ] 历史数据分析完整
- [ ] 预测模型合理

### V-002: 方案可行性
- [ ] 预算可行
- [ ] 技术可行

### 验证结果
- 验证通过: [是/否]
```



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



## Handover 准备

```yaml
handover_to_management:
  deliverable: "容量规划报告"
  status: "完成"

  summary:
    current_utilization: object
    predicted_demand: object
    capacity_gap: object
    expansion_plan: object
    budget_estimate: number
```

## Constraints

1. **数据驱动**: 基于数据分析
2. **成本效益**: 合理控制成本
3. **可执行**: 方案切实可行

## Task Description

> Describe the specific task for the plan-capacity scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for plan-capacity

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core plan-capacity activities
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
## Capacity Planning Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Capacity Plan**: Resource requirements and scaling recommendations
2. **Scaling Recommendations**: Vertical/horizontal/auto-scaling strategy
3. **Cost Projection**: Expansion cost forecast with confidence intervals
4. **Procurement Timeline**: Hardware/resource readiness schedule
5. **Headroom Analysis**: Buffer capacity for unexpected growth

### Validation Checklist
- [ ] Forecast accuracy is within 15% of actual
- [ ] Headroom maintained at 20% or higher
- [ ] Cost prediction accuracy is within 20% of actual
- [ ] All peak load scenarios are modeled

### Next Steps
- [ ] Present plan to finance and infrastructure teams
- [ ] Initiate procurement for approved resources
```

