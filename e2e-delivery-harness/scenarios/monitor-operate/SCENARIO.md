---
name: monitor-operate
description: "监控运维场景，负责系统上线后的监控、告警和运维支持"
version: "1.2.0"
type: scenario
category: operations
stage: monitoring-operations
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [monitoring, operations, sre, observability]
---
# Monitor Operate - Monitoring & Operations Scenario

## Purpose

监控系统运行状态，处理告警和故障，确保系统稳定运行和SLO达成，通过持续优化提升运维效率和系统可靠性。

### Business Value

- **保障服务稳定性**: 通过完善的监控体系和快速响应机制，确保系统高可用性（≥99.5%）
- **降低故障影响**: 快速发现和定位问题，缩短MTTD（平均检测时间）和MTTR（平均修复时间）
- **提升运维效率**: 自动化监控和告警，减少人工巡检工作量，提高问题发现和处理效率
- **数据驱动决策**: 基于监控数据进行容量规划、性能优化和架构改进，支撑业务增长
- **持续改进文化**: 通过故障复盘和运维数据分析，不断优化系统稳定性和运维流程

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成监控运维工作

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 了解系统基线和SLO
   ├─ 问：系统的SLO目标是什么？当前Error Budget剩余多少？关键监控点有哪些？
   ├─ 验证：与业务确认SLO指标（可用性、延迟、错误率）
   └─ 检查：识别核心监控点（基础设施、应用、业务三层）
   ↓
[SETUP] Step 2: 配置监控和告警
   ├─ 问：需要监控哪些指标？告警阈值如何设置？通知渠道是否畅通？
   ├─ 验证：黄金指标全覆盖（Latency、Traffic、Errors、Saturation）
   └─ 检查：告警规则合理，无频繁误报，升级机制有效
   ↓
[WATCH] Step 3: 监控系统状态
   ├─ 问：系统当前状态如何？各项指标是否在正常范围？有无异常趋势？
   ├─ 验证：监控面板数据正常，无异常告警
   └─ 检查：定期巡检，记录系统健康状态和资源使用情况
   ↓
[RESPOND] Step 4: 响应告警和事件
   ├─ 问：告警是否需要立即处理？级别是什么？根因可能在哪里？
   ├─ 验证：判断告警级别（P0/P1/P2/P3），按流程响应
   └─ 检查：快速止血优先于根因分析，及时通报相关方
   ↓
[IMPROVE] Step 5: 优化监控体系
   ├─ 问：监控是否有盲区？告警噪声是否过高？运维流程能否优化？
   ├─ 验证：分析监控覆盖率、告警有效性、响应时效
   └─ 检查：识别优化机会，更新监控配置和运维文档
   ↓
[REPORT] Step 6: 产出运维报告
   ├─ 生成：运维报告（含监控概览、告警统计、故障分析、容量评估、优化建议）
   ├─ 更新：Global Context（系统状态、SLO达成情况、遗留问题）
   └─ 交接：下一班次或下一阶段（如需求分析进行新功能开发）
```

## Decision Checkpoints

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 监控覆盖完整性 | 配置监控时 | 基础/标准/高级监控 | 系统重要性、业务复杂度、资源预算 | 监控配置文档 |
| DC-002 | 告警阈值设置 | 配置告警规则时 | 保守/平衡/激进 | 历史数据、业务容忍度、误报率要求 | 告警规则配置 |
| DC-003 | 告警响应优先级 | 收到告警时 | P0(立即)/P1(15min)/P2(1h)/P3(下一个工作日) | 影响范围、业务价值、SLA要求 | 告警处理记录 |
| DC-004 | 故障处理策略 | 发生故障时 | 快速止血/根因修复/降级方案 | 故障严重程度、修复时间预估、业务影响 | 故障报告 |
| DC-005 | 扩容决策 | 容量评估时 | 立即扩容/计划扩容/优化现有资源 | 资源使用率趋势、业务增长预测、成本考量 | 容量规划报告 |
| DC-006 | 变更窗口选择 | 执行运维变更时 | 立即/低峰期/维护窗口 | 变更风险、业务影响、紧急程度 | 变更记录 |

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### Error Scenario 1: 告警风暴 (P1)

**识别信号**: 
- 短时间内大量告警同时触发（>10个/分钟）
- 多个组件同时告警，可能存在级联效应
- 告警通知渠道被淹没，难以识别核心问题

**处理流程**:
```
IF 检测到告警风暴
THEN
  1. 立即识别根本告警（触发其他告警的根源）
  2. 暂时抑制次要告警（避免干扰，保留关键告警）
  3. 优先处理核心问题（恢复核心服务可用性）
  4. 通知相关团队（开发、运维、DBA）协同处理
  5. 记录告警风暴详情（触发时间、告警数量、影响范围）
  6. 事后优化告警规则（调整阈值、增加依赖关系、设置静默期）
