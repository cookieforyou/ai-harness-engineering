---
name: manage-change
description: "变更管理执行指南，用于处理需求变更请求"
applyTo: "scenarios/manage-change/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
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
>
> 变更管理是 E2E 交付生命周期中的关键管控环节。通过规范的变更评估、审批、实施和验证流程，确保所有变更安全可控，最小化变更对业务的负面影响，同时保持团队的交付效率。

## Technical Specifications

> Detailed technical requirements and implementation guidelines for manage-change.

### Required Tools

| 工具类别 | 推荐工具 | 用途 |
|----------|----------|------|
| 变更管理系统 | Jira/ServiceNow/ChangeSnap | 变更记录、审批流转 |
| 沟通协作 | Slack/钉钉/飞书 | 变更通知和审批提醒 |
| CI/CD 平台 | Jenkins/GitLab CI/ArgoCD | 变更自动化部署 |
| 监控系统 | Prometheus/Datadog/Grafana | 变更后监控验证 |
| 文档平台 | Confluence/Notion | 变更文档存储 |
| 配置管理 | Ansible/Terraform | 基础设施变更管理 |

### Environment Requirements

- 变更管理系统应支持自定义审批流和时间窗口管理
- CI/CD 管道应支持灰度发布和快速回滚
- 监控系统应覆盖变更相关的所有服务和指标
- 变更记录需要长期归档以满足审计要求

### Configuration Parameters

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `max_active_changes_per_service` | number | 3 | 单服务最大同时变更数 |
| `approval_timeout_hours` | number | 24 | 审批超时时间 |
| `observation_period_minutes` | number | 30 | 变更后观察期 |
| `standard_change_auto_approve` | boolean | true | 标准变更自动批准 |
| `cab_meeting_frequency` | string | "weekly" | CAB 会议频率 |
| `emergency_change_compliance_window` | number | 24 | 紧急变更补录时限(小时) |

## 变更请求模板

### 变更单基本信息

```yaml
change_request:
  header:
    change_id: "CHG-{{YYYYMMDD}}-{{XXX}}"
    title: "{{change_title}}"
    requester: "{{name}}"
    department: "{{department}}"
    created_at: "{{ISO8601}}"
    priority: "P0/P1/P2/P3"
    
  change_details:
    description: "变更内容详细描述"
    reason: "变更原因和背景"
    scope: "变更范围（系统/服务/模块）"
    
    change_type: "standard/normal/emergency"
    risk_level: "low/medium/high/critical"
    
    affected_services:
      - "{{service_name}}"
      - "{{service_name}}"
      
    affected_users: "internal/external/all"
    business_impact: "{{impact_description}}"
    
  timeline:
    requested_window: "{{start_time}} - {{end_time}}"
    expected_duration: "{{duration}}"
    
  rollback_plan:
    rollback_type: "auto/manual"
    rollback_steps:
      - "{{step_description}}"
    rollback_duration: "{{duration}}"
    rollback_verification: "{{verification_method}}"
    
  approval_chain:
    current_step: "{{step_name}}"
    approvers:
      - role: "{{role}}"
        name: "{{name}}"
        status: "pending/approved/rejected"
        commented_at: "{{ISO8601}}"
```

## 影响分析框架

### 多维度影响分析

| 分析维度 | 评估要点 | 判定标准 | 数据来源 |
|----------|----------|----------|----------|
| **功能影响** | 变更涉及的功能点、对上下游的影响 | 功能完整性检查 | 需求文档、接口文档 |
| **技术影响** | 代码变更量、API 变更、数据模型变更 | 代码审查、静态分析 | Git 变更、Schema Diff |
| **性能影响** | 响应时间、吞吐量、资源消耗变化 | 性能基准测试 | 压测报告 |
| **安全影响** | 权限变更、数据暴露面、认证机制 | 安全审查 | 安全扫描报告 |
| **兼容性影响** | API 向前/向后兼容、数据格式兼容 | 兼容性测试 | 集成测试报告 |
| **运维影响** | 监控告警、日志、部署方式变化 | 运维 checklist | 运维手册 |

### 影响评分矩阵

```yaml
impact_scoring:
  功能影响:
    - score=1: "仅影响内部辅助功能"
    - score=2: "影响非核心功能"
    - score=3: "影响核心功能"
    - score=4: "影响跨系统核心流程"
    - score=5: "全站功能受影响"
    
  技术影响:
    - score=1: "配置文件变更，无代码变更"
    - score=2: "少量代码变更，无 Schema 变更"
    - score=3: "中等代码变更，向后兼容 API"
    - score=4: "大量代码变更，不兼容 API 变更"
    - score=5: "涉及数据库迁移、架构重构"
    
  回滚风险:
    - score=1: "一键回滚，< 5 分钟完成"
    - score=2: "简单回滚，< 15 分钟"
    - score=3: "需要手动操作回滚"
    - score=4: "回滚涉及数据迁移"
    - score=5: "回滚复杂，> 1 小时或不可回滚"
```

## 审批链配置指南

### 审批链层级

```
Level 1 - 技术负责人审批
  适用范围: 低风险变更
  审批要求: 
    - 变更技术方案合理
    - 影响分析完整
    - 回滚方案可行
    
Level 2 - 变更经理审批
  适用范围: 中风险变更
  审批要求（在 L1 基础上）:
    - 风险等级判定合理
    - 变更窗口合适
    - 干系人已通知
    
Level 3 - CAB 评审
  适用范围: 高风险变更
  审批要求（在 L2 基础上）:
    - CAB 投票通过
    - 安全团队审核通过
    - 业务代表确认
    
Level 4 - CTO/VP 审批
  适用范围: 严重风险变更
  审批要求（在 L3 基础上）:
    - 管理层评估业务影响
    - 跨团队资源协调确认
```

