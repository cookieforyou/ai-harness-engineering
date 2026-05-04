---
name: development
description: 按照任务清单完成代码开发、单元测试和文档更新，确保代码质量
category: implementation
version: "1.1.0"
---

# Development Skill

## Use When

使用此技能的场景：

- 任务分解完成后，需要进行编码实现
- 需要实现特定功能模块
- 需要修复代码缺陷
- 需要进行代码重构

## Expected Input

### 必需输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 任务卡片 | 文件 | 来自任务分解阶段的输出 |
| 技术规范 | 文件 | 编码规范和技术标准 |

### 可选输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 架构设计 | 文件 | 系统的架构设计文档 |
| 接口定义 | 文件 | 相关接口的详细定义 |
| 已有代码 | 代码库 | 相关代码参考 |

## Instructions

### 步骤 1：任务理解

**目标**：深入理解任务需求和验收标准

**操作**：
1. 理解业务需求和背景
2. 确认验收标准
3. 识别依赖和边界
4. 查阅相关代码和文档
5. 准备必要的技术资料

**检查点**：
- [ ] 需求理解准确
- [ ] 验收标准明确
- [ ] 技术资料已准备

### 步骤 2：技术方案设计

**目标**：制定具体的技术实现方案

**操作**：
1. 设计类/函数结构
2. 定义接口和数据结构
3. 考虑异常处理
4. 评估技术风险
5. 编写伪代码或设计图（如需要）

**检查点**：
- [ ] 代码结构已设计
- [ ] 接口已定义
- [ ] 异常处理已考虑

### 步骤 3：编码实现

**目标**：按照规范完成代码编写

**操作**：
1. 遵循团队编码规范
2. 保持代码风格一致
3. 添加必要的注释
4. 避免重复代码
5. 考虑可维护性

**检查点**：
- [ ] 代码规范遵守
- [ ] 注释已添加
- [ ] 无重复代码

### 步骤 4：单元测试编写

**目标**：编写覆盖核心逻辑的单元测试

**操作**：
1. 设计测试用例
2. 覆盖正常路径
3. 覆盖异常路径
4. 覆盖边界条件
5. 执行测试验证

**检查点**：
- [ ] 测试用例完整
- [ ] 覆盖率达标
- [ ] 测试全部通过

### 步骤 5：代码自检

**目标**：进行自我代码审查

**操作**：
1. 对照规范自查
2. 检查代码逻辑
3. 确保测试覆盖
4. 修复发现的问题
5. 准备审查材料

**检查点**：
- [ ] 规范自查通过
- [ ] 问题已修复
- [ ] 审查材料已准备

### 步骤 6：文档更新

**目标**：更新必要的代码和接口文档

**操作**：
1. 更新 API 文档
2. 添加代码注释
3. 更新变更记录
4. 维护接口定义

**检查点**：
- [ ] API 文档已更新
- [ ] 注释已完善
- [ ] 变更已记录

## Expected Output

### 产出列表

1. **源代码**：符合规范的实现代码
2. **单元测试**：覆盖核心逻辑的测试代码
3. **测试报告**：测试执行结果
4. **变更记录**：代码变更的说明

### 输出格式

```markdown
## 实现报告

### 任务完成情况
...

### 代码变更
...

### 测试结果
...

### 遗留问题
...
```

## Quality Criteria

| 维度 | 标准 | 检查方法 |
|------|------|----------|
| 功能正确性 | 实现符合需求 | 验收标准核对 |
| 代码质量 | 规范、可维护 | 代码审查 |
| 测试覆盖 | 核心逻辑覆盖 | 覆盖率报告 |
| 文档完整 | 文档同步更新 | 文档检查 |

## Related Assets

- **Agent**: [../../agents/implement-feature.agent.md](../../agents/implement-feature.agent.md)
- **Instruction**: [../../instructions/development.instructions.md](../../instructions/development.instructions.md)
- **Prompt**: [../../prompts/implement-feature.prompt.md](../../prompts/implement-feature.prompt.md)


## Core Knowledge

> Essential knowledge domain for implement-feature execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for implement-feature excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during implement-feature execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