END
```

**降级方案**: 暂时关闭非关键告警，聚焦核心服务恢复

**升级条件**: 核心服务不可用或影响超过50%用户

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-001"
  timestamp: "{{ISO8601}}"
  level: "P1"
  type: "alert_storm"
  description: "告警风暴：{详细描述，包括告警数量、触发时间、影响范围}"
  alert_statistics:
    total_alerts: {number}
    duration_minutes: {number}
    affected_services: ["service_1", "service_2"]
    root_cause_alert: "{根本告警ID}"
  suppression_applied: true/false
  suppressed_alerts_count: {number}
  action_taken: "{已采取的行动}"
  result: "resolved/partial/unresolved"
  post_mortem_required: true/false
```

---

### Error Scenario 2: 告警误报 (P2)

**识别信号**: 
- 告警触发但实际无问题（虚假告警）
- 同一告警频繁触发又自动恢复（抖动）
- 告警阈值设置不合理（过于敏感或过于宽松）
- 误报率超过20%

**处理流程**:
```
IF 检测到告警误报
THEN
  1. 验证告警真伪（检查监控数据、日志、系统状态）
  2. 分析误报原因（阈值不当、数据采集问题、临时波动）
  3. 调整告警阈值（基于历史数据和业务容忍度）
  4. 优化告警条件（增加持续时间要求、组合多个指标）
  5. 测试新告警规则（在staging环境验证）
  6. 更新告警配置并监控效果
  7. 记录误报案例，纳入知识库
END
```

**降级方案**: 暂时降低告警级别或增加静默期，持续观察

**升级条件**: 误报率超过20%且影响运维团队工作效率

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-002"
  timestamp: "{{ISO8601}}"
  level: "P2"
  type: "false_positive_alert"
  description: "告警误报：{详细描述}"
  alert_rule: "{告警规则名称}"
  false_positive_count: {number}
  time_period: "{时间段}"
  root_cause: "threshold_too_sensitive/data_spike/temporary_fluctuation"
  action_taken: "adjusted_threshold/added_duration_requirement/combined_metrics"
  new_threshold: "{新阈值}"
  result: "reduced_noise/still_noisy/resolved"
  follow_up_required: true/false
```

---

### Error Scenario 3: SLO即将违反 (P1)

**识别信号**: 
- Error Budget消耗速度过快（预计7天内耗尽）
- 可用性、延迟、错误率等指标接近SLO阈值
- 趋势分析显示SLO将在短期内违反

**处理流程**:
```
IF SLO趋势显示即将违反目标
THEN
  1. 立即升级告警（通知技术负责人、产品经理、业务方）
  2. 启动应急响应流程（成立应急小组，制定缓解方案）
  3. 分析SLO违反原因（代码问题、容量不足、外部依赖故障）
  4. 采取缓解措施：
     a. 短期：降级非核心功能、限流、扩容
     b. 中期：修复代码缺陷、优化性能
     c. 长期：架构改进、容量规划
  5. 持续监控SLO达成情况（每小时更新）
  6. 准备事后复盘（分析根因、制定改进计划）
  7. 考虑暂停新功能发布，专注稳定性提升
END
```

**降级方案**: 降级非核心功能，保障核心服务SLO

**升级条件**: SLO已违反或预计24小时内违反

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-003"
  timestamp: "{{ISO8601}}"
  level: "P1"
  type: "slo_breach_risk"
  description: "SLO即将违反：{详细描述}"
  slo_details:
    metric_name: "{SLO指标名称}"
    target: "{SLO目标值}"
    current_value: "{当前值}"
    error_budget_remaining: "{剩余Error Budget百分比}"
    estimated_breach_time: "{预计违反时间}"
  trend_analysis:
    direction: "worsening/stable/improving"
    rate_of_change: "{变化速率}"
  mitigation_actions:
    - action_1: "{缓解措施1}"
    - action_2: "{缓解措施2}"
  action_taken: "degraded_non_critical/scaled_up/optimized_performance"
  result: "stabilized/at_risk/breached"
  feature_freeze_recommended: true/false
```

