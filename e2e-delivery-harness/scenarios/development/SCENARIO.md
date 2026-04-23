# Development Scenario

## Purpose

按照任务清单完成代码开发、单元测试和文档更新，确保代码质量。

## Primary Assets

### Agent

- **Agent**: [../../agents/developer.agent.md](../../agents/developer.agent.md)

### Instruction

- **Instruction**: [../../instructions/development.impl.instructions.md](../../instructions/development.impl.instructions.md)

### Prompt

- **Prompt**: [../../prompts/implement-feature.prompt.md](../../prompts/implement-feature.prompt.md)

### Skills

- **Skill**: [../../skills/development/SKILL.md](../../skills/development/SKILL.md)

## Expected Output

### 产出清单

1. **源代码**：符合规范的实现代码
2. **单元测试**：覆盖核心逻辑的测试代码
3. **测试报告**：测试执行结果
4. **变更记录**：代码变更的说明

### 输出格式

```markdown
## 实现报告

### 1. 任务信息
...

### 2. 实现摘要
...

### 3. 代码变更
...

### 4. 测试结果
...

### 5. 遗留问题
...

### 6. 后续建议
...
```

## Prerequisites

### 必需前置条件

1. 任务分解清单已确认
2. 技术规范已定义
3. 开发环境已就绪

### 可选前置条件

1. 相关代码参考
2. 接口定义文档
3. 编码规范文档

## Quality Gates

### 阶段准入

- [ ] 任务已分配
- [ ] 需求理解清晰
- [ ] 技术方案已确认

### 阶段准出

- [ ] 代码实现完成
- [ ] 单元测试通过
- [ ] 代码审查通过
- [ ] 文档已更新

## Workflow

```
1. 启动 → 理解任务需求
2. 技术方案 → 设计实现方案
3. 编码实现 → 编写代码
4. 单元测试 → 编写测试
5. 代码审查 → 自检和审查
6. 文档更新 → 更新文档
7. 完成 → 提交交付
```

## Related Scenarios

- **Next**: [../testing/SCENARIO.md](../testing/SCENARIO.md) - 测试验证
- **Previous**: [../task-decomposition/SCENARIO.md](../task-decomposition/SCENARIO.md) - 任务分解

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 任务完成率 | 100% | 任务清单 |
| 代码规范合规 | 100% | 规范检查 |
| 测试覆盖率 | > 70% | 覆盖率报告 |
| 缺陷密度 | < 5/千行 | 缺陷统计 |
