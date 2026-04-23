# Testing Scenario

## Purpose

设计和执行测试用例，验证功能正确性，发现并跟踪缺陷，确保软件质量。

## Primary Assets

### Agent

- **Agent**: [../../agents/tester.agent.md](../../agents/tester.agent.md)

### Instruction

- **Instruction**: [../../instructions/testing-verification.instructions.md](../../instructions/testing-verification.instructions.md)

### Prompt

- **Prompt**: [../../prompts/verify-test.prompt.md](../../prompts/verify-test.prompt.md)

### Skills

- **Skill**: [../../skills/testing/SKILL.md](../../skills/testing/SKILL.md)

## Expected Output

### 产出清单

1. **测试计划**：测试策略和资源规划
2. **测试用例集**：完整的测试用例
3. **测试报告**：测试执行结果和分析
4. **缺陷报告**：发现的缺陷清单

### 输出格式

```markdown
## 测试报告

### 1. 测试概要
...

### 2. 测试结果
...

### 3. 缺陷统计
...

### 4. 测试用例详情
...

### 5. 风险评估
...

### 6. 测试结论与建议
...
```

## Prerequisites

### 必需前置条件

1. 开发任务已完成
2. 测试环境已就绪
3. 需求规格已确认

### 可选前置条件

1. 接口文档
2. 测试规范
3. 历史缺陷数据

## Quality Gates

### 阶段准入

- [ ] 开发产出已提交
- [ ] 测试环境可用
- [ ] 测试数据已准备

### 阶段准出

- [ ] 测试用例全部执行
- [ ] 测试报告已输出
- [ ] 缺陷已跟踪
- [ ] 测试结论明确

## Workflow

```
1. 启动 → 理解测试范围
2. 测试计划 → 制定测试策略
3. 用例设计 → 设计测试用例
4. 环境准备 → 搭建测试环境
5. 测试执行 → 执行测试用例
6. 缺陷管理 → 跟踪缺陷
7. 测试报告 → 输出测试报告
8. 完成 → 给出测试结论
```

## Related Scenarios

- **Next**: [../deployment/SCENARIO.md](../deployment/SCENARIO.md) - 部署发布
- **Previous**: [../development/SCENARIO.md](../development/SCENARIO.md) - 开发实现

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 用例执行率 | > 95% | 执行统计 |
| 用例通过率 | > 90% | 通过统计 |
| 缺陷修复率 | > 95% | 缺陷跟踪 |
| 测试覆盖 | > 90% | 覆盖率报告 |
