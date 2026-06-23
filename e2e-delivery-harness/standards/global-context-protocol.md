---
name: global-context-protocol
description: "Global Context 自动更新协议，定义每阶段必须更新的具体字段、上下文快照机制和回滚恢复策略"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'context', 'state-management', 'handoff']
---

# Global Context 自动更新协议

## 概述

本文件定义了 E2E Delivery Harness 的 **Global Context 自动更新协议**。Global Context 是贯穿整个交付生命周期的共享状态存储器，每个核心阶段完成后必须更新特定字段以确保下游 Agent 获得完整的上下文信息。

## Global Context 数据结构

```yaml
global_context:
  # === 项目元数据 ===
  project:
    name: "string"           # 项目名称
    code: "string"           # 项目代号
    version: "string"        # 当前版本
    stage: "string"          # 当前 Pipeline 阶段 ID
    status: "init|in_progress|paused|completed|blocked"
    
  # === 团队信息 ===
  team:
    product_owner: "string"
    tech_lead: "string"
    members: ["string"]
    on_call: "string"
    
  # === 时间线 ===
  timeline:
    started_at: "ISO8601"
    updated_at: "ISO8601"
    milestones:
      - id: "MS-001"
        name: "string"
        date: "ISO8601"
        status: "pending|achieved|delayed"
        
  # === 技术栈 ===
  tech_stack:
    languages: ["string"]
    frameworks: ["string"]
    databases: ["string"]
    infrastructure: ["string"]
    constraints: ["string"]
    
  # === 当前阶段状态 ===
  status:
    risk_level: "low|medium|high|critical"
    blocking_issues: ["string"]
    quality_score: 0-100
    completion_percentage: 0-100
    
  # === 最近交接记录 ===
  last_handover:
    handover_id: "HO-{ISO8601}-{seq}"
    from_stage: "string"
    to_stage: "string"
    timestamp: "ISO8601"
    
  # === 环境信息 ===
  environments:
    production:
      url: "string"
      version: "string"
      health: "healthy|degraded|down"
    staging:
      url: "string"
      version: "string"
      
  # === 上下文快照 ===
  snapshots: []
```

## 每阶段必更新字段

### Stage 1: analyze-requirement → 更新字段

```yaml
required_updates:
  project.stage: "analyze-requirement"
  project.status: "in_progress → completed"
  timeline.updated_at: "{ISO8601}"
  status.risk_level: "基于需求不确定性评估"
  status.quality_score: "{KPI综合评分}"
  last_handover:
    handover_id: "HO-{ISO8601}-{seq}"
    from_stage: "analyze-requirement"
    to_stage: "design-system"
  
  optional_updates:
    tech_stack.constraints: "需求中识别的技术约束"
    timeline.milestones: "新增需求阶段里程碑"
```

### Stage 2: design-system → 更新字段

```yaml
required_updates:
  project.stage: "design-system"
  project.status: "completed"
  timeline.updated_at: "{ISO8601}"
  tech_stack.languages: "{确定的技术栈}"
  tech_stack.frameworks: "{确定的框架}"
  tech_stack.databases: "{确定的数据库}"
  status.risk_level: "基于技术风险评估"
  status.quality_score: "{KPI综合评分}"
  last_handover:
    from_stage: "design-system"
    to_stage: "decompose-task"
    
  optional_updates:
    tech_stack.infrastructure: "{确定的基础设施组件}"
    environments.staging.url: "{如已搭建预发环境}"
```

### Stage 3: decompose-task → 更新字段

```yaml
required_updates:
  project.stage: "decompose-task"
  project.status: "completed"
  timeline.updated_at: "{ISO8601}"
  timeline.milestones: "迭代里程碑更新"
  status.quality_score: "{KPI综合评分}"
  last_handover:
    from_stage: "decompose-task"
    to_stage: "implement-feature"
```

### Stage 4: implement-feature → 更新字段

