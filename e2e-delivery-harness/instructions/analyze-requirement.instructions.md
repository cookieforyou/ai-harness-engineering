---
name: analyze-requirement
description: "Technical instructions for requirement analysis execution"
type: instruction
version: "1.1.0"
stage: "analyze-requirement"
---

# Requirement Analysis Instructions

## Purpose

本文档定义了需求分析阶段的标准操作流程、质量检查标准和工作产出规范。需求分析是将原始业务需求转换为结构化、可验证的需求规格说明书的系统性过程。

## Investigation Flow

### 流程概览

```
需求收集 → 干系人分析 → 业务建模 → 需求规格化 → 评审确认
```

### 步骤 1：需求收集

**目的**：从多渠道收集原始需求，建立完整的需求池

**输入**：
- 业务方的原始需求描述
- 相关的业务文档和背景材料
- 现有系统的问题反馈

**操作**：

1. **渠道识别**
   - 识别需求来源渠道（会议、邮件、工单、访谈等）
   - 记录每个需求的来源和时间

2. **初步整理**
   - 去重合并相似的需求
   - 按业务领域分类整理
   - 标注需求优先级（高/中/低）

3. **缺失识别**
   - 识别信息不完整的需求
   - 列出需要进一步澄清的问题

**输出**：初步整理的需求清单

### 步骤 2：干系人分析

**目的**：识别所有相关干系人，理解其诉求和期望

**输入**：
- 项目背景和组织架构
- 已识别的干系人名单
- 利益相关程度

**操作**：

1. **干系人识别**
   - 列出所有利益相关方
   - 分类：决策者、使用者、影响者、监管者

2. **诉求分析**
   - 访谈关键干系人
   - 整理各干系人的核心诉求
   - 识别诉求间的冲突点

3. **优先级确定**
   - 基于干系人影响力确定优先级
   - 明确关键干系人的关键诉求

**输出**：干系人分析报告

### 步骤 3：业务建模

**目的**：构建业务流程和用例模型，可视化业务逻辑

**输入**：
- 业务需求描述
- 现有业务流程（如有）
- 业务规则和约束

**操作**：

1. **流程识别**
   - 识别主要业务流程
   - 识别业务流程的起点和终点
   - 识别流程中的角色和系统

2. **流程描述**
   - 使用流程图描述业务流转
   - 标注关键决策点
   - 说明异常处理流程

3. **用例建模**
   - 识别系统用例
   - 描述用例的前置条件和后置条件
   - 编写主要流程和扩展流程

**输出**：业务流程图和用例模型

### 步骤 4：需求规格化

**目的**：将需求转换为结构化、可验证的规格说明

**输入**：
- 初步需求清单
- 干系人分析结果
- 业务模型

**操作**：

1. **功能需求定义**
   - 使用 "As a... I want... so that..." 格式描述
   - 明确每个需求的验收标准
   - 标注需求优先级和依赖关系

2. **非功能需求定义**
   - 性能需求（响应时间、吞吐量）
   - 安全需求（认证、授权、审计）
   - 可用性需求（可用率、恢复时间）
   - 可维护性需求（监控、日志、配置）

3. **约束条件整理**
   - 技术约束（技术栈、兼容性）
   - 时间约束（交付节点）
   - 资源约束（预算、人力）

**输出**：需求规格说明书

### 步骤 5：评审确认

**目的**：与干系人评审需求，确保理解一致

**输入**：
- 需求规格说明书（草稿）
- 相关业务和技术人员

**操作**：

1. **评审准备**
   - 提前发送评审材料
   - 准备评审议程
   - 邀请关键干系人

2. **评审执行**
   - 逐项讲解需求
   - 收集反馈意见
   - 记录修改建议

3. **确认签字**
   - 根据评审意见修订
   - 获得干系人签字确认
   - 锁定需求基线

**输出**：需求规格说明书（确认版）

## What To Check

### 必检项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 业务目标清晰 | 每个需求都关联业务目标 | 逐条核对 | 100% 需求有业务目标 |
| 干系人覆盖 | 关键干系人都有输入 | 干系人核对表 | 100% 关键干系人已覆盖 |
| 验收标准明确 | 每个功能需求有验收标准 | 逐条检查 | 100% 功能需求有验收标准 |
| 需求无遗漏 | 核心业务流程都有覆盖 | 用例核对表 | 覆盖率 > 95% |
| 需求无冲突 | 需求之间无逻辑冲突 | 交叉检查 | 无发现冲突 |
| 非功能需求完整 | 包含性能、安全等非功能需求 | 检查清单 | 包含所有必需类型 |

### 建议检查项

| 检查项 | 标准 | 检查方法 | 通过条件 |
|--------|------|----------|----------|
| 需求可测试 | 每个需求可转化为测试用例 | 测试映射 | 可转化率 > 90% |
| 优先级合理 | 优先级与业务价值一致 | 干系人确认 | 100% 高优先级需求已确认 |
| 依赖关系明确 | 需求间的依赖已标注 | 依赖图检查 | 所有依赖已标注 |

## Quality Criteria

### 质量维度

| 维度 | 要求 | 权重 |
|------|------|------|
| 完整性 | 产出包含所有必需项 | 30% |
| 准确性 | 业务理解正确 | 30% |
| 可追溯性 | 需求与目标可追溯 | 20% |
| 可验证性 | 验收标准明确可测 | 20% |

### 评分标准

| 等级 | 分值 | 描述 |
|------|------|------|
| 卓越 | 5 | 需求完整清晰，干系人高度认可 |
| 优秀 | 4 | 需求基本完整，有小幅改进空间 |
| 良好 | 3 | 满足核心要求，有优化空间 |
| 合格 | 2 | 基本可用，需补充不完整项 |
| 不合格 | 1 | 不满足基本要求 |

## Output Specification

### 产出清单

| 产出 | 格式 | 必填 | 描述 |
|------|------|------|------|
| 需求规格说明书 | .md | 是 | 结构化的需求文档 |
| 干系人分析报告 | .md | 是 | 干系人识别和诉求 |
| 业务流程图 | .md/.png | 是 | 主要业务流程 |
| 用例模型 | .md | 是 | 系统用例定义 |

### 产出模板

```markdown
# 需求规格说明书

## 1. 文档信息
- 项目名称：
- 版本：
- 日期：
- 作者：

## 2. 业务背景与目标
...

## 3. 干系人分析
...

## 4. 功能需求
...

## 5. 非功能需求
...

## 6. 用例模型
...

## 7. 验收标准
...

## 8. 假设与约束
...

## 9. 未解决问题
...
```


## Overview

> High-level description of the analyze-requirement execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the analyze-requirement scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for analyze-requirement.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for analyze-requirement execution.

1. **Practice 1**: Elicit requirements through structured interviews and workshops
2. **Practice 2**: Document functional and non-functional requirements with acceptance criteria
3. **Practice 3**: Validate requirements with stakeholders before formal sign-off


## Error Handling

> Common error scenarios and resolution strategies for analyze-requirement.

### Error Category 1
**Symptom**: Requirements are ambiguous or conflicting
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Stakeholders provide incomplete or inconsistent input
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for analyze-requirement deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | All requirements have unambiguous acceptance criteria | Automated check |
| Standard 2 | Stakeholder sign-off achieved for scope baseline | Automated check |
| Standard 3 | Traceability matrix covers all business objectives | Automated check |
