---
name: analyze-requirement
description: 将原始业务需求转换为结构化的需求规格说明书，包含干系人分析、业务建模和验收标准定义
category: analysis
version: "1.0.0"
---

# Requirement Analysis Skill

## Use When

使用此技能的场景：

- 新项目启动，需要进行需求调研和分析
- 业务方提出新需求，需要结构化澄清
- 现有需求文档不完整，需要梳理重构
- 需求变更频繁，需要重新评估影响

## Expected Input

### 必需输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 原始需求 | 文本 | 业务方的原始需求描述 |
| 业务背景 | 文本 | 项目的业务背景和历史上下文 |

### 可选输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 干系人信息 | 列表 | 已知干系人及其联系方式 |
| 现有文档 | 文件 | 已有的需求文档或相关资料 |
| 约束条件 | 文本 | 已知的技术或资源约束 |

## Instructions

### 步骤 1：业务目标理解

**目标**：识别需求背后的业务触发点和期望达成的目标

**操作**：
1. 理解业务背景和发起需求的原因
2. 识别期望达成的业务目标
3. 理解需求解决的问题或机会
4. 将业务目标量化为可衡量的指标

**检查点**：
- [ ] 业务目标清晰定义
- [ ] 目标可衡量、可达成
- [ ] 目标与业务价值关联

### 步骤 2：干系人分析

**目标**：识别所有相关干系人，理解其诉求和期望

**操作**：
1. 列出所有利益相关方
2. 对干系人进行分类（决策者、使用者、影响者）
3. 访谈关键干系人，了解诉求
4. 识别诉求间的潜在冲突

**检查点**：
- [ ] 关键干系人已识别
- [ ] 各干系人诉求已整理
- [ ] 冲突点已标注

### 步骤 3：业务流程建模

**目标**：构建业务流程和用例模型

**操作**：
1. 识别主要业务流程
2. 描述流程的输入、处理、输出
3. 标注关键决策点
4. 定义异常处理流程
5. 编写系统用例

**检查点**：
- [ ] 主要流程已描述
- [ ] 决策点已标注
- [ ] 异常处理已定义
- [ ] 用例已编写

### 步骤 4：功能需求定义

**目标**：将需求转换为结构化的功能需求规格

**操作**：
1. 使用 "As a... I want... so that..." 格式描述需求
2. 为每个需求定义明确的验收标准
3. 标注需求的优先级（P0/P1/P2）
4. 识别需求间的依赖关系

**检查点**：
- [ ] 需求格式规范
- [ ] 验收标准明确
- [ ] 优先级标注
- [ ] 依赖关系已识别

### 步骤 5：非功能需求定义

**目标**：定义系统的非功能性需求

**操作**：
1. 识别性能需求（响应时间、吞吐量、并发）
2. 定义安全需求（认证、授权、审计）
3. 定义可用性需求（可用率、恢复时间）
4. 定义可维护性需求（监控、日志、配置）
5. 定义兼容性需求

**检查点**：
- [ ] 性能需求已定义
- [ ] 安全需求已定义
- [ ] 可用性需求已定义

### 步骤 6：约束与假设整理

**目标**：整理已知约束条件和假设

**操作**：
1. 整理技术约束
2. 整理时间约束
3. 整理资源约束
4. 列出当前做出的假设
5. 识别未解决的问题

**检查点**：
- [ ] 约束条件已整理
- [ ] 假设已列出
- [ ] 未解决问题已标注

### 步骤 7：需求评审确认

**目标**：与干系人评审需求，确保理解一致

**操作**：
1. 准备评审材料
2. 组织评审会议
3. 收集评审反馈
4. 根据反馈修订需求
5. 获得干系人签字确认

**检查点**：
- [ ] 评审已完成
- [ ] 反馈已处理
- [ ] 需求已确认

## Expected Output

### 产出列表

1. **需求规格说明书**：结构化的需求文档
2. **干系人分析表**：干系人识别和诉求分析
3. **业务流程描述**：主要业务流程
4. **用例模型**：系统用例定义

### 输出格式

```markdown
## 需求规格说明书

### 文档信息
- 项目名称：
- 版本：
- 日期：
- 状态：草稿/确认

### 业务背景与目标
...

### 干系人分析
...

### 功能需求
...

### 非功能需求
...

### 业务流程
...

### 用例模型
...

### 验收标准
...

### 约束与假设
...
```

## Quality Criteria

### 质量标准

| 维度 | 标准 | 检查方法 |
|------|------|----------|
| 完整性 | 所有必需项已包含 | 对照检查清单 |
| 准确性 | 业务理解正确 | 干系人确认 |
| 可追溯性 | 需求与目标关联 | 映射检查 |
| 可验证性 | 验收标准明确 | 测试映射 |

## Examples

### 示例 1

**场景**：电商平台增加积分功能

**输入**：
- 业务方希望增加积分功能
- 用户消费可以获得积分
- 积分可以兑换礼品

**处理过程**：
1. 识别业务目标：提升用户粘性、增加复购率
2. 分析干系人：用户、运营、财务
3. 建模业务流程：积分获取、积分兑换
4. 定义功能需求：积分规则、兑换流程
5. 定义非功能需求：实时性、准确性
6. 整理约束：现有系统兼容性
7. 评审确认：与业务方确认

**输出**：
- 完整的需求规格说明书
- 干系人分析表
- 业务流程图
- 用例模型

## Troubleshooting

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 需求模糊不清 | 信息不足 | 主动与干系人沟通澄清 |
| 干系人诉求冲突 | 利益不一致 | 协商优先级，请上级决策 |
| 验收标准不明确 | 描述不具体 | 使用可量化的标准重写 |
| 需求范围蔓延 | 边界不清晰 | 明确范围和非范围 |

## Related Assets

- **Agent**: [../../agents/analyze-requirement.agent.md](../../agents/analyze-requirement.agent.md)
- **Instruction**: [../../instructions/analyze-requirement.instructions.md](../../instructions/analyze-requirement.instructions.md)
- **Prompt**: [../../prompts/analyze-requirement.prompt.md](../../prompts/analyze-requirement.prompt.md)


## Core Knowledge

> Essential knowledge domain for analyze-requirement execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for analyze-requirement excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during analyze-requirement execution.

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
