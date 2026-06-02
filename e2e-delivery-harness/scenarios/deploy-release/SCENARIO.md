---
name: deploy-release
description: "部署发布场景，负责将软件部署到目标环境并完成发布"
version: "1.2.0"
type: scenario
category: operations
stage: deployment
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [deployment, release, operations, devops]
---
# Deploy Release - Deployment Scenario

## Purpose

将测试通过的软件安全、可靠地部署到目标环境，执行发布流程，确保部署成功并建立完善的监控和回滚机制，最小化对用户的影响。

### Business Value

- **保证服务连续性**: 通过零停机或最短停机时间的部署策略，确保用户服务不中断
- **降低部署风险**: 完善的回滚机制和灰度发布策略，快速应对异常情况
- **提升部署效率**: 自动化部署流程和标准化操作，减少人工干预和错误
- **增强可追溯性**: 完整的部署记录和监控数据，便于问题定位和事后分析
- **支持业务敏捷**: 快速可靠的部署能力，加速产品迭代和功能上线

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成部署发布工作

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 确认发布范围和计划
   ├─ 问：发布范围是什么？是否有回滚计划？是否获得发布授权？
   ├─ 验证：检查测试报告、审批记录、回滚方案
   └─ 检查：版本号、变更清单、目标环境、时间窗口
   ↓
[ANALYZE] Step 2: 分析部署环境和依赖
   ├─ 问：目标环境是否就绪？依赖服务是否正常？资源配置充足吗？
   ├─ 验证：环境检查、资源评估、依赖服务健康状态
   └─ 检查：服务器、网络、数据库、缓存、消息队列等
   ↓
[DESIGN] Step 3: 设计部署流程和监控方案
   ├─ 问：采用什么部署策略（蓝绿/滚动/灰度）？如何监控？告警阈值是多少？
   ├─ 验证：部署流程清晰，监控指标明确，告警规则合理
   └─ 检查：部署步骤、验证点、回滚触发条件、监控面板
   ↓
[IMPLEMENT] Step 4: 执行部署操作
   ├─ 问：按步骤执行，实时监控状态，有异常吗？
   ├─ 验证：每个步骤执行成功，无异常告警，健康检查通过
   └─ 检查：部署日志、服务状态、资源使用、错误率
   ↓
[VERIFY] Step 5: 验证部署结果
   ├─ 执行：功能验证、性能验证、集成验证、数据验证
   ├─ 验证：所有验证通过，监控指标正常，用户体验良好
   └─ 检查：核心功能、API响应、数据库一致性、日志无异常
   ↓
[HANDOVER] Step 6: 准备交接给运维监控阶段
   ├─ 生成：Handover Context（含部署统计、监控配置、遗留问题、建议）
   ├─ 更新：Global Context（发布状态、监控重点、应急联系人）
   └─ 通知：Monitor Operate Agent（开始持续监控）
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 发布授权确认 | 开始部署前 | 批准/延期/取消 | 是否满足发布条件（测试通过、审批完成、时间窗口合适） | 发布确认清单 |
| DC-002 | 部署策略选择 | 制定部署计划时 | 滚动/蓝绿/灰度/直接 | 业务连续性要求、风险等级、基础设施支持、停机容忍度 | 部署执行计划 |
| DC-003 | 回滚触发判断 | 部署过程中出现异常 | 继续/暂停/回滚 | 问题严重程度、影响范围、恢复时间、SLA要求 | 部署执行日志 |
| DC-004 | 验证充分性判断 | 部署后验证阶段 | 通过/失败/需进一步验证 | 功能测试结果、性能指标、错误率、用户反馈 | 部署验证报告 |
| DC-005 | 发布时间窗口 | 计划发布时间 | 立即/低峰期/维护窗口 | 业务影响、用户活跃度、风险评估、变更紧急程度 | 发布计划 |
| DC-006 | 灰度发布比例 | 采用灰度发布时 | 5%/10%/20%/50%/100% | 风险控制、监控反馈、逐步扩大、用户接受度 | 灰度发布策略 |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### Error Scenario 1: 部署失败 (P0)