### 审批时效要求

| 变更优先级 | 审批 SLA | 审批人 |
|------------|----------|--------|
| P0 - 紧急 | < 30 分钟 | 紧急审批人 |
| P1 - 高 | < 4 小时 | 变更经理 |
| P2 - 中 | < 24 小时 | 技术负责人 |
| P3 - 低 | < 72 小时 | 审批链流转 |

## 变更日历管理

### 变更日历要素

```yaml
change_calendar:
  view: "周视图 / 月视图"
  
  event_attributes:
    - "变更 ID"
    - "变更标题"
    - "变更类型"
    - "风险等级"
    - "计划窗口"
    - "影响的服务"
    - "实施人"
    - "状态（计划中/审批中/已批准/实施中/已完成/已回滚）"
    
  conflict_detection:
    - "同一服务在同一窗口内多个变更"
    - "同一基础设施组件的并发变更"
    - "变更窗口资源争用"
    
  freeze_periods:
    - name: "业务高峰冻结"
      period: "大促期间"
      rules: "仅允许紧急变更"
    - name: "周末冻结"
      period: "周五 18:00 - 周一 08:00"
      rules: "仅允许紧急变更和预授权的窗口变更"
    - name: "版本冻结"
      period: "发布前 24 小时"
      rules: "不允许新的变更进入"
```

### 变更冲突解决流程

```
1. 发现冲突: 系统自动检测或变更经理人工识别
2. 冲突分析: 评估冲突变更的影响范围和优先级
3. 协商调整: 与相关变更发起人协商调整窗口
4. 升级决策: 无法协商时升级到变更经理决策
5. 窗口分配: 优先级高、影响大的变更优先获得窗口
6. 记录通知: 更新变更日历并通知所有干系人
```

## 变更后验证步骤

### 验证清单

```yaml
post_change_validation:
  功能验证:
    - [ ] "核心业务功能正常运行"
    - [ ] "本次变更涉及的特定功能验证通过"
    - [ ] "主要上下游接口调用正常"
    
  性能验证:
    - [ ] "响应时间在预期范围内"
    - [ ] "吞吐量正常"
    - [ ] "资源使用率（CPU/内存/磁盘）在正常范围"
    - [ ] "错误率无异常升高"
    
  监控验证:
    - [ ] "关键指标都在正常范围"
    - [ ] "无新告警产生"
    - [ ] "日志无异常错误"
    - [ ] "用户无投诉反馈"
    
  回滚准备:
    - [ ] 回滚方案就绪，可在 15 分钟内执行
    - [ ] 回滚条件已明确定义
    - [ ] 回滚责任人已确认
    
  文档更新:
    - [ ] "系统架构图已更新"
    - [ ] "运维手册已更新"
    - [ ] "API 文档已更新"
    - [ ] "配置文档已更新"
```

### 验证频率

| 阶段 | 验证内容 | 频率 |
|------|----------|------|
| 实施后即时 | 核心功能 + 关键指标 | 实施完成后立即 |
| 短期观察 | 全面功能 + 性能指标 | 实施后 30 分钟 |
| 中期观察 | 系统稳定性 + 异常 | 实施后 4 小时 |
| 长期验证 | 业务效果 + 用户反馈 | 实施后 24 小时 - 1 周 |

## Error Handling

> Common error scenarios and resolution strategies for manage-change.

### Error Category 1: 变更导致意外服务中断
**Symptom**: Change causes unexpected service disruption
**Cause**: 风险评估不充分，未识别关键依赖关系；回滚方案未验证
**Resolution**: 
1. 立即评估中断影响范围
2. 触发回滚流程，执行回滚方案
3. 通知相关干系人当前状态
4. 回滚完成后进行全面验证
5. 启动事后复盘，分析未识别风险的原因

### Error Category 2: 审批流程延误紧急变更
**Symptom**: Approval process delays critical changes
**Cause**: 审批链过长或审批人不可用；紧急通道不畅通
**Resolution**: 
1. 识别审批阻塞环节
2. 启用紧急变更通道（如有）
3. 联系审批链备份审批人
4. 升级到变更经理介入协调
5. 事后优化审批链配置，增加备份审批人

### Error Category 3: 变更窗口冲突无法协调
**Symptom**: Multiple changes compete for the same window and same service
**Cause**: 变更日历管理缺失或冲突检测机制不完善
**Resolution**:
1. 评估各变更的优先级和业务影响
2. 与相关变更发起人协商错开窗口
3. 如无法协商，按优先级排序
4. 必要时升级到管理层决策
5. 优化变更日历管理流程，增加自动化冲突检测

## Quality Standards

> Acceptance criteria and quality gates for manage-change deliverables.

| Standard | Criteria | Verification Method | Owner |
|----------|----------|---------------------|-------|
| CHANGE-SUCCESS | Change success rate is 95% or higher | Automated check from change tracking system | Change Manager |
| APPROVAL-SLA | Approval SLA is within 24 hours | Automated SLA tracking | Change Manager |
| INCIDENT-CORRELATION | Change-correlated incident rate is below 2% | Automated incident correlation analysis | SRE Team |
| ROLLBACK-READINESS | 100% of changes have verified rollback plans | Manual audit of 10% sample | QA Lead |
| EMERGENCY-COMPLIANCE | 100% of emergency changes have post-completion records | Automated compliance check | Audit Team |

## References

- [harness-engineering.md](../standards/harness-engineering.md) — 工程标准
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md) — 输出验证清单
- [regression-checklist.md](../evaluations/regression-checklist.md) — 回归检查清单
- [change-management.md](../standards/change-management.md) — 变更管理标准
- [change-request-template.md](../templates/change-request.template.md) — 变更请求模板
