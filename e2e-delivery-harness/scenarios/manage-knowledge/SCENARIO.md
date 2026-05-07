---
name: manage-knowledge
description: 知识管理场景，建立和维护团队知识库，确保知识有效积累和共享
type: scenario
version: 1.1.0
trigger: 当需要创建、更新或组织知识时触发
agent: document-project
phase: document-project
tags: null
input: null
output: null
author: AI Harness Engineering Team
stage: governance
---

# Knowledge Management Scenario

## Overview

知识管理是组织智力资产的核心，涉及知识的创建、组织、分享和维护。本场景确保团队知识有效积累、方便获取、持续更新。

## Knowledge Categories

### Category 1: Technical Documentation
| Type | Description | Examples |
|------|-------------|----------|
| Architecture | 系统架构设计 | 架构图、设计文档 |
| Runbooks | 运维操作指南 | 部署手册、故障处理 |
| API Docs | 接口文档 | OpenAPI、SDK 文档 |
| Code Examples | 代码示例 | 最佳实践、模板 |

### Category 2: Process Documentation
| Type | Description | Examples |
|------|-------------|----------|
| Workflows | 工作流程 | 部署流程、审批流程 |
| Guidelines | 开发规范 | 代码规范、安全规范 |
| Checklists | 检查清单 | 发布检查、安全检查 |
| Templates | 文档模板 | 需求模板、设计模板 |

### Category 3: Organizational Knowledge
| Type | Description | Examples |
|------|-------------|----------|
| Onboarding | 新人入职 | 快速入门、团队介绍 |
| Decisions | 决策记录 | ADR、技术决策 |
| Retrospectives | 回顾总结 | 经验教训、改进措施 |
| Glossary | 术语表 | 业务术语、技术术语 |

## Chain of Thought

```
1. 识别知识需求
   ↓
2. 确定知识类型
   ↓
3. 收集相关信息
   ↓
4. 组织知识结构
   ↓
5. 编写/更新内容
   ↓
6. 评审和审核
   ↓
7. 发布和分享
   ↓
8. 持续维护更新
```

## Decision Checkpoints

### Checkpoint 1: 知识识别
- 是否已有相关文档？
- 是否值得文档化？
- 受众是谁？
- 时效性要求？

### Checkpoint 2: 结构设计
- 如何组织？
- 需要什么层级？
- 如何便于搜索？
- 如何维护？

### Checkpoint 3: 内容质量
- 内容准确？
- 表达清晰？
- 示例充分？
- 易于理解？

### Checkpoint 4: 维护机制
- 如何保持更新？
- 何时审核？
- 如何跟踪变更？
- 过期内容处理？


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `KNOWLEDGE-INDEX` | ≥95% | 知识索引率：已分类知识占比 |
| `SEARCH-SUCCESS` | ≥80% | 搜索成功率：用户找到所需信息 |
| `FRESHNESS` | ≥90% | 新鲜度：过去6个月更新的知识占比 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [ ] 知识内容完整准确
- [ ] 结构清晰便于查找
- [ ] 审核通过
- [ ] 发布到知识库
- [ ] 相关方已通知
- [ ] 维护计划已制定

## Related Scenarios

- [document-project](./document-project/SCENARIO.md) - 项目文档
- [review-design](./review-design/SCENARIO.md) - 设计审查
- [review-incident](./review-incident/SCENARIO.md) - 事件复盘
- [monitor-operate](./monitor-operate/SCENARIO.md) - 监控运维


## Purpose

> Define the objectives and scope of the manage-knowledge scenario.
>
> This scenario ensures systematic execution of manage-knowledge activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: Knowledge domains and taxonomy are defined
- [ ] Prerequisite 2: Knowledge platform or repository is provisioned
- [ ] Prerequisite 3: Content owners and reviewers are assigned


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/manage-knowledge/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/manage-knowledge.prompt.md` | Execution prompt |
| Instructions | `instructions/manage-knowledge.instructions.md` | Technical instructions |
| Agent | `agents/manage-knowledge.agent.md` | Responsible agent |
| Skill | `skills/manage-knowledge/SKILL.md` | Domain skill |


## Error Handling

### Error Scenario 1
**Error**: Knowledge articles are created without proper categorization
**Handling**: [Resolution steps]

### Error Scenario 2
**Error**: Outdated content is not identified or archived
**Handling**: [Resolution steps]
