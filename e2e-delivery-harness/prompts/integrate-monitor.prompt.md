---
name: integrate-monitor
description: "integrate monitor execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 监控集成 (Integrate Monitor)

## Purpose

本提示词指导AI执行监控集成任务，作为 **SRE Engineer (站点可靠性工程师)**，负责监控系统的规划、集成和维护，确保服务可观测性全面覆盖、告警准确有效。

### Key Objectives

- **全面指标覆盖**: 对核心服务实现RED/USE指标体系全覆盖，指标覆盖率≥95%
- **精准告警**: 配置高精度告警规则，告警准确率≥80%，减少误报
- **完整面板**: 搭建覆盖SLO、服务、资源、业务四个维度的监控面板，完成度=100%
- **SLO全追踪**: 对所有定义的服务SLO实现实时跟踪和可视化，跟踪率=100%

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Description | Validation |
|----------|------|----------|-------------|------------|
| `target_services` | array | true | 目标服务列表（服务名、类型、关键程度） | 非空，每个服务包含name和criticality字段 |
| `metric_types` | array | true | 需要采集的指标类型（RED/USE/业务指标） | 至少包含Rate/Errors/Duration核心指标 |
| `log_sources` | array | true | 日志来源列表（服务日志、系统日志、审计日志） | 非空，每个来源包含path和format |
| `trace_config` | object | false | 链路追踪配置（采样率、传播协议、后端地址） | 包含sampling_rate和protocol字段 |
| `alerting_channels` | array | true | 告警通知渠道（email/slack/pagerduty/webhook） | 至少1个渠道，每个含type和endpoint |
| `slo_definitions` | array | true | SLO定义列表（指标、目标值、时间窗口） | 每个SLO包含indicator、target和window |
| `dashboard_requirements` | array | false | 面板需求（业务视角/技术视角/管理层视角） | 包含view_type和target_audience描述 |

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解监控需求和可观测性目标
   ├─ 输入: target_services, metric_types, slo_definitions, dashboard_requirements
   ├─ 思考: 哪些服务是关键业务路径？需要采集哪些指标？SLO目标是什么？
   ├─ 验证: 确认理解了所有服务的重要性和监控优先级
   └─ 输出: 监控需求分析（服务重要度矩阵、指标需求清单、SLO目标汇总）
   ↓
[ANALYZE] Step 2: 分析监控架构和技术选型
   ├─ 输入: 监控需求分析, log_sources, trace_config
   ├─ 思考: 合适的监控栈是什么？指标采集方案如何设计？日志和Trace如何关联？
   ├─ 验证: 技术选型满足可观测性三大支柱（指标/日志/Trace）覆盖
   └─ 输出: 监控架构方案（组件拓扑、数据流设计、技术选型决策）
   ↓
[INSTRUMENT] Step 3: 实施监控埋点和数据采集
   ├─ 输入: 监控架构方案, target_services
   ├─ 执行:
   │   ├─ 指标埋点: 集成Prometheus SDK/StatsD/OpenTelemetry，实现RED+USE指标
   │   ├─ 日志采集: 配置日志收集Agent（Fluentd/Logstash），结构化日志格式
   │   ├─ 链路追踪: 集成OpenTelemetry/Jaeger，配置采样率和Trace传播
   │   └─ 业务指标: 埋点采集业务KPI（GMV/DAU/转化率等自定义指标）
   ├─ 验证: 指标覆盖率≥95%，所有目标服务已埋点
   └─ 输出: 埋点代码 + 采集配置 + 指标清单 + 数据验证报告
   ↓
[CONFIGURE] Step 4: 配置告警规则和通知策略
   ├─ 输入: slo_definitions, alerting_channels, 指标清单
   ├─ 执行:
   │   ├─ 告警规则: 基于阈值/变化率/复合条件配置告警（Critical/Warning/Info层级）
   │   ├─ 告警抑制: 配置告警聚合、静默规则、依赖告警抑制
   │   ├─ 通知路由: 根据严重级别配置通知渠道和升级策略
   │   └─ 告警验证: 触发测试告警验证通知可达和准确性
   ├─ 验证: 告警准确率≥80%，所有SLO违规可被告警捕获
   └─ 输出: 告警规则配置 + 通知路由表 + 告警测试报告
   ↓
