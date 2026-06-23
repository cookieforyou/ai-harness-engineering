---
name: alerting-guidelines
type: standard
version: "2.0.0"
status: active
---

# 告警规范

> 本规范定义 E2E Delivery Harness 中所有告警的路由、分级、通知策略与疲劳预防。审查基准见 [harness-engineering.md](harness-engineering.md)。告警严重级别定义见 [monitoring-standards.md](monitoring-standards.md)。

## 1. 告警规则设计原则

### 1.1 RED 原则

告警规则应遵循 **RED** (Rate / Errors / Duration) 模型：

| 信号 | 告警条件示例 | 建议阈值 |
|------|-------------|----------|
| **Rate (流量)** | 请求量突然归零或陡降 > 50% | 同比/环比 (same period) |
| **Errors (错误)** | 错误率超过基线 + 绝对值 > N | 基线 + 3σ 或 0.1% |
| **Duration (延迟)** | P99 延迟超过 SLO 阈值 | SLO × 1.5 |

### 1.2 告警公式

```
alert = metric_problem × (user_impact + business_impact) ≥ threshold
```

- **metric_problem**: 指标偏离基线的程度
- **user_impact**: 受影响用户比例
- **business_impact**: 业务收入/体验影响

不是所有指标异常都需要告警 — 只对用户或业务有可感知影响时才触发。

## 2. 告警路由规则 (Alert Routing)

### 2.1 路由矩阵

| 告警级别 | 通知方式 | 目标人群 | 响应 SLA |
|----------|----------|----------|----------|
| **P0** | 电话 + Slack @channel + PagerDuty | On-call 一级工程师 + Incident Commander | ≤ 5 分钟 |
| **P1** | Slack @here + PagerDuty 推送 | On-call 工程师 + 技术负责人 | ≤ 15 分钟 |
| **P2** | Slack channel 告警 | 服务团队 | ≤ 1 小时 |
| **P3** | Slack channel（可选静音） | 服务团队（工作时段） | 下一工作日 |
| **Notification** | 邮件 / Dashboard badge | 所有干系人 | N/A |

### 2.2 On-call 轮换

| 轮换类型 | 周期 | 人数 | 交接方式 |
|----------|------|------|----------|
| **Primary (一级)** | 1 周 | 1 人 | 每周一 10:00 交接会议 |
| **Secondary (二级)** | 1 周 | 1 人 | 同时轮换 |
| **Escalation (升级)** | 1 周 | Team Lead | 自动升级 |

**规则**:
- Primary 响应超时 → 自动升级到 Secondary
- Secondary 响应超时 → 自动升级到 Team Lead
- 同一人连续 on-call ≤ 2 周
- On-call 工程师在该周内不安排重要发布任务

### 2.3 静默期 (Silencing) 与零值告警

- 维护窗口期告警自动静默（需创建 maintenance window）
- P3 及以下告警在 22:00 - 07:00 静默（除非 P0/P1 升级路径触发）
- 零值指标（如 `error_total == 0`）不应产生告警 — 使用 `absent()` 检测指标缺失

## 3. 告警疲劳预防 (Alert Fatigue Prevention)

### 3.1 告警量控制目标

| 指标 | 目标 | 警告线 |
|------|------|--------|
| 每日告警总数 | ≤ 20 | ≥ 50 |
| 每日 P0 告警数 | ≤ 1 | ≥ 3 |
| 每日 P1 告警数 | ≤ 5 | ≥ 10 |
| 告警 - 事件转化率 | ≥ 30% | < 10%（太多无用的告警） |
| MTTA (平均响应时间) | ≤ 5 min (P0) | > 15 min |
| MTTR (平均修复时间) | ≤ 30 min (P0) | > 60 min |

### 3.2 告警规则自查清单

每个告警规则创建前应回答：

- [ ] 此告警是否有明确的行动指南 (Runbook)？
- [ ] 收到此告警，工程师具体要做什么操作？
- [ ] 如果什么也不做，会有什么后果？
- [ ] 这个告警可以自动化解决吗？（如果可以，先做自动化）
- [ ] 是否配置了合理的持续时长 (for: 5m) 避免抖动？
- [ ] 是否有类似的告警规则导致重复告警？