---

### Error Scenario 4: 监控数据缺失 (P2)

**识别信号**: 
- 关键指标无数据或数据中断
- 监控Agent离线或采集失败
- 数据存储故障或查询超时
- 监控面板显示空白或错误

**处理流程**:
```
IF 关键监控指标无数据
THEN
  1. 检查监控Agent状态（是否运行、是否正常采集）
  2. 检查网络连通性（Agent到监控服务器的网络）
  3. 验证指标定义是否正确（指标名称、标签、数据类型）
  4. 检查数据存储状态（Prometheus、InfluxDB等是否正常）
  5. IF 问题可快速修复（<15分钟） THEN
       a. 重启Agent或修复配置
       b. 验证数据恢复
     ELSE
       a. 标记为 [数据缺失]
       b. 通知监控团队
       c. 使用备用监控手段（日志分析、手动检查）
     END
  6. 记录数据缺失详情和影响范围
  7. 事后分析根因，优化监控架构
END
```

**降级方案**: 使用备用监控手段（日志分析、手动检查），承诺尽快修复

**升级条件**: 核心指标数据缺失超过30分钟，影响故障检测能力

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-004"
  timestamp: "{{ISO8601}}"
  level: "P2"
  type: "monitoring_data_missing"
  description: "监控数据缺失：{详细描述}"
  affected_metrics: ["metric_1", "metric_2"]
  affected_services: ["service_1", "service_2"]
  duration_minutes: {number}
  root_cause: "agent_offline/network_issue/storage_failure/misconfiguration"
  action_taken: "restarted_agent/fixed_config/notified_team"
  result: "restored/partial/still_missing"
  backup_monitoring_used: true/false
  estimated_fix_time: "{预计修复时间}"
```

## Quality Metrics

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | MTTD | ≤5min | 异常发生到告警触发的平均时间 | 告警日志分析 | 25% |
| KPI-002 | MTTR | ≤30min | 告警触发到问题修复的平均时间 | 故障记录统计 | 25% |
| KPI-003 | ALERT-NOISE | ≤20% | (无效告警数/总告警数) × 100% | 告警有效性分析 | 20% |
| KPI-004 | SLO-COMPLY | ≥99.5% | (SLO达标时间/总时间) × 100% | SLO监控面板 | 30% |

**综合评分计算**: 
```
Quality Score = (KPI-001得分 × 0.25) + (KPI-002得分 × 0.25) + (KPI-003得分 × 0.20) + (KPI-004得分 × 0.30)

KPI得分计算:
- MTTD: ≤5min=100分, 5-10min=80分, 10-15min=60分, >15min=0分
- MTTR: ≤30min=100分, 30-60min=80分, 60-120min=60分, >120min=0分
- ALERT-NOISE: ≤20%=100分, 20-30%=80分, 30-40%=60分, >40%=0分
- SLO-COMPLY: ≥99.5%=100分, 99-99.5%=80分, 98-99%=60分, <98%=0分

合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

**KPI详细说明**:
- **MTTD (Mean Time To Detect)**: 衡量监控体系的灵敏度，越短表示问题发现越快
- **MTTR (Mean Time To Repair)**: 衡量运维团队的响应和修复能力，越短表示故障影响越小
- **ALERT-NOISE**: 衡量告警质量，越低表示告警越精准，减少运维疲劳
- **SLO-COMPLY**: 衡量系统稳定性，越高表示服务质量越好

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 黄金指标全覆盖（Latency、Traffic、Errors、Saturation）
- [ ] 基础设施监控完整（CPU、内存、磁盘、网络）
- [ ] 应用层监控完整（QPS、响应时间、错误率、JVM GC）
- [ ] 业务指标监控完整（订单量、转化率、用户活跃度）
- [ ] 告警规则配置完整（阈值、级别、通知渠道、升级机制）

**一致性验证 (Consistency)**:
- [ ] 监控指标命名统一（符合命名规范）
- [ ] 告警级别定义一致（P0/P1/P2/P3标准明确）
- [ ] 监控面板风格一致（布局、颜色、刷新频率）
- [ ] 运维文档与其他资产协调（与部署、测试阶段衔接）