[VISUALIZE] Step 5: 搭建监控面板和SLO仪表盘
   ├─ 输入: 指标清单, slo_definitions, dashboard_requirements
   ├─ 执行:
   │   ├─ 面板设计: 概览面板（SLO状态）、服务面板（性能指标）、资源面板（系统资源）、业务面板（业务指标）
   │   ├─ 可视化配置: 图表类型选择、布局设计、变量配置、时间范围
   │   └─ SLO仪表盘: 实时SLO状态、错误预算消耗、剩余时间预测
   ├─ 验证: 面板完成度=100%，SLO跟踪率=100%
   └─ 输出: 面板配置导出 + 面板URL列表 + 使用指南
   ↓
[VALIDATE] Step 6: 验证监控体系完整性和有效性
   ├─ 输入: 面板配置, 告警规则, 埋点数据
   ├─ 执行:
   │   ├─ 覆盖验证: 检查指标覆盖率、日志覆盖率、Trace覆盖率
   │   ├─ 告警验证: 模拟故障验证告警触发和通知准确
   │   ├─ 面板验证: 确认所有面板数据正常加载
   │   └─ SLO验证: 确认SLO计算正确，错误预算消耗可视化
   ├─ 验证: 指标覆盖率≥95%、告警准确率≥80%、面板完成度=100%、SLO跟踪率=100%
   └─ 输出: 监控体系验证报告 + 交接文档
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 指标数据丢失或采集失败

**识别信号**: 
- 预期指标在Grafana/Prometheus中无数据显示
- 采集端点返回错误或超时
- 指标数据出现断点或间隙
- 采集日志显示连接失败

**处理流程**:
```
IF 指标数据丢失
THEN
  1. 检查采集Agent/Exporter的运行状态
  2. 确认网络连通性和端口可达性
  3. 验证采集配置（端点URL、认证信息、采集间隔）
  4. 检查服务端存储容量和写入速率限制
  5. IF Agent故障 THEN
       a. 重启采集Agent
       b. 检查Agent版本兼容性
       c. 更新Agent配置
     ELSE IF 网络问题 THEN
       a. 检查防火墙规则和安全组
       b. 验证DNS解析
       c. 测试端到端连接
     END
  6. 验证数据恢复后无永久性丢失
END
```

**降级方案**: 启用本地缓存暂存指标数据，待采集通道恢复后批量上报

**升级条件**: 核心服务（标为critical的服务）指标连续丢失超过5分钟

---

### Error Scenario 2: 告警误报频繁

**识别信号**: 
- 告警频繁触发但实际无故障
- 同一指标的告警在短时间内反复触发/恢复
- 业务高峰期正常波动被误判为异常
- 告警疲劳导致团队忽视真实告警

**处理流程**:
```
IF 告警误报频繁
THEN
  1. 分析误报告警的模式和规律
  2. 识别根本原因：
       a. 阈值过于敏感（正常波动触发）
       b. 缺少足够的持续评估时间
       c. 缺乏基线或季节性调整
       d. 采集数据存在抖动
     END
  3. 调整告警配置：
       a. 调整阈值（基于历史数据百分位数）
       b. 增加评估持续时间（for: 5m → 10m）
       c. 配置季节性基线（业务高低峰不同阈值）
       d. 添加复合条件减少误报
     END
  4. 设置告警抑制规则，避免告警风暴
  5. 验证调整后的告警准确率≥80%
  6. 记录告警优化历史
END
```

**降级方案**: 暂时将误报告警调整为WARNING级别，持续优化阈值后再恢复CRITICAL

**升级条件**: 告警误报导致关键告警被淹没，或PagerDuty轮值人员产生告警疲劳

