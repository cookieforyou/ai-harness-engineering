# Requirement Analysis Scenario

## Purpose

将原始业务需求转换为结构化的需求规格说明书，为后续系统设计和开发提供清晰的输入。

## Primary Assets

### Agent

- **Agent**: [../../agents/requirement-analyst.agent.md](../../agents/requirement-analyst.agent.md)

### Instruction

- **Instruction**: [../../instructions/requirement-analysis.instructions.md](../../instructions/requirement-analysis.instructions.md)

### Prompt

- **Prompt**: [../../prompts/analyze-requirement.prompt.md](../../prompts/analyze-requirement.prompt.md)

### Skills

- **Skill**: [../../skills/requirement-analysis/SKILL.md](../../skills/requirement-analysis/SKILL.md)

## Expected Output

### 产出清单

1. **需求规格说明书**：结构化的需求文档
2. **干系人分析表**：干系人识别和诉求分析
3. **业务流程描述**：主要业务流程
4. **用例模型**：系统用例定义

### 输出格式

```markdown
## 需求规格说明书

### 1. 文档信息
- 项目名称：
- 版本：
- 日期：
- 状态：

### 2. 业务背景与目标
...

### 3. 干系人分析
...

### 4. 功能需求
...

### 5. 非功能需求
...

### 6. 业务流程
...

### 7. 用例模型
...

### 8. 验收标准
...

### 9. 约束与假设
...

### 10. 未解决问题
...
```

## Prerequisites

### 必需前置条件

1. 业务方提出明确的需求请求
2. 项目背景和目标已定义
3. 有足够的时间进行需求调研

### 可选前置条件

1. 现有的需求文档或资料
2. 干系人联系信息
3. 相关系统的文档

## Quality Gates

### 阶段准入

- [ ] 有明确的业务需求输入
- [ ] 有业务背景和目标描述
- [ ] 有可访问的干系人

### 阶段准出

- [ ] 需求规格说明书完成
- [ ] 干系人评审通过
- [ ] 验收标准已定义
- [ ] 无未解决的重大问题

## Workflow

```
1. 启动 → 收集原始需求
2. 干系人分析 → 识别干系人和诉求
3. 业务建模 → 构建业务流程和用例
4. 需求规格化 → 结构化需求描述
5. 评审确认 → 干系人评审签字
6. 完成 → 输出需求规格说明书
```

## Related Scenarios

- **Next**: [../system-design/SCENARIO.md](../system-design/SCENARIO.md) - 系统设计
- **Previous**: - (项目起点)

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 需求完整性 | > 95% | 验收标准覆盖率 |
| 干系人满意度 | > 4.0 | 评审评分 |
| 评审通过率 | 100% | 评审会议 |
