---
name: deploy-release
description: 部署发布场景，负责将软件部署到目标环境并完成发布
type: scenario
category: operations
stage: deployment
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [deployment, release, operations]
---

# Deploy Release - Deployment Scenario

## Purpose

将软件部署到目标环境，执行发布流程，确保部署成功并建立回滚机制。

**核心目标**:
- 安全可靠地将新版本部署到目标环境
- 最小化部署对服务的影响（零停机或最短停机时间）
- 验证部署后系统功能正常
- 建立完善的监控和回滚机制

**成功标准**:
- 部署成功率 ≥99%
- 部署过程零停机或停机时间 <5分钟
- 部署后功能验证100%通过
- 回滚方案就绪且可在15分钟内完成

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 确认发布范围和计划
   ├─ 输入: release_version, target_environment, release_notes
   ├─ 思考: 发布范围是什么？是否有回滚计划？
   ├─ 验证: 获得发布授权，回滚方案已准备
   └─ 输出: 发布确认清单
   ↓
Step 2: [ANALYZE] 分析部署环境和依赖
   ├─ 输入: 发布确认清单, environment_config
   ├─ 思考: 目标环境是否就绪？依赖服务是否正常？
   ├─ 验证: 环境检查通过，资源配置充足
   └─ 输出: 环境准备报告
   ↓
Step 3: [DESIGN] 设计部署流程和监控方案
   ├─ 输入: 环境准备报告
   ├─ 思考: 采用什么部署策略？如何监控？
   ├─ 验证: 部署流程清晰，监控指标明确
   └─ 输出: 部署执行计划
   ↓
Step 4: [IMPLEMENT] 执行部署操作
   ├─ 输入: 部署执行计划
   ├─ 思考: 按步骤执行，实时监控状态
   ├─ 验证: 每个步骤执行成功，无异常告警
   └─ 输出: 部署执行日志
   ↓
Step 5: [VERIFY] 验证部署结果
   ├─ 输入: 部署执行日志
   ├─ 执行: 功能验证、性能验证、集成验证
   ├─ 验证: 所有验证通过，监控指标正常
   └─ 输出: 部署验证报告
   ↓
Step 6: [HANDOVER] 准备交接给运维监控阶段
   ├─ 生成: Handover Context
   ├─ 更新: Global Context (发布状态)
   └─ 通知: Monitor Operate Agent
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 发布授权确认 | 开始部署前 | 批准/延期/取消 | 是否满足发布条件（测试通过、审批完成） | 发布确认清单 |
| DC-002 | 部署策略选择 | 制定部署计划时 | 滚动/蓝绿/灰度/直接 | 业务连续性要求、风险等级、基础设施 | 部署执行计划 |
| DC-003 | 回滚触发判断 | 部署过程中出现异常 | 继续/暂停/回滚 | 问题严重程度、影响范围、恢复时间 | 部署执行日志 |
| DC-004 | 验证充分性判断 | 部署后验证阶段 | 通过/失败/需进一步验证 | 功能测试结果、性能指标、错误率 | 部署验证报告 |
| DC-005 | 发布时间窗口 | 计划发布时间 | 立即/低峰期/维护窗口 | 业务影响、用户活跃度、风险评估 | 发布计划 |
| DC-006 | 灰度发布比例 | 采用灰度发布时 | 5%/10%/20%/50%/100% | 风险控制、监控反馈、逐步扩大 | 灰度发布策略 |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，部署失败或服务不可用 | 立即回滚，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，核心功能异常 | 评估修复时间，超时则回滚 |
| P2 - Minor | ERR-MINOR | 一般错误，非核心功能受影响 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响主要功能 | 记录并继续监控 |

### Error Scenario 1: 部署失败 (P0)

**识别信号**: 
- 部署脚本执行失败
- 服务启动失败
- 健康检查不通过
- 关键依赖缺失或配置错误

**处理流程**:
```
IF 部署过程出现错误导致部署失败
THEN
  1. 立即停止部署流程
  2. 分析错误原因（查看日志、监控）
  3. IF 错误可快速修复（<5分钟） THEN
       a. 尝试修复并重试部署
       b. 最多重试2次
     ELSE
       a. 立即执行回滚操作
       b. 恢复到上一个稳定版本
       c. 验证回滚后系统正常
     END
  4. 记录详细的失败原因和处理过程
  5. 升级到技术负责人和运维团队
  6. 标记发布为 [失败-已回滚]
END
```

**降级方案**: 回滚到上一稳定版本，保证服务可用性