---

### Error Scenario 3: 采集性能开销过高

**识别信号**: 
- 采集Agent CPU/内存占用超过10%
- 应用响应时间因埋点增加超过5%
- 日志采集导致磁盘IO成为瓶颈
- 网络出口带宽因指标上报耗尽

**处理流程**:
```
IF 采集开销过高
THEN
  1. 分析当前采集配置的资源消耗分布
  2. 定位开销最高的采集点
  3. 执行优化措施：
       a. 降低高频指标的采集频率（10s → 30s）
       b. 减少不必要的指标维度（Label基数优化）
       c. 调整Trace采样率（100% → 1-10%）
       d. 使用聚合指标替代原始指标
       e. 启用日志采样或只采集WARN/ERROR级别
     END
  4. 验证优化后性能开销可接受（应用RT增加≤5%）
  5. 记录优化决策和权衡
END
```

**降级方案**: 关闭非关键服务的详细指标采集，仅保留RED核心指标

**升级条件**: 采集开销导致应用SLO违规或生产事故，需立即回滚采集配置

## Quality Score (质量评分)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 权重 | 计算公式 | 验证方法 |
|--------|----------|--------|------|----------|----------|
| KPI-001 | METRIC-COVERAGE | ≥95% | 30% | (已采集指标的服务数 / 应采集指标的服务数) × 100% | 对比目标服务指标清单与已采集指标清单 |
| KPI-002 | ALERT-PRECISION | ≥80% | 25% | (真实告警数 / 总告警触发数) × 100% | 统计告警记录中真实事件的比例 |
| KPI-003 | DASHBOARD-COMPLETE | =100% | 25% | (已完成面板数 / 计划面板数) × 100% | 面板需求清单对照验证 |
| KPI-004 | SLO-TRACKING | =100% | 20% | (已实现SLO跟踪数 / 总SLO定义数) × 100% | 逐一核对SLO定义在仪表盘中的可视化 |

**综合评分计算**:
```
Quality Score = (METRIC-COVERAGE_SCORE × 0.30) + (ALERT-PRECISION_SCORE × 0.25) + (DASHBOARD-SCORE × 0.25) + (SLO-TRACKING_SCORE × 0.20)

METRIC-COVERAGE_SCORE = min(100, actual_coverage / 95% × 100)
ALERT-PRECISION_SCORE = min(100, actual_precision / 80% × 100)
DASHBOARD-SCORE       = IF complete = 100% THEN 100 ELSE actual_completion_rate
SLO-TRACKING_SCORE    = IF tracking = 100% THEN 100 ELSE actual_tracking_rate

合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Validation (输出验证)

> **AI 在提交监控交付物前，必须完成以下验证步骤**

### Monitoring Validation Checklist

**V-001: Metric Coverage Validation (指标覆盖验证)**
- [ ] All target services have RED metrics implemented (Rate/Errors/Duration)
- [ ] All infrastructure resources have USE metrics implemented (Utilization/Saturation/Errors)
- [ ] Custom business metrics are implemented as specified
- [ ] Metric naming follows the standardized convention
- [ ] Metric labels/cardinality is controlled (≤ 1000 unique label combinations)
- [ ] Metric coverage rate ≥ 95% confirmed

**V-002: Log Collection Validation (日志采集验证)**
- [ ] All specified log sources are configured for collection
- [ ] Logs are structured (JSON) with consistent schema
- [ ] Log levels (DEBUG/INFO/WARN/ERROR) are correctly captured
- [ ] Log retention policy is configured per requirements
- [ ] Log shipping latency is within acceptable limits (≤ 60s)
- [ ] Audit logs are collected separately (if required)

**V-003: Alerting Validation (告警验证)**
- [ ] All SLO definitions have corresponding alerting rules
- [ ] Alert severity levels (Critical/Warning/Info) are correctly mapped
- [ ] Alert evaluation period and conditions are properly configured
- [ ] Notification channels are correctly routing by severity
- [ ] Alert deduplication and grouping are configured
- [ ] Test alerts have been triggered and confirmed delivered
- [ ] Alert precision rate ≥ 80% verified

**V-004: Dashboard Validation (面板验证)**
- [ ] All required dashboards are created (Overview/Service/Resource/Business)
- [ ] SLO tracking dashboard shows real-time status for all defined SLOs
- [ ] All graphs and charts display data correctly (no empty panels)
- [ ] Time range selector and template variables work correctly
- [ ] Dashboard permissions are set correctly for target audience
- [ ] Dashboard exports are saved as JSON/PDF

**V-005: Trace & SLO Validation (链路与SLO验证)**
- [ ] Distributed tracing is integrated (OpenTelemetry/Jaeger)
- [ ] Trace sampling rate is configured appropriately (1-10% for prod)
- [ ] Trace context propagation is working across service boundaries
- [ ] SLO error budget calculation is correct
- [ ] SLO burn rate alerts are configured
- [ ] SLO tracking rate = 100% confirmed

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. Identify specific failed items and impact severity
  2. IF metric coverage (V-001) fails THEN add missing instrumentation
  3. IF alerting (V-003) fails THEN adjust rules and re-test
  4. IF dashboard (V-004) or SLO (V-005) fails THEN fix before handover
  5. Generate validation report with pass/fail status for each check
  6. Document pending items and remediation timeline
END
```

