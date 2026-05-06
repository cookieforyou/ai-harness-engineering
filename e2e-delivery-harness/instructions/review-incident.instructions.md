---
name: review-incident
description: 故障复盘执行指南，用于执行故障复盘
type: instruction
version: "1.1.0"
stage: monitoring
---

# Incident Review Instruction

## Objective

对已解决的故障进行复盘分析，找出根本原因，制定改进措施，防止同类故障再次发生。

## Prerequisites

1. 故障已完全恢复
2. 相关日志可用
3. 关键人员参与

## Process Steps

### Step 1: 收集信息

1. 收集故障报告
2. 收集监控数据
3. 收集日志
4. 收集沟通记录

### Step 2: 重构时间线

1. 按时间顺序排列事件
2. 标注关键节点
3. 识别触发事件
4. 识别恢复动作

### Step 3: 分析原因

1. 分析直接原因
2. 使用 5 Why 分析
3. 识别根本原因
4. 区分内因外因

### Step 4: 评估影响

1. 用户影响
2. 业务影响
3. 财务影响
4. 声誉影响

### Step 5: 制定改进措施

1. 预防措施
2. 检测措施
3. 响应措施
4. 持续改进

### Step 6: 编写报告

1. 整理复盘内容
2. 分配行动项
3. 确定责任人
4. 归档报告

## Quality Gates

### 准入检查

- [ ] 故障已恢复
- [ ] 数据已收集
- [ ] 人员已确认

### 准出检查

- [ ] 根本原因已确定
- [ ] 改进措施已制定
- [ ] 责任人已确认

## Handoff Criteria

交接给运维前：

- [ ] 复盘报告已完成
- [ ] 行动项已分配
- [ ] 跟踪计划已制定


## Overview

> High-level description of the review-incident execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the review-incident scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for review-incident.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for review-incident execution.

1. **Practice 1**: Conduct blameless postmortems focused on system improvements
2. **Practice 2**: Identify root cause using structured methods like 5 Whys
3. **Practice 3**: Track action items to completion with defined owners


## Error Handling

> Common error scenarios and resolution strategies for review-incident.

### Error Category 1
**Symptom**: Postmortem does not identify actionable improvements
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Similar incidents recur without corrective action
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for review-incident deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | All P0/P1 incidents have completed postmortems | Automated check |
| Standard 2 | Action item closure rate is 90% or higher | Automated check |
| Standard 3 | Incident recurrence rate is 5% or lower | Automated check |