**准确性验证 (Accuracy)**:
- [ ] 监控数据准确无误（无数据漂移、无采集错误）
- [ ] 告警阈值设置合理（基于历史数据和业务容忍度）
- [ ] SLO计算正确（Error Budget计算准确）
- [ ] 容量评估准确（基于真实负载和增长趋势）

**可执行性验证 (Executability)**:
- [ ] 告警响应流程清晰可执行（Runbook完整）
- [ ] 故障排查步骤明确（诊断手册可用）
- [ ] 扩容方案可行（资源充足、流程顺畅）
- [ ] 监控工具稳定可靠（无频繁故障）

**规范性验证 (Compliance)**:
- [ ] 遵循SRE最佳实践（Google SRE Book推荐做法）
- [ ] 符合行业标准（ITIL、ISO 27001等）
- [ ] 满足合规要求（数据保护、审计日志、隐私政策）
- [ ] 运维文档完整归档（便于查阅和审计）

## Handover Criteria

### 准出条件

```
✅ 监控系统已配置并正常运行（所有关键指标有数据）
✅ 告警规则已设置并测试（无频繁误报，通知渠道畅通）
✅ 运维手册已编写（常见场景处理流程完整）
✅ 应急预案已准备（P0/P1故障处理流程明确）
✅ SLO监控面板已就绪（实时显示SLO达成情况）
✅ 至少完成一次完整巡检（记录系统健康状态）
✅ Handover Context 已生成，所有必需字段完整
✅ 质量评分 ≥70分（基于KPIs计算）
```

### 交付物清单

| 交付物 | 格式 | 位置 | 版本 | 说明 |
|--------|------|------|------|------|
| 监控配置文件 | YAML/JSON | monitoring/configs/ | v1.0.0 | 监控采集和告警规则配置 |
| 监控面板定义 | JSON/Grafana Dashboard | monitoring/dashboards/ | v1.0.0 | Grafana或其他监控工具的面板配置 |
| 运维手册库 | Markdown | docs/runbooks/ | v1.0.0 | 常见场景处理流程（至少覆盖90%告警类型） |
| SLO监控面板 | URL/Dashboard Link | monitoring/slo-dashboard/ | v1.0.0 | SLO达成率实时监控和报告 |
| 告警路由配置 | YAML/JSON | monitoring/alert-routing/ | v1.0.0 | 告警通知渠道和升级策略 |
| 巡检报告模板 | Markdown | templates/inspection-report.template.md | v1.0.0 | 日常巡检报告模板 |
| 故障报告模板 | Markdown | templates/incident-report.template.md | v1.0.0 | 故障复盘报告模板 |

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "monitoring-operations"
    to_stage: "requirement-analysis" or "next-shift"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "stable/attention_required/alerting"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    monitoring_period: "{{start_time}} to {{end_time}}"
    
  artifacts:
    delivered:
      - name: "Monitoring Configuration"
        path: "monitoring/configs/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "Dashboard Definitions"
        path: "monitoring/dashboards/"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "Runbook Library"
        path: "docs/runbooks/"
        version: "1.0.0"
        runbook_count: {{number}}
      - name: "SLO Dashboard"
        path: "monitoring/slo-dashboard/"
        version: "1.0.0"
        url: "{dashboard_url}"
      - name: "Alert Routing Configuration"
        path: "monitoring/alert-routing/"
        version: "1.0.0"
        
  decisions:
    - id: "DC-002"
      description: "告警阈值设置"
      rationale: "基于历史数据和业务容忍度设置阈值，平衡敏感性和误报率"
      criteria_used: "P95响应时间<500ms，错误率<0.1%，CPU使用率<80%"
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "某非核心服务监控数据偶尔缺失，正在调查根因"
        severity: "P3"
        planned_fix: "下个迭代优化监控Agent配置"
        
  risks:
    - id: "RISK-001"
      description: "Error Budget剩余20%，按当前消耗速度预计15天后耗尽"
      probability: "medium"
      impact: "high"
      affected_areas: ["API响应时间", "数据库查询性能"]
      mitigation: "已启动性能优化项目，预计10天内完成"
      contingency_plan: "如Error Budget耗尽，暂停新功能发布，专注稳定性提升"
      
  recommendations:
    - "继续监控Error Budget消耗速度，每周review一次"
    - "优化告警规则，减少误报（当前误报率15%，目标<10%）"
    - "完善Runbook库，补充最近3次故障的处理流程"
    - "建议在下次迭代中增加业务指标监控（转化率、用户留存）"
    - "考虑引入AIOps工具，提升异常检测能力"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "MTTD"
        value: 3
        target: 5
        unit: "minutes"
        status: "pass"
        score: 100
      - kpi_id: "KPI-002"
        name: "MTTR"
        value: 25
        target: 30
        unit: "minutes"
        status: "pass"
        score: 100
      - kpi_id: "KPI-003"
        name: "ALERT-NOISE"
        value: 15
        target: 20
        unit: "%"
        status: "pass"
        score: 100
      - kpi_id: "KPI-004"
        name: "SLO-COMPLY"
        value: 99.7
        target: 99.5
        unit: "%"
        status: "pass"
        score: 100
        slo_details:
          availability: 99.9%
          latency_p95: 450ms (target: 500ms)
          error_rate: 0.05% (target: 0.1%)
          error_budget_remaining: 20%
    overall_score: 100
    grade: "excellent"
    recommendation: "continue_monitoring"
      
  next_steps:
    if_to_next_shift:
      - "继续关注Error Budget消耗速度"
      - "如有P0/P1告警，立即按Runbook处理"
      - "完成每日巡检并记录结果"
      - "交接班时口头沟通重点关注事项"
    if_to_requirement_analysis:
      - "基于监控数据识别性能瓶颈和优化机会"
      - "为新功能设计监控方案和SLO目标"
      - "评估当前架构的扩展性和可靠性"
      - "提出架构改进建议"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Agent | `../../agents/monitor-operate.agent.md` | 监控运维Agent角色定义 |
