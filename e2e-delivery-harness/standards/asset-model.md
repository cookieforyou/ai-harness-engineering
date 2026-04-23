# Asset Model - 资产模型规范

## 概述

本文档定义了 E2E Delivery Harness 资产库的核心资产模型，包括资产类型、层级关系和组合模式。

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

## 资产层级

```
Scenario (场景层)
├── Agent (角色定义)
├── Instruction (操作指令)
├── Prompt (提示词)
└── Skills[] (技能组合)
    └── Skill (技能模块)
```

## Agent 资产模型

```yaml
---
name: <agent-name>
description: <role-description>
tools: [<tool-list>]
version: <version>
---
```

**字段说明**：

| 字段 | 必填 | 描述 |
|------|------|------|
| name | 是 | 角色名称，采用 kebab-case |
| description | 是 | 角色职责描述 |
| tools | 是 | 可用工具列表 |
| version | 否 | 版本号 |

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
- Agent: [../agents/requirement-analyst.agent.md](../agents/requirement-analyst.agent.md)
- Skill: [../skills/requirement-analysis/SKILL.md](../skills/requirement-analysis/SKILL.md)
```

### 绝对路径引用

```markdown
资产路径：${HARNESS_ROOT}/agents/requirement-analyst.agent.md
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
