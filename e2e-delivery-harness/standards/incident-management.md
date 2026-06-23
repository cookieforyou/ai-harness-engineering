---
name: incident-management
type: standard
version: "2.0.0"
status: active
---

# 事件管理

> 本规范定义 E2E Delivery Harness 中所有 Incident 的分级、响应、升级与复盘流程。审查基准见 [harness-engineering.md](harness-engineering.md)。告警规则见 [alerting-guidelines.md](alerting-guidelines.md)，SRE 原理见 [sre-best-practices.md](sre-best-practices.md)。

## 1. 事件严重级别 (Severity Levels)

| 级别 | 定义 | 影响标准 | 响应 SLA | 示例 |
|------|------|----------|----------|------|
| **P0 (Critical)** | 核心服务完全中断或数据严重受损 | 全部用户受影响 / 收入损失 > $10K / 数据丢失 | ≤ 5 分钟 | 支付服务宕机、数据库损坏、安全入侵 |
| **P1 (High)** | 核心功能严重受损，有变通方案或影响部分用户 | 核心用户 > 20% 受影响 / 核心功能不可用 | ≤ 15 分钟 | 搜索不返回结果、订单无法取消 |
| **P2 (Medium)** | 非核心功能受损，有变通方案 | ≤ 5% 用户受影响 / 用户体验下降 | ≤ 1 小时 | 页面加载慢、非核心页面报错 |
| **P3 (Low)** | 轻微功能问题，无用户影响 | 延迟响应、内部工具问题 | ≤ 24 小时 | 后台报表数据延迟、非关键告警误报 |
| **P4 (Cosmetic)** | 视觉/体验问题，不影响功能 | 仅美观/易用性 | 下一个版本 | 按钮不对齐、文字拼写错误 |

## 2. 响应时间目标 (Response Times)

| Severity | Acknowledged | Triage Start | Mitigation Start | Resolution Target |
|----------|-------------|--------------|------------------|-------------------|
| **P0** | ≤ 5 min | ≤ 10 min | ≤ 15 min | ≤ 60 min |
| **P1** | ≤ 15 min | ≤ 20 min | ≤ 30 min | ≤ 4 hours |
| **P2** | ≤ 1 hour | ≤ 2 hours | ≤ 4 hours | ≤ 8 hours |
| **P3** | ≤ 24 hours | ≤ 48 hours | — | Next release |

## 3. 事件响应角色 (Incident Response Roles)

### 3.1 角色定义

| 角色 | 职责 | 指定方式 |
|------|------|----------|
| **Incident Commander (IC)** | 事件总指挥，协调各团队，决策优先级 | On-call 工程师 或 技术负责人 |
| **Communications Lead** | 对外沟通（内部干系人 + 客户沟通） | 技术主管或 PM |
| **Operations Lead** | 执行缓解/恢复操作 | On-call 工程师 |
| **Scribe** | 记录时间线、决策、操作 | 任意团队成员 |
| **Subject Matter Expert** | 特定领域的专家（DB、网络、安全） | 按需加入 |

### 3.2 切换原则

- IC 不直接操作 — 避免陷入技术细节导致失去全局视角
- 30 分钟无进展 → IC 考虑升级或切换策略
- 如果 incident 持续 > 1 小时 → 建立专门的沟通频道

## 4. 事件生命周期 (Incident Lifecycle)

### 4.1 检测与申报

```
Detection: 监控告警 / 用户反馈 / 例行巡检
    ↓
Initial Assessment (≤ 5 min):
  ├── 确认是否真实 Incident（排除误报）
  ├── 确定 Severity 级别
  ├── 影响范围评估（用户数、请求量、收入）
  └── 初始 Root Cause 假设
    ↓
Declaration: 在 Incident 管理系统中创建事件记录
  ├── 标题: [P0] 服务名 - 问题摘要
  ├── 时间: 检测时间
  ├── Severity: P0 / P1 / P2 / P3
  └── 初始描述
```

### 4.2 缓解 (Mitigation)

**优先恢复服务，不优先 Root Cause 分析**

```
Mitigation Actions:
├── 是否可回滚？ → 立即执行回滚（参见 rollback-procedures.md）
├── 是否可降级？ → 关闭非关键功能，保留核心服务
├── 是否可限流？ → 增加限流阈值保护下游
├── 是否可扩容？ → 快速增加副本数应对流量
└── 以上都不行 → 持续排查（引入 SME）
```

### 4.3 解决 (Resolution)