```yaml
required_updates:
  project.stage: "implement-feature"
  project.status: "completed"
  project.version: "{语义化版本号增量}"
  timeline.updated_at: "{ISO8601}"
  status.quality_score: "{KPI综合评分}"
  status.completion_percentage: "基于已完成任务/总任务"
  last_handover:
    from_stage: "implement-feature"
    to_stage: "verify-test"
    
  optional_updates:
    status.blocking_issues: "开发中发现的阻塞问题"
```

### Stage 5: verify-test → 更新字段

```yaml
required_updates:
  project.stage: "verify-test"
  project.status: "completed"
  timeline.updated_at: "{ISO8601}"
  status.quality_score: "{KPI综合评分}"
  status.risk_level: "基于缺陷严重程度分布"
  last_handover:
    from_stage: "verify-test"
    to_stage: "deploy-release"  # or "implement-feature" if failed
    
  optional_updates:
    status.blocking_issues: "P0/P1 阻塞缺陷列表"
```

### Stage 6: deploy-release → 更新字段

```yaml
required_updates:
  project.stage: "deploy-release"
  project.status: "completed"
  timeline.updated_at: "{ISO8601}"
  environments.production:
    url: "{生产环境URL}"
    version: "{已部署版本}"
    health: "healthy"
  status.quality_score: "{KPI综合评分}"
  last_handover:
    from_stage: "deploy-release"
    to_stage: "monitor-operate"
    
  optional_updates:
    environments.staging.version: "{同步更新预发版本}"
```

### Stage 7: monitor-operate → 更新字段

```yaml
required_updates:
  project.stage: "monitor-operate"
  project.status: "completed → in_progress"  # 运维是持续过程
  timeline.updated_at: "{ISO8601}"
  environments.production.health: "healthy|degraded|down"
  status.risk_level: "基于生产监控数据"
  status.quality_score: "{SLO达成率}"
  
  optional_updates:
    last_handover:
      from_stage: "monitor-operate"
      to_stage: "analyze-requirement"  # 反馈循环
```

## 上下文快照机制

### 快照触发条件

```yaml
snapshot_triggers:
  on_stage_completion: true       # 每阶段完成时自动快照
  on_handover: true               # 每次交接时快照
  on_error_escalation: true       # 错误升级时保存现场
  on_manual_request: true         # 支持手动触发
  max_snapshots: 20               # 保留最近20个快照
```

### 快照数据结构

```yaml
snapshot:
  id: "SNAP-{ISO8601}-{seq}"
  timestamp: "ISO8601"
  trigger: "stage_completion|handover|error|manual"
  stage: "string"
  context_hash: "SHA256"
  summary:
    quality_score: 0-100
    open_issues: {count}
    completed_artifacts: ["string"]
  full_context: "{完整的 Global Context YAML}"
```

## 回滚恢复策略

### 阶段级回滚

```yaml
stage_rollback:
  trigger: "阶段准出检查未通过"
  process:
    1. "加载上一阶段的 context_snapshot"
    2. "将 project.stage 回退到上一阶段"
    3. "恢复 timeline.milestones 到快照状态"
    4. "通知上游 Agent 重新执行"
    5. "记录回滚原因到 status.blocking_issues"
```

### 上下文冲突解决

```yaml
conflict_resolution:
  concurrent_update:
    strategy: "Last-Write-Wins with merge"
    merge_rules:
      - "数组字段: 合并去重"
      - "对象字段: 递归合并"
      - "标量字段: 保留时间戳较新的值"
      
  stale_context:
    detection: "比较 handover_id 链"
    action: "请求上游 Agent 重新生成 Handover"
```

## 相关资产

- [contexts/global-context.md](../contexts/global-context.md) - Global Context 模板
- [contexts/unified-handover-template.md](../contexts/unified-handover-template.md) - 统一交接模板
- [workflows/e2e-delivery.pipeline.md](../workflows/e2e-delivery.pipeline.md) - 主交付流水线
- [cross-pipeline-protocol.md](cross-pipeline-protocol.md) - 跨流水线协议