| Prompt | `../../prompts/monitor-operate.prompt.md` | 监控运维提示词模板 |
| Skill | `../../skills/monitor-operate/SKILL.md` | 监控运维技能包 |
| Instruction | `../../instructions/monitor-operate.instructions.md` | 监控运维技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [SRE Best Practices](../../standards/sre-best-practices.md) - SRE最佳实践指南
  - [Monitoring Standards](../../standards/monitoring-standards.md) - 监控配置标准
  - [Alerting Guidelines](../../standards/alerting-guidelines.md) - 告警配置指南
  - [Incident Management](../../standards/incident-management.md) - 事件管理标准
- **Templates**: 
  - [Runbook Template](../../templates/runbook.template.md) - 运维手册模板
  - [Incident Report Template](../../templates/incident-report.template.md) - 故障报告模板
  - [Post-Mortem Template](../../templates/post-mortem.template.md) - 事故复盘模板
  - [Inspection Report Template](../../templates/inspection-report.template.md) - 巡检报告模板
- **Evaluations**: 
  - [Monitoring Quality Checklist](../../evaluations/monitoring-quality-checklist.md) - 监控质量检查清单
  - [Alert Effectiveness Analysis](../../evaluations/alert-effectiveness.md) - 告警有效性分析
  - [SLO Compliance Report](../../evaluations/slo-compliance.md) - SLO合规报告

## Prerequisites

### 必需前置条件

1. ✅ 系统已部署上线 (deploy-release 场景输出)
2. ✅ 具备监控工具（Prometheus、Grafana、ELK等）
3. ✅ 明确SLO指标（可用性、延迟、错误率目标）
4. ✅ 监控网络已打通（Agent能上报数据）
5. ✅ 告警通知渠道已配置（Slack、邮件、短信等）
6. ✅ On-Call值班安排已确定

### 期望输入

| Input Variable | Type | Required | Default | Description | Validation |
|----------------|------|----------|---------|-------------|------------|
| `system_info` | object | true | - | 系统信息 | 包含架构、组件、依赖服务 |
| `slo_targets` | object | true | - | SLO目标 | 包含可用性、延迟、错误率目标 |
| `monitoring_tools` | array | true | - | 监控工具列表 | Prometheus、Grafana、ELK等 |
| `alert_channels` | array | true | - | 告警渠道 | Slack、邮件、短信、电话 |
| `oncall_schedule` | object | false | {} | 值班安排 | 主值班、备值班、轮换规则 |
| `historical_incidents` | array | false | [] | 历史故障记录 | 用于优化监控和告警规则 |
| `baseline_metrics` | object | false | {} | 基线指标 | 正常状态下的指标范围 |
