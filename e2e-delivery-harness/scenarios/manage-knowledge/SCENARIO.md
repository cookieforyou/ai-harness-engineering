---
name: manage-knowledge
description: "知识管理场景，建立和维护团队知识库，确保知识有效积累和共享"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['workflow', 'process']
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

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 范围确认 | 执行启动前 | 继续 / 缩小范围 / 升级 | 与上游 Handover 一致 | 执行记录 |
| DC-002 | 质量门禁 | 产出验证前 | 修复后继续 / 记录 open_issues | Scenario KPI ≥70 | 验证报告 |
| DC-003 | 交接准出 | 阶段完成前 | 完成交接 / 部分交接 / 阻塞 | Handover 必填字段齐全 | Handover YAML |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```

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

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "manage-knowledge"
    to_stage: "monitor-operate"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "{{artifact_name}}"
        path: "{{file_path}}"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-XXX"
      description: "{{决策描述}}"
      rationale: "{{决策理由}}"
      alternatives_considered: ["选项1", "选项2"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{{问题描述}}"
        
  risks:
    - id: "RISK-XXX"
      description: "{{风险描述}}"
      probability: "low/medium/high"
      impact: "low/medium/high"
      mitigation: "{{缓解措施}}"
      
  recommendations:
    - "{{建议1}}"
    - "{{建议2}}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{actual_value}}
        target: {{target_value}}
        status: "pass/fail"
```