**识别信号**: 
- 部署脚本执行失败
- 服务启动失败
- 健康检查不通过
- 关键依赖缺失或配置错误
- 容器崩溃或重启循环

**处理流程**:
```
IF 部署过程出现错误导致部署失败
THEN
  1. 立即停止部署流程
  2. 分析错误原因（查看日志、监控、事件记录）
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
  error_details:
    log_snippet: "{相关日志片段}"
    stack_trace: "{堆栈跟踪（如适用）}"
    affected_services: ["service_1", "service_2"]
  rollback_executed: true/false
  rollback_result: "success/failed/partial"
  action_taken: "{已采取的行动}"
  result: "rolled_back/retry_failed/escalated"
  estimated_recovery_time: "{预计恢复时间}"
```

---

### Error Scenario 2: 部署后验证不通过 (P1)

**识别信号**: 
- 功能测试失败
- 性能指标异常（响应时间>阈值、错误率>阈值）
- 健康检查端点返回非200状态
- 用户反馈问题或投诉
- 监控告警触发

**处理流程**:
```
IF 部署后功能验证失败
THEN
  1. 快速定位问题原因和影响范围
  2. 评估问题的严重程度（P0/P1/P2）
  3. IF 问题为P0级别（核心功能异常） THEN
       a. 立即执行回滚
       b. 通知相关干系人（产品、运营、客服）
     ELSE IF 问题为P1级别 THEN
       a. 评估修复时间
       b. IF 可在15分钟内修复 THEN 尝试热修复
       c. ELSE 执行回滚
     ELSE
       a. 记录问题并持续监控
       b. 计划在下一个补丁版本修复
     END
  4. 更新部署状态和问题跟踪
  5. 编写事故报告（如需要）
END
```

**降级方案**: 根据问题严重程度决定回滚或热修复

**升级条件**: 核心功能异常或SLA面临违约风险

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-002"
  timestamp: "{{ISO8601}}"
  level: "P1"
  type: "post_deployment_verification_failure"
  description: "部署后验证失败：{详细描述}"
  failed_checks:
    - check_name: "{检查项名称}"
      expected: "{预期结果}"
      actual: "{实际结果}"
      severity: "P0/P1/P2"
  impact_assessment:
    affected_users: "{受影响用户数或比例}"
    business_impact: "{业务影响描述}"
    sla_risk: "high/medium/low"
  action_taken: "rollback/hotfix/monitor"
  result: "resolved/monitoring/escalated"
```

---

### Error Scenario 3: 性能下降 (P1/P2)

**识别信号**: 
- 响应时间显著增加（>基线30%）
- 吞吐量下降
- 资源利用率异常（CPU>80%、内存>90%、磁盘IO高）
- 数据库慢查询增多
- 用户投诉性能问题

**处理流程**:
```
IF 部署后性能指标异常
THEN
  1. 对比部署前后的性能基线
  2. 识别性能瓶颈（应用层、数据库、网络、缓存等）
  3. 评估性能下降对业务的影响
  4. IF 性能下降严重影响业务（>30%） THEN
       a. 考虑回滚或紧急优化
       b. 扩容资源作为临时方案（增加实例数、提升配置）
     ELSE
       a. 持续监控性能趋势
       b. 计划在后续版本优化
     END
  5. 记录性能数据和优化建议
  6. 更新性能基线（如新基线更合理）
END
```

**降级方案**: 临时扩容资源，承诺后续优化

**升级条件**: 性能下降超过30%或SLA面临违约风险

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-003"
  timestamp: "{{ISO8601}}"
  level: "P1/P2"
  type: "performance_degradation"
  description: "性能下降：{详细描述}"
  metrics_comparison:
    before_deployment:
      response_time: "{基线响应时间}ms"
      throughput: "{基线吞吐量}req/s"
      cpu_usage: "{基线CPU}%"
      memory_usage: "{基线内存}%"
    after_deployment:
      response_time: "{当前响应时间}ms"
      throughput: "{当前吞吐量}req/s"
      cpu_usage: "{当前CPU}%"
      memory_usage: "{当前内存}%"
  degradation_percentage: "{下降百分比}%"
  bottleneck_identified: "{瓶颈位置：应用/数据库/网络/缓存}"
  action_taken: "scale_up/optimize/rollback/monitor"
  result: "improved/stable/degraded"
```

