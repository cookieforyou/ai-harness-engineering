---
name: alert-effectiveness
type: evaluation
version: "1.1.0"
status: active
updated: 2026-06-23
description: >
  告警有效性评估，覆盖告警精准度(Precision≥80%)、告警召回率(Recall≥95%)、
  告警响应时间(MTTA≤5min)和告警噪声比(≤20%)四个核心维度。
  通过量化指标评估告警系统在实际运维中的表现，驱动告警治理持续改进。
---

# 告警有效性评估 (Alert Effectiveness Evaluation)

## Overview

告警有效性评估用于衡量监控告警系统的实际运维效能，确保告警能够准确、及时地发现真实问题，同时控制告警噪声对运维团队的干扰。本评估适用于运维告警系统的定期审计、告警规则优化和 On-Call 轮值质量回溯。

### 适用场景

- 告警规则上线后运行效果评估（运行 ≥ 7 天后）
- 季度告警治理回顾和阈值调优
- 事件复盘中的告警效果分析
- On-Call 轮值交接时的告警质量检查

---

## Evaluation Criteria

| 维度 | 权重 | 目标值 | 测量方法 |
|------|------|--------|----------|
| 告警精准度 (Precision) | 30% | ≥ 80% | Precision = TP / (TP + FP)，统计过去 30 天数据 |
| 告警召回率 (Recall) | 25% | ≥ 95% | Recall = TP / (TP + FN)，对照事件记录核查 |
| 告警响应时间 (MTTA) | 25% | ≤ 5 min | MTTA = 告警触发 → 首次响应确认的平均时间 |
| 告警噪声比 (Noise Ratio) | 20% | ≤ 20% | 噪声比 = 无效告警 / 总告警数，含自动恢复的告警 |

### 指标说明

- **TP (True Positive)**：告警对应真实故障，运维确认有效
- **FP (False Positive)**：告警但实际无故障（误报）
- **FN (False Negative)**：故障发生但未触发告警（漏报）
- **MTTA (Mean Time to Acknowledge)**：从告警触发到运维人员首次响应的平均耗时

---

## Scoring Formula

### 加权评分

```
精准度得分 = min(Precision / 80%, 1) × 100
召回率得分 = min(Recall / 95%, 1) × 100
响应得分   = max(0, 100 - (MTTA - 1) × 10)        // MTTA=1min得100分, 每增1min扣10分
噪声得分   = max(0, 100 - NoiseRatio / 20% × 100)  // 噪声比每超1%扣5分

总分 = 精准度得分 × 30% + 召回率得分 × 25% + 响应得分 × 25% + 噪声得分 × 20%
```

### 等级划分

| 等级 | 分数范围 | 判定 |
|------|----------|------|
| S (Excellent) | ≥ 90 | 告警系统健康，持续监控 |
| A (Good) | 80-89 | 少量优化空间，纳入下季度改进 |
| B (Fair) | 70-79 | 需要告警治理专项工作 |
| F (Failed) | < 70 | 告警系统存在严重问题，需立即整改 |

---

## Checklist

### 1. 告警精准度检查 (6项)

- [ ] **ALP-001**: 告警规则有明确的阈值（非默认值），基于历史数据校准
- [ ] **ALP-002**: 告警规则配置了持续时间（Duration），避免瞬时抖动触发
- [ ] **ALP-003**: 已配置告警聚合（Alert Deduplication），相同根源告警 30 分钟内合并
- [ ] **ALP-004**: 告警规则有对应的 Runbook，标明确认步骤和应急处理方法
- [ ] **ALP-005**: 过去 30 天 Precision ≥ 80%，无已知未解决的 FP 模式
- [ ] **ALP-006**: 告警规则有负责人和有效期，过期未检视的规则触发通知

### 2. 告警召回率检查 (5项)

- [ ] **ALR-001**: 所有 P0/P1 故障场景均有至少一条告警规则覆盖
- [ ] **ALR-002**: 告警规则覆盖指标维度：可用性、延迟、吞吐量、错误率、饱和度
- [ ] **ALR-003**: 过去 30 天 Recall ≥ 95%，已分析全部 FN 根因
- [ ] **ALR-004**: 新上线的服务/模块在 48 小时内完成告警规则配置
- [ ] **ALR-005**: 定期（至少每月）进行告警规则覆盖度盲测，补充遗漏场景

### 3. 告警响应时间检查 (6项)

- [ ] **ALT-001**: P0 告警 MTTA ≤ 5 分钟，P1 告警 MTTA ≤ 15 分钟
- [ ] **ALT-002**: On-Call 排班表有效，无空窗期或单人长期 On-Call
- [ ] **ALT-003**: 告警通知渠道多样化（电话 + IM + 邮件），至少 2 种渠道可达
- [ ] **ALT-004**: 告警升级机制已配置（10 分钟未响应升级至 Team Lead，20 分钟升级至 Manager）
- [ ] **ALT-005**: 节假日/非工作时间 On-Call 有 Escalation 路径
- [ ] **ALT-006**: 告警确认率 100%（所有告警均有确认操作，非标记已读）

### 4. 告警噪声比检查 (5项)

- [ ] **ALN-001**: 噪声比 ≤ 20%，Predicted Noise Ratio 未来 30 天趋势不上升
- [ ] **ALN-002**: 自动恢复（Auto-Recovery）的告警标记为噪声并纳入统计
- [ ] **ALN-003**: 每周有告警回顾例会，分析 Top 10 噪声来源并制定改进措施
- [ ] **ALN-004**: 重复告警已通过抑制规则（Silence/Maintenance Window）管理
- [ ] **ALN-005**: 告警风暴期间有自动化抑制机制，同一故障根源产生的告警不超过 10 条

---

## Report Template

```markdown
# 告警有效性评估报告

## 概要

| 项目 | 值 |
|------|-----|
| 评估周期 | YYYY-MM-DD ~ YYYY-MM-DD |
| 评估范围 | [环境/服务/模块] |
| 总告警数 | [N] |
| TP / FP / FN | [N] / [N] / [N] |
| 综合评分 | [XX.X] 分 / 100 |
| 等级判定 | [S/A/B/F] |

## 核心指标

| 指标 | 实际值 | 目标值 | 达标 |
|------|--------|--------|------|
| Precision | XX.X% | ≥ 80% | Y/N |
| Recall | XX.X% | ≥ 95% | Y/N |
| MTTA | X.X min | ≤ 5 min | Y/N |
| Noise Ratio | XX.X% | ≤ 20% | Y/N |

## Top 5 噪声来源

| 排名 | 告警规则 | 噪声数 | 占比 | 根因 | 改进措施 | 责任人 |
|------|----------|--------|------|------|----------|--------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

## 漏报分析 (FN)

| 事件 | 发生时间 | 影响范围 | 缺失的告警规则 | 补充计划 | 优先级 |
|------|----------|----------|----------------|----------|--------|
| | | | | | |

## 改进项跟踪

| # | 改进项 | 优先级 | 责任人 | 计划完成 | 状态 |
|---|--------|--------|--------|----------|------|
| 1 | | | | | Open/In Progress/Done |

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | YYYY-MM-DD | Initial assessment | [Name] |
```

---

## Related Evaluations

- [slo-compliance.md](slo-compliance.md)
- [response-time-analysis.md](response-time-analysis.md)
- [monitoring-quality-checklist.md](monitoring-quality-checklist.md)
- [performance-baseline.md](performance-baseline.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)
