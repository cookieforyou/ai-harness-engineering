# System Design Scenario

## Purpose

将需求规格说明书转换为技术架构设计方案，为开发实现提供技术指导。

## Primary Assets

### Agent

- **Agent**: [../../agents/system-designer.agent.md](../../agents/system-designer.agent.md)

### Instruction

- **Instruction**: [../../instructions/system-design.instructions.md](../../instructions/system-design.instructions.md)

### Prompt

- **Prompt**: [../../prompts/design-system.prompt.md](../../prompts/design-system.prompt.md)

### Skills

- **Skill**: [../../skills/system-design/SKILL.md](../../skills/system-design/SKILL.md)

## Expected Output

### 产出清单

1. **架构设计文档**：完整的技术架构设计
2. **组件设计文档**：组件详细设计
3. **接口设计文档**：API 和数据接口定义
4. **风险分析报告**：风险识别和应对策略

### 输出格式

```markdown
## 架构设计文档

### 1. 文档信息
...

### 2. 设计范围与目标
...

### 3. 架构概述
...

### 4. 技术选型
...

### 5. 系统架构
...

### 6. 组件设计
...

### 7. 数据设计
...

### 8. 接口设计
...

### 9. 部署架构
...

### 10. 风险分析
...

### 11. 实施计划
...
```

## Prerequisites

### 必需前置条件

1. 需求规格说明书已确认
2. 架构设计有明确的时间要求
3. 有可用的技术资源

### 可选前置条件

1. 团队技术能力评估
2. 现有的技术规范
3. 相关的架构案例

## Quality Gates

### 阶段准入

- [ ] 需求规格说明书已确认
- [ ] 设计约束已明确
- [ ] 技术资源已评估

### 阶段准出

- [ ] 架构设计文档完成
- [ ] 技术评审通过
- [ ] 风险评估完成
- [ ] 方案可行可落地

## Workflow

```
1. 启动 → 理解需求规格
2. 架构选型 → 选择架构风格
3. 组件设计 → 划分组件职责
4. 数据设计 → 设计数据模型
5. 接口设计 → 定义接口规范
6. 风险分析 → 识别技术风险
7. 方案评审 → 技术评审通过
8. 完成 → 输出架构设计文档
```

## Related Scenarios

- **Next**: [../task-decomposition/SCENARIO.md](../task-decomposition/SCENARIO.md) - 任务分解
- **Previous**: [../requirement-analysis/SCENARIO.md](../requirement-analysis/SCENARIO.md) - 需求分析

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 需求覆盖率 | 100% | 设计映射 |
| 评审通过率 | 100% | 评审会议 |
| 风险覆盖率 | > 90% | 风险清单 |
| 方案可行性 | 可落地 | 可行性评估 |