---

### Error Scenario 4: 回滚失败 (P0)

**识别信号**: 
- 回滚脚本执行失败
- 回滚后服务仍不正常
- 数据不一致或丢失
- 数据库迁移无法回退

**处理流程**:
```
IF 回滚操作失败
THEN
  1. 立即升级到最高优先级（P0）
  2. 召集应急响应团队（开发、运维、DBA、架构师）
  3. 诊断回滚失败的根本原因
  4. 尝试替代回滚方案：
     a. 手动回滚（逐个服务回退）
     b. 数据库恢复（从备份还原）
     c. 切换到备用环境（如有）
  5. IF 仍无法恢复 THEN
       a. 启动灾难恢复预案
       b. 考虑切换到灾备站点
       c. 通知业务方和用户（发布公告）
     END
  6. 全程记录处理过程和决策
  7. 事后编写详细的事故报告
END
```

**降级方案**: 启动灾难恢复预案，切换到备用环境或灾备站点

**升级条件**: 回滚失败且服务无法恢复，立即升级到CTO级别

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-004"
  timestamp: "{{ISO8601}}"
  level: "P0"
  type: "rollback_failure"
  description: "回滚失败：{详细描述}"
  rollback_attempt:
    strategy_used: "{使用的回滚策略}"
    failure_reason: "{失败原因}"
    attempted_alternatives: ["替代方案1", "替代方案2"]
  current_status: "degraded/down/partial"
  emergency_team_assembled: true/false
  disaster_recovery_activated: true/false
  action_taken: "{已采取的行动}"
  result: "recovered/partial_recovery/unrecoverable"
  estimated_downtime: "{预计停机时间}"
  business_impact: "{业务影响评估}"