## Execution Flow (执行流程)

> **领域特定的监控集成执行流程**

### Phase 1: 监控体系规划 (Monitoring Architecture Planning)

**目标**: 设计完整的监控架构和指标体系

1. **指标识别（RED + USE方法）**
   - RED（面向服务）: Rate（请求率）、Errors（错误率）、Duration（延迟）
   - USE（面向资源）: Utilization（利用率）、Saturation（饱和度）、Errors（错误）
   - 业务指标: 根据业务需求定义自定义指标

2. **指标层次设计**
   - 基础设施层: CPU、Memory、Disk、Network（USE方法）
   - 应用层: QPS、Latency、Error Rate、Apdex（RED方法）
   - 业务层: GMV、DAU、Conversion Rate、User Retention

3. **采集策略规划**
   - 指标采集频率（高/中/低频分类）
   - 数据保留周期（热/温/冷数据分层）
   - 聚合和降采样策略

4. **监控栈选型**
   - 指标存储: Prometheus/Thanos/VictoriaMetrics
   - 日志平台: ELK/Loki/CloudWatch Logs
   - 链路追踪: Jaeger/Tempo/X-Ray
   - 可视化: Grafana/Kibana

**输出**: 监控架构设计方案 + 指标清单 + 监控栈部署计划

### Phase 2: 埋点与配置实施 (Instrumentation & Configuration)

**目标**: 在服务和基础设施中实施监控埋点和配置

1. **SDK集成和指标埋点**
   - 选择合适的客户端库（Prometheus SDK/OpenTelemetry）
   - HTTP请求埋点（请求量、延迟、状态码分布）
   - 数据库操作埋点（查询时间、连接池状态）
   - 外部依赖调用埋点（下游服务响应时间、错误率）
   - 自定义业务指标埋点

2. **日志采集配置**
   - 配置日志采集Agent（Fluentd/Logstash/Vector）
   - 定义结构化日志格式（JSON schema）
   - 配置日志源和过滤规则
   - 设置日志存储和保留策略

3. **链路追踪集成**
   - 集成OpenTelemetry SDK
   - 配置采样策略（基于头的概率采样）
   - 传播Trace Context（W3C TraceContext格式）
   - 配置Trace到Metrics的关联

4. **告警规则配置**
   - 定义告警规则（基于阈值/趋势/复合条件）
   - 配置多级告警（Critical/Warning/Info）
   - 设置告警路由和通知渠道
   - 配置告警抑制和静默规则

**输出**: 埋点代码 + 采集配置 + 告警规则 + 部署验证

