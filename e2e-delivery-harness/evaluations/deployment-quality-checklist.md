---
name: deployment-quality-checklist
type: evaluation
version: "1.0.0"
status: active
description: "部署质量清单，用于评估部署流程的完整性、回滚准备和发布验证"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
tags: ['evaluation', 'deployment', 'quality', 'checklist']
---

# 部署质量检查清单 (Deployment Quality Checklist)

## Purpose

本清单用于部署发布阶段的质量把控，覆盖部署前准备、部署执行、部署后验证及回滚四个环节。确保每次发布可重复、可监控、可回滚。

## Scoring

- **PASS**: 完全满足要求
- **PARTIAL**: 部分满足，存在可接受的微小偏差
- **FAIL**: 不满足要求，必须修复
- **NA**: 不适用

## 使用时机

- 发布审批前的部署方案评审
- 部署执行过程中的实时检查
- 部署后的质量回溯评估

---

## 1. 部署前准备 (Pre-Deploy)

- [ ] **PRE-001**: 部署包构建可重现（基于相同 commit 的构建结果一致，CI 构建编号已记录）
- [ ] **PRE-002**: 部署包完整性校验通过（MD5/SHA256 checksum 与构建产物匹配）
- [ ] **PRE-003**: 制品版本号遵循语义化版本规范（SemVer: MAJOR.MINOR.PATCH），无 SNAPSHOT 或未标记版本
- [ ] **PRE-004**: 目标环境已就绪（资源配额充足、网络策略已更新、证书未过期，环境健康检查通过）
- [ ] **PRE-005**: 数据库迁移脚本已评审且可回退（提供 `up` 和 `down` 脚本，无 destructive 操作）
- [ ] **PRE-006**: 配置变更清单已审批（diff 可见、变更影响范围已评估）
- [ ] **PRE-007**: 部署计划文档完整，包含：部署步骤、人员分工、时间窗口、暂停点和回滚触发条件
- [ ] **PRE-008**: 相关方已通知（on-call 工程师、业务 owner、上下游团队），发布窗口已确认
- [ ] **PRE-009**: 灰度/金丝雀策略已定义（灰度比例、验证时长、自动推进/回滚条件）

## 2. 部署执行 (Deploy Execution)

- [ ] **EXE-001**: 部署步骤按自动化流水线执行（手工操作步骤 ≤ 3 步且有 checklist 记录）
- [ ] **EXE-002**: 数据库变更先于应用部署执行，且已验证向后兼容（新旧版本均可正常工作）
- [ ] **EXE-003**: 金丝雀/灰度发布已按计划逐步推进，每阶段验证通过后再继续
- [ ] **EXE-004**: 部署过程中的关键指标（错误率、响应时间、CPU/内存）已实时监控，无异常突增
- [ ] **EXE-005**: 配置变更通过配置中心/环境变量分发，非手动修改生产服务器文件
- [ ] **EXE-006**: 每步部署操作均有日志记录（操作人、时间、命令、输出），可审计追溯
- [ ] **EXE-007**: 部署过程异常时执行预定义的暂停或回退决策，无未经评估的继续推进

## 3. 部署后验证 (Post-Deploy)

- [ ] **POST-001**: 健康检查端点（`/health` 或 `/readyz`）返回 200，且依赖服务状态均正常
- [ ] **POST-002**: 端到端冒烟测试通过（核心业务场景 P0 用例全部通过）
- [ ] **POST-003**: 数据库迁移已确认：数据完整性校验通过（行数/checksum 对比），无丢失或损坏
- [ ] **POST-004**: 静态资源/CDN 缓存已刷新（前端发布场景），用户可获取最新版本
- [ ] **POST-005**: 部署后 15 分钟内错误率 ≤ 基线的 1.2 倍、P95 响应时间 ≤ 基线的 1.3 倍
- [ ] **POST-006**: 监控告警规则已更新（新增/变更的指标有对应告警，不再适用的告警已静默）
- [ ] **POST-007**: 部署报告已生成（部署时间、版本号、变更内容、验证结果、参与者签名）

## 4. 回滚方案 (Rollback)

- [ ] **ROL-001**: 回滚方案在部署前已准备，预计回滚时间 ≤ 15 分钟
- [ ] **ROL-002**: 回滚命令/脚本经过预演验证（在 staging 环境执行过至少 1 次）
- [ ] **ROL-003**: 回滚不依赖新版本中的数据变更（数据库变更可回退，或仅向前兼容）
- [ ] **ROL-004**: 回滚触发条件量化定义（如：错误率上升 ≥ 5%、P95 延迟上升 ≥ 50%、核心功能不可用）
- [ ] **ROL-005**: 回滚后验证流程已定义：确认旧版本正常运行、数据一致、用户无感知

---

## Summary

| 环节 | PASS | PARTIAL | FAIL | 通过率 |
|------|------|---------|------|--------|
| 部署前准备 | __ | __ | __ | __% |
| 部署执行 | __ | __ | __ | __% |
| 部署后验证 | __ | __ | __ | __% |
| 回滚方案 | __ | __ | __ | __% |
| **总计** | **__** | **__** | **__** | **__%** |

### 判定标准

| 通过率 | 结果 |
|--------|------|
| ≥ 90% | PASS - 可发布 |
| 75-89% | CONDITIONAL PASS - 修复 FAIL 项后发布 |
| < 75% | FAIL - 禁止发布，需重新规划部署 |

### 部署结果

- [ ] 部署成功并稳定运行
- [ ] 部署成功但需后续跟进（列在遗留问题中）
- [ ] 触发回滚（回滚编号: ____）
- [ ] 部署终止/取消

### 遗留问题

| # | 环节 | 检查项 | 问题描述 | 跟踪人 | 计划解决日期 |
|---|------|--------|----------|--------|------------|
| 1 | | | | | |
| 2 | | | | | |

---

## References

- [regression-checklist.md](regression-checklist.md)
- [rollback-drill-report.md](rollback-drill-report.md)
- [monitoring-quality-checklist.md](monitoring-quality-checklist.md)
- [standards/harness-engineering.md](../standards/harness-engineering.md)

## 相关评估

- [regression-checklist.md](regression-checklist.md) — 回归检查清单
- [hotfix-quality-checklist.md](hotfix-quality-checklist.md) — 热修复质量清单
- [monitoring-quality-checklist.md](monitoring-quality-checklist.md) — 监控质量清单
- [rollback-drill-report.md](rollback-drill-report.md) — 回滚演练报告
