---
name: deployment-best-practices
description: "部署最佳实践标准，定义部署策略对比、预部署检查清单、后部署验证和环境晋升流程规范"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'deployment', 'canary', 'blue-green', 'ci-cd']
---

# 部署最佳实践

> 本规范定义 E2E Delivery Harness 中所有场景的部署策略、质量门禁与回退准则。审查基准见 [harness-engineering.md](../harness-engineering.md)。

## 1. 部署策略对比

选择部署策略时应根据业务容忍度、基础设施能力和团队成熟度综合评估。

| 策略 | 停机时间 | 回滚速度 | 资源成本 | 适用场景 |
|------|----------|----------|----------|----------|
| **蓝绿部署 (Blue/Green)** | 零停机 | 即时切换回 Green | 2x 资源 | 核心交易链路、用户面向服务 |
| **滚动更新 (Rolling)** | 逐步替换 | 逐批回滚 | 1x+N buffer | 无状态微服务、批处理任务 |
| **金丝雀发布 (Canary)** | 零停机 | 流量摘除即回滚 | 1.1x~1.3x | 高风险变更、大版本发布 |
| **灰度发布 (Feature Flags)** | 零停机 | 开关关闭即回滚 | 无额外成本 | 功能开关、A/B 测试 |
| **重建部署 (Recreate)** | 完全停机 | 重新部署旧版本 | 1x | 单体应用、开发/测试环境 |

### 1.1 选择决策矩阵

```
变更风险高 → 金丝雀发布 (Canary) + Feature Flags
变更风险低 → 滚动更新 (Rolling) 或 蓝绿 (Blue/Green)
基础设施受限 → 滚动更新 (Rolling)
零停机要求 → 蓝绿部署 或 金丝雀发布
```

## 2. 预部署检查清单 (Pre-deploy Checklist)

在每个部署开始前，必须逐项确认以下内容。参见 [change-management.md](../standards/change-management.md) 变更审批流程。

### 2.1 变更准入

- [ ] 变更单已审批（risk level ≤ medium 可自动批准，high/ critical 需人工审批）
- [ ] 对应 [testing-guidelines.md](../standards/testing-guidelines.md) 测试门禁已通过（单元测试通过率≥90%，集成测试通过率≥80%）
- [ ] 代码审查已完成（参见 [code-review-checklist.md](../standards/code-review-checklist.md)）
- [ ] 制品 (artifact) 签名校验通过
- [ ] 配置变更已审查，敏感信息未硬编码

### 2.2 环境就绪

- [ ] 目标环境健康检查通过（参见 [health-check-guidelines.md](../standards/health-check-guidelines.md)）
- [ ] 数据库迁移脚本已检查向后兼容性
- [ ] 依赖服务已确认可用或已同步变更
- [ ] 存储容量监控正常（磁盘、数据库连接池、消息队列积压）
- [ ] SSL/证书有效期 ≥ 30 天

### 2.3 发布准备

- [ ] 版本标签已创建（格式 v{MAJOR}.{MINOR}.{PATCH}-{build_number}）
- [ ] Release Notes 已编写（用户可见变更 + 内部变更）
- [ ] 监控仪表盘已就绪（参见 [monitoring-standards.md](../standards/monitoring-standards.md)）
- [ ] 告警阈值已审查（参见 [alerting-guidelines.md](../standards/alerting-guidelines.md)）
- [ ] Playbook 已更新，值班团队已通知

## 3. 后部署检查清单 (Post-deploy Checklist)

### 3.1 验证

- [ ] 所有健康检查端点返回 200 OK（liveness + readiness）
- [ ] 核心业务流程冒烟测试通过
- [ ] 监控仪表盘无异常（错误率、延迟 P99、CPU/内存水位）
- [ ] 日志中无新增 ERROR 级别条目
- [ ] 数据库连接数在预期范围内

### 3.2 观察期

- [ ] 观察窗口：高风险变更 ≥ 30 分钟，普通变更 ≥ 15 分钟
- [ ] 逐步放量（金丝雀）：5% → 20% → 50% → 100%，每阶段观察 ≥ 5 分钟
- [ ] 确认 SLI 指标在 SLO 阈值内（参见 [sre-best-practices.md](../standards/sre-best-practices.md)）

### 3.3 收尾

- [ ] 部署状态已更新至发布跟踪系统
- [ ] 变更单标记为已完成
- [ ] 相关人员已通知

## 4. 环境晋升流程 (Environment Promotion Flow)

```
feature → dev → test → staging → canary → production (5%→20%→50%→100%)
```

每阶段晋升条件：

| 环境 | 准入条件 | 验证内容 | 超时回退 |
|------|----------|----------|----------|
| **dev** | 代码提交+CI通过 | 单元测试、lint、构建 | 30min |
| **test** | Dev 冒烟通过 | 集成测试、API 测试 | 1h |
| **staging** | Test 全量通过 | 性能测试、安全扫描 | 2h |
| **canary** | Staging 评审通过 | 流量染色、业务指标 | 4h |
| **production** | Canary 观察无异常 | 全量放量、SLO 达标 | 持续监控 |

环境晋升应使用相同的构建制品 (build artifact)，避免重新编译引入差异。参见 [rollback-strategy.md](../standards/rollback-strategy.md) 回退策略。

## 5. 回滚触发标准 (Rollback Criteria)

任一下列条件满足时自动触发回滚：

### 5.1 自动回滚条件

- **错误率**: 相比基线上升 > 5%（HTTP 5xx、业务异常码）
- **延迟**: P99 延迟超过 SLO 阈值 × 1.5
- **健康检查**: 连续 3 次 readiness check 失败
- **内存/CPU**: 超过 resource limit 的 90% 持续 > 2 分钟
- **业务指标**: 核心业务转化率下降 > 10%
- **数据库**: 迁移后读写错误率 > 1%

### 5.2 人工决策回滚

- 功能缺陷影响 ≤ 5% 用户时，决策窗口 ≤ 30 分钟
- 安全漏洞被公开披露，立即回滚
- 数据完整性受损，立即回滚并执行 [rollback-procedures.md](../standards/rollback-procedures.md)

## 6. 部署窗口规范 (Deployment Window Guidelines)

| 环境 | 允许窗口 | 例外审批 |
|------|----------|----------|
| **production** | 周一至周四 09:00-16:00 UTC | VP/SVP 审批 |
| **staging** | 周一至周五 07:00-20:00 UTC | 技术负责人审批 |
| **test/dev** | 全天 | 无需审批 |

- 禁止：周五下午、周末、法定节假日前一日部署生产环境（P0 安全修复除外）
- 变更窗口：高风险变更部署持续时间 ≤ 60 分钟
- 冻结期：发版前 48 小时至发版后 24 小时为部署冻结期（hotfix 需特批）

## 7. 出站审查对应 (HO-* Mapping)

本标准中各检查项映射到 handover HO-* 字段：

- `HO-001` (部署版本) → 第 2.3 节版本标签
- `HO-002` (部署策略) → 第 1 节选择的策略
- `HO-003` (验证结果) → 第 3.1 节验证项
- `HO-004` (回滚就绪) → 第 5 节回滚计划
- `HO-005` (监控链接) → 监控仪表盘 URL & 告警状态

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [rollback-strategy.md](../standards/rollback-strategy.md)
- [rollback-procedures.md](../standards/rollback-procedures.md)
