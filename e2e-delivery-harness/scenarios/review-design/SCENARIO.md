# Review Design Scenario (技术方案评审场景)

## Purpose

本场景用于指导 AI Agent 执行技术方案评审工作，评估方案的可行性、安全性、性能和可维护性。

## Chain of Thought (思维链)

### Think-Aloud Protocol

```
THINK: 理解业务背景和需求
   ↓
THINK: 分析技术方案完整性
   ↓
THINK: 评估技术风险
   ↓
THINK: 检查合规性
   ↓
VALIDATE: 综合评审结论
   ↓
OUTPUT: 输出评审报告
```

## Primary Assets

- **Agent**: [../../agents/review-design.agent.md](../../agents/review-design.agent.md)
- **Instruction**: [../../instructions/review-design.instructions.md](../../instructions/review-design.instructions.md)
- **Prompt**: [../../prompts/review-design.prompt.md](../../prompts/review-design.prompt.md)
- **Skill**: [../../skills/review-design/SKILL.md](../../skills/review-design/SKILL.md)

## Error Handling (错误处理)

### EH-1: 方案信息不足

- **识别信号**：缺少关键设计信息
- **处理方式**：
  1. 列出缺失信息清单
  2. 要求补充
  3. 标注 [待补充]
- **升级条件**：关键信息无法获取

### EH-2: 评审意见分歧

- **识别信号**：评审意见不一致
- **处理方式**：
  1. 讨论达成共识
  2. 记录分歧点
  3. 升级决策
- **升级条件**：无法达成共识

## Decision Checkpoints (决策检查点)

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: 评审范围确认** | 开始评审前 | 评审重点和范围？ | 执行评审 |
| **DC-2: 评审结论确认** | 完成评审后 | 结论是否通过？ | 结束评审 |

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 评审报告 | ☐ | 完整准确 |
| 评审结论 | ☐ | 通过/不通过 |
| 改进建议 | ☐ | 已记录 |

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 方案完整性 | ≥ 90% | 评审检查项 |
| 风险识别率 | 100% | 关键风险 |
| 评审通过率 | - | 统计结果 |


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]