**升级条件**: 
- 部署失败且无法快速恢复
- 回滚操作也失败
- 服务中断超过15分钟

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-001"
  timestamp: "{{ISO8601}}"
  level: "P0"
  type: "deployment_failure"
  description: "部署失败：{详细错误信息}"
  failed_step: "{失败的部署步骤}"
  rollback_executed: true/false
  action_taken: "{已采取的行动}"
  result: "rolled_back/retry_failed/escalated"
```

---

### Error Scenario 2: 部署后验证不通过 (P1)

**识别信号**: 
- 功能测试失败
- 性能指标异常
- 错误率升高
- 用户反馈问题

**处理流程**:
```
IF 部署后功能验证失败
THEN
  1. 快速定位问题原因和影响范围
  2. 评估问题的严重程度（P0/P1/P2）
  3. IF 问题为P0级别（核心功能异常） THEN
       a. 立即执行回滚
       b. 通知相关干系人
     ELSE IF 问题为P1级别 THEN
       a. 评估修复时间
       b. IF 可在15分钟内修复 THEN 尝试热修复
       c. ELSE 执行回滚
     ELSE
       a. 记录问题并持续监控
       b. 计划在下一个补丁版本修复
     END
  4. 更新部署状态和问题跟踪
END
```

**降级方案**: 根据问题严重程度决定回滚或热修复

**升级条件**: 核心功能异常或SLA面临违约风险

---

### Error Scenario 3: 性能下降 (P1/P2)

**识别信号**: 
- 响应时间显著增加
- 吞吐量下降
- 资源利用率异常（CPU、内存、磁盘IO）
- 用户投诉性能问题

**处理流程**:
```
IF 部署后性能指标异常
THEN
  1. 对比部署前后的性能基线
  2. 识别性能瓶颈（应用层、数据库、网络等）
  3. 评估性能下降对业务的影响
  4. IF 性能下降严重影响业务（>30%） THEN
       a. 考虑回滚或紧急优化
       b. 扩容资源作为临时方案
     ELSE
       a. 持续监控性能趋势
       b. 计划在后续版本优化
     END
  5. 记录性能数据和优化建议
END
```

**降级方案**: 临时扩容资源，承诺后续优化

**升级条件**: 性能下降超过30%或SLA面临违约风险

---

### Error Scenario 4: 回滚失败 (P0)

**识别信号**: 
- 回滚脚本执行失败
- 回滚后服务仍不正常
- 数据不一致

**处理流程**:
```
IF 回滚操作失败
THEN
  1. 立即升级到最高优先级（P0）
  2. 召集应急响应团队（开发、运维、DBA）
  3. 诊断回滚失败的根本原因
  4. 尝试替代回滚方案（手动回滚、数据库恢复等）
  5. IF 仍无法恢复 THEN
       a. 启动灾难恢复预案
       b. 考虑切换到备用环境
       c. 通知业务方和用戶
     END
  6. 全程记录处理过程和决策
