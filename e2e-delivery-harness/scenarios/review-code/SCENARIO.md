---
name: review-code
type: scenario
stage: development
version: 1.1.0
difficulty: medium
prerequisites: null
description: Review Code scenario for the E2E delivery lifecycle
author: AI Harness Engineering Team
---

# Code Review Scenario

## Purpose

执行代码审查，发现代码质量问题，确保代码符合规范，减少缺陷进入测试阶段。

## Chain of Thought (思维链)

```
THINK: 理解代码变更内容
   ↓
THINK: 检查代码规范合规
   ↓
THINK: 分析代码质量
   ↓
THINK: 识别潜在风险
   ↓
THINK: 评估安全风险
   ↓
THINK: 给出审查结论
```

### Step-by-Step Reasoning

**Step 1: 变更理解**
- 问：这次变更做了什么？
- 验证：理解业务逻辑
- 检查：变更范围是否合理

**Step 2: 规范检查**
- 问：代码符合编码规范吗？
- 验证：逐项对照规范
- 检查：命名、格式、注释

**Step 3: 质量分析**
- 问：代码质量如何？
- 验证：检查复杂度、耦合度
- 检查：是否有坏味道

**Step 4: 风险识别**
- 问：有什么潜在风险？
- 验证：性能、并发、边界
- 检查：是否有遗漏

**Step 5: 安全评估**
- 问：有安全漏洞吗？
- 验证：常见安全检查
- 检查：注入、XSS、权限

## Error Handling

### EH-1: 代码逻辑错误

- **识别信号**：发现业务逻辑问题
- **处理方式**：
  1. 明确指出问题
  2. 说明影响
  3. 提出修改建议
- **升级条件**：影响核心功能

### EH-2: 发现安全漏洞

- **识别信号**：发现安全风险
- **处理方式**：
  1. 标记为安全评论
  2. 说明漏洞类型
  3. 提供修复建议
  4. 优先级设为高
- **升级条件**：高危漏洞

### EH-3: 审查意见分歧

- **识别信号**：开发者不认同审查意见
- **处理方式**：
  1. 解释审查标准
  2. 提供参考案例
  3. 寻求共识
- **升级条件**：无法达成共识

## Primary Assets

- **Agent**: [../../agents/review-code.agent.md](../../agents/review-code.agent.md)
- **Instruction**: [../../instructions/review-code.instructions.md](../../instructions/review-code.instructions.md)
- **Prompt**: [../../prompts/review-code.prompt.md](../../prompts/review-code.prompt.md)

## Expected Output

### 产出清单

1. **代码审查报告**：审查结果汇总
2. **审查评论**：具体问题列表
3. **审查结论**：通过/需要修改

### 输出格式

```markdown
## Code Review Report

### 1. 审查信息
- 变更编号：
- 审查人：
- 日期：
- 代码作者：

### 2. 变更摘要
...

### 3. 审查结果
- 严重问题：N
- 一般问题：N
- 建议改进：N

### 4. 问题详情
...

### 5. 审查结论
...
```

## Prerequisites

### 必需前置条件

1. 代码已提交到审查分支
2. 单元测试已通过
3. 代码规范可用

### 可选前置条件

1. PR 描述完整
2. 相关文档已更新

## Quality Gates

### 阶段准入

- [ ] 代码已提交审查
- [ ] PR 描述完整
- [ ] 测试已通过

### 阶段准出

- [ ] 所有严重问题已解决
- [ ] 所有一般问题已处理
- [ ] 审查结论已给出

## Decision Checkpoints (决策检查点)

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: 审查范围确认** | 开始审查前 | 审查重点是什么？优先级？ | 继续审查 |
| **DC-2: 严重问题确认** | 发现严重问题时 | 是否接受继续？条件？ | 修复或讨论 |
| **DC-3: 最终结论确认** | 所有问题处理后 | 是否批准合并？ | 合并或继续 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `DEFECT-DETECTION` | ≥85% | 缺陷检出率：代码审查发现的问题 |
| `REVIEW-TURNAROUND` | ≤24h | 审查周转时间 |
| `SECURITY-FINDINGS` | 0 | 安全漏洞遗留：P0/P1安全漏洞数 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 审查报告 | ☐ | 问题清单完整 |
| 严重问题 | ☐ | 全部已解决 |
| 一般问题 | ☐ | 全部已处理 |
| 审查结论 | ☐ | APPROVED/CHANGES |

## Workflow

```
1. 接收审查请求
2. 理解变更内容
3. 执行代码审查
4. 标注问题
5. 给出审查结论
6. 跟踪问题修复
7. 完成审查
```

## Related Scenarios

- **Related**: [../implement-feature/](../implement-feature/) - 开发实现
- **Related**: [../verify-test/](../verify-test/) - 测试验证

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 审查覆盖率 | 100% | PR 覆盖率 |
| 问题发现率 | > 3 个/PR | 统计 |
| 严重问题遗漏率 | < 5% | 漏检统计 |
| 审查周期 | < 24h | 平均时间 |
