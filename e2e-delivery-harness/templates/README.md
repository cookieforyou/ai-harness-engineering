# Templates

Templates 提供**起点**用于创建新资产，确保一致性和完整性。

## 概述

模板包含：

- **YAML front matter**：必需的元数据字段
- **章节结构**：必需和可选的章节
- **内容占位符**：包含什么的指导
- **示例**：可选的示例内容

## 文件结构

```
templates/
├── agent-template.agent.md              # Agent 模板
├── instruction-template.instructions.md  # Instruction 模板
├── prompt-template.prompt.md            # Prompt 模板
└── skill-template/
    └── SKILL.md                         # Skill 模板
```

## Agent 模板 (agent-template.agent.md)

创建 Agent 定义的起点。

### 必需章节

```markdown
---
# YAML front matter 元数据
---

# Agent 名称

## 角色定义

## 能力

## 约束

## 职责

## 交接协议
```

## Instruction 模板 (instruction-template.instructions.md)

创建 Instruction 文档的起点。

### 必需章节

```markdown
---
# YAML front matter 元数据
---

# Instruction 标题

## 目标

## Prerequisites

## 处理步骤

## 质量门禁

## 故障排除

## 交接标准
```

## Prompt 模板 (prompt-template.prompt.md)

创建 Prompt 模板的起点。

### 必需章节

```markdown
---
# YAML front matter 元数据
---

# Prompt 标题

## 系统提示词

## 用户提示词模板

## 输入变量

## 输出格式

## 约束
```

## Skill 模板 (skill-template/SKILL.md)

创建 Skill 模块的起点。

### 必需章节

```markdown
---
# YAML front matter 元数据
---

# Skill 名称

## 技能概述

## Prerequisites

## 知识库

## 操作流程

## 工具与资源

## 验证

## Example
```

## 使用方式

创建新资产：

1. 复制适当的模板
2. 填写 YAML front matter
3. 用实际内容替换占位符
4. 遵循章节结构
5. 按质量评分验证
6. 提交审查

## 命名规范

- 模板文件名包含 `-template`
- 主文件名匹配资产类型命名惯例

## 相关资产

- **Standards**: [../standards/](..//standards/) - 规范性指南
- **Examples**: 参考相应目录中的现有资产