END
```

**降级方案**: 启动灾难恢复预案，切换到备用环境

**升级条件**: 回滚失败且服务无法恢复，立即升级到CTO级别

---

## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | DEPLOY-SUCCESS-RATE | ≥99% | (成功部署次数/总部署次数) × 100% | 部署历史记录 | 30% |
| KPI-002 | ROLLBACK-TIME | ≤15min | 从触发回滚到服务恢复的时间 | 回滚演练/实际回滚记录 | 25% |
| KPI-003 | ZERO-DOWNTIME | 100% | (零停机部署次数/总部署次数) × 100% | 部署监控日志 | 25% |
| KPI-004 | POST-DEPLOY-VERIFICATION | 100% | (通过的验证项/总验证项) × 100% | 部署验证报告 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.25) + (KPI-003 × 0.25) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 部署清单所有步骤已执行
- [ ] 所有环境（dev/staging/prod）部署一致
- [ ] 配置文件已正确更新
- [ ] 数据库迁移已执行（如需要）
- [ ] 回滚方案已验证可用

**一致性验证 (Consistency)**:
- [ ] 版本号在所有位置一致
- [ ] 配置与环境匹配
- [ ] 依赖服务版本兼容
- [ ] API契约未破坏（或有版本控制）

**准确性验证 (Accuracy)**:
- [ ] 部署脚本执行无误
- [ ] 配置参数正确
- [ ] 环境变量设置准确
- [ ] 健康检查通过

**可执行性验证 (Executability)**:
- [ ] 服务正常启动并运行
- [ ] 功能验证全部通过
- [ ] 性能指标符合预期
- [ ] 监控告警已配置

**规范性验证 (Compliance)**:
- [ ] 遵循部署流程和检查清单
- [ ] 安全配置已应用（SSL、访问控制等）
- [ ] 合规要求已满足（数据保护、审计等）
- [ ] 部署文档已更新

---

## Handover Criteria (交接标准)

### 准出条件

```
✅ 部署清单所有步骤已执行
✅ 部署后验证全部通过
✅ 监控告警已配置并正常运行
✅ 回滚方案已就绪并验证
✅ 发布记录已归档
✅ Handover Context 已生成
```

### 交付物清单

| 交付物 | 格式 | 位置 | 版本 | 说明 |
|--------|------|------|------|------|
| 部署包 | Docker Image/Tarball | registry/releases/ | {version} | 发布版本 |
| 部署脚本 | Shell/Python | deploy/scripts/ | v1.0.0 | 自动化部署脚本 |
| 部署记录 | Markdown/YAML | logs/deployment-log.md | - | 部署过程日志 |
| 回滚方案 | Markdown | docs/rollback-plan.md | v1.0.0 | 回滚脚本和步骤 |
| 发布报告 | Markdown | docs/release-report.md | v1.0.0 | 发布总结 |
| 监控配置 | YAML/JSON | monitoring/alerts.yaml | v1.0.0 | 告警规则 |

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "deployment"
    to_stage: "monitoring-operations"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "success/partial/failed_rolled_back"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    deployment_duration: "{{duration}}"
    downtime: "{{duration_or_zero}}"
    
  artifacts:
    delivered:
      - name: "Release Package"
        path: "registry/releases/{version}"
        version: "{release_version}"
        checksum: "{{SHA256}}"
      - name: "Deployment Scripts"
        path: "deploy/scripts/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "Deployment Log"
        path: "logs/deployment-log.md"
        version: "1.0.0"
      - name: "Rollback Plan"
        path: "docs/rollback-plan.md"
        version: "1.0.0"
      
  decisions:
    - id: "DC-002"
      description: "部署策略选择"
      rationale: "选择蓝绿部署以最小化停机时间"
      alternatives_considered: ["滚动部署", "灰度发布"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "非核心功能X存在小问题，计划下版本修复"
        
  risks:
    - id: "RISK-001"
      description: "新版本依赖的中间件版本较新，需密切监控"
      probability: "low"
      impact: "medium"
      mitigation: "已在测试环境充分验证，生产环境加强监控"
      
  recommendations:
    - "前24小时密切监控错误率和响应时间"
    - "关注数据库性能，必要时优化慢查询"
    - "准备好热修复方案应对紧急情况"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "DEPLOY-SUCCESS-RATE"
        value: 100
        target: 99
        status: "pass"
      - kpi_id: "KPI-002"
        name: "ROLLBACK-TIME"
        value: 8
        target: 15
        status: "pass"
        unit: "minutes"
      - kpi_id: "KPI-003"
        name: "ZERO-DOWNTIME"
        value: 100
        target: 100
        status: "pass"
      - kpi_id: "KPI-004"
        name: "POST-DEPLOY-VERIFICATION"
        value: 100
        target: 100
        status: "pass"
    overall_score: 100
    grade: "excellent"
```

---

## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| **Agent** | `../../agents/deploy-release.agent.md` | 部署发布角色定义 |
| **Prompt** | `../../prompts/deploy-release.prompt.md` | 部署发布执行提示词 |
| **Instruction** | `../../instructions/deploy-release.instructions.md` | 部署发布技术指令 |
| **Skill** | `../../skills/deploy-release/SKILL.md` | 部署发布领域技能 |

---

## Prerequisites

### Required Preconditions

1. ✅ 测试验证已通过 (verify-test 场景输出)
2. ✅ 部署环境已准备并验证
3. ✅ 发布计划已确认并获得批准
4. ✅ 回滚方案已准备并测试
5. ✅ 监控告警已配置
6. ✅ 相关干系人已通知

### Expected Input

| Input Variable | Type | Required | Default | Description | Validation |
|----------------|------|----------|---------|-------------|------------|
| `release_version` | string | true | - | 发布版本号 | 语义化版本格式 |
| `release_scope` | markdown | true | - | 发布范围说明 | 包含变更清单 |
| `target_environment` | string | true | - | 目标环境 | prod/staging/dev |
| `rollback_plan` | markdown | true | - | 回滚方案 | 包含详细步骤 |
| `deployment_config` | yaml | true | - | 部署配置 | 有效的YAML配置 |
| `health_check_url` | string | false | "" | 健康检查URL | 有效的URL |
| `smoke_tests` | array | false | [] | 冒烟测试用例 | 测试脚本路径 |

---

## Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识
- **Version**: 1.2.0

---

**Scenario Version**: 1.2.0  
**Last Updated**: 2026-05-07  
**Author**: AI Harness Engineering Team
