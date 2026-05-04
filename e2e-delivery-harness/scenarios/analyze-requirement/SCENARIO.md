---
name: analyze-requirement
description: 需求分析场景，负责将原始业务需求转换为结构化的需求规格说明书
type: scenario
category: planning
stage: requirement-analysis
version: "1.1.0"
---

# Analyze Requirement

## Purpose

将原始业务需求转换为结构化的需求规格说明书，确保需求的完整性、一致性和可追溯性。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成需求分析工作

### Think-Aloud Protocol

```
[THINK] 理解业务背景和目标
   ↓
[ANALYZE] 识别干系人和诉求
   ↓
[GATHER] 收集和整理需求
   ↓
[MODEL] 构建业务模型
   ↓
[SPECIFY] 编写需求规格
   ↓
[VALIDATE] 与干系人确认
```

### Step-by-Step Reasoning

**Step 1: 业务理解**
- 问：业务背景和核心目标是什么？
- 验证：与业务方确认理解
- 检查：是否了解行业背景和约束

**Step 2: 干系人分析**
- 问：谁是主要干系人？他们各自的诉求是什么？
- 验证：列出干系人矩阵
- 检查：是否覆盖所有关键干系人

**Step 3: 需求收集**
- 问：收集到的需求是否完整？
- 验证：需求覆盖业务场景
- 检查：功能需求与非功能需求

**Step 4: 业务建模**
- 问：业务流程是否清晰？
- 验证：绘制业务流程图
- 检查：识别关键路径和分支

**Step 5: 需求规格化**
- 问：需求是否SMART？
- 验证：每条需求可测试
- 检查：需求可追溯到业务目标

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 干系人确认 | 是否与所有关键干系人确认需求？ |
| DC-002 | 需求完整性 | 是否覆盖所有业务场景？ |
| DC-003 | 需求可测试性 | 每条需求是否有验收标准？ |
| DC-004 | 优先级排序 | 需求优先级是否经过共识？ |

## Error Handling

### 需求模糊

| 属性 | 值 |
|------|-----|
| **识别信号** | 需求描述含糊不清，存在多种理解 |
| **处理方式** | 1. 列出所有可能的理解；2. 与业务方澄清；3. 选择最合理理解；4. 记录决策依据 |
| **升级条件** | 业务方无法澄清超过3次 |

### 干系人冲突

| 属性 | 值 |
|------|-----|
| **识别信号** | 不同干系人对同一需求有矛盾要求 |
| **处理方式** | 1. 识别冲突点；2. 分析各方诉求；3. 提出折中方案；4. 高层拍板 |
| **升级条件** | 无法达成共识超过2轮 |

### 需求蔓延

| 属性 | 值 |
|------|-----|
| **识别信号** | 需求范围不断扩大，超出原定边界 |
| **处理方式** | 1. 标记新增需求；2. 评估影响；3. 与产品负责人确认；4. 调整范围或延期 |
| **升级条件** | 影响超过20%原定范围 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `REQ-COVER` | ≥95% | 需求覆盖率：已分析需求占总需求比例 |
| `STAKEHOLDER-ID` | 100% | 干系人识别率：关键干系人全部识别 |
| `AC-CLARITY` | ≥90% | 验收标准清晰度：可量化验收标准占比 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

```
✅ 需求规格说明书已完成
✅ 干系人分析报告已输出
✅ 业务流程图已绘制
✅ 用例模型已构建
✅ 需求已评审通过
✅ 所有疑问已澄清
```

### 交付物清单

1. **需求规格说明书 (SRS)**：结构化的需求文档
2. **干系人分析报告**：干系人识别和诉求分析
3. **业务流程图 (BPMN)**：主要业务流程可视化
4. **用例模型 (UML)**：系统用例定义

## Primary Assets

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/analyze-requirement.agent.md` | 需求分析角色 |
| **Prompt** | `../../prompts/analyze-requirement.prompt.md` | 需求分析提示词 |
| **Instruction** | `../../instructions/analyze-requirement.instructions.md` | 需求分析技术指令 |
| **Skill** | `../../skills/analyze-requirement/SKILL.md` | 需求分析技能 |

## Prerequisites

### 必需前置条件

1. 业务方提出需求请求
2. 具备项目背景信息
3. 可联系到关键干系人

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `project_name` | 是 | 项目名称 |
| `raw_requirements` | 是 | 原始需求描述 |
| `stakeholders` | 否 | 已知干系人列表 |
| `business_context` | 否 | 业务背景信息 |
