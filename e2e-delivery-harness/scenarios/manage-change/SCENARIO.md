---
name: manage-change
type: scenario
stage: cross-phase
version: 1.1.0
difficulty: medium
prerequisites: null
description: Manage Change scenario for the E2E delivery lifecycle
author: AI Harness Engineering Team
---

# Change Management Scenario

## Purpose

管理需求变更请求，评估变更影响，制定变更实施计划，确保变更可控可追溯。

## Chain of Thought (思维链)

```
THINK: 理解变更请求
   ↓
THINK: 评估变更影响
   ↓
THINK: 制定决策方案
   ↓
THINK: 规划实施步骤
   ↓
THINK: 更新相关文档
   ↓
THINK: 沟通变更计划
```

### Step-by-Step Reasoning

**Step 1: 变更理解**
- 问：变更的背景和原因是什么？
- 验证：与变更发起人确认
- 检查：变更范围是否清晰

**Step 2: 影响评估**
- 问：变更会影响哪些部分？
- 验证：逐项分析影响
- 检查：是否需要重新设计

**Step 3: 决策制定**
- 问：接受/拒绝/延迟的理由？
- 验证：权衡利弊
- 检查：决策是否合理

**Step 4: 实施规划**
- 问：如何在不影响进度的情况下实施？
- 验证：评估资源需求
- 检查：是否有风险

## Error Handling

### EH-1: 变更范围蔓延

- **识别信号**：变更范围不断扩大
- **处理方式**：
  1. 明确原变更范围
  2. 将扩展部分作为新变更
  3. 重新评估
- **升级条件**：影响核心功能

### EH-2: 变更与现有设计冲突

- **识别信号**：变更与已实现功能冲突
- **处理方式**：
  1. 分析冲突点
  2. 评估重构成本
  3. 考虑替代方案
- **升级条件**：需要大量返工

### EH-3: 变更影响无法评估

- **识别信号**：无法确定变更影响
- **处理方式**：
  1. 进行更深入分析
  2. 咨询相关专家
  3. 分阶段实施
- **升级条件**：影响决策

## Primary Assets

- **Agent**: [../../agents/manage-change.agent.md](../../agents/manage-change.agent.md)
- **Instruction**: [../../instructions/manage-change.instructions.md](../../instructions/manage-change.instructions.md)
- **Prompt**: [../../prompts/manage-change.prompt.md](../../prompts/manage-change.prompt.md)

## Expected Output

### 产出清单

1. **变更评估报告**：变更影响的完整分析
2. **变更决策**：接受/拒绝/延迟的决策
3. **实施计划**：变更实施的时间表
4. **更新文档**：需求规格和相关文档

### 输出格式

```markdown
## Change Assessment Report

### 1. 变更信息
- 变更编号：
- 发起人：
- 日期：
- 状态：

### 2. 变更描述
...

### 3. 影响评估
...

### 4. 变更决策
...

### 5. 实施计划
...

### 6. 更新记录
...
```

## Prerequisites

### 必需前置条件

1. 有明确的变更请求
2. 有原始需求文档
3. 有相关干系人

### 可选前置条件

1. 变更影响的相关分析
2. 类似的变更案例

## Quality Gates

### 阶段准入

- [ ] 有正式的变更请求
- [ ] 变更描述清晰
- [ ] 变更原因明确

### 阶段准出

- [ ] 变更评估完成
- [ ] 变更决策已做出
- [ ] 实施计划已制定
- [ ] 相关文档已更新

## Decision Checkpoints (决策检查点)

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: 变更类型确认** | 完成变更分析后 | 变更类型是否正确？风险等级？ | 继续评估 |
| **DC-2: 审批确认** | 完成风险评估后 | 是否批准变更？条件？ | 继续或拒绝 |
| **DC-3: 回滚决策** | 变更执行异常时 | 继续还是回滚？ | 回滚或继续 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `CHANGE-SUCCESS` | ≥95% | 变更成功率：按计划完成且无回退 |
| `APPROVAL-SLA` | ≤24h | 审批SLA：提交到批准时间 |
| `INCIDENT-CORRELATION` | ≤2% | 事件关联率：变更引发的事件占比 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 变更评估报告 | ☐ | 含风险等级 |
| 变更决策记录 | ☐ | 审批完成 |
| 实施计划 | ☐ | 含回滚方案 |
| 执行记录 | ☐ | 完整可追溯 |

## Workflow

```
1. 接收变更请求
2. 分析变更内容
3. 评估影响范围
4. 制定决策建议
5. 评审变更决策
6. 制定实施计划
7. 执行变更
8. 更新文档
```

## Related Scenarios

- **Related**: [../analyze-requirement/](../analyze-requirement/) - 需求分析
- **Related**: [../design-system/](../design-system/) - 系统设计
- **Related**: [../implement-feature/](../implement-feature/) - 开发实现

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 评估完整性 | > 95% | 检查清单覆盖率 |
| 决策合理性 | 100% | 评审通过率 |
| 实施成功率 | > 90% | 实施完成率 |
