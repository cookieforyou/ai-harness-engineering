---
name: design-system
description: 将需求规格转换为技术架构设计方案，包括组件设计、接口设计、数据设计和部署架构
category: design
version: "1.1.0"
---

# System Design Skill

## Use When

使用此技能的场景：

- 需求分析完成后，需要进行技术架构设计
- 系统需要重构或重大技术升级
- 新技术选型需要评估和决策
- 跨系统集成需要架构层面的规划

## Expected Input

### 必需输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 需求规格说明书 | 文件 | 来自需求分析阶段的输出 |
| 设计约束 | 文本 | 技术约束和标准 |

### 可选输入

| 输入项 | 类型 | 描述 |
|--------|------|------|
| 团队能力信息 | 文本 | 团队的技术栈和能力情况 |
| 资源限制 | 文本 | 时间和人力的限制条件 |
| 历史设计 | 文件 | 相关的历史设计文档 |

## Instructions

### 步骤 1：需求理解与分解

**目标**：深入理解业务需求和技术约束

**操作**：
1. 梳理核心业务功能
2. 识别关键性能指标
3. 理解数据处理需求
4. 确定设计边界和假设

**检查点**：
- [ ] 核心功能已梳理
- [ ] 性能指标已识别
- [ ] 设计边界已确定

### 步骤 2：架构选型

**目标**：评估并选择适合项目特点的架构风格

**操作**：
1. 调研可选架构风格（单体、微服务、分层等）
2. 评估各风格与项目的匹配度
3. 考虑团队能力和运维成本
4. 做出决策并记录理由

**检查点**：
- [ ] 架构风格已选择
- [ ] 决策理由已记录
- [ ] 备选方案已评估

### 步骤 3：组件设计

**目标**：划分系统组件并定义各组件的职责

**操作**：
1. 按业务领域划分组件
2. 按层次划分组件（前端、后端、数据）
3. 识别共享组件和基础组件
4. 定义组件的边界和职责
5. 设计组件间的协作关系

**检查点**：
- [ ] 组件划分合理
- [ ] 职责定义清晰
- [ ] 协作关系已设计

### 步骤 4：数据架构设计

**目标**：设计数据模型和存储方案

**操作**：
1. 设计核心数据模型
2. 确定数据存储策略（关系型、NoSQL、缓存）
3. 设计数据流和处理流程
4. 考虑数据安全和隐私保护
5. 设计数据迁移和同步方案

**检查点**：
- [ ] 数据模型已设计
- [ ] 存储策略已确定
- [ ] 数据安全已考虑

### 步骤 5：接口设计

**目标**：设计组件间的接口和数据交互

**操作**：
1. 识别对外接口和内部接口
2. 确定接口协议（REST、gRPC、消息队列）
3. 设计接口规范和数据格式
4. 定义错误码和异常处理
5. 绘制接口交互图

**检查点**：
- [ ] 接口已识别
- [ ] 协议已确定
- [ ] 规范已定义

### 步骤 6：技术选型

**目标**：确定各组件的技术选型

**操作**：
1. 根据组件需求选择技术栈
2. 评估技术的成熟度和风险
3. 考虑团队的技能储备
4. 做出选型决策并记录理由

**检查点**：
- [ ] 技术栈已确定
- [ ] 选型理由已记录
- [ ] 风险已评估

### 步骤 7：部署架构设计

**目标**：设计系统的部署拓扑和策略

**操作**：
1. 设计部署拓扑结构
2. 确定部署策略（滚动、蓝绿、灰度）
3. 设计容灾和备份方案
4. 规划扩容和缩容机制
5. 考虑基础设施需求

**检查点**：
- [ ] 部署拓扑已设计
- [ ] 策略已确定
- [ ] 容灾方案已规划

### 步骤 8：风险分析与应对

**目标**：识别技术风险并制定应对策略

**操作**：
1. 识别技术风险（新技术、复杂集成）
2. 评估风险发生概率和影响
3. 制定风险缓解措施
4. 制定风险应急预案

**检查点**：
- [ ] 风险已识别
- [ ] 应对措施已制定
- [ ] 应急预案已准备

### 步骤 9：方案评审

**目标**：评审架构设计方案

**操作**：
1. 准备评审材料
2. 组织评审会议
3. 收集评审反馈
4. 根据反馈修订方案
5. 获得评审通过

**检查点**：
- [ ] 评审已完成
- [ ] 问题已修复
- [ ] 方案已确认

## Expected Output

### 产出列表

1. **架构设计文档**：完整的技术架构设计
2. **组件设计文档**：组件详细设计
3. **接口设计文档**：API 和数据接口定义
4. **数据设计文档**：数据模型和存储方案
5. **风险分析报告**：风险识别和应对策略

### 输出格式

```markdown
## 架构设计文档

### 文档信息
...

### 设计范围与目标
...

### 架构概述
...

### 技术选型
...

### 系统架构
...

### 组件设计
...

### 数据设计
...

### 接口设计
...

### 部署架构
...

### 风险分析
...

### 实施计划
...
```

## Quality Criteria

| 维度 | 标准 | 检查方法 |
|------|------|----------|
| 需求覆盖 | 所有需求有对应设计 | 需求映射 |
| 架构合理性 | 架构风格与项目匹配 | 评审检查 |
| 风险可控 | 主要风险有应对 | 风险检查 |
| 可落地性 | 方案可实施 | 可行性评估 |

## Related Assets

- **Agent**: [../../agents/design-systemer.agent.md](../../agents/design-systemer.agent.md)
- **Instruction**: [../../instructions/design-system.instructions.md](../../instructions/design-system.instructions.md)
- **Prompt**: [../../prompts/design-system.prompt.md](../../prompts/design-system.prompt.md)


## Core Knowledge

> Essential knowledge domain for design-system execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for design-system excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during design-system execution.

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
