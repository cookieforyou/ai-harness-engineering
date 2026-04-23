# Agents

Agent 是 AI Harness 中的**角色定义**资产，定义 AI Agent 在特定交付阶段的身份、能力边界和行为模式。

## 概述

每个 Agent 定义包含：

- **角色 (Role)**：Agent 在交付流程中的身份定位
- **能力 (Capabilities)**：Agent 能做什么、应该关注什么
- **约束 (Constraints)**：Agent 行为的边界和限制
- **职责 (Responsibilities)**：Agent 负责的内容
- **交接 (Handoffs)**：Agent 如何将工作转交给下一阶段

## 文件结构

```
agents/
├── requirement-analyst.agent.md    # 需求分析师
├── system-designer.agent.md        # 系统设计师
├── task-decomposer.agent.md        # 任务分解师
├── developer.agent.md              # 开发工程师
├── tester.agent.md                 # 测试工程师
├── devops-engineer.agent.md        # 运维工程师
└── sre-monitor.agent.md            # SRE 监控工程师
```

## 标准格式

每个 Agent 文件必须包含：

```yaml
---
name: agent-name
type: agent
version: "1.0"
stage: [阶段名称]
author: [作者]
created: [ISO日期]
updated: [ISO日期]
tags: [相关标签]
---
```

### 核心章节

1. **角色定义 (Role Definition)**：Agent 的身份定位
2. **能力 (Capabilities)**：Agent 能完成什么
3. **约束 (Constraints)**：Agent 不应该做什么
4. **职责 (Responsibilities)**：Agent 拥有的责任
5. **交接协议 (Handoff Protocol)**：如何向下一阶段过渡

## 命名规范

- 文件名：`{角色名称}.agent.md`
- 使用 kebab-case（连字符分隔小写）
- 角色名称应具有描述性，以动作为导向

## 使用方式

进入交付阶段时，首先加载 Agent。它定义了后续技能和指令执行时的上下文和边界。

## 相关资产

- **Instructions**: [../instructions/](..//instructions/) - 执行指南
- **Prompts**: [../prompts/](..//prompts/) - 提示词模板
- **Skills**: [../skills/](..//skills/) - 能力模块