```

## Quality Metrics

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | DEPLOY-SUCCESS-RATE | ≥99% | (成功部署次数/总部署次数) × 100% | 部署历史记录统计 | 30% |
| KPI-002 | ROLLBACK-TIME | ≤15min | 从触发回滚到服务恢复的时间 | 回滚演练/实际回滚记录 | 25% |
| KPI-003 | ZERO-DOWNTIME | 100% | (零停机部署次数/总部署次数) × 100% | 部署监控日志分析 | 25% |
| KPI-004 | POST-DEPLOY-VERIFICATION | 100% | (通过的验证项/总验证项) × 100% | 部署验证报告检查 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.25) + (KPI-003 × 0.25) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

**KPI详细说明**:
- **DEPLOY-SUCCESS-RATE**: 反映部署流程的可靠性和稳定性，过低表示部署流程存在问题
- **ROLLBACK-TIME**: 衡量应急响应能力，快速回滚是降低故障影响的关键
- **ZERO-DOWNTIME**: 体现部署策略的先进性，零停机部署是DevOps最佳实践
- **POST-DEPLOY-VERIFICATION**: 确保部署质量，避免带病上线

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 部署清单所有步骤已执行
- [ ] 所有环境（dev/staging/prod）部署一致
- [ ] 配置文件已正确更新
- [ ] 数据库迁移已执行（如需要）
- [ ] 回滚方案已验证可用
- [ ] 监控告警已配置并测试

**一致性验证 (Consistency)**:
- [ ] 版本号在所有位置一致（代码、镜像、配置、文档）
- [ ] 配置与环境匹配（dev/staging/prod差异化配置）
- [ ] 依赖服务版本兼容
- [ ] API契约未破坏（或有版本控制）

**准确性验证 (Accuracy)**:
- [ ] 部署脚本执行无误
- [ ] 配置参数正确（数据库连接、API密钥、环境变量）
- [ ] 健康检查通过（所有端点返回200）
- [ ] 数据迁移完整且一致

**可执行性验证 (Executability)**:
- [ ] 服务正常启动并运行
- [ ] 功能验证全部通过
- [ ] 性能指标符合预期（响应时间、吞吐量、错误率）
- [ ] 监控告警已配置并正常工作

**规范性验证 (Compliance)**:
- [ ] 遵循部署流程和检查清单
- [ ] 安全配置已应用（SSL、访问控制、防火墙规则）
- [ ] 合规要求已满足（数据保护、审计日志、隐私政策）
- [ ] 部署文档已更新（README、CHANGELOG、部署手册）

## Handover Criteria

### 准出条件

```
✅ 部署清单所有步骤已执行
✅ 部署后验证全部通过（功能、性能、集成、数据）
✅ 监控告警已配置并正常运行
✅ 回滚方案已就绪并验证可用
✅ 发布记录已归档（部署日志、验证报告、监控快照）
✅ Handover Context 已生成，所有必需字段完整
✅ 质量评分 ≥70分（基于KPIs计算）
```

### 交付物清单

| 交付物 | 格式 | 位置 | 版本 | 说明 |
|--------|------|------|------|------|
| 部署包 | Docker Image/Tarball | registry/releases/ | {version} | 发布版本的制品 |
| 部署脚本 | Shell/Python | deploy/scripts/ | v1.0.0 | 自动化部署脚本 |
| 部署记录 | Markdown/YAML | logs/deployment-log.md | - | 部署过程详细日志 |
| 回滚方案 | Markdown | docs/rollback-plan.md | v1.0.0 | 回滚脚本和步骤 |
| 发布报告 | Markdown | docs/release-report.md | v1.0.0 | 发布总结和质量评估 |
| 监控配置 | YAML/JSON | monitoring/alerts.yaml | v1.0.0 | 告警规则和监控面板 |
| 验证报告 | Markdown | reports/verification-report.md | v1.0.0 | 部署后验证结果 |

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
    deployment_strategy: "blue-green/rolling/canary/direct"
    
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
      - name: "Release Report"
        path: "docs/release-report.md"
        version: "1.0.0"
      - name: "Monitoring Configuration"
        path: "monitoring/alerts.yaml"
        version: "1.0.0"
      - name: "Verification Report"
        path: "reports/verification-report.md"
        version: "1.0.0"
      
  decisions:
    - id: "DC-002"
      description: "部署策略选择"
      rationale: "选择蓝绿部署以最小化停机时间"
      alternatives_considered: ["滚动部署", "灰度发布"]
      criteria_used: "业务连续性要求高，基础设施支持蓝绿部署"
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "非核心功能X存在小问题，计划下版本修复"
        severity: "P3"
        planned_fix: "v1.1.0"
        
  risks:
    - id: "RISK-001"
      description: "新版本依赖的中间件版本较新，需密切监控"
      probability: "low"
      impact: "medium"
      affected_areas: ["缓存服务", "消息队列"]
      mitigation: "已在测试环境充分验证，生产环境加强监控"
      contingency_plan: "如出现问题，立即回滚到上一版本"
      
  recommendations:
    - "前24小时密切监控错误率和响应时间"
    - "关注数据库性能，必要时优化慢查询"
    - "准备好热修复方案应对紧急情况"
    - "建议在下次迭代中优化启动时间（当前>30秒）"
    - "建议增加自动化冒烟测试，减少人工验证工作量"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "DEPLOY-SUCCESS-RATE"
        value: 100
        target: 99
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-002"
        name: "ROLLBACK-TIME"
        value: 8
        target: 15
        unit: "minutes"
        status: "pass"
        note: "回滚演练时间，实际未触发回滚"
      - kpi_id: "KPI-003"
        name: "ZERO-DOWNTIME"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
      - kpi_id: "KPI-004"
        name: "POST-DEPLOY-VERIFICATION"
        value: 100
        target: 100
        unit: "%"
        status: "pass"
        verification_items:
          - item: "功能验证"
            status: "pass"
          - item: "性能验证"
            status: "pass"
          - item: "集成验证"
            status: "pass"
          - item: "数据验证"
            status: "pass"
    overall_score: 100
    grade: "excellent"
    recommendation: "approved_for_production"
      
  next_steps:
    immediate:
      - "Monitor Operate Agent开始持续监控（至少24小时）"
      - "重点关注错误率、响应时间、资源使用率"
      - "设置告警通知渠道（Slack、邮件、短信）"
    short_term:
      - "24小时后编写部署回顾报告"
      - "收集团队反馈，优化部署流程"
      - "更新部署文档和最佳实践"
    long_term:
      - "分析部署数据，识别改进机会"
      - "探索更先进的部署策略（如GitOps、渐进式交付）"
      - "提升自动化水平，减少人工干预"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/deploy-release.agent.md` | 部署发布Agent角色定义 |
