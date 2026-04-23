# Prompts

Prompts 是**提示词模板**，指导 AI 模型为特定任务生成合适的响应。

## 概述

每个提示词模板提供：

- **上下文设置**：任务的背景信息
- **任务描述**：需要完成什么
- **输入规格**：提示词期望的输入
- **输出格式**：输出应该如何结构化
- **示例**：理想输出的可选示例

## 文件结构

```
prompts/
├── analyze-requirement.prompt.md      # 需求分析提示词
├── design-system.prompt.md            # 系统设计提示词
├── decompose-task.prompt.md           # 任务分解提示词
├── implement-feature.prompt.md        # 功能实现提示词
├── verify-test.prompt.md             # 测试验证提示词
├── deploy-release.prompt.md          # 部署发布提示词
└── monitor-operate.prompt.md         # 监控运维提示词
```

## 标准格式

每个提示词文件必须包含：

```yaml
---
name: prompt-name
type: prompt
version: "1.0"
stage: [阶段名称]
author: [作者]
created: [ISO日期]
updated: [ISO日期]
tags: [相关标签]
---
```

### 核心章节

1. **系统提示词 (System Prompt)**：角色和上下文定义
2. **用户提示词模板 (User Prompt Template)**：包含占位符的实际提示词
3. **输入变量 (Input Variables)**：期望变量的定义
4. **输出格式 (Output Format)**：期望的响应结构
5. **约束 (Constraints)**：任何限制或要求

## 提示词模板语法

```
{{variable_name}}     # 必需变量
[[optional_var]]     # 可选变量
{{#each items}}      # 循环块
{{/each}}
```

## 命名规范

- 文件名：`{动作名称}.prompt.md`
- 使用 kebab-case（连字符分隔小写）
- 动作名称应遵循"动词-名词"模式（如 `analyze-requirement`）

## 使用方式

在运行时通过用当前上下文的实际值填充模板变量来实例化提示词。

## 最佳实践

- 使用清晰、具体的指令
- 为复杂输出包含示例
- 明确指定输出格式
- 保持提示词专注于一个任务

## 相关资产

- **Agents**: [../agents/](..//agents/) - 角色定义
- **Instructions**: [../instructions/](..//instructions/) - 执行指南
- **Skills**: [../skills/](..//skills/) - 能力模块
