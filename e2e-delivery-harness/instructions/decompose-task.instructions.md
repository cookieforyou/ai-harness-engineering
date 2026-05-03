---
applyTo: "**/*.md"
phase: task-decomposition
order: 3
version: "1.0.0"
---

# Task Decomposition Instructions

## Purpose

本文档定义了任务分解阶段的标准操作流程、质量检查标准和工作产出规范。任务分解是将架构设计拆解为可执行、可管理的小任务的过程。

## Investigation Flow

### 流程概览

```
任务识别 → 任务细化 → 依赖分析 → 估算排序 → 迭代规划
```

### 步骤 1：任务识别

**目的**：从架构设计中识别需要完成的开发任务

**输入**：
- 架构设计文档
- 组件设计文档
- 接口设计文档

**操作**：

1. **功能拆解**
   - 按组件拆解功能点
   - 按层次拆解（前端、后端、数据）
   - 按业务流程拆解

2. **技术任务识别**
   - 基础设施搭建任务
   - 公共模块开发任务
   - 集成对接任务
   - 测试环境任务

3. **任务分类**
   - 分类：功能开发、技术债务、基础设施、测试、文档
   - 标注任务类型

**输出**：初步任务清单

### 步骤 2：任务细化

**目的**：将大任务拆分为可执行的小任务

**输入**：
- 初步任务清单
- 团队能力信息
- 历史项目数据

**操作**：

1. **粒度控制**
   - 目标粒度：1-3 天可完成
   - 超过 5 天的任务需进一步拆分
   - 少于 0.5 天的任务可合并

2. **任务描述**
   - 每个任务有明确的名称
   - 有清晰的验收标准
   - 有明确的完成定义（Definition of Done）

3. **任务卡片**
   - 描述任务内容
   - 明确验收条件
   - 标注涉及组件
   - 列出技术要点

**输出**：细化后的任务清单

### 步骤 3：依赖分析

**目的**：分析任务间的依赖关系，确保执行顺序合理

**输入**：
- 细化后的任务清单
- 组件关系图
- 接口依赖图

**操作**：

1. **依赖识别**
   - 识别任务间的硬依赖（必须先完成）
   - 识别任务间的软依赖（建议顺序）
   - 识别并行可执行任务

2. **依赖建模**
   - 绘制任务依赖图
   - 标注依赖类型
   - 识别关键路径

3. **冲突检测**
   - 检测循环依赖
   - 检测资源冲突
   - 识别瓶颈任务

**输出**：任务依赖图

### 步骤 4：估算排序

**目的**：评估任务工作量并确定优先级

**输入**：
- 任务依赖图
- 团队能力信息
- 交付时间要求

**操作**：

1. **工作量估算**
   - 使用历史数据参考
   - 采用三点估算法（乐观、悲观、最可能）
   - 考虑学习和准备时间

2. **优先级排序**
   - 依据：业务价值、技术依赖、风险
   - 分类：P0（紧急重要）、P1（重要）、P2（一般）
   - 考虑干系人期望

3. **资源分配**
   - 根据技能匹配分配任务
   - 考虑团队成员负载
   - 标注负责人

**输出**：带优先级的工作量估算

### 步骤 5：迭代规划

**目的**：将任务分配到迭代计划中

**输入**：
- 带优先级的工作量估算
- 迭代周期要求
- 团队可用资源

**操作**：

1. **迭代划分**
   - 确定迭代周期（通常 1-2 周）
   - 确定每个迭代的目标
   - 分配任务到迭代

2. **容量规划**
   - 计算团队可用容量
   - 预留缓冲时间（10-20%）
   - 平衡迭代负载

3. **计划输出**
   - 制定迭代计划表
   - 制定里程碑计划
   - 识别关键风险点

**输出**：迭代计划文档

## What To Check

### 必检项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 任务粒度 | 任务在 1-3 天内可完成 | 估算检查 | 90% 任务在范围内 |
| 依赖完整 | 所有依赖关系已标注 | 依赖图检查 | 无未标注依赖 |
| 无循环依赖 | 任务间无循环依赖 | 依赖分析 | 无发现循环 |
| 优先级明确 | 所有任务有明确优先级 | 优先级检查 | 100% 已标注 |
| 验收标准 | 每个任务有明确验收标准 | DoD 检查 | 100% 有标准 |

### 建议检查项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 估算合理性 | 估算与历史数据对比 | 对比分析 | 偏差 < 20% |
| 迭代平衡 | 迭代间负载相对均衡 | 容量分析 | 负载差 < 30% |
| 风险分散 | 高风险任务不过度集中 | 分布检查 | 无风险集中 |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 |
|------|------|------|
| 完整性 | 所有设计都有对应任务 | 25% |
| 可执行性 | 任务粒度适中可执行 | 30% |
| 依赖清晰 | 依赖关系明确 | 20% |
| 优先级合理 | 优先级与价值匹配 | 25% |

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 |
|------|------|------|------|
| 任务分解清单 | .md | 是 | 完整的任务列表 |
| 任务依赖图 | .md | 是 | 依赖关系说明 |
| 迭代计划 | .md | 是 | 各迭代任务分配 |
| 工作量评估 | .md | 是 | 工时估算汇总 |


## Overview

> High-level description of the decompose-task execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the decompose-task scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for decompose-task.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for decompose-task execution.

1. **Practice 1**: [Description]
2. **Practice 2**: [Description]
3. **Practice 3**: [Description]


## Error Handling

> Common error scenarios and resolution strategies for decompose-task.

### Error Category 1
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for decompose-task deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | [Description] | [How to verify] |
| Standard 2 | [Description] | [How to verify] |
| Standard 3 | [Description] | [How to verify] |
