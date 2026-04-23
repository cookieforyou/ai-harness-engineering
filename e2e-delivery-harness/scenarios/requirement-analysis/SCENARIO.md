# Requirement Analysis Scenario

## Purpose

将原始业务需求转换为结构化的需求规格说明书，为后续系统设计和开发提供清晰的输入。

## Chain of Thought (思维链)

> AI 执行时的思维引导，帮助逐步完成需求分析工作

### Think-Aloud Protocol

```
THINK: 理解业务目标
   ↓
THINK: 识别干系人和诉求
   ↓
THINK: 梳理业务流程和边界
   ↓
THINK: 规格化功能和非功能需求
   ↓
THINK: 定义验收标准和优先级
   ↓
THINK: 验证需求完整性和一致性
```

### Step-by-Step Reasoning

**Step 1: 业务目标理解**
- 问：我理解的是正确的业务目标吗？
- 验证：与业务方确认核心价值主张
- 检查：目标是否 SMART（具体、可衡量、可达成、相关、有时限）

**Step 2: 干系人识别**
- 问：所有相关干系人都识别到了吗？
- 验证：检查是否有遗漏的角色
- 检查：干系人之间的利益冲突是否已识别

**Step 3: 需求收集与分类**
- 问：需求是否覆盖了所有业务场景？
- 验证：按业务流程逐环节梳理
- 检查：功能需求与非功能需求是否分开

**Step 4: 验收标准定义**
- 问：每个需求都有可验证的验收标准吗？
- 验证：标准是否可测试
- 检查：优先级是否与业务价值一致

**Step 5: 一致性检查**
- 问：需求之间是否有冲突？
- 验证：假设条件是否合理
- 检查：约束条件是否被满足

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
