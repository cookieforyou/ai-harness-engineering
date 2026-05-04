---
name: implement-feature
description: 开发实现场景，按照任务清单完成代码开发、单元测试和文档更新
type: scenario
category: development
stage: development
version: "1.1.0"
---

# Implement Feature

## Purpose

按照任务清单完成代码开发、单元测试和文档更新，确保代码质量和交付进度。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成开发实现工作

### Think-Aloud Protocol

```
[THINK] 理解任务需求和验收标准
   ↓
[DESIGN] 设计实现方案
   ↓
[CODE] 编写代码和单元测试
   ↓
[CHECK] 自检代码规范和质量
   ↓
[REVIEW] 提交代码审查
   ↓
[FIX] 修复审查反馈
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

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 需求理解 | 验收标准是否清晰？ |
| DC-002 | 方案合理性 | 是否符合架构设计？ |
| DC-003 | 代码规范 | 是否遵循编码规范？ |
| DC-004 | 测试覆盖 | 核心逻辑是否全覆盖？ |

## Error Handling

### 验收标准不清晰

| 属性 | 值 |
|------|-----|
| **识别信号** | 验收标准模糊或有歧义 |
| **处理方式** | 1. 列出所有可能的理解；2. 选择最合理的理解；3. 在代码注释中说明假设；4. 标记为 [需确认] |
| **升级条件** | 影响功能实现 |

### 技术难点

| 属性 | 值 |
|------|-----|
| **识别信号** | 遇到无法解决的技术问题 |
| **处理方式** | 1. 分析问题根本原因；2. 尝试替代方案；3. 如无法解决，向上升级；4. 记录尝试的解决方案 |
| **升级条件** | 阻塞任务完成 |

### 设计问题

| 属性 | 值 |
|------|-----|
| **识别信号** | 设计与实现不匹配 |
| **处理方式** | 1. 分析差异影响；2. 判断是设计还是实现问题；3. 联系系统设计师 |
| **升级条件** | 需要修改设计 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `CODE-COVERAGE` | ≥80% | 单元测试覆盖率 |
| `BUG-DENSITY` | ≤0.5/KLOC | 缺陷密度：每千行代码缺陷数 |
| `CYCLOMATIC` | ≤15 | 圈复杂度：函数平均圈复杂度 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

```
✅ 代码实现完成
✅ 单元测试通过
✅ 代码规范检查通过
✅ Code Review 通过
✅ 接口文档已更新
✅ 相关文档已同步
```

### 交付物清单

1. **源代码**：功能实现代码
2. **单元测试**：测试用例和报告
3. **接口文档**：API 接口说明
4. **部署脚本**：部署配置（如有）

## Primary Assets

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/implement-feature.agent.md` | 开发实现角色 |
| **Prompt** | `../../prompts/implement-feature.prompt.md` | 功能实现提示词 |
| **Instruction** | `../../instructions/implement-feature.instructions.md` | 开发实现技术指令 |
| **Skill** | `../../skills/implement-feature/SKILL.md` | 功能实现技能 |

## Prerequisites

### 必需前置条件

1. 任务分解已完成
2. 技术方案已确认
3. 接口定义已明确

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `task_id` | 是 | 任务ID |
| `task_name` | 是 | 任务名称 |
| `acceptance_criteria` | 是 | 验收标准 |
| `tech_stack` | 是 | 技术栈 |
