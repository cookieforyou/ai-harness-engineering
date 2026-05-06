---
name: review-incident
type: scenario
stage: monitoring
version: "1.1.0"
difficulty: medium
prerequisites: 
---

# Incident Review Scenario

## Purpose

对已解决的故障进行复盘分析，找出根本原因，制定改进措施，防止同类故障再次发生。

## Chain of Thought (思维链)

```
THINK: 还原故障经过
   ↓
THINK: 分析故障原因
   ↓
THINK: 识别问题根因
   ↓
THINK: 评估影响范围
   ↓
THINK: 制定改进措施
   ↓
THINK: 跟踪改进落地
```

### Step-by-Step Reasoning

**Step 1: 故障还原**
- 问：故障是如何发生和发展的？
- 验证：收集时间线
- 检查：关键节点

**Step 2: 原因分析**
- 问：直接原因是什么？
- 验证：技术层面分析
- 检查：操作记录

**Step 3: 根因识别**
- 问：根本原因是什么？
- 验证：5 Why 分析
- 检查：系统性问题

**Step 4: 影响评估**
- 问：故障影响了什么？
- 验证：用户、数据、业务
- 检查：损失评估

**Step 5: 改进制定**
- 问：如何防止再次发生？
- 验证：可执行性
- 检查：资源需求

## Error Handling

### EH-1: 原因不明确

- **识别信号**：无法确定根本原因
- **处理方式**：
  1. 收集更多证据
  2. 咨询相关专家
  3. 进行更深入分析
- **升级条件**：需要额外资源

### EH-2: 改进措施冲突

- **识别信号**：改进措施之间有冲突
- **处理方式**：
  1. 评估优先级
  2. 制定实施顺序
  3. 协调相关方
- **升级条件**：需要管理层决策

### EH-3: 责任归属争议

- **识别信号**：团队对责任有争议
- **处理方式**：
  1. 聚焦问题而非责任
  2. 关注系统性改进
  3. 达成共识
- **升级条件**：影响复盘结论

## Primary Assets

- **Agent**: [../../agents/review-incident.agent.md](../../agents/review-incident.agent.md)
- **Instruction**: [../../instructions/review-incident.instructions.md](../../instructions/review-incident.instructions.md)
- **Prompt**: [../../prompts/review-incident.prompt.md](../../prompts/review-incident.prompt.md)

## Expected Output

### 产出清单

1. **故障复盘报告**：完整的故障分析
2. **根本原因分析**：RCA 文档
3. **改进措施清单**：action items
4. **跟踪计划**：改进落地计划

### 输出格式

```markdown
## Incident Postmortem Report

### 1. 故障概述
- 故障编号：
- 故障时间：
- 恢复时间：
- 影响范围：
- 严重程度：

### 2. 故障时间线
...

### 3. 根本原因分析 (RCA)
...

### 4. 影响评估
...

### 5. 改进措施

| 措施 | 负责人 | 完成日期 | 状态 |
|------|--------|----------|------|
| | | | |

### 6. 经验教训
...
```

## Prerequisites

### 必需前置条件

1. 故障已完全恢复
2. 相关日志可用
3. 关键人员可用

### 可选前置条件

1. 故障报告初稿
2. 相关监控数据
3. 历史类似案例

## Quality Gates

### 阶段准入

- [ ] 故障已完全恢复
- [ ] 关键人员参与
- [ ] 数据已收集

### 阶段准出

- [ ] 根本原因已确定
- [ ] 改进措施已制定
- [ ] 责任人已确认

## Decision Checkpoints (决策检查点)

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: 根本原因确认** | 完成初步分析后 | 根因分析是否到位？是否还有遗漏？ | 继续完善 |
| **DC-2: 改进措施确认** | 完成改进措施制定后 | 措施是否有效？优先级？ | 确认责任人 |
| **DC-3: 复盘结论确认** | 完成复盘报告后 | 复盘结论是否各方认可？ | 结束复盘 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `POSTMORTEM-COMPLETION` | 100% | 复盘完成率：所有P0/P1有复盘 |
| `ACTION-CLOSURE` | ≥90% | 措施关闭率：改进措施按时关闭 |
| `RECURRENCE-RATE` | ≤5% | 复发率：同类事件再次发生比例 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 复盘报告 | ☐ | 完整归档 |
| 根本原因 | ☐ | 5 Why 完成 |
| 改进措施 | ☐ | SMART 化 |
| 责任人 | ☐ | 已确认 |

## Workflow

```
1. 收集故障信息
2. 重构故障时间线
3. 分析直接原因
4. 识别根本原因
5. 评估影响
6. 制定改进措施
7. 编写复盘报告
8. 跟踪改进落地
```

## Related Scenarios

- **Related**: [../respond-incident/](../respond-incident/) - Incident Response
- **Related**: [../plan-disaster-recovery/](../plan-disaster-recovery/) - Disaster Recovery Planning

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| RCA 完整性 | 100% | 5 Why 完成 |
| 改进措施完成率 | > 90% | 跟踪统计 |
| 同类故障率 | 下降 | 趋势分析 |
| MTTR 改善 | > 20% | 对比历史 |
