---
applyTo: "**/*.md"
phase: system-design
order: 2
version: "1.0.0"
---

# System Design Instructions

## Purpose

本文档定义了系统设计阶段的标准操作流程、质量检查标准和工作产出规范。系统设计是将需求规格转换为具体技术架构方案的设计过程。

## Investigation Flow

### 流程概览

```
需求理解 → 架构选型 → 组件设计 → 接口设计 → 风险分析 → 方案评审
```

### 步骤 1：需求理解

**目的**：深入理解业务需求和技术约束

**输入**：
- 需求规格说明书
- 非功能需求指标
- 技术约束条件

**操作**：

1. **需求梳理**
   - 梳理核心业务功能
   - 识别关键性能指标
   - 理解数据处理需求

2. **约束识别**
   - 识别技术约束（技术栈、安全、性能）
   - 识别资源约束（预算、人力、时间）
   - 识别环境约束（基础设施、第三方依赖）

3. **设计前提**
   - 确定设计边界
   - 明确设计假设
   - 识别风险接受标准

**输出**：需求理解备忘录

### 步骤 2：架构选型

**目的**：评估并选择适合项目特点的架构风格

**输入**：
- 需求理解备忘录
- 技术约束条件
- 团队技术能力

**操作**：

1. **架构风格调研**
   - 单体架构 vs 微服务架构
   - 分层架构 vs 事件驱动架构
   - 云原生架构 vs 传统架构

2. **评估维度**
   - 业务复杂度匹配度
   - 团队能力匹配度
   - 运维成本考量
   - 扩展性考量

3. **决策记录**
   - 选择架构风格及理由
   - 记录备选方案及放弃原因
   - 明确架构原则

**输出**：架构选型报告

### 步骤 3：组件设计

**目的**：划分系统组件并定义各组件的职责

**输入**：
- 架构选型报告
- 业务功能需求
- 数据处理需求

**操作**：

1. **组件识别**
   - 按业务领域划分组件
   - 按层次划分组件（前端、后端、数据）
   - 识别共享组件和基础组件

2. **职责定义**
   - 明确每个组件的核心职责
   - 定义组件的边界
   - 标注组件间的协作关系

3. **技术实现**
   - 确定组件的技术选型
   - 定义组件的技术规范
   - 规划组件的部署模式

**输出**：组件设计文档

### 步骤 4：接口设计

**目的**：设计组件间的接口和数据流

**输入**：
- 组件设计文档
- 数据处理需求
- 集成需求

**操作**：

1. **接口识别**
   - 识别组件间的交互点
   - 分类接口类型（同步、异步）
   - 定义接口的调用频率

2. **接口定义**
   - 定义接口协议（REST、gRPC、消息队列）
   - 详细设计接口参数和返回值
   - 定义错误码和异常处理

3. **数据流设计**
   - 绘制数据流图
   - 定义数据存储方案
   - 设计数据同步机制

**输出**：接口设计文档

### 步骤 5：风险分析

**目的**：识别技术风险并制定应对策略

**输入**：
- 架构设计方案
- 技术选型清单
- 历史项目经验

**操作**：

1. **风险识别**
   - 技术风险（新技术、复杂集成）
   - 性能风险（高并发、大数据量）
   - 安全风险（认证、授权、数据保护）
   - 运维风险（监控、部署、扩展）

2. **风险评估**
   - 评估风险发生概率
   - 评估风险影响程度
   - 计算风险优先级

3. **应对策略**
   - 制定风险缓解措施
   - 制定风险应急预案
   - 确定风险接受标准

**输出**：风险分析报告

### 步骤 6：方案评审

**目的**：评审架构设计方案，获得团队和干系人认可

**输入**：
- 完整的架构设计文档
- 评审参与人员

**操作**：

1. **评审准备**
   - 编写评审材料
   - 邀请评审人员
   - 确定评审议程

2. **评审执行**
   - 架构概述讲解
   - 逐个评审关键设计点
   - 收集评审意见

3. **修订确认**
   - 根据评审意见修订
   - 获得评审通过
   - 锁定设计基线

**输出**：架构设计文档（确认版）

## What To Check

### 必检项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 需求覆盖 | 所有需求都有对应设计 | 需求映射表 | 覆盖率 > 95% |
| 架构合理性 | 架构风格与项目匹配 | 评审检查 | 评审通过 |
| 组件划分 | 组件职责清晰、耦合度低 | 组件检查 | 评审通过 |
| 接口设计 | 接口定义完整规范 | 接口检查 | 评审通过 |
| 风险可控 | 主要风险有应对措施 | 风险检查 | 无高风险未处理 |
| 非功能满足 | 非功能需求有对应设计 | 对照检查 | 100% 覆盖 |

### 建议检查项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 可扩展性 | 考虑未来扩展需求 | 评审检查 | 评审通过 |
| 可测试性 | 架构支持测试实施 | 设计检查 | 支持主流测试 |
| 成本效益 | 技术选型成本合理 | 成本分析 | 在预算范围内 |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 |
|------|------|------|
| 完整性 | 覆盖所有设计要点 | 25% |
| 合理性 | 架构方案合理可行 | 30% |
| 风险可控 | 主要风险有应对 | 20% |
| 可落地性 | 方案可实施 | 25% |

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 |
|------|------|------|------|
| 架构设计文档 | .md | 是 | 完整的技术架构设计 |
| 组件设计文档 | .md | 是 | 组件详细设计 |
| 接口设计文档 | .md | 是 | API 和数据接口 |
| 风险分析报告 | .md | 是 | 风险识别和应对 |


## Overview

> High-level description of the design-system execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the design-system scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for design-system.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for design-system execution.

1. **Practice 1**: [Description]
2. **Practice 2**: [Description]
3. **Practice 3**: [Description]


## Error Handling

> Common error scenarios and resolution strategies for design-system.

### Error Category 1
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for design-system deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | [Description] | [How to verify] |
| Standard 2 | [Description] | [How to verify] |
| Standard 3 | [Description] | [How to verify] |