### Phase 3: 可视化与SLO追踪 (Visualization & SLO Tracking)

**目标**: 搭建监控面板，实现SLO全追踪

1. **监控面板搭建**
   - 概览面板: 全局SLO状态、服务健康度、告警汇总
   - 服务面板: 服务RED指标、依赖拓扑、错误详情
   - 资源面板: 资源利用率、饱和度、容量规划
   - 业务面板: 业务KPI趋势、用户行为分析

2. **SLO仪表盘配置**
   - 定义SLO指标和计算方式（SLI指标 → SLO目标）
   - 配置错误预算计算和可视化
   - 配置SLO燃烧速率告警
   - 设置SLO仪表盘的多时间窗口视图

3. **面板验证和优化**
   - 验证所有面板数据源连接正常
   - 确认图表类型和布局合理
   - 优化面板加载性能
   - 导出面板配置JSON备份

**输出**: 面板配置 + SLO仪表盘 + 使用指南 + 导出备份

## Output Format (输出格式)

> AI必须按照以下结构化模板生成监控交付物

```markdown
# Monitoring Integration Deliverables

## 1. Monitoring Architecture

### 1.1 Architecture Overview
- **Metrics Stack**: {prometheus/thanos/victoriametrics}
- **Log Stack**: {elk/loki/cloudwatch}
- **Tracing**: {jaeger/tempo/x-ray}
- **Visualization**: {grafana/kibana}
- **Alerting**: {alertmanager/pagerduty/opsgenie}

### 1.2 Component Topology
```
{architecture_diagram_text}
```

### 1.3 Data Flow
| Data Type | Source | Collection Agent | Storage | Retention |
|-----------|--------|-----------------|---------|-----------|
| Metrics | {service} | {exporter/sdk} | {storage} | {period} |
| Logs | {service} | {agent} | {storage} | {period} |
| Traces | {service} | {sdk} | {storage} | {period} |

## 2. Service Instrumentation

### 2.1 Target Services
| Service | Criticality | RED Metrics | Logs | Tracing | Status |
|---------|-------------|-------------|------|---------|--------|
| {service} | Critical/Standard | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

### 2.2 Metric Coverage
- **Total Services**: {N}
- **Instrumented Services**: {N}
- **Metric Coverage**: {X}% (Target: ≥95%)

### 2.3 Key Metrics Summary
| Metric | Type | Service | Collection | Interval |
|--------|------|---------|------------|----------|
| {metric} | Counter/Gauge | {service} | {sdk/exporter} | {interval} |

## 3. Alerting Configuration

### 3.1 Alert Rules
| Alert Name | Severity | Condition | Duration | Channel |
|------------|----------|-----------|----------|---------|
| {alert_name} | Critical/Warning/Info | {expr} | {duration} | {channel} |

### 3.2 Alert Precision
- **Total Alerts Triggered (Test)**: {N}
- **True Positives**: {N}
- **False Positives**: {N}
- **Alert Precision**: {X}% (Target: ≥80%)

## 4. Dashboards

### 4.1 Dashboard Overview
| Dashboard Name | Type | Panels | Data Source | URL |
|----------------|------|--------|-------------|-----|
| SLO Overview | Business | {N} | {source} | {url} |
| Service Health | Service | {N} | {source} | {url} |
| Resource Monitor | Resource | {N} | {source} | {url} |
| Business Metrics | Business | {N} | {source} | {url} |

### 4.2 SLO Tracking
| SLO ID | SLI | Target | Current | Error Budget | Status |
|--------|-----|--------|---------|--------------|--------|
| {slo_id} | {indicator} | {target} | {current} | {remaining} | ✅/⚠️/❌ |

### 4.3 Dashboard Completeness
- **Planned Dashboards**: {N}
- **Completed Dashboards**: {N}
- **Completeness**: {X}% (Target: 100%)

## 5. Quality Score

### 5.1 KPI Results
| KPI ID | Metric | Target | Actual | Score | Weight | Weighted |
|--------|--------|--------|--------|-------|--------|----------|
| KPI-001 | METRIC-COVERAGE | ≥95% | {X}% | {S} | 30% | {W} |
| KPI-002 | ALERT-PRECISION | ≥80% | {X}% | {S} | 25% | {W} |
| KPI-003 | DASHBOARD-COMPLETE | =100% | {X}% | {S} | 25% | {W} |
| KPI-004 | SLO-TRACKING | =100% | {X}% | {S} | 20% | {W} |

### 5.2 Overall Score
- **Total Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)

## 6. Handover Information

### 6.1 Access Information
- **Grafana**: {url} | **Prometheus**: {url} | **Alertmanager**: {url} | **Trace UI**: {url}

### 6.2 Operations Runbook
- **Alert Response**: {link} | **Dashboard Guide**: {link} | **Monitoring FAQ**: {link}

### 6.3 Known Issues
| Issue | Impact | Workaround | Resolution |
|-------|--------|------------|------------|
| {issue} | {impact} | {workaround} | {plan} |
```

