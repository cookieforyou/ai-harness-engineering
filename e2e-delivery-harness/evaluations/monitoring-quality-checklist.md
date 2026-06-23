---
name: monitoring-quality-checklist
type: evaluation
version: "1.0.0"
status: active
updated: 2026-06-23
---

# 监控质量检查清单 (Monitoring Quality Checklist)

## Purpose

本清单用于评估监控运维体系的质量，覆盖告警配置、仪表盘完整性、SLO 覆盖和 Runbook 完备度四个维度。确保系统可观测性满足运维需求。

## Scoring

- **PASS**: 完全满足要求
- **PARTIAL**: 大部分满足，少量可接受偏差
- **FAIL**: 不满足要求，必须补充
- **NA**: 不适用

## 使用时机

- 新服务上线前的监控就绪检查
- 定期监控质量审计（建议每季度一次）
- 重大架构变更后监控覆盖度评估

---

## 1. 告警配置 (Alert Configuration)

- [ ] **ALR-001**: 所有关键指标已配置告警规则，无"静默故障"风险（未监控的关键路径）
- [ ] **ALR-002**: 告警阈值基于基线数据设定（非随意取值），误报率 ≤ 5%（即每 100 次告警中真阳性 ≥ 95）
- [ ] **ALR-003**: 告警分级清晰：P0（页面不可用）→ 即时电话通知，P1（功能受损）→ 5 分钟内 IM 通知，P2（非关键异常）→ 工作时间内通知
- [ ] **ALR-004**: 告警通知渠道已配置并验证（电话/Slack/钉钉/PagerDuty，至少两个渠道避免单点失效）
- [ ] **ALR-005**: 告警聚合/防重复策略已配置（相同告警在 30 分钟内最多发送 3 次，避免告警风暴）
- [ ] **ALR-006**: 无长期静默（snoozed）且未解决的告警，所有静默规则有到期时间

## 2. 仪表盘完备性 (Dashboard Completeness)

- [ ] **DSH-001**: 存在服务级仪表盘，展示 USE 指标（Utilization/Saturation/Errors）：CPU、内存、磁盘、网络、连接数
- [ ] **DSH-002**: 存在业务级仪表盘，展示 RED 指标（Rate/Errors/Duration）：请求量、错误率、延迟分布（P50/P95/P99）
- [ ] **DSH-003**: 存在依赖服务仪表盘：下游依赖的健康状态、调用量、响应时间、错误率
- [ ] **DSH-004**: 仪表盘加载时间 ≤ 5 秒，时间范围选择器工作正常，数据刷新间隔 ≤ 1 分钟
- [ ] **DSH-005**: 关键维度可下钻（按地域/版本/实例/错误码），支持从仪表盘直接跳转到日志查询
- [ ] **DSH-006**: 仪表盘通过版本管理（Grafana JSON 模型存储在 Git 仓库中），变更可追溯

## 3. SLO 覆盖 (SLO Coverage)

- [ ] **SLO-001**: 服务级别指标（SLI）已定义：可用性、延迟、吞吐量、错误率，至少覆盖 3 个维度
- [ ] **SLO-002**: 服务级别目标（SLO）已设定且可达成（基于历史数据设定，接 ≥ 99% 可用性为目标）
- [ ] **SLO-003**: SLO 燃烧率告警已配置：15 分钟快速燃烧、1 小时中等燃烧、6 小时慢速燃烧告警
- [ ] **SLO-004**: 错误预算（Error Budget）可实时查看，消耗速度有趋势预警
- [ ] **SLO-005**: SLO 达成率月度报告已产出，未达成时有改进行动计划

## 4. Runbook 质量 (Runbook Quality)

- [ ] **RNB-001**: 所有 P0/P1 告警均有对应 Runbook，覆盖率 100%
- [ ] **RNB-002**: Runbook 包含：告警含义、排查步骤（含预期输出）、修复操作命令、升级联系人
- [ ] **RNB-003**: Runbook 每季度至少演练一次（GameDay/桌面推演），演练记录可查
- [ ] **RNB-004**: Runbook 存储在版本控制中，与实际系统配置保持同步（变更触发 Runbook 更新）
- [ ] **RNB-005**: Runbook 搜索可在 30 秒内定位到对应文档（按告警名/服务名/故障类型可检索）

## 5. 日志与追踪 (Logging & Tracing)

- [ ] **LOG-001**: 应用日志结构化（JSON 格式），包含：timestamp、level、service、trace_id、message 等标准字段
- [ ] **LOG-002**: 分布式追踪已接入（OpenTelemetry/Jaeger/Zipkin），端到端请求链路可追踪
- [ ] **LOG-003**: 日志保留策略符合合规要求（至少 30 天在线，12 个月归档），日志存储容量有监控
- [ ] **LOG-004**: 日志查询可在 10 秒内返回结果（按 trace_id/request_id），支持全文检索和结构化过滤

---

## Summary

| 维度 | PASS | PARTIAL | FAIL | 通过率 |
|------|------|---------|------|--------|
| 告警配置 | __ | __ | __ | __% |
| 仪表盘完备性 | __ | __ | __ | __% |
| SLO 覆盖 | __ | __ | __ | __% |
| Runbook 质量 | __ | __ | __ | __% |
| 日志与追踪 | __ | __ | __ | __% |
| **总计** | **__** | **__** | **__** | **__%** |

### 判定标准

| 通过率 | 结果 |
|--------|------|
| ≥ 90% | PASS - 监控体系健康 |
| 75-89% | PARTIAL - 需补充缺失项 |
| < 75% | FAIL - 监控存在重大缺口，暂不可交付 |

### 关键缺口

| # | 维度 | 问题 | 优先级 | 负责人 |
|---|------|------|--------|--------|
| 1 | | | P0/P1/P2 | |
| 2 | | | P0/P1/P2 | |

---

## References

- [regression-checklist.md](regression-checklist.md)
- [alert-effectiveness.md](alert-effectiveness.md)
- [slo-compliance.md](slo-compliance.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)