### 3.3 告警分组与聚合

| 策略 | 说明 | 示例 |
|------|------|------|
| **Group By** | 按特定标签聚合同一事件 | `group_by: ['service', 'error_type']` |
| **Rate Limit** | 限制同一告警的发送频率 | `rate_limit: 1/h` |
| **Group Interval** | 合并窗口内同类告警 | `group_interval: 5m` |
| **Repeat Interval** | 未解决的告警重复通知间隔 | `repeat_interval: 4h` |

### 3.4 反模式

- ❌ 为每一个指标创建告警规则（造成告警风暴）
- ❌ 使用固定阈值而不考虑基线变化（应结合动态阈值或同比）
- ❌ 告警内容不包含上下文（需要工程师登录服务器查看）
- ❌ 没有 Runbook 的告警（"这是什么错误？"）
- ❌ 告警-告警依赖（A 告警导致连锁告警 B、C、D）

## 4. 告警内容规范 (Notification Content)

### 4.1 告警消息模板

```
[P0] 支付服务 - 错误率超过 5%
服务: payment-api (v2.1.3)
环境: production
指标: error_rate = 7.2% (基线: 0.5%)
持续时间: 5 分钟 (since 10:25 UTC)
受影响: 约 3,200 请求受影响
Runbook: https://runbook.internal/alerts/payment-high-error-rate
Dashboard: https://grafana.internal/d/payment-overview
标签: severity=critical, team=payment, incident_id=INC-2026-0421
```

### 4.2 告警必含字段

- 标题：`[级别] 服务名 - 告警内容摘要`
- 服务名 + 版本号
- 环境（production/staging/dev）
- 当前值 + 阈值 + 基线值
- 持续时长
- 受影响的业务纬度（用户数/请求量/交易金额）
- Runbook 链接
- Dashboard 链接
- 标签用于过滤和路由

## 5. 告警规则模板 (Alert Rule Templates)

### 5.1 高错误率告警

```yaml
# PrometheusRule 示例
name: HighErrorRate
expr: |
  sum(rate(http_requests_total{status=~"5..", environment="production"}[5m]))
  /
  sum(rate(http_requests_total{environment="production"}[5m]))
  > 0.01
for: 5m
labels:
  severity: p1
  team: "{{ $labels.service }}"
annotations:
  summary: "{{ $labels.service }} 错误率超过 1%"
  description: "当前值: {{ $value | humanizePercentage }}，持续 5 分钟"
```

### 5.2 延迟告警

```yaml
name: HighLatency
expr: |
  histogram_quantile(0.99,
    sum(rate(http_request_duration_seconds_bucket{environment="production"}[5m]))
      by (le, service)
  ) > 0.5
for: 10m
labels:
  severity: p1
annotations:
  summary: "{{ $labels.service }} P99 延迟超过 500ms"
```

### 5.3 实例宕机告警

```yaml
name: InstanceDown
expr: up{environment="production", job="harness-services"} == 0
for: 1m
labels:
  severity: p0
annotations:
  summary: "{{ $labels.instance }} 不可达"
```

### 5.4 证书即将过期

```yaml
name: TLSCertExpiring
expr: probe_ssl_earliest_cert_expiry - time() < 86400 * 14  # 14 days
for: 0m
labels:
  severity: p2
```

## 6. 告警测试与验证

- **单元测试**: 使用 `promtool test rules` 验证告警规则语法
- **集成测试**: 在 staging 环境注入故障，验证告警触发 + 通知
- **定期演练**: 每月一次告警响应演练 (Tabletop Exercise)
- **告警规则审查**: 每季度审查一次告警规则，清除不再需要的规则

## 引用

- [asset-model.md](asset-model.md)
- [authoring-checklist.md](authoring-checklist.md)
- [monitoring-standards.md](monitoring-standards.md)
- [incident-management.md](incident-management.md)
- [sre-best-practices.md](sre-best-practices.md)
