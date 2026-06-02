---
name: manage-change
description: "变更管理执行指南，用于处理需求变更请求"
applyTo: "scenarios/manage-change/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Change Management Instruction

## Objective

有效管理需求变更，确保变更可控、可追溯、最小化对项目的影响。

## Prerequisites

1. 已有需求规格说明书
2. 有变更发起人
3. 有项目干系人

## Process Steps

### Step 1: 接收变更请求

1. 记录变更基本信息
2. 确认变更来源
3. 分配变更编号
4. 通知相关干系人

### Step 2: 分析变更内容

1. 理解变更目的
2. 分析变更范围
3. 识别变更类型
4. 评估紧迫程度

### Step 3: 评估影响

1. 功能影响分析
2. 技术影响分析
3. 测试影响分析
4. 文档影响分析
5. 资源需求评估

### Step 4: 制定决策

1. 权衡变更利弊
2. 给出决策建议
3. 说明决策理由
4. 准备评审材料

### Step 5: 评审变更

1. 组织评审会议
2. 邀请相关干系人
3. 讨论决策建议
4. 达成变更决策

### Step 6: 实施变更

1. 更新需求文档
2. 调整设计和代码
3. 更新测试
4. 更新文档
5. 通知相关方

## Quality Gates

### 准入检查

- [ ] 变更描述清晰
- [ ] 变更原因明确
- [ ] 相关干系人已知

### 准出检查

- [ ] 影响分析完整
- [ ] 决策已达成
- [ ] 实施计划已制定

## Handoff Criteria

交接给下一阶段前：

- [ ] 变更评估报告已完成
- [ ] 变更决策已确认
- [ ] 实施计划已制定
- [ ] 相关文档已更新


## Overview

> High-level description of the manage-change execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the manage-change scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for manage-change.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for manage-change execution.

1. **Practice 1**: Assess change impact on systems, users, and operations
2. **Practice 2**: Obtain required approvals before implementation
3. **Practice 3**: Validate changes post-deployment with defined criteria


## Error Handling

> Common error scenarios and resolution strategies for manage-change.

### Error Category 1
**Symptom**: Change causes unexpected service disruption
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Approval process delays critical changes
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for manage-change deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Change success rate is 95% or higher | Automated check |
| Standard 2 | Approval SLA is within 24 hours | Automated check |
| Standard 3 | Change-correlated incident rate is below 2% | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