- 确认服务恢复正常（健康检查 + 业务指标回归基线）
- 持续观察 ≥ 15 分钟（P0）/ ≥ 5 分钟（P1）
- 更新 incident 状态为 "Resolved"
- 通知所有干系人

### 4.4 复盘 (Postmortem)

**时间**: 事件解决后 72 小时内

**参会人**: IC + 所有参与人 + 相关团队代表

**模板**:

```markdown
# Postmortem: INC-2026-0421

## Summary
[简述事件：时间、影响、Root Cause]

## Timeline
| 时间 (UTC) | 事件 |
|------------|------|
| 10:25 | 告警触发：payment-api error rate > 5% |
| 10:27 | On-call 确认 alert |
| 10:30 | IC 宣布 P0 incident |
| 10:32 | 决定回滚 v2.1.3 |
| 10:35 | 开始回滚操作 |
| 10:38 | 回滚完成，监控恢复 |
| 10:45 | 观察确认服务正常 |

## Impact
- 受影响用户: ~3,200
- 受影响请求: ~12,000
- 收入影响: ~$2,500
- 持续时间: 20 分钟 (10:25 - 10:45)

## Root Cause (5 Whys)
1. 支付超时增加 → 因为连接池配置错误
2. 连接池配置错误 → 因为配置文件中参数被意外修改
3. 配置被修改 → 因为配置变更未经过 review
4. 配置变更未 review → 因为紧急变更跳过了流程
5. **Why 根本原因**: 紧急变更流程缺少审计环节

## Action Items
| # | 行动项 | 类型 | 责任人 | 截止日期 |
|---|--------|------|--------|----------|
| 1 | 配置变更必须经过 PR review | Prevention | Team A | T+1d |
| 2 | 连接池配置变更前自动测试 | Detection | Team B | T+7d |
| 3 | 配置审计日志告警 | Detection | Team B | T+14d |

## Blameless Statement
本次事件的根本原因是流程缺失而非个人错误。
团队已识别改进项，将在截止日期前完成。
```

## 5. 沟通模板 (Communication Templates)

### 5.1 事件声明 (Internal)

```
:rotating_light: [P0] 支付服务 - 高错误率 (INC-2026-0421)

时间: 2026-06-23 10:25 UTC
影响: 支付成功率从 99.9% 降至 85%，约 3,200 用户受影响
状态: 调查中 / 缓解中 / 已解决
IC: @john.smith
频道: #incident-payment

更新频率: 每 15 分钟
```

### 5.2 解决通知

```
✅ [P0] 支付服务 - 已解决 (INC-2026-0421)

时间: 2026-06-23 10:45 UTC
持续时间: 20 分钟
Root Cause: 连接池配置错误
操作: 回滚至 v2.1.2
总结: https://wiki.internal/postmortems/INC-2026-0421
```

### 5.3 客户沟通模板 (面向外部)

```
[Subject] Service Incident Report - June 23, 2026

Dear customers,

Between 10:25 and 10:45 UTC on June 23, 2026, our payment service
experienced elevated error rates affecting approximately 3,200
transactions.

Root cause: A configuration change to the database connection pool
was deployed without proper review, causing connection exhaustion
under load.

Resolution: The configuration was rolled back to the previous stable
version. Service returned to normal at 10:45 UTC.

We have implemented the following improvements:
1. All configuration changes now require code review
2. Automated testing for connection pool configuration changes
3. Enhanced alerting for connection pool saturation

We apologize for the inconvenience.
```

## 6. Incident 指标跟踪 (Key Metrics)

| 指标 | 定义 | 目标 | 追踪频率 |
|------|------|------|----------|
| **MTTD** | 平均检测时间（告警触发到确认） | P0 ≤ 2 min, P1 ≤ 5 min | 每月 |
| **MTTA** | 平均确认时间（告警到响应） | P0 ≤ 5 min, P1 ≤ 15 min | 每月 |
| **MTTR** | 平均修复时间 | P0 ≤ 60 min, P1 ≤ 4 h | 每月 |
| **Incident 数量** | 每月 P0/P1 总数 | P0 ≤ 2/月, P1 ≤ 8/月 | 每月 |
| **复盘完成率** | 复盘按时完成比例 | ≥ 90% | 每月 |
| **行动项关闭率** | 复盘行动项按时关闭比例 | ≥ 85% | 每月 |

## 引用

- [asset-model.md](asset-model.md)
- [authoring-checklist.md](authoring-checklist.md)
- [alerting-guidelines.md](alerting-guidelines.md)
- [sre-best-practices.md](sre-best-practices.md)
- [change-management.md](change-management.md)
- [rollback-procedures.md](rollback-procedures.md)
