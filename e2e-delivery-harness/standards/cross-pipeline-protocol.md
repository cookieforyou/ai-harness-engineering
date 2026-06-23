---
name: cross-pipeline-protocol
description: "主交付 Pipeline A 与故障响应 Pipeline B 之间的切换协议，定义触发条件、上下文保留、恢复机制和交织执行规则"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'pipeline', 'incident', 'context-switching', 'resilience']
---

# 跨流水线集成协议

## 概述

E2E Delivery Harness 有两套流水线：**Pipeline A（主交付）** 和 **Pipeline B（故障响应）**。本协议定义了二者之间的切换规则，确保在故障发生时能无缝从主交付切换到故障响应，并在恢复后平滑切回。

## 双流水线架构

```
Pipeline A (主交付):                    Pipeline B (故障响应):
analyze-requirement                     detect & classify
    ↓                                        ↓
design-system                           respond & mitigate
    ↓                                        ↓
decompose-task                          recover & close
    ↓                                        ↓
implement-feature                       review & improve
    ↓
verify-test
    ↓
deploy-release
    ↓
monitor-operate ←──────── 交织点 ──────→ respond-incident
```

## 切换触发条件

### A → B（主交付 → 故障响应）

```yaml
a_to_b_triggers:
  production_incident:
    description: "生产环境发生 P0/P1 故障"
    detection: "monitor-operate 检测到 SLO 突破或告警触发"
    action: "暂停当前主交付阶段，切换到 respond-incident"
    priority: "P0: 立即切换 | P1: 15分钟内切换"
    
  deployment_failure:
    description: "部署发布失败且回滚后仍需修复"
    detection: "deploy-release 阶段回滚后验证未通过"
    action: "切换到 apply-hotfix 或 implement-feature"
    priority: "P0: 立即切换"
    
  security_breach:
    description: "安全漏洞被利用或数据泄露"
    detection: "audit-security 或 monitor-operate 检测到异常"
    action: "切换到 respond-incident (P0)，并行触发 audit-security"
    priority: "P0: 立即切换"
```

### B → A（故障响应 → 主交付）

```yaml
b_to_a_triggers:
  incident_resolved:
    description: "故障已恢复且验证通过"
    condition: "respond-incident 完成 + apply-hotfix 已验证（如需）"
    action: "恢复到主交付流程，从 monitor-operate 继续"
    
  postmortem_complete:
    description: "复盘完成，改进项已排入 backlog"
    condition: "review-incident 完成"
    action: "恢复主交付，将改进项注入 manage-tech-debt 或 manage-knowledge"
    
  false_alarm:
    description: "告警被确认为误报"
    action: "立即恢复到主交付流程，无上下文损失"
```

## 上下文保留协议

### 切换时上下文保存

```yaml
context_save_on_switch:
  pipeline_a_to_b:
    save_fields:
      - "project.stage"               # 当前阶段（用于恢复）
      - "project.version"             # 当前版本
      - "status.risk_level"           # 风险等级
      - "last_handover"               # 最后交接记录
      - "timeline.milestones"         # 里程碑状态
      - "team.on_call"                # 值班人员
    save_format: "contexts/pipeline-a-suspend-{timestamp}.yaml"
    
  pipeline_b_to_a:
    save_fields:
      - "incident.timeline"           # 事件时间线
      - "incident.root_cause"         # 根因分析
      - "incident.action_items"       # 后续行动项
      - "environments.production.health"  # 生产环境健康状态
    save_format: "contexts/pipeline-b-close-{timestamp}.yaml"
```

### 恢复时上下文合并

```yaml
context_merge_on_resume:
  strategy: "分层合并"
  layers:
    - priority: 1
      source: "pipeline-b-close 快照"
      fields: ["environments.production", "incident.*"]
      reason: "故障响应后的生产状态是最新的"
      
    - priority: 2
      source: "pipeline-a-suspend 快照"
      fields: ["project.stage", "timeline.milestones", "last_handover"]
      reason: "恢复到主交付的挂起点"
      
    - priority: 3
      source: "实时查询"
      fields: ["team.on_call", "status.risk_level"]
      reason: "人员可能已换班，风险需重新评估"
```

## 交织执行规则

### 允许交织的场景

```yaml
interleaving_allowed:
  - pair: [monitor-operate, respond-incident]
    condition: "监控仍持续运行，但事件响应获得更高优先级"
    
  - pair: [deploy-release, apply-hotfix]
    condition: "如热修复部署使用独立流水线，可与常规部署并行"
    
  - pair: [review-incident, manage-knowledge]
    condition: "复盘产生的知识可并行沉淀到知识库"
```

### 禁止交织的场景

```yaml
interleaving_forbidden:
  - pair: [deploy-release, migrate-data]
    reason: "部署和数据迁移不能同时操作生产环境"
    
  - pair: [respond-incident, plan-disaster-recovery]
    reason: "正在处理的故障不应同时启动灾备切换（除非故障升级为灾难）"
```

## 通知协议

```yaml
notification_on_switch:
  a_to_b:
    recipients: ["on_call_engineer", "tech_lead", "product_manager"]
    template: |
      🚨 Pipeline Switch: 主交付 → 故障响应
      触发条件: {trigger}
      暂停阶段: {suspended_stage}
      故障等级: P{severity}
      预计影响: {impact_summary}
      切换到: respond-incident
      
  b_to_a:
    recipients: ["tech_lead", "product_manager", "team_members"]
    template: |
      ✅ Pipeline Restore: 故障响应 → 主交付
      故障状态: 已恢复
      恢复阶段: {resumed_stage}
      复盘结论: {postmortem_summary}
      改进项数量: {action_count}
```

## 相关资产

- [workflows/e2e-delivery.pipeline.md](../workflows/e2e-delivery.pipeline.md)
- [workflows/incident-response.pipeline.md](../workflows/incident-response.pipeline.md)
- [global-context-protocol.md](global-context-protocol.md)
- [scenario-dependency-graph.md](scenario-dependency-graph.md)
- [error-classification.md](error-classification.md)
