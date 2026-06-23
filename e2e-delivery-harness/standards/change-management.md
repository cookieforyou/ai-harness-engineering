---
name: change-management
description: "变更管理标准，定义变更类型分类、风险等级评估矩阵、变更窗口与审批流程规范"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'change-management', 'risk', 'approval']
---

# 变更管理

> 本规范定义 E2E Delivery Harness 中所有变更的分类、审批流程、变更窗口与风险评估标准。审查基准见 [harness-engineering.md](../harness-engineering.md)。

## 1. 变更类型 (Change Types)

### 1.1 标准变更分类

| 类型 | 定义 | 风险等级 | 审批流程 | 示例 |
|------|------|----------|----------|------|
| **常规发布 (Standard)** | 遵循既定流程的低风险变更 | Low | 无需审批（CI/CD 门禁通过即可） | Bug 修复、常规功能发布 |
| **紧急修复 (Emergency)** | 影响生产服务的紧急修复 | High/Critical | 快速审批（on-call 工程师 + 技术负责人） | P0/P1 事故的 hotfix |
| **重大变更 (Major)** | 影响架构、数据、接口的变更 | High | 变更咨询委员会 (CAB) 审批 | 数据库 schema 变更、API 不兼容升级 |
| **基础设施变更** | 服务器/网络/云资源配置变更 | Medium-High | 技术负责人审批 | Terraform 变更、K8s 集群升级 |
| **配置变更** | 非功能配置调整 | Low-Medium | 按环境分级审批 | Feature Flag 开关、限流阈值调整 |
| **安全补丁** | 安全漏洞修复 | Critical | 安全团队 + 技术负责人审批 | CVE 修复、依赖升级 |

### 1.2 变更类型代码

每个变更在跟踪系统中应标记类型代码：

| 代码 | 含义 |
|------|------|
| `CHG-STD` | 标准变更 (Standard) |
| `CHG-EMG` | 紧急变更 (Emergency) |
| `CHG-MAJ` | 重大变更 (Major) |
| `CHG-INF` | 基础设施变更 |
| `CHG-CFG` | 配置变更 |
| `CHG-SEC` | 安全补丁 |

## 2. 风险等级与审批矩阵 (Risk Assessment Matrix)

### 2.1 风险评分

风险 = 影响程度 × 发生概率

| 影响程度 | 评分 | 标准 |
|----------|------|------|
| **Critical (5)** | 5 | 数据丢失/泄露、服务完全不可用、收入影响 > $100K |
| **High (4)** | 4 | 核心功能受损 > 30 分钟、收入影响 $10K-$100K |
| **Medium (3)** | 3 | 非核心功能受损、用户体验下降 |
| **Low (2)** | 2 | 内部功能受影响、无用户感知 |
| **Minimal (1)** | 1 | 不影响运行时 |

| 发生概率 | 评分 | 标准 |
|----------|------|------|
| **Almost Certain (5)** | 5 | 几乎必然发生（全新代码无测试） |
| **Likely (4)** | 4 | 很可能发生（修改了核心逻辑） |
| **Possible (3)** | 3 | 可能发生（修改了次要路径） |
| **Unlikely (2)** | 2 | 不太可能（配置变更、文档变更） |
| **Rare (1)** | 1 | 几乎不会（测试覆盖的纯前端样式） |

### 2.2 审批矩阵

| 综合评分 | 风险级别 | 审批人 | 审批时限 |
|----------|----------|--------|----------|
| 1-4 | **Low** | 自动批准（CI 门禁通过） | 即时 |
| 5-9 | **Medium** | 技术负责人 | ≤ 4 小时 |
| 10-16 | **High** | 技术负责人 + 架构师 | ≤ 24 小时 |
| 17-25 | **Critical** | CAB (变更咨询委员会) | ≤ 48 小时 |

## 3. 变更窗口 (Change Windows)

### 3.1 窗口定义

| 环境 | 常规变更窗口 | 紧急变更窗口 | 冻结期 |
|------|-------------|-------------|--------|
| **Production** | 周一至周四 09:00-16:00 UTC | 全天候 (P0/P1) | 重大发版前 48h ~ 后 24h |
| **Staging** | 周一至周五 07:00-20:00 UTC | 同上 | 无 |
| **Test** | 全天 | 全天 | 无 |
| **Dev** | 全天 | 全天 | 无 |

### 3.2 窗口合规

- 高风险变更必须在工作窗口内完成（含回滚时间）
- 低风险变更可在窗口外执行（但需通知 on-call）
- 节假日自动进入部署冻结（仅安全补丁可例外）

## 4. 变更流程 (Change Workflow)

### 4.1 标准变更流程

```
创建 → 风险评估 → 审批 → 实施 → 验证 → 关闭
```

| 阶段 | 职责 | 产出物 |
|------|------|--------|
| **创建** | 变更发起人 | 变更单（描述、原因、范围、风险等级、回滚计划） |
| **风险评估** | 技术负责人 | 风险评分 + 审批矩阵结果 |
| **审批** | 授权审批人 | 审批通过/拒绝（附理由） |
| **实施** | 实施工程师 | 部署日志、检查清单完成记录 |
| **验证** | 验证人（非实施人） | 测试结果、监控截图、确认签名 |
| **关闭** | 变更管理人 | 关闭时间、结果总结、 Lessons Learned |

### 4.2 紧急变更流程 (Emergency Change)

```
1. 检测到 P0/P1 incident
2. On-call 工程师初步评估 root cause
3. 在变更管理系统中创建紧急变更单（简化字段）
4. 口头/即时消息审批（事后 24 小时内补签）
5. 实施修复（遵循部署最佳实践）
6. 验证修复效果（监控 + 冒烟测试）
7. 关闭变更
8. 24 小时内补全变更单信息 + 提交复盘
```

### 4.3 变更单必含字段

- **标题**: 简明明了的变更描述
- **类型**: 标准/紧急/重大/配置
- **风险等级**: Low / Medium / High / Critical
- **范围**: 影响的服务/模块/API
- **实施计划**: 具体步骤（参照 [deployment-best-practices.md](../standards/deployment-best-practices.md)）
- **回滚计划**: 回滚步骤（参照 [rollback-procedures.md](../standards/rollback-procedures.md)）
- **测试结果**: 测试通过确认
- **审批人**: 审批记录
- **时间线**: 创建 → 审批 → 实施 → 验证 → 关闭的时间戳

## 5. 变更审查清单 (Change Review Checklist)

- [ ] 变更目的和范围是否明确？
- [ ] 风险评分是否正确？
- [ ] 审批人是否符合矩阵要求？
- [ ] 回滚计划是否可行且已测试？
- [ ] 测试是否覆盖了正向 + 异常路径？
- [ ] 变更是否符合部署窗口规范？
- [ ] 相关的监控和告警是否已配置？
- [ ] 相关干系人是否已通知？
- [ ] 变更单信息是否完整？

## 6. 变更审计 (Change Audit)

- 所有变更记录保留 ≥ 3 年
- 每月生成变更报告（成功/失败率、平均实施时间、高风险变更比例）
- 失败变更自动标记并触发分析（变更失败率 > 5% 需要改进流程）
- 季度变更委员会回顾：检查变更失败趋势、更新审批矩阵

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [deployment-best-practices.md](../standards/deployment-best-practices.md)
- [rollback-strategy.md](../standards/rollback-strategy.md)
- [incident-management.md](../standards/incident-management.md)
