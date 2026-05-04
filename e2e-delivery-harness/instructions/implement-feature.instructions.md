---
type: "instruction"
stage: "implement-feature"
version: "1.1.0"
applyTo: "**/*.{ts,js,py,java}"
phase: development
order: 4
---

# Development Implementation Instructions

## Purpose

本文档定义了开发实现阶段的标准操作流程、质量检查标准和工作产出规范。开发实现是按照任务清单完成代码编写和功能交付的过程。

## Investigation Flow

### 流程概览

```
任务理解 → 技术方案 → 编码实现 → 单元测试 → 代码审查 → 文档更新
```

### 步骤 1：任务理解

**目的**：深入理解任务需求和验收标准

**输入**：
- 任务卡片
- 相关的架构设计
- 接口定义文档

**操作**：

1. **需求确认**
   - 理解业务需求和背景
   - 确认验收标准
   - 识别依赖和边界

2. **技术准备**
   - 查阅相关代码和文档
   - 了解现有实现方式
   - 准备必要的技术资料

3. **疑问澄清**
   - 有疑问及时沟通
   - 不清楚的地方主动确认
   - 记录关键决策

**输出**：任务理解备忘录

### 步骤 2：技术方案

**目的**：制定具体的技术实现方案

**输入**：
- 任务理解备忘录
- 编码规范
- 相关技术文档

**操作**：

1. **方案设计**
   - 设计类/函数结构
   - 定义接口和数据结构
   - 考虑异常处理

2. **方案评审（如需要）**
   - 复杂任务进行方案评审
   - 获得评审通过后再实现
   - 记录评审结论

3. **任务估算**
   - 确认工作量估算
   - 制定开发计划
   - 识别潜在风险

**输出**：技术实现方案

### 步骤 3：编码实现

**目的**：按照规范完成代码编写

**输入**：
- 技术实现方案
- 代码规范
- 编码工具

**操作**：

1. **代码编写**
   - 遵循编码规范
   - 保持代码风格一致
   - 添加必要的注释

2. **代码组织**
   - 合理的目录结构
   - 清晰的命名规范
   - 适当的模块划分

3. **质量保证**
   - 避免重复代码
   - 考虑可维护性
   - 遵循 SOLID 原则

**输出**：源代码文件

### 步骤 4：单元测试

**目的**：编写并执行单元测试，确保代码质量

**输入**：
- 源代码文件
- 测试规范
- 测试框架

**操作**：

1. **测试设计**
   - 设计测试用例
   - 覆盖正常路径和异常路径
   - 考虑边界条件

2. **测试编写**
   - 遵循测试规范
   - 测试用例命名清晰
   - 适当的断言

3. **测试执行**
   - 执行单元测试
   - 确保测试通过
   - 检查代码覆盖率

**输出**：单元测试代码和测试报告

### 步骤 5：代码审查

**目的**：进行自检并准备代码审查

**输入**：
- 源代码
- 单元测试
- 代码审查清单

**操作**：

1. **自检**
   - 对照规范自查
   - 检查代码逻辑
   - 确保测试覆盖

2. **提交审查**
   - 创建 Pull Request
   - 填写审查信息
   - 标注重点关注

3. **审查响应**
   - 及时响应审查意见
   - 修复发现的问题
   - 获得审查通过

**输出**：审查通过的代码

### 步骤 6：文档更新

**目的**：更新必要的代码和接口文档

**输入**：
- 代码变更
- 相关文档

**操作**：

1. **接口文档**
   - 更新 API 文档
   - 更新接口说明
   - 添加使用示例

2. **代码注释**
   - 添加必要的注释
   - 更新复杂逻辑说明
   - 保持注释更新

3. **变更记录**
   - 记录变更内容
   - 更新版本号
   - 记录迁移说明

**输出**：更新后的文档

## What To Check

### 必检项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 代码规范 | 遵循团队编码规范 | 规范检查工具 | 无规范违规 |
| 功能实现 | 实现所有计划功能 | 功能对比 | 100% 功能实现 |
| 测试覆盖 | 核心逻辑有测试 | 覆盖率报告 | 覆盖率 > 70% |
| 代码审查 | 通过代码审查 | 审查记录 | 审查通过 |
| 文档同步 | 代码变更有文档 | 文档检查 | 关键文档已更新 |

### 建议检查项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 性能考虑 | 考虑性能影响 | 评审检查 | 无明显性能问题 |
| 安全考虑 | 避免安全漏洞 | 安全扫描 | 无高危漏洞 |
| 错误处理 | 异常情况有处理 | 代码检查 | 关键异常已处理 |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 |
|------|------|------|
| 功能正确性 | 实现符合需求 | 35% |
| 代码质量 | 规范、可维护 | 25% |
| 测试覆盖 | 核心逻辑覆盖 | 20% |
| 文档完整 | 文档同步更新 | 20% |

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 |
|------|------|------|------|
| 源代码 | 源文件 | 是 | 实现的代码 |
| 单元测试 | 测试文件 | 是 | 测试代码 |
| 测试报告 | .md | 是 | 测试结果 |
| 变更记录 | .md | 是 | 代码变更说明 |


## Overview

> High-level description of the implement-feature execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the implement-feature scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for implement-feature.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for implement-feature execution.

1. **Practice 1**: [Description]
2. **Practice 2**: [Description]
3. **Practice 3**: [Description]


## Error Handling

> Common error scenarios and resolution strategies for implement-feature.

### Error Category 1
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for implement-feature deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | [Description] | [How to verify] |
| Standard 2 | [Description] | [How to verify] |
| Standard 3 | [Description] | [How to verify] |
