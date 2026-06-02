# Asset Model - 资产模型规范

## 概述

本文档定义了 E2E Delivery Harness 资产库的核心资产模型，包括资产类型、层级关系和组合模式。

**Harness Engineering 对齐**：各资产如何映射六层驾驭模型，见 [harness-engineering.md](harness-engineering.md)。

## 资产类型

### 基础资产

| 类型 | 描述 | 文件格式 |
|------|------|----------|
| Agent | AI 角色代理定义 | `*.agent.md` |
| Skill | AI 技能模块 | `skills/*/SKILL.md` |
| Instruction | 操作指令 | `*.instructions.md` |
| Prompt | AI 提示词 | `*.prompt.md` |

### 复合资产

| 类型 | 描述 | 文件格式 |
|------|------|----------|
| Scenario | 场景定义 | `scenarios/*/SCENARIO.md` |
| Template | 资产模板 | `templates/*/` |

### 支持资产

| 类型 | 描述 | 文件格式 |
|------|------|----------|
| Standard | 规范标准 | `standards/*.md` |
| Evaluation | 评估工具 | `evaluations/*.md` |
| Pipeline | 工作流定义 | `workflows/*.pipeline.md` |
| Context | 上下文定义 | `contexts/*.md` |

## 资产层级

```
Pipeline (工作流层)
├── 定义端到端流程
└── 编排多个 Scenario

Scenario (场景层) ← AI 主要入口
├── Chain of Thought (思维链)
├── Error Handling (错误处理)
└── 引用以下资产:
    ├── Agent (角色定义)
    ├── Instruction (操作指令)
    ├── Prompt (提示词)
    └── Skills[] (技能组合)

Context (上下文层)
├── Global Context (全局上下文)
└── Handover Context (交接上下文)

Evaluation (评估层)
├── Regression Checklist (回归检查)
└── Scorecard (质量评分)
```

## Agent 资产模型

```yaml
---
name: <agent-name>
description: <role-description>
type: agent
tools: [<tool-list>]
harness_layers: [goal, strategy, tooling, constraint, feedback, observability]
version: "<semver>"
status: active
---
```

**字段说明**：

| 字段 | 必填 | 描述 |
|------|------|------|
| name | 是 | 角色名称，采用 kebab-case |
| description | 是 | 角色职责描述 |
| type | 是 | 固定值 `agent` |
| tools | 是 | Tooling 层：可用工具列表（非空） |
| harness_layers | 是 | 本角色涉及的 Harness 层 |
| version | 否 | 版本号 |
| status | 否 | draft / active / deprecated |

## Skill 资产模型

```yaml
---
name: <skill-name>
description: <skill-description>
category: <category>
version: <version>
---
```

**字段说明**：

| 字段 | 必填 | 描述 |
|------|------|------|
| name | 是 | 技能名称 |
| description | 是 | 技能描述 |
| category | 是 | 技能分类 |
| version | 否 | 版本号 |

## Instruction 资产模型

```yaml
---
applyTo: "<glob-pattern>"
phase: <phase-name>
order: <priority>
---
```

**字段说明**：

| 字段 | 必填 | 描述 |
|------|------|------|
| applyTo | 是 | 适用文件模式 |
| phase | 是 | 所属阶段 |
| order | 否 | 执行优先级 |

## Pipeline 资产模型

```yaml
---
name: <pipeline-name>
type: pipeline
version: "<version>"
description: <pipeline-description>
stages: [<stage1>, <stage2>, ...]
---
```

**字段说明**：

| 字段 | 必填 | 描述 |
|------|------|------|
| name | 是 | Pipeline 名称，采用 kebab-case |
| type | 是 | 固定值 `pipeline` |
| description | 是 | Pipeline 描述 |
| stages | 是 | 包含的阶段列表 |

**标准章节**：

1. Overview - 流程概述
2. Stage Flow - 阶段流程图
3. Stage Definitions - 各阶段定义
4. Data Flow - 数据流向
5. Error Handling - 异常处理
6. Quality Gates - 质量门禁

## Context 资产模型

```yaml
---
name: <context-name>
type: context
version: "<version>"
scope: <all-stages|stage-specific>
---
```

**字段说明**：

| 字段 | 必填 | 描述 |
|------|------|------|
| name | 是 | Context 名称 |
| type | 是 | 固定值 `context` |
| scope | 是 | 适用范围 |

**Context 类型**：

| 类型 | 描述 | 文件格式 |
|------|------|----------|
| Global Context | 贯穿全流程的共享数据 | `global-context.md` |
| Handover Context | 阶段间交接数据 | `handover-context.template.md` |

## Scenario 资产模型

```yaml
---
name: <scenario-name>
phase: <phase-name>
difficulty: <level>
prerequisites: []
---
```

**字段说明**：

| 字段 | 必填 | 描述 |
|------|------|------|
| name | 是 | 场景名称 |
| phase | 是 | 所属阶段 |
| difficulty | 是 | 难度等级 |
| prerequisites | 否 | 前置条件 |

## 资产组合模式

### 场景组合

```
场景 = Agent + Instruction + Prompt + Skills[]
```

### 流水线组合

```
Pipeline = Scenario[] (按顺序连接)
```

### 角色协同

```
Team = Agent[] (主从关系定义)
```

## 资产引用规范

### 相对路径引用

```markdown
依赖资产：
- Agent: [../agents/analyze-requirement.agent.md](../agents/analyze-requirement.agent.md)
- Skill: [../skills/analyze-requirement/SKILL.md](../skills/analyze-requirement/SKILL.md)
```

### 绝对路径引用

```markdown
资产路径：${HARNESS_ROOT}/agents/analyze-requirement.agent.md
```

## 资产元数据

每个资产应包含以下元数据：

| 字段 | 描述 |
|------|------|
| created | 创建时间 |
| updated | 更新时间 |
| author | 作者 |
| tags | 标签 |
| status | 状态（draft/active/deprecated） |
