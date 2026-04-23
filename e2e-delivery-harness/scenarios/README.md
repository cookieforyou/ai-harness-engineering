# Scenarios

Scenarios 是**场景包**，将实际用例与推荐的资产组合关联起来。

## 概述

每个场景包映射：

- **目的 (Purpose)**：场景要达成什么
- **主要资产**：核心的 Agent、Instruction 和 Prompt
- **支持技能**：需要的额外技能
- **预期输出**：场景应该产出什么
- **验证 (Validation)**：如何验证输出

## 目录结构

```
scenarios/
├── requirement-analysis/
│   └── SCENARIO.md           # 需求分析场景
├── system-design/
│   └── SCENARIO.md           # 系统设计场景
├── task-decomposition/
│   └── SCENARIO.md           # 任务分解场景
├── development/
│   └── SCENARIO.md           # 开发实现场景
├── testing/
│   └── SCENARIO.md           # 测试验证场景
├── deployment/
│   └── SCENARIO.md           # 部署发布场景
└── monitoring/
    └── SCENARIO.md           # 监控运维场景
```

## 标准场景包

一个标准包应包含：

- **purpose**：这个场景的目标
- **primary agent**：这个场景的主要 Agent
- **primary instruction**：执行指南
- **primary prompt**：提示词模板
- **supporting skills**：需要的额外技能
- **expected output**：场景应该产出什么
- **prerequisites**：必须具备什么
- **quality gates**：验证检查点
- **handoff protocol**：如何过渡到下一阶段

## 标准格式

每个场景文件必须包含：

```yaml
---
name: scenario-name
type: scenario
version: "1.0"
stage: [阶段名称]
author: [作者]
created: [ISO日期]
updated: [ISO日期]
tags: [相关标签]
---
```

## 场景工作流

```
启动 → 加载主要资产 → 使用技能执行
     → 验证输出 → 质量门禁检查
     → 交接给下一阶段 → 完成
```

## 命名规范

- 目录：`{场景名称}/`
- 主文件：`SCENARIO.md`（大写）
- 目录名使用 kebab-case（连字符分隔小写）

## 使用方式

场景是用户最快的入门入口。它们为特定用例提供完整、一致的资产组合。

## 相关资产

- **Agents**: [../agents/](..//agents/) - 角色定义
- **Instructions**: [../instructions/](..//instructions/) - 执行指南
- **Prompts**: [../prompts/](..//prompts/) - 提示词模板
- **Skills**: [../skills/](..//skills/) - 能力模块
