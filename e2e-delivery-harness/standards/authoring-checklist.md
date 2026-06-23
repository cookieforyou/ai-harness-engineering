---
name: authoring-checklist
description: "资产创作检查清单标准，定义 Agent/Skill/Instruction/Prompt/Scenario 各类资产创作的质量检查项与提交流程"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'authoring', 'checklist', 'quality', 'scaffold']
---

# Authoring Checklist - 资产创作检查清单

## 概述

本文档为 E2E Delivery Harness 资产库的创作者提供完整的检查清单，确保产出的资产符合质量标准。

**Harness 合规**：创作前阅读 [harness-engineering.md](harness-engineering.md)，完成后运行 `python3 scripts/harness-full-compliance.py`。

## 创作前准备

### 需求确认

- [ ] 明确资产的目标用户
- [ ] 确认资产要解决的问题
- [ ] 了解现有相关资产
- [ ] 确定资产的范围和边界

### 资源准备

- [ ] 收集相关参考资料
- [ ] 整理最佳实践案例
- [ ] 确认命名规范
- [ ] 准备元数据模板

## Agent 创作检查

### 配置段检查

- [ ] 包含完整的 YAML 配置头
- [ ] `name` 字段符合 kebab-case 规范
- [ ] `description` 清晰表达角色职责
- [ ] `tools` 列表完整且合理
- [ ] `version` 格式正确

### 内容检查

- [ ] 包含 `# <Role Name>` 标题
- [ ] 包含 `## Use When` 适用场景
- [ ] 包含 `## Working Rules` 工作规则
- [ ] 工作规则清晰、可执行
- [ ] 包含 `## Handoff` 交接规范

### Example检查

```yaml
---
name: analyze-requirement
description: 负责需求分析与规划的AI角色代理
tools: ["search", "edit", "analyze"]
version: "2.0.0"
---
```

## Skill 创作检查

### 元数据检查

- [ ] 包含完整的 YAML 配置头
- [ ] `name` 字段唯一且有意义
- [ ] `description` 清晰描述技能用途
- [ ] `category` 分类正确

### 内容结构检查

- [ ] `# <Skill Name>` 一级标题
- [ ] `## Use When` 适用场景
- [ ] `## Expected Input` 预期输入
- [ ] `## Instructions` 操作步骤
- [ ] `## Expected Output` 预期输出
- [ ] `## Examples` 示例（如适用）

### 步骤完整性检查

- [ ] 步骤逻辑清晰
- [ ] 步骤之间有合理顺序，每个步骤的执行时间应 ≤15 分钟
- [ ] 每个步骤有明确目标，完成率 ≥95%
- [ ] 包含必要的检查点

## Instruction 创作检查

### 配置段检查

- [ ] 包含 YAML 配置头
- [ ] `applyTo` 模式正确
- [ ] `phase` 所属阶段正确

### 内容检查

- [ ] `# <Instruction Name>` 标题
- [ ] `## Purpose` 目的说明
- [ ] `## Investigation Flow` 调研流程
- [ ] `## What To Check` 检查清单
- [ ] `## Quality Criteria` 质量标准

### 清单完整性检查

- [ ] 检查项全面、不遗漏
- [ ] 清单覆盖率达到 ≥90% 的检查项才可提交
- [ ] 检查项可验证
- [ ] 包含通过/失败判定标准

## Prompt 创作检查

### 元数据检查

- [ ] 包含 YAML 配置头
- [ ] `name` 命名规范
- [ ] `description` 描述清晰

### 内容检查

- [ ] 明确的任务目标
- [ ] 清晰的输入格式
- [ ] 详细的步骤指引
- [ ] 明确的输出格式要求

### 输出格式检查

- [ ] 定义清晰的输出结构
- [ ] 包含所有必需字段
- [ ] 提供格式示例

## Scenario 创作检查

### 元数据检查

- [ ] 包含 YAML 配置头
- [ ] `name` 唯一且规范
- [ ] `phase` 阶段正确
- [ ] `difficulty` 难度合理

### 内容检查

- [ ] `# <Scenario Name>` 标题
- [ ] `## Purpose` 场景目标
- [ ] `## Primary Assets` 依赖资产
- [ ] `## Expected Output` 预期输出
- [ ] `## Prerequisites` 前置条件

### 资产关联检查

- [ ] 引用的 Agent 存在
- [ ] 引用的 Skill 存在
- [ ] 引用的 Instruction 存在
- [ ] 引用的 Prompt 存在

## 文档完整性检查

### 必需章节

- [ ] 概述/背景介绍
- [ ] 核心内容
- [ ] 示例/案例
- [ ] 常见问题

### 格式规范检查

- [ ] 标题层级正确
- [ ] 列表格式一致
- [ ] 代码块有语言标识
- [ ] 链接有效

### 术语一致性检查

- [ ] 使用统一的术语
- [ ] 避免歧义表达
- [ ] 关键术语有定义

## 质量自检

### 可读性检查

- [ ] 段落长度适中
- [ ] 句子简洁明了
- [ ] 避免冗余表达

### 可执行性检查

- [ ] 操作步骤具体可执行
- [ ] 判断标准明确
- [ ] 无歧义指令

### 完整性检查

- [ ] 无遗漏的关键信息
- [ ] 边界情况有覆盖
- [ ] 异常情况有处理

## 提交流程

### 提交前检查

1. [ ] 格式规范自检通过
2. [ ] 内容完整性自检通过
3. [ ] 相关资产引用正确
4. [ ] 元数据完整准确

### 提交内容

- [ ] 资产文件
- [ ] 更新日志
- [ ] 测试用例（如需要）
- [ ] 更新文档
- [ ] 交付物完整率 ≥95%

### 评审配合

- [ ] 提供清晰的变更说明
- [ ] 准备评审答疑
- [ ] 及时响应反馈

## 相关资产

- [naming-conventions.md](../standards/naming-conventions.md)
- [lifecycle.md](../standards/lifecycle.md)
- [harness-engineering.md](../harness-engineering.md)
- [output-quality-rubric.md](../standards/output-quality-rubric.md)
- [asset-model.md](../standards/asset-model.md)
