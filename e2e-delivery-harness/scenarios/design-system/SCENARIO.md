---
name: design-system
description: 系统设计场景，负责设计系统架构、技术方案和数据模型
type: scenario
category: design
stage: system-design
version: 1.1.0
author: AI Harness Engineering Team
---

# Design System

## Purpose

基于需求规格说明书，设计系统的整体架构、技术方案和数据模型，为开发实现提供技术指导。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成系统设计工作

### Think-Aloud Protocol

```
[THINK] 理解系统边界和范围
   ↓
[ANALYZE] 分析非功能性需求
   ↓
[DESIGN] 设计系统架构
   ↓
[MODEL] 设计数据模型
   ↓
[SPECIFY] 定义接口方案
   ↓
[VALIDATE] 技术方案评审
```

### Step-by-Step Reasoning

**Step 1: 系统边界理解**
- 问：系统的边界和范围是什么？
- 验证：与需求规格对照
- 检查：识别核心模块和外部依赖

**Step 2: 非功能性分析**
- 问：性能、安全、可用性要求是什么？
- 验证：量化非功能指标
- 检查：识别技术约束

**Step 3: 架构设计**
- 问：采用什么架构风格？
- 验证：满足非功能需求
- 检查：模块划分合理

**Step 4: 数据建模**
- 问：核心实体和关系是什么？
- 验证：满足业务需求
- 检查：符合范式要求

**Step 5: 接口定义**
- 问：模块间如何交互？
- 验证：接口清晰稳定
- 检查：考虑扩展性

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 架构选型 | 是否适合团队技术能力？ |
| DC-002 | 技术栈 | 是否满足性能要求？ |
| DC-003 | 模块划分 | 是否高内聚低耦合？ |
| DC-004 | 数据模型 | 是否满足业务需求？ |

## Error Handling

### 架构不确定

| 属性 | 值 |
|------|-----|
| **识别信号** | 多种架构方案各有优劣，难以抉择 |
| **处理方式** | 1. 列出各方案优缺点；2. 权重评估；3. 选择最平衡方案；4. 记录决策依据 |
| **升级条件** | 团队无法达成共识 |

### 技术风险

| 属性 | 值 |
|------|-----|
| **识别信号** | 关键技术存在不确定性 |
| **处理方式** | 1. 识别技术风险点；2. 制定应对策略；3. 预留技术验证时间；4. 高层确认 |
| **升级条件** | 风险等级为 High/Critical |

### 需求冲突

| 属性 | 值 |
|------|-----|
| **识别信号** | 设计方案与需求存在冲突 |
| **处理方式** | 1. 分析冲突原因；2. 与需求分析师确认；3. 调整设计或需求；4. 记录决策 |
| **升级条件** | 影响核心功能实现 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `DESIGN-COMPLETENESS` | ≥95% | 设计完整性：必需章节覆盖率 |
| `REQ-TRACE` | 100% | 需求可追溯性：所有需求都有设计对应 |
| `REVIEW-PASS` | ≥90% | 设计评审通过率 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

```
✅ 系统架构图已完成
✅ 技术方案文档已编写
✅ 数据模型已设计
✅ 接口定义已明确
✅ 技术方案已评审通过
✅ 风险清单已识别
```

### 交付物清单

1. **系统架构文档**：架构设计和技术选型
2. **技术方案**：核心模块详细设计
3. **数据模型**：ER图和数据字典
4. **接口定义**：API 接口规格

## Primary Assets

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/design-system.agent.md` | 系统设计角色 |
| **Prompt** | `../../prompts/design-system.prompt.md` | 系统设计提示词 |
| **Instruction** | `../../instructions/design-system.instructions.md` | 系统设计技术指令 |
| **Skill** | `../../skills/design-system/SKILL.md` | 系统设计技能 |

## Prerequisites

### 必需前置条件

1. 需求规格说明书已评审通过
2. 具备技术团队
3. 可获取技术约束信息

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `requirements_spec` | 是 | 需求规格说明书 |
| `tech_constraints` | 否 | 技术约束条件 |
| `team_capability` | 否 | 团队技术能力 |
