---
name: rollback-strategy
description: "回滚策略标准，定义回滚决策矩阵、RTO/RPO 目标、回滚策略分类与回滚就绪检查规范"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'rollback', 'strategy', 'rto', 'rpo']
---

# 回滚策略

> 本规范定义 E2E Delivery Harness 中所有场景的回滚决策标准、各组件回滚流程与 RTO 目标。审查基准见 [harness-engineering.md](../harness-engineering.md)。具体操作步骤见 [rollback-procedures.md](../standards/rollback-procedures.md)。

## 1. 回滚决策矩阵 (Rollback Decision Matrix)

回滚决策综合以下维度进行评估：

| 触发条件 | 严重级别 | 决策动作 | 决策者 | 响应时限 |
|----------|----------|----------|--------|----------|
| 安全漏洞 (CVE Critical) | **P0** | 强制立即回滚 | On-call 工程师 + 安全团队 | 15 分钟内 |
| 数据完整性受损 | **P0** | 强制立即回滚 + 数据恢复 | 值班 DBA + 技术负责人 | 15 分钟内 |
| 核心业务指标下降 > 10% | **P0** | 强制立即回滚 | Incident Commander | 15 分钟内 |
| P99 延迟超过 SLO × 2 | **P1** | 建议回滚，可尝试原地修复 | 技术负责人 | 30 分钟内 |
| 错误率上升 > 5% | **P1** | 建议回滚 | 技术负责人 | 30 分钟内 |
| 非核心功能缺陷 | **P2** | 向前修复 (Forward Fix) | 开发团队 | 4 小时内 |
| UI/UX 显示问题 | **P2-P3** | 向前修复 | 开发团队 | 下一个版本 |
| 配置错误 (非安全) | **P1** | 建议回滚或热修复配置 | On-call 工程师 | 30 分钟内 |

### 1.1 回滚 vs 向前修复决策树

```
变更部署后发现问题
├── 数据受影响？
│   ├── 是 → 立即回滚（防止数据损坏扩散）
│   └── 否 →
│       ├── 安全漏洞？
│       │   ├── 是 → 立即回滚
│       │   └── 否 →
│       │       ├── 修复时间 < 回滚时间 ← 向前修复
│       │       ├── 修复时间 > 回滚时间 ← 回滚
│       │       └── 修复过程中用户是否持续受损？
│       │           ├── 是 → 回滚
│       │           └── 否 → 向前修复
```

## 2. 回滚策略分类

### 2.1 按回滚方式

| 策略 | 机制 | 适用组件 | 恢复速度 |
|------|------|----------|----------|
| **版本切换** | 蓝绿部署切换回上一版本 | 无状态服务 | < 1 分钟 |
| **滚动回滚** | 逐步 re-deploy 上一版本 | 无状态微服务 | 2-10 分钟 |
| **前向恢复** | 执行补偿事务 (Saga rollback) | 有状态/事务性服务 | 1-30 分钟 |
| **数据回档** | 恢复数据库快照 | 数据库 | 10-60 分钟 |
| **功能开关** | 关闭 Feature Flag | 任意功能 | < 1 分钟 |

### 2.2 按组件类型

| 组件 | 推荐策略 | 说明 |
|------|----------|------|
| **前端 (SPA/SSR)** | 版本切换（CDN 缓存刷新） | 保持前一个版本的构建包 |
| **后端 API** | 版本切换（蓝绿）或滚动回滚 | 注意 API 向后兼容 |
| **数据库** | Schema 版本回退 + 数据回档 | 需提前规划迁移回退脚本 |
| **配置** | 外部配置中心版本切换 | 回滚配置+服务重启（如必要） |
| **消息队列消费者** | 滚动回滚，暂停消费→回滚→恢复 | 注意消息积压处理 |
| **批处理/定时任务** | 停止调度 → 恢复旧代码 → 重跑 | 可选跳过已处理数据 |

## 3. RTO/RPO 目标 (Recovery Time / Point Objectives)

### 3.1 按服务分级

| 服务 Tier | RTO 目标 | RPO 目标 | 参考 |
|-----------|----------|----------|------|
| **Tier 0 (Critical)** | ≤ 5 分钟 | ≤ 1 秒 | 支付、认证、核心交易 |
| **Tier 1 (High)** | ≤ 15 分钟 | ≤ 60 秒 | 核心业务 API、用户数据 |
| **Tier 2 (Standard)** | ≤ 30 分钟 | ≤ 5 分钟 | 非核心业务、后台服务 |
| **Tier 3 (Best Effort)** | ≤ 4 小时 | ≤ 15 分钟 | 内部工具、辅助服务 |

### 3.2 RTO 分解（以 Tier 0 为例）

```
Detection    ≤ 1 min
Assessment   ≤ 1 min
Decision     ≤ 1 min
Rollback     ≤ 2 min (自动化回滚)
Verification ≤ 1 min
           Total: ≤ 6 min (满足 ≤ 5 min 需进一步优化自动化)
```

## 4. 回滚就绪检查 (Rollback Readiness)

每次部署前必须确认以下事项已准备：

### 4.1 技术就绪

- [ ] 上一个已知良好版本 (Last Known Good, LKG) 的构建制品仍在制品库中
- [ ] 数据库迁移脚本具有对应的回滚脚本（可逆迁移）
- [ ] 功能开关 (Feature Flag) 已就绪（可独立关闭功能而不影响其他功能）
- [ ] 回滚 playbook 已更新并且测试过
- [ ] 配置中心保留了上一版本的完整配置快照

### 4.2 流程就绪

- [ ] 值班工程师知晓回滚流程
- [ ] 回滚授权人已确认（P0 级别回滚可自动触发）
- [ ] 回滚通知模板已准备（相关干系人清单）
- [ ] 回滚后验证 checklist 已编写

## 5. 回滚测试频率

| 组件类型 | 测试频率 | 测试方式 |
|----------|----------|----------|
| 无状态服务 | 每次部署 | 自动化回滚测试（CI pipeline） |
| 数据库迁移 | 每次 schema 变更 | 在 staging 环境执行回滚 |
| 配置变更 | 每季度 | 配置中心版本切换演练 |
| 完整 DR 演练 | 每半年 | 全组件回滚 + 数据恢复演练 |

## 6. HO-* 映射

- `HO-RB-001` — 回滚策略已文档化并匹配组件类型
- `HO-RB-002` — RTO/RPO 已定义并经过测试
- `HO-RB-003` — 数据库回滚脚本已准备
- `HO-RB-004` — 回滚 playbook 已测试通过
- `HO-RB-005` — LKG 制品可用

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [rollback-procedures.md](../standards/rollback-procedures.md)
- [deployment-best-practices.md](../standards/deployment-best-practices.md)
- [sre-best-practices.md](../standards/sre-best-practices.md)