| Prompt | `../../prompts/deploy-release.prompt.md` | 部署发布提示词模板 |
| Skill | `../../skills/deploy-release/SKILL.md` | 部署发布技能包 |
| Instruction | `../../instructions/deploy-release.instructions.md` | 部署发布技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [Deployment Best Practices](../../standards/deployment-best-practices.md) - 部署最佳实践指南
  - [Rollback Strategy](../../standards/rollback-strategy.md) - 回滚策略标准
  - [Health Check Guidelines](../../standards/health-check-guidelines.md) - 健康检查指南
  - [Monitoring Standards](../../standards/monitoring-standards.md) - 监控配置标准
- **Templates**: 
  - [Deployment Plan Template](../../templates/deployment-plan.template.md) - 部署计划模板
  - [Rollback Plan Template](../../templates/rollback-plan.template.md) - 回滚方案模板
  - [Release Report Template](../../templates/release-report.template.md) - 发布报告模板
  - [Post-Mortem Template](../../templates/post-mortem.template.md) - 事故复盘模板
- **Evaluations**: 
  - [Deployment Quality Checklist](../../evaluations/deployment-quality-checklist.md) - 部署质量检查清单
  - [Rollback Drill Report](../../evaluations/rollback-drill-report.md) - 回滚演练报告
  - [Performance Baseline](../../evaluations/performance-baseline.md) - 性能基线报告

## Prerequisites

### 必需前置条件

1. ✅ 测试验证已通过 (verify-test 场景输出)
2. ✅ 部署环境已准备并验证（服务器、网络、依赖服务）
3. ✅ 发布计划已确认并获得批准（产品经理、技术负责人签字）
4. ✅ 回滚方案已准备并测试（回滚演练通过）
5. ✅ 监控告警已配置（Prometheus、Grafana、AlertManager等）
6. ✅ 相关干系人已通知（产品、运营、客服、管理层）

### 期望输入

| Input Variable | Type | Required | Default | Description | Validation |
|----------------|------|----------|---------|-------------|------------|
| `release_version` | string | true | - | 发布版本号 | 语义化版本格式（如v1.2.3） |
| `release_scope` | markdown | true | - | 发布范围说明 | 包含变更清单、新功能、Bug修复 |
| `target_environment` | string | true | - | 目标环境 | prod/staging/dev，必须明确指定 |
| `rollback_plan` | markdown | true | - | 回滚方案 | 包含详细步骤、预计时间、验证方法 |
| `deployment_config` | yaml | true | - | 部署配置 | 有效的YAML配置，包含所有必需参数 |
| `health_check_url` | string | false | "" | 健康检查URL | 有效的URL，返回200表示健康 |
| `smoke_tests` | array | false | [] | 冒烟测试用例 | 测试脚本路径列表，用于快速验证 |
| `deployment_strategy` | string | false | "rolling" | 部署策略 | blue-green/rolling/canary/direct |
| `maintenance_window` | object | false | {} | 维护窗口 | 开始时间、结束时间、通知对象 |