## Handover Context (交接上下文)

> 完成监控集成后，生成以下交接信息

```yaml
handover:
  header: {from_stage: "monitoring", to_stage: "operations", handover_id: "HO-{timestamp}-{sequence}", timestamp: "{ISO8601}", prepared_by: "{agent.name}"}

  summary: {status: "completed/partial/blocked", metric_coverage: {X}%, alert_precision: {X}%, dashboard_complete: {X}%, slo_tracking: {X}%}

  artifacts:
    - name: "Instrumentation Code"
      path: "monitoring/instrumentation/"
      includes: ["SDK configs", "metric definitions", "trace setup"]
    - name: "Alerting Rules"
      path: "monitoring/alerts/"
      includes: ["alert rules YAML", "notification configs"]
    - name: "Dashboard Exports"
      path: "monitoring/dashboards/"
      includes: ["Grafana JSON exports"]
    - name: "Integration Guide"
      path: "docs/monitoring-guide.md"
      includes: ["Setup instructions", "runbooks", "FAQ"]

  endpoints:
    grafana: "{url}"
    prometheus: "{url}"
    traces: "{url}"

  slo_status:
    - slo_id: "{slo_id}"
      indicator: "{indicator}"
      status: "on_track/at_risk/violated"

  next_steps:
    - "Validate alerting with simulated failure scenarios"
    - "Train operations team on dashboard usage"

  quality_metrics:
    kpi_results:
      - {kpi: "KPI-001 METRIC-COVERAGE", value: {X}, target: 95, unit: "%", status: "pass/fail"}
      - {kpi: "KPI-002 ALERT-PRECISION", value: {X}, target: 80, unit: "%", status: "pass/fail"}
      - {kpi: "KPI-003 DASHBOARD-COMPLETE", value: {X}, target: 100, unit: "%", status: "pass/fail"}
      - {kpi: "KPI-004 SLO-TRACKING", value: {X}, target: 100, unit: "%", status: "pass/fail"}
    overall_score: {0-100}
    grade: "excellent/good/satisfactory/needs_improvement"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/integrate-monitor/SCENARIO.md` | 监控集成场景定义 |
| Agent | `../agents/integrate-monitor.agent.md` | 监控Agent角色 |
| Skill | `../skills/integrate-monitor/SKILL.md` | 监控技能包 |
| Instruction | `../instructions/integrate-monitor.instructions.md` | 监控技术指令 |

## Related Resources (相关资源)

- **Standards**:
  - [RED Method Guide](../standards/red-method-guide.md) - RED指标方法指南
  - [SLO Framework](../standards/slo-framework.md) - SLO框架
  - [Alerting Best Practices](../standards/alerting-best-practices.md) - 告警最佳实践
- **Templates**:
  - [Dashboard Template](../templates/grafana-dashboard.template.json) - Grafana面板模板
  - [Alert Rule Template](../templates/prometheus-alert.template.yml) - 告警规则模板

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。
