# Skills

Skills 是**能力模块**，封装特定领域的知识和操作流程。

## 概述

每个技能模块包含：

- **领域知识**：该领域的专业知识和最佳实践
- **操作流程**：如何执行特定任务
- **工具参考**：可用的工具和资源
- **示例**：技能使用的演示
- **验证标准**：如何验证技能执行

## 目录结构

```
skills/
├── requirement-analysis/
│   ├── SKILL.md              # 需求分析技能
│   └── resources/            # 辅助资源
├── system-design/
│   ├── SKILL.md
│   └── resources/
├── task-decomposition/
│   ├── SKILL.md
│   └── resources/
├── development/
│   ├── SKILL.md
│   └── resources/
├── testing/
│   ├── SKILL.md
│   └── resources/
├── deployment/
│   ├── SKILL.md
│   └── resources/
└── monitoring/
    ├── SKILL.md
    └── resources/
```

## 标准格式

每个技能文件必须包含：

```yaml
---
name: skill-name
type: skill
version: "1.0"
stage: [阶段名称]
author: [作者]
created: [ISO日期]
updated: [ISO日期]
tags: [相关标签]
---
```

### 核心章节

1. **技能概述 (Skill Overview)**：这个技能做什么
2. **前置条件 (Prerequisites)**：必须具备什么
3. **知识库 (Knowledge Base)**：领域专业知识内容
4. **操作流程 (Procedures)**：分步说明
5. **工具与资源 (Tools & Resources)**：可用工具和参考
6. **验证 (Validation)**：如何验证完成
7. **示例 (Examples)**：使用演示

## 命名规范

- 目录：`{技能名称}/`
- 主文件：`SKILL.md`（大写）
- 目录名使用 kebab-case（连字符分隔小写）

## 技能组成

每个技能通常包含：

| 组成部分 | 描述 |
|---------|------|
| Overview | 高级描述 |
| Concepts | 领域知识 |
| Procedures | 操作指南 |
| Tools | 可用工具 |
| Examples | 使用演示 |
| Validation | 成功标准 |

## 使用方式

在加载 Agent 之后、执行 Instructions 之前加载 Skills。它为任务完成提供知识基础。

## 相关资产

- **Agents**: [../agents/](..//agents/) - 角色定义
- **Instructions**: [../instructions/](..//instructions/) - 执行指南
- **Prompts**: [../prompts/](..//prompts/) - 提示词模板
