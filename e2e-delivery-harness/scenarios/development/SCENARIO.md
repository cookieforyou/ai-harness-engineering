# Development Scenario

## Purpose

按照任务清单完成代码开发、单元测试和文档更新，确保代码质量。

## Chain of Thought (思维链)

> AI 执行时的思维引导，帮助逐步完成开发实现工作

### Think-Aloud Protocol

```
THINK: 理解任务需求和验收标准
   ↓
THINK: 设计实现方案
   ↓
THINK: 编写代码和单元测试
   ↓
THINK: 自检代码规范和质量
   ↓
THINK: 提交代码审查
   ↓
THINK: 修复审查反馈
```

### Step-by-Step Reasoning

**Step 1: 任务理解**
- 问：我理解的需求和验收标准正确吗？
- 验证：与需求规格对照
- 检查：是否有模糊不清的地方

**Step 2: 方案设计**
- 问：实现方案是否合理？
- 验证：是否符合架构设计
- 检查：是否考虑了异常情况

**Step 3: 编码实现**
- 问：代码是否遵循编码规范？
- 验证：命名、结构、注释
- 检查：是否有安全漏洞

**Step 4: 单元测试**
- 问：测试用例覆盖了核心逻辑吗？
- 验证：边界条件和异常场景
- 检查：测试是否可重复执行

**Step 5: 代码审查**
- 问：审查反馈是否都处理了？
- 验证：修改是否正确
- 检查：是否引入了新问题

## Primary Assets

### Agent

- **Agent**: [../../agents/developer.agent.md](../../agents/developer.agent.md)

### Instruction

- **Instruction**: [../../instructions/development.instructions.md](../../instructions/development.instructions.md)

### Prompt

- **Prompt**: [../../prompts/implement-feature.prompt.md](../../prompts/implement-feature.prompt.md)

### Skills

- **Skill**: [../../skills/development/SKILL.md](../../skills/development/SKILL.md)

## Error Handling (错误处理)

### EH-1: 验收标准不清晰

- **识别信号**：验收标准模糊或有歧义
- **处理方式**：
  1. 列出所有可能的理解
  2. 选择最合理的理解
  3. 在代码注释中说明假设
  4. 标记为 `[需确认]`
- **升级条件**：影响功能实现

### EH-2: 技术难点

- **识别信号**：遇到无法解决的技术问题
- **处理方式**：
  1. 分析问题根本原因
  2. 尝试替代方案
  3. 如无法解决，向上升级
  4. 记录尝试的解决方案
- **升级条件**：阻塞任务完成

### EH-3: 发现设计问题

- **识别信号**：设计与实现不匹配
- **处理方式**：
  1. 分析差异影响
  2. 判断是设计还是实现问题
  3. 联系系统设计师
- **升级条件**：需要修改设计

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
