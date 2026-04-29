---
name: <scenario-name>
type: scenario
version: "1.0.0"
description: <scenario-description>
category: <category>
stage: <stage-name>
---

# {scenario-name}

## Purpose

{场景目标描述，1-3句话说明此场景的核心目标}

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成场景工作

### Think-Aloud Protocol

```
[THINK] 步骤1：<子目标>
   ↓
[THINK] 步骤2：<子目标>
   ↓
[ANALYZE] 步骤3：<分析活动>
   ↓
[IMPLEMENT] 步骤4：<实施活动>
   ↓
[VERIFY] 验证和输出
```

### Step-by-Step Reasoning

**Step 1: {子步骤1}**
- 问：{自问1}？
- 验证：{验证方式}
- 检查：{检查点}

**Step 2: {子步骤2}**
- 问：{自问1}？
- 验证：{验证方式}
- 检查：{检查点}

**Step 3: {子步骤3}**
- 问：{自问1}？
- 验证：{验证方式}
- 检查：{检查点}

## Decision Checkpoints

> 执行过程中需要确认的决策点

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | {条件1} | {决策1} |
| DC-002 | {条件2} | {决策2} |
| DC-003 | {条件3} | {决策3} |

## Error Handling

> 遇到以下情况时的处理策略

### 错误类型 1：{错误描述}

| 属性 | 值 |
|------|-----|
| **识别信号** | {信号描述} |
| **处理方式** | {处理方式} |
| **升级条件** | {升级条件} |

### 错误类型 2：{错误描述}

| 属性 | 值 |
|------|-----|
| **识别信号** | {信号描述} |
| **处理方式** | {处理方式} |
| **升级条件** | {升级条件} |

## Handover Criteria

> 场景完成的验收标准

```
✅ 交付物 1：{标准1}
✅ 交付物 2：{标准2}
✅ 交付物 3：{标准3}
```

### 交付物清单

1. **{交付物1}**：{说明}
2. **{交付物2}**：{说明}

## Primary Assets

> 场景执行所需的核心资产

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/{agent}.agent.md` | 角色定义 |
| **Prompt** | `../../prompts/{prompt}.prompt.md` | 执行提示词 |
| **Instruction** | `../../instructions/{instruction}.instructions.md` | 技术指令 |
| **Skill** | `../../skills/{skill}/SKILL.md` | 技能知识 |

## Prerequisites

### 必需前置条件

1. {前置条件1}
2. {前置条件2}
3. {前置条件3}

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| 输入 1 | 是/否 | {描述} |
| 输入 2 | 是/否 | {描述} |
