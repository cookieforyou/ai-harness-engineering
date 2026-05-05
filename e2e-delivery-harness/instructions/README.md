# Instructions

Instructions 是**执行指南**资产，定义如何在交付流程中执行特定任务。

## 概述

每份指令文档提供：

- **步骤程序**：如何执行工作
- **决策点**：何时分支或升级
- **质量检查点**：每步需要验证什么
- **错误处理**：如何处理失败
- **输出规格**：输出应该是什么样子

## 文件结构

```
instructions/
├── requirement-analysis.instructions.md    # 需求分析执行指南
├── system-design.instructions.md            # 系统设计执行指南
├── task-decomposition.instructions.md      # 任务分解执行指南
├── development.instructions.md        # 开发实现执行指南
├── testing-verification.instructions.md    # 测试验证执行指南
├── deploy-release.instructions.md      # 部署发布执行指南
└── monitoring-operations.instructions.md   # 监控运维执行指南
```

## 标准格式

每份指令文件必须包含：

```yaml
---
name: instruction-name
type: instruction
version: "1.0"
stage: [阶段名称]
author: [作者]
created: [ISO日期]
updated: [ISO日期]
tags: [相关标签]
---
```

### 核心章节

1. **目标 (Objective)**：这份指令要达成什么
2. **前置条件 (Prerequisites)**：开始前必须具备什么
3. **处理步骤 (Process Steps)**：执行的编号步骤
4. **质量门禁 (Quality Gates)**：验证的检查点
5. **故障排除 (Troubleshooting)**：常见问题和解决方案
6. **交接标准 (Handoff Criteria)**：交接前需验证什么

## 命名规范

- 文件名：`{任务名称}.instructions.md`
- 使用 kebab-case（连字符分隔小写）
- 任务名称应反映具体活动

## 使用方式

在加载 Agent 和 Skill 之后执行 Instructions。它提供完成工作的程序框架。

## 相关资产

- **Agents**: [../agents/](..//agents/) - 角色定义
- **Prompts**: [../prompts/](..//prompts/) - 提示词模板
- **Skills**: [../skills/](..//skills/) - 能力模块
