---
name: hotfix-quality-checklist
type: evaluation
version: "1.0.0"
status: active
language: "zh-CN"
description: "热修复质量清单，用于评估紧急修复的审批流程、验证步骤和风险控制"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
tags: ['evaluation', 'hotfix', 'quality', 'checklist', 'emergency']
---

# 热修复质量检查清单 (Hotfix Quality Checklist)

## Purpose

本清单用于评估紧急热修复的质量管控，确保在快速响应生产问题的同时不引入新的风险。涵盖应急评估、代码隔离、部署验证与事后复盘四个环节。

## Scoring

- **PASS**: 完全满足要求
- **PARTIAL**: 部分满足，需标注例外理由
- **FAIL**: 不满足要求，禁止发布
- **NA**: 不适用

## 使用时机

- 生产 P0/P1 故障需紧急修复时
- 热修复合入前的质量门禁
- 热修复发布后的复盘评估

## 重要提示

热修复流程允许适当加速但**不可跳过质量门禁**。每项 FAIL 需技术负责人审批豁免并记录风险。

---

## 1. 应急评估 (Emergency Assessment)

- [ ] **HEM-001**: 故障已确认为生产问题（有监控截图/用户报障记录/错误日志），非误报或测试环境问题
- [ ] **HEM-002**: 故障影响范围已评估：影响用户数、影响功能模块、是否涉及数据安全/资金损失
- [ ] **HEM-003**: 故障等级确认：P0（核心功能完全不可用）/ P1（主要功能受损且有变通方案），P2 以下不建议发 Hotfix
- [ ] **HEM-004**: 根因定位完成后方可开始修复（有根因分析的链路追踪/日志证据），禁止"猜修复"
- [ ] **HEM-005**: 修复方案已评审（至少 1 名同级或上级工程师 Review），评审时间 < 60 分钟
- [ ] **HEM-006**: 恢复优先级已明确：止损（回滚/降级）优先于修复发布，回滚可行时优先回滚

## 2. 代码隔离 (Isolation Verification)

- [ ] **HISO-001**: Hotfix 分支基于目标发布标签（tag）创建，非基于开发分支的最新代码
- [ ] **HISO-002**: 变更仅包含与本次修复直接相关的代码，无无关功能/重构/格式化变更（diff 中每行可追溯至根因）
- [ ] **HISO-003**: Hotfix commit message 包含故障编号（INC-* 或 BUG-*）和简要根因说明
- [ ] **HISO-004**: 修复代码已通过静态分析（lint/SAST），阻塞级别问题已清零
- [ ] **HISO-005**: 修复涉及的数据变更脚本已验证幂等性（可重复执行不产生副作用）

## 3. 部署验证 (Deployment Verification)

- [ ] **HDEP-001**: Hotfix 已在预发布环境完成验证：修复效果确认（故障复现场景通过）+ 回归冒烟测试（核心 P0 场景通过）
- [ ] **HDEP-002**: 灰度发布：先部署到 1 台/1% 流量观察 5-10 分钟，确认无新异常后逐步放量
- [ ] **HDEP-003**: 关键指标对比：发布后 15 分钟内，错误率 ≤ 故障前基线水平，P95 延迟 ≤ 基线的 1.2 倍
- [ ] **HDEP-004**: 回滚方案就绪：Hotfix 出问题时可在 5 分钟内回滚（已知可工作版本已标记 Ready）
- [ ] **HDEP-005**: 部署过程有 on-call 工程师实时关注告警，发现异常立即暂停

## 4. 事后处理 (Post-Mortem Requirements)

- [ ] **HPST-001**: 故障复盘文档在修复后 48 小时内完成，包含：故障时间线、根因、影响范围、修复措施
- [ ] **HPST-002**: 5 Whys 分析完整：从现象层层推导至根因，无"人为疏忽"作为终极原因
- [ ] **HPST-003**: 改进措施已创建对应 Jira/Issue 任务（至少 1 个防复发措施），有负责人和截止日期
- [ ] **HPST-004**: Hotfix 变更已在下一个常规迭代中被合入主开发分支（cherry-pick/merge back）
- [ ] **HPST-005**: 监控告警已补充：针对本次故障的模式添加新的监控指标或告警规则
- [ ] **HPST-006**: 知识库已更新：将本次故障的诊断方法/修复步骤写入 Runbook 或 FAQ

---

## Summary

| 环节 | PASS | PARTIAL | FAIL | 通过率 |
|------|------|---------|------|--------|
| 应急评估 | __ | __ | __ | __% |
| 代码隔离 | __ | __ | __ | __% |
| 部署验证 | __ | __ | __ | __% |
| 事后处理 | __ | __ | __ | __% |
| **总计** | **__** | **__** | **__** | **__%** |

### 判定标准

| 通过率 | 结果 |
|--------|------|
| ≥ 85% | PASS - 热修复可发布（需修复 FAIL 项） |
| 70-84% | CONDITIONAL PASS - 需技术总监审批 |
| < 70% | FAIL - 热修复流程执行不完整，禁止发布 |

### 审批

- 技术负责人: __________ 日期: __________
- [ ] 批准发布
- [ ] 需要补充验证后再次审批

### 故障基本信息

| 字段 | 值 |
|------|-----|
| 故障编号 | INC-_____ |
| 修复版本号 | _____ |
| 修复时间 | _____ |
| 影响时长 | _____ 分钟 |
| 影响用户数 | _____ |

---

## References

- [regression-checklist.md](regression-checklist.md)
- [deployment-quality-checklist.md](deployment-quality-checklist.md)
- [monitoring-quality-checklist.md](monitoring-quality-checklist.md)
- [common-error-patterns.md](common-error-patterns.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)

## 相关评估

- [deployment-quality-checklist.md](deployment-quality-checklist.md) — 部署质量清单
- [regression-checklist.md](regression-checklist.md) — 回归检查清单
- [monitoring-quality-checklist.md](monitoring-quality-checklist.md) — 监控质量清单
- [code-quality-checklist.md](code-quality-checklist.md) — 代码质量清单
